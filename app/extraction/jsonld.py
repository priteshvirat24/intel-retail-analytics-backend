import json
import re
from typing import Dict, Any, Optional, List, Union
from bs4 import BeautifulSoup
from app.extraction.base import BaseExtractor


class JsonLdExtractor(BaseExtractor):
    """Extracts structured product data from Schema.org JSON-LD scripts."""

    def extract(self, html: str, url: str, soup: Optional[BeautifulSoup] = None) -> Optional[Dict[str, Any]]:
        if not html:
            return None

        if soup is None:
            soup = BeautifulSoup(html, "html.parser")

        script_tags = soup.find_all("script", type=re.compile(r"application/ld\+json", re.I))
        if not script_tags:
            return None

        for script in script_tags:
            content = script.string or script.get_text()
            if not content:
                continue
            try:
                data = json.loads(content.strip())
                extracted = self._find_and_parse_product(data)
                if extracted and (extracted.get("title") or extracted.get("price") or extracted.get("sku")):
                    extracted["extraction_source"] = "JSON_LD"
                    return extracted
            except Exception:
                continue

        return None

    def _find_and_parse_product(self, node: Any) -> Optional[Dict[str, Any]]:
        if isinstance(node, list):
            for item in node:
                res = self._find_and_parse_product(item)
                if res:
                    return res
            return None

        if not isinstance(node, dict):
            return None

        # Check @graph
        if "@graph" in node and isinstance(node["@graph"], list):
            for item in node["@graph"]:
                res = self._find_and_parse_product(item)
                if res:
                    return res

        # Check @type
        node_type = node.get("@type", "")
        if isinstance(node_type, list):
            is_product = any("Product" in str(t) for t in node_type)
        else:
            is_product = "Product" in str(node_type)

        if is_product:
            return self._parse_product_dict(node)

        # Recursively search sub-objects
        for val in node.values():
            if isinstance(val, (dict, list)):
                res = self._find_and_parse_product(val)
                if res:
                    return res

        return None

    def _parse_product_dict(self, data: Dict[str, Any]) -> Dict[str, Any]:
        result: Dict[str, Any] = {}

        # Title / Name
        title = data.get("name") or data.get("headline")
        if title and isinstance(title, str):
            result["title"] = title.strip()

        # Description
        description = data.get("description")
        if description and isinstance(description, str):
            result["description"] = description.strip()

        # Brand
        brand = data.get("brand")
        if isinstance(brand, dict):
            result["brand"] = brand.get("name")
        elif isinstance(brand, str):
            result["brand"] = brand.strip()

        # Model
        model = data.get("model")
        if isinstance(model, dict):
            result["model"] = model.get("name")
        elif isinstance(model, str):
            result["model"] = model.strip()

        # SKU / Product ID / GTIN
        sku = data.get("sku") or data.get("productID") or data.get("mpn")
        if sku:
            result["sku"] = str(sku).strip()

        gtin = data.get("gtin") or data.get("gtin13") or data.get("gtin14") or data.get("gtin12") or data.get("gtin8") or data.get("isbn")
        if gtin:
            result["gtin"] = str(gtin).strip()

        # Category
        category = data.get("category")
        if category and isinstance(category, str):
            result["category"] = category.strip()

        # Images
        image = data.get("image")
        image_urls = []
        if isinstance(image, str):
            image_urls.append(image)
        elif isinstance(image, list):
            for img in image:
                if isinstance(img, str):
                    image_urls.append(img)
                elif isinstance(img, dict) and img.get("url"):
                    image_urls.append(img["url"])
        elif isinstance(image, dict) and image.get("url"):
            image_urls.append(image["url"])
        if image_urls:
            result["image_urls"] = image_urls

        # Rating / Reviews
        agg_rating = data.get("aggregateRating")
        if isinstance(agg_rating, dict):
            try:
                r_val = agg_rating.get("ratingValue")
                if r_val is not None:
                    result["rating"] = float(str(r_val).replace(",", "."))
                r_count = agg_rating.get("reviewCount") or agg_rating.get("ratingCount")
                if r_count is not None:
                    result["review_count"] = int(str(r_count))
            except (ValueError, TypeError):
                pass

        # Offers (Price, Currency, Availability, Seller)
        offers = data.get("offers")
        offer = None
        if isinstance(offers, dict):
            offer = offers
        elif isinstance(offers, list) and len(offers) > 0:
            offer = offers[0]

        if offer and isinstance(offer, dict):
            # Price
            raw_price = offer.get("price") or offer.get("lowPrice") or offer.get("highPrice")
            if raw_price is not None:
                try:
                    cleaned_p = re.sub(r"[^\d.]", "", str(raw_price).replace(",", "."))
                    if cleaned_p:
                        result["price"] = float(cleaned_p)
                except (ValueError, TypeError):
                    pass

            # Currency
            currency = offer.get("priceCurrency")
            if currency and isinstance(currency, str):
                result["currency"] = currency.strip().upper()

            # Availability
            avail = offer.get("availability")
            if avail and isinstance(avail, str):
                cleaned_avail = avail.split("/")[-1].split("#")[-1]
                result["availability"] = cleaned_avail
                result["stock_status"] = "In Stock" if "InStock" in cleaned_avail else "Out of Stock" if "OutOfStock" in cleaned_avail else cleaned_avail

            # Seller
            seller = offer.get("seller")
            if isinstance(seller, dict):
                result["seller"] = seller.get("name")
            elif isinstance(seller, str):
                result["seller"] = seller.strip()

        return result
