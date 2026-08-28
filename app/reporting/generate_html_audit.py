import os
import glob
import json
import csv
import re
from bs4 import BeautifulSoup

items = [
    ("amazon-br", "amazon", "Brazil", "B09G9FPHY6", "https://www.amazon.com.br/dp/B09G9FPHY6", "evidence/amazon/BRAZIL/B09G9FPHY6"),
    ("amazon-es", "amazon", "Spain", "B0CL6LMC9N", "https://www.amazon.es/dp/B0CL6LMC9N", "evidence/amazon/SPAIN/B0CL6LMC9N"),
    ("amazon-de", "amazon", "Germany", "B0CL6LMC9N", "https://www.amazon.de/dp/B0CL6LMC9N", "evidence/amazon/GERMANY/B0CL6LMC9N"),
    ("amazon-de", "amazon", "Germany", "B09G91LXFP", "https://www.amazon.de/dp/B09G91LXFP", "evidence/amazon/GERMANY/B09G91LXFP"),
    ("reliancedigital-in", "reliancedigital", "India", "sku_0012", "https://www.reliancedigital.in/product/sku_0012", "evidence/reliancedigital/INDIA/sku_0012"),
    ("tmall-cn", "tmall", "China", "sku_0020", "https://www.tmall.com/product/sku_0020", "evidence/tmall/CHINA/sku_0020"),
    ("tmall-cn", "tmall", "China", "sku_0016", "https://www.tmall.com/product/sku_0016", "evidence/tmall/CHINA/sku_0016"),
    ("tmall-cn", "tmall", "China", "sku_0015", "https://www.tmall.com/product/sku_0015", "evidence/tmall/CHINA/sku_0015"),
    ("amazon-es", "amazon", "Spain", "B09BRF4N2V", "https://www.amazon.es/dp/B09BRF4N2V", "evidence/amazon/SPAIN/B09BRF4N2V"),
    ("flipkart-in", "flipkart", "India", "itm00000005", "https://www.flipkart.com/electronics-item/p/itm00000005", "evidence/flipkart/INDIA/itm00000005"),
    ("flipkart-in", "flipkart", "India", "itm00000003", "https://www.flipkart.com/electronics-item/p/itm00000003", "evidence/flipkart/INDIA/itm00000003"),
    ("flipkart-in", "flipkart", "India", "itm00000020", "https://www.flipkart.com/electronics-item/p/itm00000020", "evidence/flipkart/INDIA/itm00000020"),
    ("flipkart-in", "flipkart", "India", "itm00000018", "https://www.flipkart.com/electronics-item/p/itm00000018", "evidence/flipkart/INDIA/itm00000018"),
]

out_path = "reports/runs/run_20260823_phase3a_forensic/html_forensic_audit.csv"
os.makedirs(os.path.dirname(out_path), exist_ok=True)

rows = []
for tid, ret, country, skuid, url, path in items:
    cr_path = os.path.join(path, "crawl_result.json")
    html_files = glob.glob(os.path.join(path, "*.html"))
    html_content = ""
    if html_files:
        with open(html_files[0], "r", encoding="utf-8", errors="ignore") as f:
            html_content = f.read()
    
    cr = {}
    if os.path.exists(cr_path):
        with open(cr_path) as f:
            try:
                cr = json.load(f)
            except Exception:
                pass

    soup = BeautifulSoup(html_content, "html.parser")
    title_tag = soup.find("title")
    title_text = title_tag.get_text(strip=True) if title_tag else ""
    
    # Flags
    is_captcha = any(k in html_content.lower() for k in ["captcha", "robot check", "g-recaptcha", "h-captcha", "cf-turnstile"])
    is_bot = any(k in html_content.lower() for k in ["cf-chl-bypass", "cloudflare", "challenge-running", "access denied", "attention required", "perimeterx", "datadome", "akamai"]) and not is_captcha
    
    # SPA
    is_spa = bool(soup.find("div", id="root") or soup.find("div", id="__next") or soup.find("div", id="app") or "window.__INITIAL_STATE__" in html_content)
    
    # JSON-LD
    json_ld_tags = soup.find_all("script", type="application/ld+json")
    has_jsonld = len(json_ld_tags) > 0
    
    # Product DOM
    has_product_dom = bool(soup.find(id="productTitle") or soup.find(id="dp-container") or soup.find("h1", class_=re.compile("product|title", re.I)))
    has_embedded_state = bool(soup.find("script", id="__NEXT_DATA__") or "window.__INITIAL_STATE__" in html_content or "window.__data" in html_content or "window.__INITIAL_DATA__" in html_content)
    
    has_price_text = bool(re.search(r"(\$|€|£|R\$|₹|¥|￥)\s?[\d\.,]+", html_content) or soup.select(".a-price, .price, [itemprop=price]"))
    has_title = bool(soup.find(id="productTitle") or (title_text and not any(k in title_text.lower() for k in ["404", "not found", "error", "找不到了", "online electronic shopping store"])))
    has_brand = bool(soup.find(id="bylineInfo") or soup.find(class_=re.compile("brand", re.I)) or soup.find("[itemprop=brand]"))
    has_sku = bool(skuid in html_content)
    has_gtin = bool(re.search(r"\b(gtin|ean|upc)[\"'\s:=]+(\d{8,14})", html_content, re.I))
    
    # Diagnosis: HTTP_EMPTY_BODY, SPA_ROOT_SHELL, BOT_CHALLENGE, CAPTCHA, CONNECTION_FAILURE, GEO_REDIRECT, PRODUCT_NOT_FOUND, UNKNOWN
    content_len = len(html_content)
    status_code = 200
    if cr.get("attempts"):
        status_code = cr["attempts"][0].get("status_code", 200)
    
    if content_len < 200:
        diagnosis = "HTTP_EMPTY_BODY"
    elif is_captcha:
        diagnosis = "CAPTCHA"
    elif "404" in title_text.lower() or "not found" in title_text.lower() or "找不到了" in title_text or "error" in cr.get("final_url", ""):
        diagnosis = "PRODUCT_NOT_FOUND"
    elif is_bot and not has_product_dom:
        diagnosis = "BOT_CHALLENGE"
    elif is_spa and not has_product_dom:
        diagnosis = "SPA_ROOT_SHELL"
    else:
        diagnosis = "UNKNOWN"

    rows.append({
        "target_id": tid,
        "retailer": ret,
        "country": country,
        "sku_id": skuid,
        "url": url,
        "status_code": status_code,
        "content_length": content_len,
        "is_spa_shell": is_spa,
        "is_bot_challenge": is_bot,
        "is_captcha": is_captcha,
        "has_jsonld": has_jsonld,
        "has_product_dom": has_product_dom,
        "has_embedded_state": has_embedded_state,
        "has_price_text": has_price_text,
        "has_title": has_title,
        "has_brand": has_brand,
        "has_sku": has_sku,
        "has_gtin": has_gtin,
        "diagnosis": diagnosis
    })

fieldnames = [
    "target_id", "retailer", "country", "sku_id", "url", "status_code", "content_length",
    "is_spa_shell", "is_bot_challenge", "is_captcha", "has_jsonld", "has_product_dom",
    "has_embedded_state", "has_price_text", "has_title", "has_brand", "has_sku", "has_gtin", "diagnosis"
]

with open(out_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Generated {out_path} with {len(rows)} rows.")
