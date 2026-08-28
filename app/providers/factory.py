"""
Provider Factory for selecting scraping providers dynamically.
Supports PROVIDER=apify or PROVIDER=brightdata.
"""
import os
from typing import Optional
from app.providers.base import ScrapingProvider
from app.providers.brightdata_provider import BrightDataProvider
from app.providers.apify_provider import ApifyProvider


def get_provider(name: Optional[str] = None) -> ScrapingProvider:
    """Returns the requested ScrapingProvider instance based on name or PROVIDER env var."""
    provider_name = (name or os.getenv("PROVIDER") or "apify").lower().strip()
    
    if provider_name in ("apify", "apify_provider"):
        return ApifyProvider()
    elif provider_name in ("brightdata", "bright_data", "brd"):
        return BrightDataProvider()
    else:
        raise ValueError(
            f"Unknown scraping provider: '{provider_name}'. "
            f"Available providers: 'apify', 'brightdata'."
        )
