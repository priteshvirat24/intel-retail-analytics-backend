"""
Self-Hosted Open-Source Firecrawl Crawler Client.
Connects directly to the self-hosted Firecrawl API / Playwright service stack.
AGPL-3.0 License Attribution: https://github.com/firecrawl/firecrawl
"""
import os
import time
import base64
import json
import httpx
from typing import Dict, Any, Optional, List, Tuple
from app.crawlers.base import BaseCrawler, CrawlerResponse
from app.crawlers.proxy import ProxyConfig
from app.models.retailer import RetailerTargetConfig


class FirecrawlCrawler(BaseCrawler):
    """
    Client for interacting with a self-hosted Firecrawl deployment.
    Supports scrape, browser render, explicit wait, map discovery, and asynchronous crawl.
    """

    def __init__(
        self,
        target_config: RetailerTargetConfig,
        base_url: Optional[str] = None,
        api_key: Optional[str] = None
    ):
        super().__init__(target_config)
        self.base_url = (
            base_url
            or os.getenv("FIRECRAWL_BASE_URL")
            or "http://localhost:3008"
        ).rstrip("/")
        self.api_key = api_key or os.getenv("FIRECRAWL_API_KEY", "")
        self.default_timeout = float(os.getenv("FIRECRAWL_TIMEOUT", "30.0"))
        self.default_wait_for = int(os.getenv("FIRECRAWL_WAIT_FOR", "1000"))
        self.enable_screenshot = os.getenv("FIRECRAWL_SCREENSHOT", "false").lower() in ("true", "1", "yes")

    def _get_headers(self, custom_headers: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "MultiSiteCrawlOrchestrator/2.0 (Self-Hosted Firecrawl Client)"
        }
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        if custom_headers:
            headers.update(custom_headers)
        return headers

    async def check_health(self) -> Tuple[bool, str, Dict[str, Any]]:
        """
        Verifies if the self-hosted Firecrawl service is running and reachable.
        Returns: (is_available, status_string, details)
        """
        endpoints_to_try = [
            f"{self.base_url}/health",
            f"{self.base_url}/e2e-test",
            f"{self.base_url}/",
            f"{self.base_url}/v1/health",
        ]
        start_t = time.perf_counter()
        async with httpx.AsyncClient(timeout=5.0) as client:
            for ep in endpoints_to_try:
                try:
                    resp = await client.get(ep, headers=self._get_headers())
                    latency_ms = (time.perf_counter() - start_t) * 1000
                    if resp.status_code in (200, 204):
                        details = {
                            "status_code": resp.status_code,
                            "latency_ms": latency_ms,
                            "endpoint": ep,
                            "base_url": self.base_url
                        }
                        try:
                            data = resp.json()
                            if isinstance(data, dict):
                                details.update(data)
                        except Exception:
                            details["raw_text"] = resp.text[:100]

                        return True, "AVAILABLE", details
                except httpx.ConnectError:
                    continue
                except httpx.TimeoutException:
                    continue
                except Exception:
                    continue

        latency_ms = (time.perf_counter() - start_t) * 1000
        return False, "UNAVAILABLE", {
            "error": "Connection refused or unreachable",
            "base_url": self.base_url,
            "latency_ms": latency_ms
        }

    async def fetch(
        self,
        url: str,
        timeout_sec: Optional[float] = None,
        headers: Optional[Dict[str, str]] = None,
        proxy_config: Optional[ProxyConfig] = None,
        mode: int = 2,
        wait_for: Optional[int] = None,
        check_selector: Optional[str] = None
    ) -> CrawlerResponse:
        """
        Scrapes a single URL using Firecrawl with specified execution mode.
        Modes:
            Mode 1: Basic Scrape (fast HTTP / non-wait)
            Mode 2: Browser-Rendered Scrape (Playwright headless)
            Mode 3: Browser-Rendered with Explicit Wait
            Mode 4: Scrape with Interaction/Selector Check
        """
        timeout = timeout_sec or self.default_timeout
        wait_ms = wait_for if wait_for is not None else (self.default_wait_for if mode >= 2 else 0)
        
        start_time = time.perf_counter()
        async with httpx.AsyncClient(timeout=timeout + 5.0) as client:
            try:
                formats = ["html", "markdown"]
                if self.enable_screenshot:
                    formats.append("screenshot")

                base_candidates = [self.base_url]
                if "api.firecrawl.dev" in self.base_url and "http://localhost:3008" not in base_candidates:
                    base_candidates.append("http://localhost:3008")
                elif "localhost" in self.base_url and self.api_key and "https://api.firecrawl.dev" not in base_candidates:
                    base_candidates.insert(0, "https://api.firecrawl.dev")

                endpoints = []
                for base in base_candidates:
                    if "api.firecrawl.dev" in base:
                        cloud_payload = {
                            "url": url,
                            "formats": formats,
                            "onlyMainContent": False,
                            "waitFor": wait_ms,
                            "timeout": int(timeout * 1000)
                        }
                        if headers:
                            cloud_payload["headers"] = headers
                        endpoints.append((f"{base}/v1/scrape", cloud_payload))
                    else:
                        local_scrape_payload = {
                            "url": url,
                            "timeout": int(timeout * 1000),
                            "wait_after_load": wait_ms,
                            "check_selector": check_selector
                        }
                        if headers:
                            local_scrape_payload["headers"] = headers
                        endpoints.append((f"{base}/scrape", local_scrape_payload))

                        local_v1_payload = {
                            "url": url,
                            "formats": formats,
                            "onlyMainContent": False,
                            "waitFor": wait_ms,
                            "timeout": int(timeout * 1000)
                        }
                        if headers:
                            local_v1_payload["headers"] = headers
                        endpoints.append((f"{base}/v1/scrape", local_v1_payload))

                last_resp = None
                data_json = None
                for ep, payload in endpoints:
                    try:
                        resp = await client.post(ep, json=payload, headers=self._get_headers(headers))
                        last_resp = resp
                        if resp.status_code == 200:
                            data_json = resp.json()
                            break
                        elif resp.status_code in (404, 402, 502, 503):
                            # Try next candidate (e.g. cloud -> local fallback)
                            continue
                        else:
                            break
                    except httpx.HTTPError:
                        continue

                latency_ms = (time.perf_counter() - start_time) * 1000

                if last_resp and last_resp.status_code == 200 and data_json is not None:
                    html_content = ""
                    markdown_content = ""
                    status_code = 200
                    metadata = {}
                    screenshot_bytes = None

                    if "content" in data_json:
                        # Direct Firecrawl Playwright service response
                        html_content = data_json.get("content") or ""
                        status_code = data_json.get("pageStatusCode") or 200
                        metadata = {
                            "contentType": data_json.get("contentType"),
                            "statusCode": status_code,
                            "headers": data_json.get("headers") or {}
                        }
                    else:
                        # Firecrawl API v1 response
                        data = data_json.get("data", {})
                        if not data and "markdown" in data_json:
                            data = data_json
                        html_content = data.get("html") or data.get("rawHtml") or ""
                        markdown_content = data.get("markdown") or ""
                        metadata = data.get("metadata") or {}
                        status_code = metadata.get("statusCode") or 200

                        raw_screenshot = data.get("screenshot")
                        if raw_screenshot and isinstance(raw_screenshot, str):
                            try:
                                if "," in raw_screenshot:
                                    raw_screenshot = raw_screenshot.split(",", 1)[1]
                                screenshot_bytes = base64.b64decode(raw_screenshot)
                            except Exception:
                                pass

                    final_url = metadata.get("sourceURL") or metadata.get("url") or url

                    # If markdown wasn't generated by v1 API, generate clean markdown from HTML
                    if not markdown_content and html_content:
                        try:
                            from bs4 import BeautifulSoup
                            soup = BeautifulSoup(html_content, "html.parser")
                            for tag in soup(["script", "style", "svg", "noscript"]):
                                tag.decompose()
                            markdown_content = soup.get_text(separator="\n", strip=True)
                        except Exception:
                            markdown_content = ""

                    # Detect bot/captcha from html and markdown
                    combined_text = (html_content + " " + markdown_content).lower()
                    is_captcha = any(k in combined_text for k in ["captcha", "robot check", "verify you are human", "cf-turnstile"])
                    is_blocked = any(k in combined_text for k in ["access denied", "blocked", "forbidden", "cloudflare", "datadome"])

                    bytes_count = len(html_content.encode("utf-8")) + len(markdown_content.encode("utf-8"))

                    return CrawlerResponse(
                        url=url,
                        final_url=final_url,
                        status_code=status_code,
                        headers=dict(last_resp.headers),
                        html=html_content,
                        markdown=markdown_content,
                        metadata=metadata,
                        response_time_ms=latency_ms,
                        bytes_received=bytes_count,
                        screenshot_bytes=screenshot_bytes,
                        strategy="FIRECRAWL",
                        success=True,
                        is_blocked=is_blocked,
                        is_captcha=is_captcha,
                        is_js_rendered=True
                    )

                else:
                    # Non-200 response from Firecrawl API
                    resp_status = last_resp.status_code if last_resp else 500
                    err_text = last_resp.text[:500] if last_resp else "No response from Firecrawl endpoints"
                    provider_reason = None
                    if last_resp:
                        try:
                            err_json = last_resp.json()
                            provider_reason = err_json.get("error") or err_json.get("message")
                        except Exception:
                            provider_reason = err_text
                    else:
                        provider_reason = err_text

                    return CrawlerResponse(
                        url=url,
                        final_url=url,
                        status_code=resp_status,
                        response_time_ms=latency_ms,
                        strategy="FIRECRAWL",
                        success=False,
                        error_message=f"Firecrawl API returned HTTP {resp_status}: {provider_reason}",
                        failure_reason="FIRECRAWL_ERROR",
                        provider_failure_reason=provider_reason
                    )

            except httpx.ConnectError as e:
                latency_ms = (time.perf_counter() - start_time) * 1000
                return CrawlerResponse(
                    url=url,
                    final_url=url,
                    status_code=0,
                    response_time_ms=latency_ms,
                    strategy="FIRECRAWL",
                    success=False,
                    error_message=f"Cannot connect to self-hosted Firecrawl at {self.base_url}: {e}",
                    failure_reason="FIRECRAWL_SERVICE_UNAVAILABLE",
                    provider_failure_reason="ECONNREFUSED"
                )
            except httpx.TimeoutException as e:
                latency_ms = (time.perf_counter() - start_time) * 1000
                return CrawlerResponse(
                    url=url,
                    final_url=url,
                    status_code=0,
                    response_time_ms=latency_ms,
                    strategy="FIRECRAWL",
                    success=False,
                    error_message=f"Firecrawl request timed out after {timeout}s: {e}",
                    failure_reason="FIRECRAWL_TIMEOUT",
                    provider_failure_reason="TIMEOUT"
                )
            except Exception as e:
                latency_ms = (time.perf_counter() - start_time) * 1000
                return CrawlerResponse(
                    url=url,
                    final_url=url,
                    status_code=0,
                    response_time_ms=latency_ms,
                    strategy="FIRECRAWL",
                    success=False,
                    error_message=f"Firecrawl exception: {str(e)}",
                    failure_reason="FIRECRAWL_INTERNAL_ERROR",
                    provider_failure_reason=str(e)
                )

    async def scrape(
        self,
        url: str,
        formats: Optional[List[str]] = None,
        only_main_content: bool = False,
        wait_for: Optional[int] = None,
        timeout_sec: Optional[float] = None,
        headers: Optional[Dict[str, str]] = None
    ) -> CrawlerResponse:
        """Executes explicit scrape with format specification."""
        return await self.fetch(
            url=url,
            timeout_sec=timeout_sec,
            headers=headers,
            mode=2,
            wait_for=wait_for
        )

    async def render(
        self,
        url: str,
        wait_for: int = 2000,
        check_selector: Optional[str] = None,
        timeout_sec: Optional[float] = None,
        headers: Optional[Dict[str, str]] = None
    ) -> CrawlerResponse:
        """Executes browser render with explicit selector and wait thresholds."""
        return await self.fetch(
            url=url,
            timeout_sec=timeout_sec,
            headers=headers,
            mode=3,
            wait_for=wait_for,
            check_selector=check_selector
        )

    async def map(
        self,
        url: str,
        search: Optional[str] = None,
        limit: int = 50,
        timeout_sec: float = 30.0,
        headers: Optional[Dict[str, str]] = None
    ) -> List[str]:
        """
        Discovers URLs for a given domain using Firecrawl /v1/map endpoint.
        Returns list of discovered URLs.
        """
        map_url = f"{self.base_url}/v1/map"
        payload: Dict[str, Any] = {
            "url": url,
            "limit": limit
        }
        if search:
            payload["search"] = search

        async with httpx.AsyncClient(timeout=timeout_sec) as client:
            try:
                resp = await client.post(map_url, json=payload, headers=self._get_headers(headers))
                if resp.status_code == 200:
                    data = resp.json()
                    links = data.get("links") or data.get("data", {}).get("links") or []
                    return [l for l in links if isinstance(l, str)]
                return []
            except Exception:
                return []

    async def crawl(
        self,
        url: str,
        limit: int = 20,
        max_depth: int = 2,
        timeout_sec: float = 60.0,
        headers: Optional[Dict[str, str]] = None
    ) -> Dict[str, Any]:
        """
        Initiates an asynchronous multi-page crawl using Firecrawl /v1/crawl.
        Returns crawl status dict with job ID or crawl results.
        """
        crawl_url = f"{self.base_url}/v1/crawl"
        payload = {
            "url": url,
            "limit": limit,
            "maxDepth": max_depth
        }
        async with httpx.AsyncClient(timeout=timeout_sec) as client:
            try:
                resp = await client.post(crawl_url, json=payload, headers=self._get_headers(headers))
                if resp.status_code == 200:
                    return resp.json()
                return {"success": False, "status_code": resp.status_code, "error": resp.text[:200]}
            except Exception as e:
                return {"success": False, "error": str(e)}

    async def extract(
        self,
        url: str,
        schema: Optional[Dict[str, Any]] = None,
        prompt: Optional[str] = None,
        timeout_sec: float = 30.0,
        headers: Optional[Dict[str, str]] = None
    ) -> Dict[str, Any]:
        """
        Executes structured schema extraction if supported by the running Firecrawl endpoint.
        """
        extract_url = f"{self.base_url}/v1/scrape"
        payload: Dict[str, Any] = {
            "url": url,
            "formats": ["extract"],
            "extract": {
                "schema": schema or {},
                "prompt": prompt or "Extract product title, price, currency, availability, and SKU."
            }
        }
        async with httpx.AsyncClient(timeout=timeout_sec) as client:
            try:
                resp = await client.post(extract_url, json=payload, headers=self._get_headers(headers))
                if resp.status_code == 200:
                    data = resp.json()
                    return data.get("data", {}).get("extract") or data.get("extract") or {}
                return {}
            except Exception:
                return {}
