"""
Bright Data Cost Guard & Rate Limiter.
Strict rate limiter, budget guard, and request cap controller to prevent high bills / excessive costs
when testing Bright Data proxies, Web Unlocker, and Scraping Browser.
"""
import os
import time
import asyncio
from typing import Dict, Any, Optional, Tuple
from dataclasses import dataclass, field
from pydantic import BaseModel


class BrightDataBudgetExceededError(Exception):
    """Raised when Bright Data request limit or bandwidth budget has been reached."""
    pass


class BrightDataRateLimitError(Exception):
    """Raised when request rate exceeds configured thresholds."""
    pass


@dataclass
class BrightDataUsageTelemetry:
    """Real-time tracking of Bright Data usage and estimated cost."""
    total_requests: int = 0
    successful_requests: int = 0
    failed_requests: int = 0
    blocked_by_guard: int = 0
    total_bytes_transferred: int = 0
    per_target_requests: Dict[str, int] = field(default_factory=dict)
    start_time: float = field(default_factory=time.time)
    last_request_time: float = 0.0

    @property
    def total_mb(self) -> float:
        return round(self.total_bytes_transferred / (1024 * 1024), 3)

    @property
    def estimated_cost_usd(self) -> float:
        # Standard estimate: ~$8.40 per GB residential or ~$2.00 per 1k Unlocker requests
        cpm_rate = float(os.getenv("BRIGHTDATA_ESTIMATED_CPM_USD", "2.00")) # per 1000 requests
        per_gb_rate = float(os.getenv("BRIGHTDATA_ESTIMATED_PER_GB_USD", "8.40")) # per GB
        request_cost = (self.total_requests / 1000.0) * cpm_rate
        bandwidth_cost = (self.total_bytes_transferred / (1024 * 1024 * 1024.0)) * per_gb_rate
        return round(max(request_cost, bandwidth_cost), 4)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "total_requests": self.total_requests,
            "successful_requests": self.successful_requests,
            "failed_requests": self.failed_requests,
            "blocked_by_guard": self.blocked_by_guard,
            "total_bytes": self.total_bytes_transferred,
            "total_mb": self.total_mb,
            "estimated_cost_usd": self.estimated_cost_usd,
            "per_target_requests": self.per_target_requests.copy(),
            "uptime_seconds": round(time.time() - self.start_time, 1)
        }


class BrightDataCostGuard:
    """
    Singleton / Global Cost Guard & Rate Limiter for all Bright Data interactions.
    Guarantees that test runs NEVER exceed safety budget, rate limits, or request limits.
    """
    _instance: Optional["BrightDataCostGuard"] = None
    _lock: asyncio.Lock = None

    def __init__(self):
        self._load_config()
        self.telemetry = BrightDataUsageTelemetry()
        self._async_lock = asyncio.Lock()

    @classmethod
    def get_instance(cls) -> "BrightDataCostGuard":
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def _load_config(self):
        """Loads safety guardrails from environment variables with conservative defaults."""
        # 1. Global Request Hard Cap (Default: 20 test requests max)
        self.max_global_requests = int(os.getenv("BRIGHTDATA_MAX_REQUESTS", "20"))
        
        # 2. Per-Target Hard Cap (Default: strictly 1 test request per target)
        self.max_requests_per_target = int(os.getenv("BRIGHTDATA_MAX_REQUESTS_PER_TARGET", "1"))
        
        # 3. Bandwidth Hard Cap in Megabytes (Default: 25 MB max)
        self.max_bandwidth_mb = float(os.getenv("BRIGHTDATA_MAX_BANDWIDTH_MB", "25.0"))
        
        # 4. Minimum Delay Between Requests (Default: 2.0s = 0.5 QPS to prevent bursting)
        self.delay_between_requests_sec = float(os.getenv("BRIGHTDATA_DELAY_BETWEEN_REQUESTS_SEC", "2.0"))
        
        # 5. Maximum Retries Allowed on Paid Proxy (Default: 0 - no expensive looping)
        self.max_retries = int(os.getenv("BRIGHTDATA_MAX_RETRIES", "0"))
        
        # 6. Global Enabled Flag
        self.enabled = os.getenv("BRIGHTDATA_ENABLED", "false").lower() in ("true", "1", "yes")

        # 7. Probe / Test-Only Mode (blocks recursive link following)
        self.probe_only_mode = os.getenv("BRIGHTDATA_PROBE_ONLY", "true").lower() in ("true", "1", "yes")

    def reload_config(self):
        """Refreshes configuration parameters from environment."""
        self._load_config()

    async def check_and_acquire(self, target_id: str, url: str) -> Tuple[bool, Optional[str]]:
        """
        Validates whether a request can be executed against Bright Data.
        Enforces rate limiting delay, per-target caps, global request caps, and bandwidth budgets.
        Returns (is_allowed, denial_reason).
        """
        if "127.0.0.1" in (url or "") or "localhost" in (url or "") or (target_id or "").startswith("mock"):
            return True, None

        async with self._async_lock:
            # 1. Check Global Request Budget
            if self.telemetry.total_requests >= self.max_global_requests:
                self.telemetry.blocked_by_guard += 1
                reason = (
                    f"Bright Data SAFETY CAP REACHED: Total requests ({self.telemetry.total_requests}) "
                    f"reached global max limit ({self.max_global_requests}). "
                    f"Blocking call to prevent unexpected fees."
                )
                return False, reason

            # 2. Check Per-Target Cap
            target_count = self.telemetry.per_target_requests.get(target_id, 0)
            if target_count >= self.max_requests_per_target:
                self.telemetry.blocked_by_guard += 1
                reason = (
                    f"Bright Data TARGET CAP REACHED: Target '{target_id}' has already used "
                    f"{target_count}/{self.max_requests_per_target} test requests. "
                    f"Skipping to prevent redundant costs."
                )
                return False, reason

            # 3. Check Cumulative Bandwidth Cap
            if self.telemetry.total_mb >= self.max_bandwidth_mb:
                self.telemetry.blocked_by_guard += 1
                reason = (
                    f"Bright Data BANDWIDTH CAP REACHED: Total data ({self.telemetry.total_mb:.2f} MB) "
                    f"exceeded budget limit ({self.max_bandwidth_mb} MB). "
                    f"Blocking call to prevent high bandwidth fees."
                )
                return False, reason

            # 4. Enforce Rate Limiting Delay
            now = time.time()
            elapsed_since_last = now - self.telemetry.last_request_time
            if self.telemetry.last_request_time > 0 and elapsed_since_last < self.delay_between_requests_sec:
                sleep_needed = self.delay_between_requests_sec - elapsed_since_last
                await asyncio.sleep(sleep_needed)

            # 5. Increment Usage Counters
            self.telemetry.total_requests += 1
            self.telemetry.per_target_requests[target_id] = target_count + 1
            self.telemetry.last_request_time = time.time()

            return True, None

    def record_response(self, target_id: str, success: bool, bytes_transferred: int):
        """Records transferred payload bytes and outcome to maintain accurate budget telemetry."""
        if success:
            self.telemetry.successful_requests += 1
        else:
            self.telemetry.failed_requests += 1
        self.telemetry.total_bytes_transferred += max(bytes_transferred, 0)

    def get_summary_report(self) -> str:
        """Generates a human-readable budget and cost audit summary."""
        d = self.telemetry.to_dict()
        return (
            f"--- BRIGHT DATA COST GUARD AUDIT ---\n"
            f"Requests Made: {d['total_requests']} / {self.max_global_requests} (Max Cap)\n"
            f"Successful: {d['successful_requests']} | Failed: {d['failed_requests']}\n"
            f"Blocked by Safety Guard: {d['blocked_by_guard']}\n"
            f"Bandwidth Used: {d['total_mb']:.3f} MB / {self.max_bandwidth_mb:.1f} MB (Budget)\n"
            f"Estimated Session Cost: ${d['estimated_cost_usd']:.4f} USD\n"
            f"Targets Tested: {len(d['per_target_requests'])}\n"
            f"------------------------------------"
        )
