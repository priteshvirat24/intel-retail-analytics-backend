"""
Final Rescue Script for Remaining 13 Retailers.
================================================
Targets ONLY the 13 unresolved retailers:
1. elkjop-dk
2. elkjop-no
3. euronics-it
4. expert-de
5. fnac-fr
6. gmarket-kr
7. jd-cn
8. magazineluiza-br
9. mediamarkt-de
10. mercadolibre-cl
11. reliancedigital-in
12. tmall-cn
13. yodobashi-jp

Uses Bright Data SDK:
- Direct category scraping with exact product link extraction
- SDK Google search with localized queries
- Full multilingual classifier with brand, model, spec extraction
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

TARGETS_13 = [
    {
        "target_id": "elkjop-dk",
        "retailer": "Elkjøp / Elgiganten", "country": "Denmark", "domain": "elgiganten.dk",
        "category_urls": [
            "https://www.elgiganten.dk/catalog/baerbar-computer/4626",
            "https://www.elgiganten.dk/product/computer-kontor/computere/baerbar-computer",
        ],
        "search_queries": [
            "site:elgiganten.dk/product/ lenovo bærbar computer",
            "site:elgiganten.dk/product/ hp bærbar computer",
            "site:elgiganten.dk bærbar computer ideapad",
        ],
        "product_patterns": [r"/product/.+/\d+", r"baerbar"],
    },
    {
        "target_id": "elkjop-no",
        "retailer": "Elkjøp", "country": "Norway", "domain": "elkjop.no",
        "category_urls": [
            "https://www.elkjop.no/catalog/barbar-pc/4626",
            "https://www.elkjop.no/product/pc-data-og-kontor/datamaskiner/barbar-pc",
        ],
        "search_queries": [
            "site:elkjop.no/product/ lenovo bærbar pc",
            "site:elkjop.no/product/ hp bærbar pc",
            "site:elkjop.no bærbar pc ideapad",
        ],
        "product_patterns": [r"/product/.+/\d+", r"barbar"],
    },
    {
        "target_id": "euronics-it",
        "retailer": "Euronics", "country": "Italy", "domain": "euronics.it",
        "category_urls": [
            "https://www.euronics.it/informatica/computer-portatili/notebook/",
        ],
        "search_queries": [
            "site:euronics.it/informatica/computer-portatili/ notebook",
            "site:euronics.it notebook lenovo portatile",
            "site:euronics.it notebook asus portatile",
        ],
        "product_patterns": [r"/computer-portatili/notebook.+", r"/informatica/.+\.html"],
    },
    {
        "target_id": "expert-de",
        "retailer": "Expert", "country": "Germany", "domain": "expert.de",
        "category_urls": [
            "https://www.expert.de/shop/unsere-produkte/computer-zubehor/notebooks",
        ],
        "search_queries": [
            "site:expert.de/shop/ notebook",
            "site:expert.de lenovo ideapad notebook",
            "site:expert.de hp 15 notebook",
        ],
        "product_patterns": [r"notebook.*\.html", r"/shop/.+notebook.*"],
    },
    {
        "target_id": "fnac-fr",
        "retailer": "Fnac", "country": "France", "domain": "fnac.com",
        "category_urls": [
            "https://www.fnac.com/l149/PC-Portable",
        ],
        "search_queries": [
            "site:fnac.com/PC-Portable- lenovo",
            "site:fnac.com/PC-Portable- asus",
            "site:fnac.com PC Portable /a",
        ],
        "product_patterns": [r"/PC-Portable-.+/a\d+", r"/mp\d+/"],
    },
    {
        "target_id": "gmarket-kr",
        "retailer": "Gmarket", "country": "South Korea", "domain": "gmarket.co.kr",
        "category_urls": [
            "https://browse.gmarket.co.kr/listcategory/100000033",
        ],
        "search_queries": [
            "site:item.gmarket.co.kr 노트북",
            "site:item.gmarket.co.kr 삼성 노트북",
            "site:item.gmarket.co.kr 레노버 노트북",
        ],
        "product_patterns": [r"goodscode=\d+", r"item\.gmarket\.co\.kr"],
    },
    {
        "target_id": "jd-cn",
        "retailer": "JD", "country": "China", "domain": "jd.com",
        "category_urls": [],
        "search_queries": [
            "site:item.jd.com 联想 笔记本",
            "site:item.jd.com ThinkPad 笔记本",
            "site:item.jd.com 华硕 笔记本电脑",
        ],
        "product_patterns": [r"item\.jd\.com/\d+\.html"],
    },
    {
        "target_id": "magazineluiza-br",
        "retailer": "Magazine Luiza", "country": "Brazil", "domain": "magazineluiza.com.br",
        "category_urls": [
            "https://www.magazineluiza.com.br/notebook/informatica/s/in/note/",
        ],
        "search_queries": [
            "site:magazineluiza.com.br/notebook- /p/",
            "site:magazineluiza.com.br notebook lenovo /p/",
            "site:magazineluiza.com.br notebook samsung /p/",
        ],
        "product_patterns": [r"/p/\w+", r"in/note"],
    },
    {
        "target_id": "mediamarkt-de",
        "retailer": "MediaMarkt", "country": "Germany", "domain": "mediamarkt.de",
        "category_urls": [
            "https://www.mediamarkt.de/de/category/laptops-notebooks-362.html",
        ],
        "search_queries": [
            "site:mediamarkt.de/de/product/ lenovo notebook",
            "site:mediamarkt.de/de/product/ asus laptop",
            "site:mediamarkt.de/de/product/ hp notebook",
        ],
        "product_patterns": [r"/de/product/.+-\d+\.html", r"/product/"],
    },
    {
        "target_id": "mercadolibre-cl",
        "retailer": "MercadoLibre", "country": "Chile", "domain": "mercadolibre.cl",
        "category_urls": [
            "https://listado.mercadolibre.cl/notebooks",
        ],
        "search_queries": [
            "site:articulo.mercadolibre.cl notebook lenovo",
            "site:articulo.mercadolibre.cl notebook asus",
            "site:mercadolibre.cl/p/MLC notebook",
        ],
        "product_patterns": [r"MLC-\d+", r"/p/MLC\d+", r"articulo\.mercadolibre\.cl"],
    },
    {
        "target_id": "reliancedigital-in",
        "retailer": "Reliance Digital", "country": "India", "domain": "reliancedigital.in",
        "category_urls": [
            "https://www.reliancedigital.in/sections/laptops",
        ],
        "search_queries": [
            "site:reliancedigital.in/ -laptop- /p/",
            "site:reliancedigital.in hp laptop /p/",
            "site:reliancedigital.in lenovo laptop /p/",
        ],
        "product_patterns": [r"/p/\d{6,}"],
    },
    {
        "target_id": "tmall-cn",
        "retailer": "Tmall", "country": "China", "domain": "tmall.com",
        "category_urls": [],
        "search_queries": [
            "site:detail.tmall.com 联想 笔记本",
            "site:detail.tmall.com ThinkPad 笔记本电脑",
            "site:detail.tmall.com 华为 笔记本",
        ],
        "product_patterns": [r"id=\d+", r"detail\.tmall\.com"],
    },
    {
        "target_id": "yodobashi-jp",
        "retailer": "Yodobashi", "country": "Japan", "domain": "yodobashi.com",
        "category_urls": [
            "https://www.yodobashi.com/category/19-36-503-501/",
        ],
        "search_queries": [
            "site:yodobashi.com/product/ ノートパソコン lenovo",
            "site:yodobashi.com/product/ ノートパソコン dynabook",
            "site:yodobashi.com/product/ ノートパソコン nec",
        ],
        "product_patterns": [r"/product/\d+/"],
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


def extract_product_links(html: str, domain: str, patterns: List[str]) -> List[str]:
    soup = BeautifulSoup(html, "html.parser")
    urls = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if not href.startswith("http"):
            href = f"https://{domain}{href}" if href.startswith("/") else ""
        if not href or domain not in href:
            continue
        
        # Check exclusion
        skip = ["/login", "/cart", "/checkout", "/account", "/blog/", "/aide/",
                "/help/", "/faq/", "javascript:", "#", "mailto:", "tel:", "/service/"]
        if any(s in href.lower() for s in skip):
            continue

        # Check pattern match
        if any(re.search(pat, href, re.IGNORECASE) for pat in patterns):
            urls.append(href)
            
    return list(dict.fromkeys(urls))[:10]


def save_evidence(target_id: str, result: Dict, html: str = ""):
    ev_dir = EVIDENCE_BASE / target_id
    ev_dir.mkdir(parents=True, exist_ok=True)
    summary = {
        "target_id": target_id,
        "retailer": result.get("retailer"),
        "country": result.get("country"),
        "domain": result.get("domain"),
        "can_scrape": result.get("can_scrape", "NO"),
        "strategy": result.get("strategy", "NONE"),
        "method": result.get("method", ""),
        "url": result.get("url"),
        "title": result.get("title"),
        "brand": result.get("brand"),
        "specs": result.get("specs", {}),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "failure_reason": result.get("failure_reason")
    }
    with open(ev_dir / "evidence_summary.json", "w") as f:
        json.dump(summary, f, indent=2, default=str)
    if html:
        with open(ev_dir / "product_page.html", "w", errors="replace") as f:
            f.write(html[:50000])
    print(f"  📁 Evidence saved: {target_id}", flush=True)


def sdk_scrape(client: SyncBrightDataClient, url: str) -> Optional[str]:
    try:
        res = client.scrape_url(url)
        if res.success and res.data and len(str(res.data)) > 200:
            return str(res.data)
    except Exception as e:
        print(f"     ⚠️  SDK scrape error: {str(e)[:80]}", flush=True)
    return None


def rescue_single(client: SyncBrightDataClient, target: Dict) -> Dict:
    t_id = target["target_id"]
    retailer = target["retailer"]
    country = target["country"]
    domain = target["domain"]
    patterns = target.get("product_patterns", [])

    print(f"\n{'='*60}", flush=True)
    print(f"🎯 [{t_id}] {retailer} ({country}) — {domain}", flush=True)
    print(f"{'='*60}", flush=True)

    def test_url(url: str, method: str) -> Optional[Dict]:
        html = sdk_scrape(client, url)
        if not html:
            return None
        title = extract_title(html)
        cls_res = LaptopClassifier.classify(title=title, html=html, url=url)
        if cls_res.is_genuine_laptop:
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
            print(f"     {cls_res.product_class}: {title[:50]} (score={cls_res.confidence_score})", flush=True)
            return {"html": html}

    # Step 1: SDK Search queries
    for q in target.get("search_queries", []):
        print(f"  🔍 SDK Search: {q[:60]}...", flush=True)
        try:
            sr = client.search.google(query=q, num_results=10)
            if sr.success and sr.data:
                found_links = []
                for item in sr.data:
                    if isinstance(item, dict):
                        u = item.get("url", item.get("link", ""))
                        if domain in u:
                            found_links.append(u)
                
                print(f"     Found {len(found_links)} search result links", flush=True)
                for u in found_links[:4]:
                    print(f"  🔄 Testing search link: {u[:80]}...", flush=True)
                    r = test_url(u, "Search→Direct")
                    if r and "can_scrape" in r:
                        return r
                    elif r and "html" in r:
                        # Extract product links from this page
                        nested_links = extract_product_links(r["html"], domain, patterns)
                        for nu in nested_links[:3]:
                            print(f"  🔄 Testing nested link: {nu[:80]}...", flush=True)
                            nr = test_url(nu, "Search→Page→Product")
                            if nr and "can_scrape" in nr:
                                return nr
                            time.sleep(1)
                    time.sleep(1)
        except Exception as e:
            print(f"     ⚠️  Search error: {str(e)[:80]}", flush=True)
        time.sleep(1)

    # Step 2: Category page scraping
    for cat_url in target.get("category_urls", []):
        print(f"  📂 Category scrape: {cat_url[:80]}...", flush=True)
        cat_html = sdk_scrape(client, cat_url)
        if cat_html:
            cat_links = extract_product_links(cat_html, domain, patterns)
            print(f"     Found {len(cat_links)} matching product links", flush=True)
            for cl in cat_links[:5]:
                print(f"  🔄 Testing category product link: {cl[:80]}...", flush=True)
                r = test_url(cl, "Category→Product")
                if r and "can_scrape" in r:
                    return r
                time.sleep(1)
        time.sleep(1)

    # All exhausted
    print(f"  ❌ FAILED: {retailer} ({country})", flush=True)
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
    print("  FINAL RESCUE FOR 13 REMAINING RETAILERS", flush=True)
    print(f"  Timestamp: {datetime.now(timezone.utc).isoformat()}", flush=True)
    print("=" * 60, flush=True)

    results = []
    with SyncBrightDataClient() as client:
        for target in TARGETS_13:
            res = rescue_single(client, target)
            results.append(res)
            time.sleep(2)

    rescued = [r for r in results if r.get("can_scrape") == "YES"]
    failed = [r for r in results if r.get("can_scrape") != "YES"]

    print(f"\n{'='*60}", flush=True)
    print(f"  RESCUE COMPLETE: {len(rescued)}/{len(TARGETS_13)} newly rescued", flush=True)
    print(f"{'='*60}", flush=True)
    for r in rescued:
        print(f"  ✅ {r['retailer']:25s} ({r['country']:12s}) → {(r.get('title') or '')[:50]}", flush=True)
    for r in failed:
        print(f"  ❌ {r['retailer']:25s} ({r['country']:12s})", flush=True)

    # Update overall summary
    all_ev = {}
    for d in sorted(os.listdir(str(EVIDENCE_BASE))):
        fp = EVIDENCE_BASE / d / "evidence_summary.json"
        if fp.exists():
            all_ev[d] = json.load(open(fp))
    total_ok = sum(1 for v in all_ev.values() if v.get("can_scrape") == "YES")
    total = len(all_ev)
    print(f"\n  📊 OVERALL BENCHMARK: {total_ok}/{total} ({100*total_ok/total:.1f}%)", flush=True)


if __name__ == "__main__":
    main()
