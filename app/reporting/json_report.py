import json
from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime, timezone
from app.models.crawl_result import TargetCrawlReport


class JsonReportGenerator:
    """Generates complete JSON report containing full audit traces across all targets."""

    @classmethod
    def generate(cls, reports: List[TargetCrawlReport], output_path: str = "reports/crawl_report.json") -> str:
        out_file = Path(output_path)
        out_file.parent.mkdir(parents=True, exist_ok=True)

        summary_data = {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "total_targets_evaluated": len(reports),
            "overall_sku_coverage": round(sum(r.sku_coverage for r in reports) / max(1, len(reports)), 3) if reports else 0.0,
            "overall_validated_skus": sum(r.validated_count for r in reports),
            "overall_target_skus": sum(r.target_skus for r in reports),
            "grade_distribution": {
                "A": sum(1 for r in reports if r.capability_grade == "A"),
                "B": sum(1 for r in reports if r.capability_grade == "B"),
                "C": sum(1 for r in reports if r.capability_grade == "C"),
                "D": sum(1 for r in reports if r.capability_grade == "D"),
                "E": sum(1 for r in reports if r.capability_grade == "E"),
            },
            "category_distribution": {},
            "targets": [r.model_dump() for r in reports]
        }

        for r in reports:
            cat = r.capability_category
            summary_data["category_distribution"][cat] = summary_data["category_distribution"].get(cat, 0) + 1

        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(summary_data, f, indent=2)

        return str(out_file)
