"""
Deterministic Laptop Product Page Validator & Confidence Scorer.
Computes a rigorous confidence score (0.0 to 1.0) and validates whether a page
represents an authentic, unblocked laptop product page.
"""
import re
import json
from typing import Dict, Any, Optional, Tuple, List
from bs4 import BeautifulSoup
from pydantic import BaseModel, Field

from app.crawlers.base import CrawlerResponse
from app.evaluation.failures import FailureClassifier


class LaptopValidationResult(BaseModel):
    """Rigorous evaluation and extraction of laptop product page candidate."""
    is_valid_laptop: bool = False
    confidence_score: float = 0.0
    status_code: int = 0
    failure_class: Optional[str] = None
    failure_vendor: Optional[str] = None
    
    # Extracted Minimum Product Fields
    product_name: Optional[str] = None
    brand: Optional[str] = None
    model_or_sku: Optional[str] = None
    price: Optional[float] = None
    currency: Optional[str] = None
    availability: Optional[str] = None
    specifications: Dict[str, str] = Field(default_factory=dict)
    
    # Signals Found
    has_jsonld_product: bool = False
    has_product_title: bool = False
    has_laptop_keywords: bool = False
    has_breadcrumbs: bool = False
    has_price: bool = False
    has_specs: bool = False
    detected_keywords: List[str] = Field(default_factory=list)
    evidence_notes: str = ""


class LaptopValidator:
    """Evaluates CrawlerResponse and determines product validity with confidence scoring."""

    MULTILANG_LAPTOP_KEYWORDS = [
        # English
        "laptop", "notebook", "macbook", "chromebook", "ultrabook", "gaming laptop",
        "thinkpad", "zenbook", "vivobook", "ideapad", "pavilion", "legion", "alienware",
        "spectre", "yoga", "inspiron", "latitude", "vostro", "envy", "swift", "aspire",
        "predator", "surface laptop", "surface pro",
        # German
        "tragbarer computer", "tragbare computer",
        # French
        "ordinateur portable", "ordinateurs portables", "pc portable", "pc portables",
        # Italian
        "portatile", "portatili", "pc portatile", "computer portatile",
        # Spanish
        "portátil", "portatiles", "portátiles", "ordenador portátil", "ordenadores portátiles",
        # Portuguese
        "computador portátil", "computadores portáteis",
        # Polish
        "laptopy", "notebooki", "komputer przenośny",
        # Korean
        "노트북", "노트북 컴퓨터", "맥북",
        # Japanese
        "ノートパソコン", "ノートpc", "ラップトップ",
        # Vietnamese
        "máy tính xách tay", "may tinh xach tay",
        # Turkish
        "dizüstü", "dizüstü bilgisayar"
    ]

    HARDWARE_SPECS_PATTERNS = [
        r"\b(intel|amd|ryzen|core\s*i[3579]|m[1234]\s*(pro|max)?)\b",
        r"\b\d{1,2}(\.\d)?[\"\']\s*(display|screen|fhd|oled|ips|uhd)?\b",
        r"\b(4|8|16|32|64)\s*gb\s*(ram|ddr[45]|lpddr)?\b",
        r"\b(128|256|512|1024|1|2)\s*(gb|tb)\s*(ssd|nvme|emmc|hdd)\b",
        r"\b(rtx\s*\d{4}|gtx\s*\d{4}|radeon|iris\s*xe|geforce)\b"
    ]

    @classmethod
    def validate(cls, response: CrawlerResponse, expected_url: str, threshold: float = 0.80) -> LaptopValidationResult:
        """
        Computes deterministic validation score and extracts minimum product identity.
        Threshold default: 0.80.
        """
        res = LaptopValidationResult(status_code=response.status_code)

        # 1. Transport & HTTP Failure Checks
        if response.status_code == 0:
            err = (response.error_message or "").lower()
            if "timeout" in err:
                res.failure_class = "CONNECTION_TIMEOUT"
            elif "refused" in err or "econnrefused" in err:
                res.failure_class = "SERVICE_UNAVAILABLE"
            else:
                res.failure_class = "TRANSPORT_FAILURE"
            return res

        if response.status_code == 404:
            res.failure_class = "HTTP_404_NOT_FOUND"
            return res
        if response.status_code == 403:
            res.failure_class = "HTTP_403_FORBIDDEN"
        elif response.status_code == 429:
            res.failure_class = "HTTP_429_RATE_LIMITED"
        elif response.status_code >= 500:
            res.failure_class = "HTTP_5XX_SERVER_ERROR"

        html = response.html or ""
        markdown = response.markdown or ""
        combined_text = (html + " " + markdown).lower()

        # 2. Anti-Bot / WAF Vendor Detection
        vendor = FailureClassifier.detect_anti_bot_vendor(html, response.headers or {}, response.status_code)
        res.failure_vendor = vendor

        # Extract title if HTML present
        soup = BeautifulSoup(html, "html.parser") if html else None
        page_title = (soup.title.string.strip() if (soup and soup.title and soup.title.string) else "").lower()

        # True interactive challenge signatures (Page title or explicit blocking status)
        is_explicit_challenge = (
            response.status_code in (403, 429)
            or any(t in page_title for t in ["robot check", "just a moment...", "access denied", "attention required", "security check", "verify you are human", "blocked"])
            or ("cf-turnstile" in html and len(html) < 10000)
            or ("amazon.com/errors/validatecaptcha" in html and len(html) < 15000)
        )

        if is_explicit_challenge:
            if any(t in page_title or t in combined_text for t in ["robot check", "captcha", "cf-turnstile", "recaptcha", "hcaptcha"]):
                res.failure_class = "CAPTCHA_CHALLENGE"
            else:
                res.failure_class = "WAF_BOT_CHALLENGE"
            return res

        # 3. Detect Empty / SPA Shell
        if len(html.strip()) < 150 and len(markdown.strip()) < 80:
            res.failure_class = "EMPTY_RESPONSE"
            return res

        if any(spa in combined_text for spa in ['<div id="root"></div>', '<div id="app"></div>', 'please enable javascript']) and len(html) < 2000:
            res.failure_class = "EMPTY_SPA_SHELL"
            return res

        if res.failure_class:
            return res

        # 4. Parse Document & Extract Signals
        score = 0.0

        # Signal 1: JSON-LD Product (+0.35)
        if soup:
            for s in soup.find_all("script", type="application/ld+json"):
                txt = s.string or ""
                if '"@type"' in txt and any(t in txt for t in ['"Product"', '"IndividualProduct"', '"Laptop"']):
                    res.has_jsonld_product = True
                    score += 0.35
                    try:
                        parsed_json = json.loads(txt)
                        items = parsed_json if isinstance(parsed_json, list) else [parsed_json]
                        if isinstance(parsed_json, dict) and "@graph" in parsed_json:
                            items = parsed_json["@graph"]
                        for item in items:
                            if item.get("@type") in ("Product", "IndividualProduct"):
                                res.product_name = res.product_name or item.get("name")
                                if isinstance(item.get("brand"), dict):
                                    res.brand = item["brand"].get("name")
                                elif isinstance(item.get("brand"), str):
                                    res.brand = item["brand"]
                                res.model_or_sku = res.model_or_sku or item.get("sku") or item.get("mpn") or item.get("gtin13")
                                offers = item.get("offers")
                                if isinstance(offers, dict):
                                    res.price = res.price or float(offers.get("price") or 0.0) or None
                                    res.currency = res.currency or offers.get("priceCurrency")
                                    res.availability = offers.get("availability")
                    except Exception:
                        pass
                    break

        # Signal 2: Product Title & Laptop Keywords (+0.30)
        title_text = ""
        if soup:
            h1 = soup.find("h1")
            if h1 and len(h1.get_text(strip=True)) > 5:
                title_text = h1.get_text(strip=True)
            elif soup.title and len(soup.title.get_text(strip=True)) > 5:
                title_text = soup.title.get_text(strip=True)
        elif markdown:
            for l in markdown.splitlines():
                if l.startswith("# "):
                    title_text = l[2:].strip()
                    break

        res.product_name = res.product_name or title_text
        title_lower = (res.product_name or "").lower()

        # Reject generic home/category titles
        if any(g in title_lower for g in ["welcome", "homepage", "search results", "category", "404 not found", "error"]):
            res.failure_class = "WRONG_PAGE_NON_PRODUCT"
            return res

        matched_kws = []
        for kw in cls.MULTILANG_LAPTOP_KEYWORDS:
            if kw in title_lower or kw in combined_text[:12000]:
                matched_kws.append(kw)

        res.detected_keywords = matched_kws[:6]
        if len(title_text) >= 8:
            res.has_product_title = True
            score += 0.15

        if matched_kws:
            res.has_laptop_keywords = True
            score += 0.15

        # Signal 3: Breadcrumb / Category (+0.15)
        if soup:
            bc = soup.find(class_=re.compile(r"breadcrumb", re.I)) or soup.find("nav", attrs={"aria-label": re.compile(r"breadcrumb", re.I)})
            if bc and any(k in bc.get_text().lower() for k in cls.MULTILANG_LAPTOP_KEYWORDS + ["computer", "pc", "informatica", "eletronicos", "electronics"]):
                res.has_breadcrumbs = True
                score += 0.15

        # Signal 4: Price & Currency (+0.15)
        if not res.price and soup:
            price_el = (
                soup.select_one(".a-price .a-offscreen")
                or soup.select_one('[data-test*="price"]')
                or soup.select_one('[class*="price"]')
                or soup.find(itemprop="price")
            )
            if price_el:
                price_text = price_el.get_text(strip=True)
                p_match = re.search(r"([0-9]+([.,][0-9]{2})?)", price_text)
                if p_match:
                    try:
                        res.price = float(p_match.group(1).replace(",", ""))
                        res.has_price = True
                        score += 0.15
                    except Exception:
                        pass

            if not res.has_price:
                price_match = re.search(r"[\$€£₹¥R\$]\s*([0-9]+([.,][0-9]{2})?)", html[:25000])
                if price_match:
                    try:
                        res.price = float(price_match.group(1).replace(",", ""))
                        res.has_price = True
                        score += 0.15
                    except Exception:
                        pass
        elif res.price:
            res.has_price = True
            score += 0.15

        # Signal 5: Hardware Specifications (+0.15)
        spec_matches = 0
        for pat in cls.HARDWARE_SPECS_PATTERNS:
            if re.search(pat, combined_text[:35000], re.I):
                spec_matches += 1
        if spec_matches >= 2:
            res.has_specs = True
            score += 0.15

        # Signal 6: Add to Cart / Buy Box Element (+0.15)
        if soup:
            buy_btn = (
                soup.select_one("#add-to-cart-button")
                or soup.select_one('[id*="add-to-cart"]')
                or soup.select_one('[name*="add-to-cart"]')
                or soup.select_one('button[class*="buy"]')
                or soup.select_one('button[class*="cart"]')
                or soup.select_one('[data-button-action*="add-to-cart"]')
            )
            if buy_btn:
                score += 0.15

        # Signal 7: OpenGraph Product Meta (+0.10)
        if soup:
            og_type = soup.find("meta", property="og:type") or soup.find("meta", attrs={"name": "og:type"})
            og_title = soup.find("meta", property="og:title") or soup.find("meta", attrs={"name": "og:title"})
            if (og_type and "product" in str(og_type.get("content", "")).lower()) or (og_title and any(k in str(og_title.get("content", "")).lower() for k in cls.MULTILANG_LAPTOP_KEYWORDS)):
                score += 0.10

        # Signal 8: Brand / SKU Identification (+0.10)
        known_brands = ["hp", "dell", "lenovo", "asus", "acer", "apple", "msi", "samsung", "lg", "microsoft", "razer", "gigabyte", "huawei", "dynabook"]
        for b in known_brands:
            if b in title_lower:
                res.brand = res.brand or b.upper()
                score += 0.05
                break

        # Check SKU in URL
        sku_match = re.search(r"/(?:dp|product|p|ref|item)/([A-Z0-9]{8,15})", expected_url, re.I)
        if sku_match:
            res.model_or_sku = res.model_or_sku or sku_match.group(1)
            score += 0.05

        res.confidence_score = round(min(score, 1.0), 2)

        if res.confidence_score >= threshold:
            res.is_valid_laptop = True
            res.failure_class = "NONE"
            res.evidence_notes = f"Validated Laptop (Score: {res.confidence_score}): '{res.product_name[:60]}' | Keywords: {', '.join(res.detected_keywords[:3])}"
        else:
            if not res.has_laptop_keywords:
                res.failure_class = "NOT_A_LAPTOP_PRODUCT"
            elif not res.has_product_title:
                res.failure_class = "PRODUCT_IDENTITY_MISSING"
            else:
                res.failure_class = "LOW_CONFIDENCE_PRODUCT_PAGE"

        return res
