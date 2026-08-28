import pytest
from app.crawlers.firecrawl import FirecrawlCrawler
from app.crawlers.base import CrawlerResponse
from app.evaluation.failures import FailureClassifier
from app.models.failure import FailureCategory, SpecificReason, CrawlStage
from app.models.retailer import RetailerTargetConfig
from app.orchestrator.strategies.controller import StrategyController
from app.orchestrator.manifest import ManifestManager


@pytest.fixture
def mock_target_config():
    return RetailerTargetConfig(
        target_id="amazon-de",
        retailer="amazon",
        brand_name="Amazon",
        base_url="https://www.amazon.de",
        country="Germany",
        iso_country="DE",
        domain="amazon.de",
        locale="de-DE",
        currency="EUR",
        timezone="Europe/Berlin",
        discovery_methods=[],
        category_seeds=[],
        sitemap_urls=[],
        seed_urls=[],
        max_concurrency=2,
        rate_limit=1.0
    )


def test_firecrawl_health_unavailable(mock_target_config):
    # Connects to non-existent local port
    crawler = FirecrawlCrawler(mock_target_config, base_url="http://127.0.0.1:59999")
    is_avail, status, details = pytest.importorskip("asyncio").run(crawler.check_health())
    assert is_avail is False
    assert status == "UNAVAILABLE"
    assert "Connection refused" in details.get("error", "") or "unreachable" in details.get("error", "")


def test_firecrawl_failure_classifier_service_unavailable(mock_target_config):
    resp = CrawlerResponse(
        url="https://www.amazon.de/dp/B09G91LXFP",
        final_url="https://www.amazon.de/dp/B09G91LXFP",
        status_code=0,
        strategy="FIRECRAWL",
        success=False,
        error_message="Cannot connect to self-hosted Firecrawl at http://localhost:3002: Connection refused",
        failure_reason="FIRECRAWL_SERVICE_UNAVAILABLE",
        provider_failure_reason="ECONNREFUSED"
    )

    diagnosis = FailureClassifier.classify_crawl_failure(resp)
    assert diagnosis.category == FailureCategory.NETWORK
    assert diagnosis.specific_reason == SpecificReason.FIRECRAWL_SERVICE_UNAVAILABLE
    assert diagnosis.source_strategy == "FIRECRAWL"
    assert diagnosis.provider_failure_reason == "ECONNREFUSED"
    assert diagnosis.is_recoverable is False


def test_firecrawl_failure_classifier_timeout(mock_target_config):
    resp = CrawlerResponse(
        url="https://www.amazon.de/dp/B09G91LXFP",
        final_url="https://www.amazon.de/dp/B09G91LXFP",
        status_code=0,
        strategy="FIRECRAWL",
        success=False,
        error_message="Firecrawl scrape request timed out after 30s",
        failure_reason="FIRECRAWL_TIMEOUT",
        provider_failure_reason="ETIMEDOUT"
    )

    diagnosis = FailureClassifier.classify_crawl_failure(resp)
    assert diagnosis.category == FailureCategory.NETWORK
    assert diagnosis.specific_reason == SpecificReason.FIRECRAWL_TIMEOUT
    assert diagnosis.source_strategy == "FIRECRAWL"
    assert diagnosis.provider_failure_reason == "ETIMEDOUT"
    assert diagnosis.is_recoverable is True


def test_strategy_controller_chain_modes(mock_target_config):
    # Test explicit mode
    ctrl_fc = StrategyController(mock_target_config, mode="firecrawl")
    assert ctrl_fc.get_strategy_chain() == ["FIRECRAWL"]

    ctrl_http = StrategyController(mock_target_config, mode="http")
    assert ctrl_http.get_strategy_chain() == ["HTTP"]

    ctrl_pw = StrategyController(mock_target_config, mode="playwright")
    assert ctrl_pw.get_strategy_chain() == ["PLAYWRIGHT"]

    ctrl_compare = StrategyController(mock_target_config, mode="compare")
    assert ctrl_compare.get_strategy_chain() == ["HTTP", "PLAYWRIGHT", "FIRECRAWL"]


def test_firecrawl_manifest_creation(tmp_path):
    manifest_path = ManifestManager.create_manifest(
        run_id="test_run_firecrawl",
        target_ids=["amazon-de", "amazon-br"],
        sku_limit=10,
        configuration_hash="abc123hash",
        strategies_enabled=["HTTP", "PLAYWRIGHT", "FIRECRAWL", "ADAPTER"],
        base_dir=tmp_path
    )

    assert manifest_path.exists()
    import json
    with open(manifest_path) as f:
        data = json.load(f)

    assert data["firecrawl_enabled"] is True
    assert data["firecrawl_base_url"] == "http://localhost:3002"
    assert "FIRECRAWL" in data["strategies_enabled"]
