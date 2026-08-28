import asyncio
import time
from typing import Dict, Any, Optional
from app.crawlers.base import BaseCrawler, CrawlerResponse
from app.models.retailer import RetailerTargetConfig


class PlaywrightCrawler(BaseCrawler):
    """Playwright Chromium crawler for dynamic JavaScript rendering and anti-bot mitigation."""

    STEALTH_SCRIPTS = """
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
    window.chrome = { runtime: {} };
    Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5] });
    Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] });
    """

    _is_available: bool = True

    def __init__(self, target_config: RetailerTargetConfig, headless: bool = True):
        super().__init__(target_config)
        self.headless = headless

    async def fetch(
        self,
        url: str,
        timeout_sec: float = 12.0,
        headers: Optional[Dict[str, str]] = None
    ) -> CrawlerResponse:
        if not PlaywrightCrawler._is_available:
            return CrawlerResponse(
                url=url,
                final_url=url,
                status_code=0,
                strategy="PLAYWRIGHT",
                error_message="Playwright Chromium is not available in the current environment."
            )

        try:
            return await asyncio.wait_for(
                self._fetch_internal(url, timeout_sec, headers),
                timeout=timeout_sec + 2.0
            )
        except asyncio.TimeoutError:
            return CrawlerResponse(
                url=url,
                final_url=url,
                status_code=0,
                strategy="PLAYWRIGHT",
                error_message=f"Playwright render timed out after {timeout_sec}s"
            )
        except Exception as e:
            return CrawlerResponse(
                url=url,
                final_url=url,
                status_code=0,
                strategy="PLAYWRIGHT",
                error_message=f"Playwright execution error: {str(e)}"
            )

    async def _fetch_internal(
        self,
        url: str,
        timeout_sec: float = 12.0,
        headers: Optional[Dict[str, str]] = None
    ) -> CrawlerResponse:
        start_time = time.time()
        try:
            from playwright.async_api import async_playwright
        except ImportError:
            PlaywrightCrawler._is_available = False
            return CrawlerResponse(
                url=url,
                final_url=url,
                status_code=0,
                strategy="PLAYWRIGHT",
                error_message="Playwright is not installed in the environment."
            )

        try:
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
            is_brightdata = bool(proxy_url and ("superproxy" in proxy_url or "brightdata" in proxy_url or guard.enabled))

            if is_brightdata:
                allowed, denial_reason = await guard.check_and_acquire(self.target_config.target_id, url)
                if not allowed:
                    return CrawlerResponse(
                        url=url,
                        final_url=url,
                        status_code=0,
                        strategy="PLAYWRIGHT",
                        success=False,
                        is_blocked=True,
                        failure_reason="BRIGHTDATA_SAFETY_CAP_REACHED",
                        error_message=denial_reason
                    )

            proxy = {"server": proxy_url} if proxy_url else None

            async with async_playwright() as p:
                try:
                    browser = await p.chromium.launch(
                        headless=self.headless,
                        proxy=proxy,
                        args=[
                            "--disable-blink-features=AutomationControlled",
                            "--no-sandbox",
                            "--disable-setuid-sandbox",
                            "--disable-infobars",
                            "--window-size=1440,900",
                        ]
                    )
                except Exception as launch_err:
                    PlaywrightCrawler._is_available = False
                    return CrawlerResponse(
                        url=url,
                        final_url=url,
                        status_code=0,
                        strategy="PLAYWRIGHT",
                    )
                context = await browser.new_context(
                    viewport={"width": 1440, "height": 900},
                    user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
                    locale=self.target_config.locale,
                    timezone_id="America/New_York",
                    extra_http_headers=headers or {}
                )
                await context.add_init_script(self.STEALTH_SCRIPTS)

                page = await context.new_page()

                # Block heavy media/fonts if desired to speed up crawl
                await page.route(
                    "**/*.{png,jpg,jpeg,webp,svg,gif,woff,woff2,ttf,otf,mp4,avi}",
                    lambda route: route.abort() if "captcha" not in route.request.url.lower() else route.continue_()
                )

                try:
                    response = await page.goto(url, wait_until="domcontentloaded", timeout=int(timeout_sec * 1000))
                    # Allow JS execution
                    await page.wait_for_timeout(2000)

                    status_code = response.status if response else 200
                    final_url = page.url
                    html = await page.content()
                    bytes_len = len(html.encode("utf-8"))

                    if is_brightdata:
                        guard.record_response(self.target_config.target_id, status_code == 200, bytes_len)

                    # Capture screenshot
                    screenshot_bytes = None
                    try:
                        screenshot_bytes = await page.screenshot(type="png", full_page=False)
                    except Exception:
                        pass

                    elapsed_ms = round((time.time() - start_time) * 1000, 2)
                    lower_html = html.lower()

                    is_captcha = any(sig in lower_html for sig in ["captcha", "robot check", "verify you are human"])
                    is_blocked = status_code in (403, 429) or is_captcha

                    await context.close()
                    await browser.close()

                    return CrawlerResponse(
                        url=url,
                        final_url=final_url,
                        status_code=status_code,
                        html=html,
                        bytes_received=bytes_len,
                        response_time_ms=elapsed_ms,
                        strategy="PLAYWRIGHT",
                        is_blocked=is_blocked,
                        is_captcha=is_captcha,
                        is_js_rendered=True,
                        screenshot_bytes=screenshot_bytes
                    )

                except Exception as page_err:
                    await context.close()
                    await browser.close()
                    elapsed_ms = round((time.time() - start_time) * 1000, 2)
                    return CrawlerResponse(
                        url=url,
                        final_url=url,
                        status_code=0,
                        response_time_ms=elapsed_ms,
                        strategy="PLAYWRIGHT",
                        error_message=f"Playwright navigation error: {str(page_err)}"
                    )

        except Exception as e:
            elapsed_ms = round((time.time() - start_time) * 1000, 2)
            return CrawlerResponse(
                url=url,
                final_url=url,
                status_code=0,
                response_time_ms=elapsed_ms,
                strategy="PLAYWRIGHT",
                error_message=f"Playwright engine failed: {str(e)}"
            )
