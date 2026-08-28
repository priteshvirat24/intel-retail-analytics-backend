import re
from typing import Dict, Any, Optional
from bs4 import BeautifulSoup
from app.retailers.base_adapter import BaseRetailerAdapter


class MediaMarktAdapter(BaseRetailerAdapter):
    """Specialized adapter for MediaMarkt (DE, ES, IT, TR)."""

    def extract_custom(self, html: str, url: str, soup: Optional[BeautifulSoup] = None) -> Optional[Dict[str, Any]]:
        if not html:
            return None

        if soup is None:
            soup = BeautifulSoup(html, "html.parser")

        result: Dict[str, Any] = {}

        # 1. Product ID from URL (e.g., product-name-1234567.html)
        id_match = re.search(r"-([0-9]{6,10})\.html", url)
        if id_match:
            result["product_id"] = id_match.group(1)
            result["sku"] = result["product_id"]

        # 2. Title
        title_el = soup.select_one("h1[data-test='product-title']") or soup.select_one("h1")
        if title_el:
            result["title"] = title_el.get_text(strip=True)

        # 3. Price
        price_el = (
            soup.select_one("span[data-test='branded-price-whole-value']")
            or soup.select_one("span.font-headline-bold")
            or soup.select_one("div[data-test='mms-branded-price']")
        )
        if price_el:
            p_text = price_el.get_text(strip=True)
            match = re.search(r"[\d.,]+", p_text)
            if match:
                try:
                    result["price"] = float(match.group(0).replace(".", "").replace(",", "."))
                except ValueError:
                    pass

        if result.get("title") or result.get("price"):
            result["extraction_source"] = "MEDIAMARKT_ADAPTER"
            return result

        return None
