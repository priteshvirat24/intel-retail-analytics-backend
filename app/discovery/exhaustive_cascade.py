"""
Exhaustive 10-Method Laptop Product URL Discovery Cascade.
Implements all 10 independent discovery methods with multi-language terminology support.
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
from app.crawlers.playwright import PlaywrightCrawler
from app.evaluation.failures import FailureClassifier
from app.evaluation.laptop_validator import LaptopValidator, LaptopValidationResult
from app.crawlers.base import CrawlerResponse


class ExhaustiveCascadeEngine:
    """Orchestrates all 10 independent discovery methods per retailer target."""

    MULTILANG_SEARCH_TERMS = {
        "en": ["laptop", "notebook", "gaming laptop", "macbook"],
        "de": ["laptop", "notebook", "gaming notebook"],
        "fr": ["ordinateur portable", "pc portable", "macbook"],
        "it": ["portatile", "notebook", "pc portatile"],
        "es": ["portatil", "portatiles", "ordenador portatil", "notebook"],
        "pt": ["notebook", "laptop", "computador portatil"],
        "pl": ["laptop", "notebook", "laptopy"],
        "ko": ["노트북", "맥북", "게이밍 노트북"],
        "ja": ["ノートパソコン", "ノートPC", "MacBook"],
        "vi": ["laptop", "máy tính xách tay"],
        "tr": ["laptop", "dizüstü bilgisayar", "notebook"],
        "id": ["laptop", "notebook", "laptop gaming"]
    }

    PRODUCT_PATH_INDICATORS = [
        "/dp/", "/product/", "/ip/", "/p/", "/ref/", "/item/", "/pd/", "/pdp/",
        "/produkt/", "/articulo/", "/itm/", "/laptops/", "/ordinateur-portable/",
        "/portatiles/", "/notebooks/", "/pc-portatili/"
    ]

    @classmethod
    async def discover_and_validate(
        cls,
        target: CanonicalTarget,
        firecrawl_crawler: Optional[FirecrawlCrawler] = None,
        playwright_crawler: Optional[PlaywrightCrawler] = None
    ) -> Tuple[Optional[str], str, str, Optional[str], Optional[LaptopValidationResult], List[Dict[str, Any]], Dict[str, Any]]:
        """
        Executes full 10-method cascade for target.
        Returns:
            (validated_url, discovery_method, discovery_status, failure_reason, val_res, attempts_log, domain_meta)
        """
        attempts_log: List[Dict[str, Any]] = []
        domain_meta: Dict[str, Any] = {
            "domain": target.domain,
            "base_url": target.base_url,
            "http_status": 0,
            "final_url": target.base_url,
            "robots_txt_found": False,
            "sitemaps_found": [],
            "waf_detected": None,
            "latency_ms": 0.0
        }

        lang = (target.locale or "en")[:2].lower()
        search_terms = cls.MULTILANG_SEARCH_TERMS.get(lang, cls.MULTILANG_SEARCH_TERMS["en"])
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": f"{getattr(target, 'locale', 'en-US')},en;q=0.9"
        }

        candidate_pool: List[Tuple[str, str]] = [] # (url, method_name)

        # -------------------------------------------------------------------------
        # METHOD 1: Retailer Homepage & Navigation Menus
        # -------------------------------------------------------------------------
        t0 = time.perf_counter()
        homepage_html = ""
        try:
            async with httpx.AsyncClient(timeout=8.0, follow_redirects=True, verify=False, headers=headers) as client:
                hp_resp = await client.get(target.base_url)
                lat = round((time.perf_counter() - t0) * 1000.0, 1)
                domain_meta["http_status"] = hp_resp.status_code
                domain_meta["final_url"] = str(hp_resp.url)
                domain_meta["latency_ms"] = lat
                waf = FailureClassifier.detect_anti_bot_vendor(hp_resp.text, hp_resp.headers, hp_resp.status_code)
                domain_meta["waf_detected"] = waf

                if hp_resp.status_code == 200 and len(hp_resp.text) > 500:
                    homepage_html = hp_resp.text
                    found = cls._extract_links(hp_resp.text, str(hp_resp.url), target.domain, search_terms)
                    for u in found:
                        candidate_pool.append((u, "method_1_homepage_nav"))
                    attempts_log.append({
                        "method": "METHOD_1_HOMEPAGE",
                        "status": "SUCCESS" if found else "NO_LINKS",
                        "http_status": hp_resp.status_code,
                        "latency_ms": lat,
                        "candidates_found": len(found)
                    })
                else:
                    attempts_log.append({
                        "method": "METHOD_1_HOMEPAGE",
                        "status": "BLOCKED" if waf else "HTTP_ERROR",
                        "http_status": hp_resp.status_code,
                        "latency_ms": lat,
                        "candidates_found": 0
                    })
        except Exception as e:
            attempts_log.append({
                "method": "METHOD_1_HOMEPAGE",
                "status": "CONNECTION_ERROR",
                "error": str(e),
                "candidates_found": 0
            })

        # -------------------------------------------------------------------------
        # METHOD 2: Robots.txt Inspection & Allowed Paths
        # -------------------------------------------------------------------------
        robots_url = urljoin(target.base_url, "/robots.txt")
        t0 = time.perf_counter()
        try:
            async with httpx.AsyncClient(timeout=6.0, follow_redirects=True, verify=False, headers=headers) as client:
                r_resp = await client.get(robots_url)
                lat = round((time.perf_counter() - t0) * 1000.0, 1)
                if r_resp.status_code == 200:
                    domain_meta["robots_txt_found"] = True
                    for line in r_resp.text.splitlines():
                        if line.lower().startswith("sitemap:"):
                            sm = line.split(":", 1)[1].strip()
                            if sm and sm not in domain_meta["sitemaps_found"]:
                                domain_meta["sitemaps_found"].append(sm)
                    attempts_log.append({
                        "method": "METHOD_2_ROBOTS_TXT",
                        "status": "SUCCESS",
                        "sitemaps_found": len(domain_meta["sitemaps_found"]),
                        "latency_ms": lat
                    })
                else:
                    attempts_log.append({
                        "method": "METHOD_2_ROBOTS_TXT",
                        "status": "NOT_FOUND",
                        "http_status": r_resp.status_code,
                        "latency_ms": lat
                    })
        except Exception as e:
            attempts_log.append({"method": "METHOD_2_ROBOTS_TXT", "status": "ERROR", "error": str(e)})

        # -------------------------------------------------------------------------
        # METHOD 3: XML Sitemaps Streaming Recursive Discovery
        # -------------------------------------------------------------------------
        sitemaps_to_try = list(domain_meta["sitemaps_found"]) or [
            urljoin(target.base_url, "/sitemap.xml"),
            urljoin(target.base_url, "/sitemap_index.xml"),
            urljoin(target.base_url, "/products_sitemap.xml")
        ]
        t0 = time.perf_counter()
        sm_found = []
        for sm_url in sitemaps_to_try[:2]:
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
                        root = ET.fromstring(content)
                        for elem in root.iter():
                            if elem.tag.endswith("loc") and elem.text:
                                u = elem.text.strip()
                                if any(k in u.lower() for k in search_terms) and any(p in u.lower() for p in cls.PRODUCT_PATH_INDICATORS):
                                    candidate_pool.append((u, "method_3_sitemap"))
                                    sm_found.append(u)
                                    if len(sm_found) >= 5:
                                        break
            except Exception:
                pass
        attempts_log.append({
            "method": "METHOD_3_XML_SITEMAP",
            "status": "SUCCESS" if sm_found else "NO_MATCH",
            "candidates_found": len(sm_found)
        })

        # -------------------------------------------------------------------------
        # METHOD 4: Website Search Endpoints
        # -------------------------------------------------------------------------
        search_templates = [
            f"{target.base_url}/search?q={{q}}",
            f"{target.base_url}/s?k={{q}}",
            f"{target.base_url}/search?query={{q}}",
            f"{target.base_url}/catalogsearch/result/?q={{q}}",
            f"{target.base_url}/buscar?q={{q}}"
        ]
        s_found = []
        for st in search_templates[:2]:
            for q in search_terms[:2]:
                s_url = st.format(q=quote_plus(q))
                try:
                    async with httpx.AsyncClient(timeout=6.0, follow_redirects=True, verify=False, headers=headers) as client:
                        sr = await client.get(s_url)
                        if sr.status_code == 200 and len(sr.text) > 800:
                            f_links = cls._extract_links(sr.text, str(sr.url), target.domain, search_terms)
                            for u in f_links:
                                candidate_pool.append((u, "method_4_website_search"))
                                s_found.append(u)
                            if s_found:
                                break
                except Exception:
                    pass
            if s_found:
                break
        attempts_log.append({
            "method": "METHOD_4_WEBSITE_SEARCH",
            "status": "SUCCESS" if s_found else "FAILED",
            "candidates_found": len(s_found)
        })

        # -------------------------------------------------------------------------
        # METHOD 5: Category Navigation & Traversal
        # -------------------------------------------------------------------------
        cat_candidates = []
        if target.category_seeds:
            for cs in target.category_seeds:
                if any(k in cs.category.lower() for k in search_terms) or any(k in cs.url.lower() for k in search_terms):
                    cat_candidates.append(cs.url)

        if not cat_candidates:
            cat_candidates = [
                f"{target.base_url}/laptops",
                f"{target.base_url}/category/laptops",
                f"{target.base_url}/c/laptops",
                f"{target.base_url}/computers/laptops",
                f"{target.base_url}/ordinateurs-portables",
                f"{target.base_url}/portatiles",
                f"{target.base_url}/notebooks",
                f"{target.base_url}/pc-portatili"
            ]

        c_found = []
        for cat_url in cat_candidates[:3]:
            try:
                async with httpx.AsyncClient(timeout=7.0, follow_redirects=True, verify=False, headers=headers) as client:
                    cr = await client.get(cat_url)
                    if cr.status_code == 200 and len(cr.text) > 800:
                        f_links = cls._extract_links(cr.text, str(cr.url), target.domain, search_terms)
                        for u in f_links:
                            candidate_pool.append((u, "method_5_category_nav"))
                            c_found.append(u)
                        if c_found:
                            break
            except Exception:
                pass
        attempts_log.append({
            "method": "METHOD_5_CATEGORY_NAV",
            "status": "SUCCESS" if c_found else "FAILED",
            "candidates_found": len(c_found)
        })

        # -------------------------------------------------------------------------
        # METHOD 6: HTML / JSON-LD / schema.org Extraction from Homepage
        # -------------------------------------------------------------------------
        j_found = []
        if homepage_html:
            soup = BeautifulSoup(homepage_html, "html.parser")
            for s in soup.find_all("script", type="application/ld+json"):
                try:
                    txt = s.string or ""
                    if '"url"' in txt:
                        urls = re.findall(r'https?://[^\s",]+', txt)
                        for u in urls:
                            if target.domain in u and any(k in u.lower() for k in search_terms):
                                candidate_pool.append((u, "method_6_jsonld_extracted"))
                                j_found.append(u)
                except Exception:
                    pass
        attempts_log.append({
            "method": "METHOD_6_JSONLD_EXTRACTION",
            "status": "SUCCESS" if j_found else "NO_LINKS",
            "candidates_found": len(j_found)
        })

        # -------------------------------------------------------------------------
        # METHOD 7: Inferred Known Product URL Patterns
        # -------------------------------------------------------------------------
        # Check configured non-synthetic seeds
        seed_found = []
        if target.seed_urls:
            for s in target.seed_urls:
                if not re.search(r"/sku_00\d\d", s.url) and any(k in s.url.lower() for k in search_terms + ["/dp/"]):
                    candidate_pool.append((s.url, "method_7_inferred_pattern"))
                    seed_found.append(s.url)
        attempts_log.append({
            "method": "METHOD_7_KNOWN_PATTERNS",
            "status": "SUCCESS" if seed_found else "NO_MATCH",
            "candidates_found": len(seed_found)
        })

        # -------------------------------------------------------------------------
        # METHOD 8: Search Engine Query Discovery
        # -------------------------------------------------------------------------
        se_found = []
        if not candidate_pool:
            se_endpoints = [
                f"https://html.duckduckgo.com/html/?q=site:{target.domain}+{search_terms[0]}+product"
            ]
            for se_url in se_endpoints:
                try:
                    async with httpx.AsyncClient(timeout=5.0, follow_redirects=True, verify=False, headers=headers) as client:
                        ser = await client.get(se_url)
                        if ser.status_code == 200:
                            soup = BeautifulSoup(ser.text, "html.parser")
                            for a in soup.find_all("a", href=True):
                                href = a["href"]
                                if target.domain in href and any(p in href.lower() for p in cls.PRODUCT_PATH_INDICATORS):
                                    candidate_pool.append((href, "method_8_search_engine"))
                                    se_found.append(href)
                except Exception:
                    pass
        attempts_log.append({
            "method": "METHOD_8_SEARCH_ENGINE",
            "status": "SUCCESS" if se_found else "NO_MATCH",
            "candidates_found": len(se_found)
        })

        # -------------------------------------------------------------------------
        # METHOD 9: Firecrawl map() Discovery
        # -------------------------------------------------------------------------
        fc_found = []
        if not candidate_pool and firecrawl_crawler:
            try:
                map_urls = await firecrawl_crawler.map(url=target.base_url, search=search_terms[0], limit=20, timeout_sec=8.0)
                for u in map_urls:
                    if any(k in u.lower() for k in search_terms) and any(p in u.lower() for p in cls.PRODUCT_PATH_INDICATORS):
                        candidate_pool.append((u, "method_9_firecrawl_map"))
                        fc_found.append(u)
            except Exception:
                pass
        attempts_log.append({
            "method": "METHOD_9_FIRECRAWL_DISCOVERY",
            "status": "SUCCESS" if fc_found else "FAILED",
            "candidates_found": len(fc_found)
        })

        # -------------------------------------------------------------------------
        # METHOD 10: Playwright Rendered Discovery (For SPA / Dynamic JS)
        # -------------------------------------------------------------------------
        pw_found = []
        if not candidate_pool and playwright_crawler:
            try:
                pw_resp = await playwright_crawler.fetch(target.base_url)
                if pw_resp.success and pw_resp.html:
                    pw_links = cls._extract_links(pw_resp.html, pw_resp.final_url or target.base_url, target.domain, search_terms)
                    for u in pw_links:
                        candidate_pool.append((u, "method_10_playwright_render"))
                        pw_found.append(u)
            except Exception:
                pass
        attempts_log.append({
            "method": "METHOD_10_PLAYWRIGHT_DISCOVERY",
            "status": "SUCCESS" if pw_found else "FAILED",
            "candidates_found": len(pw_found)
        })

        # -------------------------------------------------------------------------
        # VALIDATION PHASE: Deterministic Validation with LaptopValidator
        # -------------------------------------------------------------------------
        if not candidate_pool:
            waf = domain_meta.get("waf_detected")
            if waf:
                return None, "none", "DISCOVERY_BLOCKED", f"DISCOVERY_BLOCKED ({waf})", None, attempts_log, domain_meta
            if domain_meta["http_status"] == 0:
                return None, "none", "DISCOVERY_TIMEOUT", "DISCOVERY_TIMEOUT", None, attempts_log, domain_meta
            return None, "none", "NO_PRODUCT_FOUND", "NO_LAPTOP_URL_DISCOVERED", None, attempts_log, domain_meta

        # Deduplicate candidates
        seen_cand = set()
        deduped_candidates = []
        for u, m in candidate_pool:
            if u not in seen_cand:
                seen_cand.add(u)
                deduped_candidates.append((u, m))

        # Validate candidate URLs using lightweight HTTP probe
        best_cand = None
        best_method = None
        best_val_res = None

        for cand_url, method in deduped_candidates[:8]:
            try:
                async with httpx.AsyncClient(timeout=7.0, follow_redirects=True, verify=False, headers=headers) as client:
                    probe_resp = await client.get(cand_url)
                    c_resp = CrawlerResponse(
                        url=cand_url,
                        final_url=str(probe_resp.url),
                        status_code=probe_resp.status_code,
                        html=probe_resp.text,
                        bytes_received=len(probe_resp.content),
                        strategy="VALIDATION_PROBE",
                        success=(probe_resp.status_code == 200)
                    )
                    val_res = LaptopValidator.validate(c_resp, cand_url, threshold=0.80)

                    if val_res.is_valid_laptop:
                        return cand_url, method, "PRODUCT_URL_VALIDATED", None, val_res, attempts_log, domain_meta
                    elif probe_resp.status_code == 200 and not best_cand:
                        best_cand = cand_url
                        best_method = method
                        best_val_res = val_res
            except Exception:
                continue

        if best_cand:
            return best_cand, best_method, "PRODUCT_URL_FOUND", best_val_res.failure_class if best_val_res else None, best_val_res, attempts_log, domain_meta

        first_u, first_m = deduped_candidates[0]
        return first_u, first_m, "PRODUCT_URL_FOUND", None, None, attempts_log, domain_meta

    @classmethod
    def _extract_links(cls, html: str, base_url: str, domain: str, search_terms: List[str]) -> List[str]:
        soup = BeautifulSoup(html, "html.parser")
        found = []
        for a in soup.find_all("a", href=True):
            raw_href = a["href"].strip()
            full_url = urljoin(base_url, raw_href)
            parsed = urlparse(full_url)
            path_lower = parsed.path.lower()
            text_lower = (a.get_text() or "").lower()

            if domain not in parsed.netloc:
                continue

            has_prod_indicator = any(p in path_lower for p in cls.PRODUCT_PATH_INDICATORS)
            has_term_in_text = any(k in text_lower for k in search_terms)
            has_term_in_path = any(k in path_lower for k in search_terms)

            if (has_prod_indicator and (has_term_in_text or has_term_in_path)) or (has_term_in_path and len(path_lower.split("/")) >= 3):
                if full_url not in found:
                    found.append(full_url)
        return found
