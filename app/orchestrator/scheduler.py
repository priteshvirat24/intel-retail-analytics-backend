import asyncio
import time
from typing import Dict


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
