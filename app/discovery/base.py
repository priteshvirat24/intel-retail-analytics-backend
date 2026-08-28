from abc import ABC, abstractmethod
from typing import List, Optional
from app.models.retailer import RetailerTargetConfig


class BaseDiscovery(ABC):
    """Abstract interface for product URL discovery strategies."""

    def __init__(self, target_config: RetailerTargetConfig):
        self.target_config = target_config

    @abstractmethod
    async def discover_urls(self, limit: int = 20) -> List[str]:
        """Discover product candidate URLs up to the specified limit."""
        pass
