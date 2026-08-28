import csv
from pathlib import Path
from typing import List
from app.models.crawl_result import TargetCrawlReport


class CsvReportGenerator:
    """Generates structured CSV/PSV matrix for data analytics and spreadsheet imports."""

    @classmethod
    def generate(
        cls,
        reports: List[TargetCrawlReport],
        output_path: str = "reports/retailer_matrix.csv",
        delimiter: str = ","
    ) -> str:
        out_file = Path(output_path)
        out_file.parent.mkdir(parents=True, exist_ok=True)

        headers = [
            "RETAILER",
            "COUNTRY",
            "GRADE",
            "CATEGORY",
            "TARGET SKUS",
            "DISCOVERED",
            "HTTP SUCCESS",
            "BROWSER SUCCESS",
            "EXTRACTION SUCCESS",
            "VALIDATION SUCCESS",
            "COVERAGE %",
            "BLOCK RATE %",
            "CAPTCHA RATE %",
            "TIMEOUT RATE %",
            "AVG LATENCY (MS)",
            "P95 LATENCY (MS)",
            "PRIMARY STRATEGY",
            "FALLBACK STRATEGY",
            "MAIN FAILURE REASON",
            "NOTES"
        ]

        rows = []
        for r in reports:
            rows.append([
                r.brand_name,
                r.country,
                r.capability_grade,
                r.capability_category,
                r.target_skus,
                r.discovered,
                r.http_success_count,
                r.browser_success_count,
                r.extracted_count,
                r.validated_count,
                f"{round(r.sku_coverage * 100, 1)}%",
                f"{round(r.block_rate * 100, 1)}%",
                f"{round(r.captcha_rate * 100, 1)}%",
                f"{round(r.timeout_rate * 100, 1)}%",
                r.avg_latency_ms,
                r.p95_latency_ms,
                r.primary_strategy,
                r.fallback_strategy or "None",
                r.main_failure_reason or "None",
                r.notes or ""
            ])

        with open(out_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=delimiter, quoting=csv.QUOTE_MINIMAL)
            writer.writerow(headers)
            writer.writerows(rows)

        return str(out_file)


class PsvReportGenerator(CsvReportGenerator):
    """Specialized generator producing standard pipe-separated (PSV) reports."""

    @classmethod
    def generate(
        cls,
        reports: List[TargetCrawlReport],
        output_path: str = "reports/retailer_matrix.psv",
        delimiter: str = "|"
    ) -> str:
        return super().generate(reports, output_path=output_path, delimiter=delimiter)

