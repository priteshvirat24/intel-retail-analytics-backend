from typing import Dict, Any, Optional
from bs4 import BeautifulSoup
from app.retailers.base_adapter import BaseRetailerAdapter


class CustomGenericAdapter(BaseRetailerAdapter):
    """Generic fallback adapter that applies configured custom selectors."""

    def extract_custom(self, html: str, url: str, soup: Optional[BeautifulSoup] = None) -> Optional[Dict[str, Any]]:
        # Relies on target custom selectors and standard DOM logic
        return None
