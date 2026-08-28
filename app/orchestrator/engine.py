import asyncio
import uuid
import time
from typing import List, Dict, Any, Optional, Union
from app.models.registry import CanonicalTarget
from app.models.retailer import RetailerTargetConfig
from app.models.crawl_result import SkuCrawlResult, CrawlAttempt, TargetCrawlReport
from app.models.product import NormalizedProduct
from app.models.failure import FailureDiagnosis, FailureCategory, SpecificReason, CrawlStage, StageStatus
from app.discovery import ProductDiscoveryEngine
from app.crawlers.http import HttpCrawler
from app.crawlers.playwright import PlaywrightCrawler
from app.crawlers.firecrawl import FirecrawlCrawler
from app.crawlers.scrapy_bridge import ScrapyCrawlerBridge
from app.extraction.engine import ProductExtractionEngine
from app.extraction.template import ProductTemplateIdentifier
from app.retailers.registry import RetailerAdapterRegistry
from app.orchestrator.retry import RetryPolicy
from app.orchestrator.strategy import AdaptiveStrategyController
from app.orchestrator.scheduler import CrawlScheduler
from app.orchestrator.session import SessionManager
from app.evaluation.failures import FailureClassifier
from app.evaluation.metrics import MetricsCalculator
from app.evaluation.scoring import CapabilityScorer
from app.evidence.store import EvidenceStore


class CrawlOrchestrator:
    """Production-grade Multi-Site Crawl Orchestrator for empirical SKU data extraction."""

    def __init__(
        self,
        evidence_store: Optional[EvidenceStore] = None,
        scheduler: Optional[CrawlScheduler] = None,
        session_manager: Optional[SessionManager] = None,
        headful: bool = False
    ):
        self.evidence_store = evidence_store or EvidenceStore()
        self.scheduler = scheduler or CrawlScheduler()
        self.session_manager = session_manager or SessionManager()
        self.headful = headful

    async def crawl_target(
        self,
        target_config: Union[CanonicalTarget, RetailerTargetConfig],
        limit: int = 20,
        forced_strategy: Optional[str] = None,
        explicit_urls: Optional[List[str]] = None
    ) -> TargetCrawlReport:
        """Executes complete 7-stage discovery, crawling, extraction, validation, and evaluation for a retailer target."""
        target_limit = limit
        if hasattr(target_config, "max_test_skus"):
            target_limit = min(limit, target_config.max_test_skus)

        candidate_records: List[Dict[str, Any]] = []

        # 1. Product Discovery
        if explicit_urls:
            candidate_records = [{"url": u, "category": "Explicit", "sku_id": f"sku_{i+1:03d}"} for i, u in enumerate(explicit_urls[:target_limit])]
            discovery_msg = f"Using {len(candidate_records)} explicitly provided URLs."
        else:
            discovery_engine = ProductDiscoveryEngine(target_config)
            candidate_records, is_limited, discovery_msg = await discovery_engine.discover_products(limit=target_limit)

        print(f"   [{target_config.target_id}] Discovery complete: found {len(candidate_records)} URLs ({discovery_msg})", flush=True)

        if not candidate_records:
            fail = FailureDiagnosis(
                category=FailureCategory.SCHEMA,
                specific_reason=SpecificReason.PRODUCT_SCHEMA_NOT_FOUND,
                stage=CrawlStage.DISCOVERY,
                failure_reason_human=discovery_msg,
                is_recoverable=False
            )
            report = TargetCrawlReport(
                target_id=target_config.target_id,
                retailer=target_config.retailer,
                brand_name=target_config.brand_name,
                country=target_config.country,
                iso_country=getattr(target_config, "iso_country", "US"),
                target_skus=target_limit,
                discovered=0,
                failed_count=target_limit,
                sku_coverage=0.0,
                main_failure_reason="DISCOVERY_FAILURE",
                failure_breakdown={"DISCOVERY_FAILURE": target_limit},
                failure_diagnosis_summary=discovery_msg,
                capability_grade="E",
                capability_category="DISCOVERY_LIMITED",
                notes=discovery_msg
            )
            return report

        # 2. Setup domain rate limiter
        rate_limit = getattr(target_config, "rate_limit", 1.0)
        max_conc = getattr(target_config, "max_concurrency", 2)
        limiter = self.scheduler.get_limiter(
            domain=target_config.domain,
            max_concurrency=max_conc,
            requests_per_second=rate_limit,
            base_delay_sec=1.0 / max(0.1, rate_limit)
        )

        # 3. Initialize Crawlers & Extractors
        http_crawler = HttpCrawler(target_config)
        playwright_crawler = PlaywrightCrawler(target_config, headless=not self.headful)
        firecrawl_crawler = FirecrawlCrawler(target_config)
        scrapy_crawler = ScrapyCrawlerBridge(target_config)
        extraction_engine = ProductExtractionEngine(target_config)
        strategy_controller = AdaptiveStrategyController(target_config)
        retry_policy = RetryPolicy(max_retries=2)
        retailer_adapter = RetailerAdapterRegistry.get_adapter(target_config)

        # 4. Crawl all discovered SKUs concurrently (throttled by DomainRateLimiter)
        async def _crawl_single_sku(rec: Dict[str, Any], sku_index: int) -> SkuCrawlResult:
            url = rec["url"]
            category = rec.get("category", "General")
            sku_id = rec.get("sku_id") or f"sku_{sku_index + 1:03d}"

            result = SkuCrawlResult(
                sku_id=sku_id,
                target_id=target_config.target_id,
                retailer=target_config.retailer,
                country=target_config.country,
                source_url=url,
                category=category,
                primary_strategy=forced_strategy or strategy_controller.select_initial_strategy()
            )
            
            # Stage 1: Discovery
            result.stage_statuses[CrawlStage.DISCOVERY.value] = StageStatus.SUCCESS.value
            result.discovery_success = True

            current_strategy = result.primary_strategy
            attempt_number = 0
            start_total_time = time.time()

            while attempt_number < 2:
                attempt_number += 1
                await limiter.acquire()

                try:
                    strat_start = time.time()
                    if current_strategy == "PLAYWRIGHT":
                        resp = await playwright_crawler.fetch(url)
                        browser_secs = round(time.time() - strat_start, 2)
                    elif current_strategy == "FIRECRAWL":
                        resp = await firecrawl_crawler.fetch(url)
                        browser_secs = round(time.time() - strat_start, 2)
                    elif current_strategy == "SCRAPY":
                        resp = await scrapy_crawler.fetch(url)
                        browser_secs = 0.0
                    else:
                        resp = await http_crawler.fetch(url)
                        browser_secs = 0.0

                    byte_len = len(resp.html.encode("utf-8")) if resp.html else (len(resp.markdown.encode("utf-8")) if resp.markdown else 0)

                    attempt = CrawlAttempt(
                        attempt_number=attempt_number,
                        strategy=current_strategy,
                        status_code=resp.status_code,
                        response_time_ms=resp.response_time_ms,
                        browser_seconds=browser_secs,
                        bytes_received=byte_len,
                        success=(resp.status_code == 200 and not resp.is_blocked and not resp.is_captcha),
                        headers=resp.headers,
                        error_message=resp.error_message
                    )

                    self.evidence_store.save_attempt(
                        retailer=target_config.retailer,
                        country=target_config.country,
                        sku_id=sku_id,
                        attempt=attempt,
                        raw_html=resp.html,
                        raw_markdown=resp.markdown,
                        screenshot_bytes=resp.screenshot_bytes
                    )
                    result.attempts.append(attempt)
                    result.final_url = resp.final_url
                    result.browser_seconds_total += browser_secs
                    result.bytes_received_total += byte_len

                    # Stage 2: URL Reachability
                    if resp.status_code != 0:
                        result.stage_statuses[CrawlStage.URL_REACHABILITY.value] = StageStatus.SUCCESS.value
                    else:
                        result.stage_statuses[CrawlStage.URL_REACHABILITY.value] = StageStatus.FAILED.value

                    # Stage 3: Content Availability
                    content_body = resp.html or resp.markdown or ""
                    is_content_available = (
                        resp.status_code == 200 and
                        not resp.is_blocked and
                        not resp.is_captcha and
                        len(content_body.strip()) >= 200
                    )

                    if is_content_available:
                        limiter.throttle_down()
                        result.stage_statuses[CrawlStage.CONTENT_AVAILABILITY.value] = StageStatus.SUCCESS.value

                        if current_strategy == "PLAYWRIGHT":
                            result.browser_success = True
                        elif current_strategy == "FIRECRAWL":
                            result.firecrawl_success = True
                        else:
                            result.http_success = True

                        # Stage 4: Product Identification (Structural Template)
                        template_id = ProductTemplateIdentifier.identify_template(resp.html or resp.markdown or "")
                        result.product_template_id = template_id

                        if template_id != "tmpl_empty_shell":
                            result.stage_statuses[CrawlStage.PRODUCT_IDENTIFICATION.value] = StageStatus.SUCCESS.value
                        else:
                            result.stage_statuses[CrawlStage.PRODUCT_IDENTIFICATION.value] = StageStatus.FAILED.value

                        # Stage 5: Extraction
                        custom_res = None
                        if retailer_adapter:
                            try:
                                custom_res = retailer_adapter.extract_custom(resp.html, resp.final_url)
                            except Exception:
                                pass

                        product, extract_err = extraction_engine.extract_product(
                            html=resp.html,
                            url=resp.final_url,
                            crawler_strategy=current_strategy,
                            custom_adapter_result=custom_res,
                            markdown=resp.markdown
                        )

                        if product:
                            result.stage_statuses[CrawlStage.EXTRACTION.value] = StageStatus.SUCCESS.value
                            result.extraction_success = True
                            product.product_template_id = template_id
                            product.category = category
                            result.product = product
                            result.effective_strategy = current_strategy

                            # Stage 6: Field Validation
                            if product.validation:
                                if product.validation.title_valid:
                                    result.stage_statuses[CrawlStage.FIELD_VALIDATION.value] = StageStatus.SUCCESS.value
                                else:
                                    result.stage_statuses[CrawlStage.FIELD_VALIDATION.value] = StageStatus.PARTIAL_SUCCESS.value

                                # Stage 7: Product Validation
                                if product.validation.is_valid_sku:
                                    result.stage_statuses[CrawlStage.PRODUCT_VALIDATION.value] = StageStatus.SUCCESS.value
                                    result.status = "SUCCESS"
                                    result.validation_success = True
                                    break
                                else:
                                    result.stage_statuses[CrawlStage.PRODUCT_VALIDATION.value] = StageStatus.PARTIAL_SUCCESS.value
                                    result.status = "PARTIAL_SUCCESS"
                                    failure_diag = FailureDiagnosis(
                                        category=FailureCategory.VALIDATION,
                                        specific_reason=SpecificReason.REQUIRED_FIELD_MISSING,
                                        stage=CrawlStage.PRODUCT_VALIDATION,
                                        failure_reason_human="Product data was partially extracted but failed composite valid SKU requirements.",
                                        is_recoverable=True
                                    )
                                    result.failure = failure_diag
                                    break
                            else:
                                result.stage_statuses[CrawlStage.FIELD_VALIDATION.value] = StageStatus.FAILED.value
                                result.stage_statuses[CrawlStage.PRODUCT_VALIDATION.value] = StageStatus.FAILED.value
                                break
                        else:
                            result.stage_statuses[CrawlStage.EXTRACTION.value] = StageStatus.FAILED.value
                            failure_diag = FailureClassifier.classify_extraction_failure(
                                extraction_err=extract_err,
                                raw_html=resp.html,
                                retry_count=attempt_number - 1
                            )
                            attempt.failure_diagnosis = failure_diag
                            result.failure = failure_diag

                            should_esc, next_strat, esc_reason = strategy_controller.should_escalate(
                                current_strategy, resp, failure_diag
                            )
                            if should_esc and next_strat and attempt_number < 2:
                                current_strategy = next_strat
                                result.escalation_reason = esc_reason
                                continue
                            break
                    else:
                        result.stage_statuses[CrawlStage.CONTENT_AVAILABILITY.value] = StageStatus.FAILED.value
                        limiter.throttle_up()
                        failure_diag = FailureClassifier.classify_crawl_failure(
                            response=resp,
                            stage=CrawlStage.CONTENT_AVAILABILITY if resp.status_code != 0 else CrawlStage.URL_REACHABILITY,
                            retry_count=attempt_number - 1
                        )
                        attempt.failure_diagnosis = failure_diag
                        result.failure = failure_diag

                        should_esc, next_strat, esc_reason = strategy_controller.should_escalate(
                            current_strategy, resp, failure_diag
                        )
                        if should_esc and next_strat and attempt_number < 2:
                            current_strategy = next_strat
                            result.escalation_reason = esc_reason
                            continue

                        if retry_policy.should_retry(attempt_number, resp.status_code, failure_diag.specific_reason):
                            await retry_policy.backoff_sleep(attempt_number)
                            continue
                        else:
                            break

                finally:
                    limiter.release()

            result.total_latency_ms = round((time.time() - start_total_time) * 1000, 2)
            status_tag = "VALIDATED" if result.status == "SUCCESS" else f"FAILED ({result.failure.specific_reason.value if result.failure else 'unknown'})"
            print(f"      [SKU {sku_index+1:02d}/{len(candidate_records):02d}] {status_tag} - {result.source_url[:60]}... [{result.total_latency_ms}ms]", flush=True)
            self.evidence_store.save_sku_result(result)
            return result

        sku_tasks = [_crawl_single_sku(rec, idx) for idx, rec in enumerate(candidate_records)]
        sku_results = await asyncio.gather(*sku_tasks)

        # 5. Evaluate Metrics and Capability Scores
        report = MetricsCalculator.calculate_target_metrics(
            target_config=target_config,
            target_skus=target_limit,
            discovered_count=len(candidate_records),
            sku_results=sku_results
        )
        report = CapabilityScorer.score_and_diagnose(report)

        return report
