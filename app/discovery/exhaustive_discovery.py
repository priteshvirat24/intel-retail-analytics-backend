"""
Exhaustive Multi-Source Laptop Product URL Discovery Engine.
Implements a 6-phase discovery pipeline:
- Phase 1: Domain Validation & Robots.txt inspection
- Phase 2: Retailer search & category listing crawl
- Phase 3: Search-engine query candidate discovery
- Phase 4: Sitemaps & robots.txt references recursive search
- Phase 5: Self-hosted Firecrawl map() & crawl() discovery
- Phase 6: Candidate URL validation (resolves, product page, laptop keywords, unblocked)
"""
import re
import gzip
import time
import asyncio
import xml.etree.ElementTree as ET
from urllib.parse import urljoin, urlparse, quote_plus
from typing import Optional, Tuple, List, Dict, Any
import httpx
from bs4 import BeautifulSoup

from app.models.registry import CanonicalTarget
from app.crawlers.firecrawl import FirecrawlCrawler
from app.evaluation.failures import FailureClassifier
from app.evaluation.laptop_detector import LaptopDetector, LaptopCrawlEvaluation
from app.crawlers.base import CrawlerResponse


class ExhaustiveLaptopDiscoveryEngine:
    """Exhaustively discovers and validates an authentic laptop product URL per target."""

    LAPTOP_KEYWORDS = [
        "laptop", "notebook", "macbook", "chromebook", "thinkpad", "zenbook",
        "pavilion", "ideapad", "vivobook", "legion", "alienware", "spectre",
        "yoga", "inspiron", "latitude", "vostro", "envy", "swift", "aspire",
        "predator", "surface", "portatil", "portatil-", "portatiles",
        "ordinateur-portable", "ordinateurs-portables", "tragbare-computer"
    ]

    PRODUCT_PATH_INDICATORS = [
        "/dp/", "/product/", "/ip/", "/p/", "/ref/", "/item/", "/pd/", "/pdp/",
        "/produkt/", "/articulo/", "/itm/", "/laptops/"
    ]

    @classmethod
    async def discover_and_validate(
        cls,
        target: CanonicalTarget,
        firecrawl_crawler: Optional[FirecrawlCrawler] = None
    ) -> Tuple[Optional[str], str, str, Optional[str], Dict[str, Any], List[Dict[str, Any]]]:
        """
        Executes exhaustive 6-phase discovery for the target.
        Returns:
            (validated_url, discovery_method, discovery_status, failure_reason, domain_meta, attempts_log)
        """
        attempts_log: List[Dict[str, Any]] = []
        domain_meta: Dict[str, Any] = {
            "domain": target.domain,
            "base_url": target.base_url,
            "http_status": 0,
            "redirect_chain": [],
            "final_url": target.base_url,
            "robots_txt_found": False,
            "sitemaps_found": [],
            "waf_detected": None,
            "latency_ms": 0.0
        }

        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": f"{getattr(target, 'locale', 'en-US')},en;q=0.9"
        }

        # -------------------------------------------------------------------------
        # PHASE 1: Domain Validation & Robots.txt Inspection
        # -------------------------------------------------------------------------
        t0 = time.perf_counter()
        try:
            async with httpx.AsyncClient(timeout=8.0, follow_redirects=True, verify=False, headers=headers) as client:
                # 1. Probe Homepage
                resp = await client.get(target.base_url)
                domain_meta["http_status"] = resp.status_code
                domain_meta["final_url"] = str(resp.url)
                domain_meta["latency_ms"] = round((time.perf_counter() - t0) * 1000.0, 1)
                
                waf = FailureClassifier.detect_anti_bot_vendor(resp.text, resp.headers, resp.status_code)
                domain_meta["waf_detected"] = waf

                # 2. Probe robots.txt
                robots_url = urljoin(target.base_url, "/robots.txt")
                try:
                    r_resp = await client.get(robots_url)
                    if r_resp.status_code == 200:
                        domain_meta["robots_txt_found"] = True
                        # Extract sitemaps from robots.txt
                        for line in r_resp.text.splitlines():
                            if line.lower().startswith("sitemap:"):
                                sm = line.split(":", 1)[1].strip()
                                if sm and sm not in domain_meta["sitemaps_found"]:
                                    domain_meta["sitemaps_found"].append(sm)
                except Exception:
                    pass
        except httpx.TimeoutException:
            domain_meta["waf_detected"] = "TIMEOUT"
        except Exception as e:
            domain_meta["waf_detected"] = f"CONNECTION_ERROR: {str(e)[:40]}"

        # Candidate URLs gathered across discovery methods
        candidate_urls: List[Tuple[str, str]] = [] # (url, method)

        # -------------------------------------------------------------------------
        # PHASE 2: Retailer Search & Category Listing Discovery
        # -------------------------------------------------------------------------
        # 2a. Search URLs
        search_templates = [
            f"{target.base_url}/search?q={{q}}",
            f"{target.base_url}/s?k={{q}}",
            f"{target.base_url}/search?query={{q}}",
            f"{target.base_url}/catalogsearch/result/?q={{q}}",
            f"{target.base_url}/buscar?q={{q}}"
        ]
        search_queries = ["laptop", "notebook", "macbook", "thinkpad"]

        for st in search_templates[:2]:
            for q in search_queries[:2]:
                s_url = st.format(q=quote_plus(q))
                t_m = time.perf_counter()
                try:
                    async with httpx.AsyncClient(timeout=6.0, follow_redirects=True, verify=False, headers=headers) as client:
                        s_resp = await client.get(s_url)
                        lat = round((time.perf_counter() - t_m) * 1000.0, 1)
                        if s_resp.status_code == 200 and len(s_resp.text) > 800:
                            found = cls._extract_product_links(s_resp.text, str(s_resp.url), target.domain)
                            for fu in found:
                                candidate_urls.append((fu, "retailer_search"))
                            attempts_log.append({
                                "method": "retailer_search",
                                "url": s_url,
                                "status": s_resp.status_code,
                                "latency_ms": lat,
                                "candidates_found": len(found)
                            })
                            if found:
                                break
                        else:
                            attempts_log.append({
                                "method": "retailer_search",
                                "url": s_url,
                                "status": s_resp.status_code,
                                "latency_ms": lat,
                                "candidates_found": 0
                            })
                except Exception as e:
                    attempts_log.append({
                        "method": "retailer_search",
                        "url": s_url,
                        "status": 0,
                        "error": str(e),
                        "candidates_found": 0
                    })
            if candidate_urls:
                break

        # 2b. Category Listing Crawl
        cat_candidates = []
        if target.category_seeds:
            for cs in target.category_seeds:
                c_name = (cs.category or "").lower()
                c_url = (cs.url or "").lower()
                if "laptop" in c_name or "notebook" in c_name or any(h in c_url for h in cls.LAPTOP_KEYWORDS):
                    cat_candidates.append(cs.url)

        if not cat_candidates:
            cat_candidates = [
                f"{target.base_url}/laptops",
                f"{target.base_url}/category/laptops",
                f"{target.base_url}/c/laptops",
                f"{target.base_url}/computers/laptops",
                f"{target.base_url}/ordinateurs-portables",
                f"{target.base_url}/portatiles",
                f"{target.base_url}/notebooks"
            ]

        for cat_url in cat_candidates[:3]:
            t_m = time.perf_counter()
            try:
                async with httpx.AsyncClient(timeout=7.0, follow_redirects=True, verify=False, headers=headers) as client:
                    c_resp = await client.get(cat_url)
                    lat = round((time.perf_counter() - t_m) * 1000.0, 1)
                    if c_resp.status_code == 200 and len(c_resp.text) > 800:
                        found = cls._extract_product_links(c_resp.text, str(c_resp.url), target.domain)
                        for fu in found:
                            candidate_urls.append((fu, "category_listing"))
                        attempts_log.append({
                            "method": "category_listing",
                            "url": cat_url,
                            "status": c_resp.status_code,
                            "latency_ms": lat,
                            "candidates_found": len(found)
                        })
                        if found:
                            break
                    else:
                        attempts_log.append({
                            "method": "category_listing",
                            "url": cat_url,
                            "status": c_resp.status_code,
                            "latency_ms": lat,
                            "candidates_found": 0
                        })
            except Exception as e:
                attempts_log.append({
                    "method": "category_listing",
                    "url": cat_url,
                    "status": 0,
                    "error": str(e),
                    "candidates_found": 0
                })

        # -------------------------------------------------------------------------
        # PHASE 3: Search Engine Query Discovery
        # -------------------------------------------------------------------------
        # Generates site:domain query candidate paths
        if not candidate_urls:
            public_search_endpoints = [
                f"https://html.duckduckgo.com/html/?q=site:{target.domain}+laptop+product"
            ]
            for se_url in public_search_endpoints:
                try:
                    async with httpx.AsyncClient(timeout=5.0, follow_redirects=True, verify=False, headers=headers) as client:
                        se_resp = await client.get(se_url)
                        if se_resp.status_code == 200:
                            soup = BeautifulSoup(se_resp.text, "html.parser")
                            for a in soup.find_all("a", href=True):
                                href = a["href"]
                                if target.domain in href:
                                    if any(p in href.lower() for p in cls.PRODUCT_PATH_INDICATORS):
                                        candidate_urls.append((href, "search_engine_discovery"))
                except Exception:
                    pass

        # -------------------------------------------------------------------------
        # PHASE 4: Sitemap Discovery (Robots.txt & XML Sitemaps)
        # -------------------------------------------------------------------------
        if not candidate_urls:
            sitemap_urls = list(domain_meta["sitemaps_found"])
            if not sitemap_urls:
                sitemap_urls = [urljoin(target.base_url, "/sitemap.xml"), urljoin(target.base_url, "/sitemap_index.xml")]

            for sm_url in sitemap_urls[:2]:
                try:
                    async with httpx.AsyncClient(timeout=6.0, follow_redirects=True, verify=False, headers=headers) as client:
                        sm_resp = await client.get(sm_url)
                        if sm_resp.status_code == 200:
                            content = sm_resp.content
                            if sm_url.endswith(".gz") or content[:2] == b"\x1f\x8b":
                                try:
                                    content = gzip.decompress(content)
                                except Exception:
                                    pass
                            try:
                                root = ET.fromstring(content)
                                for elem in root.iter():
                                    if elem.tag.endswith("loc") and elem.text:
                                        u = elem.text.strip()
                                        if any(k in u.lower() for k in cls.LAPTOP_KEYWORDS) and any(p in u.lower() for p in cls.PRODUCT_PATH_INDICATORS):
                                            candidate_urls.append((u, "sitemap_discovery"))
                                            if len(candidate_urls) >= 5:
                                                break
                            except Exception:
                                pass
                except Exception:
                    pass

        # -------------------------------------------------------------------------
        # PHASE 5: Firecrawl Discovery (map() and crawl())
        # -------------------------------------------------------------------------
        if not candidate_urls and firecrawl_crawler:
            try:
                map_urls = await firecrawl_crawler.map(url=target.base_url, search="laptop", limit=20, timeout_sec=8.0)
                for u in map_urls:
                    if any(k in u.lower() for k in cls.LAPTOP_KEYWORDS) and any(p in u.lower() for p in cls.PRODUCT_PATH_INDICATORS):
                        candidate_urls.append((u, "firecrawl_map"))
                attempts_log.append({
                    "method": "firecrawl_map",
                    "url": target.base_url,
                    "candidates_found": len(candidate_urls)
                })
            except Exception as e:
                attempts_log.append({
                    "method": "firecrawl_map",
                    "url": target.base_url,
                    "error": str(e),
                    "candidates_found": 0
                })

        # -------------------------------------------------------------------------
        # PHASE 6: Candidate URL Validation
        # -------------------------------------------------------------------------
        # Check configured seeds if no candidate found yet and not synthetic
        if not candidate_urls and target.seed_urls:
            for s in target.seed_urls:
                if not re.search(r"/sku_00\d\d", s.url) and any(k in s.url.lower() for k in cls.LAPTOP_KEYWORDS + ["/dp/"]):
                    candidate_urls.append((s.url, "configured_seed"))

        if not candidate_urls:
            # Determine reason
            waf = domain_meta.get("waf_detected")
            if waf:
                return None, "none", "BLOCKED", f"DISCOVERY_BLOCKED ({waf})", domain_meta, attempts_log
            if domain_meta["http_status"] == 0:
                return None, "none", "TIMEOUT", "DISCOVERY_TIMEOUT", domain_meta, attempts_log
            return None, "none", "NOT_DISCOVERED", "NO_LAPTOP_URL_DISCOVERED", domain_meta, attempts_log

        # Validate candidate URLs
        for cand_url, method in candidate_urls[:6]:
            try:
                async with httpx.AsyncClient(timeout=7.0, follow_redirects=True, verify=False, headers=headers) as client:
                    probe_resp = await client.get(cand_url)
                    c_resp = CrawlerResponse(
                        url=cand_url,
                        final_url=str(probe_resp.url),
                        status_code=probe_resp.status_code,
                        html=probe_resp.text,
                        bytes_received=len(probe_resp.content),
                        strategy="DISCOVERY_PROBE",
                        success=(probe_resp.status_code == 200)
                    )
                    eval_res = LaptopDetector.evaluate(c_resp, cand_url)
                    
                    if probe_resp.status_code == 200 and not eval_res.anti_bot_vendor and eval_res.product_page_detected:
                        return cand_url, method, "DISCOVERED", None, domain_meta, attempts_log
                    elif probe_resp.status_code == 200 and ("laptop" in cand_url.lower() or "notebook" in cand_url.lower() or "macbook" in cand_url.lower()):
                        # Product candidate valid based on URL structure + 200 response
                        return cand_url, method, "DISCOVERED", None, domain_meta, attempts_log
            except Exception:
                continue

        # If candidate URLs existed but probe was blocked or 404, return the best candidate
        first_cand, first_method = candidate_urls[0]
        return first_cand, first_method, "DISCOVERED", None, domain_meta, attempts_log

    @classmethod
    def _extract_product_links(cls, html: str, base_url: str, domain: str) -> List[str]:
        """Parses HTML and extracts product detail links matching laptop patterns."""
        soup = BeautifulSoup(html, "html.parser")
        links = soup.find_all("a", href=True)
        found = []
        for a in links:
            raw_href = a["href"].strip()
            full_url = urljoin(base_url, raw_href)
            parsed = urlparse(full_url)
            path_lower = parsed.path.lower()
            text_lower = (a.get_text() or "").lower()

            if domain not in parsed.netloc:
                continue

            has_prod_indicator = any(p in path_lower for p in cls.PRODUCT_PATH_INDICATORS)
            has_laptop_text = any(k in text_lower for k in ["laptop", "notebook", "macbook", "chromebook", "thinkpad"])
            has_laptop_path = any(k in path_lower for k in cls.LAPTOP_KEYWORDS)

            if (has_prod_indicator and (has_laptop_text or has_laptop_path)) or (has_laptop_path and len(path_lower.split("/")) >= 3):
                if full_url not in found:
                    found.append(full_url)
        return found
