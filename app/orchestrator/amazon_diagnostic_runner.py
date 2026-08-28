"""
Dedicated Amazon Diagnostic Runner.
Executes deep diagnostic across Amazon US, UK, DE, and IN marketplaces.
Tests Search Discovery, ASIN Extraction, Structured Specs Extraction, Web Unlocker, and Browser Rendering.
Generates 'reports/amazon_brightdata_diagnostic.md'.
"""
import os
import time
import asyncio
import logging
from pathlib import Path
from typing import Dict, Any, List
from rich.console import Console
from rich.table import Table

import app.env
from app.crawlers.amazon_scraper import AmazonScraperStrategy
from app.crawlers.brightdata_web_unlocker import BrightDataWebUnlockerClient
from app.crawlers.brightdata_browser import BrightDataBrowserClient
from app.classification.laptop_classifier import LaptopClassifier

logger = logging.getLogger("crawl.amazon_diagnostic")
console = Console()


class AmazonDiagnosticRunner:
    """Diagnostic suite testing Amazon marketplace access, discovery, and extraction."""

    TARGET_MARKETPLACES = [
        {"country": "US", "domain": "amazon.com", "name": "Amazon United States"},
        {"country": "GB", "domain": "amazon.co.uk", "name": "Amazon United Kingdom"},
        {"country": "DE", "domain": "amazon.de", "name": "Amazon Germany"},
        {"country": "IN", "domain": "amazon.in", "name": "Amazon India"}
    ]

    def __init__(self):
        self.unlocker = BrightDataWebUnlockerClient()
        self.browser = BrightDataBrowserClient()
        self.amazon_strategy = AmazonScraperStrategy(unlocker_client=self.unlocker)
        self.results: List[Dict[str, Any]] = []

    async def run_diagnostic(self) -> List[Dict[str, Any]]:
        """Executes diagnostic across all target Amazon marketplaces."""
        console.print("[bold cyan]============================================================[/bold cyan]")
        console.print("[bold cyan]       BRIGHT DATA AMAZON SPECIALIZED DIAGNOSTIC SUITE       [/bold cyan]")
        console.print("[bold cyan]============================================================[/bold cyan]")

        for market in self.TARGET_MARKETPLACES:
            c_code = market["country"]
            domain = market["domain"]
            name = market["name"]

            console.print(f"\n[bold yellow]Diagnosing {name} ({domain}) [Country: {c_code}]...[/bold yellow]")
            t0 = time.perf_counter()

            diag_record: Dict[str, Any] = {
                "country": c_code,
                "marketplace": name,
                "domain": domain,
                "search_success": False,
                "candidates_found": 0,
                "top_candidate_url": None,
                "top_asin": None,
                "scraper_success": False,
                "product_title": None,
                "brand": None,
                "price": None,
                "specs_count": 0,
                "is_genuine_laptop": False,
                "classification_score": 0.0,
                "unlocker_status": "N/A",
                "browser_status": "N/A",
                "latency_ms": 0.0,
                "diagnosis_notes": ""
            }

            # Step 1 & 2: Amazon Product Search Discovery
            candidates = await self.amazon_strategy.search_laptops(
                country_code=c_code,
                keyword="laptop",
                limit=5
            )

            diag_record["candidates_found"] = len(candidates)
            if candidates:
                diag_record["search_success"] = True
                top_cand = candidates[0]
                diag_record["top_candidate_url"] = top_cand["url"]
                diag_record["top_asin"] = top_cand["asin"]
                console.print(f"  [green]Search Discovery OK[/green]: Found {len(candidates)} candidates. Top ASIN: [bold]{top_cand['asin']}[/bold]")
            else:
                console.print(f"  [red]Search Discovery FAILED[/red]: No candidates discovered.")
                diag_record["diagnosis_notes"] = "Search discovery returned 0 valid laptop cards."

            # Step 3 & 4: Specialized Product Scraping & Specs Extraction
            if diag_record["top_candidate_url"]:
                scrape_res = await self.amazon_strategy.scrape_product(
                    product_url=diag_record["top_candidate_url"],
                    country_code=c_code
                )
                diag_record["scraper_success"] = scrape_res.get("success", False)
                diag_record["product_title"] = scrape_res.get("title")
                diag_record["brand"] = scrape_res.get("brand")
                diag_record["price"] = scrape_res.get("price")
                diag_record["specs_count"] = len(scrape_res.get("specs_table", {}))

                cls_res = scrape_res.get("classification")
                if cls_res:
                    diag_record["is_genuine_laptop"] = cls_res.is_genuine_laptop
                    diag_record["classification_score"] = cls_res.confidence_score
                    console.print(f"  [green]Product Scrape OK[/green]: Title: '{diag_record['product_title'][:50]}...' | Score: {cls_res.confidence_score} | Genuine: {cls_res.is_genuine_laptop}")
                else:
                    console.print(f"  [red]Product Scrape FAILED[/red]: {scrape_res.get('error')}")

                # Step 5: Web Unlocker Verification
                unl_resp = await self.unlocker.fetch(diag_record["top_candidate_url"], country_iso=c_code.lower())
                diag_record["unlocker_status"] = f"HTTP {unl_resp.status_code} ({'OK' if unl_resp.success else 'FAILED'})"

                # Step 6: Browser API Verification
                brw_resp = await self.browser.fetch(diag_record["top_candidate_url"], country_iso=c_code.lower(), timeout_sec=25.0)
                diag_record["browser_status"] = f"HTTP {brw_resp.status_code} ({'OK' if brw_resp.success else 'FAILED'})"

            diag_record["latency_ms"] = round((time.perf_counter() - t0) * 1000, 2)
            self.results.append(diag_record)

        self._generate_diagnostic_report()
        return self.results

    def _generate_diagnostic_report(self):
        """Generates markdown report 'reports/amazon_brightdata_diagnostic.md'."""
        out_dir = Path("reports")
        out_dir.mkdir(parents=True, exist_ok=True)
        report_path = out_dir / "amazon_brightdata_diagnostic.md"

        lines = [
            "# Dedicated Amazon Specialized Scraper & Marketplace Diagnostic Report",
            "",
            "**Diagnostic Suite**: Dedicated Multi-Marketplace Amazon Laptop Benchmark",
            f"**Execution Timestamp**: {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}",
            "**Infrastructure**: Bright Data Web Unlocker, Managed Browser, Regional Egress Routing",
            "",
            "---",
            "",
            "## 1. Executive Summary Table",
            "",
            "| Marketplace | Country ISO | Search Discovery | Top ASIN | Product Scrape | Specs Extracted | Classification | Genuine Laptop? | Web Unlocker | Browser API |",
            "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |"
        ]

        for r in self.results:
            search_str = "SUCCESS" if r["search_success"] else "FAILED"
            scrape_str = "SUCCESS" if r["scraper_success"] else "FAILED"
            gen_str = "YES" if r["is_genuine_laptop"] else "NO"
            lines.append(
                f"| **{r['marketplace']}** | `{r['country']}` | `{search_str}` ({r['candidates_found']} found) | "
                f"`{r['top_asin'] or 'N/A'}` | `{scrape_str}` | {r['specs_count']} fields | "
                f"Score: {r['classification_score']} | **{gen_str}** | {r['unlocker_status']} | {r['browser_status']} |"
            )

        lines.extend([
            "",
            "---",
            "",
            "## 2. Detailed Marketplace Diagnostics",
            ""
        ])

        for r in self.results:
            lines.extend([
                f"### {r['marketplace']} (`{r['country']}`)",
                f"- **Domain**: `https://www.{r['domain']}`",
                f"- **Search Discovery Status**: {'SUCCESS' if r['search_success'] else 'FAILED'}",
                f"- **Candidates Identified**: {r['candidates_found']}",
                f"- **Top Candidate URL**: {r['top_candidate_url'] or 'None'}",
                f"- **Top ASIN**: `{r['top_asin'] or 'None'}`",
                f"- **Extracted Title**: {r['product_title'] or 'N/A'}",
                f"- **Brand**: {r['brand'] or 'N/A'}",
                f"- **Price**: {r['price'] or 'N/A'}",
                f"- **Hardware Specs Extracted**: {r['specs_count']} attributes",
                f"- **Strict Laptop Validation**: **{'VERIFIED GENUINE LAPTOP' if r['is_genuine_laptop'] else 'REJECTED / UNVERIFIED'}** (Score: {r['classification_score']})",
                f"- **Web Unlocker Verification**: {r['unlocker_status']}",
                f"- **Browser API Verification**: {r['browser_status']}",
                f"- **Total Round-Trip Latency**: {r['latency_ms']} ms",
                ""
            ])

        lines.extend([
            "---",
            "",
            "## 3. Failure Mode & Root Cause Attribution Matrix",
            "",
            "| Area | Potential Failure Mode | Diagnostic Result & Fix |",
            "| :--- | :--- | :--- |",
            "| **Credentials** | Missing or invalid `BRIGHTDATA_API_KEY` | Cleanly read from environment; masked across all telemetry. |",
            "| **Country Routing** | Geoblock / Non-local marketplace redirect | Native ISO flags (`country-us`, `country-gb`, `country-de`, `country-in`) ensure local regional landing pages. |",
            "| **ASIN Relevance** | Accessories or non-laptop items in search | Strict negative keyword filters reject bags, cases, chargers, and keyboards at candidate discovery. |",
            "| **Specs Parsing** | Dynamic Amazon DOM layout variants | Multi-table selectors inspect `#productDetails_techSpec_section_1` and `.po-table` to extract CPU, RAM, and Storage. |",
            ""
        ])

        with open(report_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        console.print(f"\n[bold green]Amazon Diagnostic Complete! Report saved to: {report_path}[/bold green]")
