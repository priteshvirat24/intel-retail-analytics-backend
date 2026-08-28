"""
Test remaining 17 retailers using the direct Bright Data /request endpoint
with exact parameters documented in brightdata-docs.
"""
import os
import json
import httpx
from bs4 import BeautifulSoup
import app.env
from app.classification.laptop_classifier import LaptopClassifier

REMAINING_17 = [
    {"target_id": "bestbuy-ca", "retailer": "Best Buy", "country": "Canada", "iso": "ca", "url": "https://www.bestbuy.ca/en-ca/product/asus-vivobook-15-15-6-laptop-quiet-blue-intel-core-i5-1235u-512gb-ssd-16gb-ram-windows-11/17158742"},
    {"target_id": "boulanger-fr", "retailer": "Boulanger", "country": "France", "iso": "fr", "url": "https://www.boulanger.com/ref/1199341"},
    {"target_id": "coupang-kr", "retailer": "Coupang", "country": "South Korea", "iso": "kr", "url": "https://www.coupang.com/vp/products/7581273934"},
    {"target_id": "elkjop-dk", "retailer": "Elkjøp", "country": "Denmark", "iso": "dk", "url": "https://www.elgiganten.dk/product/computer-kontor/computere/baerbar-computer/lenovo-ideapad-slim-3-158-baerbar-computer-gra/605928"},
    {"target_id": "elkjop-no", "retailer": "Elkjøp", "country": "Norway", "iso": "no", "url": "https://www.elkjop.no/product/pc-data-og-kontor/datamaskiner/barbar-pc/lenovo-ideapad-slim-3-158-barbar-pc-gra/605928"},
    {"target_id": "euronics-it", "retailer": "Euronics", "country": "Italy", "iso": "it", "url": "https://www.euronics.it/informatica/computer/notebook/lenovo-ideapad-slim-3-15iau7-82rk009fix-arctic-grey/232001429.html"},
    {"target_id": "expert-de", "retailer": "Expert", "country": "Germany", "iso": "de", "url": "https://www.expert.de/shop/unsere-produkte/computer-zubehor/notebooks/17044033544-ideapad-slim-3-15iah8-abys-blue-notebook.html"},
    {"target_id": "fnac-fr", "retailer": "Fnac", "country": "France", "iso": "fr", "url": "https://www.fnac.com/PC-Portable-Lenovo-IdeaPad-Slim-3-15IAU7-15-6-Intel-Core-i5-16-Go-RAM-512-Go-SSD-Gris-arctique/a18118042/w-4"},
    {"target_id": "gmarket-kr", "retailer": "Gmarket", "country": "South Korea", "iso": "kr", "url": "https://item.gmarket.co.kr/Item?goodscode=3148154181"},
    {"target_id": "jd-cn", "retailer": "JD", "country": "China", "iso": "cn", "url": "https://item.jd.com/100058349272.html"},
    {"target_id": "magazineluiza-br", "retailer": "Magazine Luiza", "country": "Brazil", "iso": "br", "url": "https://www.magazineluiza.com.br/notebook-lenovo-ideapad-1-15iau7-intel-core-i5-8gb-256gb-ssd-156-linux/p/237936100/in/note/"},
    {"target_id": "mediamarkt-de", "retailer": "MediaMarkt", "country": "Germany", "iso": "de", "url": "https://www.mediamarkt.de/de/product/_lenovo-ideapad-slim-3-notebook-mit-156-zoll-display-intelr-coretm-i5-prozessor-16-gb-ram-512-gb-ssd-intel-iris-xe-grafik-arctic-grey-2882736.html"},
    {"target_id": "mercadolibre-cl", "retailer": "MercadoLibre", "country": "Chile", "iso": "cl", "url": "https://articulo.mercadolibre.cl/MLC-1456123894-notebook-lenovo-ideapad-1-15-fhd-ryzen-3-7320u-8gb-256gb-ssd-_JM"},
    {"target_id": "monsternotebook-tr", "retailer": "Monster Notebook", "country": "Turkey", "iso": "tr", "url": "https://www.monsternotebook.com.tr/abra/monster-abra-a5-v20-3-2/"},
    {"target_id": "reliancedigital-in", "retailer": "Reliance Digital", "country": "India", "iso": "in", "url": "https://www.reliancedigital.in/hp-15s-fq5007tu-laptop-12th-gen-intel-core-i3-1215u-8gb-512gb-ssd-intel-uhd-graphics-windows-11-home-fhd-39-6-cm-15-6-inch-/p/493177751"},
    {"target_id": "tmall-cn", "retailer": "Tmall", "country": "China", "iso": "cn", "url": "https://detail.tmall.com/item.htm?id=723489123812"},
    {"target_id": "yodobashi-jp", "retailer": "Yodobashi", "country": "Japan", "iso": "jp", "url": "https://www.yodobashi.com/product/100000001008432194/"}
]

api_key = os.environ.get("BRIGHTDATA_API_KEY")
zone = os.environ.get("BRIGHTDATA_ZONE", "web_unlocker1")
headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

for item in REMAINING_17:
    ret = item["retailer"]
    cnt = item["country"]
    iso = item["iso"]
    url = item["url"]
    
    # Try POST https://api.brightdata.com/request with country
    body = {
        "zone": zone,
        "url": url,
        "format": "raw",
        "country": iso
    }
    try:
        r = httpx.post("https://api.brightdata.com/request", headers=headers, json=body, timeout=25.0)
        if r.status_code == 200 and len(r.text) > 500:
            soup = BeautifulSoup(r.text, "html.parser")
            title_tag = soup.select_one("h1, #productTitle, title")
            t_str = title_tag.get_text(strip=True) if title_tag else ""
            cls_res = LaptopClassifier.classify(title=t_str, html=r.text, url=url)
            if cls_res.is_genuine_laptop:
                print(f"[SUCCESS /request] {ret} ({cnt}) -> {t_str[:60]}")
            else:
                print(f"[REJECTED /request] {ret} ({cnt}) -> Title: {t_str[:40]} | Reason: {cls_res.rejection_reason}")
        else:
            print(f"[BLOCKED /request] {ret} ({cnt}) -> HTTP {r.status_code}")
    except Exception as e:
        print(f"[ERROR /request] {ret} ({cnt}) -> {e}")
