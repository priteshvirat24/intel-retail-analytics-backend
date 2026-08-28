"""
Comprehensive Automated Test Suite for Fair Strategy Matrix & Forensic Benchmark Engine.
"""
import pytest
from app.crawlers.proxy import ProxyProvider, ProxyConfig, StrategyRequestContext
from app.extraction.template import ProductTemplateIdentifier, TemplateProfile
from app.extraction.validators import ExtractionValidator
from app.models.product import FieldState, FieldValidation
from app.models.retailer import RetailerTargetConfig
from app.models.failure import FailureDiagnosis, FailureCategory, SpecificReason
from app.evaluation.failures import FailureClassifier
from app.orchestrator.strategies.controller import StrategyController
from app.discovery import ProductDiscoveryEngine


def test_proxy_provider_default_direct():
    proxy = ProxyProvider.get_proxy()
    assert isinstance(proxy, ProxyConfig)
    sanitized = proxy.get_sanitized_repr()
    assert "proxy_enabled" in sanitized
    assert "proxy_endpoint_id" in sanitized


def test_strategy_request_context_creation():
    ctx = StrategyRequestContext(
        url="https://www.example.com/p/123",
        target_id="test-target",
        retailer="test-retailer",
        country="US",
        sku_id="sku_001",
        category="Electronics",
        strategy="FIRECRAWL"
    )
    assert ctx.strategy == "FIRECRAWL"
    assert ctx.sku_id == "sku_001"
    assert ctx.category == "Electronics"


def test_template_profile_analysis():
    html_nextjs = """
    <!DOCTYPE html>
    <html>
      <head><title>Product Page</title></head>
      <body>
        <div id="product-detail-container" class="pdp-container">
          <h1>Smartphone 128GB</h1>
        </div>
        <script id="__NEXT_DATA__" type="application/json">{"props": {"pageProps": {}}}</script>
      </body>
    </html>
    """
    profile = ProductTemplateIdentifier.analyze_template(html_nextjs)
    assert isinstance(profile, TemplateProfile)
    assert "tmpl_nextjs" in profile.template_id
    assert profile.framework_detected == "nextjs"
    assert "EMBEDDED_NEXT_DATA" in profile.extraction_sources


def test_field_level_validation_5_states():
    # Valid product payload
    valid_data = {
        "title": "Apple iPhone 15 Pro Max 256GB Titanium",
        "price": 1199.0,
        "currency": "USD",
        "availability": "InStock",
        "sku": "IPHONE15PM256",
        "brand": "Apple"
    }
    val = ExtractionValidator.validate_fields(valid_data, expected_currency="USD")
    assert val.is_valid_sku is True
    assert val.field_states["title"] == FieldState.FIELD_PRESENT_VALID
    assert val.field_states["price"] == FieldState.FIELD_PRESENT_VALID
    assert val.field_states["currency"] == FieldState.FIELD_PRESENT_VALID
    assert val.field_states["gtin"] == FieldState.FIELD_NOT_PRESENT

    # Invalid title due to bot phrase
    bot_data = {
        "title": "Robot Check - Please enter CAPTCHA",
        "price": 10.0,
        "currency": "USD",
        "availability": "InStock",
        "sku": "BOT123"
    }
    bot_val = ExtractionValidator.validate_fields(bot_data, expected_currency="USD")
    assert bot_val.is_valid_sku is False
    assert bot_val.field_states["title"] == FieldState.FIELD_INVALID


def test_anti_bot_vendor_detection():
    cf_html = "<html><head><title>Just a moment...</title></head><body><div class='cf-turnstile'></div></body></html>"
    vendor_cf = FailureClassifier.detect_anti_bot_vendor(cf_html, {"cf-ray": "12345"}, 403)
    assert vendor_cf == "Cloudflare Turnstile"

    akamai_html = "<html><head><title>Access Denied</title></head><body>Reference #18.123</body></html>"
    vendor_ak = FailureClassifier.detect_anti_bot_vendor(akamai_html, {}, 403)
    assert vendor_ak == "Akamai Bot Manager"


def test_strategy_controller_best_attribution():
    attempts = [
        {"strategy": "HTTP", "status_code": 403, "latency_ms": 120.0, "success": False, "validated_success": False},
        {"strategy": "PLAYWRIGHT", "status_code": 200, "latency_ms": 4500.0, "success": True, "validated_success": True},
        {"strategy": "FIRECRAWL", "status_code": 200, "latency_ms": 2300.0, "success": True, "validated_success": True},
    ]
    first_strat, best_strat = StrategyController.determine_best_strategy(attempts)
    assert first_strat == "PLAYWRIGHT"
    assert best_strat == "FIRECRAWL"  # Firecrawl had lower latency (2300ms < 4500ms)


def test_category_diversity_interleaving():
    dummy_cfg = RetailerTargetConfig(
        target_id="test-cat-target",
        retailer="test",
        brand_name="Test",
        base_url="https://example.com",
        country="US",
        domain="example.com",
        locale="en-US",
        currency="USD"
    )
    engine = ProductDiscoveryEngine(dummy_cfg)
    raw_candidates = [
        {"url": "https://example.com/p1", "category": "Phones"},
        {"url": "https://example.com/p2", "category": "Phones"},
        {"url": "https://example.com/l1", "category": "Laptops"},
        {"url": "https://example.com/t1", "category": "Tablets"},
    ]
    balanced = engine._balance_category_diversity(raw_candidates, limit=3)
    cats = [b["category"] for b in balanced]
    assert len(set(cats)) == 3  # All 3 categories represented in first 3 picks
