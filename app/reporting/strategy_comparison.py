"""
Fair Same-URL Multi-Strategy Benchmark Runner.
Executes independent evaluation across HTTP, Playwright, Firecrawl, and Adapters
on an immutable frozen SKU population, storing strategy-specific evidence and matrix records.
"""
import os
import time
import json
import csv
import statistics
from datetime import datetime, timezone
from typing import List, Dict, Any, Optional
from rich.console import Console
from rich.table import Table

from app.models.registry import TargetRegistry, CanonicalTarget
from app.crawlers.http import HttpCrawler
from app.crawlers.playwright import PlaywrightCrawler
from app.crawlers.firecrawl import FirecrawlCrawler
from app.extraction.engine import ProductExtractionEngine
from app.extraction.template import ProductTemplateIdentifier
from app.retailers.registry import RetailerAdapterRegistry
from app.evidence.store import EvidenceStore
from app.models.crawl_result import CrawlAttempt
from app.models.failure import FailureDiagnosis, FailureCategory, SpecificReason
from app.evaluation.failures import FailureClassifier
from app.discovery import ProductDiscoveryEngine

console = Console()


async def run_fair_strategy_comparison(
    targets: List[CanonicalTarget],
    strategies: List[str],
    limit: int = 10,
    save_evidence: bool = True,
    firecrawl_base_url: Optional[str] = None,
    run_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Executes a fair A/B comparison across identical real SKU URLs
    for each configured crawler strategy (HTTP, PLAYWRIGHT, FIRECRAWL, ADAPTER).
    Freezes the target population into population.json and writes strategy_matrix.csv.
    """
    actual_run_id = run_id or f"run_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}_matrix"
    run_dir = os.path.join("reports", "runs", actual_run_id)
    os.makedirs(run_dir, exist_ok=True)

    evidence_store = EvidenceStore() if save_evidence else None
    results: Dict[str, Dict[str, Any]] = {
        s: {
            "attempts": 0,
            "reached": 0,
            "content_ok": 0,
            "identified": 0,
            "extracted": 0,
            "validated": 0,
            "latencies": [],
            "bytes_received": 0,
            "browser_seconds": 0.0,
            "failures": {},
            "per_sku": []
        }
        for s in strategies
    }

    # 1. Population Discovery & Freezing
    frozen_population: List[Dict[str, Any]] = []
    target_sku_map: Dict[str, List[Dict[str, Any]]] = {}

    console.print(f"[bold cyan]Freezing Population & Running Fair Same-URL Strategy Comparison on {len(targets)} target(s) across: {', '.join(strategies)}[/bold cyan]\n")

    for target in targets:
        discovery_engine = ProductDiscoveryEngine(target)
        candidate_records, _, msg = await discovery_engine.discover_products(limit=limit)

        if not candidate_records:
            console.print(f"[yellow]No URLs discovered for target {target.target_id}[/yellow]")
            continue

        target_sku_map[target.target_id] = candidate_records

        for idx, rec in enumerate(candidate_records):
            sku_id = rec.get("sku_id") or f"sku_{idx+1:03d}"
            frozen_population.append({
                "target_id": target.target_id,
                "retailer": target.retailer,
                "country": target.country,
                "category": rec.get("category", "General"),
                "sku_id": sku_id,
                "sku_url": rec["url"],
                "selection_method": "category_balanced_seed_sitemap",
                "selection_timestamp": datetime.now(timezone.utc).isoformat()
            })

    # Save frozen population
    pop_file = os.path.join(run_dir, "population.json")
    with open(pop_file, "w", encoding="utf-8") as f:
        json.dump(frozen_population, f, indent=2)

    console.print(f"[green]Frozen population of {len(frozen_population)} SKU URLs saved to {pop_file}[/green]\n")

    # Strategy matrix tracking for CSV output
    matrix_rows: List[Dict[str, Any]] = []

    # 2. Execute Fair Benchmark Across Same URLs
    for target in targets:
        candidate_records = target_sku_map.get(target.target_id, [])
        if not candidate_records:
            continue

        console.print(f"Target: [bold]{target.brand_name} ({target.country})[/bold] - Testing {len(candidate_records)} identical SKU URLs across strategies...")

        http_crawler = HttpCrawler(target)
        playwright_crawler = PlaywrightCrawler(target, headless=True)
        firecrawl_crawler = FirecrawlCrawler(target, base_url=firecrawl_base_url)
        extraction_engine = ProductExtractionEngine(target)
        retailer_adapter = RetailerAdapterRegistry.get_adapter(target)

        for idx, rec in enumerate(candidate_records):
            url = rec["url"]
            sku_id = rec.get("sku_id") or f"sku_{idx+1:03d}"
            category = rec.get("category", "General")

            sku_strategy_attempts: Dict[str, Any] = {}

            for strat in strategies:
                strat_metrics = results[strat]
                strat_metrics["attempts"] += 1

                t_start = time.perf_counter()
                browser_sec = 0.0

                try:
                    if strat == "PLAYWRIGHT":
                        resp = await playwright_crawler.fetch(url)
                        browser_sec = (time.perf_counter() - t_start)
                    elif strat == "FIRECRAWL":
                        resp = await firecrawl_crawler.fetch(url)
                        browser_sec = (time.perf_counter() - t_start)
                    elif strat == "ADAPTER" and retailer_adapter:
                        resp = await http_crawler.fetch(url)
                    else:
                        resp = await http_crawler.fetch(url)
                except Exception as e:
                    from app.crawlers.base import CrawlerResponse
                    resp = CrawlerResponse(
                        url=url,
                        final_url=url,
                        status_code=0,
                        strategy=strat,
                        success=False,
                        error_message=str(e),
                        failure_reason="UNKNOWN_FAILURE"
                    )

                latency_ms = resp.response_time_ms or ((time.perf_counter() - t_start) * 1000)
                strat_metrics["latencies"].append(latency_ms)
                strat_metrics["bytes_received"] += resp.bytes_received or len(resp.html or "")
                strat_metrics["browser_seconds"] += browser_sec

                is_reached = resp.status_code > 0
                if is_reached:
                    strat_metrics["reached"] += 1

                is_content_ok = resp.status_code == 200 and len(resp.html or resp.markdown or "") > 200 and not resp.is_blocked and not resp.is_captcha
                if is_content_ok:
                    strat_metrics["content_ok"] += 1

                # Extraction & Validation
                product = None
                extract_err = None
                template_id = "tmpl_none"
                if is_content_ok:
                    template_id = ProductTemplateIdentifier.identify_template(resp.html or "")
                    adapter_res = None
                    if strat == "ADAPTER" and retailer_adapter:
                        adapter_res = retailer_adapter.extract(resp.html or "", url)

                    product, extract_err = extraction_engine.extract_product(
                        html=resp.html or "",
                        url=url,
                        crawler_strategy=strat,
                        custom_adapter_result=adapter_res,
                        markdown=resp.markdown
                    )

                is_identified = bool(product and product.sku)
                if is_identified:
                    strat_metrics["identified"] += 1

                is_extracted = bool(product and (product.title or product.price is not None))
                if is_extracted:
                    strat_metrics["extracted"] += 1

                is_validated = bool(product and product.validation and product.validation.is_valid_sku)
                if is_validated:
                    strat_metrics["validated"] += 1

                # Classify failure if not validated
                diag = None
                if not is_validated:
                    if not is_content_ok:
                        diag = FailureClassifier.classify_crawl_failure(resp)
                    else:
                        diag = FailureClassifier.classify_extraction_failure(extract_err or "Required fields missing", strategy=strat)
                    
                    reason_key = diag.specific_reason.value if diag else "UNKNOWN_FAILURE"
                    strat_metrics["failures"][reason_key] = strat_metrics["failures"].get(reason_key, 0) + 1

                # Save strategy-specific evidence
                if evidence_store:
                    attempt_meta = CrawlAttempt(
                        attempt_number=1,
                        strategy=strat,
                        status_code=resp.status_code,
                        response_time_ms=latency_ms,
                        browser_seconds=browser_sec,
                        bytes_received=resp.bytes_received or len(resp.html or ""),
                        success=is_validated,
                        evidence_path=f"evidence/{target.retailer}/{target.country}/{sku_id}/{strat.lower()}/raw.html",
                        failure_diagnosis=diag
                    )
                    evidence_store.save_attempt(
                        retailer=target.retailer,
                        country=target.country,
                        sku_id=sku_id,
                        attempt=attempt_meta,
                        raw_html=resp.html,
                        raw_markdown=resp.markdown,
                        screenshot_bytes=resp.screenshot_bytes,
                        response_data=resp.metadata
                    )

                sku_strategy_attempts[strat] = {
                    "reached": is_reached,
                    "content_ok": is_content_ok,
                    "validated": is_validated,
                    "latency_ms": latency_ms,
                    "bytes": resp.bytes_received or len(resp.html or ""),
                    "template_id": template_id,
                    "failure_reason": diag.specific_reason.value if diag else None,
                    "anti_bot_vendor": diag.anti_bot_vendor if diag else None
                }

                # Record matrix row
                matrix_rows.append({
                    "run_id": actual_run_id,
                    "target_id": target.target_id,
                    "retailer": target.retailer,
                    "country": target.country,
                    "sku_id": sku_id,
                    "sku_url": url,
                    "category": category,
                    "strategy": strat,
                    "status_code": resp.status_code,
                    "latency_ms": round(latency_ms, 2),
                    "bytes_received": resp.bytes_received or len(resp.html or ""),
                    "is_reached": is_reached,
                    "is_content_ok": is_content_ok,
                    "is_identified": is_identified,
                    "is_extracted": is_extracted,
                    "is_validated": is_validated,
                    "template_id": template_id,
                    "failure_category": diag.category.value if diag else None,
                    "failure_reason": diag.specific_reason.value if diag else None,
                    "anti_bot_vendor": diag.anti_bot_vendor if diag else None
                })

    # Save Strategy Matrix CSV
    matrix_csv_path = os.path.join(run_dir, "strategy_matrix.csv")
    if matrix_rows:
        with open(matrix_csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(matrix_rows[0].keys()))
            writer.writeheader()
            writer.writerows(matrix_rows)
        console.print(f"[green]Strategy matrix CSV saved to {matrix_csv_path}[/green]")

    # Save Run Manifest
    manifest_data = {
        "run_id": actual_run_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "target_count": len(targets),
        "sku_limit": limit,
        "population_count": len(frozen_population),
        "targets": [t.target_id for t in targets],
        "strategies_enabled": strategies,
        "firecrawl_version": "v2.11.0",
        "firecrawl_commit": "ca0be9b7d91eb9b48d3430f5678211f0d47e1d90",
        "firecrawl_base_url": firecrawl_base_url or os.getenv("FIRECRAWL_BASE_URL", "http://localhost:3008"),
        "results_summary": {
            s: {
                "attempts": results[s]["attempts"],
                "reached": results[s]["reached"],
                "content_ok": results[s]["content_ok"],
                "validated": results[s]["validated"],
                "avg_latency_ms": round(statistics.mean(results[s]["latencies"]), 2) if results[s]["latencies"] else 0.0
            }
            for s in strategies
        }
    }
    manifest_file = os.path.join(run_dir, "manifest.json")
    with open(manifest_file, "w", encoding="utf-8") as f:
        json.dump(manifest_data, f, indent=2)

    # 3. Print Rich Comparison Table
    table = Table(title="Same-URL Fair Strategy Comparison Benchmark", header_style="bold magenta")
    table.add_column("Strategy", style="cyan", justify="left")
    table.add_column("Attempts", justify="right")
    table.add_column("Reachability", justify="right")
    table.add_column("Content OK", justify="right")
    table.add_column("Product ID", justify="right")
    table.add_column("Extracted", justify="right")
    table.add_column("Validated", justify="right")
    table.add_column("Avg Latency", justify="right")
    table.add_column("P95 Latency", justify="right")
    table.add_column("Bytes", justify="right")

    for strat in strategies:
        m = results[strat]
        att = m["attempts"] or 1
        lats = m["latencies"] or [0]
        avg_lat = statistics.mean(lats)
        p95_lat = statistics.quantiles(lats, n=20)[-1] if len(lats) >= 20 else max(lats)

        table.add_row(
            strat,
            str(m["attempts"]),
            f"{(m['reached']/att)*100:.1f}%\n({m['reached']}/{att})",
            f"{(m['content_ok']/att)*100:.1f}%\n({m['content_ok']}/{att})",
            f"{(m['identified']/att)*100:.1f}%\n({m['identified']}/{att})",
            f"{(m['extracted']/att)*100:.1f}%\n({m['extracted']}/{att})",
            f"{(m['validated']/att)*100:.1f}%\n({m['validated']}/{att})",
            f"{avg_lat:,.0f}ms",
            f"{p95_lat:,.0f}ms",
            f"{m['bytes_received']:,} B"
        )

    console.print(table)
    return results
