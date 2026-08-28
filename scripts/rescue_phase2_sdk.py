"""
Phase 2 SDK Rescue — 15 Remaining Targets (after classifier fix).
================================================================

With the improved multilingual classifier (Turkish, Danish, Norwegian,
Japanese, Italian suffixes, body-level scanning, URL brand detection),
re-attempt the 15 still-failing targets.

Key improvements over Phase 1:
1. Better product URL extraction from category pages (CSS selectors)
2. Smarter Google queries with localized terms
3. HTML body content scanning for laptop signals
4. Retry on pages that were fetched but mis-classified
"""
import os
import sys
import json
import time
import re
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
from app.classification.laptop_classifier import LaptopClassifier, ClassificationResult, ProductClass
from bs4 import BeautifulSoup

EVIDENCE_BASE = PROJECT_ROOT / "evidence" / "brightdata"
REPORTS_DIR = PROJECT_ROOT / "reports"

# 15 remaining targets (boulanger-fr and monsternotebook-tr already rescued)
PHASE2_TARGETS = [
    {
        "target_id": "bestbuy-ca",
        "retailer": "Best Buy", "country": "Canada", "domain": "bestbuy.ca", "iso": "ca",
        "serp_queries": [
            "bestbuy.ca en-ca product laptop",
            "best buy canada asus vivobook laptop site:bestbuy.ca",
            "best buy canada hp laptop 15 site:bestbuy.ca",
        ],
    },
    {
        "target_id": "coupang-kr",
        "retailer": "Coupang", "country": "South Korea", "domain": "coupang.com", "iso": "kr",
        "serp_queries": [
            "coupang 노트북 laptop vp products site:coupang.com",
            "coupang.com lenovo ideapad 노트북",
        ],
    },
    {
        "target_id": "elkjop-dk",
        "retailer": "Elkjøp / Elgiganten", "country": "Denmark", "domain": "elgiganten.dk", "iso": "dk",
        "serp_queries": [
            "elgiganten.dk bærbar computer laptop product",
            "site:elgiganten.dk lenovo ideapad bærbar",
            "site:elgiganten.dk hp laptop bærbar computer",
        ],
    },
    {
        "target_id": "elkjop-no",
        "retailer": "Elkjøp", "country": "Norway", "domain": "elkjop.no", "iso": "no",
        "serp_queries": [
            "elkjop.no bærbar PC laptop product",
            "site:elkjop.no lenovo ideapad bærbar",
            "site:elkjop.no hp laptop bærbar pc",
        ],
    },
    {
        "target_id": "euronics-it",
        "retailer": "Euronics", "country": "Italy", "domain": "euronics.it", "iso": "it",
        "serp_queries": [
            "euronics.it notebook portatile laptop prodotto",
            "site:euronics.it lenovo notebook portatile",
            "site:euronics.it hp notebook 15",
        ],
    },
    {
        "target_id": "expert-de",
        "retailer": "Expert", "country": "Germany", "domain": "expert.de", "iso": "de",
        "serp_queries": [
            "expert.de notebook laptop produkt",
            "site:expert.de lenovo ideapad notebook",
            "site:expert.de hp notebook 15",
        ],
    },
    {
        "target_id": "fnac-fr",
        "retailer": "Fnac", "country": "France", "domain": "fnac.com", "iso": "fr",
        "serp_queries": [
            "fnac.com PC portable laptop produit",
            "site:fnac.com lenovo ideapad pc portable",
            "site:fnac.com HP 15 PC portable",
        ],
    },
    {
        "target_id": "gmarket-kr",
        "retailer": "Gmarket", "country": "South Korea", "domain": "gmarket.co.kr", "iso": "kr",
        "serp_queries": [
            "gmarket.co.kr 노트북 laptop Item goodscode",
            "site:gmarket.co.kr 삼성 노트북",
            "site:item.gmarket.co.kr 노트북",
        ],
    },
    {
        "target_id": "jd-cn",
        "retailer": "JD", "country": "China", "domain": "jd.com", "iso": "cn",
        "serp_queries": [
            "jd.com 笔记本电脑 item",
            "site:item.jd.com 联想 笔记本",
            "site:item.jd.com ThinkPad 笔记本电脑",
        ],
    },
    {
        "target_id": "magazineluiza-br",
        "retailer": "Magazine Luiza", "country": "Brazil", "domain": "magazineluiza.com.br", "iso": "br",
        "serp_queries": [
            "magazineluiza.com.br notebook laptop produto",
            "site:magazineluiza.com.br notebook lenovo ideapad",
            "site:magazineluiza.com.br notebook samsung book",
        ],
    },
    {
        "target_id": "mediamarkt-de",
        "retailer": "MediaMarkt", "country": "Germany", "domain": "mediamarkt.de", "iso": "de",
        "serp_queries": [
            "mediamarkt.de notebook laptop produkt",
            "site:mediamarkt.de lenovo ideapad notebook",
            "site:mediamarkt.de HP 15 notebook",
        ],
    },
    {
        "target_id": "mercadolibre-cl",
        "retailer": "MercadoLibre", "country": "Chile", "domain": "mercadolibre.cl", "iso": "cl",
        "serp_queries": [
            "mercadolibre.cl notebook laptop MLC articulo",
            "site:articulo.mercadolibre.cl notebook lenovo",
            "site:articulo.mercadolibre.cl notebook HP",
        ],
    },
    {
        "target_id": "reliancedigital-in",
        "retailer": "Reliance Digital", "country": "India", "domain": "reliancedigital.in", "iso": "in",
        "serp_queries": [
            "reliancedigital.in laptop notebook product",
            "site:reliancedigital.in HP laptop 15",
            "site:reliancedigital.in lenovo ideapad laptop",
        ],
    },
    {
        "target_id": "tmall-cn",
        "retailer": "Tmall", "country": "China", "domain": "tmall.com", "iso": "cn",
        "serp_queries": [
            "tmall.com 笔记本电脑 detail item",
            "site:detail.tmall.com 联想 笔记本",
            "site:detail.tmall.com ThinkPad 笔记本电脑",
        ],
    },
    {
        "target_id": "yodobashi-jp",
        "retailer": "Yodobashi", "country": "Japan", "domain": "yodobashi.com", "iso": "jp",
        "serp_queries": [
            "yodobashi.com ノートパソコン product",
            "site:yodobashi.com lenovo ノートパソコン",
            "site:yodobashi.com HP ノートパソコン",
        ],
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


def extract_product_urls_smart(html: str, domain: str) -> List[str]:
    """Smart product URL extraction from category/listing pages."""
    soup = BeautifulSoup(html, "html.parser")
    urls = []
    
    # Product link selectors used by common ecommerce platforms
    product_selectors = [
        "a[href*='/product/']", "a[href*='/item/']", "a[href*='/p/']",
        "a[href*='/dp/']", "a[href*='/ref/']", "a[href*='.html']",
        "a[href*='/vp/products/']", "a[href*='goodscode']",
        "a[href*='/pdp/']", "a[href*='articulo']",
        # Product cards
        ".product-card a", ".product-item a", ".item-card a",
        "[data-testid*='product'] a", ".productGrid a",
        ".product-list a", ".products a[href]",
    ]
    
    for sel in product_selectors:
        for a in soup.select(sel):
            href = a.get("href", "")
            if not href.startswith("http"):
                href = f"https://{domain}{href}" if href.startswith("/") else ""
            if href and domain in href:
                # Skip obvious non-product links
                skip_patterns = ["/category/", "/categories/", "/search", "/login",
                                "/cart", "/checkout", "/account", "/blog/",
                                "/aide/", "/help/", "/faq/", "javascript:",
                                "/translate", "google.com", "/servicelog"]
                if not any(sp in href.lower() for sp in skip_patterns):
                    urls.append(href)
    
    return list(dict.fromkeys(urls))[:8]


def extract_serp_urls(html: str, domain: str) -> List[str]:
    """Extract domain-matching URLs from Google SERP HTML."""
    soup = BeautifulSoup(html, "html.parser")
    urls = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "/url?q=" in href:
            actual = href.split("/url?q=")[1].split("&")[0]
            if domain in actual and "google.com" not in actual and "translate.google" not in actual:
                urls.append(actual)
        elif domain in href and href.startswith("http") and "google.com" not in href:
            urls.append(href)
    # Filter out accounts/login/translate
    urls = [u for u in urls if not any(x in u for x in ["accounts.google", "translate.google", "/ServiceLogin"])]
    return list(dict.fromkeys(urls))[:8]


def classify(html: str, url: str) -> Tuple[bool, ClassificationResult, str]:
    title = extract_title(html)
    cls = LaptopClassifier.classify(title=title, html=html, url=url)
    return cls.is_genuine_laptop, cls, title


def save_evidence(target_id: str, result: Dict, html: str = "") -> None:
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


def sdk_scrape(client, url: str) -> Optional[str]:
    try:
        result = client.scrape_url(url)
        if result.success and result.data and len(str(result.data)) > 200:
            return str(result.data)
    except Exception as e:
        print(f"     ⚠️  SDK error: {str(e)[:80]}", flush=True)
    return None


def rescue_target(client, target: Dict) -> Dict:
    t_id = target["target_id"]
    retailer = target["retailer"]
    country = target["country"]
    domain = target["domain"]
    
    print(f"\n{'='*60}", flush=True)
    print(f"🎯 [{t_id}] {retailer} ({country}) — {domain}", flush=True)
    print(f"{'='*60}", flush=True)

    def check_and_return(html, url, method):
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
            print(f"     Content ({len(html)} bytes) class={cls_res.product_class}. Title: {title[:60]}", flush=True)
            return None

    # Phase 1: SERP Discovery with better queries
    for query in target.get("serp_queries", []):
        google_url = f"https://www.google.com/search?q={query.replace(' ', '+')}&num=15"
        print(f"  🔍 SERP: {query[:60]}...", flush=True)
        serp_html = sdk_scrape(client, google_url)
        if serp_html:
            discovered = extract_serp_urls(serp_html, domain)
            if discovered:
                print(f"     Found {len(discovered)} URLs", flush=True)
                for d_url in discovered[:5]:
                    print(f"  🔄 Trying: {d_url[:80]}...", flush=True)
                    d_html = sdk_scrape(client, d_url)
                    if d_html:
                        result = check_and_return(d_html, d_url, "SERP Discovery")
                        if result:
                            return result
                        # If category page, extract product links
                        prod_urls = extract_product_urls_smart(d_html, domain)
                        if prod_urls:
                            print(f"     🔍 Extracted {len(prod_urls)} product links", flush=True)
                            for pu in prod_urls[:3]:
                                print(f"  🔄 Product link: {pu[:80]}...", flush=True)
                                pu_html = sdk_scrape(client, pu)
                                if pu_html:
                                    result = check_and_return(pu_html, pu, "SERP→Category→Product")
                                    if result:
                                        return result
                                time.sleep(1)
                    time.sleep(1)
        time.sleep(1)
    
    # Phase 2: Google Shopping
    shop_query = f"{retailer} laptop notebook"
    shop_url = f"https://www.google.com/search?q={shop_query.replace(' ', '+')}&tbm=shop"
    print(f"  🛒 Google Shopping: {shop_query}...", flush=True)
    shop_html = sdk_scrape(client, shop_url)
    if shop_html:
        shop_urls = extract_serp_urls(shop_html, domain)
        for su in shop_urls[:3]:
            su_html = sdk_scrape(client, su)
            if su_html:
                result = check_and_return(su_html, su, "Google Shopping")
                if result:
                    return result
            time.sleep(1)
    
    # All exhausted
    print(f"  ❌ FAILED — all strategies exhausted", flush=True)
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
    print("  PHASE 2 SDK RESCUE — 15 REMAINING (improved classifier)", flush=True)
    print(f"  Timestamp: {datetime.now(timezone.utc).isoformat()}", flush=True)
    print("=" * 60, flush=True)
    
    results = []
    with SyncBrightDataClient() as client:
        for target in PHASE2_TARGETS:
            result = rescue_target(client, target)
            results.append(result)
            time.sleep(2)
    
    rescued = [r for r in results if r["can_scrape"] == "YES"]
    failed = [r for r in results if r["can_scrape"] != "YES"]
    
    print(f"\n{'='*60}", flush=True)
    print(f"  PHASE 2 COMPLETE: {len(rescued)}/{len(PHASE2_TARGETS)} rescued", flush=True)
    print(f"{'='*60}", flush=True)
    if rescued:
        print("\n  ✅ NEWLY RESCUED:", flush=True)
        for r in rescued:
            print(f"    {r['retailer']:25s} ({r['country']:12s}) → {(r.get('title') or 'N/A')[:50]}", flush=True)
    if failed:
        print("\n  ❌ STILL FAILED:", flush=True)
        for r in failed:
            print(f"    {r['retailer']:25s} ({r['country']:12s})", flush=True)
    
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    with open(REPORTS_DIR / "rescue_phase2_results.json", "w") as f:
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
