from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from bs4 import BeautifulSoup
from app.models.retailer import RetailerTargetConfig


class BaseTargetAdapter(ABC):
    """Abstract base class for custom retailer site adapters."""

    def __init__(self, target_config: RetailerTargetConfig):
        self.target_config = target_config

    @abstractmethod
    def extract_custom(self, html: str, url: str, soup: Optional[BeautifulSoup] = None) -> Optional[Dict[str, Any]]:
        """Extracts normalized product attributes from actual page DOM, JSON-LD, or state."""
        pass
