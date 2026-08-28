import asyncio
import re
from urllib.parse import urljoin, quote_plus
from typing import List, Union
from bs4 import BeautifulSoup
import httpx
from app.discovery.base import BaseDiscovery
from app.discovery.deduplicator import ProductDeduplicator
from app.models.retailer import RetailerTargetConfig
from app.models.registry import CanonicalTarget


class SearchDiscovery(BaseDiscovery):
    """Discovers product URLs by performing searches on the retailer site for core electronics queries."""

    CORE_QUERIES = ["laptop", "notebook", "macbook"]

    async def discover_urls(self, limit: int = 20) -> List[str]:
        search_template = None
        patterns = []
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": f"{getattr(self.target_config, 'locale', 'en-US')},en;q=0.9"
        }

        if hasattr(self.target_config, "discovery") and self.target_config.discovery:
            search_template = getattr(self.target_config.discovery, "search_url", None)
            raw_pats = getattr(self.target_config.discovery, "product_url_patterns", [])
            patterns = [re.compile(p) for p in raw_pats]
            headers.update(getattr(self.target_config.discovery, "headers", {}))
        elif hasattr(self.target_config, "base_url"):
            search_template = f"{self.target_config.base_url}/search?q={{query}}"

        if not search_template:
            return []

        discovered: List[str] = []

        async def _fetch_query(query: str) -> List[str]:
            formatted_url = search_template.format(query=quote_plus(query))
            try:
                async with httpx.AsyncClient(timeout=6.0, follow_redirects=True, verify=False, headers=headers) as client:
                    resp = await client.get(formatted_url)
                    if resp.status_code != 200:
                        return []

                    soup = BeautifulSoup(resp.text, "html.parser")
                    links = soup.find_all("a", href=True)
                    found = []
                    for a in links:
                        raw_href = a["href"].strip()
                        full_url = urljoin(str(resp.url), raw_href)

                        if patterns:
                            if any(p.search(full_url) for p in patterns):
                                found.append(full_url)
                        else:
                            if any(k in full_url.lower() for k in ["/dp/", "/product/", "/ip/", "/p/", "/ref/", "/item/", "/pd/"]):
                                found.append(full_url)
                    return found
            except Exception:
                return []

        tasks = [_fetch_query(q) for q in self.CORE_QUERIES[:2]]
        results = await asyncio.gather(*tasks)
        for r in results:
            discovered.extend(r)

        return ProductDeduplicator.deduplicate(discovered, max_count=limit)
