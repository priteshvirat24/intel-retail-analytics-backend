from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from pydantic import BaseModel, Field
from app.models.retailer import RetailerTargetConfig


class CrawlerResponse(BaseModel):
    url: str
    final_url: str
    status_code: int
    headers: Dict[str, str] = Field(default_factory=dict)
    html: str = ""
    markdown: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)
    response_time_ms: float = 0.0
    bytes_received: int = 0
    content_type: str = "text/html"
    screenshot_bytes: Optional[bytes] = None
    strategy: str = "HTTP"
    success: bool = True
    error_message: Optional[str] = None
    failure_reason: Optional[str] = None
    provider_failure_reason: Optional[str] = None
    is_blocked: bool = False
    is_captcha: bool = False
    is_js_rendered: bool = False


class BaseCrawler(ABC):
    """Abstract interface for crawler engines."""

    def __init__(self, target_config: RetailerTargetConfig):
        self.target_config = target_config

    @abstractmethod
    async def fetch(
        self,
        url: str,
        timeout_sec: float = 30.0,
        headers: Optional[Dict[str, str]] = None
    ) -> CrawlerResponse:
        """Fetch the page and return standardized CrawlerResponse."""
        pass
