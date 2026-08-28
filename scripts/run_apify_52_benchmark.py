"""
Production 52-Retailer Apify-Only Independent Laptop Crawling & Validation Benchmark Runner.
Evaluates Apify alone across all 52 targets with controlled concurrency, idempotency, and full metrics.
"""
import os
import sys
import json
import time
import asyncio
import argparse
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Dict, Any, Optional
import statistics

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# Load .env
for line in open(PROJECT_ROOT / ".env"):
    if "=" in line and not line.startswith("#"):
        k, v = line.strip().split("=", 1)
        os.environ.setdefault(k, v)

from app.models.registry import TargetRegistry, CanonicalTarget
from app.providers.apify_provider import ApifyProvider
from app.providers.base import ProviderTargetResult

REPORTS_DIR = PROJECT_ROOT / "reports"
PROGRESS_FILE = REPORTS_DIR / "laptop_apify_52_progress.json"
EVIDENCE_APIFY_BASE = PROJECT_ROOT / "evidence" / "apify"


async def run_benchmark(
    concurrency: int = 4,
    force: bool = False,
    timeout: int = 45,
    max_retries: int = 2
) -> Dict[str, Any]:
    """Runs the 52-target Apify-only benchmark."""
    print("=" * 80)
    print(" 🚀 STARTING 52-RETAILER APIFY-ONLY INDEPENDENT BENCHMARK")
    print(f" Concurrency: {concurrency} | Timeout: {timeout}s | Max Retries: {max_retries} | Force Rerun: {force}")
    print("=" * 80)

    provider = ApifyProvider(timeout_sec=timeout, max_retries=max_retries)
    is_healthy, status_str, details = provider.health_check()
    print(f"Apify Provider Health Check: [{status_str}]")
    if not is_healthy:
        print(f"⚠️ Warning: {details.get('error')}")
        print("Note: Benchmark will execute with ApifyProvider and record authentic auth/access outcomes for all 52 targets.")

    reg = TargetRegistry()
    targets = sorted(reg.all_targets(), key=lambda t: t.target_id)
    print(f"\nLoaded {len(targets)} Canonical Targets from config/targets.yaml.\n")

    # Load existing progress for idempotency
    completed_results: Dict[str, Dict[str, Any]] = {}
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    if not force and PROGRESS_FILE.exists():
        try:
            with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
                saved = json.load(f)
                completed_results = saved.get("results", {})
                print(f"Resuming previous run: {len(completed_results)} completed targets loaded.")
        except Exception:
            completed_results = {}

    sem = asyncio.Semaphore(concurrency)
    results_lock = asyncio.Lock()
    all_results: Dict[str, ProviderTargetResult] = {}

    async def _process_target(target: CanonicalTarget) -> ProviderTargetResult:
        t_id = target.target_id
        
        # Check idempotency
        if not force and t_id in completed_results:
            ev_file = EVIDENCE_APIFY_BASE / t_id / "evidence_summary.json"
            if ev_file.exists():
                try:
                    with open(ev_file, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        res = ProviderTargetResult.model_validate(data)
                        print(f"  [CACHED] [{t_id:20s}] Status: {res.status:7s} | Validated: {str(res.validation_success):5s}")
                        return res
                except Exception:
                    pass

        async with sem:
            print(f"  ⏳ [{t_id:20s}] Starting Apify crawl ({target.retailer}, {target.country})...")
            try:
                res = await provider.crawl_and_scrape(target)
            except Exception as e:
                res = ProviderTargetResult(
                    target_id=t_id,
                    retailer=target.retailer,
                    country=target.country,
                    domain=target.domain,
                    provider_name="apify",
                    status="FAILURE",
                    can_scrape="NO",
                    failure_stage="ACTOR_EXECUTION",
                    failure_category="APIFY_ACTOR_FAILURE",
                    failure_reason="UNKNOWN_FAILURE",
                    failure_message=str(e)
                )

            icon = "✅" if res.status == "SUCCESS" else "❌"
            print(f"  {icon} [{t_id:20s}] Status: {res.status:7s} | Access: {str(res.access_success):5s} | Disc: {str(res.discovery_success):5s} | Ext: {str(res.extraction_success):5s} | Val: {str(res.validation_success):5s} | {res.failure_reason or 'OK'}")

            async with results_lock:
                completed_results[t_id] = res.model_dump()
                # Save incremental progress
                with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
                    json.dump({
                        "timestamp": datetime.now(timezone.utc).isoformat(),
                        "completed_count": len(completed_results),
                        "results": completed_results
                    }, f, indent=2, ensure_ascii=False)

            return res

    tasks = [_process_target(t) for t in targets]
    res_list = await asyncio.gather(*tasks)
    
    for r in res_list:
        all_results[r.target_id] = r

    # Compute comprehensive metrics
    total = len(all_results)
    successful = sum(1 for r in all_results.values() if r.status == "SUCCESS")
    failed = total - successful
    success_rate = (successful / total * 100) if total > 0 else 0.0

    access_success_cnt = sum(1 for r in all_results.values() if r.access_success)
    discovery_success_cnt = sum(1 for r in all_results.values() if r.discovery_success)
    extraction_success_cnt = sum(1 for r in all_results.values() if r.extraction_success)
    validation_success_cnt = sum(1 for r in all_results.values() if r.validation_success)

    durations = [r.execution_duration_sec for r in all_results.values() if r.execution_duration_sec > 0]
    avg_duration = statistics.mean(durations) if durations else 0.0
    median_duration = statistics.median(durations) if durations else 0.0

    pages_crawled_list = [r.pages_crawled for r in all_results.values()]
    avg_pages = statistics.mean(pages_crawled_list) if pages_crawled_list else 0.0
    successful_pages = [r.pages_crawled for r in all_results.values() if r.status == "SUCCESS"]
    avg_successful_pages = statistics.mean(successful_pages) if successful_pages else 0.0

    retries_list = [r.retry_count for r in all_results.values()]
    avg_retries = statistics.mean(retries_list) if retries_list else 0.0

    # Failure counts
    waf_failures = sum(1 for r in all_results.values() if r.failure_category in ("WAF_OR_ANTI_BOT", "ACCESS_FAILURE") or r.failure_reason == "BOT_PROTECTION")
    discovery_failures = sum(1 for r in all_results.values() if r.failure_category == "URL_DISCOVERY_FAILURE" or r.failure_stage == "DISCOVERY")
    extraction_failures = sum(1 for r in all_results.values() if r.failure_category == "EXTRACTION_FAILURE" or r.failure_stage == "EXTRACTION")
    validation_failures = sum(1 for r in all_results.values() if r.failure_category == "VALIDATION_FAILURE" or r.failure_stage == "VALIDATION")
    timeouts = sum(1 for r in all_results.values() if r.failure_reason in ("TIMEOUT", "APIFY_TIMEOUT"))
    actor_failures = sum(1 for r in all_results.values() if r.failure_reason in ("APIFY_ACTOR_FAILURE", "APIFY_AUTH_FAILED"))

    summary_metrics = {
        "benchmark_name": "52-Retailer Apify-Only Independent Laptop Benchmark",
        "provider": "apify",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "total_targets": total,
        "successful_targets": successful,
        "failed_targets": failed,
        "success_rate": f"{success_rate:.1f}%",
        "access_success_count": access_success_cnt,
        "discovery_success_count": discovery_success_cnt,
        "extraction_success_count": extraction_success_cnt,
        "validation_success_count": validation_success_cnt,
        "average_execution_time_sec": round(avg_duration, 2),
        "median_execution_time_sec": round(median_duration, 2),
        "average_pages_crawled": round(avg_pages, 2),
        "average_pages_crawled_successful": round(avg_successful_pages, 2),
        "average_retries": round(avg_retries, 2),
        "waf_failures": waf_failures,
        "discovery_failures": discovery_failures,
        "extraction_failures": extraction_failures,
        "validation_failures": validation_failures,
        "timeouts": timeouts,
        "actor_or_auth_failures": actor_failures
    }

    print("\n" + "=" * 80)
    print(" 📊 APIFY BENCHMARK SUMMARY METRICS")
    print("=" * 80)
    for k, v in summary_metrics.items():
        print(f"  {k:35s}: {v}")
    print("=" * 80 + "\n")

    return {
        "summary": summary_metrics,
        "results": {k: v.model_dump() for k, v in all_results.items()}
    }


def main():
    parser = argparse.ArgumentParser(description="Run 52-retailer Apify-only benchmark")
    parser.add_argument("--concurrency", type=int, default=4, help="Number of concurrent workers (default: 4)")
    parser.add_argument("--force", action="store_true", help="Force rerun even if results exist")
    parser.add_argument("--timeout", type=int, default=45, help="Timeout in seconds per target")
    parser.add_argument("--retries", type=int, default=2, help="Max retries per target")
    args = parser.parse_args()

    asyncio.run(run_benchmark(
        concurrency=args.concurrency,
        force=args.force,
        timeout=args.timeout,
        max_retries=args.retries
    ))


if __name__ == "__main__":
    main()
