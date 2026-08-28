import pytest
import os
import asyncio
from app.crawlers.brightdata_guard import BrightDataCostGuard, BrightDataUsageTelemetry
from app.crawlers.proxy import ProxyProvider, ProxyConfig
from app.models.retailer import RetailerTargetConfig
from app.crawlers.http import HttpCrawler


@pytest.fixture
def mock_target():
    return RetailerTargetConfig(
        target_id="amazon-us-guard-test",
        retailer="amazon",
        brand_name="Amazon",
        base_url="https://www.amazon.com",
        country="United States",
        iso_country="US",
        domain="amazon.com",
        locale="en-US",
        currency="USD",
        timezone="America/New_York",
        discovery_methods=[],
        category_seeds=[],
        sitemap_urls=[],
        seed_urls=[],
        max_concurrency=1,
        rate_limit=1.0
    )


@pytest.mark.asyncio
async def test_brightdata_cost_guard_global_request_cap(monkeypatch):
    monkeypatch.setenv("BRIGHTDATA_MAX_REQUESTS", "2")
    monkeypatch.setenv("BRIGHTDATA_MAX_REQUESTS_PER_TARGET", "5")
    monkeypatch.setenv("BRIGHTDATA_DELAY_BETWEEN_REQUESTS_SEC", "0.0")

    guard = BrightDataCostGuard()
    guard.reload_config()

    # Request 1: Allowed
    allowed1, reason1 = await guard.check_and_acquire("target-1", "https://example.com/1")
    assert allowed1 is True
    assert reason1 is None

    # Request 2: Allowed
    allowed2, reason2 = await guard.check_and_acquire("target-2", "https://example.com/2")
    assert allowed2 is True
    assert reason2 is None

    # Request 3: Blocked by global cap (2 max)
    allowed3, reason3 = await guard.check_and_acquire("target-3", "https://example.com/3")
    assert allowed3 is False
    assert "SAFETY CAP REACHED" in reason3
    assert guard.telemetry.blocked_by_guard == 1


@pytest.mark.asyncio
async def test_brightdata_cost_guard_per_target_cap(monkeypatch):
    monkeypatch.setenv("BRIGHTDATA_MAX_REQUESTS", "10")
    monkeypatch.setenv("BRIGHTDATA_MAX_REQUESTS_PER_TARGET", "1")
    monkeypatch.setenv("BRIGHTDATA_DELAY_BETWEEN_REQUESTS_SEC", "0.0")

    guard = BrightDataCostGuard()
    guard.reload_config()

    # Target A - Call 1: Allowed
    allowed1, reason1 = await guard.check_and_acquire("target-a", "https://example.com/a1")
    assert allowed1 is True

    # Target A - Call 2: Blocked (1 per target cap)
    allowed2, reason2 = await guard.check_and_acquire("target-a", "https://example.com/a2")
    assert allowed2 is False
    assert "TARGET CAP REACHED" in reason2

    # Target B - Call 1: Allowed
    allowed_b, reason_b = await guard.check_and_acquire("target-b", "https://example.com/b1")
    assert allowed_b is True


@pytest.mark.asyncio
async def test_brightdata_cost_guard_bandwidth_cap(monkeypatch):
    monkeypatch.setenv("BRIGHTDATA_MAX_REQUESTS", "10")
    monkeypatch.setenv("BRIGHTDATA_MAX_BANDWIDTH_MB", "1.0") # 1MB limit
    monkeypatch.setenv("BRIGHTDATA_DELAY_BETWEEN_REQUESTS_SEC", "0.0")

    guard = BrightDataCostGuard()
    guard.reload_config()

    # Record 1.5 MB response
    guard.record_response("target-c", True, int(1.5 * 1024 * 1024))

    # Next acquire attempt should be blocked by bandwidth cap
    allowed, reason = await guard.check_and_acquire("target-c", "https://example.com/c1")
    assert allowed is False
    assert "BANDWIDTH CAP REACHED" in reason


def test_proxy_provider_brightdata_credentials(monkeypatch):
    monkeypatch.setenv("BRIGHTDATA_ENABLED", "true")
    monkeypatch.setenv("BRIGHTDATA_CUSTOMER_ID", "test_cust")
    monkeypatch.setenv("BRIGHTDATA_PASSWORD", "secret_pass")
    monkeypatch.setenv("BRIGHTDATA_ZONE", "residential")

    proxy_cfg = ProxyProvider.get_proxy(target_country="Germany", target_country_iso="DE")
    assert proxy_cfg.enabled is True
    assert proxy_cfg.is_residential is True
    assert "brd-customer-test_cust-zone-residential-country-de" in proxy_cfg.server
    assert "secret_pass" in proxy_cfg.server
    
    # Check that sanitized representation does not leak plaintext password
    sanitized = proxy_cfg.get_sanitized_repr()
    assert "secret_pass" not in str(sanitized)
    assert sanitized["proxy_enabled"] is True


@pytest.mark.asyncio
async def test_http_crawler_blocks_when_brightdata_budget_exceeded(monkeypatch, mock_target):
    monkeypatch.setenv("BRIGHTDATA_ENABLED", "true")
    monkeypatch.setenv("BRIGHTDATA_CUSTOMER_ID", "test_cust")
    monkeypatch.setenv("BRIGHTDATA_PASSWORD", "secret_pass")
    monkeypatch.setenv("BRIGHTDATA_MAX_REQUESTS", "0") # 0 budget to test immediate block

    crawler = HttpCrawler(mock_target)
    resp = await crawler.fetch("https://www.amazon.com/dp/B08N5WRW88")
    
    assert resp.success is False
    assert resp.failure_reason == "BRIGHTDATA_SAFETY_CAP_REACHED"
    assert "SAFETY CAP REACHED" in resp.error_message
