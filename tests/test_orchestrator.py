import pytest
import asyncio
from app.models.retailer import RetailerTargetConfig, DiscoveryConfig
from app.orchestrator.engine import CrawlOrchestrator
from app.evidence.store import EvidenceStore
from tests.mock_server import run_mock_server_in_thread


@pytest.fixture(scope="session", autouse=True)
def start_mock_server():
    server = run_mock_server_in_thread()
    # Give server time to bind port
    import time
    time.sleep(0.5)
    yield


@pytest.mark.asyncio
async def test_orchestrator_integration_crawl(tmp_path):
    target_cfg = RetailerTargetConfig(
        target_id="mock-store",
        retailer="mockstore",
        brand_name="Mock Ecommerce Store",
        country="US",
        domain="127.0.0.1",
        base_url="http://127.0.0.1:8765",
        locale="en-US",
        currency="USD",
        discovery=DiscoveryConfig(
            sitemaps=["http://127.0.0.1:8765/sitemap.xml"],
            category_urls=["http://127.0.0.1:8765/category/laptops"]
        )
    )

    evidence_store = EvidenceStore(base_evidence_dir=str(tmp_path / "evidence"))
    orchestrator = CrawlOrchestrator(evidence_store=evidence_store)

    report = await orchestrator.crawl_target(
        target_config=target_cfg,
        limit=20
    )

    assert report.discovered == 20
    assert report.target_skus == 20
    assert report.extracted_count >= 15
    assert report.validated_count >= 14
    assert report.sku_coverage >= 0.70
    assert report.capability_grade in ("A", "B", "C")
    assert (tmp_path / "evidence" / "mockstore" / "US").exists()
