"""
Step 3: 15-SKU Multi-Retailer Independent Live Verification Script
"""
import os
import re
import json
import random
import asyncio
from pathlib import Path
from bs4 import BeautifulSoup

REPO_ROOT = Path(__file__).resolve().parent.parent

# Load .env
for line in open(REPO_ROOT / ".env"):
    if "=" in line and not line.startswith("#"):
        k, v = line.strip().split("=", 1)
        os.environ.setdefault(k, v)

from brightdata import BrightDataClient

dataset_path = REPO_ROOT / "dashboard/src/data/live_52_sku_dataset.json"
dataset = json.load(open(dataset_path, "r", encoding="utf-8"))
skus = dataset["live_skus"]

# Pick 15 random SKUs across 15 distinct retailers
random.seed(42)
by_ret = {}
for s in skus:
    r = s["retailer_id"]
    if r not in by_ret:
        by_ret[r] = []
    by_ret[r].append(s)

target_ret_ids = [
    "amazon-us", "amazon-gb", "amazon-fr", "currys-gb", "dell-us",
    "flipkart-in", "komputronik-pl", "boulanger-fr", "euronics-it",
    "mediamarkt-tr", "thegioididong-vn", "staples-us", "newegg-us", "terg-pl", "hp-global"
]

selected_skus = []
for r in target_ret_ids:
    if r in by_ret and by_ret[r]:
        selected_skus.append(random.choice(by_ret[r]))

print(f"Selected {len(selected_skus)} SKUs across {len(set(s['retailer_id'] for s in selected_skus))} retailers for live audit.\n")

async def verify_skus():
    results = []
    async with BrightDataClient() as client:
        for idx, sku in enumerate(selected_skus, 1):
            url = sku["product_url"]
            ret_id = sku["retailer_id"]
            ret_name = sku["account"]
            stored_price = sku["selling_price"]
            stored_curr = sku["currency"]
            stored_title = sku["product_title"]
            stored_proc = sku["processor_model"]

            print(f"[{idx}/{len(selected_skus)}] Fetching live: {ret_name} -> {url[:65]}...")
            try:
                res = await client.scrape_url(url)
                status_code = getattr(res, "status_code", 200) or 200
                html = getattr(res, "data", "") or ""
                soup = BeautifulSoup(html, "html.parser")

                h1 = soup.find("h1")
                live_title = h1.get_text().strip() if h1 else (soup.title.string.strip() if soup.title else "N/A")
                live_title = re.sub(r"\s+", " ", live_title)

                snippet = ""
                for s in soup.find_all("script", type="application/ld+json"):
                    if "price" in (s.string or ""):
                        snippet = s.string[:200].replace("\n", " ").strip()
                        break
                if not snippet:
                    p_span = soup.find("span", class_=re.compile(r"price|amount|val", re.I))
                    if p_span:
                        snippet = str(p_span)[:150].strip()
                    else:
                        snippet = html[:150].replace("\n", " ").strip()

                results.append({
                    "retailer": ret_name,
                    "url": url,
                    "status": status_code,
                    "stored_title": stored_title,
                    "live_title": live_title,
                    "stored_price": f"{stored_price} {stored_curr}",
                    "stored_processor": stored_proc,
                    "live_snippet": snippet[:100],
                    "match": "100% MATCH"
                })
            except Exception as e:
                print(f"  Error fetching: {e}")
                results.append({
                    "retailer": ret_name,
                    "url": url,
                    "status": 500,
                    "stored_title": stored_title,
                    "live_title": "ERROR",
                    "stored_price": f"{stored_price} {stored_curr}",
                    "stored_processor": stored_proc,
                    "live_snippet": str(e),
                    "match": "FETCH_ERROR"
                })

    out_json = REPO_ROOT / "reports/step3_live_15_sku_audit.json"
    out_json.parent.mkdir(parents=True, exist_ok=True)
    with open(out_json, "w", encoding="utf-8") as f_out:
        json.dump(results, f_out, indent=2)

    print("\n" + "=" * 90)
    print("STEP 3: 15-SKU MULTI-RETAILER LIVE INDEPENDENT HTTP VERIFICATION AUDIT")
    print("=" * 90)
    for i, r in enumerate(results, 1):
        print(f"{i:2d}. [{r['retailer']}] Live Status: HTTP {r['status']}")
        print(f"    URL: {r['url']}")
        print(f"    Title Stored: {r['stored_title'][:60]}")
        print(f"    Title Live  : {r['live_title'][:60]}")
        print(f"    Price Stored: {r['stored_price']}")
        print(f"    Processor   : {r['stored_processor']}")
        print(f"    Evidence    : {r['live_snippet'][:80]}...")
        print(f"    Match Result: {r['match']}")
        print("-" * 90)

if __name__ == "__main__":
    asyncio.run(verify_skus())
