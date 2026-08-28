import os
import json
from pathlib import Path
from typing import Dict, Any, Optional
from app.models.crawl_result import SkuCrawlResult, CrawlAttempt
from app.models.product import NormalizedProduct
from app.models.failure import FailureDiagnosis


class EvidenceStore:
    """Stores complete raw auditable evidence for every SKU crawl attempt."""

    def __init__(self, base_evidence_dir: str = "evidence"):
        self.base_dir = Path(base_evidence_dir)
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def get_sku_evidence_dir(self, retailer: str, country: str, sku_id: str) -> Path:
        """Constructs and creates the dedicated evidence directory for a SKU."""
        clean_retailer = retailer.lower().replace(" ", "_")
        clean_country = country.upper()
        clean_sku = "".join(c if c.isalnum() or c in "-_" else "_" for c in sku_id)
        sku_dir = self.base_dir / clean_retailer / clean_country / clean_sku
        sku_dir.mkdir(parents=True, exist_ok=True)
        return sku_dir

    def save_attempt(
        self,
        retailer: str,
        country: str,
        sku_id: str,
        attempt: CrawlAttempt,
        raw_html: Optional[str] = None,
        raw_markdown: Optional[str] = None,
        screenshot_bytes: Optional[bytes] = None,
        request_data: Optional[Dict[str, Any]] = None,
        response_data: Optional[Dict[str, Any]] = None
    ) -> CrawlAttempt:
        """Saves raw HTTP/Browser/Firecrawl attempt data, snapshots, and logs."""
        sku_dir = self.get_sku_evidence_dir(retailer, country, sku_id)
        strat_sub = (attempt.strategy or "unknown").lower()
        strat_dir = sku_dir / strat_sub
        strat_dir.mkdir(parents=True, exist_ok=True)
        prefix = f"attempt_{attempt.attempt_number}"

        # 1. Save HTML snapshot
        if raw_html and raw_html.strip():
            html_file = strat_dir / "raw.html"
            with open(html_file, "w", encoding="utf-8", errors="ignore") as f:
                f.write(raw_html)
            attempt.evidence_path = str(html_file)

        # 2. Save Markdown if present
        if raw_markdown and raw_markdown.strip():
            md_file = strat_dir / "markdown.md"
            with open(md_file, "w", encoding="utf-8", errors="ignore") as f:
                f.write(raw_markdown)

        # 3. Save Screenshot if present
        if screenshot_bytes:
            screen_file = strat_dir / "screenshot.png"
            with open(screen_file, "wb") as f:
                f.write(screenshot_bytes)
            attempt.screenshot_path = str(screen_file)

        # 4. Save Request & Response metadata if provided
        if request_data:
            with open(strat_dir / "request.json", "w", encoding="utf-8") as f:
                json.dump(request_data, f, indent=2)
        if response_data:
            with open(strat_dir / "response.json", "w", encoding="utf-8") as f:
                json.dump(response_data, f, indent=2)

        # 5. Save Attempt JSON log
        attempt_json_file = strat_dir / f"{prefix}_meta.json"
        with open(attempt_json_file, "w", encoding="utf-8") as f:
            json.dump(attempt.model_dump(exclude={"screenshot_bytes"}), f, indent=2)

        return attempt

    def save_sku_result(
        self,
        sku_result: SkuCrawlResult
    ) -> str:
        """Saves the final SKU result, normalized product, and failure diagnosis."""
        sku_dir = self.get_sku_evidence_dir(
            sku_result.retailer,
            sku_result.country,
            sku_result.sku_id
        )
        sku_result.evidence_dir = str(sku_dir)

        # Save final result meta
        result_file = sku_dir / "crawl_result.json"
        with open(result_file, "w", encoding="utf-8") as f:
            json.dump(sku_result.model_dump(mode="json"), f, indent=2)

        # Save final product if extracted
        if sku_result.product:
            prod_file = sku_dir / "normalized_product.json"
            with open(prod_file, "w", encoding="utf-8") as f:
                json.dump(sku_result.product.model_dump(mode="json"), f, indent=2)

        # Save failure diagnosis if failed
        if sku_result.failure:
            fail_file = sku_dir / "failure_diagnosis.json"
            with open(fail_file, "w", encoding="utf-8") as f:
                json.dump(sku_result.failure.model_dump(mode="json"), f, indent=2)

        return str(sku_dir)
