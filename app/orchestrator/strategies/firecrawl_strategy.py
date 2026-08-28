"""
Self-Hosted Open-Source Firecrawl Strategy Implementation.
Exposes multi-mode crawl, render, and extraction capabilities through the Strategy interface.
"""
import os
from typing import Dict, Any, Optional, List, Tuple
from app.orchestrator.strategies.base import BaseCrawlStrategy
from app.crawlers.firecrawl import FirecrawlCrawler
from app.crawlers.base import CrawlerResponse
from app.crawlers.proxy import ProxyConfig


class FirecrawlStrategy(BaseCrawlStrategy):
    """Self-hosted open-source Firecrawl API & Browser Rendering strategy."""

    def __init__(self, target_config, base_url: Optional[str] = None):
        super().__init__(target_config)
        self.base_url = base_url or os.getenv("FIRECRAWL_BASE_URL", "http://localhost:3008")
        self.crawler = FirecrawlCrawler(self.target_config, base_url=self.base_url)

    @property
    def strategy_name(self) -> str:
        return "FIRECRAWL"

    async def execute(
        self,
        url: str,
        timeout_sec: float = 30.0,
        headers: Optional[Dict[str, str]] = None,
        context: Optional[Dict[str, Any]] = None
    ) -> CrawlerResponse:
        """
        Executes Firecrawl crawling with dynamic mode escalation based on diagnostic context.
        """
        ctx = context or {}
        proxy_config: Optional[ProxyConfig] = ctx.get("proxy_config")
        mode = ctx.get("mode", 2)
        wait_for = ctx.get("wait_for", 1000)
        check_selector = ctx.get("check_selector")

        # Dynamic failure escalation
        last_reason = ctx.get("last_failure_reason")
        if last_reason == "EMPTY_RESPONSE":
            mode = 2  # Force full browser rendering
            wait_for = 1500
        elif last_reason == "JAVASCRIPT_REQUIRED":
            mode = 3  # Browser render with extended wait
            wait_for = 2500
        elif last_reason == "PRODUCT_SCHEMA_NOT_FOUND":
            mode = 3
            wait_for = 2000

        return await self.crawler.fetch(
            url=url,
            timeout_sec=timeout_sec,
            headers=headers,
            proxy_config=proxy_config,
            mode=mode,
            wait_for=wait_for,
            check_selector=check_selector
        )

    async def health_check(self) -> Tuple[bool, str, Dict[str, Any]]:
        """Verifies health of the Firecrawl instance."""
        return await self.crawler.check_health()

    async def map_urls(self, domain_url: str, search: Optional[str] = None, limit: int = 50) -> List[str]:
        """Discovers domain URLs via Firecrawl map endpoint."""
        return await self.crawler.map(url=domain_url, search=search, limit=limit)
