import asyncio
import random
from typing import Set, Optional, Union
from app.models.failure import SpecificReason


class RetryPolicy:
    """Manages retry decisions and exponential backoff with jitter."""

    DEFAULT_TRANSIENT_STATUSES: Set[int] = {408, 429, 500, 502, 503, 504}
    PERMANENT_STATUSES: Set[int] = {400, 401, 403, 404, 410}

    def __init__(
        self,
        max_retries: int = 3,
        backoff_factor: float = 1.5,
        jitter_factor: float = 0.5,
        transient_statuses: Optional[Set[int]] = None
    ):
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor
        self.jitter_factor = jitter_factor
        self.transient_statuses = transient_statuses or self.DEFAULT_TRANSIENT_STATUSES

    def should_retry(self, attempt_count: int, status_code: Optional[int], failure_reason: Optional[Union[SpecificReason, str]]) -> bool:
        """Determines if a failed attempt should be retried."""
        if attempt_count >= self.max_retries:
            return False

        if status_code in self.PERMANENT_STATUSES:
            return False

        reason_val = failure_reason.value if hasattr(failure_reason, "value") else str(failure_reason)

        if reason_val in (
            "HTTP_404_NOT_FOUND",
            "HTTP_410_GONE",
            "PRODUCT_SCHEMA_NOT_FOUND",
            "LOGIN_REQUIRED",
            "ROBOTS_RESTRICTION"
        ):
            return False

        if status_code in self.transient_statuses:
            return True

        if reason_val in (
            "HTTP_TIMEOUT",
            "CONNECTION_TIMEOUT",
            "HTTP_5XX_SERVER_ERROR",
            "HTTP_429_RATE_LIMITED",
            "RATE_LIMITED",
            "EMPTY_RESPONSE"
        ):
            return True

        return False

    async def backoff_sleep(self, attempt_count: int):
        """Sleeps with exponential backoff and randomized jitter."""
        base_delay = self.backoff_factor ** attempt_count
        jitter = random.uniform(0, self.jitter_factor * base_delay)
        total_sleep = base_delay + jitter
        await asyncio.sleep(min(total_sleep, 5.0))
