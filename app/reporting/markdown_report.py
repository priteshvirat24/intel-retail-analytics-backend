from pathlib import Path
from typing import List
from datetime import datetime, timezone
from app.models.crawl_result import TargetCrawlReport


class MarkdownReportGenerator:
    """Generates detailed, readable Markdown report with capability matrix and failure diagnosis."""

    @classmethod
    def generate(cls, reports: List[TargetCrawlReport], output_path: str = "reports/crawl_report.md") -> str:
        out_file = Path(output_path)
        out_file.parent.mkdir(parents=True, exist_ok=True)

        total_targets = len(reports)
        overall_coverage = round(sum(r.sku_coverage for r in reports) / max(1, total_targets) * 100, 1) if reports else 0.0
        total_discovered = sum(r.discovered for r in reports)
        total_validated = sum(r.validated_count for r in reports)
        total_target_skus = sum(r.target_skus for r in reports)

        lines = [
            "# Global Retailer Multi-Site Crawl & SKU Extraction Capability Report",
            "",
            f"> **Generated at**: `{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}`  ",
            f"> **Scope**: `{total_targets}` Retailer-Country Targets | `{total_target_skus}` Total Target SKUs  ",
            f"> **Overall Empirical SKU Coverage**: **`{overall_coverage}%`** (`{total_validated}/{total_target_skus}` valid SKUs across catalog)",
            "",
            "---",
            "",
            "## 1. Executive Summary & Capability Classification",
            "",
            "| Grade | Level | Description | Target Count | Targets |",
            "| :---: | :--- | :--- | :---: | :--- |",
        ]

        grades = {
            "A": ("Excellent (>=95% Coverage)", []),
            "B": ("Good (85-94% Coverage)", []),
            "C": ("Partial (70-84% Coverage)", []),
            "D": ("Poor (50-69% Coverage)", []),
            "E": ("Not Practically Crawlable (<50% Coverage)", [])
        }

        for r in reports:
            g = r.capability_grade
            if g in grades:
                grades[g][1].append(f"`{r.brand_name} ({r.country})`")

        for g, (desc, t_list) in grades.items():
            t_str = ", ".join(t_list) if t_list else "_None_"
            lines.append(f"| **{g}** | {desc} | High confidence extraction | {len(t_list)} | {t_str} |")

        lines.extend([
            "",
            "---",
            "",
            "## 2. Retailer-by-Retailer Capability Matrix",
            "",
            "| Retailer | Country | Grade | Category | Target | Discovered | HTTP | Browser | Extracted | Validated | Coverage | Block % | Latency | Primary Strategy | Main Failure |",
            "| :--- | :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |"
        ])

        for r in reports:
            cov_pct = f"**{round(r.sku_coverage * 100)}%**"
            block_pct = f"{round(r.block_rate * 100)}%"
            lat = f"{int(r.avg_latency_ms)}ms"
            fail = f"`{r.main_failure_reason}`" if r.main_failure_reason else "None"
            lines.append(
                f"| **{r.brand_name}** | {r.country} | `{r.capability_grade}` | `{r.capability_category}` | "
                f"{r.target_skus} | {r.discovered} | {r.http_success_count} | {r.browser_success_count} | "
                f"{r.extracted_count} | {r.validated_count} | {cov_pct} | {block_pct} | {lat} | "
                f"{r.primary_strategy} | {fail} |"
            )

        lines.extend([
            "",
            "---",
            "",
            "## 3. Failure Root Cause Analysis & Empirical Diagnosis",
            "",
            "Detailed analysis for retailers achieving below 90% coverage threshold:",
            ""
        ])

        sub_90 = [r for r in reports if r.sku_coverage < 0.90]
        if sub_90:
            for r in sub_90:
                lines.extend([
                    f"### {r.brand_name} ({r.country}) - Coverage: {round(r.sku_coverage * 100)}% (Grade {r.capability_grade})",
                    f"- **Observed Category**: `{r.capability_category}`",
                    f"- **Main Failure**: `{r.main_failure_reason or 'UNKNOWN'}`",
                    f"- **Discovered**: `{r.discovered}/{r.target_skus}` | **Page Loads**: HTTP: `{r.http_success_count}`, Browser: `{r.browser_success_count}`",
                    f"- **Diagnosis**: {r.failure_diagnosis_summary or 'No specific failures recorded.'}",
                    f"- **Recommended Crawling Architecture**: **{r.recommended_strategy or 'Playwright + Adaptive throttling'}**",
                    ""
                ])
        else:
            lines.append("_All tested retailer targets achieved >= 90% SKU extraction coverage._\n")

        lines.extend([
            "---",
            "",
            "## 4. Auditable Evidence Directory Structure",
            "",
            "Evidence for every attempted SKU is stored in the local evidence store:",
            "```",
            "evidence/",
            "  ├── <retailer_slug>/",
            "  │     ├── <country_code>/",
            "  │     │     ├── sku_001/",
            "  │     │     │     ├── attempt_1_snapshot.html",
            "  │     │     │     ├── attempt_1_screenshot.png (if browser used)",
            "  │     │     │     ├── attempt_1_meta.json",
            "  │     │     │     ├── normalized_product.json",
            "  │     │     │     └── crawl_result.json",
            "  │     │     └── ...",
            "```",
            ""
        ])

        with open(out_file, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        return str(out_file)
