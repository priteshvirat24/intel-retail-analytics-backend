from typing import Dict, Any, Optional
from app.orchestrator.strategies.base import BaseCrawlStrategy
from app.crawlers.http import HttpCrawler
from app.crawlers.base import CrawlerResponse


class HttpStrategy(BaseCrawlStrategy):
    """HTTP-first lightweight fetching strategy."""

    @property
    def strategy_name(self) -> str:
        return "HTTP"

    async def execute(
        self,
        url: str,
        timeout_sec: float = 30.0,
        headers: Optional[Dict[str, str]] = None,
        context: Optional[Dict[str, Any]] = None
    ) -> CrawlerResponse:
        crawler = HttpCrawler(self.target_config)
        return await crawler.fetch(url, timeout_sec=timeout_sec, headers=headers)
