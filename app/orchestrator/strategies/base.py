from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from app.crawlers.base import CrawlerResponse
from app.models.retailer import RetailerTargetConfig


class BaseCrawlStrategy(ABC):
    """Abstract base class for modular crawl & extraction strategies."""

    def __init__(self, target_config: RetailerTargetConfig):
        self.target_config = target_config

    @property
    @abstractmethod
    def strategy_name(self) -> str:
        """Name identifier of the strategy (e.g. HTTP, PLAYWRIGHT, FIRECRAWL, ADAPTER)."""
        pass

    @abstractmethod
    async def execute(
        self,
        url: str,
        timeout_sec: float = 30.0,
        headers: Optional[Dict[str, str]] = None,
        context: Optional[Dict[str, Any]] = None
    ) -> CrawlerResponse:
        """Executes the crawl or extraction step and returns a normalized CrawlerResponse."""
        pass
