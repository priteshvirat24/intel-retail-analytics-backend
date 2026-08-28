import json
import re
from typing import Dict, Any, Optional
from bs4 import BeautifulSoup
from app.retailers.base_adapter import BaseRetailerAdapter


class WalmartAdapter(BaseRetailerAdapter):
    """Specialized adapter for Walmart US (extracts from __NEXT_DATA__ payload)."""

    def extract_custom(self, html: str, url: str, soup: Optional[BeautifulSoup] = None) -> Optional[Dict[str, Any]]:
        if not html:
            return None

        if soup is None:
            soup = BeautifulSoup(html, "html.parser")

        # Extract Item ID from URL
        item_id_match = re.search(r"/ip/(?:[^/]+/)?([0-9]+)", url)
        item_id = item_id_match.group(1) if item_id_match else None

        # Check __NEXT_DATA__
        script = soup.find("script", id="__NEXT_DATA__")
        if script and script.string:
            try:
                data = json.loads(script.string.strip())
                initial_data = data.get("props", {}).get("pageProps", {}).get("initialData", {})
                product_data = initial_data.get("data", {}).get("product", {})

                if product_data:
                    result: Dict[str, Any] = {
                        "product_id": product_data.get("usItemId") or item_id,
                        "sku": product_data.get("usItemId") or item_id,
                        "title": product_data.get("name"),
                        "brand": product_data.get("brand"),
                        "description": product_data.get("shortDescription"),
                        "extraction_source": "WALMART_NEXT_DATA"
                    }

                    # Price
                    price_info = product_data.get("priceInfo", {}).get("currentPrice", {})
                    if price_info.get("price") is not None:
                        result["price"] = float(price_info["price"])
                        result["currency"] = "USD"

                    # Availability
                    avail_status = product_data.get("inventoryStatus") or product_data.get("availabilityStatus")
                    if avail_status:
                        result["stock_status"] = avail_status
                        result["availability"] = "InStock" if "in" in str(avail_status).lower() else "OutOfStock"

                    # Images
                    images = product_data.get("imageInfo", {}).get("allImages", [])
                    img_urls = [img.get("url") for img in images if img.get("url")]
                    if img_urls:
                        result["image_urls"] = img_urls

                    # Rating
                    reviews = product_data.get("reviews", {})
                    if reviews.get("averageOverallRating") is not None:
                        result["rating"] = float(reviews["averageOverallRating"])
                        result["review_count"] = int(reviews.get("totalReviewCount", 0))

                    return result
            except Exception:
                pass

        # Fallback DOM
        title_el = soup.select_one("h1#main-title") or soup.select_one("h1")
        price_el = soup.select_one("[itemprop='price']") or soup.select_one("span[itemprop='price']")
        if title_el:
            res = {
                "title": title_el.get_text(strip=True),
                "product_id": item_id,
                "sku": item_id,
                "extraction_source": "WALMART_DOM"
            }
            if price_el:
                try:
                    res["price"] = float(re.sub(r"[^\d.]", "", price_el.get_text(strip=True)))
                    res["currency"] = "USD"
                except ValueError:
                    pass
            return res

        return None
