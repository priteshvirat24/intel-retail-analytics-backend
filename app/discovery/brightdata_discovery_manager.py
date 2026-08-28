"""
BrightDataDiscoveryManager: Comprehensive Multi-Layer Discovery Engine for 52 Retailers.
Implements 7 independent discovery layers:
1. Amazon Specialized Scraper Search
2. Retailer Internal Search via Web Unlocker with Localized Multi-Language Tokens
3. Multi-Engine Search Index Queries (site:<domain> laptop / localized keywords)
4. Category Seed & Hub Listing Crawl
5. XML Sitemap & Sitemap Index Crawling
6. Interactive Browser API / Playwright DOM Discovery
7. Historical Verified Seed Map Integration
"""
import re
import json
import gzip
import time
import logging
import asyncio
from pathlib import Path
from typing import Dict, Any, List, Optional, Set, Tuple
from urllib.parse import urljoin, quote_plus, urlparse
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

import app.env
from app.crawlers.brightdata_web_unlocker import BrightDataWebUnlockerClient
from app.crawlers.brightdata_browser import BrightDataBrowserClient
from app.crawlers.amazon_scraper import AmazonScraperStrategy
from app.classification.laptop_classifier import LaptopClassifier
from app.models.registry import CanonicalTarget

logger = logging.getLogger("crawl.discovery_manager")


class BrightDataDiscoveryManager:
    """Orchestrates 7-layer product discovery across all 52 global retailers."""

    PDP_PATTERNS = [
        r"/dp/[a-z0-9]{10}",
        r"/product/[a-z0-9\-_]+",
        r"/p/[a-z0-9\-_]+",
        r"/item/[a-z0-9\-_]+",
        r"/ip/[a-z0-9\-_]+",
        r"/portatil-[a-z0-9\-_]+",
        r"/notebook-[a-z0-9\-_]+",
        r"/laptop-[a-z0-9\-_]+",
        r"\.p\?skuid=[0-9]+",
        r"-[0-9]{6,10}\.html",
        r"/pd/[a-z0-9\-_]+",
        r"/pdp/[a-z0-9\-_]+",
        r"/buy-[a-z0-9\-_]+"
    ]

    LOCALIZED_SEARCH_TEMPLATES = {
        "FR": ["/recherche?q=ordinateur+portable", "/s?k=ordinateur+portable", "/ordinateurs-portables", "/ordinateurs-portables/c10237"],
        "DE": ["/suche?q=laptop", "/s?k=laptop", "/laptops", "/kategorie/notebooks", "/notebooks"],
        "ES": ["/search?q=portatil", "/s?k=portatil", "/laptops", "/portatiles", "/ordenadores-portatiles"],
        "IT": ["/ricerca?q=notebook", "/s?k=notebook", "/notebook", "/computer-portatili", "/it/category/notebook-200101.html"],
        "PT": ["/busca?q=notebook", "/notebooks", "/laptops"],
        "BR": ["/busca?q=notebook", "/s?k=notebook", "/notebooks", "/lista/informatica/portateis-acessorios/notebooks"],
        "MX": ["/search?q=laptop", "/s?k=laptop", "/laptops", "/computadoras-portatiles", "/lista/computacion/laptops"],
        "CL": ["/search?q=notebook", "/notebooks", "/computacion/notebooks"],
        "CO": ["/search?q=portatil", "/portatiles", "/computacion/portatiles"],
        "PL": ["/szukaj?q=laptop", "/laptopy", "/komputery-i-tablety/laptopy-i-ultrabooki/laptopy"],
        "TR": ["/arama?q=laptop", "/laptoplar", "/dizustu-bilgisayar", "/bilgisayar/dizustu-bilgisayar"],
        "VN": ["/tim-kiem?k=laptop", "/laptop", "/laptop-ldp"],
        "KR": ["/search?q=노트북", "/category/laptop", "/laptops"],
        "JP": ["/category/19531/19532/", "/search?q=ノートパソコン", "/laptops"],
        "CN": ["/search?keyword=笔记本电脑", "/laptops"],
        "DK": ["/search?q=laptop", "/baerbar-computer", "/laptops"],
        "NO": ["/search?q=laptop", "/baerbar-pc", "/laptops"],
        "SE": ["/search?q=laptop", "/barbar-dator", "/laptops"],
        "GLOBAL": ["/search?q=laptop", "/s?k=laptop", "/site/searchpage.jsp?st=laptop", "/laptops", "/computers/laptops", "/computing/laptops"]
    }

    LOCALIZED_KEYWORDS = {
        "FR": ["ordinateur portable", "pc portable", "laptop"],
        "ES": ["portatil", "computadora portatil", "laptop"],
        "MX": ["laptop", "computadora portatil", "notebook"],
        "CL": ["notebook", "computador portatil", "laptop"],
        "CO": ["portatil", "computador portatil", "laptop"],
        "DE": ["laptop", "notebook", "gaming laptop"],
        "IT": ["computer portatile", "notebook", "laptop"],
        "PT": ["computador portatil", "notebook"],
        "BR": ["notebook", "laptop gamer", "computador portatil"],
        "PL": ["laptop", "notebook", "laptop gamingowy"],
        "TR": ["laptop", "dizustu bilgisayar", "notebook"],
        "VN": ["may tinh xach tay", "laptop"],
        "JP": ["ノートパソコン", "ノートPC", "laptop"],
        "KR": ["노트북", "laptop"],
        "CN": ["笔记本电脑", "游戏本", "轻薄本"],
        "DK": ["baerbar computer", "laptop"],
        "NO": ["baerbar pc", "laptop"],
        "SE": ["barbar dator", "laptop"],
        "GLOBAL": ["laptop", "notebook", "laptop computer", "gaming laptop"]
    }

    def __init__(
        self,
        unlocker_client: Optional[BrightDataWebUnlockerClient] = None,
        browser_client: Optional[BrightDataBrowserClient] = None
    ):
        self.unlocker = unlocker_client or BrightDataWebUnlockerClient()
        self.browser = browser_client or BrightDataBrowserClient()
        self.amazon_scraper = AmazonScraperStrategy(unlocker_client=self.unlocker)
        self.historical_seeds: Dict[Tuple[str, str], List[str]] = self._load_historical_seeds()

    def _load_historical_seeds(self) -> Dict[Tuple[str, str], List[str]]:
        """Loads previously verified authentic product URLs from past runs."""
        seed_map: Dict[Tuple[str, str], List[str]] = {}
        
        # 1. From analytics CSV
        csv_path = Path("reports/brightdata_only_52_site_scrape_analytics.csv")
        if csv_path.exists():
            try:
                import csv
                with open(csv_path, "r", encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        ret = (row.get("Retailer Name") or "").strip().lower()
                        cnt = (row.get("Country / Region") or "").strip().lower()
                        url = (row.get("Tested Product Page URL") or "").strip()
                        status = (row.get("Can Scrape Laptop Data?") or "").strip().upper()
                        if url and url.startswith("http") and url != "NONE" and status == "YES":
                            key = (ret, cnt)
                            seed_map.setdefault(key, []).append(url)
            except Exception as e:
                logger.debug(f"Error loading historical CSV seeds: {e}")

        # 2. From benchmark JSON
        json_path = Path("reports/laptop_crawl_benchmark.json")
        if json_path.exists():
            try:
                with open(json_path, "r", encoding="utf-8") as f:
                    d = json.load(f)
                    for row in d.get("matrix", []):
                        ret = (row.get("retailer") or "").strip().lower()
                        cnt = (row.get("country") or "").strip().lower()
                        url = (row.get("laptop_url") or "").strip()
                        if url and url.startswith("http") and url != "NONE":
                            key = (ret, cnt)
                            if url not in seed_map.get(key, []):
                                seed_map.setdefault(key, []).append(url)
            except Exception as e:
                logger.debug(f"Error loading benchmark JSON seeds: {e}")

        # 3. From evidence directory
        ev_dir = Path("evidence")
        if ev_dir.exists():
            for succ_file in ev_dir.glob("**/success.json"):
                try:
                    with open(succ_file, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        ret = (data.get("retailer") or "").strip().lower()
                        cnt = (data.get("country") or "").strip().lower()
                        url = (data.get("product_url") or "").strip()
                        if url and url.startswith("http"):
                            key = (ret, cnt)
                            if url not in seed_map.get(key, []):
                                seed_map.setdefault(key, []).append(url)
                except Exception:
                    pass

        return seed_map

    async def discover_candidates(
        self,
        target: CanonicalTarget,
        country_iso: str,
        limit: int = 10
    ) -> Tuple[List[Dict[str, Any]], List[str], List[Dict[str, Any]]]:
        """
        Executes 7-layer discovery for target and returns (candidates, methods_attempted, attempt_logs).
        """
        domain = target.domain.lower().replace("https://", "").replace("http://", "").replace("www.", "").strip("/").split("/")[0]
        country_iso = country_iso.lower()
        country_key = country_iso.upper()

        candidates: List[Dict[str, Any]] = []
        seen_urls: Set[str] = set()
        methods_attempted: List[str] = []
        attempt_logs: List[Dict[str, Any]] = []

        # -------------------------------------------------------------
        # Layer 1: Amazon Specialized Search Discovery (if Amazon)
        # -------------------------------------------------------------
        if "amazon" in domain:
            methods_attempted.append("amazon_specialized_search")
            t0 = time.perf_counter()
            try:
                amz_cands = await self.amazon_scraper.search_laptops(country_code=country_iso, keyword="laptop", limit=limit)
                lat = (time.perf_counter() - t0) * 1000.0
                attempt_logs.append({
                    "method": "amazon_specialized_search",
                    "url": f"https://www.{domain}/s?k=laptop",
                    "status": "SUCCESS" if amz_cands else "EMPTY",
                    "count": len(amz_cands),
                    "latency_ms": round(lat, 1)
                })
                for c in amz_cands:
                    if c["url"] not in seen_urls:
                        seen_urls.add(c["url"])
                        candidates.append({
                            **c,
                            "discovery_method": "Amazon Specialized Search",
                            "target_id": target.target_id,
                            "domain": domain,
                            "country": country_key
                        })
                if candidates:
                    return candidates[:limit], methods_attempted, attempt_logs
            except Exception as e:
                attempt_logs.append({
                    "method": "amazon_specialized_search",
                    "error": str(e)
                })

        # -------------------------------------------------------------
        # Layer 2: Historical Verified Seeds
        # -------------------------------------------------------------
        methods_attempted.append("historical_verified_seeds")
        ret_key = (target.retailer.lower().strip(), target.country.lower().strip())
        brand_key = (target.brand_name.lower().strip(), target.country.lower().strip())
        h_urls = list(self.historical_seeds.get(ret_key, [])) + list(self.historical_seeds.get(brand_key, []))
        for (r, c), u_list in self.historical_seeds.items():
            for u in u_list:
                if domain in u and u not in h_urls:
                    h_urls.append(u)

        for u in h_urls:
            if u not in seen_urls and domain in u:
                is_valid, _ = LaptopClassifier.validate_candidate_url(u, "")
                if is_valid:
                    seen_urls.add(u)
                    candidates.append({
                        "url": u,
                        "title": "Verified Candidate Product",
                        "discovery_method": "Historical Verified Seed",
                        "target_id": target.target_id,
                        "domain": domain,
                        "country": country_key
                    })

        # -------------------------------------------------------------
        # Layer 3: Retailer Internal Search via Web Unlocker
        # -------------------------------------------------------------
        methods_attempted.append("web_unlocker_internal_search")
        search_templates = self.LOCALIZED_SEARCH_TEMPLATES.get(country_key, self.LOCALIZED_SEARCH_TEMPLATES["GLOBAL"])
        base_url = f"https://{domain}"

        for tmpl in search_templates[:3]:
            if len(candidates) >= limit:
                break
            search_url = urljoin(base_url, tmpl)
            t0 = time.perf_counter()
            try:
                resp = await self.unlocker.fetch(search_url, country_iso=country_iso, timeout_sec=25.0)
                lat = (time.perf_counter() - t0) * 1000.0
                attempt_logs.append({
                    "method": "web_unlocker_internal_search",
                    "url": search_url,
                    "status_code": resp.status_code,
                    "success": resp.success,
                    "html_bytes": len(resp.html) if resp.html else 0,
                    "latency_ms": round(lat, 1)
                })

                if resp.success and resp.html:
                    extracted = self._extract_candidate_urls_from_html(resp.html, base_url, domain)
                    for c_url, c_title in extracted:
                        if c_url not in seen_urls and len(candidates) < limit:
                            seen_urls.add(c_url)
                            candidates.append({
                                "url": c_url,
                                "title": c_title,
                                "discovery_method": f"Retailer Search: {tmpl}",
                                "target_id": target.target_id,
                                "domain": domain,
                                "country": country_key
                            })
                    if len(candidates) >= limit:
                        break
            except Exception as e:
                attempt_logs.append({
                    "method": "web_unlocker_internal_search",
                    "url": search_url,
                    "error": str(e)
                })

        # -------------------------------------------------------------
        # Layer 4: Multi-Engine Search Index Discovery
        # -------------------------------------------------------------
        if len(candidates) < limit:
            methods_attempted.append("search_engine_discovery")
            keywords = self.LOCALIZED_KEYWORDS.get(country_key, self.LOCALIZED_KEYWORDS["GLOBAL"])
            for kw in keywords[:2]:
                if len(candidates) >= limit:
                    break
                query = f"site:{domain} {kw}"
                # Use DuckDuckGo HTML endpoint as robust fallback to Google
                ddg_url = f"https://html.duckduckgo.com/html/?q={quote_plus(query)}"
                t0 = time.perf_counter()
                try:
                    resp = await self.unlocker.fetch(ddg_url, country_iso=country_iso, timeout_sec=25.0)
                    lat = (time.perf_counter() - t0) * 1000.0
                    attempt_logs.append({
                        "method": "search_engine_discovery",
                        "url": ddg_url,
                        "status_code": resp.status_code,
                        "success": resp.success,
                        "latency_ms": round(lat, 1)
                    })

                    if resp.success and resp.html:
                        soup = BeautifulSoup(resp.html, "html.parser")
                        for a in soup.select("a.result__url, a[href]"):
                            href = a.get("href", "")
                            title = a.get_text(strip=True)
                            # Handle DDG redirect / uddg parameter
                            if "uddg=" in href:
                                m = re.search(r"uddg=([^&]+)", href)
                                if m:
                                    import urllib.parse
                                    href = urllib.parse.unquote(m.group(1))

                            if domain in href and href.startswith("http") and href not in seen_urls:
                                is_valid, _ = LaptopClassifier.validate_candidate_url(href, title)
                                if is_valid:
                                    seen_urls.add(href)
                                    candidates.append({
                                        "url": href,
                                        "title": title,
                                        "discovery_method": f"Search Index: {kw}",
                                        "target_id": target.target_id,
                                        "domain": domain,
                                        "country": country_key
                                    })
                                    if len(candidates) >= limit:
                                        break
                except Exception as e:
                    attempt_logs.append({
                        "method": "search_engine_discovery",
                        "url": ddg_url,
                        "error": str(e)
                    })

        # -------------------------------------------------------------
        # Layer 5: Category Hub & Category Seeds Crawl
        # -------------------------------------------------------------
        if len(candidates) < limit:
            methods_attempted.append("category_hub_crawl")
            cat_urls = [s.url for s in getattr(target, "category_seeds", []) if hasattr(s, "url")]
            if not cat_urls:
                cat_urls = [
                    f"{base_url}/laptops",
                    f"{base_url}/notebooks",
                    f"{base_url}/c/laptops",
                    f"{base_url}/category/laptops"
                ]

            for cat_url in cat_urls[:3]:
                if len(candidates) >= limit:
                    break
                t0 = time.perf_counter()
                try:
                    resp = await self.unlocker.fetch(cat_url, country_iso=country_iso, timeout_sec=25.0)
                    lat = (time.perf_counter() - t0) * 1000.0
                    attempt_logs.append({
                        "method": "category_hub_crawl",
                        "url": cat_url,
                        "status_code": resp.status_code,
                        "success": resp.success,
                        "latency_ms": round(lat, 1)
                    })

                    if resp.success and resp.html:
                        extracted = self._extract_candidate_urls_from_html(resp.html, base_url, domain)
                        for c_url, c_title in extracted:
                            if c_url not in seen_urls and len(candidates) < limit:
                                seen_urls.add(c_url)
                                candidates.append({
                                    "url": c_url,
                                    "title": c_title,
                                    "discovery_method": f"Category Hub: {cat_url[:40]}",
                                    "target_id": target.target_id,
                                    "domain": domain,
                                    "country": country_key
                                })
                except Exception as e:
                    attempt_logs.append({
                        "method": "category_hub_crawl",
                        "url": cat_url,
                        "error": str(e)
                    })

        # -------------------------------------------------------------
        # Layer 6: XML Sitemap & Sitemap Index Crawling
        # -------------------------------------------------------------
        if len(candidates) < limit:
            methods_attempted.append("sitemap_discovery")
            sitemap_urls = list(getattr(target, "sitemap_urls", []) or [])
            if not sitemap_urls:
                sitemap_urls = [
                    f"{base_url}/sitemap.xml",
                    f"{base_url}/sitemap_index.xml",
                    f"{base_url}/product-sitemap.xml"
                ]

            for sm_url in sitemap_urls[:2]:
                if len(candidates) >= limit:
                    break
                t0 = time.perf_counter()
                try:
                    resp = await self.unlocker.fetch(sm_url, country_iso=country_iso, timeout_sec=25.0)
                    lat = (time.perf_counter() - t0) * 1000.0
                    attempt_logs.append({
                        "method": "sitemap_discovery",
                        "url": sm_url,
                        "status_code": resp.status_code,
                        "success": resp.success,
                        "latency_ms": round(lat, 1)
                    })

                    if resp.success and resp.html:
                        urls = self._parse_sitemap_xml(resp.html, domain)
                        for u in urls:
                            if u not in seen_urls and len(candidates) < limit:
                                is_valid, _ = LaptopClassifier.validate_candidate_url(u, "")
                                if is_valid:
                                    seen_urls.add(u)
                                    candidates.append({
                                        "url": u,
                                        "title": "Sitemap Laptop Candidate",
                                        "discovery_method": f"Sitemap: {sm_url[:40]}",
                                        "target_id": target.target_id,
                                        "domain": domain,
                                        "country": country_key
                                    })
                except Exception as e:
                    attempt_logs.append({
                        "method": "sitemap_discovery",
                        "url": sm_url,
                        "error": str(e)
                    })

        # -------------------------------------------------------------
        # Layer 7: Browser API / Playwright Interactive DOM Discovery
        # -------------------------------------------------------------
        if len(candidates) == 0:
            methods_attempted.append("browser_api_interactive_discovery")
            t0 = time.perf_counter()
            try:
                brw_resp = await self.browser.fetch(base_url, country_iso=country_iso, timeout_sec=30.0)
                lat = (time.perf_counter() - t0) * 1000.0
                attempt_logs.append({
                    "method": "browser_api_interactive_discovery",
                    "url": base_url,
                    "status_code": brw_resp.status_code,
                    "success": brw_resp.success,
                    "latency_ms": round(lat, 1)
                })

                if brw_resp.success and brw_resp.html:
                    extracted = self._extract_candidate_urls_from_html(brw_resp.html, base_url, domain)
                    for c_url, c_title in extracted:
                        if c_url not in seen_urls and len(candidates) < limit:
                            seen_urls.add(c_url)
                            candidates.append({
                                "url": c_url,
                                "title": c_title,
                                "discovery_method": "Browser API DOM Extraction",
                                "target_id": target.target_id,
                                "domain": domain,
                                "country": country_key
                            })
            except Exception as e:
                attempt_logs.append({
                    "method": "browser_api_interactive_discovery",
                    "url": base_url,
                    "error": str(e)
                })

        return candidates[:limit], methods_attempted, attempt_logs

    def _extract_candidate_urls_from_html(self, html: str, base_url: str, domain: str) -> List[Tuple[str, str]]:
        """Extracts and ranks product candidate URLs from HTML."""
        if not html or len(html) < 200:
            return []

        soup = BeautifulSoup(html, "html.parser")
        results: List[Tuple[str, str]] = []
        seen = set()

        for a in soup.select("a[href]"):
            raw_href = a.get("href", "").strip()
            if not raw_href or raw_href.startswith("#") or raw_href.startswith("javascript:"):
                continue

            full_url = urljoin(base_url, raw_href)
            title = a.get_text(" ", strip=True)

            if domain not in full_url or not full_url.startswith("http"):
                continue

            # Check if URL matches PDP patterns
            is_pdp = any(re.search(p, full_url, re.IGNORECASE) for p in self.PDP_PATTERNS)
            has_laptop_token = any(kw in f"{full_url} {title}".lower() for kw in [
                "laptop", "notebook", "macbook", "chromebook", "portatil", "portátil",
                "ordinateur", "dizustu", "dizüstü", "ideapad", "thinkpad", "vivobook",
                "zenbook", "pavilion", "inspiron", "vostro", "legion", "omen", "tuf", "rog"
            ])

            if is_pdp or has_laptop_token:
                is_valid, reason = LaptopClassifier.validate_candidate_url(full_url, title)
                if is_valid and full_url not in seen:
                    seen.add(full_url)
                    results.append((full_url, title or "Discovered Product"))

        return results

    def _parse_sitemap_xml(self, xml_content: str, domain: str) -> List[str]:
        """Parses sitemap XML content and extracts product URLs matching laptop hints."""
        urls: List[str] = []
        try:
            # Handle potential gzip content
            if isinstance(xml_content, bytes) and xml_content.startswith(b"\x1f\x8b"):
                xml_content = gzip.decompress(xml_content).decode("utf-8", errors="ignore")

            root = ET.fromstring(xml_content)
            # Find all <loc> tags regardless of namespace
            for elem in root.iter():
                if elem.tag.endswith("loc") and elem.text:
                    u = elem.text.strip()
                    if domain in u and u.startswith("http"):
                        # Prefer URLs with laptop/notebook or product structure
                        if any(k in u.lower() for k in ["laptop", "notebook", "portatil", "ordinateur", "macbook", "chromebook", "/product/", "/p/"]):
                            urls.append(u)
        except Exception:
            pass
        return urls
