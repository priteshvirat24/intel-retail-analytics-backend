"""
Dedicated Amazon Specialized Scraper Strategy.
Provides specialized marketplace discovery, search keyword queries, ASIN extraction,
and structured product scraping across international Amazon domains (US, UK, DE, IN, FR, IT, ES, CA, MX, BR).
"""
import os
import re
import time
import asyncio
import logging
from typing import Dict, Any, List, Optional, Tuple
from urllib.parse import quote_plus, urljoin
import httpx
from bs4 import BeautifulSoup

import app.env
from app.crawlers.base import CrawlerResponse
from app.crawlers.brightdata_web_unlocker import BrightDataWebUnlockerClient
from app.classification.laptop_classifier import LaptopClassifier, ClassificationResult

logger = logging.getLogger("crawl.amazon_scraper")


class AmazonScraperStrategy:
    """Specialized Amazon scraping and discovery engine."""

    AMAZON_MARKETPLACES = {
        "US": {"domain": "amazon.com", "iso": "us", "currency": "USD", "name": "Amazon US"},
        "GB": {"domain": "amazon.co.uk", "iso": "gb", "currency": "GBP", "name": "Amazon UK"},
        "DE": {"domain": "amazon.de", "iso": "de", "currency": "EUR", "name": "Amazon Germany"},
        "FR": {"domain": "amazon.fr", "iso": "fr", "currency": "EUR", "name": "Amazon France"},
        "IT": {"domain": "amazon.it", "iso": "it", "currency": "EUR", "name": "Amazon Italy"},
        "ES": {"domain": "amazon.es", "iso": "es", "currency": "EUR", "name": "Amazon Spain"},
        "CA": {"domain": "amazon.ca", "iso": "ca", "currency": "CAD", "name": "Amazon Canada"},
        "IN": {"domain": "amazon.in", "iso": "in", "currency": "INR", "name": "Amazon India"},
        "MX": {"domain": "amazon.com.mx", "iso": "mx", "currency": "MXN", "name": "Amazon Mexico"},
        "BR": {"domain": "amazon.com.br", "iso": "br", "currency": "BRL", "name": "Amazon Brazil"}
    }

    SEARCH_KEYWORDS = [
        "laptop",
        "laptop computer",
        "notebook",
        "gaming laptop",
        "business laptop",
        "ultrabook"
    ]

    def __init__(self, unlocker_client: Optional[BrightDataWebUnlockerClient] = None):
        self.unlocker = unlocker_client or BrightDataWebUnlockerClient()

    @classmethod
    def extract_asin(cls, url: str) -> Optional[str]:
        """Extracts 10-character Amazon Standard Identification Number (ASIN) from URL."""
        if not url:
            return None
        m = re.search(r"/(?:dp|gp/product|exec/obidos/ASIN)/([A-Z0-9]{10})", url, re.IGNORECASE)
        if m:
            return m.group(1).upper()
        m2 = re.search(r"\b(B0[A-Z0-9]{8})\b", url, re.IGNORECASE)
        if m2:
            return m2.group(1).upper()
        return None

    async def search_laptops(
        self,
        country_code: str = "US",
        keyword: str = "laptop",
        limit: int = 10
    ) -> List[Dict[str, Any]]:
        """
        Executes Amazon search for laptop products in the specified regional marketplace.
        Returns a list of candidate items with URL, ASIN, title, and ranking score.
        """
        market = self.AMAZON_MARKETPLACES.get(country_code.upper(), self.AMAZON_MARKETPLACES["US"])
        domain = market["domain"]
        iso = market["iso"]

        search_url = f"https://www.{domain}/s?k={quote_plus(keyword)}&i=computers"
        logger.info(f"Searching Amazon ({country_code}) at {search_url}")

        resp = await self.unlocker.fetch(search_url, country_iso=iso, timeout_sec=35.0)
        candidates: List[Dict[str, Any]] = []

        if not resp.success or not resp.html:
            logger.warning(f"Amazon search failed for {country_code}: {resp.error_message}")
            return candidates

        soup = BeautifulSoup(resp.html, "html.parser")
        product_cards = soup.select("div[data-component-type='s-search-result'], div.s-result-item[data-asin]")

        for card in product_cards:
            asin = card.get("data-asin", "").strip()
            if not asin or len(asin) != 10:
                continue

            # Title
            title_el = card.select_one("h2 a span, h2 span, a.a-link-normal span.a-text-normal")
            title = title_el.get_text(strip=True) if title_el else ""

            # Link
            link_el = card.select_one("h2 a, a.a-link-normal[href*='/dp/']")
            href = link_el.get("href", "") if link_el else ""
            if href:
                full_url = urljoin(f"https://www.{domain}", href).split("?")[0]
            else:
                full_url = f"https://www.{domain}/dp/{asin}"

            # Filter out non-laptops at search level
            is_valid_cand, reason = LaptopClassifier.validate_candidate_url(full_url, title)
            if not is_valid_cand:
                continue

            candidates.append({
                "asin": asin,
                "url": full_url,
                "title": title,
                "marketplace": domain,
                "country": country_code.upper(),
                "discovery_method": f"Amazon Search ('{keyword}')"
            })

            if len(candidates) >= limit:
                break

        return candidates

    async def scrape_product(
        self,
        product_url: str,
        country_code: str = "US"
    ) -> Dict[str, Any]:
        """
        Scrapes and extracts detailed structured specs from an Amazon product page.
        """
        market = self.AMAZON_MARKETPLACES.get(country_code.upper(), self.AMAZON_MARKETPLACES["US"])
        iso = market["iso"]
        asin = self.extract_asin(product_url)

        resp = await self.unlocker.fetch(product_url, country_iso=iso, timeout_sec=35.0)
        
        result: Dict[str, Any] = {
            "url": product_url,
            "asin": asin,
            "success": False,
            "status_code": resp.status_code,
            "error": resp.error_message,
            "raw_html": resp.html,
            "extracted_specs": {},
            "classification": None
        }

        if not resp.success or not resp.html:
            return result

        soup = BeautifulSoup(resp.html, "html.parser")

        # 1. Title Extraction
        title_el = soup.select_one("#productTitle, #title, h1.a-size-large")
        title = title_el.get_text(strip=True) if title_el else ""
        result["title"] = title

        # 2. Price Extraction
        price_val: Optional[float] = None
        price_el = soup.select_one("span.a-price span.a-offscreen, #priceblock_ourprice, #priceblock_dealprice, span.priceToPay")
        if price_el:
            price_text = price_el.get_text(strip=True)
            p_m = re.search(r"[\d,.]+", price_text.replace(",", ""))
            if p_m:
                try:
                    price_val = float(p_m.group(0))
                except ValueError:
                    pass
        result["price"] = price_val
        result["currency"] = market["currency"]

        # 3. Brand Extraction
        brand_el = soup.select_one("tr.po-brand td.a-span9 span, #bylineInfo, a#bylineInfo")
        brand = brand_el.get_text(strip=True) if brand_el else ""
        if "visit the" in brand.lower():
            brand = re.sub(r"(?i)visit the\s+", "", brand).replace("store", "").strip()
        result["brand"] = brand

        # 4. Technical Specs Table
        specs: Dict[str, str] = {}
        for row in soup.select("#productDetails_techSpec_section_1 tr, #technicalSpecifications_section_1 tr, table.prodDetTable tr, table.a-keyvalue tr"):
            th = row.select_one("th")
            td = row.select_one("td")
            if th and td:
                k = th.get_text(strip=True)
                v = td.get_text(strip=True)
                if k and v:
                    specs[k.lower()] = v

        for row in soup.select("table.po-table tr, div.po-row"):
            label = row.select_one("td.a-span3 span, div.po-label")
            val = row.select_one("td.a-span9 span, div.po-value")
            if label and val:
                k = label.get_text(strip=True)
                v = val.get_text(strip=True)
                if k and v:
                    specs[k.lower()] = v

        result["specs_table"] = specs

        # 5. Classify & Validate with Strict 12-Class Classifier
        classification = LaptopClassifier.classify(
            title=title,
            html=resp.html,
            url=product_url,
            price=price_val
        )
        result["classification"] = classification
        result["is_genuine_laptop"] = classification.is_genuine_laptop
        result["success"] = classification.is_genuine_laptop

        return result
