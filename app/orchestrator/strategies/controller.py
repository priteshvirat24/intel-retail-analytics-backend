import os
from typing import Dict, Any, Optional, List, Tuple
from app.models.retailer import RetailerTargetConfig
from app.crawlers.base import CrawlerResponse
from app.models.failure import FailureDiagnosis, SpecificReason, CrawlStage
from app.evaluation.failures import FailureClassifier
from app.orchestrator.strategies.base import BaseCrawlStrategy
from app.orchestrator.strategies.http_strategy import HttpStrategy
from app.orchestrator.strategies.playwright_strategy import PlaywrightStrategy
from app.orchestrator.strategies.firecrawl_strategy import FirecrawlStrategy
from app.orchestrator.strategies.adapter_strategy import AdapterStrategy
from app.crawlers.proxy import ProxyProvider, ProxyConfig


class StrategyController:
    """
    Dynamic Multi-Strategy Controller.
    Executes and sequences crawler strategies (HTTP, PLAYWRIGHT, FIRECRAWL, ADAPTER)
    with support for fallback escalation and independent same-URL matrix comparison.
    """

    def __init__(
        self,
        target_config: RetailerTargetConfig,
        mode: str = "auto",
        headful: bool = False,
        firecrawl_base_url: Optional[str] = None
    ):
        self.target_config = target_config
        self.mode = mode.lower()
        self.headful = headful
        self.firecrawl_base_url = firecrawl_base_url or os.getenv("FIRECRAWL_BASE_URL", "http://localhost:3008")
        self.proxy_config = ProxyProvider.get_proxy(getattr(target_config, "country", None))

        # Initialize strategy registry
        self.strategies: Dict[str, BaseCrawlStrategy] = {
            "HTTP": HttpStrategy(target_config),
            "PLAYWRIGHT": PlaywrightStrategy(target_config, headless=not headful),
            "FIRECRAWL": FirecrawlStrategy(target_config, base_url=self.firecrawl_base_url),
            "ADAPTER": AdapterStrategy(target_config)
        }

    def get_strategy_chain(self) -> List[str]:
        """Determines the ordered sequence of strategies to attempt."""
        if self.mode == "http":
            return ["HTTP"]
        elif self.mode == "playwright":
            return ["PLAYWRIGHT"]
        elif self.mode == "firecrawl":
            return ["FIRECRAWL"]
        elif self.mode == "adapter":
            return ["HTTP", "ADAPTER"]
        elif self.mode == "compare":
            return ["HTTP", "PLAYWRIGHT", "FIRECRAWL"]

        # Mode "auto": Dynamic escalation chain
        chain = ["HTTP", "PLAYWRIGHT", "FIRECRAWL"]
        if hasattr(self.target_config, "adapter_available") and getattr(self.target_config, "adapter_available"):
            chain.append("ADAPTER")
        return chain

    async def execute_chain(
        self,
        url: str,
        timeout_sec: float = 30.0,
        headers: Optional[Dict[str, str]] = None
    ) -> Tuple[CrawlerResponse, List[Dict[str, Any]], Optional[FailureDiagnosis]]:
        """
        Executes the strategy chain for a given SKU URL.
        Returns:
            (final_successful_or_last_response, attempt_chain_history, final_failure_diagnosis)
        """
        chain = self.get_strategy_chain()
        attempt_history: List[Dict[str, Any]] = []
        last_response: Optional[CrawlerResponse] = None
        last_diagnosis: Optional[FailureDiagnosis] = None

        for strat_name in chain:
            strat = self.strategies.get(strat_name)
            if not strat:
                continue

            # Execute the strategy
            try:
                response = await strat.execute(
                    url=url,
                    timeout_sec=timeout_sec,
                    headers=headers,
                    context={
                        "last_response": last_response,
                        "last_failure_reason": last_diagnosis.specific_reason.value if last_diagnosis else None,
                        "proxy_config": self.proxy_config
                    }
                )
            except Exception as e:
                response = CrawlerResponse(
                    url=url,
                    final_url=url,
                    status_code=0,
                    strategy=strat_name,
                    success=False,
                    error_message=str(e),
                    failure_reason="UNKNOWN_FAILURE",
                    provider_failure_reason=str(e)
                )

            last_response = response
            diagnosis = FailureClassifier.classify_crawl_failure(response)
            last_diagnosis = diagnosis

            attempt_record = {
                "strategy": strat_name,
                "status_code": response.status_code,
                "latency_ms": response.response_time_ms,
                "bytes_received": response.bytes_received,
                "success": response.success and response.status_code == 200 and len(response.html or response.markdown or "") > 200 and not response.is_blocked and not response.is_captcha,
                "specific_reason": diagnosis.specific_reason.value if diagnosis else None,
                "failure_category": diagnosis.category.value if diagnosis else None,
                "anti_bot_vendor": diagnosis.anti_bot_vendor if diagnosis else None,
                "error_message": response.error_message or (diagnosis.failure_reason_human if diagnosis else None)
            }
            attempt_history.append(attempt_record)

            # In compare mode, do NOT stop on first success: run all strategies
            if self.mode == "compare":
                continue

            # In auto mode, check if this attempt yielded valid, unblocked structural content
            if attempt_record["success"]:
                return response, attempt_history, None

            # If failure is non-recoverable (like 404 Not Found), do not waste further browser/firecrawl cycles
            if diagnosis.specific_reason in (SpecificReason.HTTP_404_NOT_FOUND, SpecificReason.HTTP_410_GONE):
                break

        return last_response, attempt_history, last_diagnosis

    @classmethod
    def determine_best_strategy(cls, attempts: List[Dict[str, Any]]) -> Tuple[Optional[str], Optional[str]]:
        """
        Determines first_successful_strategy and best_strategy based on validation and latency.
        Returns: (first_successful_strategy, best_strategy)
        """
        successful = [a for a in attempts if a.get("validated_success") or a.get("success")]
        if not successful:
            return None, None

        first_successful = successful[0]["strategy"]
        
        # Best strategy: minimum latency among valid successes
        sorted_by_latency = sorted(successful, key=lambda a: a.get("latency_ms", 999999))
        best = sorted_by_latency[0]["strategy"]

        return first_successful, best
