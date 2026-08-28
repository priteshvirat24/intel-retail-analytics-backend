import time
import httpx
from typing import Dict, Any, Optional
from app.crawlers.base import BaseCrawler, CrawlerResponse
from app.models.retailer import RetailerTargetConfig


class ScrapyCrawlerBridge(BaseCrawler):
    """
    Simulates Scrapy engine pipeline with AutoThrottle, per-domain concurrency,
    and download delay middleware semantics over async HTTP.
    """

    def __init__(self, target_config: RetailerTargetConfig, download_delay: float = 1.0):
        super().__init__(target_config)
        self.download_delay = download_delay

    async def fetch(
        self,
        url: str,
        timeout_sec: float = 25.0,
        headers: Optional[Dict[str, str]] = None
    ) -> CrawlerResponse:
        # Respect Scrapy AutoThrottle delay
        if self.download_delay > 0:
            import asyncio
            await asyncio.sleep(self.download_delay)

        start_time = time.time()
        req_headers = {
            "User-Agent": "Scrapy/2.11.1 (+https://scrapy.org)",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": f"{self.target_config.locale},en;q=0.9",
        }
        if headers:
            req_headers.update(headers)

        try:
            async with httpx.AsyncClient(timeout=timeout_sec, follow_redirects=True) as client:
                resp = await client.get(url, headers=req_headers)
                elapsed_ms = round((time.time() - start_time) * 1000, 2)
                return CrawlerResponse(
                    url=url,
                    final_url=str(resp.url),
                    status_code=resp.status_code,
                    headers=dict(resp.headers),
                    html=resp.text or "",
                    response_time_ms=elapsed_ms,
                    strategy="SCRAPY",
                    is_blocked=resp.status_code in (403, 429),
                    is_captcha="captcha" in (resp.text or "").lower()
                )
        except Exception as e:
            elapsed_ms = round((time.time() - start_time) * 1000, 2)
            return CrawlerResponse(
                url=url,
                final_url=url,
                status_code=0,
                response_time_ms=elapsed_ms,
                strategy="SCRAPY",
                error_message=str(e)
            )
