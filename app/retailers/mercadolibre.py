import re
from typing import Dict, Any, Optional
from bs4 import BeautifulSoup
from app.retailers.base_adapter import BaseRetailerAdapter


class MercadoLibreAdapter(BaseRetailerAdapter):
    """Specialized adapter for Mercado Libre (MX, CL, CO) and Mercado Livre (BR)."""

    def extract_custom(self, html: str, url: str, soup: Optional[BeautifulSoup] = None) -> Optional[Dict[str, Any]]:
        if not html:
            return None

        if soup is None:
            soup = BeautifulSoup(html, "html.parser")

        result: Dict[str, Any] = {}

        # 1. Product / Item ID from URL
        item_match = re.search(r"/(ML[A-Z]-[0-9]+)", url) or re.search(r"/p/(ML[A-Z0-9]+)", url)
        if item_match:
            result["product_id"] = item_match.group(1)
            result["sku"] = result["product_id"]

        # 2. Title
        title_el = soup.select_one("h1.ui-pdp-title") or soup.select_one("h1")
        if title_el:
            result["title"] = title_el.get_text(strip=True)

        # 3. Price
        price_el = (
            soup.select_one(".ui-pdp-price__second-line .andes-money-amount__fraction")
            or soup.select_one(".andes-money-amount__fraction")
        )
        if price_el:
            p_text = price_el.get_text(strip=True)
            try:
                result["price"] = float(p_text.replace(".", "").replace(",", "."))
            except ValueError:
                pass

        # 4. Brand
        brand_el = soup.select_one(".ui-pdp-seller__link-trigger") or soup.select_one("tr.andes-table__row th")
        if brand_el:
            result["brand"] = brand_el.get_text(strip=True)

        # 5. Availability
        stock_el = soup.select_one(".ui-pdp-buybox__quantity__available")
        if stock_el:
            result["stock_status"] = stock_el.get_text(strip=True)
            result["availability"] = "InStock"
        else:
            result["availability"] = "InStock"

        if result.get("title") or result.get("price"):
            result["extraction_source"] = "MERCADOLIBRE_ADAPTER"
            return result

        return None
