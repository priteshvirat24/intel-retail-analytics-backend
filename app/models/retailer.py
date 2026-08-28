from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class DiscoveryConfig(BaseModel):
    sitemaps: List[str] = Field(default_factory=list)
    category_urls: List[str] = Field(default_factory=list)
    search_url: Optional[str] = None
    seed_urls: List[str] = Field(default_factory=list)
    product_url_patterns: List[str] = Field(default_factory=list)
    headers: Dict[str, str] = Field(default_factory=dict)


class RetailerTargetConfig(BaseModel):
    target_id: str
    retailer: str
    brand_name: str
    country: str
    domain: str
    base_url: str
    locale: str
    currency: str
    enabled: bool = True
    max_test_skus: int = 20
    preferred_strategy: str = "auto"
    rate_limit_policy: str = "default"
    discovery: DiscoveryConfig = Field(default_factory=DiscoveryConfig)
    custom_adapter: Optional[str] = None
    custom_selectors: Dict[str, Any] = Field(default_factory=dict)


class RetailerProfile(BaseModel):
    retailer: str
    country: str
    preferred_strategy: str = "auto"
    http_success_rate: float = 0.0
    browser_success_rate: float = 0.0
    preferred_concurrency: int = 3
    preferred_delay_sec: float = 1.0
    known_failures: List[str] = Field(default_factory=list)
    capability_grade: str = "E"  # A, B, C, D, E
    capability_category: str = "UNKNOWN"  # HTTP_ONLY, BROWSER_REQUIRED, CUSTOM_ADAPTER_REQUIRED, BLOCKED, etc.
