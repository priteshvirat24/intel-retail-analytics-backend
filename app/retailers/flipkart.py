import re
from typing import Dict, Any, Optional
from bs4 import BeautifulSoup
from app.retailers.base_adapter import BaseRetailerAdapter


class FlipkartAdapter(BaseRetailerAdapter):
    """Specialized adapter for Flipkart India."""

    PID_PATTERN = re.compile(r"/p/([a-zA-Z0-9]+)", re.I)

    def extract_custom(self, html: str, url: str, soup: Optional[BeautifulSoup] = None) -> Optional[Dict[str, Any]]:
        if not html:
            return None

        if soup is None:
            soup = BeautifulSoup(html, "html.parser")

        result: Dict[str, Any] = {}

        # 1. Product ID
        pid_match = self.PID_PATTERN.search(url)
        if pid_match:
            result["product_id"] = pid_match.group(1)
            result["sku"] = result["product_id"]

        # 2. Title
        title_el = soup.select_one("span.B_NuCI") or soup.select_one("h1._6EBuvT") or soup.select_one("h1")
        if title_el:
            result["title"] = title_el.get_text(strip=True)

        # 3. Price
        price_el = soup.select_one("div._30jeq3._16J0vi") or soup.select_one("div._30jeq3") or soup.select_one("div.Nx9bqj.CxhGGd")
        if price_el:
            p_text = price_el.get_text(strip=True)
            match = re.search(r"[\d,]+", p_text)
            if match:
                try:
                    result["price"] = float(match.group(0).replace(",", ""))
                    result["currency"] = "INR"
                except ValueError:
                    pass

        # 4. Rating & Reviews
        rating_el = soup.select_one("div._3LWZlK") or soup.select_one("div.XQDdHH")
        if rating_el:
            try:
                result["rating"] = float(rating_el.get_text(strip=True))
            except ValueError:
                pass

        # 5. Availability
        out_of_stock = soup.select_one("div._16FRp0") or soup.select_one("div._1V5SDn")
        if out_of_stock:
            result["availability"] = "OutOfStock"
            result["stock_status"] = "Sold Out / Currently Unavailable"
        else:
            result["availability"] = "InStock"
            result["stock_status"] = "In Stock"

        # 6. Images
        images = []
        for img in soup.select("img._396cs4, img.DByuf4"):
            src = img.get("src")
            if src and src.startswith("http") and src not in images:
                images.append(src)
        if images:
            result["image_urls"] = images

        if result.get("title") or result.get("price"):
            result["extraction_source"] = "FLIPKART_ADAPTER"
            return result

        return None
