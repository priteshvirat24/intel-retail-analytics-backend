import statistics
from typing import List, Dict, Any, Union
from collections import defaultdict
from app.models.crawl_result import SkuCrawlResult, TargetCrawlReport, CostTelemetry, StrategyBenchmark
from app.models.registry import CanonicalTarget
from app.models.retailer import RetailerTargetConfig
from app.models.failure import FailureCategory, SpecificReason, CrawlStage


class MetricsCalculator:
    """Calculates granular evaluation metrics, cost telemetry, strategy comparison, and summary statistics."""

    @classmethod
    def calculate_target_metrics(
        cls,
        target_config: Union[CanonicalTarget, RetailerTargetConfig],
        target_skus: int,
        discovered_count: int,
        sku_results: List[SkuCrawlResult]
    ) -> TargetCrawlReport:
        total_attempted = len(sku_results)

        http_success_count = sum(1 for r in sku_results if r.http_success)
        browser_success_count = sum(1 for r in sku_results if r.browser_success)
        extracted_count = sum(1 for r in sku_results if r.extraction_success)
        validated_count = sum(1 for r in sku_results if r.status == "SUCCESS")
        partial_count = sum(1 for r in sku_results if r.status == "PARTIAL_SUCCESS")
        failed_count = sum(1 for r in sku_results if r.status == "FAILED")

        # Rates with explicit denominators
        discovery_rate = round(discovered_count / max(1, target_skus), 3)
        page_load_rate = round((http_success_count + browser_success_count) / max(1, total_attempted), 3) if total_attempted else 0.0
        extraction_rate = round(extracted_count / max(1, (http_success_count + browser_success_count)), 3) if (http_success_count + browser_success_count) else 0.0
        validation_rate = round(validated_count / max(1, extracted_count), 3) if extracted_count else 0.0
        sku_coverage = round(validated_count / max(1, target_skus), 3)

        # Field completeness avg
        completeness_scores = [
            r.product.validation.field_completeness
            for r in sku_results
            if r.product and r.product.validation
        ]
        avg_completeness = round(statistics.mean(completeness_scores), 3) if completeness_scores else 0.0

        # Cost Telemetry
        request_count = sum(len(r.attempts) for r in sku_results)
        successful_requests = sum(1 for r in sku_results for a in r.attempts if a.success)
        failed_requests = request_count - successful_requests
        browser_seconds = sum(a.browser_seconds for r in sku_results for a in r.attempts)
        total_latency_ms = sum(r.total_latency_ms for r in sku_results)
        bytes_received = sum(a.bytes_received for r in sku_results for a in r.attempts)
        total_retries = sum(len(r.attempts) - 1 for r in sku_results if len(r.attempts) > 1)

        latencies = [r.total_latency_ms for r in sku_results if r.total_latency_ms > 0]
        avg_latency = round(statistics.mean(latencies), 2) if latencies else 0.0
        median_latency = round(statistics.median(latencies), 2) if latencies else 0.0

        if len(latencies) >= 2:
            sorted_latencies = sorted(latencies)
            p95_idx = int(len(sorted_latencies) * 0.95)
            p95_latency = round(sorted_latencies[min(p95_idx, len(sorted_latencies) - 1)], 2)
        elif latencies:
            p95_latency = latencies[0]
        else:
            p95_latency = 0.0

        avg_retries = round(total_retries / max(1, total_attempted), 2) if total_attempted else 0.0

        cost_telemetry = CostTelemetry(
            request_count=request_count,
            successful_requests=successful_requests,
            failed_requests=failed_requests,
            browser_seconds=round(browser_seconds, 2),
            total_latency_ms=round(total_latency_ms, 2),
            average_latency_ms=avg_latency,
            p95_latency_ms=p95_latency,
            retry_count=total_retries,
            bytes_received=bytes_received
        )

        # Strategy Benchmarking
        http_valid = sum(1 for r in sku_results if r.effective_strategy == "HTTP" and r.status == "SUCCESS")
        pw_valid = sum(1 for r in sku_results if r.effective_strategy == "PLAYWRIGHT" and r.status == "SUCCESS")
        fc_valid = sum(1 for r in sku_results if r.effective_strategy == "FIRECRAWL" and r.status == "SUCCESS")
        adapt_valid = sum(1 for r in sku_results if r.effective_strategy == "ADAPTER" and r.status == "SUCCESS")

        scores = [("HTTP", http_valid), ("PLAYWRIGHT", pw_valid), ("FIRECRAWL", fc_valid), ("ADAPTER", adapt_valid)]
        best_strat = max(scores, key=lambda x: x[1])[0]

        cost_per_sku = round(total_latency_ms / (1000 * validated_count), 2) if validated_count > 0 else None

        strategy_benchmark = StrategyBenchmark(
            http_coverage=round(http_valid / max(1, target_skus), 3),
            http_numerator=http_valid,
            http_denominator=target_skus,
            playwright_coverage=round(pw_valid / max(1, target_skus), 3),
            playwright_numerator=pw_valid,
            playwright_denominator=target_skus,
            firecrawl_coverage=round(fc_valid / max(1, target_skus), 3),
            firecrawl_numerator=fc_valid,
            firecrawl_denominator=target_skus,
            adapter_coverage=round(adapt_valid / max(1, target_skus), 3),
            adapter_numerator=adapt_valid,
            adapter_denominator=target_skus,
            best_strategy=best_strat,
            cost_per_successful_sku=cost_per_sku
        )

        # Hierarchical Failures
        block_count = 0
        captcha_count = 0
        timeout_count = 0
        failure_breakdown: Dict[str, int] = {}
        hierarchical_failures: List[Dict[str, Any]] = []

        for r in sku_results:
            if r.failure:
                reason_str = r.failure.specific_reason.value if hasattr(r.failure, "specific_reason") else str(r.failure.reason)
                cat_str = r.failure.category.value if hasattr(r.failure, "category") else "UNKNOWN"
                stage_str = r.failure.stage.value if hasattr(r.failure, "stage") else "URL_REACHABILITY"
                failure_breakdown[reason_str] = failure_breakdown.get(reason_str, 0) + 1
                hierarchical_failures.append({
                    "sku_id": r.sku_id,
                    "category": cat_str,
                    "specific_reason": reason_str,
                    "stage": stage_str,
                    "human_reason": r.failure.failure_reason_human
                })
                if reason_str in ("BOT_PROTECTION", "RATE_LIMITED", "HTTP_429_RATE_LIMITED"):
                    block_count += 1
                elif reason_str in ("CAPTCHA", "CAPTCHA_CHALLENGE"):
                    captcha_count += 1
                elif "TIMEOUT" in reason_str:
                    timeout_count += 1

        block_rate = round(block_count / max(1, total_attempted), 3) if total_attempted else 0.0
        captcha_rate = round(captcha_count / max(1, total_attempted), 3) if total_attempted else 0.0
        timeout_rate = round(timeout_count / max(1, total_attempted), 3) if total_attempted else 0.0

        main_failure = None
        if failure_breakdown:
            main_failure = max(failure_breakdown.items(), key=lambda x: x[1])[0]

        # Template & Category Breakdown
        template_stats = defaultdict(lambda: {"total": 0, "valid": 0})
        category_stats = defaultdict(lambda: {"total": 0, "valid": 0})

        for r in sku_results:
            tmpl = r.product_template_id or (r.product.product_template_id if r.product else "tmpl_unknown")
            cat = r.category or (r.product.category if r.product else "General")
            template_stats[tmpl]["total"] += 1
            category_stats[cat]["total"] += 1
            if r.status == "SUCCESS":
                template_stats[tmpl]["valid"] += 1
                category_stats[cat]["valid"] += 1

        template_breakdown = {
            t: {"total": d["total"], "valid": d["valid"], "coverage": round(d["valid"] / d["total"], 2)}
            for t, d in template_stats.items()
        }
        category_breakdown = {
            c: {"total": d["total"], "valid": d["valid"], "coverage": round(d["valid"] / d["total"], 2)}
            for c, d in category_stats.items()
        }

        # Strategy breakdown
        strategy_breakdown: Dict[str, int] = {}
        for r in sku_results:
            if r.effective_strategy:
                strategy_breakdown[r.effective_strategy] = strategy_breakdown.get(r.effective_strategy, 0) + 1

        iso_country = getattr(target_config, "iso_country", "US")

        return TargetCrawlReport(
            target_id=target_config.target_id,
            retailer=target_config.retailer,
            brand_name=target_config.brand_name,
            country=target_config.country,
            iso_country=iso_country,
            target_skus=target_skus,
            discovered=discovered_count,
            http_success_count=http_success_count,
            browser_success_count=browser_success_count,
            extracted_count=extracted_count,
            validated_count=validated_count,
            partial_count=partial_count,
            failed_count=failed_count,
            discovery_rate=discovery_rate,
            page_load_success_rate=page_load_rate,
            extraction_success_rate=extraction_rate,
            validation_success_rate=validation_rate,
            field_completeness_avg=avg_completeness,
            sku_coverage=sku_coverage,
            block_rate=block_rate,
            captcha_rate=captcha_rate,
            timeout_rate=timeout_rate,
            sample_size=total_attempted,
            validated_sample_size=validated_count,
            observed_coverage_statement=f"{round(sku_coverage * 100, 1)}% observed coverage in {total_attempted} tested SKUs",
            confidence_level=0.95,
            cost_telemetry=cost_telemetry,
            strategy_benchmark=strategy_benchmark,
            avg_latency_ms=avg_latency,
            median_latency_ms=median_latency,
            p95_latency_ms=p95_latency,
            avg_retries=avg_retries,
            primary_strategy=getattr(target_config, "preferred_strategy", "HTTP"),
            strategy_success_breakdown=strategy_breakdown,
            main_failure_reason=main_failure,
            failure_breakdown=failure_breakdown,
            hierarchical_failures=hierarchical_failures,
            template_breakdown=template_breakdown,
            category_breakdown=category_breakdown,
            sku_results=sku_results
        )
