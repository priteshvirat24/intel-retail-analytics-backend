import time
import httpx
from typing import Dict, Any, Optional
from app.crawlers.base import BaseCrawler, CrawlerResponse
from app.models.retailer import RetailerTargetConfig


class HttpCrawler(BaseCrawler):
    """Fast, lightweight asynchronous HTTP crawler powered by HTTPX."""

    BOT_CHALLENGE_SIGNALS = [
        "cf-chl-bypass", "cloudflare-static", "challenge-running", "cf-browser-verification",
        "access denied", "attention required! | cloudflare", "please verify you are a human",
        "checking your browser before accessing", "perimeterx", "datadome", "akamai-bm",
        "incapsula_resource", "shield_square", "px-captcha", "awswaf"
    ]

    CAPTCHA_SIGNALS = [
        "g-recaptcha", "h-captcha", "cf-turnstile", "geetest", "arkose",
        "type the characters you see in this image", "enter the characters below",
        "robot check", "solve the puzzle", "captcha-box"
    ]

    def _get_default_headers(self) -> Dict[str, str]:
        return {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": f"{self.target_config.locale},en-US;q=0.9,en;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Sec-Ch-Ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"macOS"',
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
        }

    async def fetch(
        self,
        url: str,
        timeout_sec: float = 8.0,
        headers: Optional[Dict[str, str]] = None
    ) -> CrawlerResponse:
        req_headers = self._get_default_headers()
        if headers:
            req_headers.update(headers)

        start_time = time.time()
        use_http2 = url.startswith("https://")
        
        import os
        from app.crawlers.proxy import ProxyProvider
        from app.crawlers.brightdata_guard import BrightDataCostGuard

        proxy_cfg = ProxyProvider.get_proxy(
            target_country=self.target_config.country,
            target_country_iso=getattr(self.target_config, "iso_country", None)
        )
        proxy_url = proxy_cfg.server if proxy_cfg.enabled else os.environ.get("CRAWL_PROXY_URL")
        if "127.0.0.1" in url or "localhost" in url or (getattr(self.target_config, "target_id", "")).startswith("mock"):
            proxy_url = None

        guard = BrightDataCostGuard.get_instance()
        guard.reload_config()
        is_brightdata = bool(proxy_url and ("superproxy" in proxy_url or "brightdata" in proxy_url or guard.enabled))

        if is_brightdata:
            allowed, denial_reason = await guard.check_and_acquire(self.target_config.target_id, url)
            if not allowed:
                return CrawlerResponse(
                    url=url,
                    final_url=url,
                    status_code=0,
                    strategy="HTTP",
                    success=False,
                    is_blocked=True,
                    failure_reason="BRIGHTDATA_SAFETY_CAP_REACHED",
                    error_message=denial_reason
                )
        
        try:
            async with httpx.AsyncClient(
                timeout=timeout_sec,
                follow_redirects=True,
                http2=use_http2,
                verify=False,
                proxy=proxy_url
            ) as client:
                resp = await client.get(url, headers=req_headers)
                elapsed_ms = round((time.time() - start_time) * 1000, 2)
                html = resp.text or ""
                bytes_len = len(resp.content) if hasattr(resp, "content") else len(html.encode("utf-8"))

                if is_brightdata:
                    guard.record_response(self.target_config.target_id, resp.status_code == 200, bytes_len)

                lower_html = html.lower()
                is_captcha = any(sig in lower_html for sig in self.CAPTCHA_SIGNALS)
                is_blocked = (
                    resp.status_code in (403, 429)
                    or any(sig in lower_html for sig in self.BOT_CHALLENGE_SIGNALS)
                    or is_captcha
                )

                return CrawlerResponse(
                    url=url,
                    final_url=str(resp.url),
                    status_code=resp.status_code,
                    headers=dict(resp.headers),
                    html=html,
                    bytes_received=bytes_len,
                    response_time_ms=elapsed_ms,
                    strategy="HTTP",
                    success=(resp.status_code == 200 and not is_blocked),
                    is_blocked=is_blocked,
                    is_captcha=is_captcha,
                    is_js_rendered=False
                )

        except httpx.TimeoutException as e:
            elapsed_ms = round((time.time() - start_time) * 1000, 2)
            return CrawlerResponse(
                url=url,
                final_url=url,
                status_code=0,
                response_time_ms=elapsed_ms,
                strategy="HTTP",
                success=False,
                error_message=f"HTTP Timeout: {str(e)}"
            )
        except Exception as e:
            elapsed_ms = round((time.time() - start_time) * 1000, 2)
            return CrawlerResponse(
                url=url,
                final_url=url,
                status_code=0,
                response_time_ms=elapsed_ms,
                strategy="HTTP",
                success=False,
                error_message=f"HTTP Connection Error: {str(e)}"
            )
