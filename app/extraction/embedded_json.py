import json
import re
from typing import Dict, Any, Optional, List
from bs4 import BeautifulSoup
from app.extraction.base import BaseExtractor


class EmbeddedJsonExtractor(BaseExtractor):
    """Extracts product data from embedded application JSON state (Next.js, Nuxt, Redux, Apollo)."""

    SCRIPT_PATTERNS = [
        re.compile(r"window\.__INITIAL_STATE__\s*=\s*({.+?});", re.DOTALL),
        re.compile(r"window\.__PRELOADED_STATE__\s*=\s*({.+?});", re.DOTALL),
        re.compile(r"window\.__APOLLO_STATE__\s*=\s*({.+?});", re.DOTALL),
        re.compile(r"window\.pageData\s*=\s*({.+?});", re.DOTALL),
        re.compile(r"window\.productData\s*=\s*({.+?});", re.DOTALL),
        re.compile(r"var\s+digitalData\s*=\s*({.+?});", re.DOTALL),
    ]

    def extract(self, html: str, url: str, soup: Optional[BeautifulSoup] = None) -> Optional[Dict[str, Any]]:
        if not html:
            return None

        if soup is None:
            soup = BeautifulSoup(html, "html.parser")

        # 1. Check Next.js __NEXT_DATA__
        next_data_script = soup.find("script", id="__NEXT_DATA__")
        if next_data_script:
            script_content = next_data_script.string or next_data_script.get_text()
            if script_content:
                try:
                    data = json.loads(script_content.strip())
                    extracted = self._extract_from_state_tree(data)
                    if extracted and (extracted.get("title") or extracted.get("price")):
                        extracted["extraction_source"] = "EMBEDDED_NEXT_DATA"
                        return extracted
                except Exception:
                    pass

        # 2. Check inline JavaScript state assignments
        for script in soup.find_all("script"):
            text = script.string or script.get_text()
            if not text:
                continue
            for pattern in self.SCRIPT_PATTERNS:
                match = pattern.search(text)
                if match:
                    try:
                        raw_json = match.group(1)
                        data = json.loads(raw_json)
                        extracted = self._extract_from_state_tree(data)
                        if extracted and (extracted.get("title") or extracted.get("price")):
                            extracted["extraction_source"] = "EMBEDDED_JS_STATE"
                            return extracted
                    except Exception:
                        continue

        return None

    def _extract_from_state_tree(self, data: Any) -> Optional[Dict[str, Any]]:
        """Deep search for product objects in state trees."""
        if not isinstance(data, dict):
            return None

        # Check direct product keys
        for key in ["product", "productData", "item", "productDetails", "catalogItem"]:
            if key in data and isinstance(data[key], dict):
                p = self._parse_state_product(data[key])
                if p and (p.get("title") or p.get("price")):
                    return p

        # Check props.pageProps for Next.js
        page_props = data.get("props", {}).get("pageProps", {})
        if isinstance(page_props, dict):
            for key in ["product", "initialData", "productDetails", "item"]:
                if key in page_props and isinstance(page_props[key], dict):
                    # Check nested initialData.product
                    sub_p = page_props[key]
                    if isinstance(sub_p, dict) and "product" in sub_p and isinstance(sub_p["product"], dict):
                        p = self._parse_state_product(sub_p["product"])
                        if p and (p.get("title") or p.get("price")):
                            return p
                    p = self._parse_state_product(sub_p)
                    if p and (p.get("title") or p.get("price")):
                        return p

        # Recursive search
        for val in data.values():
            if isinstance(val, dict):
                res = self._extract_from_state_tree(val)
                if res:
                    return res

        return None

    def _parse_state_product(self, p: Dict[str, Any]) -> Dict[str, Any]:
        result: Dict[str, Any] = {}

        # Title
        title = p.get("title") or p.get("name") or p.get("productName") or p.get("heading")
        if title and isinstance(title, str):
            result["title"] = title.strip()

        # Description
        desc = p.get("description") or p.get("shortDescription") or p.get("longDescription")
        if desc and isinstance(desc, str):
            result["description"] = desc.strip()

        # Brand
        brand = p.get("brand") or p.get("brandName") or p.get("manufacturer")
        if isinstance(brand, str):
            result["brand"] = brand.strip()
        elif isinstance(brand, dict) and brand.get("name"):
            result["brand"] = str(brand["name"]).strip()

        # SKU / Product ID
        sku = p.get("sku") or p.get("id") or p.get("productId") or p.get("code") or p.get("upc")
        if sku:
            result["sku"] = str(sku).strip()

        # Price & Currency
        price_info = p.get("price") or p.get("pricing") or p.get("priceInfo")
        if isinstance(price_info, dict):
            raw_p = price_info.get("currentPrice") or price_info.get("price") or price_info.get("amount") or price_info.get("value")
            if isinstance(raw_p, dict):
                raw_p_val = raw_p.get("price") or raw_p.get("amount") or raw_p.get("value")
                cur = raw_p.get("currency") or raw_p.get("currencyCode")
                if cur:
                    result["currency"] = str(cur).strip().upper()
                raw_p = raw_p_val

            if raw_p is not None:
                try:
                    result["price"] = float(re.sub(r"[^\d.]", "", str(raw_p).replace(",", ".")))
                except (ValueError, TypeError):
                    pass

            cur = price_info.get("currency") or price_info.get("currencyCode")
            if cur and isinstance(cur, str):
                result["currency"] = cur.strip().upper()
        elif price_info is not None:
            try:
                result["price"] = float(re.sub(r"[^\d.]", "", str(price_info).replace(",", ".")))
            except (ValueError, TypeError):
                pass

        # Availability
        avail = p.get("availability") or p.get("inStock") or p.get("stockStatus")
        if isinstance(avail, bool):
            result["availability"] = "InStock" if avail else "OutOfStock"
            result["stock_status"] = "In Stock" if avail else "Out of Stock"
        elif isinstance(avail, str):
            result["availability"] = "InStock" if "in" in avail.lower() else "OutOfStock"
            result["stock_status"] = avail.strip()

        # Images
        images = p.get("images") or p.get("imageUrls") or p.get("media")
        img_list = []
        if isinstance(images, list):
            for img in images:
                if isinstance(img, str):
                    img_list.append(img)
                elif isinstance(img, dict) and img.get("url"):
                    img_list.append(img["url"])
        elif isinstance(p.get("image"), str):
            img_list.append(p["image"])

        if img_list:
            result["image_urls"] = img_list

        return result
