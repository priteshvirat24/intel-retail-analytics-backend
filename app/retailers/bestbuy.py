import re
from typing import Dict, Any, Optional
from bs4 import BeautifulSoup
from app.retailers.base_adapter import BaseRetailerAdapter


class BestBuyAdapter(BaseRetailerAdapter):
    """Specialized adapter for Best Buy (US and CA)."""

    def extract_custom(self, html: str, url: str, soup: Optional[BeautifulSoup] = None) -> Optional[Dict[str, Any]]:
        if not html:
            return None

        if soup is None:
            soup = BeautifulSoup(html, "html.parser")

        result: Dict[str, Any] = {}

        # 1. SKU extraction from URL
        sku_match = re.search(r"/([0-9]{7,8})\.p", url) or re.search(r"/product/[^/]+/([0-9]+)", url)
        if sku_match:
            result["sku"] = sku_match.group(1)
            result["product_id"] = result["sku"]

        # 2. Title
        title_el = soup.select_one(".sku-title h1") or soup.select_one("h1.heading-5") or soup.select_one("h1")
        if title_el:
            result["title"] = title_el.get_text(strip=True)

        # 3. Price
        price_el = (
            soup.select_one("div.priceView-hero-price.priceView-customer-price span[aria-hidden='true']")
            or soup.select_one("span.screenReaderOnly_3anTj")
            or soup.select_one("div.priceView-hero-price span")
        )
        if price_el:
            p_text = price_el.get_text(strip=True)
            match = re.search(r"[\d.,]+", p_text)
            if match:
                try:
                    result["price"] = float(match.group(0).replace(",", ""))
                except ValueError:
                    pass

        # 4. Model / Brand
        model_el = soup.select_one(".product-data-value.body-copy")
        if model_el:
            result["model"] = model_el.get_text(strip=True)

        if result.get("title") or result.get("price"):
            result["extraction_source"] = "BESTBUY_ADAPTER"
            return result

        return None
