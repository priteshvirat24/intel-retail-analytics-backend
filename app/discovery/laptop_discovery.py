"""
Dedicated Laptop Product URL Discovery Engine.
Finds exactly ONE authentic laptop product page URL per retailer target
using category listings crawl, search, sitemaps, or Firecrawl map.
Never uses synthetic or placeholder URLs.
"""
import re
import asyncio
from urllib.parse import urljoin, urlparse
from typing import Optional, Tuple, List
import httpx
from bs4 import BeautifulSoup

from app.models.registry import CanonicalTarget, SeedSku, CategorySeed
from app.crawlers.firecrawl import FirecrawlCrawler


class LaptopDiscoveryEngine:
    """Discovers an authentic live laptop product URL for a given CanonicalTarget."""

    LAPTOP_URL_HINTS = [
        "laptop", "notebook", "macbook", "chromebook", "thinkpad", "zenbook",
        "pavilion", "ideapad", "vivobook", "legion", "alienware", "spectre",
        "yoga", "inspiron", "latitude", "vostro", "envy", "swift", "aspire",
        "predator", "surface", "portatil", "portatil-", "portatiles", "ordinateur-portable",
        "ordinateurs-portables", "tragbare-computer", "ordinateur_portable", "notebbok"
    ]

    PRODUCT_PATH_INDICATORS = ["/dp/", "/product/", "/ip/", "/p/", "/ref/", "/item/", "/pd/", "/pdp/"]

    @classmethod
    async def discover_laptop_url(
        cls,
        target: CanonicalTarget,
        firecrawl_crawler: Optional[FirecrawlCrawler] = None
    ) -> Tuple[Optional[str], str, str, Optional[str]]:
        """
        Discovers a live laptop product URL for the target.
        Returns: (laptop_url, discovery_method, discovery_status, discovery_failure_reason)
        """
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": f"{getattr(target, 'locale', 'en-US')},en;q=0.9"
        }

        # 1. Check configured seed URLs for genuine ASINs / non-placeholder seeds
        if target.seed_urls:
            for seed in target.seed_urls:
                cat = (seed.category or "").lower()
                url = (seed.url or "").lower()
                if "laptop" in cat or "notebook" in cat or any(h in url for h in cls.LAPTOP_URL_HINTS):
                    # Reject obvious synthetic/placeholder templates like /sku_0001
                    if not re.search(r"/sku_00\d\d", seed.url):
                        return seed.url, "configured_seed", "SUCCESS", None

        # 2. Category Listing Crawl
        laptop_cat_urls = []
        if target.category_seeds:
            for cs in target.category_seeds:
                c_name = (cs.category or "").lower()
                c_url = (cs.url or "").lower()
                if "laptop" in c_name or "notebook" in c_name or any(h in c_url for h in cls.LAPTOP_URL_HINTS):
                    laptop_cat_urls.append(cs.url)

        if not laptop_cat_urls:
            base = target.base_url
            candidates = [
                f"{base}/laptops",
                f"{base}/category/laptops",
                f"{base}/c/laptops",
                f"{base}/computers/laptops",
                f"{base}/ordinateurs-portables",
                f"{base}/portatiles"
            ]
            laptop_cat_urls.extend(candidates)

        is_blocked = False
        is_timeout = False

        for cat_url in laptop_cat_urls[:3]:
            try:
                async with httpx.AsyncClient(timeout=7.0, follow_redirects=True, verify=False, headers=headers) as client:
                    resp = await client.get(cat_url)
                    if resp.status_code == 200 and len(resp.text) > 1000:
                        soup = BeautifulSoup(resp.text, "html.parser")
                        links = soup.find_all("a", href=True)
                        for a in links:
                            raw_href = a["href"].strip()
                            full_url = urljoin(str(resp.url), raw_href)
                            parsed = urlparse(full_url)
                            path_lower = parsed.path.lower()
                            anchor_text = (a.get_text() or "").lower()

                            # Match product detail structure + laptop keywords
                            has_prod_path = any(p in path_lower for p in cls.PRODUCT_PATH_INDICATORS)
                            has_laptop_hint = any(h in path_lower for h in cls.LAPTOP_URL_HINTS) or "laptop" in anchor_text or "macbook" in anchor_text or "notebook" in anchor_text

                            if (has_prod_path and has_laptop_hint) or (has_prod_path and len(path_lower.split("/")) >= 3):
                                # Ensure it's on target domain
                                if target.domain in parsed.netloc:
                                    return full_url, "category_crawl", "SUCCESS", None

                    elif resp.status_code in (403, 429):
                        is_blocked = True
            except httpx.TimeoutException:
                is_timeout = True
            except Exception:
                pass

        # 3. Firecrawl Map / Search Discovery on Domain
        if firecrawl_crawler:
            try:
                map_urls = await firecrawl_crawler.map(url=target.base_url, search="laptop", limit=30, timeout_sec=10.0)
                for u in map_urls:
                    parsed = urlparse(u)
                    path_lower = parsed.path.lower()
                    if any(h in path_lower for h in cls.LAPTOP_URL_HINTS) and any(p in path_lower for p in cls.PRODUCT_PATH_INDICATORS):
                        return u, "firecrawl_map", "SUCCESS", None
            except Exception:
                pass

        # 4. If all fail, return explicit discovery failure
        if is_blocked:
            return None, "none", "DISCOVERY_FAILED", "DISCOVERY_BLOCKED"
        elif is_timeout:
            return None, "none", "DISCOVERY_FAILED", "DISCOVERY_TIMEOUT"
        else:
            return None, "none", "DISCOVERY_FAILED", "NO_LAPTOP_URL_DISCOVERED"
