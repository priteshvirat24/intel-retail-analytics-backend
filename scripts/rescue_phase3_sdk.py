"""
Phase 3 — Targeted Category-Aware Product Extraction.
=====================================================

For each remaining target:
1. Use SDK search.google to find the notebook/laptop category page
2. Scrape that category page
3. Extract ONLY links within the laptop/notebook category path
4. Scrape and classify individual product pages

The key insight: category pages have 100+ links, but only ~20 are
actual laptop product links. We filter by category path keywords.
"""
import os, sys, json, time, re
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime, timezone

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

for line in open(PROJECT_ROOT / ".env"):
    if "=" in line and not line.startswith("#"):
        k, v = line.strip().split("=", 1)
        os.environ.setdefault(k, v)
os.environ.setdefault("BRIGHTDATA_API_TOKEN", os.environ.get("BRIGHTDATA_API_KEY", ""))

from brightdata import SyncBrightDataClient
from app.classification.laptop_classifier import LaptopClassifier, ProductClass
from bs4 import BeautifulSoup

EVIDENCE_BASE = PROJECT_ROOT / "evidence" / "brightdata"
REPORTS_DIR = PROJECT_ROOT / "reports"

# Category path keywords — if a URL contains these, it's likely a laptop product
LAPTOP_PATH_KEYWORDS = [
    "notebook", "laptop", "portatil", "portable", "computer-portatili",
    "baerbar", "bærbar", "barbar", "notebooks", "laptops",
    "노트북", "ノートパソコン", "笔记本",
]

# 15 remaining targets with their known category page URLs and search hints
TARGETS = [
    {
        "target_id": "bestbuy-ca",
        "retailer": "Best Buy", "country": "Canada", "domain": "bestbuy.ca",
        "category_urls": [
            "https://www.bestbuy.ca/en-ca/category/laptops-macbooks/20352",
        ],
        "search_query": "site:bestbuy.ca laptop notebook product",
        "path_filters": ["product", "/en-ca/product/"],
    },
    {
        "target_id": "coupang-kr",
        "retailer": "Coupang", "country": "South Korea", "domain": "coupang.com",
        "category_urls": [
            "https://www.coupang.com/np/categories/187808",
        ],
        "search_query": "coupang 노트북 laptop product",
        "path_filters": ["/vp/products/"],
    },
    {
        "target_id": "elkjop-dk",
        "retailer": "Elkjøp / Elgiganten", "country": "Denmark", "domain": "elgiganten.dk",
        "category_urls": [
            "https://www.elgiganten.dk/catalog/baerbar-computer/4626",
        ],
        "search_query": "site:elgiganten.dk bærbar computer laptop product",
        "path_filters": ["product", "baerbar"],
    },
    {
        "target_id": "elkjop-no",
        "retailer": "Elkjøp", "country": "Norway", "domain": "elkjop.no",
        "category_urls": [
            "https://www.elkjop.no/catalog/barbar-pc/4626",
        ],
        "search_query": "site:elkjop.no bærbar PC laptop product",
        "path_filters": ["product", "barbar"],
    },
    {
        "target_id": "euronics-it",
        "retailer": "Euronics", "country": "Italy", "domain": "euronics.it",
        "category_urls": [
            "https://www.euronics.it/informatica/computer-portatili/notebook/",
        ],
        "search_query": "euronics.it notebook portatile",
        "path_filters": ["computer-portatili/notebook", "informatica/"],
    },
    {
        "target_id": "expert-de",
        "retailer": "Expert", "country": "Germany", "domain": "expert.de",
        "category_urls": [
            "https://www.expert.de/shop/unsere-produkte/computer-zubehor/notebooks",
        ],
        "search_query": "site:expert.de notebook laptop",
        "path_filters": ["notebooks/", "notebook"],
    },
    {
        "target_id": "fnac-fr",
        "retailer": "Fnac", "country": "France", "domain": "fnac.com",
        "category_urls": [
            "https://www.fnac.com/l149/PC-Portable",
        ],
        "search_query": "site:fnac.com PC portable laptop",
        "path_filters": ["PC-Portable", "/a"],
    },
    {
        "target_id": "gmarket-kr",
        "retailer": "Gmarket", "country": "South Korea", "domain": "gmarket.co.kr",
        "category_urls": [],
        "search_query": "site:item.gmarket.co.kr 노트북 notebook",
        "path_filters": ["Item?goodscode=", "item.gmarket"],
    },
    {
        "target_id": "jd-cn",
        "retailer": "JD", "country": "China", "domain": "jd.com",
        "category_urls": [],
        "search_query": "site:item.jd.com 笔记本电脑 ThinkPad",
        "path_filters": ["item.jd.com"],
    },
    {
        "target_id": "magazineluiza-br",
        "retailer": "Magazine Luiza", "country": "Brazil", "domain": "magazineluiza.com.br",
        "category_urls": [
            "https://www.magazineluiza.com.br/notebook/informatica/s/in/note/",
        ],
        "search_query": "site:magazineluiza.com.br notebook laptop /p/",
        "path_filters": ["/p/", "in/note"],
    },
    {
        "target_id": "mediamarkt-de",
        "retailer": "MediaMarkt", "country": "Germany", "domain": "mediamarkt.de",
        "category_urls": [
            "https://www.mediamarkt.de/de/category/laptops-notebooks-362.html",
        ],
        "search_query": "site:mediamarkt.de notebook laptop product",
        "path_filters": ["/product/", "product/_"],
    },
    {
        "target_id": "mercadolibre-cl",
        "retailer": "MercadoLibre", "country": "Chile", "domain": "mercadolibre.cl",
        "category_urls": [
            "https://listado.mercadolibre.cl/notebooks",
        ],
        "search_query": "site:articulo.mercadolibre.cl notebook laptop MLC",
        "path_filters": ["articulo.mercadolibre", "MLC-"],
    },
    {
        "target_id": "reliancedigital-in",
        "retailer": "Reliance Digital", "country": "India", "domain": "reliancedigital.in",
        "category_urls": [
            "https://www.reliancedigital.in/collection/best-gaming-laptops-20-02",
        ],
        "search_query": "site:reliancedigital.in laptop notebook /p/",
        "path_filters": ["/p/"],
    },
    {
        "target_id": "tmall-cn",
        "retailer": "Tmall", "country": "China", "domain": "tmall.com",
        "category_urls": [],
        "search_query": "site:detail.tmall.com 笔记本电脑 联想",
        "path_filters": ["detail.tmall.com/item"],
    },
    {
        "target_id": "yodobashi-jp",
        "retailer": "Yodobashi", "country": "Japan", "domain": "yodobashi.com",
        "category_urls": [
            "https://www.yodobashi.com/category/19-36-503-501/",
        ],
        "search_query": "site:yodobashi.com ノートパソコン product",
        "path_filters": ["/product/"],
    },
]


def extract_title(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    for sel in ["#productTitle", ".product-title", ".pdp-title",
                "[data-testid='product-title']", ".product-name",
                ".product_title", "h1.title", "h1.name",
                "[itemprop='name']", ".pdp__title", "h1"]:
        el = soup.select_one(sel)
        if el:
            txt = el.get_text(strip=True)
            if 5 < len(txt) < 500:
                return txt
    t = soup.select_one("title")
    return t.get_text(strip=True) if t else ""


def extract_laptop_product_urls(html: str, domain: str, path_filters: List[str]) -> List[str]:
    """Extract URLs from HTML that match laptop product path patterns."""
    soup = BeautifulSoup(html, "html.parser")
    urls = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if not href.startswith("http"):
            href = f"https://{domain}{href}" if href.startswith("/") else ""
            if not href:
                continue
        # Must contain the domain
        if domain not in href:
            continue
        # Must match at least one path filter
        if not any(pf in href.lower() for pf in path_filters):
            continue
        # Skip navigation / account / cart
        skip = ["login", "cart", "checkout", "account", "blog", "aide", "help", 
                "faq", "javascript:", "category", "catalog", "/c/", "/search",
                "#", "mailto:", "tel:"]
        if any(s in href.lower() for s in skip):
            continue
        urls.append(href)
    return list(dict.fromkeys(urls))[:10]


def classify(html: str, url: str):
    title = extract_title(html)
    cls = LaptopClassifier.classify(title=title, html=html, url=url)
    return cls.is_genuine_laptop, cls, title


def save_evidence(target_id, result, html=""):
    ev_dir = EVIDENCE_BASE / target_id
    ev_dir.mkdir(parents=True, exist_ok=True)
    summary = {k: result.get(k) for k in ["target_id", "retailer", "country", "domain",
        "can_scrape", "strategy", "method", "url", "title", "brand", "specs"]}
    summary["timestamp"] = datetime.now(timezone.utc).isoformat()
    summary["failure_reason"] = result.get("failure_reason")
    with open(ev_dir / "evidence_summary.json", "w") as f:
        json.dump(summary, f, indent=2, default=str)
    if html:
        with open(ev_dir / "product_page.html", "w", errors="replace") as f:
            f.write(html[:50000])
    print(f"  📁 Evidence saved: {target_id}", flush=True)


def sdk_scrape(client, url):
    try:
        result = client.scrape_url(url)
        if result.success and result.data and len(str(result.data)) > 200:
            return str(result.data)
    except Exception as e:
        print(f"     ⚠️  SDK error: {str(e)[:80]}", flush=True)
    return None


def rescue_target(client, target):
    t_id = target["target_id"]
    retailer = target["retailer"]
    country = target["country"]
    domain = target["domain"]
    path_filters = target.get("path_filters", [])

    print(f"\n{'='*60}", flush=True)
    print(f"🎯 [{t_id}] {retailer} ({country})", flush=True)
    print(f"{'='*60}", flush=True)

    def try_product_url(url, method):
        html = sdk_scrape(client, url)
        if html:
            is_laptop, cls_res, title = classify(html, url)
            if is_laptop:
                print(f"  ✅ SUCCESS! [{method}] {title[:70]}", flush=True)
                result = {
                    "target_id": t_id, "retailer": retailer, "country": country,
                    "domain": domain, "can_scrape": "YES",
                    "strategy": "BRIGHTDATA_SDK_SCRAPE", "url": url,
                    "title": title, "brand": cls_res.detected_brand or retailer,
                    "specs": cls_res.extracted_specs, "method": method,
                }
                save_evidence(t_id, result, html)
                return result
            else:
                print(f"     {cls_res.product_class}: {title[:50]}", flush=True)
                return ("html", html)  # Return HTML for further extraction
        return None

    # Strategy 1: Scrape known category pages and extract product links
    for cat_url in target.get("category_urls", []):
        print(f"  📂 Category: {cat_url[:80]}...", flush=True)
        cat_html = sdk_scrape(client, cat_url)
        if cat_html:
            print(f"     Got {len(cat_html)} bytes", flush=True)
            prod_urls = extract_laptop_product_urls(cat_html, domain, path_filters)
            if prod_urls:
                print(f"     🔍 Found {len(prod_urls)} laptop product links", flush=True)
                for pu in prod_urls[:5]:
                    print(f"  🔄 Product: {pu[:80]}...", flush=True)
                    res = try_product_url(pu, "Category→Product")
                    if isinstance(res, dict):
                        return res
                    time.sleep(1)
            else:
                # Try broader extraction — any link with laptop-related text
                soup = BeautifulSoup(cat_html, "html.parser")
                laptop_links = []
                for a in soup.find_all("a", href=True):
                    href = a["href"]
                    text = a.get_text(strip=True).lower()
                    if not href.startswith("http"):
                        href = f"https://{domain}{href}" if href.startswith("/") else ""
                    if domain in href and any(kw in f"{href} {text}" for kw in LAPTOP_PATH_KEYWORDS):
                        if "category" not in href and "search" not in href and "blog" not in href:
                            laptop_links.append(href)
                laptop_links = list(dict.fromkeys(laptop_links))[:5]
                if laptop_links:
                    print(f"     🔍 Found {len(laptop_links)} laptop-keyword links", flush=True)
                    for ll in laptop_links:
                        print(f"  🔄 Keyword link: {ll[:80]}...", flush=True)
                        res = try_product_url(ll, "Category→KeywordLink")
                        if isinstance(res, dict):
                            return res
                        time.sleep(1)
        time.sleep(1)

    # Strategy 2: Use SDK search.google with structured results
    search_query = target.get("search_query", f"{domain} laptop notebook")
    print(f"  🔍 SDK Search: {search_query[:60]}...", flush=True)
    try:
        search_results = client.search.google(query=search_query, num_results=15)
        if search_results.success and search_results.data:
            urls_from_search = []
            for item in search_results.data:
                if isinstance(item, dict):
                    url = item.get("url", item.get("link", ""))
                    if domain in url:
                        urls_from_search.append(url)
            
            print(f"     Found {len(urls_from_search)} domain URLs", flush=True)
            for su in urls_from_search[:5]:
                print(f"  🔄 Search result: {su[:80]}...", flush=True)
                res = try_product_url(su, "Search→Direct")
                if isinstance(res, dict):
                    return res
                elif isinstance(res, tuple) and res[0] == "html":
                    # Got a page — extract product links from it
                    prod_urls = extract_laptop_product_urls(res[1], domain, path_filters)
                    if prod_urls:
                        print(f"     🔍 Extracted {len(prod_urls)} product links", flush=True)
                        for pu in prod_urls[:3]:
                            print(f"  🔄 Extracted: {pu[:80]}...", flush=True)
                            res2 = try_product_url(pu, "Search→Category→Product")
                            if isinstance(res2, dict):
                                return res2
                            time.sleep(1)
                time.sleep(1)
    except Exception as e:
        print(f"     ⚠️  Search error: {str(e)[:80]}", flush=True)

    # All exhausted
    print(f"  ❌ FAILED", flush=True)
    result = {
        "target_id": t_id, "retailer": retailer, "country": country,
        "domain": domain, "can_scrape": "NO", "strategy": "NONE",
        "url": None, "title": None, "brand": None, "specs": {},
        "failure_reason": "All Bright Data SDK strategies exhausted.",
    }
    save_evidence(t_id, result)
    return result


def main():
    print("=" * 60, flush=True)
    print("  PHASE 3 — CATEGORY-AWARE PRODUCT EXTRACTION", flush=True)
    print(f"  Timestamp: {datetime.now(timezone.utc).isoformat()}", flush=True)
    print("=" * 60, flush=True)

    results = []
    with SyncBrightDataClient() as client:
        for target in TARGETS:
            result = rescue_target(client, target)
            results.append(result)
            time.sleep(2)

    rescued = [r for r in results if r["can_scrape"] == "YES"]
    failed = [r for r in results if r["can_scrape"] != "YES"]

    print(f"\n{'='*60}", flush=True)
    print(f"  PHASE 3 COMPLETE: {len(rescued)}/{len(TARGETS)} rescued", flush=True)
    print(f"{'='*60}", flush=True)
    if rescued:
        print("\n  ✅ NEWLY RESCUED:", flush=True)
        for r in rescued:
            print(f"    {r['retailer']:25s} → {(r.get('title') or 'N/A')[:50]}", flush=True)
    if failed:
        print("\n  ❌ STILL FAILED:", flush=True)
        for r in failed:
            print(f"    {r['retailer']:25s} ({r['country']})", flush=True)

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    with open(REPORTS_DIR / "rescue_phase3_results.json", "w") as f:
        json.dump(results, f, indent=2, default=str)

    all_ev = {}
    for d in sorted(os.listdir(str(EVIDENCE_BASE))):
        fp = EVIDENCE_BASE / d / "evidence_summary.json"
        if fp.exists():
            all_ev[d] = json.load(open(fp))
    total_ok = sum(1 for v in all_ev.values() if v.get("can_scrape") == "YES")
    total = len(all_ev)
    print(f"\n  📊 OVERALL: {total_ok}/{total} ({100*total_ok/total:.1f}%)", flush=True)


if __name__ == "__main__":
    main()
