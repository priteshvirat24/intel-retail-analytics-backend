from typing import Tuple
from app.models.crawl_result import TargetCrawlReport
from app.models.retailer import RetailerProfile


class CapabilityScorer:
    """Evaluates retailer capability grades (A-E), primary categories, and diagnoses root causes."""

    @classmethod
    def score_and_diagnose(cls, report: TargetCrawlReport) -> TargetCrawlReport:
        coverage = report.sku_coverage

        # 1. Capability Grade
        if coverage >= 0.95:
            grade = "A"
        elif coverage >= 0.85:
            grade = "B"
        elif coverage >= 0.70:
            grade = "C"
        elif coverage >= 0.50:
            grade = "D"
        else:
            grade = "E"

        report.capability_grade = grade

        # 2. Capability Category
        if report.block_rate >= 0.40 or report.captcha_rate >= 0.30:
            category = "BLOCKED"
        elif report.discovery_rate < 0.50:
            category = "DISCOVERY_LIMITED"
        elif report.browser_success_count > report.http_success_count:
            category = "BROWSER_REQUIRED"
        elif report.strategy_success_breakdown.get("ADAPTER", 0) > 0:
            category = "CUSTOM_ADAPTER_REQUIRED"
        elif report.http_success_count > 0 and report.validated_count >= (report.target_skus * 0.7):
            category = "HTTP_ONLY"
        else:
            category = "EXTRACTION_LIMITED"

        report.capability_category = category

        # 3. Actionable Diagnosis & Recommendation
        diagnosis_lines = []
        rec = "HTTP-first standard crawling."

        if coverage >= 0.90:
            diagnosis_lines.append(f"High reliability extraction achieved ({round(coverage * 100)}% coverage). Standard HTTP extraction is highly effective.")
            rec = "Fast HTTP-first pipeline with standard concurrency."
        else:
            diagnosis_lines.append(f"Coverage is at {round(coverage * 100)}% ({report.validated_count}/{report.target_skus} valid SKUs).")
            if report.block_rate > 0.15:
                diagnosis_lines.append(f"- Anti-bot / rate limiting triggered on {round(report.block_rate * 100)}% of requests.")
                rec = "Playwright with stealth headers, conservative concurrency (1-2 concurrent), and higher request delays."
            if report.captcha_rate > 0.10:
                diagnosis_lines.append(f"- CAPTCHA challenges detected on {round(report.captcha_rate * 100)}% of attempts.")
            if report.failure_breakdown.get("JAVASCRIPT_REQUIRED", 0) > 0 or report.failure_breakdown.get("EMPTY_RESPONSE", 0) > 0:
                diagnosis_lines.append("- Dynamic JavaScript rendering is required for catalog hydration.")
                rec = "Playwright Chromium headless crawler with full DOM hydration."
            if report.failure_breakdown.get("PRICE_MISSING", 0) > 0 or report.failure_breakdown.get("EXTRACTION_FAILURE", 0) > 0:
                diagnosis_lines.append("- Generic extractors failed to locate pricing or SKU identifiers in DOM/JSON-LD.")
                rec = "Specialized Retailer Adapter to parse proprietary hydration payload."

        report.failure_diagnosis_summary = " ".join(diagnosis_lines)
        report.recommended_strategy = rec
        report.notes = f"Grade {grade} ({category}). Discovered: {report.discovered}/{report.target_skus}, Validated: {report.validated_count}."

        return report

    @classmethod
    def generate_retailer_profile(cls, report: TargetCrawlReport) -> RetailerProfile:
        """Generates dynamic strategy profile based on empirical performance."""
        total_skus = max(1, len(report.sku_results))
        http_rate = round(report.http_success_count / total_skus, 2)
        browser_rate = round(report.browser_success_count / total_skus, 2)

        preferred = "http"
        concurrency = 3
        delay = 1.0

        if browser_rate > http_rate:
            preferred = "playwright"
            concurrency = 2
            delay = 2.0

        if report.block_rate > 0.2:
            concurrency = 1
            delay = 3.5

        return RetailerProfile(
            retailer=report.retailer,
            country=report.country,
            preferred_strategy=preferred,
            http_success_rate=http_rate,
            browser_success_rate=browser_rate,
            preferred_concurrency=concurrency,
            preferred_delay_sec=delay,
            known_failures=list(report.failure_breakdown.keys()),
            capability_grade=report.capability_grade,
            capability_category=report.capability_category
        )
