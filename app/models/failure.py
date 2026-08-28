from enum import Enum
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime, timezone


class CrawlStage(str, Enum):
    DISCOVERY = "DISCOVERY"
    URL_REACHABILITY = "URL_REACHABILITY"
    CONTENT_AVAILABILITY = "CONTENT_AVAILABILITY"
    PRODUCT_IDENTIFICATION = "PRODUCT_IDENTIFICATION"
    EXTRACTION = "EXTRACTION"
    FIELD_VALIDATION = "FIELD_VALIDATION"
    PRODUCT_VALIDATION = "PRODUCT_VALIDATION"


class StageStatus(str, Enum):
    SUCCESS = "SUCCESS"
    PARTIAL_SUCCESS = "PARTIAL_SUCCESS"
    FAILED = "FAILED"
    SKIPPED = "SKIPPED"


class FailureCategory(str, Enum):
    NETWORK = "NETWORK"
    ACCESS = "ACCESS"
    HTTP_STATUS = "HTTP_STATUS"
    CONTENT = "CONTENT"
    SCHEMA = "SCHEMA"
    EXTRACTION = "EXTRACTION"
    VALIDATION = "VALIDATION"


class SpecificReason(str, Enum):
    # NETWORK
    DNS_RESOLUTION_FAILED = "DNS_RESOLUTION_FAILED"
    CONNECTION_TIMEOUT = "CONNECTION_TIMEOUT"
    TLS_ERROR = "TLS_ERROR"
    HTTP_TIMEOUT = "HTTP_TIMEOUT"
    
    # ACCESS / BOT / CHALLENGES
    BOT_PROTECTION = "BOT_PROTECTION"
    CAPTCHA_CHALLENGE = "CAPTCHA_CHALLENGE"
    ROBOTS_RESTRICTION = "ROBOTS_RESTRICTION"
    GEO_RESTRICTION = "GEO_RESTRICTION"
    LOGIN_REQUIRED = "LOGIN_REQUIRED"
    
    # HTTP_STATUS
    HTTP_403_FORBIDDEN = "HTTP_403_FORBIDDEN"
    HTTP_404_NOT_FOUND = "HTTP_404_NOT_FOUND"
    HTTP_410_GONE = "HTTP_410_GONE"
    HTTP_429_RATE_LIMITED = "HTTP_429_RATE_LIMITED"
    HTTP_5XX_SERVER_ERROR = "HTTP_5XX_SERVER_ERROR"
    
    # CONTENT / RENDERING
    EMPTY_RESPONSE = "EMPTY_RESPONSE"
    JAVASCRIPT_REQUIRED = "JAVASCRIPT_REQUIRED"
    
    # SCHEMA / PRODUCT IDENTIFICATION
    PRODUCT_SCHEMA_NOT_FOUND = "PRODUCT_SCHEMA_NOT_FOUND"
    PRODUCT_ID_NOT_FOUND = "PRODUCT_ID_NOT_FOUND"
    NOT_A_PRODUCT_PAGE = "NOT_A_PRODUCT_PAGE"
    
    # EXTRACTION
    EXTRACTION_FAILED = "EXTRACTION_FAILED"
    FIELD_EXTRACTION_FAILED = "FIELD_EXTRACTION_FAILED"
    
    # VALIDATION
    REQUIRED_FIELD_MISSING = "REQUIRED_FIELD_MISSING"
    FIELD_INVALID = "FIELD_INVALID"
    FIELD_CONFLICT = "FIELD_CONFLICT"
    
    # FIRECRAWL / INTEGRATION
    FIRECRAWL_SERVICE_UNAVAILABLE = "FIRECRAWL_SERVICE_UNAVAILABLE"
    FIRECRAWL_TIMEOUT = "FIRECRAWL_TIMEOUT"
    FIRECRAWL_CONNECTION_FAILED = "FIRECRAWL_CONNECTION_FAILED"
    FIRECRAWL_RATE_LIMITED = "FIRECRAWL_RATE_LIMITED"
    FIRECRAWL_INTERNAL_ERROR = "FIRECRAWL_INTERNAL_ERROR"
    FIRECRAWL_BROWSER_FAILURE = "FIRECRAWL_BROWSER_FAILURE"
    FIRECRAWL_RENDER_FAILURE = "FIRECRAWL_RENDER_FAILURE"
    FIRECRAWL_ERROR = "FIRECRAWL_ERROR"
    
    # BRIGHTDATA / PROXY
    BRIGHTDATA_USAGE_LIMIT_REACHED = "BRIGHTDATA_USAGE_LIMIT_REACHED"
    BRIGHTDATA_SAFETY_CAP_REACHED = "BRIGHTDATA_SAFETY_CAP_REACHED"
    BRIGHTDATA_AUTH_FAILED = "BRIGHTDATA_AUTH_FAILED"

    # APIFY / ACTOR
    APIFY_ACTOR_FAILURE = "APIFY_ACTOR_FAILURE"
    APIFY_AUTH_FAILED = "APIFY_AUTH_FAILED"
    APIFY_TIMEOUT = "APIFY_TIMEOUT"
    APIFY_RATE_LIMITED = "APIFY_RATE_LIMITED"
    APIFY_SERVICE_UNAVAILABLE = "APIFY_SERVICE_UNAVAILABLE"

    # FALLBACK
    UNKNOWN_FAILURE = "UNKNOWN_FAILURE"


# Backward compatibility alias
FailureReason = SpecificReason


class FailureDiagnosis(BaseModel):
    category: FailureCategory
    specific_reason: SpecificReason
    stage: CrawlStage
    failure_reason_human: str = Field(description="Human readable explanation of why this crawl or extraction failed.")
    http_status: Optional[int] = None
    exception_type: Optional[str] = None
    retry_count: int = 0
    last_error: Optional[str] = None
    source_strategy: Optional[str] = None
    provider_failure_reason: Optional[str] = None
    anti_bot_vendor: Optional[str] = Field(default=None, description="Cloudflare, Akamai, Kasada, PerimeterX, DataDome, etc.")
    timestamp: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    is_recoverable: bool = False
    recommended_escalation: Optional[str] = None
    details: Dict[str, Any] = Field(default_factory=dict)

    # Legacy compatibility property
    @property
    def reason(self) -> SpecificReason:
        return self.specific_reason
