from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from bs4 import BeautifulSoup
from app.models.retailer import RetailerTargetConfig


class BaseExtractor(ABC):
    """Abstract interface for product data extractors."""

    def __init__(self, target_config: Optional[RetailerTargetConfig] = None):
        self.target_config = target_config

    @abstractmethod
    def extract(self, html: str, url: str, soup: Optional[BeautifulSoup] = None) -> Optional[Dict[str, Any]]:
        """Extract structured product fields from HTML and URL."""
        pass
