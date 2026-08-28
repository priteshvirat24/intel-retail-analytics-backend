from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime, timezone
from app.models.product import NormalizedProduct
from app.models.failure import FailureDiagnosis, CrawlStage, StageStatus


class CrawlAttempt(BaseModel):
    attempt_number: int
    strategy: str  # HTTP, PLAYWRIGHT, ADAPTER
    status_code: Optional[int] = None
    response_time_ms: float = 0.0
    browser_seconds: float = 0.0
    bytes_received: int = 0
    success: bool = False
    evidence_path: Optional[str] = None
    screenshot_path: Optional[str] = None
    headers: Dict[str, str] = Field(default_factory=dict)
    error_message: Optional[str] = None
    failure_diagnosis: Optional[FailureDiagnosis] = None
    timestamp: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


class SkuCrawlResult(BaseModel):
    sku_id: str
    target_id: str
    retailer: str
    country: str
    source_url: str
    final_url: Optional[str] = None
    category: Optional[str] = None
    product_template_id: Optional[str] = None

    # Status: SUCCESS, PARTIAL_SUCCESS, FAILED
    status: str = "FAILED"

    # 7 Measurable Stages
    stage_statuses: Dict[str, str] = Field(default_factory=lambda: {
        stage.value: StageStatus.FAILED.value for stage in CrawlStage
    })

    # Strategy tracking
    primary_strategy: str = "HTTP"
    effective_strategy: Optional[str] = None
    escalation_reason: Optional[str] = None

    # Step flags for backward compatibility
    discovery_success: bool = False
    http_success: bool = False
    browser_success: bool = False
    firecrawl_success: bool = False
    extraction_success: bool = False
    validation_success: bool = False

    # Attempts & Telemetry
    attempts: List[CrawlAttempt] = Field(default_factory=list)
    total_latency_ms: float = 0.0
    browser_seconds_total: float = 0.0
    bytes_received_total: int = 0

    # Data
    product: Optional[NormalizedProduct] = None
    failure: Optional[FailureDiagnosis] = None

    # Evidence directory path
    evidence_dir: Optional[str] = None


class CostTelemetry(BaseModel):
    request_count: int = 0
    successful_requests: int = 0
    failed_requests: int = 0
    browser_seconds: float = 0.0
    total_latency_ms: float = 0.0
    average_latency_ms: float = 0.0
    p95_latency_ms: float = 0.0
    retry_count: int = 0
    bytes_received: int = 0
    firecrawl_attempts: int = 0
    firecrawl_successes: int = 0
    firecrawl_failures: int = 0
    firecrawl_latency_ms: float = 0.0
    firecrawl_bytes_received: int = 0


class StrategyBenchmark(BaseModel):
    http_coverage: float = 0.0
    http_numerator: int = 0
    http_denominator: int = 0
    playwright_coverage: float = 0.0
    playwright_numerator: int = 0
    playwright_denominator: int = 0
    firecrawl_coverage: float = 0.0
    firecrawl_numerator: int = 0
    firecrawl_denominator: int = 0
    adapter_coverage: float = 0.0
    adapter_numerator: int = 0
    adapter_denominator: int = 0
    best_strategy: str = "HTTP"
    cost_per_successful_sku: Optional[float] = None


class TargetCrawlReport(BaseModel):
    target_id: str
    retailer: str
    brand_name: str
    country: str
    iso_country: str = "US"
    target_skus: int
    discovered: int
    
    # Precise counts
    http_success_count: int = 0
    browser_success_count: int = 0
    extracted_count: int = 0
    validated_count: int = 0
    partial_count: int = 0
    failed_count: int = 0

    # Rates with explicit denominators
    discovery_rate: float = 0.0
    page_load_success_rate: float = 0.0
    extraction_success_rate: float = 0.0
    validation_success_rate: float = 0.0
    field_completeness_avg: float = 0.0
    sku_coverage: float = 0.0
    block_rate: float = 0.0
    captcha_rate: float = 0.0
    timeout_rate: float = 0.0

    # Confidence and Phrasing
    sample_size: int = 0
    validated_sample_size: int = 0
    observed_coverage_statement: str = "0% observed coverage in 0 tested SKUs"
    confidence_level: float = 0.95

    # Telemetry and Cost
    cost_telemetry: CostTelemetry = Field(default_factory=CostTelemetry)
    strategy_benchmark: StrategyBenchmark = Field(default_factory=StrategyBenchmark)

    # Latencies
    avg_latency_ms: float = 0.0
    median_latency_ms: float = 0.0
    p95_latency_ms: float = 0.0
    avg_retries: float = 0.0

    # Strategies
    primary_strategy: str = "HTTP"
    fallback_strategy: Optional[str] = None
    strategy_success_breakdown: Dict[str, int] = Field(default_factory=dict)

    # Capability classification
    capability_grade: str = "E"  # A, B, C, D, E
    capability_category: str = "UNKNOWN"
    main_failure_reason: Optional[str] = None
    failure_breakdown: Dict[str, int] = Field(default_factory=dict)
    hierarchical_failures: List[Dict[str, Any]] = Field(default_factory=list)
    failure_diagnosis_summary: Optional[str] = None
    recommended_strategy: Optional[str] = None
    notes: Optional[str] = None

    # Templates & Categories
    template_breakdown: Dict[str, Dict[str, Any]] = Field(default_factory=dict)
    category_breakdown: Dict[str, Dict[str, Any]] = Field(default_factory=dict)

    # Tested SKU results
    sku_results: List[SkuCrawlResult] = Field(default_factory=list)
