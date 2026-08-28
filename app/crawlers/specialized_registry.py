"""
Specialized Scraper & Scraper Studio (DCA) Registry.
Maintains availability status of specialized Bright Data scrapers across the 52 retailer targets.
Queries active Scraper Studio (DCA) collectors dynamically.
"""
import os
import logging
from typing import Dict, Any, List, Optional
from enum import Enum
import httpx

import app.env

logger = logging.getLogger("crawl.specialized_registry")


class ScraperAvailability(str, Enum):
    SPECIALIZED_SCRAPER_AVAILABLE = "SPECIALIZED_SCRAPER_AVAILABLE"
    SPECIALIZED_SCRAPER_UNAVAILABLE = "SPECIALIZED_SCRAPER_UNAVAILABLE"
    UNKNOWN = "UNKNOWN"


class SpecializedScraperRegistry:
    """Registry tracking pre-built dataset scrapers and active Scraper Studio (DCA) collectors."""

    # Known platform scraper capabilities mapped to retailer domains
    KNOWN_PREBUILT_PLATFORMS: Dict[str, str] = {
        "amazon.com": "amazon_products",
        "amazon.co.uk": "amazon_products",
        "amazon.de": "amazon_products",
        "amazon.fr": "amazon_products",
        "amazon.it": "amazon_products",
        "amazon.es": "amazon_products",
        "amazon.ca": "amazon_products",
        "amazon.in": "amazon_products",
        "amazon.com.mx": "amazon_products",
        "amazon.com.br": "amazon_products",
        "walmart.com": "walmart_products",
        "bestbuy.com": "bestbuy_products",
        "ebay.com": "ebay_products",
        "target.com": "target_products"
    }

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("BRIGHTDATA_API_KEY", "")
        self.dca_collectors: List[Dict[str, Any]] = []
        self._dca_checked = False

    async def refresh_dca_collectors(self) -> List[Dict[str, Any]]:
        """Queries the Bright Data API for active Scraper Studio (DCA) custom collectors."""
        if not self.api_key:
            return []

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                r = await client.get("https://api.brightdata.com/dca/collectors_list", headers=headers)
                if r.status_code == 200:
                    data = r.json()
                    self.dca_collectors = data.get("data", [])
                else:
                    self.dca_collectors = []
        except Exception as e:
            logger.warning(f"Failed to query DCA collectors: {e}")
            self.dca_collectors = []

        self._dca_checked = True
        return self.dca_collectors

    def get_retailer_scraper_status(self, domain: str) -> Tuple_Status:
        """
        Determines the specialized scraper availability for a retailer domain.
        Returns (ScraperAvailability, scraper_name_or_id).
        """
        clean_domain = domain.lower().replace("www.", "").strip()

        # 1. Check for active DCA custom collector
        for col in self.dca_collectors:
            col_target = (col.get("target_domain") or col.get("name") or "").lower()
            if clean_domain in col_target:
                return ScraperAvailability.SPECIALIZED_SCRAPER_AVAILABLE, f"DCA Collector: {col.get('id')}"

        # 2. Check for known pre-built platform scraper
        for plat_domain, plat_name in self.KNOWN_PREBUILT_PLATFORMS.items():
            if plat_domain in clean_domain or clean_domain in plat_domain:
                return ScraperAvailability.SPECIALIZED_SCRAPER_AVAILABLE, f"Prebuilt: {plat_name}"

        return ScraperAvailability.SPECIALIZED_SCRAPER_UNAVAILABLE, "None (Generic Web Unlocker / Browser Required)"


# Tuple alias for clean typing
Tuple_Status = tuple[ScraperAvailability, str]
