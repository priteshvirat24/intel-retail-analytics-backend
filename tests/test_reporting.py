import json
from pathlib import Path
from app.models.crawl_result import TargetCrawlReport
from app.models.registry import TargetRegistry
from app.reporting.json_report import JsonReportGenerator
from app.reporting.csv_report import CsvReportGenerator
from app.reporting.benchmark_summary import BenchmarkSummaryGenerator
from app.reporting.html_report import HtmlReportGenerator


def test_reports_generation(tmp_path):
    report = TargetCrawlReport(
        target_id="mock-store",
        retailer="mockstore",
        brand_name="Mock Store",
        country="US",
        target_skus=20,
        discovered=20,
        http_success_count=18,
        browser_success_count=2,
        extracted_count=18,
        validated_count=17,
        sku_coverage=0.85,
        capability_grade="B",
        capability_category="HTTP_ONLY",
        avg_latency_ms=145.2,
        p95_latency_ms=210.0
    )

    json_file = tmp_path / "report.json"
    csv_file = tmp_path / "matrix.csv"
    summary_file = tmp_path / "benchmark_summary.md"
    html_file = tmp_path / "dashboard.html"

    registry = TargetRegistry(Path("config/targets.yaml"))

    JsonReportGenerator.generate([report], output_path=str(json_file))
    CsvReportGenerator.generate([report], output_path=str(csv_file))
    BenchmarkSummaryGenerator.generate([report], registry, output_path=summary_file)
    HtmlReportGenerator.generate([report], output_path=str(html_file))

    assert json_file.exists()
    assert csv_file.exists()
    assert summary_file.exists()
    assert html_file.exists()

    with open(json_file, "r") as f:
        data = json.load(f)
        assert data["total_targets_evaluated"] == 1

    with open(summary_file, "r") as f:
        summary_text = f.read()
        assert "## A. Executive Summary" in summary_text
        assert "## B. Canonical Target Registry" in summary_text
        assert "## C. Overall Statistics" in summary_text
        assert "## K. Empirical Limitations" in summary_text
