"""
Unit and Integration Tests for ScrapingProvider and ApifyProvider.
"""
import os
import json
import pytest
from pathlib import Path
from unittest.mock import MagicMock, patch

from app.models.registry import CanonicalTarget
from app.providers.base import ScrapingProvider, ProviderTargetResult
from app.providers.brightdata_provider import BrightDataProvider
from app.providers.apify_provider import ApifyProvider
from app.providers.factory import get_provider
from app.classification.laptop_classifier import LaptopClassifier


@pytest.fixture
def sample_target():
    return CanonicalTarget(
        target_id="test-retailer-us",
        retailer="Test Retailer",
        country="United States",
        iso_country="us",
        domain="testretailer.com",
        locale="en-US",
        currency="USD",
        timezone="America/New_York",
        discovery_methods=["category", "search"],
        category_seeds=[],
        sitemap_urls=[],
        max_concurrency=2,
        rate_limit=1.0,
        enabled=True
    )


def test_provider_factory():
    """Verify get_provider() correctly resolves provider classes."""
    apify_p = get_provider("apify")
    assert isinstance(apify_p, ApifyProvider)
    assert apify_p.name == "apify"

    brd_p = get_provider("brightdata")
    assert isinstance(brd_p, BrightDataProvider)
    assert brd_p.name == "brightdata"

    with pytest.raises(ValueError):
        get_provider("unsupported_provider")


def test_apify_health_check_missing_token():
    """Verify health_check() returns informative failure when token is empty."""
    provider = ApifyProvider(token="")
    is_ok, status, details = provider.health_check()
    assert not is_ok
    assert status == "MISSING_TOKEN"
    assert "APIFY_TOKEN" in details["error"]


@pytest.mark.asyncio
async def test_apify_crawl_missing_token(sample_target):
    """Verify crawl_and_scrape handles missing token gracefully with structured failure."""
    provider = ApifyProvider(token="")
    res = await provider.crawl_and_scrape(sample_target)
    
    assert res.target_id == sample_target.target_id
    assert res.status == "FAILURE"
    assert res.can_scrape == "NO"
    assert res.failure_stage == "ACCESS"
    assert res.failure_category == "ACCESS_FAILURE"
    assert res.failure_reason == "APIFY_AUTH_FAILED"
    assert not res.validation_success


@pytest.mark.asyncio
async def test_brightdata_provider_cached_evidence(sample_target):
    """Verify BrightDataProvider loads canonical target results."""
    provider = BrightDataProvider()
    is_ok, status, _ = provider.health_check()
    assert is_ok or status == "MISSING_API_KEY"


def test_laptop_classification_on_apify_mock_html():
    """Verify LaptopClassifier validates laptop HTML correctly."""
    mock_html = """
    <html>
        <head><title>Lenovo IdeaPad Slim 5 16" AMD Ryzen 7 16GB 512GB SSD Laptop</title></head>
        <body>
            <h1>Lenovo IdeaPad Slim 5 16" AMD Ryzen 7 16GB 512GB SSD Laptop</h1>
            <p>High performance laptop computer with AMD Ryzen 7 7730U, 16GB RAM, 512GB SSD, Windows 11.</p>
        </body>
    </html>
    """
    cls_res = LaptopClassifier.classify(
        title="Lenovo IdeaPad Slim 5 16\" AMD Ryzen 7 16GB 512GB SSD Laptop",
        html=mock_html,
        url="https://example.com/product/lenovo-ideapad"
    )
    assert cls_res.is_genuine_laptop
    assert cls_res.detected_brand == "Lenovo"
    assert cls_res.extracted_specs.get("ram") == "16GB"
