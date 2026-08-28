"""
Script: run_pc_analytics_engine.py
Entrypoint for running the batch Analytics & Scoring Engine.
Computes all program KPIs and outputs structured JSON and CSV deliverables into poc_data/deliverables/.
"""
import os
import sys
import json
import csv
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, List

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from poc_scraping.brightdata_collector import BrightDataPocCollector
from poc_analytics.pricing_engine import PricingAnalyticsEngine
from poc_analytics.audit_scorer import RetailerAuditScorer
from poc_analytics.evo_tracker import EvoTracker
from poc_analytics.share_of_shelf import ShareOfShelfEngine
from poc_analytics.share_of_voice import ShareOfVoiceEngine
from poc_analytics.banner_analytics import BannerAnalyticsEngine
from poc_analytics.processor_comparator import ProcessorComparatorEngine
from poc_analytics.regional_analyzer import RegionalAnalyticsEngine

POC_DATA_DIR = PROJECT_ROOT / "poc_data"
DELIVERABLES_DIR = POC_DATA_DIR / "deliverables"
RAW_DATASET_PATH = POC_DATA_DIR / "raw_scraped_pc_dataset.json"


def load_or_collect_raw_dataset() -> Dict[str, Any]:
    """Loads raw dataset from local cache or runs one-time scraper if not present."""
    if RAW_DATASET_PATH.exists():
        with open(RAW_DATASET_PATH, "r", encoding="utf-8") as f:
            print(f"📖 Loaded cached raw dataset from: {RAW_DATASET_PATH}")
            return json.load(f)
    print("⚠️ Raw dataset not cached yet. Running one-time Bright Data scraper...")
    return BrightDataPocCollector.collect_dataset()


def main():
    print("=" * 80)
    print(" 🚀 RUNNING PC INTELLIGENCE BATCH ANALYTICS & SCORING ENGINE")
    print("=" * 80)

    DELIVERABLES_DIR.mkdir(parents=True, exist_ok=True)
    raw_dataset = load_or_collect_raw_dataset()
    products = raw_dataset.get("products", [])
    sov_searches = raw_dataset.get("sov_searches", [])
    banners = raw_dataset.get("banners", [])

    print(f"\nProcessing {len(products)} products, {len(sov_searches)} SOV keywords, and {len(banners)} banners...\n")

    # 1. In-Season Pricing & Segment Analytics
    pricing_res = PricingAnalyticsEngine.compute_pricing_segments(products)
    _save_json(DELIVERABLES_DIR / "category_pricing_segments.json", pricing_res)
    print("✅ Computed In-Season Category Management & Segment Pricing")

    # 2. Retailer Audit & Brand Compliance Scoring (85% Laptop / 15% Desktop)
    audit_res = RetailerAuditScorer.compute_retailer_audit_scores(products)
    _save_json(DELIVERABLES_DIR / "brand_benchmarking_scores.json", audit_res)
    _save_brand_scores_csv(DELIVERABLES_DIR / "brand_benchmarking_scores.csv", audit_res)
    print(f"✅ Computed Retailer Audit Scores (Overall Brand Compliance: {audit_res['program_compliance_score']}%)")

    # 3. Intel EVO Badge Tracking
    evo_res = EvoTracker.compute_evo_metrics(products)
    _save_json(DELIVERABLES_DIR / "intel_evo_tracking_report.json", evo_res)
    print(f"✅ Computed Intel EVO Badge Tracking ({evo_res['total_evo_badged_skus']} Badged / {evo_res['total_intel_laptops']} Intel Laptops = {evo_res['overall_evo_penetration_pct']}%)")

    # 4. Share of Shelf (SOS)
    sos_res = ShareOfShelfEngine.compute_share_of_shelf(products)
    _save_json(DELIVERABLES_DIR / "share_of_shelf_report.json", sos_res)
    _save_sos_csv(DELIVERABLES_DIR / "share_of_shelf_report.csv", sos_res)
    print(f"✅ Computed Share of Shelf (Overall Intel SOS: {sos_res['overall_sos']['intel_sos_pct']}%)")

    # 5. Share of Voice (Search) (SOV)
    sov_res = ShareOfVoiceEngine.compute_share_of_voice(sov_searches)
    _save_json(DELIVERABLES_DIR / "share_of_voice_report.json", sov_res)
    _save_sov_csv(DELIVERABLES_DIR / "share_of_voice_report.csv", sov_res)
    print(f"✅ Computed Share of Voice for 10 Keywords (Average Intel SOV: {sov_res['average_intel_sov_pct']}%)")

    # 6. Banner Tracking Report
    banner_res = BannerAnalyticsEngine.compute_banner_analytics(banners)
    _save_json(DELIVERABLES_DIR / "banner_tracking_report.json", banner_res)
    print(f"✅ Computed Banner Tracking Report ({banner_res['intel_banners_count']} Intel Banners / {banner_res['total_banners']} Total = {banner_res['intel_banner_share_pct']}%)")

    # 7. Processor Comparison Report (with MoM delta)
    cpu_res = ProcessorComparatorEngine.compute_processor_comparisons(products)
    _save_json(DELIVERABLES_DIR / "processor_comparison_report.json", cpu_res)
    print(f"✅ Computed Processor Comparison Report (Intel CPU Share: {cpu_res['intel_overall_cpu_share_pct']}%, Net MoM Change: {cpu_res['intel_overall_mom_delta_pct']:+.1f}%)")

    # 8. Regional Reports (US Slice + LATAM Placeholder)
    regional_res = RegionalAnalyticsEngine.compute_regional_reports(
        products=products,
        retailer_scorecards=audit_res["retailer_scorecards"],
        overall_sos=sos_res["overall_sos"]
    )
    _save_json(DELIVERABLES_DIR / "regional_report_us_latam.json", regional_res)
    print("✅ Generated Regional Intelligence Report (US Active + LATAM Placeholder)")

    # 9. Screenshot Index Deliverable
    screenshot_index = {
        "total_screenshots": len(products) + len(banners),
        "banner_screenshots": [
            {
                "banner_id": b["banner_id"],
                "retailer": b["retailer"],
                "brand": b["brand"],
                "file": b.get("screenshot_svg_path") or b.get("screenshot_file")
            }
            for b in banners
        ],
        "pdp_screenshots": [
            {
                "sku_id": p["sku_id"],
                "retailer": p["retailer"],
                "oem": p["oem"],
                "model_series": p["model_series"],
                "file": p.get("screenshot_pdp_path")
            }
            for p in products
        ]
    }
    _save_json(DELIVERABLES_DIR / "screenshot_index.json", screenshot_index)
    print("✅ Compiled Screenshot Reference Index")

    print("\n" + "=" * 80)
    print(" 🎉 ALL 8 PROGRAM DELIVERABLES GENERATED IN: poc_data/deliverables/")
    print("=" * 80)


def _save_json(path: Path, data: Any) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def _save_brand_scores_csv(path: Path, audit_res: Dict[str, Any]) -> None:
    headers = ["retailer", "total_skus", "laptop_score", "desktop_score", "brand_compliance_score", "grade"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for ret, sc in audit_res.get("retailer_scorecards", {}).items():
            writer.writerow([
                ret, sc["total_skus"], sc["laptop_compliance_score"], sc["desktop_compliance_score"],
                sc["brand_compliance_score"], sc["compliance_grade"]
            ])


def _save_sos_csv(path: Path, sos_res: Dict[str, Any]) -> None:
    headers = ["retailer", "total_skus", "intel_count", "intel_sos_pct", "amd_count", "amd_sos_pct", "apple_count", "qualcomm_count"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for ret, r in sos_res.get("retailer_sos", {}).items():
            writer.writerow([
                ret, r["total_skus"], r["intel_count"], r["intel_sos_pct"],
                r["amd_count"], r["amd_sos_pct"], r["apple_count"], r["qualcomm_count"]
            ])


def _save_sov_csv(path: Path, sov_res: Dict[str, Any]) -> None:
    headers = ["rank", "keyword", "intel_share_pct", "sponsored_intel_share_pct", "top_ranked_sku", "top2_audit_score"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for k in sov_res.get("ranked_keywords", []):
            writer.writerow([
                k.get("intel_rank"), k.get("keyword"), k.get("intel_share_pct"),
                k.get("sponsored_intel_share_pct"), k.get("top_ranked_sku"),
                k.get("top2_page_audit", {}).get("score")
            ])


if __name__ == "__main__":
    main()
