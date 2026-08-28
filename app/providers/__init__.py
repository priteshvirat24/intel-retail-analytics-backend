"""Scraping Providers Subsystem."""
from app.providers.base import ScrapingProvider, ProviderTargetResult
from app.providers.brightdata_provider import BrightDataProvider
from app.providers.apify_provider import ApifyProvider
from app.providers.factory import get_provider

__all__ = [
    "ScrapingProvider",
    "ProviderTargetResult",
    "BrightDataProvider",
    "ApifyProvider",
    "get_provider",
]
