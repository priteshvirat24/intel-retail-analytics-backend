"""
Bright Data Managed Scraping Browser Client & Strategy.
Connects to Bright Data Scraping Browser via CDP (Chrome DevTools Protocol) over WebSocket (wss://...:9222)
with Playwright, supporting dynamic DOM stabilization, human-like interaction, scrolling, waiting, and screenshot capture.
Falls back seamlessly to local stealth browser rendering if managed CDP is unavailable.
"""
import os
import time
import asyncio
import logging
from typing import Dict, Any, Optional, Tuple
from playwright.async_api import async_playwright

import app.env
from app.crawlers.base import BaseCrawler, CrawlerResponse
from app.models.retailer import RetailerTargetConfig

logger = logging.getLogger("crawl.brightdata_browser")


class BrightDataBrowserClient:
    """Official Bright Data Scraping Browser CDP Client."""

    def __init__(
        self,
        customer_id: Optional[str] = None,
        zone: Optional[str] = None,
        password: Optional[str] = None,
        host: Optional[str] = None,
        port: Optional[int] = None
    ):
        self.customer_id = customer_id or os.getenv("BRIGHTDATA_CUSTOMER_ID", "")
        self.zone = zone or os.getenv("BRIGHTDATA_BROWSER_ZONE", "scraping_browser1")
        self.password = password or os.getenv("BRIGHTDATA_PASSWORD", "")
        self.host = host or os.getenv("BRIGHTDATA_HOST", "brd.superproxy.io")
        self.port = int(port or os.getenv("BRIGHTDATA_CDP_PORT", "9222"))
        
        # Format: wss://brd-customer-<customer>-zone-<zone>:<password>@brd.superproxy.io:9222
        if self.customer_id and self.password:
            self.cdp_endpoint = f"wss://brd-customer-{self.customer_id}-zone-{self.zone}:{self.password}@{self.host}:{self.port}"
        else:
            self.cdp_endpoint = ""

    async def fetch(
        self,
        url: str,
        country_iso: Optional[str] = None,
        timeout_sec: float = 40.0,
        wait_for_selector: Optional[str] = None,
        take_screenshot: bool = False
    ) -> CrawlerResponse:
        """
        Renders an arbitrary page using Bright Data managed browser infrastructure over CDP,
        or local stealth browser engine.
        """
        if not url or url == "NONE" or not url.startswith("http"):
            return CrawlerResponse(
                url=url or "NONE",
                final_url=url or "NONE",
                status_code=0,
                strategy="BRIGHTDATA_BROWSER",
                success=False,
                error_message="Invalid URL provided."
            )

        t0 = time.perf_counter()
        screenshot_bytes: Optional[bytes] = None

        try:
            async with async_playwright() as p:
                browser = None
                is_managed_cdp = False

                # 1. Attempt connection to Bright Data Managed CDP if endpoint is available
                if self.cdp_endpoint and ("127.0.0.1" not in url and "localhost" not in url):
                    try:
                        # Append country flag if supported: -country-<iso>
                        endpoint = self.cdp_endpoint
                        if country_iso:
                            auth_part, host_part = endpoint.split("@", 1)
                            auth_part = f"{auth_part}-country-{country_iso.lower()}"
                            endpoint = f"{auth_part}@{host_part}"

                        browser = await p.chromium.connect_over_cdp(endpoint, timeout=15000)
                        is_managed_cdp = True
                    except Exception as cdp_err:
                        logger.warning(f"Bright Data Managed CDP connect failed ({cdp_err}), escalating to stealth Playwright.")
                        browser = None

                # 2. Fallback to Chromium instance with stealth args
                if browser is None:
                    browser = await p.chromium.launch(
                        headless=True,
                        args=[
                            "--disable-blink-features=AutomationControlled",
                            "--no-sandbox",
                            "--disable-setuid-sandbox",
                            "--disable-infobars",
                            "--window-size=1920,1080"
                        ]
                    )

                context = await browser.new_context(
                    viewport={"width": 1920, "height": 1080},
                    user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
                    locale="en-US"
                )

                page = await context.new_page()

                # Stealth overrides
                await page.add_init_script("""
                    Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
                    window.chrome = { runtime: {} };
                """)

                # Navigate
                resp = await page.goto(url, wait_until="domcontentloaded", timeout=int(timeout_sec * 1000))
                status_code = resp.status if resp else 200

                # Human-like interaction: Scroll to trigger lazy loading / hydration
                try:
                    await page.evaluate("window.scrollBy(0, 500)")
                    await asyncio.sleep(0.5)
                    await page.evaluate("window.scrollBy(0, 500)")
                    await asyncio.sleep(0.5)
                except Exception:
                    pass

                if wait_for_selector:
                    try:
                        await page.wait_for_selector(wait_for_selector, timeout=5000)
                    except Exception:
                        pass

                # Extract fully rendered HTML and final URL
                html = await page.content()
                final_url = page.url

                if take_screenshot:
                    try:
                        screenshot_bytes = await page.screenshot(full_page=False)
                    except Exception:
                        pass

                await browser.close()

                lat_ms = (time.perf_counter() - t0) * 1000.0
                success = status_code in (200, 301, 302) and len(html) > 500

                strat_label = "BRIGHTDATA_MANAGED_BROWSER" if is_managed_cdp else "BRIGHTDATA_BROWSER_STEALTH"

                return CrawlerResponse(
                    url=url,
                    final_url=final_url,
                    status_code=status_code,
                    strategy=strat_label,
                    success=success,
                    html=html,
                    response_time_ms=lat_ms,
                    is_js_rendered=True,
                    error_message=None if success else f"HTTP {status_code}"
                )

        except Exception as e:
            lat_ms = (time.perf_counter() - t0) * 1000.0
            return CrawlerResponse(
                url=url,
                final_url=url,
                status_code=0,
                strategy="BRIGHTDATA_BROWSER",
                success=False,
                error_message=str(e),
                response_time_ms=lat_ms
            )


class BrightDataBrowserCrawler(BaseCrawler):
    """Adapter wrapping BrightDataBrowserClient as a BaseCrawler."""

    def __init__(self, target_config: RetailerTargetConfig):
        super().__init__(target_config)
        self.client = BrightDataBrowserClient()

    async def fetch(
        self,
        url: str,
        timeout_sec: float = 40.0,
        headers: Optional[Dict[str, str]] = None
    ) -> CrawlerResponse:
        country_iso = getattr(self.target_config, "iso_country", None) or getattr(self.target_config, "country", "US")
        return await self.client.fetch(
            url=url,
            country_iso=country_iso,
            timeout_sec=timeout_sec
        )
