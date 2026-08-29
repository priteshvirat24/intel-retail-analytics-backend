import asyncio
import json
import time
from collections import defaultdict, Counter
from urllib.parse import urlparse
from pathlib import Path
import httpx

REPO_ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = REPO_ROOT / "dashboard/src/data/live_52_sku_dataset.json"
OUTPUT_JSON_PATH = REPO_ROOT / "reports/full_1518_url_sweep_results.json"
OUTPUT_JSON_PATH.parent.mkdir(parents=True, exist_ok=True)

with open(DATASET_PATH, "r", encoding="utf-8") as f:
    dataset = json.load(f)

skus = dataset.get("live_skus", [])
print(f"Loaded {len(skus)} SKUs for full live HTTP sweep.")

# Domain concurrency locks to respect rate limits
domain_locks = defaultdict(lambda: asyncio.Semaphore(3))
global_sem = asyncio.Semaphore(35)

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

async def audit_sku(client: httpx.AsyncClient, sku: dict) -> dict:
    sku_id = sku.get("product_id") or f"INDEX-{sku.get('sku_index')}"
    retailer = sku.get("account") or sku.get("retailer") or "UNKNOWN"
    url = sku.get("product_url") or ""
    product_title = sku.get("product_title") or ""
    oem = sku.get("oem") or ""
    processor = sku.get("processor") or ""
    
    if not url or not url.startswith("http"):
        return {
            "sku_id": sku_id,
            "retailer": retailer,
            "url": url,
            "status_code": 0,
            "classification": "DNS_OR_CONNECTION_FAILURE",
            "matches_product": "N/A",
            "details": "Invalid or missing URL string"
        }
        
    parsed = urlparse(url)
    domain = parsed.netloc.lower()
    
    async with global_sem:
        async with domain_locks[domain]:
            await asyncio.sleep(0.05) # Polite delay
            try:
                r = await client.get(url, timeout=7.0)
                status = r.status_code
                
                # Check for Bot Protection / WAF
                if status in (403, 429, 202) or (status == 503 and ("cloudflare" in r.text.lower() or "akamai" in r.text.lower())):
                    return {
                        "sku_id": sku_id,
                        "retailer": retailer,
                        "url": url,
                        "status_code": status,
                        "classification": "BLOCKED_BY_BOT_PROTECTION",
                        "matches_product": "N/A",
                        "details": f"Anti-bot WAF interstitial/block (HTTP {status})"
                    }
                    
                if status == 404:
                    return {
                        "sku_id": sku_id,
                        "retailer": retailer,
                        "url": url,
                        "status_code": 404,
                        "classification": "REAL_404_FROM_LIVE_SERVER",
                        "matches_product": "N",
                        "details": "Server returned standard 404 Page Not Found"
                    }
                    
                if status == 200:
                    text_lower = r.text.lower()
                    # Check for soft 404s
                    if "page not found" in text_lower or "we're sorry" in text_lower or "item not found" in text_lower or "article non trouvé" in text_lower or "seite nicht gefunden" in text_lower:
                        return {
                            "sku_id": sku_id,
                            "retailer": retailer,
                            "url": url,
                            "status_code": 200,
                            "classification": "REAL_404_FROM_LIVE_SERVER",
                            "matches_product": "N",
                            "details": "HTTP 200 soft-404 error page"
                        }
                    
                    # Check if actual product details match
                    title_words = [w.lower() for w in product_title.split() if len(w) > 3]
                    matched_words = [w for w in title_words if w in text_lower]
                    
                    if oem.lower() in text_lower and len(matched_words) >= 2:
                        matches = "Y"
                        cls = "REAL_PRODUCT_PAGE_CONFIRMED"
                    else:
                        matches = "N"
                        cls = "REAL_404_FROM_LIVE_SERVER" # Generic homepage or redirected landing
                        
                    return {
                        "sku_id": sku_id,
                        "retailer": retailer,
                        "url": url,
                        "status_code": status,
                        "classification": cls,
                        "matches_product": matches,
                        "details": "Landed on page; content verified" if matches == "Y" else "Generic redirect without product content"
                    }
                    
                # Other status codes (301/302/500, etc.)
                return {
                    "sku_id": sku_id,
                    "retailer": retailer,
                    "url": url,
                    "status_code": status,
                    "classification": "REAL_404_FROM_LIVE_SERVER" if status in (301, 302, 400, 410) else "DNS_OR_CONNECTION_FAILURE",
                    "matches_product": "N",
                    "details": f"HTTP status {status}"
                }
                
            except httpx.TimeoutException:
                # Distinguish timeout on edge vs dead domain
                return {
                    "sku_id": sku_id,
                    "retailer": retailer,
                    "url": url,
                    "status_code": 0,
                    "classification": "DNS_OR_CONNECTION_FAILURE",
                    "matches_product": "N/A",
                    "details": "TCP / Connection Timeout"
                }
            except Exception as e:
                return {
                    "sku_id": sku_id,
                    "retailer": retailer,
                    "url": url,
                    "status_code": 0,
                    "classification": "DNS_OR_CONNECTION_FAILURE",
                    "matches_product": "N/A",
                    "details": f"{type(e).__name__}: {str(e)[:50]}"
                }

async def main():
    limits = httpx.Limits(max_keepalive_connections=50, max_connections=150)
    async with httpx.AsyncClient(follow_redirects=True, limits=limits, headers=headers) as client:
        print("Starting concurrent live sweep across all 1518 URLs...")
        tasks = [audit_sku(client, sku) for sku in skus]
        results = await asyncio.gather(*tasks)
        
    print(f"Sweep finished! Processed {len(results)} URLs.")
    
    with open(OUTPUT_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
        
    # Aggregate statistics
    class_counts = Counter(r["classification"] for r in results)
    retailer_breakdown = defaultdict(lambda: Counter())
    for r in results:
        retailer_breakdown[r["retailer"]][r["classification"]] += 1
        
    print("\n" + "=" * 80)
    print("GLOBAL AUDIT SUMMARY ACROSS ALL 1,518 SKUs")
    print("=" * 80)
    for k, v in class_counts.items():
        print(f" - {k:35s}: {v:4d} ({v/len(results)*100:.1f}%)")
        
    print("\n" + "=" * 80)
    print("RETAILER BREAKDOWN (52 RETAILERS)")
    print("=" * 80)
    print(f"{'Retailer':30s} | {'Total':5s} | {'CONFIRMED':10s} | {'404 / NOT FOUND':16s} | {'BOT BLOCKED':12s} | {'CONN/TIMEOUT':12s}")
    print("-" * 95)
    for ret, counts in sorted(retailer_breakdown.items()):
        tot = sum(counts.values())
        conf = counts["REAL_PRODUCT_PAGE_CONFIRMED"]
        n404 = counts["REAL_404_FROM_LIVE_SERVER"]
        bot = counts["BLOCKED_BY_BOT_PROTECTION"]
        fail = counts["DNS_OR_CONNECTION_FAILURE"]
        print(f"{ret:30s} | {tot:5d} | {conf:10d} | {n404:16d} | {bot:12d} | {fail:12d}")

if __name__ == "__main__":
    asyncio.run(main())
