from typing import Dict, Any, Optional
from app.orchestrator.strategies.base import BaseCrawlStrategy
from app.adapters import AmazonAdapter, BoulangerAdapter
from app.crawlers.base import CrawlerResponse


class AdapterStrategy(BaseCrawlStrategy):
    """Custom target adapter extraction strategy for bespoke DOM & state parsing."""

    @property
    def strategy_name(self) -> str:
        return "ADAPTER"

    async def execute(
        self,
        url: str,
        timeout_sec: float = 30.0,
        headers: Optional[Dict[str, str]] = None,
        context: Optional[Dict[str, Any]] = None
    ) -> CrawlerResponse:
        # Adapter strategy works on existing response context or executes custom adapter
        html = (context or {}).get("html", "")
        retailer = self.target_config.retailer.lower()

        adapter = None
        if "amazon" in retailer:
            adapter = AmazonAdapter(self.target_config)
        elif "boulanger" in retailer:
            adapter = BoulangerAdapter(self.target_config)

        if adapter and html:
            extracted = adapter.extract_custom(html, url)
            if extracted:
                return CrawlerResponse(
                    url=url,
                    final_url=url,
                    status_code=200,
                    html=html,
                    strategy="ADAPTER",
                    success=True,
                    metadata={"adapter_extracted": extracted}
                )

        return CrawlerResponse(
            url=url,
            final_url=url,
            status_code=0,
            strategy="ADAPTER",
            success=False,
            error_message=f"No suitable adapter found or adapter extraction failed for {retailer}"
        )
