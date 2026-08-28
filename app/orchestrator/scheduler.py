import asyncio
import time
from typing import Dict, Optional, Any


class DomainRateLimiter:
    """Manages concurrency and request rate per retailer domain."""

    def __init__(
        self,
        domain: str,
        max_concurrency: int = 3,
        requests_per_second: float = 2.0,
        base_delay_sec: float = 1.0
    ):
        self.domain = domain
        self.max_concurrency = max_concurrency
        self.requests_per_second = requests_per_second
        self.current_delay_sec = base_delay_sec
        self.semaphore = asyncio.Semaphore(max_concurrency)
        self.last_request_time = 0.0
        self._lock = asyncio.Lock()

    async def acquire(self):
        await self.semaphore.acquire()
        sleep_time = 0.0
        async with self._lock:
            now = time.time()
            min_interval = min(2.0, max(1.0 / self.requests_per_second, self.current_delay_sec))
            elapsed = now - self.last_request_time
            if elapsed < min_interval:
                sleep_time = min_interval - elapsed
            self.last_request_time = now + sleep_time

        if sleep_time > 0:
            await asyncio.sleep(sleep_time)

    def release(self):
        self.semaphore.release()

    def throttle_up(self):
        """Increase delay when encountering rate limit (429) or high latency."""
        self.current_delay_sec = min(2.5, self.current_delay_sec * 1.3)

    def throttle_down(self):
        """Gradually decrease delay upon sustained success."""
        self.current_delay_sec = max(0.2, self.current_delay_sec * 0.9)


class CrawlScheduler:
    """Global scheduler managing domain rate limiters across targets."""

    def __init__(self):
        self._limiters: Dict[str, DomainRateLimiter] = {}

    def get_limiter(
        self,
        domain: str,
        max_concurrency: int = 3,
        requests_per_second: float = 2.0,
        base_delay_sec: float = 1.0
    ) -> DomainRateLimiter:
        if domain not in self._limiters:
            self._limiters[domain] = DomainRateLimiter(
                domain=domain,
                max_concurrency=max_concurrency,
                requests_per_second=requests_per_second,
                base_delay_sec=base_delay_sec
            )
        return self._limiters[domain]


class FeedDeliveryScheduler:
    """
    Manages automated, cadence-based data feed exports and contractual sFTP distribution.
    """

    @classmethod
    async def trigger_daily_feed_delivery(
        cls,
        products: Optional[list] = None,
        sftp_config: Optional[Any] = None
    ) -> Dict[str, Any]:
        """
        Executes daily Price & Promotion feed generation and automated sFTP push.
        Runs synchronously or as an asynchronous task within orchestrator runs.
        """
        from app.delivery.daily_feed_job import DailyFeedJob
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(
            None,
            lambda: DailyFeedJob.run_daily_delivery(products=products, sftp_config=sftp_config)
        )

