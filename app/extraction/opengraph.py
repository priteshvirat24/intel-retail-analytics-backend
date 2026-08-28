import re
from typing import Dict, Any, Optional
from bs4 import BeautifulSoup
from app.extraction.base import BaseExtractor


class OpenGraphExtractor(BaseExtractor):
    """Extracts product data from OpenGraph, Twitter Cards, and standard HTML meta tags."""

    def extract(self, html: str, url: str, soup: Optional[BeautifulSoup] = None) -> Optional[Dict[str, Any]]:
        if not html:
            return None

        if soup is None:
            soup = BeautifulSoup(html, "html.parser")

        meta_map: Dict[str, str] = {}
        for tag in soup.find_all("meta"):
            name = tag.get("property") or tag.get("name") or tag.get("itemprop")
            content = tag.get("content")
            if name and content:
                meta_map[name.lower().strip()] = content.strip()

        if not meta_map:
            return None

        result: Dict[str, Any] = {}

        # Title
        title = (
            meta_map.get("og:title")
            or meta_map.get("twitter:title")
            or meta_map.get("title")
        )
        if title:
            result["title"] = title

        # Description
        desc = (
            meta_map.get("og:description")
            or meta_map.get("twitter:description")
            or meta_map.get("description")
        )
        if desc:
            result["description"] = desc

        # Price
        price_str = (
            meta_map.get("og:price:amount")
            or meta_map.get("product:price:amount")
            or meta_map.get("price")
            or meta_map.get("twitter:data1")
        )
        if price_str:
            try:
                cleaned = re.sub(r"[^\d.]", "", price_str.replace(",", "."))
                if cleaned:
                    result["price"] = float(cleaned)
            except (ValueError, TypeError):
                pass

        # Currency
        currency = (
            meta_map.get("og:price:currency")
            or meta_map.get("product:price:currency")
            or meta_map.get("pricecurrency")
        )
        if currency:
            result["currency"] = currency.upper().strip()

        # Availability
        avail = (
            meta_map.get("og:availability")
            or meta_map.get("product:availability")
            or meta_map.get("availability")
        )
        if avail:
            if "instock" in avail.lower():
                result["availability"] = "InStock"
                result["stock_status"] = "In Stock"
            elif "oos" in avail.lower() or "out" in avail.lower():
                result["availability"] = "OutOfStock"
                result["stock_status"] = "Out of Stock"
            else:
                result["availability"] = avail

        # Brand
        brand = (
            meta_map.get("product:brand")
            or meta_map.get("og:brand")
            or meta_map.get("brand")
        )
        if brand:
            result["brand"] = brand

        # Image
        image = (
            meta_map.get("og:image")
            or meta_map.get("og:image:secure_url")
            or meta_map.get("twitter:image")
            or meta_map.get("image")
        )
        if image:
            result["image_urls"] = [image]

        # SKU / Retailer ID
        sku = meta_map.get("product:retailer_item_id") or meta_map.get("sku")
        if sku:
            result["sku"] = sku

        if result.get("title") or result.get("price"):
            result["extraction_source"] = "OPENGRAPH_META"
            return result

        return None
