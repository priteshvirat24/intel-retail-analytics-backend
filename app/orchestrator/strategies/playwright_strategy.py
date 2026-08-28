from typing import Dict, Any, Optional
from app.orchestrator.strategies.base import BaseCrawlStrategy
from app.crawlers.playwright import PlaywrightCrawler
from app.crawlers.base import CrawlerResponse


class PlaywrightStrategy(BaseCrawlStrategy):
    """Playwright Chromium headless/headful browser rendering strategy."""

    def __init__(self, target_config, headless: bool = True):
        super().__init__(target_config)
        self.headless = headless

    @property
    def strategy_name(self) -> str:
        return "PLAYWRIGHT"

    async def execute(
        self,
        url: str,
        timeout_sec: float = 30.0,
        headers: Optional[Dict[str, str]] = None,
        context: Optional[Dict[str, Any]] = None
    ) -> CrawlerResponse:
        crawler = PlaywrightCrawler(self.target_config, headless=self.headless)
        return await crawler.fetch(url, timeout_sec=timeout_sec, headers=headers)
