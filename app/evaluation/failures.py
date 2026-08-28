"""
Hierarchical Failure Classifier.
Maps raw crawl responses, network exceptions, and extraction errors into
exact machine-readable failure categories, specific reasons, pipeline stages, and anti-bot vendor attribution.
"""
from typing import Optional, Dict, Any, Tuple
from app.models.failure import FailureCategory, SpecificReason, CrawlStage, FailureDiagnosis
from app.crawlers.base import CrawlerResponse


class FailureClassifier:
    """Classifies crawl, rendering, and extraction failures into exact hierarchical taxonomies."""

    @classmethod
    def detect_anti_bot_vendor(cls, html: str, headers: Dict[str, str], status: int) -> Optional[str]:
        """Identifies specific anti-bot protection vendor signatures."""
        h_str = (html or "").lower()
        hdr_str = " ".join(f"{k}:{v}" for k, v in headers.items()).lower() if headers else ""

        if "datadome" in h_str or "datadome" in hdr_str:
            return "DataDome"
        if "perimeterx" in h_str or "px-captcha" in h_str or "_px" in hdr_str or "human security" in h_str:
            return "PerimeterX / HUMAN"
        if "kasada" in h_str or "kpsdk" in hdr_str:
            return "Kasada"
        if "cf-ray" in hdr_str or "cloudflare" in h_str or "cf-turnstile" in h_str or "just a moment..." in h_str:
            if "turnstile" in h_str:
                return "Cloudflare Turnstile"
            return "Cloudflare WAF"
        if "akamai" in h_str or "akamai" in hdr_str or "ak_bmsc" in hdr_str:
            return "Akamai Bot Manager"
        if "robot check" in h_str or "amazon.com/errors/validatecaptcha" in h_str:
            return "Amazon Robot Check"
        if "recaptcha" in h_str or "g-recaptcha" in h_str:
            return "Google reCAPTCHA"
        if "hcaptcha" in h_str:
            return "hCaptcha"
        if "access denied" in h_str and status in (400, 403):
            return "Akamai Bot Manager"
        return None

    @classmethod
    def is_challenge_page(cls, html: str, status: int) -> Tuple[bool, Optional[str]]:
        """Determines if a page is a bot challenge / CAPTCHA."""
        h_str = (html or "").lower()
        if "recaptcha" in h_str or "g-recaptcha" in h_str or "hcaptcha" in h_str or "captcha" in h_str:
            return True, "CAPTCHA"
        if "cf-turnstile" in h_str or "turnstile" in h_str or "just a moment..." in h_str:
            return True, "WAF_CHALLENGE"
        if "datadome" in h_str or "perimeterx" in h_str:
            return True, "BOT_DETECTION"
        if status in (403, 429):
            return True, "HTTP_BLOCK"
        return False, None

    @classmethod
    def classify_crawl_failure(
        cls,
        response: CrawlerResponse,
        stage: CrawlStage = CrawlStage.URL_REACHABILITY,
        retry_count: int = 0
    ) -> FailureDiagnosis:
        status = response.status_code
        err = response.error_message or ""
        html = (response.html or "").lower()
        headers = response.headers or {}

        strat = response.strategy
        prov_reason = response.provider_failure_reason

        # 0. Firecrawl Specific Failures
        if response.failure_reason == "FIRECRAWL_SERVICE_UNAVAILABLE" or (strat == "FIRECRAWL" and "econnrefused" in err.lower()):
            return FailureDiagnosis(
                category=FailureCategory.NETWORK,
                specific_reason=SpecificReason.FIRECRAWL_SERVICE_UNAVAILABLE,
                stage=CrawlStage.URL_REACHABILITY,
                failure_reason_human="Self-hosted Firecrawl service is unreachable or offline.",
                http_status=status,
                retry_count=retry_count,
                last_error=err,
                source_strategy=strat,
                provider_failure_reason=prov_reason or "ECONNREFUSED",
                is_recoverable=False,
                recommended_escalation="PLAYWRIGHT"
            )

        if response.failure_reason == "FIRECRAWL_TIMEOUT" or (strat == "FIRECRAWL" and "timeout" in err.lower()):
            return FailureDiagnosis(
                category=FailureCategory.NETWORK,
                specific_reason=SpecificReason.FIRECRAWL_TIMEOUT,
                stage=CrawlStage.URL_REACHABILITY,
                failure_reason_human="Self-hosted Firecrawl scrape request timed out.",
                http_status=status,
                retry_count=retry_count,
                last_error=err,
                source_strategy=strat,
                provider_failure_reason=prov_reason or "ETIMEDOUT",
                is_recoverable=True,
                recommended_escalation="PLAYWRIGHT"
            )

        if response.failure_reason == "FIRECRAWL_INTERNAL_ERROR":
            return FailureDiagnosis(
                category=FailureCategory.NETWORK,
                specific_reason=SpecificReason.FIRECRAWL_INTERNAL_ERROR,
                stage=CrawlStage.URL_REACHABILITY,
                failure_reason_human=f"Self-hosted Firecrawl internal error: {err}",
                http_status=status,
                retry_count=retry_count,
                last_error=err,
                source_strategy=strat,
                provider_failure_reason=prov_reason or err,
                is_recoverable=True,
                recommended_escalation="PLAYWRIGHT"
            )

        # 0. Bright Data Specific Failures & Safety Caps
        if response.failure_reason == "BRIGHTDATA_SAFETY_CAP_REACHED" or "SAFETY CAP REACHED" in err:
            return FailureDiagnosis(
                category=FailureCategory.ACCESS,
                specific_reason=SpecificReason.BRIGHTDATA_SAFETY_CAP_REACHED,
                stage=CrawlStage.URL_REACHABILITY,
                failure_reason_human="Request halted by local Bright Data Cost Guard safety cap to prevent fees.",
                http_status=status,
                retry_count=retry_count,
                last_error=err,
                source_strategy=strat,
                provider_failure_reason="COST_GUARD_BLOCKED",
                is_recoverable=False,
                recommended_escalation="NONE"
            )

        if "Zone has reached usage limit" in html or "usage_limit_reached" in err or "client_10100" in str(headers) or "client_10100" in err:
            return FailureDiagnosis(
                category=FailureCategory.ACCESS,
                specific_reason=SpecificReason.BRIGHTDATA_USAGE_LIMIT_REACHED,
                stage=CrawlStage.URL_REACHABILITY,
                failure_reason_human="Bright Data zone reached usage/spending limit in dashboard (client_10100).",
                http_status=status or 502,
                retry_count=retry_count,
                last_error=err or "Zone has reached usage limit",
                source_strategy=strat,
                provider_failure_reason="client_10100: usage_limit_reached",
                is_recoverable=False,
                recommended_escalation="MODIFY_BRIGHTDATA_ZONE_LIMIT"
            )

        # 1. Anti-Bot / CAPTCHA Vendor Detection
        anti_bot_vendor = cls.detect_anti_bot_vendor(html, headers, status)

        if response.is_captcha or any(k in html for k in ["captcha", "robot check", "verify you are human", "cf-turnstile", "recaptcha"]):
            return FailureDiagnosis(
                category=FailureCategory.ACCESS,
                specific_reason=SpecificReason.CAPTCHA_CHALLENGE,
                stage=CrawlStage.CONTENT_AVAILABILITY,
                failure_reason_human=f"Crawl halted by automated challenge ({anti_bot_vendor or 'CAPTCHA'}).",
                http_status=status,
                retry_count=retry_count,
                last_error=err,
                source_strategy=strat,
                provider_failure_reason=prov_reason,
                anti_bot_vendor=anti_bot_vendor,
                is_recoverable=False,
                recommended_escalation="PLAYWRIGHT",
                details={"page_title_excerpt": html[:200], "vendor": anti_bot_vendor}
            )

        if response.is_blocked or status in (403, 429) or (status == 400 and anti_bot_vendor) or any(k in html for k in ["access denied", "blocked", "forbidden"]):
            specific = SpecificReason.HTTP_429_RATE_LIMITED if status == 429 else SpecificReason.BOT_PROTECTION
            category = FailureCategory.HTTP_STATUS if status == 429 else FailureCategory.ACCESS
            return FailureDiagnosis(
                category=category,
                specific_reason=specific,
                stage=CrawlStage.URL_REACHABILITY if status in (403, 429) else CrawlStage.CONTENT_AVAILABILITY,
                failure_reason_human=f"Request blocked by anti-bot protection ({anti_bot_vendor or 'WAF/Edge Guard'}). HTTP {status}.",
                http_status=status,
                retry_count=retry_count,
                last_error=err,
                source_strategy=strat,
                provider_failure_reason=prov_reason,
                anti_bot_vendor=anti_bot_vendor,
                is_recoverable=(status == 429),
                recommended_escalation="PLAYWRIGHT" if stage == CrawlStage.URL_REACHABILITY else "STRICT_THROTTLE",
                details={"http_status": status, "blocked_detected": True, "vendor": anti_bot_vendor}
            )

        # 2. HTTP Status Code Errors
        if status == 404:
            return FailureDiagnosis(
                category=FailureCategory.HTTP_STATUS,
                specific_reason=SpecificReason.HTTP_404_NOT_FOUND,
                stage=CrawlStage.URL_REACHABILITY,
                failure_reason_human="Product URL returned HTTP 404 Not Found.",
                http_status=404,
                retry_count=retry_count,
                last_error=err,
                source_strategy=strat,
                provider_failure_reason=prov_reason,
                is_recoverable=False
            )

        if status == 410:
            return FailureDiagnosis(
                category=FailureCategory.HTTP_STATUS,
                specific_reason=SpecificReason.HTTP_410_GONE,
                stage=CrawlStage.URL_REACHABILITY,
                failure_reason_human="Product URL returned HTTP 410 Gone (Permanently Delisted).",
                http_status=410,
                retry_count=retry_count,
                last_error=err,
                source_strategy=strat,
                is_recoverable=False
            )

        if status >= 500:
            return FailureDiagnosis(
                category=FailureCategory.HTTP_STATUS,
                specific_reason=SpecificReason.HTTP_5XX_SERVER_ERROR,
                stage=CrawlStage.URL_REACHABILITY,
                failure_reason_human=f"Retailer server returned HTTP {status} Server Error.",
                http_status=status,
                retry_count=retry_count,
                last_error=err,
                source_strategy=strat,
                is_recoverable=True,
                recommended_escalation="RETRY_WITH_BACKOFF"
            )

        # 3. Connection / DNS / Timeouts
        if "connect" in err.lower() or "dns" in err.lower() or "getaddrinfo" in err.lower():
            return FailureDiagnosis(
                category=FailureCategory.NETWORK,
                specific_reason=SpecificReason.DNS_RESOLUTION_FAILED,
                stage=CrawlStage.URL_REACHABILITY,
                failure_reason_human=f"DNS resolution or host connection failed: {err}",
                http_status=status,
                retry_count=retry_count,
                last_error=err,
                source_strategy=strat,
                is_recoverable=True,
                recommended_escalation="RETRY_WITH_BACKOFF"
            )

        if "timeout" in err.lower() or "timed out" in err.lower():
            return FailureDiagnosis(
                category=FailureCategory.NETWORK,
                specific_reason=SpecificReason.CONNECTION_TIMEOUT,
                stage=CrawlStage.URL_REACHABILITY,
                failure_reason_human=f"Connection timed out: {err}",
                http_status=status,
                retry_count=retry_count,
                last_error=err,
                source_strategy=strat,
                is_recoverable=True,
                recommended_escalation="PLAYWRIGHT"
            )

        if "ssl" in err.lower() or "tls" in err.lower() or "certificate" in err.lower():
            return FailureDiagnosis(
                category=FailureCategory.NETWORK,
                specific_reason=SpecificReason.TLS_ERROR,
                stage=CrawlStage.URL_REACHABILITY,
                failure_reason_human=f"TLS/SSL handshake negotiation failed: {err}",
                http_status=status,
                retry_count=retry_count,
                last_error=err,
                source_strategy=strat,
                is_recoverable=False
            )

        # 4. Content / SPA / Empty Responses
        if not response.html or len(response.html.strip()) < 50:
            return FailureDiagnosis(
                category=FailureCategory.CONTENT,
                specific_reason=SpecificReason.EMPTY_RESPONSE,
                stage=CrawlStage.CONTENT_AVAILABILITY,
                failure_reason_human="Server returned an empty or zero-byte response body.",
                http_status=status,
                retry_count=retry_count,
                last_error=err,
                source_strategy=strat,
                is_recoverable=True,
                recommended_escalation="PLAYWRIGHT"
            )

        # Check for SPA Shell requiring JavaScript execution
        spa_indicators = [
            '<div id="root"></div>',
            '<div id="app"></div>',
            'please enable javascript',
            'you need to enable javascript to run this app',
            'enable javascript and reload the page'
        ]
        if any(ind in html for ind in spa_indicators) and len(html) < 2000:
            return FailureDiagnosis(
                category=FailureCategory.CONTENT,
                specific_reason=SpecificReason.JAVASCRIPT_REQUIRED,
                stage=CrawlStage.CONTENT_AVAILABILITY,
                failure_reason_human="Page returned client-side SPA shell; JavaScript rendering is mandatory.",
                http_status=status,
                retry_count=retry_count,
                last_error=err,
                source_strategy=strat,
                is_recoverable=True,
                recommended_escalation="PLAYWRIGHT"
            )

        # Default Reachability Failure
        return FailureDiagnosis(
            category=FailureCategory.NETWORK,
            specific_reason=SpecificReason.UNKNOWN_FAILURE,
            stage=stage,
            failure_reason_human=err or f"Unclassified failure with HTTP status {status}.",
            http_status=status,
            retry_count=retry_count,
            last_error=err,
            source_strategy=strat,
            is_recoverable=False
        )

    @classmethod
    def classify_extraction_failure(
        cls,
        reason_msg: str,
        stage: CrawlStage = CrawlStage.EXTRACTION,
        http_status: Optional[int] = 200,
        strategy: str = "HTTP"
    ) -> FailureDiagnosis:
        msg_lower = reason_msg.lower()

        if "conflict" in msg_lower:
            return FailureDiagnosis(
                category=FailureCategory.VALIDATION,
                specific_reason=SpecificReason.FIELD_CONFLICT,
                stage=CrawlStage.FIELD_VALIDATION,
                failure_reason_human=f"Critical field conflict across extraction sources: {reason_msg}",
                http_status=http_status,
                source_strategy=strategy,
                is_recoverable=False
            )

        if "missing" in msg_lower or "required" in msg_lower:
            return FailureDiagnosis(
                category=FailureCategory.VALIDATION,
                specific_reason=SpecificReason.REQUIRED_FIELD_MISSING,
                stage=CrawlStage.FIELD_VALIDATION,
                failure_reason_human=f"Mandatory schema field missing: {reason_msg}",
                http_status=http_status,
                source_strategy=strategy,
                is_recoverable=False
            )

        if "invalid" in msg_lower:
            return FailureDiagnosis(
                category=FailureCategory.VALIDATION,
                specific_reason=SpecificReason.FIELD_INVALID,
                stage=CrawlStage.FIELD_VALIDATION,
                failure_reason_human=f"Field failed semantic validation rules: {reason_msg}",
                http_status=http_status,
                source_strategy=strategy,
                is_recoverable=False
            )

        if "schema" in msg_lower or "no product data" in msg_lower:
            return FailureDiagnosis(
                category=FailureCategory.SCHEMA,
                specific_reason=SpecificReason.PRODUCT_SCHEMA_NOT_FOUND,
                stage=CrawlStage.EXTRACTION,
                failure_reason_human=f"No structural product schema (JSON-LD/Microdata/DOM) was discovered: {reason_msg}",
                http_status=http_status,
                source_strategy=strategy,
                is_recoverable=False
            )

        return FailureDiagnosis(
            category=FailureCategory.EXTRACTION,
            specific_reason=SpecificReason.EXTRACTION_FAILED,
            stage=CrawlStage.EXTRACTION,
            failure_reason_human=f"Extraction failed: {reason_msg}",
            http_status=http_status,
            source_strategy=strategy,
            is_recoverable=False
        )
