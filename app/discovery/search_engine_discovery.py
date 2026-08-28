"""
Search Engine Discovery Adapter.
Executes targeted search queries (site:<domain> laptop, site:<domain> notebook, localized terms)
via Bright Data Web Unlocker to discover authentic product URLs from search indexes.
"""
import re
import logging
from typing import Dict, Any, List, Optional
from urllib.parse import quote_plus, urljoin
from bs4 import BeautifulSoup

import app.env
from app.crawlers.brightdata_web_unlocker import BrightDataWebUnlockerClient
from app.classification.laptop_classifier import LaptopClassifier

logger = logging.getLogger("crawl.search_discovery")


class SearchEngineDiscoveryAdapter:
    """Discovers retailer candidate product URLs using search engine indexing queries."""

    LOCALIZED_KEYWORDS = {
        "FR": ["ordinateur portable", "pc portable", "laptop"],
        "ES": ["portatil", "computadora portatil", "laptop"],
        "MX": ["laptop", "computadora portatil"],
        "CL": ["notebook", "computador portatil", "laptop"],
        "CO": ["portatil", "computador portatil", "laptop"],
        "DE": ["laptop", "notebook", "gaming laptop"],
        "IT": ["computer portatile", "notebook", "laptop"],
        "PT": ["computador portatil", "notebook"],
        "BR": ["notebook", "laptop gamer"],
        "PL": ["laptop", "notebook", "laptop gamingowy"],
        "TR": ["laptop", "dizustu bilgisayar", "notebook"],
        "VN": ["may tinh xach tay", "laptop"],
        "JP": ["ノートパソコン", "ノートPC", "laptop"],
        "KR": ["노트북", "laptop"],
        "CN": ["笔记本电脑", "游戏本", "轻薄本"],
        "DK": ["baerbar", "laptop"],
        "NO": ["baerbar pc", "laptop"],
        "SE": ["baerbar dator", "laptop"],
        "GLOBAL": ["laptop", "notebook", "laptop computer", "gaming laptop"]
    }

    def __init__(self, unlocker_client: Optional[BrightDataWebUnlockerClient] = None):
        self.unlocker = unlocker_client or BrightDataWebUnlockerClient()

    async def discover_candidates(
        self,
        domain: str,
        country_code: str = "US",
        limit: int = 10
    ) -> List[Dict[str, Any]]:
        """
        Runs search queries for the domain and extracts genuine product candidate URLs.
        """
        clean_domain = domain.lower().replace("https://", "").replace("http://", "").replace("www.", "").strip("/").split("/")[0]
        country = country_code.upper()
        keywords = self.LOCALIZED_KEYWORDS.get(country, self.LOCALIZED_KEYWORDS["GLOBAL"])
        
        candidates: List[Dict[str, Any]] = []
        seen_urls = set()

        for kw in keywords[:3]:
            if len(candidates) >= limit:
                break

            query = f"site:{clean_domain} {kw}"
            search_url = f"https://www.google.com/search?q={quote_plus(query)}&num=15"

            try:
                resp = await self.unlocker.fetch(search_url, country_iso=country.lower(), timeout_sec=25.0)
                if not resp.success or not resp.html:
                    continue

                soup = BeautifulSoup(resp.html, "html.parser")
                # Google search result link selectors
                links = soup.select("a[href*='http']")

                for a in links:
                    href = a.get("href", "")
                    title = a.get_text(strip=True)

                    # Extract actual destination URL from Google redirect if present
                    if "/url?q=" in href:
                        m = re.search(r"/url\?q=([^&]+)", href)
                        if m:
                            href = m.group(1)

                    if clean_domain not in href or href in seen_urls:
                        continue

                    # Filter out search pages and non-product URLs
                    if any(x in href for x in ["/search", "/category", "/categories", "/collection", "/katalog", "/brand", "/cart"]):
                        continue

                    # Validate candidate URL
                    is_valid, reason = LaptopClassifier.validate_candidate_url(href, title)
                    if not is_valid:
                        continue

                    seen_urls.add(href)
                    candidates.append({
                        "url": href,
                        "title": title,
                        "discovery_method": f"Search Engine ({query})",
                        "domain": clean_domain,
                        "country": country
                    })

                    if len(candidates) >= limit:
                        break

            except Exception as e:
                logger.warning(f"Search discovery query '{query}' failed: {e}")
                continue

        return candidates
