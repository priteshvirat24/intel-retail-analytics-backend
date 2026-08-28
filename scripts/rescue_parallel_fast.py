"""
Parallel Fast Rescue for Final 7 Retailers.
============================================
Runs concurrent worker threads to scrape the remaining 7 targets in parallel.
"""
import os, sys, json, time, re
from pathlib import Path
from typing import Dict, Any, List, Optional
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor, as_completed

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

for line in open(PROJECT_ROOT / ".env"):
    if "=" in line and not line.startswith("#"):
        k, v = line.strip().split("=", 1)
        os.environ.setdefault(k, v)
os.environ.setdefault("BRIGHTDATA_API_TOKEN", os.environ.get("BRIGHTDATA_API_KEY", ""))

from brightdata import SyncBrightDataClient
from app.classification.laptop_classifier import LaptopClassifier
from bs4 import BeautifulSoup

EVIDENCE_BASE = PROJECT_ROOT / "evidence" / "brightdata"

FINAL_7 = [
    {
        "target_id": "jd-cn",
        "retailer": "JD", "country": "China", "domain": "jd.com",
        "category_urls": [],
        "search_queries": [
            "site:item.jd.com 联想 笔记本电脑",
            "site:item.jd.com ThinkPad 笔记本电脑",
            "site:item.jd.com 华硕 笔记本电脑",
            "site:item.jd.com 游戏本",
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
            "site:magazineluiza.com.br notebook dell /p/",
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
            "site:mediamarkt.de/de/product/ lenovo ideapad",
            "site:mediamarkt.de/de/product/ asus vivobook",
            "site:mediamarkt.de/de/product/ hp notebook",
            "site:mediamarkt.de/de/product/ macbook",
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
            "site:articulo.mercadolibre.cl notebook hp",
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
            "site:reliancedigital.in asus laptop /p/",
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
            "site:detail.tmall.com 华硕 笔记本",
            "site:detail.tmall.com 笔记本电脑",
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
            "site:yodobashi.com/product/ ノートパソコン fujitsu",
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
        skip = ["/login", "/cart", "/checkout", "/account", "/blog/", "/aide/",
                "/help/", "/faq/", "javascript:", "#", "mailto:", "tel:", "/service/"]
        if any(s in href.lower() for s in skip):
            continue
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


def process_target(target: Dict) -> Dict:
    t_id = target["target_id"]
    retailer = target["retailer"]
    country = target["country"]
    domain = target["domain"]
    patterns = target.get("product_patterns", [])

    print(f"🚀 [START] {retailer} ({country})", flush=True)

    with SyncBrightDataClient() as client:
        def test_url(url: str, method: str):
            try:
                res = client.scrape_url(url)
                if not res.success or not res.data or len(str(res.data)) < 200:
                    return None
                html = str(res.data)
                title = extract_title(html)
                cls_res = LaptopClassifier.classify(title=title, html=html, url=url)
                if cls_res.is_genuine_laptop:
                    print(f"  🎉 SUCCESS [{retailer} ({country})] [{method}] {title[:60]}", flush=True)
                    result = {
                        "target_id": t_id, "retailer": retailer, "country": country,
                        "domain": domain, "can_scrape": "YES",
                        "strategy": "BRIGHTDATA_SDK_SCRAPE", "url": url,
                        "title": title, "brand": cls_res.detected_brand or retailer,
                        "specs": cls_res.extracted_specs, "method": method,
                    }
                    save_evidence(t_id, result, html)
                    return result
                return {"html": html}
            except Exception as e:
                return None

        # Search queries
        for q in target.get("search_queries", []):
            try:
                sr = client.search.google(query=q, num_results=10)
                if sr.success and sr.data:
                    found = [item.get("url", item.get("link", "")) for item in sr.data if isinstance(item, dict) and domain in item.get("url", item.get("link", ""))]
                    for u in found[:5]:
                        r = test_url(u, "Search→Direct")
                        if r and "can_scrape" in r:
                            return r
                        elif r and "html" in r:
                            nested = extract_product_links(r["html"], domain, patterns)
                            for nu in nested[:3]:
                                nr = test_url(nu, "Search→Page→Product")
                                if nr and "can_scrape" in nr:
                                    return nr
            except Exception:
                pass

        # Category URLs
        for cat_url in target.get("category_urls", []):
            try:
                res = client.scrape_url(cat_url)
                if res.success and res.data:
                    cat_links = extract_product_links(str(res.data), domain, patterns)
                    for cl in cat_links[:5]:
                        r = test_url(cl, "Category→Product")
                        if r and "can_scrape" in r:
                            return r
            except Exception:
                pass

    print(f"  ❌ FAILED [{retailer} ({country})]", flush=True)
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
    print("  PARALLEL FAST RESCUE FOR 7 REMAINING TARGETS", flush=True)
    print("=" * 60, flush=True)

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(process_target, t): t["target_id"] for t in FINAL_7}
        for future in as_completed(futures):
            tid = futures[future]
            try:
                future.result()
            except Exception as e:
                print(f"Error on {tid}: {e}", flush=True)

    # Final summary
    all_ev = {}
    for d in sorted(os.listdir(str(EVIDENCE_BASE))):
        fp = EVIDENCE_BASE / d / "evidence_summary.json"
        if fp.exists():
            all_ev[d] = json.load(open(fp))
    total_ok = sum(1 for v in all_ev.values() if v.get("can_scrape") == "YES")
    total = len(all_ev)
    print(f"\n{'='*60}", flush=True)
    print(f"  FINAL OVERALL BENCHMARK: {total_ok}/{total} ({100*total_ok/total:.1f}%)", flush=True)
    print("=" * 60, flush=True)


if __name__ == "__main__":
    main()
