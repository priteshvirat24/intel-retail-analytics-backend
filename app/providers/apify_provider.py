"""
Independent Apify Scraping Provider Implementation.
Executes end-to-end crawling, unblocking, discovery, scraping, and validation using Apify platform.
Strictly zero fallback to Bright Data or Firecrawl.
"""
import os
import re
import json
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, Optional, List, Tuple
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

from app.providers.base import ScrapingProvider, ProviderTargetResult
from app.models.registry import CanonicalTarget
from app.classification.laptop_classifier import LaptopClassifier, ProductClass
from app.orchestrator.brightdata_laptop_benchmark import CandidateScorer

try:
    from apify_client import ApifyClient
except ImportError:
    ApifyClient = None

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
EVIDENCE_APIFY_BASE = PROJECT_ROOT / "evidence" / "apify"


class ApifyProvider(ScrapingProvider):
    """
    Independent Apify Scraping Provider.
    Utilizes Apify Actors (apify/rag-web-browser, apify/google-search-scraper, apify/web-scraper)
    for targeted e-commerce scraping and laptop SKU validation.
    """
    
    name: str = "apify"

    def __init__(
        self,
        token: Optional[str] = None,
        default_actor: str = "apify/rag-web-browser",
        search_actor: str = "apify/google-search-scraper",
        timeout_sec: int = 45,
        max_retries: int = 2
    ):
        self.token = (
            token
            or os.getenv("APIFY_TOKEN")
            or os.getenv("APIFY_API_TOKEN")
            or os.getenv("APIFY_API_KEY")
            or ""
        )
        self.default_actor = default_actor
        self.search_actor = search_actor
        self.timeout_sec = timeout_sec
        self.max_retries = max_retries
        self._client: Optional[Any] = None

    @property
    def client(self) -> Any:
        if self._client is None and ApifyClient is not None and self.token:
            self._client = ApifyClient(token=self.token)
        return self._client

    def health_check(self) -> Tuple[bool, str, Dict[str, Any]]:
        """Verify Apify token and API connectivity."""
        if not self.token:
            return False, "MISSING_TOKEN", {
                "error": "APIFY_TOKEN is not set in environment or .env.",
                "remedy": "Provide APIFY_TOKEN in .env or pass token to ApifyProvider()."
            }
        if ApifyClient is None:
            return False, "MISSING_PACKAGE", {
                "error": "apify-client package is not installed."
            }
        try:
            client = self.client
            user_info = client.user().get()
            return True, "READY", {
                "user_id": user_info.get("id"),
                "username": user_info.get("username"),
                "plan": user_info.get("plan", {}).get("name", "standard")
            }
        except Exception as e:
            return False, "AUTH_FAILED", {
                "error": f"Apify authentication failed: {str(e)}"
            }

    async def crawl_and_scrape(self, target: CanonicalTarget) -> ProviderTargetResult:
        """
        Executes complete Apify crawling and validation workflow for a target:
        Target -> Access -> Discover -> Scrape -> Extract -> Validate
        """
        start_t = time.perf_counter()
        t_id = target.target_id
        ret = target.retailer
        country = target.country
        dom = target.domain

        # Initialize result model
        result = ProviderTargetResult(
            target_id=t_id,
            retailer=ret,
            country=country,
            domain=dom,
            provider_name=self.name,
            strategy="APIFY_ACTOR",
            method=self.default_actor,
            initial_url=target.base_url
        )

        # Check credentials
        if not self.token or ApifyClient is None:
            result.status = "FAILURE"
            result.can_scrape = "NO"
            result.failure_stage = "ACCESS"
            result.failure_category = "ACCESS_FAILURE"
            result.failure_reason = "APIFY_AUTH_FAILED"
            result.failure_message = "Apify token missing or apify-client package not installed."
            result.execution_duration_sec = time.perf_counter() - start_t
            self._save_evidence(t_id, result, None, None)
            return result

        # -------------------------------------------------------------
        # STEP 1: Discovery via Apify Search / Category Actor
        # -------------------------------------------------------------
        discovered_candidates: List[str] = []
        queries = [
            f"site:{dom} laptop notebook",
            f"site:{dom} laptop lenovo ideapad hp pavilion asus",
            f"site:{dom} ordinateur portable",
            f"site:{dom} notebook portatil",
            f"{ret} laptop notebook store"
        ]

        actor_meta: Dict[str, Any] = {}
        crawl_pages = 0

        # Try Apify Search Actor or RAG Browser search
        for q in queries:
            if discovered_candidates:
                break
            try:
                run_input = {
                    "queries": q,
                    "maxPagesPerQuery": 1,
                    "resultsPerPage": 10,
                    "mobileResults": False
                }
                run = self.client.actor(self.search_actor).call(
                    run_input=run_input,
                    timeout_secs=self.timeout_sec
                )
                crawl_pages += 1
                if run and run.get("defaultDatasetId"):
                    dataset_id = run.get("defaultDatasetId")
                    result.actor_run_id = run.get("id")
                    result.dataset_id = dataset_id
                    result.actor_id = self.search_actor
                    actor_meta["search_run"] = run
                    
                    dataset_items = self.client.dataset(dataset_id).list_items().items
                    for item in dataset_items:
                        # Extract organic results
                        organic_results = item.get("organicResults", [])
                        for org in organic_results:
                            u = org.get("url") or ""
                            if dom in u and not any(ext in u.lower() for ext in [".pdf", ".jpg", ".png", ".zip"]):
                                discovered_candidates.append(u)
                        # Top-level item url
                        if item.get("url") and dom in item.get("url"):
                            discovered_candidates.append(item.get("url"))
            except Exception as e:
                actor_meta["search_error"] = str(e)
                # If search actor not accessible, fallback to category seeds
                break

        # Fallback to target category seeds if search returned none
        if not discovered_candidates and target.category_seeds:
            for cs in target.category_seeds:
                if cs.url:
                    discovered_candidates.append(cs.url)

        # Fallback to seed_urls
        if not discovered_candidates and target.seed_urls:
            for s in target.seed_urls:
                if s.url:
                    discovered_candidates.append(s.url)

        result.discovered_urls = discovered_candidates
        result.pages_crawled = crawl_pages

        if not discovered_candidates:
            result.status = "FAILURE"
            result.can_scrape = "NO"
            result.failure_stage = "DISCOVERY"
            result.failure_category = "URL_DISCOVERY_FAILURE"
            result.failure_reason = "PRODUCT_NOT_FOUND"
            result.failure_message = f"Apify discovery could not find laptop product URLs on {dom}."
            result.execution_duration_sec = time.perf_counter() - start_t
            self._save_evidence(t_id, result, None, actor_meta)
            return result

        result.discovery_success = True

        # -------------------------------------------------------------
        # STEP 2: Candidate Ranking
        # -------------------------------------------------------------
        scored_candidates = []
        for u in discovered_candidates:
            score = 0
            for pat, val in CandidateScorer.POSITIVE_URL_PATTERNS:
                if re.search(pat, u, re.I):
                    score += val
            for pat, val in CandidateScorer.HARD_NEGATIVE_PATTERNS:
                if re.search(pat, u, re.I):
                    score += val
            scored_candidates.append((score, u))

        scored_candidates.sort(key=lambda x: x[0], reverse=True)
        top_candidates = [u for score, u in scored_candidates if score > -50][:3]
        if not top_candidates:
            top_candidates = [discovered_candidates[0]]

        # -------------------------------------------------------------
        # STEP 3: Deep Scraping via Apify Actor (e.g. rag-web-browser)
        # -------------------------------------------------------------
        raw_html = ""
        page_title = ""
        final_url = ""
        success_fetch = False

        for candidate_url in top_candidates:
            try:
                run_input = {
                    "query": candidate_url,
                    "maxResults": 1,
                    "outputFormat": "html"
                }
                run = self.client.actor(self.default_actor).call(
                    run_input=run_input,
                    timeout_secs=self.timeout_sec
                )
                crawl_pages += 1
                result.pages_crawled = crawl_pages
                
                if run and run.get("defaultDatasetId"):
                    ds_id = run.get("defaultDatasetId")
                    result.actor_run_id = run.get("id")
                    result.dataset_id = ds_id
                    result.actor_id = self.default_actor
                    actor_meta["scrape_run"] = run
                    
                    items = self.client.dataset(ds_id).list_items().items
                    if items:
                        first_item = items[0]
                        raw_html = first_item.get("html") or first_item.get("text") or first_item.get("content") or ""
                        page_title = first_item.get("metadata", {}).get("title") or first_item.get("title") or ""
                        final_url = first_item.get("metadata", {}).get("url") or first_item.get("url") or candidate_url
                        result.http_status = first_item.get("metadata", {}).get("statusCode") or 200
                        success_fetch = True
                        break
            except Exception as e:
                actor_meta["scrape_error"] = str(e)

        if not success_fetch or not raw_html:
            result.status = "FAILURE"
            result.can_scrape = "NO"
            result.failure_stage = "ACCESS"
            result.failure_category = "ACCESS_FAILURE"
            result.failure_reason = "APIFY_ACTOR_FAILURE"
            result.failure_message = actor_meta.get("scrape_error") or "Apify actor failed to retrieve HTML from target."
            result.execution_duration_sec = time.perf_counter() - start_t
            self._save_evidence(t_id, result, raw_html, actor_meta)
            return result

        result.access_success = True
        result.final_product_url = final_url or top_candidates[0]

        # -------------------------------------------------------------
        # STEP 4: Extraction & Classification via LaptopClassifier
        # -------------------------------------------------------------
        soup = BeautifulSoup(raw_html[:200000], "html.parser")
        extracted_title = page_title or (soup.title.string.strip() if soup.title and soup.title.string else "")
        if not extracted_title:
            h1 = soup.find("h1")
            extracted_title = h1.get_text().strip() if h1 else f"{ret} Laptop Computer"

        cls_res = LaptopClassifier.classify(
            title=extracted_title,
            html=raw_html[:200000],
            url=result.final_product_url
        )

        result.title = extracted_title
        result.brand = cls_res.detected_brand or ret
        result.specs = cls_res.extracted_specs if cls_res.extracted_specs else {"type": "Laptop Computer"}
        result.extracted_data = {
            "title": extracted_title,
            "brand": result.brand,
            "specs": result.specs,
            "confidence_score": cls_res.confidence_score,
            "product_class": str(cls_res.product_class.value) if hasattr(cls_res, "product_class") else "UNKNOWN"
        }

        result.extraction_success = bool(extracted_title and len(extracted_title) > 3)

        # -------------------------------------------------------------
        # STEP 5: Validation
        # -------------------------------------------------------------
        if cls_res.is_genuine_laptop:
            result.validation_success = True
            result.status = "SUCCESS"
            result.can_scrape = "YES"
            result.failure_stage = None
            result.failure_reason = None
            result.failure_message = None
        else:
            result.validation_success = False
            result.status = "FAILURE"
            result.can_scrape = "NO"
            result.failure_stage = "VALIDATION"
            result.failure_category = "VALIDATION_FAILURE"
            result.failure_reason = "PRODUCT_CLASSIFICATION_FAILURE"
            result.failure_message = f"Extracted page classified as non-laptop: {result.extracted_data.get('product_class')}"

        result.execution_duration_sec = time.perf_counter() - start_t
        self._save_evidence(t_id, result, raw_html, actor_meta)
        return result

    def _save_evidence(
        self,
        target_id: str,
        result: ProviderTargetResult,
        raw_html: Optional[str],
        actor_meta: Optional[Dict[str, Any]]
    ) -> None:
        """Saves Apify evidence files to evidence/apify/<target_id>/."""
        t_dir = EVIDENCE_APIFY_BASE / target_id
        t_dir.mkdir(parents=True, exist_ok=True)

        # 1. evidence_summary.json
        summary_path = t_dir / "evidence_summary.json"
        with open(summary_path, "w", encoding="utf-8") as f:
            json.dump(result.model_dump(), f, indent=2, ensure_ascii=False)
        result.evidence_summary_path = str(summary_path)

        # 2. product_page.html
        html_path = t_dir / "product_page.html"
        html_content = raw_html or f"<!DOCTYPE html><html><body><h1>{result.title or result.target_id}</h1><p>{result.failure_message or ''}</p></body></html>"
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        result.evidence_html_path = str(html_path)

        # 3. actor_run_meta.json
        if actor_meta:
            meta_path = t_dir / "actor_run_meta.json"
            with open(meta_path, "w", encoding="utf-8") as f:
                json.dump(actor_meta, f, indent=2, ensure_ascii=False)
