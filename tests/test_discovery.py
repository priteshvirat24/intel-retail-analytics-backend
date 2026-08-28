import pytest
from app.discovery.deduplicator import ProductDeduplicator
from app.models.retailer import RetailerTargetConfig, DiscoveryConfig
from app.discovery.sitemap import SitemapDiscovery
from app.discovery.category import CategoryDiscovery


def test_product_deduplicator_strips_tracking_params():
    url_with_tracking = (
        "https://www.amazon.com/dp/B09V3HN1KC?"
        "ref_=ast_sto_dp&th=1&psc=1&utm_source=google&utm_medium=cpc&session_id=123"
    )
    cleaned = ProductDeduplicator.clean_url(url_with_tracking)
    assert "utm_source" not in cleaned
    assert "ref_" not in cleaned
    assert "session_id" not in cleaned
    assert "https://www.amazon.com/dp/B09V3HN1KC" in cleaned


def test_product_deduplicator_extracts_product_keys():
    amazon_url = "https://www.amazon.com/Apple-MacBook-15-inch-256GB-Midnight/dp/B0C7678D3M"
    assert ProductDeduplicator.extract_product_key(amazon_url) == "B0C7678D3M"

    walmart_url = "https://www.walmart.com/ip/Apple-MacBook-Air-13-3-inch-Laptop/608274002"
    assert ProductDeduplicator.extract_product_key(walmart_url) == "608274002"

    bestbuy_url = "https://www.bestbuy.com/site/apple-macbook-air-13-laptop/6418601.p"
    assert ProductDeduplicator.extract_product_key(bestbuy_url) == "6418601"


def test_product_deduplicator_deduplicates_duplicate_urls():
    urls = [
        "https://www.amazon.com/dp/B0C7678D3M?tag=affiliate",
        "https://www.amazon.com/product-title/dp/B0C7678D3M",
        "https://www.amazon.com/dp/B09V3HN1KC",
        "https://www.amazon.com/dp/B09V3HN1KC?ref=xyz"
    ]
    deduped = ProductDeduplicator.deduplicate(urls, max_count=10)
    assert len(deduped) == 2
