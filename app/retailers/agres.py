from typing import Dict, Any, Optional
from bs4 import BeautifulSoup
from app.retailers.base_adapter import BaseRetailerAdapter

class AgresAdapter(BaseRetailerAdapter):
    """Custom adapter for Agres Indonesia."""

    def extract_custom(self, html: str, url: str, soup: Optional[BeautifulSoup] = None) -> Optional[Dict[str, Any]]:
        if not soup:
            soup = BeautifulSoup(html, "html.parser")
            
        data = {}
        
        # Example DOM selectors for Agres
        title_el = soup.select_one("h1.product-title, h1[itemprop='name']")
        if title_el:
            data["title"] = title_el.get_text(strip=True)
            
        price_el = soup.select_one(".price-amount, .price, .product-price")
        if price_el:
            price_text = price_el.get_text(strip=True).replace("Rp", "").replace("$", "").replace(".", "").strip()
            try:
                data["price"] = float(price_text)
                data["currency"] = "IDR"
            except ValueError:
                pass
                
        brand_el = soup.select_one(".brand-name, [itemprop='brand']")
        if brand_el:
            data["brand"] = brand_el.get_text(strip=True)
            
        img_el = soup.select_one(".product-image img, [itemprop='image']")
        if img_el and img_el.get("src"):
            src = img_el.get("src")
            if not src.startswith("http"):
                src = "https:" + src if src.startswith("//") else "https://www.agres.id" + src
            data["image_urls"] = [src]
            
        sku_el = soup.select_one(".sku, [itemprop='sku']")
        if sku_el:
            data["sku"] = sku_el.get("content") or sku_el.get_text(strip=True)
            
        if not data:
            return None
            
        return data
