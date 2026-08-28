import re
from typing import Dict, Any, Optional
from bs4 import BeautifulSoup
from app.adapters.base import BaseTargetAdapter


class AmazonAdapter(BaseTargetAdapter):
    """Custom target adapter for Amazon domains (DE, ES, BR, US, UK, etc.)."""

    ASIN_PATTERN = re.compile(r"/(?:dp|gp/product|d)/([A-Z0-9]{10})", re.I)

    def extract_custom(self, html: str, url: str, soup: Optional[BeautifulSoup] = None) -> Optional[Dict[str, Any]]:
        if not html or len(html.strip()) < 50:
            return None

        if soup is None:
            soup = BeautifulSoup(html, "html.parser")

        # Bot check detection
        if any(phrase in html for phrase in ["Type the characters you see in this image", "Robot Check", "api-services-support@amazon.com"]):
            return None

        result: Dict[str, Any] = {}

        # 1. ASIN extraction
        asin_match = self.ASIN_PATTERN.search(url)
        if asin_match:
            result["product_id"] = asin_match.group(1).upper()
            result["sku"] = result["product_id"]
        else:
            asin_input = soup.select_one("input#ASIN, input[name='ASIN'], [data-asin]")
            if asin_input:
                val = asin_input.get("value") or asin_input.get("data-asin")
                if val and len(val.strip()) == 10:
                    result["product_id"] = val.strip().upper()
                    result["sku"] = result["product_id"]

        # 2. Title
        title_el = soup.select_one("#productTitle") or soup.select_one("#title")
        if title_el:
            result["title"] = title_el.get_text(strip=True)

        # 3. Price & Currency
        price_el = (
            soup.select_one(".apexPriceToPay .a-offscreen")
            or soup.select_one("#priceblock_ourprice")
            or soup.select_one("#priceblock_dealprice")
            or soup.select_one("#corePrice_desktop .a-price .a-offscreen")
            or soup.select_one("span.a-price span.a-offscreen")
            or soup.select_one(".a-price .a-offscreen")
        )
        if price_el:
            price_text = price_el.get_text(strip=True)
            # Detect currency from price symbol if present
            if "R$" in price_text:
                result["currency"] = "BRL"
            elif "€" in price_text:
                result["currency"] = "EUR"
            elif "£" in price_text:
                result["currency"] = "GBP"
            elif "₹" in price_text:
                result["currency"] = "INR"
            elif "¥" in price_text or "￥" in price_text:
                result["currency"] = "JPY"
            elif "$" in price_text and not result.get("currency"):
                result["currency"] = self.target_config.currency or "USD"

            match = re.search(r"[\d.,]+", price_text)
            if match:
                raw_num = match.group(0).strip()
                try:
                    if "," in raw_num and "." in raw_num:
                        if raw_num.rfind(",") > raw_num.rfind("."):
                            # European/Brazilian format: 2.690,00 -> 2690.00
                            clean = raw_num.replace(".", "").replace(",", ".")
                        else:
                            # US/UK format: 1,299.00 -> 1299.00
                            clean = raw_num.replace(",", "")
                    elif "," in raw_num:
                        parts = raw_num.split(",")
                        if len(parts) == 2 and len(parts[1]) == 2:
                            clean = raw_num.replace(",", ".")
                        else:
                            clean = raw_num.replace(",", "")
                    else:
                        clean = raw_num
                    clean = re.sub(r"[^\d.]", "", clean)
                    if clean:
                        result["price"] = float(clean)
                except (ValueError, TypeError):
                    pass

        # 4. Brand
        brand_el = soup.select_one("#bylineInfo") or soup.select_one(".po-brand .a-span9")
        if brand_el:
            b_text = brand_el.get_text(strip=True)
            b_text = re.sub(r"^(Visit the|Brand:|Visite a loja|Besuche den)\s*", "", b_text, flags=re.I).strip()
            if b_text:
                result["brand"] = b_text

        # 5. Availability
        avail_el = (
            soup.select_one("#availability .a-color-base")
            or soup.select_one("#availability .a-text-bold")
            or soup.select_one(".primary-availability-message")
            or soup.select_one("#availability span")
            or soup.select_one("#availability")
            or soup.select_one("#outOfStock")
            or soup.select_one(".availability")
        )
        if avail_el:
            avail_text = avail_el.get_text(strip=True)
            result["stock_status"] = avail_text
            avail_lower = avail_text.lower()
            if any(k in avail_lower for k in ["in stock", "em estoque", "en stock", "auf lager", "disponible"]):
                result["availability"] = "InStock"
            if any(k in avail_lower for k in [
                "currently unavailable", "out of stock", "não disponível", "no disponible",
                "derzeit nicht verfügbar", "nicht verfügbar", "non disponible", "esgotado", "agotado",
                "temporariamente indisponível", "temporarily out of stock", "pas disponible"
            ]):
                result["availability"] = "OutOfStock"

        # 6. Rating & Reviews
        rating_el = soup.select_one("#acrPopover") or soup.select_one("i.a-icon-star span")
        if rating_el:
            r_text = rating_el.get_text(strip=True)
            r_match = re.search(r"([\d.,]+)\s+(?:out of|von|de)", r_text)
            if r_match:
                try:
                    result["rating"] = float(r_match.group(1).replace(",", "."))
                except ValueError:
                    pass

        review_el = soup.select_one("#acrCustomerReviewText")
        if review_el:
            rev_text = review_el.get_text(strip=True)
            rev_match = re.search(r"[\d,.]+", rev_text)
            if rev_match:
                try:
                    clean_rev = rev_match.group(0).replace(",", "").replace(".", "")
                    result["review_count"] = int(clean_rev)
                except ValueError:
                    pass

        # 7. Images
        img_el = soup.select_one("#landingImage") or soup.select_one("#imgBlkFront") or soup.select_one(".imgTagWrapper img")
        if img_el:
            src = img_el.get("data-old-hires") or img_el.get("data-a-dynamic-image") or img_el.get("src")
            if src and src.startswith("http"):
                result["image_urls"] = [src]
            elif src and "{" in src:
                # Dynamic image JSON map
                try:
                    import json
                    img_dict = json.loads(src)
                    if img_dict:
                        result["image_urls"] = list(img_dict.keys())[:3]
                except Exception:
                    pass

        # 8. Description
        desc_el = soup.select_one("#productDescription") or soup.select_one("#feature-bullets")
        if desc_el:
            result["description"] = desc_el.get_text(separator=" ", strip=True)

        if result.get("title") or result.get("price"):
            result["extraction_source"] = "AMAZON_ADAPTER"
            return result

        return None
