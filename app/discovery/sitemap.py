import gzip
import re
import xml.etree.ElementTree as ET
from typing import List, Optional, Union
import httpx
from app.discovery.base import BaseDiscovery
from app.discovery.deduplicator import ProductDeduplicator
from app.models.retailer import RetailerTargetConfig
from app.models.registry import CanonicalTarget


class SitemapDiscovery(BaseDiscovery):
    """Discovers product URLs by parsing sitemap index and product sitemap XML files."""

    XML_NAMESPACES = {
        "sm": "http://www.sitemaps.org/schemas/sitemap/0.9"
    }

    async def discover_urls(self, limit: int = 20) -> List[str]:
        sitemap_urls = []
        patterns = []
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "Accept": "application/xml,text/xml,*/*"
        }

        if hasattr(self.target_config, "sitemap_urls") and self.target_config.sitemap_urls:
            sitemap_urls = self.target_config.sitemap_urls
        elif hasattr(self.target_config, "discovery") and self.target_config.discovery:
            sitemap_urls = getattr(self.target_config.discovery, "sitemaps", [])
            raw_pats = getattr(self.target_config.discovery, "product_url_patterns", [])
            patterns = [re.compile(p) for p in raw_pats]
            headers.update(getattr(self.target_config.discovery, "headers", {}))

        if not sitemap_urls:
            return []

        discovered_urls: List[str] = []

        async with httpx.AsyncClient(
            timeout=5.0,
            follow_redirects=True,
            verify=False,
            headers=headers
        ) as client:
            for sitemap_url in sitemap_urls:
                if len(discovered_urls) >= limit * 2:
                    break
                try:
                    urls = await self._fetch_and_parse_sitemap(client, sitemap_url, patterns, limit, depth=0)
                    discovered_urls.extend(urls)
                except Exception:
                    continue

        return ProductDeduplicator.deduplicate(discovered_urls, max_count=limit)

    async def _fetch_and_parse_sitemap(
        self,
        client: httpx.AsyncClient,
        url: str,
        patterns: List[re.Pattern],
        limit: int,
        depth: int = 0
    ) -> List[str]:
        if depth > 1:
            return []

        response = await client.get(url)
        if response.status_code != 200:
            return []

        content = response.content
        if url.endswith(".gz") or content[:2] == b"\x1f\x8b":
            try:
                content = gzip.decompress(content)
            except Exception:
                pass

        try:
            root = ET.fromstring(content)
        except Exception:
            return []

        discovered: List[str] = []

        # Check if sitemapindex
        sitemaps = root.findall("sm:sitemap", self.XML_NAMESPACES) or root.findall("sitemap")
        if sitemaps:
            for sm in sitemaps[:3]:
                loc_elem = sm.find("sm:loc", self.XML_NAMESPACES) if sm.find("sm:loc", self.XML_NAMESPACES) is not None else sm.find("loc")
                if loc_elem is not None and loc_elem.text:
                    sub_url = loc_elem.text.strip()
                    if "product" in sub_url.lower() or "item" in sub_url.lower() or "catalog" in sub_url.lower() or "laptop" in sub_url.lower():
                        child_urls = await self._fetch_and_parse_sitemap(client, sub_url, patterns, limit, depth=depth + 1)
                        discovered.extend(child_urls)
                        if len(discovered) >= limit:
                            break
            return discovered

        # Parse regular urlset
        url_elems = root.findall("sm:url", self.XML_NAMESPACES) or root.findall("url")
        for u in url_elems:
            loc_elem = u.find("sm:loc", self.XML_NAMESPACES) if u.find("sm:loc", self.XML_NAMESPACES) is not None else u.find("loc")
            if loc_elem is not None and loc_elem.text:
                full_url = loc_elem.text.strip()
                if patterns:
                    if any(p.search(full_url) for p in patterns):
                        discovered.append(full_url)
                else:
                    if any(k in full_url.lower() for k in ["/dp/", "/product/", "/ip/", "/p/", "/ref/", "/item/", "/pd/"]):
                        discovered.append(full_url)
            if len(discovered) >= limit:
                break

        return discovered
