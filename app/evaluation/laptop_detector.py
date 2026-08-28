"""
Laptop Product Page Detector & Crawlability Evaluator.
Rigorously distinguishes transport reachability from genuine product crawlability.
A page is CRAWLABLE only when retrieved content contains real laptop product content.
"""
import re
from typing import Dict, Any, Optional, Tuple, List
from bs4 import BeautifulSoup
from pydantic import BaseModel, Field

from app.crawlers.base import CrawlerResponse
from app.evaluation.failures import FailureClassifier


class LaptopCrawlEvaluation(BaseModel):
    """Rigorous evaluation of crawlability for a single strategy attempt."""
    strategy: str
    endpoint_reachable: bool = False
    http_status: int = 0
    response_received: bool = False
    content_bytes: int = 0
    response_time_ms: float = 0.0

    # Crawlability Dimensions
    product_page_detected: bool = False
    product_content_detected: bool = False
    crawlable: bool = False

    # Evidence & Failure Attribution
    detected_product_title: Optional[str] = None
    detected_laptop_keywords: List[str] = Field(default_factory=list)
    anti_bot_vendor: Optional[str] = None
    failure_reason: Optional[str] = None
    evidence_summary: Optional[str] = None


class LaptopDetector:
    """Evaluates whether HTML / Markdown contains authentic laptop product-page content."""

    LAPTOP_KEYWORDS = [
        "laptop", "notebook", "macbook", "chromebook", "thinkpad", "zenbook",
        "pavilion", "ideapad", "vivobook", "legion", "alienware", "spectre",
        "yoga", "inspiron", "latitude", "vostro", "envy", "swift", "aspire",
        "predator", "blade", "surface pro", "surface laptop", "portatil", "portátil",
        "ordinateur portable", "portatiles", "tragbarer computer", "gaming laptop",
        "intel core", "ryzen", "apple m1", "apple m2", "apple m3", "apple m4",
        "13.3\"", "14\"", "15.6\"", "16\"", "17.3\"", "ram", "ssd", "gb ram", "gb ssd"
    ]

    BOT_PHRASES = [
        "robot check", "captcha", "cf-turnstile", "verify you are human", "please verify",
        "access denied", "blocked", "forbidden", "just a moment...", "datadome",
        "perimeterx", "kasada", "please enable javascript", "security check"
    ]

    @classmethod
    def evaluate(cls, response: CrawlerResponse, expected_url: str) -> LaptopCrawlEvaluation:
        """
        Evaluates a raw CrawlerResponse to separate transport reachability from crawlability.
        """
        eval_res = LaptopCrawlEvaluation(
            strategy=response.strategy,
            endpoint_reachable=response.status_code > 0,
            http_status=response.status_code,
            response_received=bool(response.html or response.markdown or response.error_message),
            content_bytes=response.bytes_received or len(response.html or response.markdown or ""),
            response_time_ms=response.response_time_ms
        )

        # 1. Transport failures
        if response.status_code == 0:
            err = (response.error_message or "").lower()
            if "timeout" in err:
                eval_res.failure_reason = "CONNECTION_TIMEOUT" if response.strategy != "FIRECRAWL" else "FIRECRAWL_TIMEOUT"
            elif "econnrefused" in err or "refused" in err:
                eval_res.failure_reason = "DNS_RESOLUTION_FAILED" if response.strategy != "FIRECRAWL" else "FIRECRAWL_SERVICE_UNAVAILABLE"
            elif "tls" in err or "ssl" in err:
                eval_res.failure_reason = "TLS_ERROR"
            else:
                eval_res.failure_reason = "CONNECTION_RESET"
            return eval_res

        # 2. HTTP status code failures
        if response.status_code == 404:
            eval_res.failure_reason = "HTTP_404_NOT_FOUND"
            return eval_res
        if response.status_code == 403:
            eval_res.failure_reason = "HTTP_403_FORBIDDEN"
        elif response.status_code == 429:
            eval_res.failure_reason = "HTTP_429_RATE_LIMITED"
        elif response.status_code >= 500:
            eval_res.failure_reason = "HTTP_5XX_SERVER_ERROR"

        html = response.html or ""
        markdown = response.markdown or ""
        combined_text = (html + " " + markdown).lower()

        # 3. Detect anti-bot vendor
        vendor = FailureClassifier.detect_anti_bot_vendor(html, response.headers or {}, response.status_code)
        eval_res.anti_bot_vendor = vendor

        # 4. Detect challenge / bot wall
        if any(bp in combined_text for bp in ["robot check", "captcha", "cf-turnstile", "recaptcha", "hcaptcha"]):
            eval_res.failure_reason = "CAPTCHA_PAGE" if not vendor else f"{vendor.upper().replace(' ', '_')}_CHALLENGE"
            return eval_res

        if vendor or any(bp in combined_text for bp in ["just a moment...", "access denied", "blocked", "forbidden", "security check"]):
            eval_res.failure_reason = "BOT_CHALLENGE_PAGE" if not vendor else f"{vendor.upper().replace(' ', '_')}_BLOCK"
            return eval_res

        # 5. Detect empty or unrendered SPA shell
        if len(html.strip()) < 100 and len(markdown.strip()) < 50:
            eval_res.failure_reason = "EMPTY_RESPONSE"
            return eval_res

        if any(spa in combined_text for spa in ['<div id="root"></div>', '<div id="app"></div>', 'please enable javascript']) and len(html) < 2500:
            eval_res.failure_reason = "SPA_SHELL_ONLY"
            return eval_res

        # If HTTP status was already 403/429/500, return now
        if eval_res.failure_reason:
            return eval_res

        # 6. Parse Content & Detect Laptop Product Page
        soup = BeautifulSoup(html, "html.parser") if html else None
        extracted_title = ""
        has_product_schema = False
        has_h1 = False

        if soup:
            # Check Title / H1
            h1 = soup.find("h1")
            if h1 and len(h1.get_text(strip=True)) > 5:
                extracted_title = h1.get_text(strip=True)
                has_h1 = True
            elif soup.title and len(soup.title.get_text(strip=True)) > 5:
                extracted_title = soup.title.get_text(strip=True)

            # Check JSON-LD Product
            for s in soup.find_all("script", type="application/ld+json"):
                txt = s.string or ""
                if '"@type"' in txt and any(t in txt for t in ['"Product"', '"IndividualProduct"', '"Laptop"']):
                    has_product_schema = True
                    break

            # Check OpenGraph product
            og_type = soup.find("meta", property="og:type")
            if og_type and "product" in (og_type.get("content") or "").lower():
                has_product_schema = True

        elif markdown:
            lines = [l.strip() for l in markdown.split("\n") if l.strip()]
            for l in lines:
                if l.startswith("# "):
                    extracted_title = l[2:].strip()
                    has_h1 = True
                    break
            if not extracted_title and lines:
                extracted_title = lines[0]

        eval_res.detected_product_title = extracted_title

        # Reject generic non-product pages
        title_lower = extracted_title.lower()
        if any(gen in title_lower for gen in ["home page", "homepage", "welcome to", "category", "search results", "404 not found", "error"]):
            eval_res.failure_reason = "WRONG_PAGE"
            return eval_res

        # Check for laptop keywords in title + page body
        matched_keywords = []
        for kw in cls.LAPTOP_KEYWORDS:
            if kw in title_lower or (soup and kw in combined_text[:10000]):
                matched_keywords.append(kw)

        eval_res.detected_laptop_keywords = matched_keywords[:8]

        # Determine product_page_detected
        eval_res.product_page_detected = (has_product_schema or has_h1 or len(extracted_title) > 10)

        # Determine product_content_detected
        eval_res.product_content_detected = bool(matched_keywords) and len(extracted_title) > 5

        # Determine crawlable
        if eval_res.product_page_detected and eval_res.product_content_detected:
            eval_res.crawlable = True
            eval_res.evidence_summary = (
                f"Laptop Product Title: '{extracted_title[:80]}' | "
                f"Keywords: {', '.join(matched_keywords[:4])} | "
                f"Schema/H1: {'Yes' if (has_product_schema or has_h1) else 'No'} | "
                f"Bytes: {eval_res.content_bytes:,} B"
            )
        else:
            if not eval_res.product_page_detected:
                eval_res.failure_reason = "PRODUCT_PAGE_NOT_PRESENT"
            else:
                eval_res.failure_reason = "PRODUCT_CONTENT_NOT_DETECTED"

        return eval_res
