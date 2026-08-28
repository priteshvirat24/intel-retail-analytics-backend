"""
Automated Test Suite for 52-Target Laptop Crawlability Benchmark Engine.
"""
import pytest
from app.crawlers.base import CrawlerResponse
from app.evaluation.laptop_detector import LaptopDetector, LaptopCrawlEvaluation
from app.discovery.laptop_discovery import LaptopDiscoveryEngine
from app.models.registry import CanonicalTarget, SeedSku, CategorySeed


def test_laptop_detector_valid_laptop_page():
    html = """
    <!DOCTYPE html>
    <html>
      <head><title>Apple MacBook Pro 16-inch M3 Max - Space Black</title></head>
      <body>
        <main>
          <h1>Apple MacBook Pro 16-inch M3 Max (36GB RAM, 1TB SSD)</h1>
          <div class="product-specs">
            <p>16.2-inch Liquid Retina XDR display, Apple M3 Max chip with 14-core CPU and 30-core GPU.</p>
          </div>
        </main>
        <script type="application/ld+json">
          {"@context": "https://schema.org", "@type": "Product", "name": "Apple MacBook Pro 16"}
        </script>
      </body>
    </html>
    """
    resp = CrawlerResponse(
        url="https://example.com/product/macbook-pro-16",
        final_url="https://example.com/product/macbook-pro-16",
        status_code=200,
        html=html,
        bytes_received=len(html),
        response_time_ms=850.0,
        strategy="FIRECRAWL",
        success=True
    )
    ev = LaptopDetector.evaluate(resp, resp.url)
    assert ev.endpoint_reachable is True
    assert ev.product_page_detected is True
    assert ev.product_content_detected is True
    assert ev.crawlable is True
    assert "macbook" in ev.detected_laptop_keywords or "laptop" in ev.detected_laptop_keywords or "m3" in ev.detected_laptop_keywords
    assert ev.failure_reason is None


def test_laptop_detector_rejects_captcha_even_with_200():
    captcha_html = """
    <!DOCTYPE html>
    <html>
      <head><title>Amazon.com: Robot Check</title></head>
      <body>
        <div class="a-box">
          <h4>Enter the characters you see below</h4>
          <p>Sorry, we just need to make sure you're not a robot.</p>
        </div>
      </body>
    </html>
    """
    resp = CrawlerResponse(
        url="https://www.amazon.com/dp/B08N5WRW88",
        final_url="https://www.amazon.com/errors/validateCaptcha",
        status_code=200,
        html=captcha_html,
        bytes_received=len(captcha_html),
        response_time_ms=450.0,
        strategy="HTTP",
        success=True
    )
    ev = LaptopDetector.evaluate(resp, resp.url)
    assert ev.endpoint_reachable is True
    assert ev.product_page_detected is False
    assert ev.crawlable is False
    assert ev.failure_reason in ("CAPTCHA_PAGE", "AMAZON_ROBOT_CHECK_CHALLENGE", "BOT_CHALLENGE_PAGE")


def test_laptop_detector_rejects_cloudflare_challenge():
    cf_html = """
    <!DOCTYPE html>
    <html>
      <head><title>Just a moment...</title></head>
      <body>
        <div class="cf-turnstile">Please verify you are human</div>
      </body>
    </html>
    """
    resp = CrawlerResponse(
        url="https://example.com/laptop",
        final_url="https://example.com/laptop",
        status_code=403,
        headers={"cf-ray": "8a7c29e1234"},
        html=cf_html,
        bytes_received=len(cf_html),
        response_time_ms=320.0,
        strategy="HTTP",
        success=False
    )
    ev = LaptopDetector.evaluate(resp, resp.url)
    assert ev.endpoint_reachable is True
    assert ev.crawlable is False
    assert "CLOUDFLARE" in (ev.failure_reason or "") or ev.failure_reason in ("CAPTCHA_PAGE", "BOT_CHALLENGE_PAGE", "HTTP_403_FORBIDDEN")


def test_laptop_detector_rejects_empty_spa_shell():
    spa_html = """
    <!DOCTYPE html>
    <html>
      <head><title>Loading...</title></head>
      <body>
        <div id="root"></div>
        <script src="/bundle.js"></script>
      </body>
    </html>
    """
    resp = CrawlerResponse(
        url="https://example.com/laptop",
        final_url="https://example.com/laptop",
        status_code=200,
        html=spa_html,
        bytes_received=len(spa_html),
        response_time_ms=210.0,
        strategy="HTTP",
        success=True
    )
    ev = LaptopDetector.evaluate(resp, resp.url)
    assert ev.endpoint_reachable is True
    assert ev.crawlable is False
    assert ev.failure_reason in ("SPA_SHELL_ONLY", "EMPTY_RESPONSE", "PRODUCT_PAGE_NOT_PRESENT")


@pytest.mark.asyncio
async def test_laptop_discovery_engine_finds_seed():
    target = CanonicalTarget(
        target_id="test-target",
        retailer="test",
        country="US",
        iso_country="US",
        domain="example.com",
        locale="en-US",
        currency="USD",
        timezone="America/New_York",
        discovery_methods=["seed"],
        category_seeds=[],
        sitemap_urls=[],
        max_concurrency=2,
        rate_limit=1.0,
        enabled=True,
        seed_urls=[
            SeedSku(url="https://example.com/product/dell-xps-15-laptop", category="Laptops & Notebooks", sku_id="sku_01")
        ]
    )
    url, method, status, failure = await LaptopDiscoveryEngine.discover_laptop_url(target)
    assert status == "SUCCESS"
    assert "dell-xps-15-laptop" in url
    assert method == "configured_seed"
