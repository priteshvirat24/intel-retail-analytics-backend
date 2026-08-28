import re
from typing import Dict, Any, Optional, List
from bs4 import BeautifulSoup
from app.extraction.base import BaseExtractor


class DomExtractor(BaseExtractor):
    """Extracts product data from DOM tree using smart heuristic CSS selectors and custom selectors."""

    TITLE_SELECTORS = [
        "h1.product-title", "h1.product-name", "h1#productTitle", "h1.pdp-title",
        "h1[itemprop='name']", ".product-info h1", ".pdp-header h1", "h1.title",
        "h1", "div.product-name", "span#productTitle", ".product-detail h1"
    ]

    PRICE_SELECTORS = [
        "span.a-price span.a-offscreen", "span.a-price-whole", "span#priceblock_ourprice",
        "span#priceblock_dealprice", ".price-current", ".price-characteristic",
        "[itemprop='price']", ".product-price", ".pdp-price", ".current-price",
        ".sale-price", ".regular-price", ".price", ".offer-price", "span.price"
    ]

    BRAND_SELECTORS = [
        "[itemprop='brand']", ".product-brand", ".brand-name", "a#bylineInfo",
        ".pdp-brand", ".manufacturer", ".vendor-name"
    ]

    AVAILABILITY_SELECTORS = [
        "#availability span", ".stock-status", ".availability-msg", ".in-stock",
        "[itemprop='availability']", ".inventory-status", ".product-availability"
    ]

    DESCRIPTION_SELECTORS = [
        "#productDescription", "#feature-bullets", ".product-description",
        "[itemprop='description']", ".pdp-description", ".details-description"
    ]

    IMAGE_SELECTORS = [
        "#landingImage", "#imgTagWrapperId img", ".product-image img",
        "[itemprop='image']", ".gallery-image img", ".pdp-main-image img", "img.primary-image"
    ]

    def extract(self, html: str, url: str, soup: Optional[BeautifulSoup] = None) -> Optional[Dict[str, Any]]:
        if not html:
            return None

        if soup is None:
            soup = BeautifulSoup(html, "html.parser")

        # Merge custom selectors if configured
        custom = self.target_config.custom_selectors if self.target_config else {}
        title_selectors = custom.get("title_selectors", []) + self.TITLE_SELECTORS
        price_selectors = custom.get("price_selectors", []) + self.PRICE_SELECTORS
        brand_selectors = custom.get("brand_selectors", []) + self.BRAND_SELECTORS
        avail_selectors = custom.get("avail_selectors", []) + self.AVAILABILITY_SELECTORS
        desc_selectors = custom.get("desc_selectors", []) + self.DESCRIPTION_SELECTORS
        img_selectors = custom.get("img_selectors", []) + self.IMAGE_SELECTORS

        result: Dict[str, Any] = {}

        # Title
        for sel in title_selectors:
            el = soup.select_one(sel)
            if el:
                text = el.get_text(strip=True)
                if text and len(text) > 3 and not any(k in text.lower() for k in ["cookies", "sign in", "cart", "navigation"]):
                    result["title"] = text
                    break

        # Price
        for sel in price_selectors:
            el = soup.select_one(sel)
            if el:
                raw_text = el.get_text(strip=True)
                # Parse numeric price
                price_match = re.search(r"[\d.,]+", raw_text)
                if price_match:
                    try:
                        clean_num = re.sub(r"[^\d.]", "", price_match.group(0).replace(",", "."))
                        if clean_num:
                            val = float(clean_num)
                            if 0.01 <= val < 10000000:
                                result["price"] = val
                                # Currency heuristics
                                if "$" in raw_text:
                                    result["currency"] = "USD"
                                elif "€" in raw_text:
                                    result["currency"] = "EUR"
                                elif "£" in raw_text:
                                    result["currency"] = "GBP"
                                elif "₹" in raw_text:
                                    result["currency"] = "INR"
                                elif "¥" in raw_text:
                                    result["currency"] = "JPY"
                                elif "₩" in raw_text:
                                    result["currency"] = "KRW"
                                elif "R$" in raw_text:
                                    result["currency"] = "BRL"
                                break
                    except (ValueError, TypeError):
                        continue

        # Brand
        for sel in brand_selectors:
            el = soup.select_one(sel)
            if el:
                b_text = el.get_text(strip=True)
                b_text = re.sub(r"^(Brand|Visit the|Brand:)\s*", "", b_text, flags=re.I).strip()
                if b_text and len(b_text) < 50:
                    result["brand"] = b_text
                    break

        # Availability
        for sel in avail_selectors:
            el = soup.select_one(sel)
            if el:
                avail_text = el.get_text(strip=True)
                if avail_text:
                    result["stock_status"] = avail_text
                    lower_a = avail_text.lower()
                    if any(k in lower_a for k in ["in stock", "disponible", "en stock", "auf lager", "disponibile"]):
                        result["availability"] = "InStock"
                    elif any(k in lower_a for k in ["out of stock", "agotado", "rupture", "nicht lieferbar", "esaurito"]):
                        result["availability"] = "OutOfStock"
                    break

        # Description
        for sel in desc_selectors:
            el = soup.select_one(sel)
            if el:
                d_text = el.get_text(separator=" ", strip=True)
                if d_text and len(d_text) > 20:
                    result["description"] = d_text[:2000]
                    break

        # Images
        img_urls = []
        for sel in img_selectors:
            for img in soup.select(sel):
                src = img.get("src") or img.get("data-src") or img.get("data-old-hires")
                if src and src.startswith("http") and src not in img_urls:
                    img_urls.append(src)
        if img_urls:
            result["image_urls"] = img_urls[:5]

        if result.get("title") or result.get("price"):
            result["extraction_source"] = "DOM_SELECTOR"
            return result

        return None
