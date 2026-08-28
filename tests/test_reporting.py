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


def test_psv_report_generator(tmp_path):
    import csv
    from app.reporting.csv_report import PsvReportGenerator

    report = TargetCrawlReport(
        target_id="mock-psv",
        retailer="mockpsv",
        brand_name="Mock Store | Special & Tier-1",
        country="US",
        target_skus=10,
        discovered=10,
        http_success_count=10,
        browser_success_count=0,
        extracted_count=10,
        validated_count=10,
        sku_coverage=1.0,
        capability_grade="A",
        capability_category="HTTP_ONLY",
        avg_latency_ms=100.0,
        p95_latency_ms=150.0
    )

    psv_file = tmp_path / "matrix.psv"
    PsvReportGenerator.generate([report], output_path=str(psv_file))

    assert psv_file.exists()
    with open(psv_file, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="|")
        rows = list(reader)
        assert len(rows) == 2
        # Verify header
        assert rows[0][0] == "RETAILER"
        # Verify brand_name containing literal pipe was escaped/quoted properly
        assert rows[1][0] == "Mock Store | Special & Tier-1"


def test_deliverable_exporter_all_workstreams(tmp_path):
    import csv
    from app.reporting.deliverable_exporter import DeliverableExporter

    output_dir = tmp_path / "deliverables"
    files = DeliverableExporter.export_all_deliverables(
        dataset_path="dashboard/src/data/live_52_sku_dataset.json",
        output_dir=str(output_dir),
        delimiter="|"
    )

    expected_keys = [
        "brand_benchmarking_scorecards",
        "master_sku_compliance_scores",
        "banner_tracking",
        "share_of_shelf",
        "intel_evo_tracking",
        "share_of_voice",
        "processor_comparison",
        "regional_us",
        "regional_latam"
    ]

    for k in expected_keys:
        assert k in files
        p = Path(files[k])
        assert p.exists()
        assert p.stat().st_size > 0

    # Master SKU Catalog assertions
    master_p = Path(files["master_sku_compliance_scores"])
    with open(master_p, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="|")
        rows = list(reader)
        # 1 header + 1,518 SKU records = 1519 rows
        assert len(rows) == 1519
        headers = rows[0]
        assert "audit_depth" in headers
        assert "Overall" in headers
        assert "concatenate" in headers
        # Check audit_depth values
        depth_idx = headers.index("audit_depth")
        for row in rows[1:]:
            assert row[depth_idx] in ["FULL_PDP_AUDIT (7-Rule)", "LISTING_ONLY (2-Rule)"]

    # Share of Shelf assertions
    sos_p = Path(files["share_of_shelf"])
    with open(sos_p, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="|")
        sos_rows = {r["retailer"]: r for r in reader}
        assert len(sos_rows) == 52
        # Best Buy - US checks
        bb = sos_rows["Best Buy - US"]
        assert float(bb["intel_sos_pct"]) == 56.2
        assert int(bb["total_sample_n"]) == 32
        assert float(bb["laptop_intel_sos_pct"]) == 59.3
        assert float(bb["desktop_intel_sos_pct"]) == 40.0

