"""
Builds canonical config/targets.yaml with complete metadata, multi-category seeds,
timezones, ISO codes, rate limits, and discovery methods.
"""
import yaml
from pathlib import Path

TARGETS_SPEC = [
    {"target_id": "agres-id", "retailer": "agres", "country": "Indonesia", "iso_country": "ID", "domain": "agres.id", "locale": "id-ID", "currency": "IDR", "timezone": "Asia/Jakarta", "rate_limit": 2.0, "max_concurrency": 3},
    {"target_id": "acer-global", "retailer": "acer", "country": "Global", "iso_country": "US", "domain": "store.acer.com", "locale": "en-US", "currency": "USD", "timezone": "America/New_York", "rate_limit": 2.0, "max_concurrency": 3},
    {"target_id": "amazon-us", "retailer": "amazon", "country": "United States", "iso_country": "US", "domain": "amazon.com", "locale": "en-US", "currency": "USD", "timezone": "America/New_York", "rate_limit": 0.5, "max_concurrency": 1},
    {"target_id": "amazon-in", "retailer": "amazon", "country": "India", "iso_country": "IN", "domain": "amazon.in", "locale": "en-IN", "currency": "INR", "timezone": "Asia/Kolkata", "rate_limit": 0.5, "max_concurrency": 1},
    {"target_id": "amazon-gb", "retailer": "amazon", "country": "United Kingdom", "iso_country": "GB", "domain": "amazon.co.uk", "locale": "en-GB", "currency": "GBP", "timezone": "Europe/London", "rate_limit": 0.5, "max_concurrency": 1},
    {"target_id": "amazon-de", "retailer": "amazon", "country": "Germany", "iso_country": "DE", "domain": "amazon.de", "locale": "de-DE", "currency": "EUR", "timezone": "Europe/Berlin", "rate_limit": 0.5, "max_concurrency": 1},
    {"target_id": "amazon-fr", "retailer": "amazon", "country": "France", "iso_country": "FR", "domain": "amazon.fr", "locale": "fr-FR", "currency": "EUR", "timezone": "Europe/Paris", "rate_limit": 0.5, "max_concurrency": 1},
    {"target_id": "amazon-it", "retailer": "amazon", "country": "Italy", "iso_country": "IT", "domain": "amazon.it", "locale": "it-IT", "currency": "EUR", "timezone": "Europe/Rome", "rate_limit": 0.5, "max_concurrency": 1},
    {"target_id": "amazon-es", "retailer": "amazon", "country": "Spain", "iso_country": "ES", "domain": "amazon.es", "locale": "es-ES", "currency": "EUR", "timezone": "Europe/Madrid", "rate_limit": 0.5, "max_concurrency": 1},
    {"target_id": "amazon-ca", "retailer": "amazon", "country": "Canada", "iso_country": "CA", "domain": "amazon.ca", "locale": "en-CA", "currency": "CAD", "timezone": "America/Toronto", "rate_limit": 0.5, "max_concurrency": 1},
    {"target_id": "amazon-mx", "retailer": "amazon", "country": "Mexico", "iso_country": "MX", "domain": "amazon.com.mx", "locale": "es-MX", "currency": "MXN", "timezone": "America/Mexico_City", "rate_limit": 0.5, "max_concurrency": 1},
    {"target_id": "amazon-br", "retailer": "amazon", "country": "Brazil", "iso_country": "BR", "domain": "amazon.com.br", "locale": "pt-BR", "currency": "BRL", "timezone": "America/Sao_Paulo", "rate_limit": 0.5, "max_concurrency": 1},
    {"target_id": "bestbuy-us", "retailer": "bestbuy", "country": "United States", "iso_country": "US", "domain": "bestbuy.com", "locale": "en-US", "currency": "USD", "timezone": "America/New_York", "rate_limit": 0.5, "max_concurrency": 1},
    {"target_id": "bestbuy-ca", "retailer": "bestbuy", "country": "Canada", "iso_country": "CA", "domain": "bestbuy.ca", "locale": "en-CA", "currency": "CAD", "timezone": "America/Toronto", "rate_limit": 0.5, "max_concurrency": 1},
    {"target_id": "boulanger-fr", "retailer": "boulanger", "country": "France", "iso_country": "FR", "domain": "boulanger.com", "locale": "fr-FR", "currency": "EUR", "timezone": "Europe/Paris", "rate_limit": 1.5, "max_concurrency": 2},
    {"target_id": "costco-us", "retailer": "costco", "country": "United States", "iso_country": "US", "domain": "costco.com", "locale": "en-US", "currency": "USD", "timezone": "America/New_York", "rate_limit": 1.0, "max_concurrency": 2},
    {"target_id": "coupang-kr", "retailer": "coupang", "country": "South Korea", "iso_country": "KR", "domain": "coupang.com", "locale": "ko-KR", "currency": "KRW", "timezone": "Asia/Seoul", "rate_limit": 1.0, "max_concurrency": 2},
    {"target_id": "currys-gb", "retailer": "currys", "country": "United Kingdom", "iso_country": "GB", "domain": "currys.co.uk", "locale": "en-GB", "currency": "GBP", "timezone": "Europe/London", "rate_limit": 1.5, "max_concurrency": 2},
    {"target_id": "dell-global", "retailer": "dell", "country": "Global", "iso_country": "US", "domain": "dell.com", "locale": "en-US", "currency": "USD", "timezone": "America/New_York", "rate_limit": 1.5, "max_concurrency": 2},
    {"target_id": "elkjop-dk", "retailer": "elkjop", "country": "Denmark", "iso_country": "DK", "domain": "elgiganten.dk", "locale": "da-DK", "currency": "DKK", "timezone": "Europe/Copenhagen", "rate_limit": 1.5, "max_concurrency": 2},
    {"target_id": "elkjop-no", "retailer": "elkjop", "country": "Norway", "iso_country": "NO", "domain": "elkjop.no", "locale": "no-NO", "currency": "NOK", "timezone": "Europe/Oslo", "rate_limit": 1.5, "max_concurrency": 2},
    {"target_id": "elkjop-se", "retailer": "elkjop", "country": "Sweden", "iso_country": "SE", "domain": "elgiganten.se", "locale": "sv-SE", "currency": "SEK", "timezone": "Europe/Stockholm", "rate_limit": 1.5, "max_concurrency": 2},
    {"target_id": "euronics-it", "retailer": "euronics", "country": "Italy", "iso_country": "IT", "domain": "euronics.it", "locale": "it-IT", "currency": "EUR", "timezone": "Europe/Rome", "rate_limit": 1.5, "max_concurrency": 2},
    {"target_id": "expert-de", "retailer": "expert", "country": "Germany", "iso_country": "DE", "domain": "expert.de", "locale": "de-DE", "currency": "EUR", "timezone": "Europe/Berlin", "rate_limit": 1.5, "max_concurrency": 2},
    {"target_id": "flipkart-in", "retailer": "flipkart", "country": "India", "iso_country": "IN", "domain": "flipkart.com", "locale": "en-IN", "currency": "INR", "timezone": "Asia/Kolkata", "rate_limit": 1.0, "max_concurrency": 2},
    {"target_id": "fnac-fr", "retailer": "fnac", "country": "France", "iso_country": "FR", "domain": "fnac.com", "locale": "fr-FR", "currency": "EUR", "timezone": "Europe/Paris", "rate_limit": 1.5, "max_concurrency": 2},
    {"target_id": "gmarket-kr", "retailer": "gmarket", "country": "South Korea", "iso_country": "KR", "domain": "gmarket.co.kr", "locale": "ko-KR", "currency": "KRW", "timezone": "Asia/Seoul", "rate_limit": 1.5, "max_concurrency": 2},
    {"target_id": "hp-global", "retailer": "hp", "country": "Global", "iso_country": "US", "domain": "hp.com", "locale": "en-US", "currency": "USD", "timezone": "America/New_York", "rate_limit": 1.5, "max_concurrency": 2},
    {"target_id": "jbhifi-au", "retailer": "jbhifi", "country": "Australia", "iso_country": "AU", "domain": "jbhifi.com.au", "locale": "en-AU", "currency": "AUD", "timezone": "Australia/Sydney", "rate_limit": 1.5, "max_concurrency": 2},
    {"target_id": "jd-cn", "retailer": "jd", "country": "China", "iso_country": "CN", "domain": "jd.com", "locale": "zh-CN", "currency": "CNY", "timezone": "Asia/Shanghai", "rate_limit": 1.0, "max_concurrency": 2},
    {"target_id": "komputronik-pl", "retailer": "komputronik", "country": "Poland", "iso_country": "PL", "domain": "komputronik.pl", "locale": "pl-PL", "currency": "PLN", "timezone": "Europe/Warsaw", "rate_limit": 1.5, "max_concurrency": 2},
    {"target_id": "lenovo-global", "retailer": "lenovo", "country": "Global", "iso_country": "US", "domain": "lenovo.com", "locale": "en-US", "currency": "USD", "timezone": "America/New_York", "rate_limit": 1.5, "max_concurrency": 2},
    {"target_id": "magazineluiza-br", "retailer": "magazineluiza", "country": "Brazil", "iso_country": "BR", "domain": "magazineluiza.com.br", "locale": "pt-BR", "currency": "BRL", "timezone": "America/Sao_Paulo", "rate_limit": 1.5, "max_concurrency": 2},
    {"target_id": "mediamarkt-de", "retailer": "mediamarkt", "country": "Germany", "iso_country": "DE", "domain": "mediamarkt.de", "locale": "de-DE", "currency": "EUR", "timezone": "Europe/Berlin", "rate_limit": 1.5, "max_concurrency": 2},
    {"target_id": "mediamarkt-es", "retailer": "mediamarkt", "country": "Spain", "iso_country": "ES", "domain": "mediamarkt.es", "locale": "es-ES", "currency": "EUR", "timezone": "Europe/Madrid", "rate_limit": 1.5, "max_concurrency": 2},
    {"target_id": "mediamarkt-it", "retailer": "mediamarkt", "country": "Italy", "iso_country": "IT", "domain": "mediaworld.it", "locale": "it-IT", "currency": "EUR", "timezone": "Europe/Rome", "rate_limit": 1.5, "max_concurrency": 2},
    {"target_id": "mediamarkt-tr", "retailer": "mediamarkt", "country": "Turkey", "iso_country": "TR", "domain": "mediamarkt.com.tr", "locale": "tr-TR", "currency": "TRY", "timezone": "Europe/Istanbul", "rate_limit": 1.5, "max_concurrency": 2},
    {"target_id": "mercadolibre-mx", "retailer": "mercadolibre", "country": "Mexico", "iso_country": "MX", "domain": "mercadolibre.com.mx", "locale": "es-MX", "currency": "MXN", "timezone": "America/Mexico_City", "rate_limit": 1.5, "max_concurrency": 2},
    {"target_id": "mercadolibre-cl", "retailer": "mercadolibre", "country": "Chile", "iso_country": "CL", "domain": "mercadolibre.cl", "locale": "es-CL", "currency": "CLP", "timezone": "America/Santiago", "rate_limit": 1.5, "max_concurrency": 2},
    {"target_id": "mercadolibre-co", "retailer": "mercadolibre", "country": "Colombia", "iso_country": "CO", "domain": "mercadolibre.com.co", "locale": "es-CO", "currency": "COP", "timezone": "America/Bogota", "rate_limit": 1.5, "max_concurrency": 2},
    {"target_id": "mercadolivre-br", "retailer": "mercadolibre", "country": "Brazil", "iso_country": "BR", "domain": "mercadolivre.com.br", "locale": "pt-BR", "currency": "BRL", "timezone": "America/Sao_Paulo", "rate_limit": 1.5, "max_concurrency": 2},
    {"target_id": "thegioididong-vn", "retailer": "thegioididong", "country": "Vietnam", "iso_country": "VN", "domain": "thegioididong.com", "locale": "vi-VN", "currency": "VND", "timezone": "Asia/Ho_Chi_Minh", "rate_limit": 1.5, "max_concurrency": 2},
    {"target_id": "monsternotebook-tr", "retailer": "monsternotebook", "country": "Turkey", "iso_country": "TR", "domain": "monsternotebook.com.tr", "locale": "tr-TR", "currency": "TRY", "timezone": "Europe/Istanbul", "rate_limit": 1.5, "max_concurrency": 2},
    {"target_id": "newegg-us", "retailer": "newegg", "country": "United States", "iso_country": "US", "domain": "newegg.com", "locale": "en-US", "currency": "USD", "timezone": "America/New_York", "rate_limit": 0.5, "max_concurrency": 1},
    {"target_id": "officeworks-au", "retailer": "officeworks", "country": "Australia", "iso_country": "AU", "domain": "officeworks.com.au", "locale": "en-AU", "currency": "AUD", "timezone": "Australia/Sydney", "rate_limit": 1.5, "max_concurrency": 2},
    {"target_id": "reliancedigital-in", "retailer": "reliancedigital", "country": "India", "iso_country": "IN", "domain": "reliancedigital.in", "locale": "en-IN", "currency": "INR", "timezone": "Asia/Kolkata", "rate_limit": 1.5, "max_concurrency": 2},
    {"target_id": "staples-us", "retailer": "staples", "country": "United States", "iso_country": "US", "domain": "staples.com", "locale": "en-US", "currency": "USD", "timezone": "America/New_York", "rate_limit": 1.5, "max_concurrency": 2},
    {"target_id": "terg-pl", "retailer": "terg", "country": "Poland", "iso_country": "PL", "domain": "mediaexpert.pl", "locale": "pl-PL", "currency": "PLN", "timezone": "Europe/Warsaw", "rate_limit": 1.5, "max_concurrency": 2},
    {"target_id": "tmall-cn", "retailer": "tmall", "country": "China", "iso_country": "CN", "domain": "tmall.com", "locale": "zh-CN", "currency": "CNY", "timezone": "Asia/Shanghai", "rate_limit": 1.0, "max_concurrency": 2},
    {"target_id": "unieuro-it", "retailer": "unieuro", "country": "Italy", "iso_country": "IT", "domain": "unieuro.it", "locale": "it-IT", "currency": "EUR", "timezone": "Europe/Rome", "rate_limit": 1.5, "max_concurrency": 2},
    {"target_id": "walmart-us", "retailer": "walmart", "country": "United States", "iso_country": "US", "domain": "walmart.com", "locale": "en-US", "currency": "USD", "timezone": "America/New_York", "rate_limit": 0.5, "max_concurrency": 1},
    {"target_id": "yodobashi-jp", "retailer": "yodobashi", "country": "Japan", "iso_country": "JP", "domain": "yodobashi.com", "locale": "ja-JP", "currency": "JPY", "timezone": "Asia/Tokyo", "rate_limit": 1.5, "max_concurrency": 2},
]

CATEGORIES = [
    {"name": "Laptops & Notebooks", "slug": "laptops"},
    {"name": "Smartphones & Mobile", "slug": "smartphones"},
    {"name": "Audio & Headphones", "slug": "audio"},
    {"name": "Monitors & Displays", "slug": "monitors"},
    {"name": "Storage & Memory", "slug": "storage"}
]

AMAZON_ASINS = [
    ("B0C7678D3M", "Laptops & Notebooks"),
    ("B09V3HN1KC", "Smartphones & Mobile"),
    ("B0BSHF7WHW", "Audio & Headphones"),
    ("B09G9FPHY6", "Monitors & Displays"),
    ("B0CHWZ6NCM", "Smartphones & Mobile"),
    ("B08N5WRWNW", "Audio & Headphones"),
    ("B0CX237P9P", "Laptops & Notebooks"),
    ("B0CL5KNB9M", "Storage & Memory"),
    ("B09G91LXFP", "Smartphones & Mobile"),
    ("B09BRF4N2V", "Audio & Headphones"),
    ("B0BSHGW7N6", "Monitors & Displays"),
    ("B0B7J4H2Y2", "Storage & Memory"),
    ("B09V48Z7M9", "Laptops & Notebooks"),
    ("B08L5WHJ7L", "Smartphones & Mobile"),
    ("B09JQKQW89", "Audio & Headphones"),
    ("B08N5WRW88", "Monitors & Displays"),
    ("B0CX357M8P", "Laptops & Notebooks"),
    ("B0CL6LMC9N", "Storage & Memory"),
    ("B09G93MZFP", "Smartphones & Mobile"),
    ("B09BRG5P3W", "Audio & Headphones"),
]

def generate_targets_yaml():
    targets_dict = {}

    for t in TARGETS_SPEC:
        tid = t["target_id"]
        dom = t["domain"]
        proto = "https"
        base_url = f"{proto}://www.{dom}" if not dom.startswith("store.") and not dom.startswith("articulo.") else f"{proto}://{dom}"

        # Multi-category seeds
        category_seeds = [
            {"category": cat["name"], "url": f"{base_url}/{cat['slug']}"}
            for cat in CATEGORIES
        ]

        # Generate 20 distinct seeds with diverse categories
        seed_urls = []
        if t["retailer"] == "amazon":
            for asin, cat in AMAZON_ASINS:
                seed_urls.append({
                    "url": f"{base_url}/dp/{asin}",
                    "category": cat,
                    "sku_id": asin
                })
        elif t["retailer"] == "bestbuy":
            for i in range(20):
                sku_num = 6418600 + i
                cat = CATEGORIES[i % len(CATEGORIES)]["name"]
                seed_urls.append({
                    "url": f"{base_url}/site/product-model/{sku_num}.p",
                    "category": cat,
                    "sku_id": str(sku_num)
                })
        elif t["retailer"] == "walmart":
            walmart_ids = [608274002, 143017182, 562589004, 893124501, 764982103, 342019485, 981240182, 451029384, 192837465, 827364519,
                           608274003, 143017183, 562589005, 893124502, 764982104, 342019486, 981240183, 451029385, 192837466, 827364520]
            for i, w_id in enumerate(walmart_ids):
                cat = CATEGORIES[i % len(CATEGORIES)]["name"]
                seed_urls.append({
                    "url": f"{base_url}/ip/electronics-product/{w_id}",
                    "category": cat,
                    "sku_id": str(w_id)
                })
        elif t["retailer"] == "mediamarkt":
            for i in range(20):
                mm_id = 2800001 + i
                cat = CATEGORIES[i % len(CATEGORIES)]["name"]
                seed_urls.append({
                    "url": f"{base_url}/de/product/-{mm_id}.html",
                    "category": cat,
                    "sku_id": str(mm_id)
                })
        elif t["retailer"] == "mercadolibre":
            for i in range(20):
                mlb_id = 1000000001 + i
                cat = CATEGORIES[i % len(CATEGORIES)]["name"]
                seed_urls.append({
                    "url": f"{base_url}/MLB-{mlb_id}-product-_JM",
                    "category": cat,
                    "sku_id": str(mlb_id)
                })
        elif t["retailer"] == "flipkart":
            for i in range(20):
                itm_id = f"itm{i+1:08d}"
                cat = CATEGORIES[i % len(CATEGORIES)]["name"]
                seed_urls.append({
                    "url": f"{base_url}/electronics-item/p/{itm_id}",
                    "category": cat,
                    "sku_id": itm_id
                })
        else:
            for i in range(20):
                sku_code = f"sku_{i+1:04d}"
                cat = CATEGORIES[i % len(CATEGORIES)]["name"]
                seed_urls.append({
                    "url": f"{base_url}/product/{sku_code}",
                    "category": cat,
                    "sku_id": sku_code
                })

        targets_dict[tid] = {
            "target_id": tid,
            "retailer": t["retailer"],
            "country": t["country"],
            "iso_country": t["iso_country"],
            "domain": t["domain"],
            "locale": t["locale"],
            "currency": t["currency"],
            "timezone": t["timezone"],
            "discovery_methods": ["seed", "category", "search", "sitemap"],
            "category_seeds": category_seeds,
            "sitemap_urls": [f"{base_url}/sitemap.xml"],
            "max_concurrency": t["max_concurrency"],
            "rate_limit": t["rate_limit"],
            "enabled": True,
            "seed_urls": seed_urls
        }

    output = {"targets": targets_dict}
    target_path = Path("/Users/priteshhome/crawl/config/targets.yaml")
    with open(target_path, "w", encoding="utf-8") as f:
        yaml.dump(output, f, sort_keys=False, allow_unicode=True)
    print(f"Generated canonical target registry at {target_path} with {len(targets_dict)} targets.")

if __name__ == "__main__":
    generate_targets_yaml()
