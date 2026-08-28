from typing import Optional, Tuple
from app.models.retailer import RetailerTargetConfig
from app.models.failure import FailureReason, FailureDiagnosis
from app.crawlers.base import CrawlerResponse


class AdaptiveStrategyController:
    """Controls adaptive crawler strategy selection, escalation, and learning profiles."""

    def __init__(self, target_config: RetailerTargetConfig):
        self.target_config = target_config

    def select_initial_strategy(self) -> str:
        """Determines the primary strategy based on target configuration and history."""
        preferred = self.target_config.preferred_strategy.lower()
        if preferred == "playwright":
            return "PLAYWRIGHT"
        elif preferred == "scrapy":
            return "SCRAPY"
        elif preferred == "custom_adapter":
            return "ADAPTER"
        return "HTTP"

    def should_escalate(
        self,
        current_strategy: str,
        response: CrawlerResponse,
        failure: Optional[FailureDiagnosis]
    ) -> Tuple[bool, Optional[str], Optional[str]]:
        """
        Evaluates whether crawl should escalate to a more capable strategy.
        Returns (should_escalate, next_strategy, escalation_reason).
        """
        reason_val = failure.specific_reason.value if failure and hasattr(failure, "specific_reason") else (failure.reason.value if failure and hasattr(failure, "reason") else "")

        # If already on Playwright, cannot escalate to browser
        if current_strategy == "PLAYWRIGHT":
            if reason_val in ("EXTRACTION_FAILED", "EXTRACTION_FAILURE"):
                return True, "ADAPTER", "Generic extractor failed on rendered DOM, escalating to custom adapter."
            return False, None, None

        # If on HTTP, evaluate escalation conditions
        if current_strategy in ("HTTP", "SCRAPY"):
            # 1. JS Required or Empty HTML shell
            if reason_val in ("JAVASCRIPT_REQUIRED", "EMPTY_RESPONSE"):
                return True, "PLAYWRIGHT", f"Escalating from {current_strategy} to PLAYWRIGHT due to {reason_val}."

            # 2. Block or Captcha
            if response.is_blocked or response.is_captcha or reason_val in ("BOT_PROTECTION", "CAPTCHA_CHALLENGE", "CAPTCHA"):
                return True, "PLAYWRIGHT", f"Escalating to PLAYWRIGHT with anti-detection headers due to {reason_val or 'BOT_BLOCK'}."

            # 3. Extraction failed completely on HTTP HTML
            if reason_val in ("EXTRACTION_FAILED", "EXTRACTION_FAILURE"):
                return True, "PLAYWRIGHT", "HTTP response lacked accessible schema; escalating to PLAYWRIGHT for client-side hydration."

            # 4. HTTP response status 0 (connection reset/timeout)
            if response.status_code == 0:
                return False, None, None  # Transient network error, retry HTTP rather than escalating browser immediately

        return False, None, None
