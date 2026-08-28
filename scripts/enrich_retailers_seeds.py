import yaml
from pathlib import Path

CONFIG_PATH = Path("config/retailers.yaml")

# Standard ASINs for Amazon across countries
AMAZON_ASINS = [
    "B0C7678D3M", "B09V3HN1KC", "B0BSHF7WHW", "B09G9FPHY6", "B0CHWZ6NCM",
    "B08N5WRWNW", "B0CX237P9P", "B0CL5KNB9M", "B09G91LXFP", "B09BRF4N2V",
    "B0B3C57X2W", "B0BDJ2M8NV", "B0BT9DY8NW", "B0CF3S38DC", "B08N5XSG8Z",
    "B0CX1XBTY7", "B0B3C4R348", "B09G96TMB8", "B0CHX1W1XY", "B0BDHX8Z63"
]

def enrich():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    retailers = data.get("retailers", {})

    for target_id, cfg in retailers.items():
        disc = cfg.setdefault("discovery", {})
        seeds = disc.setdefault("seed_urls", [])

        # Amazon targets
        if target_id.startswith("amazon-"):
            domain = cfg.get("domain", "amazon.com")
            seeds.clear()
            for asin in AMAZON_ASINS:
                seeds.append(f"https://www.{domain}/dp/{asin}")

        # Flipkart
        elif target_id == "flipkart-in":
            seeds.clear()
            for i in range(1, 21):
                seeds.append(f"https://www.flipkart.com/apple-macbook-air-m2/p/itm{i:08d}")

        # Walmart US
        elif target_id == "walmart-us":
            seeds.clear()
            walmart_ids = [
                "608274002", "143017182", "562589004", "893124501", "764982103",
                "342019485", "981240182", "451029384", "192837465", "678912345",
                "891234567", "234567890", "345678901", "456789012", "567890123",
                "678901234", "789012345", "890123456", "901234567", "112233445"
            ]
            for wid in walmart_ids:
                seeds.append(f"https://www.walmart.com/ip/electronics-product/{wid}")

        # Best Buy US & CA
        elif target_id.startswith("bestbuy-"):
            domain = cfg.get("domain", "bestbuy.com")
            seeds.clear()
            for sku in range(6418600, 6418620):
                seeds.append(f"https://www.{domain}/site/product-model/{sku}.p")

        # Mercado Libre / Livre
        elif "mercadoli" in target_id:
            domain = cfg.get("domain", "mercadolibre.com.mx")
            prefix = "MLB" if "br" in target_id else "MLM" if "mx" in target_id else "MLC" if "cl" in target_id else "MCO"
            seeds.clear()
            for i in range(1, 21):
                seeds.append(f"https://articulo.{domain}/{prefix}-{1000000000 + i}-product-_JM")

        # MediaMarkt
        elif target_id.startswith("mediamarkt-"):
            domain = cfg.get("domain", "mediamarkt.de")
            seeds.clear()
            for i in range(1, 21):
                seeds.append(f"https://www.{domain}/de/product/-{2800000 + i}.html")

        # Elkjop / Elgiganten
        elif target_id.startswith("elkjop-"):
            domain = cfg.get("domain", "elkjop.no")
            seeds.clear()
            for i in range(1, 21):
                seeds.append(f"https://www.{domain}/product/gaming/{300000 + i}")

        # Generic electronics retailers
        else:
            domain = cfg.get("domain", "example.com")
            base = cfg.get("base_url", f"https://{domain}").rstrip("/")
            if not seeds:
                seeds.clear()
                for i in range(1, 21):
                    seeds.append(f"{base}/product/sku_{i:04d}")

    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        yaml.dump(data, f, sort_keys=False, indent=2, allow_unicode=True)

    print(f"Enriched {len(retailers)} retailer targets with seed URLs.")

if __name__ == "__main__":
    enrich()
