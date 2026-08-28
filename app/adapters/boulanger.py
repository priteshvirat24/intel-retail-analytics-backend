import re
from typing import Dict, Any, Optional
from bs4 import BeautifulSoup
from app.adapters.base import BaseTargetAdapter


class BoulangerAdapter(BaseTargetAdapter):
    """Custom target adapter for Boulanger France (boulanger.com)."""

    def extract_custom(self, html: str, url: str, soup: Optional[BeautifulSoup] = None) -> Optional[Dict[str, Any]]:
        if not html or len(html.strip()) < 50:
            return None

        if soup is None:
            soup = BeautifulSoup(html, "html.parser")

        # Bot / block detection
        if any(term in html for term in ["errors.edgesuite.net", "Attention Required! | Cloudflare", "Access Denied"]):
            return None

        result: Dict[str, Any] = {}

        # 1. Title
        title_el = (
            soup.select_one("h1.product-title")
            or soup.select_one("h1[itemprop='name']")
            or soup.select_one(".title-main h1")
            or soup.select_one(".pdp-header h1")
            or soup.select_one("h1")
        )
        if title_el:
            t_text = title_el.get_text(strip=True)
            if t_text and not any(err in t_text.lower() for err in ["404", "not found", "invalid url"]):
                result["title"] = t_text

        # 2. Price
        price_el = (
            soup.select_one(".price__amount")
            or soup.select_one("[itemprop='price']")
            or soup.select_one(".product-price")
            or soup.select_one(".price")
        )
        if price_el:
            price_text = price_el.get_text(strip=True)
            match = re.search(r"[\d.,]+", price_text)
            if match:
                raw_num = match.group(0).strip()
                try:
                    if "," in raw_num:
                        clean = raw_num.replace(".", "").replace(",", ".")
                    else:
                        clean = raw_num
                    clean = re.sub(r"[^\d.]", "", clean)
                    if clean:
                        result["price"] = float(clean)
                        result["currency"] = "EUR"
                except (ValueError, TypeError):
                    pass

        # 3. Brand
        brand_el = (
            soup.select_one(".brand-name")
            or soup.select_one("[itemprop='brand']")
            or soup.select_one(".product-brand")
        )
        if brand_el:
            result["brand"] = brand_el.get_text(strip=True)

        # 4. Availability
        avail_el = (
            soup.select_one("[itemprop='availability']")
            or soup.select_one(".stock-status")
            or soup.select_one(".availability")
            or soup.select_one(".stock")
        )
        if avail_el:
            avail_text = avail_el.get_text(strip=True)
            result["stock_status"] = avail_text
            avail_lower = avail_text.lower()
            if any(k in avail_lower for k in ["en stock", "in stock", "disponible"]):
                result["availability"] = "InStock"
            elif any(k in avail_lower for k in ["épuisé", "rupture", "indisponible", "out of stock"]):
                result["availability"] = "OutOfStock"

        # 5. SKU
        sku_el = (
            soup.select_one("[itemprop='sku']")
            or soup.select_one(".product-sku")
            or soup.select_one(".reference")
        )
        if sku_el:
            sku_val = sku_el.get("content") or sku_el.get_text(strip=True)
            if sku_val:
                result["sku"] = sku_val
                result["product_id"] = sku_val
        else:
            ref_match = re.search(r"/ref/(\d+)", url)
            if ref_match:
                result["sku"] = ref_match.group(1)
                result["product_id"] = result["sku"]

        # 6. Images
        img_el = (
            soup.select_one("[itemprop='image']")
            or soup.select_one(".product-image img")
            or soup.select_one(".carousel-image img")
        )
        if img_el:
            src = img_el.get("src") or img_el.get("data-src")
            if src:
                if src.startswith("//"):
                    src = "https:" + src
                elif src.startswith("/"):
                    src = "https://www.boulanger.com" + src
                result["image_urls"] = [src]

        # 7. Description
        desc_el = (
            soup.select_one("[itemprop='description']")
            or soup.select_one(".product-description")
            or soup.select_one(".description")
        )
        if desc_el:
            result["description"] = desc_el.get_text(separator=" ", strip=True)

        if result.get("title") or result.get("price"):
            result["extraction_source"] = "BOULANGER_ADAPTER"
            return result

        return None
