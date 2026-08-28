"""
Standard Scraping Provider Base Interfaces and Data Models.
Enables pluggable, independent crawling and scraping engines (Bright Data, Apify, etc.).
"""
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List, Tuple
from pydantic import BaseModel, Field
from datetime import datetime, timezone
from app.models.registry import CanonicalTarget


class ProviderTargetResult(BaseModel):
    """Normalized empirical result of running a scraping provider against a target."""
    target_id: str
    retailer: str
    country: str
    domain: str
    target_product: str = "Laptop / Notebook Computer"
    
    # High-level outcome
    can_scrape: str = "NO"  # "YES" | "NO"
    status: str = "FAILURE"  # "SUCCESS" | "FAILURE"
    
    # 4 Core Measurable Stages
    access_success: bool = False       # PAGE_FETCH_SUCCESS
    discovery_success: bool = False    # PRODUCT_DISCOVERED
    extraction_success: bool = False   # PRODUCT_EXTRACTED
    validation_success: bool = False   # PRODUCT_VALIDATED
    
    # Stage & Failure Tracking
    failure_stage: Optional[str] = None    # ACCESS, DISCOVERY, EXTRACTION, VALIDATION, ACTOR_EXECUTION, etc.
    failure_category: Optional[str] = None # ACCESS_FAILURE, WAF_OR_ANTI_BOT, etc.
    failure_reason: Optional[str] = None   # Detailed taxonomy reason
    failure_message: Optional[str] = None  # Human-readable error message
    
    # Strategy & Execution Metadata
    provider_name: str = "unknown"
    strategy: str = "DEFAULT"
    method: str = "DEFAULT"
    actor_id: Optional[str] = None
    actor_run_id: Optional[str] = None
    dataset_id: Optional[str] = None
    execution_duration_sec: float = 0.0
    retry_count: int = 0
    pages_crawled: int = 0
    crawl_depth: int = 1
    http_status: Optional[int] = None
    redirects: List[str] = Field(default_factory=list)
    
    # URLs
    initial_url: Optional[str] = None
    discovered_urls: List[str] = Field(default_factory=list)
    final_product_url: Optional[str] = None
    
    # Product Data & Validation
    title: Optional[str] = None
    brand: Optional[str] = None
    specs: Dict[str, Any] = Field(default_factory=dict)
    extracted_data: Dict[str, Any] = Field(default_factory=dict)
    validation_result: Dict[str, Any] = Field(default_factory=dict)
    
    # Evidence
    evidence_html_path: Optional[str] = None
    evidence_summary_path: Optional[str] = None
    raw_response_text: Optional[str] = None
    
    timestamp: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


class ScrapingProvider(ABC):
    """Abstract interface for independent scraping providers."""
    
    name: str = "base"

    @abstractmethod
    def health_check(self) -> Tuple[bool, str, Dict[str, Any]]:
        """Verify API credentials, service reachability, and capability."""
        pass

    @abstractmethod
    async def crawl_and_scrape(self, target: CanonicalTarget) -> ProviderTargetResult:
        """
        Executes the full end-to-end workflow for a canonical target:
        Target -> Access -> Discover -> Crawl -> Extract -> Validate
        """
        pass
