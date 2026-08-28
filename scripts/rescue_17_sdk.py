"""
Bright Data SDK-Powered Rescue for 17 Remaining Retailers.
============================================================

Uses the official brightdata-sdk Python package (SyncBrightDataClient.scrape_url)
which correctly handles authentication and routing, bypassing the blocked-IP issue
with the direct REST API.

Strategy cascade per target:
1. SDK scrape_url with candidate product URLs
2. SDK scrape_url with Google SERP discovery to find real product URLs
3. SDK scrape_url with country-specific Google Shopping queries
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

# Load env
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

# ─── 17 Remaining Failed Targets ────────────────────────────────────────
RESCUE_TARGETS = [
    {
        "target_id": "bestbuy-ca",
        "retailer": "Best Buy",
        "country": "Canada",
        "domain": "bestbuy.ca",
        "iso": "ca",
        "candidates": [
            "https://www.bestbuy.ca/en-ca/product/asus-vivobook-15-15-6-laptop-quiet-blue-intel-core-i5-1235u-512gb-ssd-16gb-ram-windows-11/17158742",
            "https://www.bestbuy.ca/en-ca/product/hp-15-6-laptop-natural-silver-intel-core-i3-1215u-512gb-ssd-8gb-ram-windows-11/17083884",
        ],
        "serp_queries": [
            "site:bestbuy.ca laptop product",
            "bestbuy.ca laptop notebook buy asus hp lenovo",
        ]
    },
    {
        "target_id": "boulanger-fr",
        "retailer": "Boulanger",
        "country": "France",
        "domain": "boulanger.com",
        "iso": "fr",
        "candidates": [
            "https://www.boulanger.com/ref/1199341",
            "https://www.boulanger.com/c/ordinateur-portable",
        ],
        "serp_queries": [
            "site:boulanger.com ordinateur portable laptop achat",
            "boulanger.com PC portable notebook achat",
        ]
    },
    {
        "target_id": "coupang-kr",
        "retailer": "Coupang",
        "country": "South Korea",
        "domain": "coupang.com",
        "iso": "kr",
        "candidates": [
            "https://www.coupang.com/vp/products/7581273934",
        ],
        "serp_queries": [
            "site:coupang.com laptop notebook 노트북",
            "coupang.com 노트북 구매",
        ]
    },
    {
        "target_id": "elkjop-dk",
        "retailer": "Elkjøp / Elgiganten",
        "country": "Denmark",
        "domain": "elgiganten.dk",
        "iso": "dk",
        "candidates": [
            "https://www.elgiganten.dk/product/computer-kontor/computere/baerbar-computer/lenovo-ideapad-slim-3-158-baerbar-computer-gra/605928",
        ],
        "serp_queries": [
            "site:elgiganten.dk bærbar computer laptop",
            "elgiganten.dk laptop bærbar notebook køb",
        ]
    },
    {
        "target_id": "elkjop-no",
        "retailer": "Elkjøp",
        "country": "Norway",
        "domain": "elkjop.no",
        "iso": "no",
        "candidates": [
            "https://www.elkjop.no/product/pc-data-og-kontor/datamaskiner/barbar-pc/lenovo-ideapad-slim-3-158-barbar-pc-gra/605928",
        ],
        "serp_queries": [
            "site:elkjop.no bærbar PC laptop",
            "elkjop.no laptop notebook kjøp",
        ]
    },
    {
        "target_id": "euronics-it",
        "retailer": "Euronics",
        "country": "Italy",
        "domain": "euronics.it",
        "iso": "it",
        "candidates": [
            "https://www.euronics.it/informatica/computer/notebook/lenovo-ideapad-slim-3-15iau7-82rk009fix-arctic-grey/232001429.html",
        ],
        "serp_queries": [
            "site:euronics.it notebook portatile laptop",
            "euronics.it notebook laptop acquista",
        ]
    },
    {
        "target_id": "expert-de",
        "retailer": "Expert",
        "country": "Germany",
        "domain": "expert.de",
        "iso": "de",
        "candidates": [
            "https://www.expert.de/shop/unsere-produkte/computer-zubehor/notebooks/17044033544-ideapad-slim-3-15iah8-abys-blue-notebook.html",
        ],
        "serp_queries": [
            "site:expert.de notebook laptop kaufen",
            "expert.de notebook laptop HP Lenovo ASUS",
        ]
    },
    {
        "target_id": "fnac-fr",
        "retailer": "Fnac",
        "country": "France",
        "domain": "fnac.com",
        "iso": "fr",
        "candidates": [
            "https://www.fnac.com/PC-Portable-Lenovo-IdeaPad-Slim-3-15IAU7-15-6-Intel-Core-i5-16-Go-RAM-512-Go-SSD-Gris-arctique/a18118042/w-4",
        ],
        "serp_queries": [
            "site:fnac.com PC portable laptop ordinateur",
            "fnac.com PC portable notebook acheter",
        ]
    },
    {
        "target_id": "gmarket-kr",
        "retailer": "Gmarket",
        "country": "South Korea",
        "domain": "gmarket.co.kr",
        "iso": "kr",
        "candidates": [
            "https://item.gmarket.co.kr/Item?goodscode=3148154181",
        ],
        "serp_queries": [
            "site:gmarket.co.kr 노트북 laptop notebook",
            "gmarket.co.kr 노트북 laptop 구매",
        ]
    },
    {
        "target_id": "jd-cn",
        "retailer": "JD",
        "country": "China",
        "domain": "jd.com",
        "iso": "cn",
        "candidates": [
            "https://item.jd.com/100058349272.html",
        ],
        "serp_queries": [
            "site:jd.com 笔记本电脑 laptop",
            "jd.com 笔记本电脑 购买",
        ]
    },
    {
        "target_id": "magazineluiza-br",
        "retailer": "Magazine Luiza",
        "country": "Brazil",
        "domain": "magazineluiza.com.br",
        "iso": "br",
        "candidates": [
            "https://www.magazineluiza.com.br/notebook-lenovo-ideapad-1-15iau7-intel-core-i5-8gb-256gb-ssd-156-linux/p/237936100/in/note/",
        ],
        "serp_queries": [
            "site:magazineluiza.com.br notebook laptop",
            "magazineluiza.com.br notebook comprar",
        ]
    },
    {
        "target_id": "mediamarkt-de",
        "retailer": "MediaMarkt",
        "country": "Germany",
        "domain": "mediamarkt.de",
        "iso": "de",
        "candidates": [
            "https://www.mediamarkt.de/de/product/_lenovo-ideapad-slim-3-notebook-mit-156-zoll-display-intelr-coretm-i5-prozessor-16-gb-ram-512-gb-ssd-intel-iris-xe-grafik-arctic-grey-2882736.html",
        ],
        "serp_queries": [
            "site:mediamarkt.de notebook laptop kaufen",
            "mediamarkt.de notebook laptop HP Lenovo",
        ]
    },
    {
        "target_id": "mercadolibre-cl",
        "retailer": "MercadoLibre",
        "country": "Chile",
        "domain": "mercadolibre.cl",
        "iso": "cl",
        "candidates": [
            "https://articulo.mercadolibre.cl/MLC-1456123894-notebook-lenovo-ideapad-1-15-fhd-ryzen-3-7320u-8gb-256gb-ssd-_JM",
        ],
        "serp_queries": [
            "site:mercadolibre.cl notebook laptop",
            "mercadolibre.cl notebook laptop comprar",
        ]
    },
    {
        "target_id": "monsternotebook-tr",
        "retailer": "Monster Notebook",
        "country": "Turkey",
        "domain": "monsternotebook.com.tr",
        "iso": "tr",
        "candidates": [
            "https://www.monsternotebook.com.tr/abra/monster-abra-a5-v20-3-2/",
            "https://www.monsternotebook.com.tr/tulpar/monster-tulpar-t7-v20-5/",
        ],
        "serp_queries": [
            "site:monsternotebook.com.tr laptop notebook",
        ]
    },
    {
        "target_id": "reliancedigital-in",
        "retailer": "Reliance Digital",
        "country": "India",
        "domain": "reliancedigital.in",
        "iso": "in",
        "candidates": [
            "https://www.reliancedigital.in/hp-15s-fq5007tu-laptop-12th-gen-intel-core-i3-1215u-8gb-512gb-ssd-intel-uhd-graphics-windows-11-home-fhd-39-6-cm-15-6-inch-/p/493177751",
        ],
        "serp_queries": [
            "site:reliancedigital.in laptop notebook buy",
            "reliancedigital.in laptop HP Lenovo buy",
        ]
    },
    {
        "target_id": "tmall-cn",
        "retailer": "Tmall",
        "country": "China",
        "domain": "tmall.com",
        "iso": "cn",
        "candidates": [
            "https://detail.tmall.com/item.htm?id=723489123812",
        ],
        "serp_queries": [
            "site:tmall.com 笔记本电脑 laptop",
            "tmall.com 笔记本电脑 购买",
        ]
    },
    {
        "target_id": "yodobashi-jp",
        "retailer": "Yodobashi",
        "country": "Japan",
        "domain": "yodobashi.com",
        "iso": "jp",
        "candidates": [
            "https://www.yodobashi.com/product/100000001008432194/",
        ],
        "serp_queries": [
            "site:yodobashi.com ノートパソコン laptop",
            "yodobashi.com ノートパソコン 購入",
        ]
    },
]


def extract_title(html: str, url: str) -> str:
    """Extract the most likely product title from HTML."""
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
    title_tag = soup.select_one("title")
    return title_tag.get_text(strip=True) if title_tag else ""


def classify(html: str, url: str) -> Tuple[bool, ClassificationResult, str]:
    """Classify content."""
    title = extract_title(html, url)
    cls = LaptopClassifier.classify(title=title, html=html, url=url)
    return cls.is_genuine_laptop, cls, title


def extract_product_urls(html: str, domain: str) -> List[str]:
    """Extract product URLs from a category/search page."""
    soup = BeautifulSoup(html, "html.parser")
    urls = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if not href.startswith("http"):
            href = f"https://{domain}{href}" if href.startswith("/") else ""
        if domain in href and any(kw in href.lower() for kw in 
            ["product", "item", "/p/", "/ref/", "/dp/", ".html", "/pdp", "/vp/", "goodscode"]):
            if "category" not in href.lower() and "search" not in href.lower():
                urls.append(href)
    return list(dict.fromkeys(urls))[:5]


def extract_serp_urls(html: str, domain: str) -> List[str]:
    """Extract domain-matching URLs from Google SERP HTML."""
    soup = BeautifulSoup(html, "html.parser")
    urls = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "/url?q=" in href:
            actual = href.split("/url?q=")[1].split("&")[0]
            if domain in actual:
                urls.append(actual)
        elif domain in href and href.startswith("http"):
            urls.append(href)
    return list(dict.fromkeys(urls))[:8]


def save_evidence(target_id: str, result: Dict[str, Any], html: str = "") -> None:
    """Save evidence."""
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
        "failure_reason": result.get("failure_reason"),
    }
    with open(ev_dir / "evidence_summary.json", "w") as f:
        json.dump(summary, f, indent=2, default=str)
    if html:
        with open(ev_dir / "product_page.html", "w", errors="replace") as f:
            f.write(html[:50000])
    print(f"  📁 Evidence saved: {target_id}", flush=True)


def sdk_scrape(client: SyncBrightDataClient, url: str) -> Optional[str]:
    """Scrape URL using SDK. Returns HTML or None."""
    try:
        result = client.scrape_url(url)
        if result.success and result.data and len(str(result.data)) > 200:
            return str(result.data)
    except Exception as e:
        print(f"     ⚠️  SDK error: {str(e)[:80]}", flush=True)
    return None


def rescue_target(client: SyncBrightDataClient, target: Dict) -> Dict:
    """Rescue a single target using the Bright Data SDK."""
    t_id = target["target_id"]
    retailer = target["retailer"]
    country = target["country"]
    domain = target["domain"]
    iso = target["iso"]
    candidates = target["candidates"]
    
    print(f"\n{'='*60}", flush=True)
    print(f"🎯 [{t_id}] {retailer} ({country}) — {domain}", flush=True)
    print(f"{'='*60}", flush=True)
    
    # Phase 1: Try candidate URLs directly
    for url in candidates:
        print(f"  🔄 SDK scrape: {url[:80]}...", flush=True)
        html = sdk_scrape(client, url)
        if html:
            is_laptop, cls_res, title = classify(html, url)
            if is_laptop:
                print(f"  ✅ SUCCESS! {title[:70]}", flush=True)
                result = {
                    "target_id": t_id, "retailer": retailer, "country": country,
                    "domain": domain, "can_scrape": "YES",
                    "strategy": "BRIGHTDATA_SDK_SCRAPE", "url": url,
                    "title": title, "brand": cls_res.detected_brand or retailer,
                    "specs": cls_res.extracted_specs, "method": "Bright Data SDK scrape_url",
                }
                save_evidence(t_id, result, html)
                return result
            else:
                print(f"     Content ({len(html)} bytes) class={cls_res.product_class}. Title: {title[:60]}", flush=True)
                
                # If category page, extract product links and retry
                if cls_res.product_class in (ProductClass.CATEGORY_PAGE, ProductClass.OTHER, ProductClass.UNKNOWN):
                    prod_urls = extract_product_urls(html, domain)
                    if prod_urls:
                        print(f"     🔍 Extracted {len(prod_urls)} product links from page", flush=True)
                        for pu in prod_urls[:3]:
                            print(f"  🔄 Extracted link: {pu[:80]}...", flush=True)
                            pu_html = sdk_scrape(client, pu)
                            if pu_html:
                                pu_laptop, pu_cls, pu_title = classify(pu_html, pu)
                                if pu_laptop:
                                    print(f"  ✅ SUCCESS via extracted link! {pu_title[:70]}", flush=True)
                                    result = {
                                        "target_id": t_id, "retailer": retailer, "country": country,
                                        "domain": domain, "can_scrape": "YES",
                                        "strategy": "BRIGHTDATA_SDK_SCRAPE", "url": pu,
                                        "title": pu_title, "brand": pu_cls.detected_brand or retailer,
                                        "specs": pu_cls.extracted_specs,
                                        "method": "Bright Data SDK (category→product)",
                                    }
                                    save_evidence(t_id, result, pu_html)
                                    return result
                            time.sleep(1)
        else:
            print(f"     ❌ No content returned", flush=True)
        time.sleep(1)
    
    # Phase 2: SERP Discovery via Google
    for query in target.get("serp_queries", []):
        google_url = f"https://www.google.com/search?q={query.replace(' ', '+')}&num=10"
        print(f"  🔍 SERP: {query[:60]}...", flush=True)
        serp_html = sdk_scrape(client, google_url)
        if serp_html:
            discovered = extract_serp_urls(serp_html, domain)
            if discovered:
                print(f"     Found {len(discovered)} domain URLs via SERP", flush=True)
                for d_url in discovered[:4]:
                    print(f"  🔄 SERP-discovered: {d_url[:80]}...", flush=True)
                    d_html = sdk_scrape(client, d_url)
                    if d_html:
                        d_laptop, d_cls, d_title = classify(d_html, d_url)
                        if d_laptop:
                            print(f"  ✅ SUCCESS via SERP! {d_title[:70]}", flush=True)
                            result = {
                                "target_id": t_id, "retailer": retailer, "country": country,
                                "domain": domain, "can_scrape": "YES",
                                "strategy": "BRIGHTDATA_SERP_DISCOVERY", "url": d_url,
                                "title": d_title, "brand": d_cls.detected_brand or retailer,
                                "specs": d_cls.extracted_specs,
                                "method": "Bright Data SDK (SERP discovery)",
                            }
                            save_evidence(t_id, result, d_html)
                            return result
                        else:
                            print(f"     Content ({len(d_html)} bytes) class={d_cls.product_class}", flush=True)
                    time.sleep(1)
            else:
                print(f"     ⚠️  No domain URLs found in SERP results", flush=True)
        time.sleep(1)
    
    # Phase 3: Try Google Shopping specifically
    shopping_query = f"{domain} laptop notebook buy"
    shopping_url = f"https://www.google.com/search?q={shopping_query.replace(' ', '+')}&tbm=shop"
    print(f"  🛒 Google Shopping: {shopping_query[:60]}...", flush=True)
    shop_html = sdk_scrape(client, shopping_url)
    if shop_html:
        shop_urls = extract_serp_urls(shop_html, domain)
        for su in shop_urls[:3]:
            su_html = sdk_scrape(client, su)
            if su_html:
                su_laptop, su_cls, su_title = classify(su_html, su)
                if su_laptop:
                    print(f"  ✅ SUCCESS via Shopping! {su_title[:70]}", flush=True)
                    result = {
                        "target_id": t_id, "retailer": retailer, "country": country,
                        "domain": domain, "can_scrape": "YES",
                        "strategy": "BRIGHTDATA_SHOPPING_DISCOVERY", "url": su,
                        "title": su_title, "brand": su_cls.detected_brand or retailer,
                        "specs": su_cls.extracted_specs,
                        "method": "Bright Data SDK (Google Shopping)",
                    }
                    save_evidence(t_id, result, su_html)
                    return result
            time.sleep(1)
    
    # All strategies exhausted
    print(f"  ❌ FAILED — all strategies exhausted", flush=True)
    result = {
        "target_id": t_id, "retailer": retailer, "country": country,
        "domain": domain, "can_scrape": "NO", "strategy": "NONE",
        "url": None, "title": None, "brand": None, "specs": {},
        "failure_reason": "All Bright Data SDK strategies exhausted — anti-bot or content issues.",
    }
    save_evidence(t_id, result)
    return result


def main():
    print("=" * 60, flush=True)
    print("  BRIGHT DATA SDK RESCUE — 17 REMAINING TARGETS", flush=True)
    print(f"  API Token: {'SET' if os.environ.get('BRIGHTDATA_API_TOKEN') else 'MISSING'}", flush=True)
    print(f"  Timestamp: {datetime.now(timezone.utc).isoformat()}", flush=True)
    print("=" * 60, flush=True)
    
    results = []
    with SyncBrightDataClient() as client:
        for target in RESCUE_TARGETS:
            result = rescue_target(client, target)
            results.append(result)
            time.sleep(2)
    
    # Summary
    rescued = [r for r in results if r["can_scrape"] == "YES"]
    failed = [r for r in results if r["can_scrape"] != "YES"]
    
    print(f"\n{'='*60}", flush=True)
    print(f"  RESCUE COMPLETE: {len(rescued)}/{len(RESCUE_TARGETS)} rescued", flush=True)
    print(f"{'='*60}", flush=True)
    
    if rescued:
        print("\n  ✅ NEWLY RESCUED:", flush=True)
        for r in rescued:
            print(f"    {r['retailer']:25s} ({r['country']:12s}) → {(r.get('title') or 'N/A')[:50]}", flush=True)
    if failed:
        print("\n  ❌ STILL FAILED:", flush=True)
        for r in failed:
            print(f"    {r['retailer']:25s} ({r['country']:12s})", flush=True)
    
    # Save results
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    with open(REPORTS_DIR / "rescue_17_sdk_results.json", "w") as f:
        json.dump(results, f, indent=2, default=str)
    
    # Overall benchmark
    all_ev = {}
    for d in sorted(os.listdir(str(EVIDENCE_BASE))):
        fp = EVIDENCE_BASE / d / "evidence_summary.json"
        if fp.exists():
            all_ev[d] = json.load(open(fp))
    
    total_ok = sum(1 for v in all_ev.values() if v.get("can_scrape") == "YES")
    total = len(all_ev)
    print(f"\n  📊 OVERALL: {total_ok}/{total} ({100*total_ok/total:.1f}%)", flush=True)
    
    # Markdown report
    lines = [
        f"# 52-Retailer Laptop Benchmark — Bright Data SDK Rescue",
        f"\n**Date**: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        f"\n**Overall**: {total_ok}/{total} ({100*total_ok/total:.1f}%)",
        f"\n**This Phase**: {len(rescued)}/{len(RESCUE_TARGETS)} rescued",
        "\n## Newly Rescued\n",
    ]
    if rescued:
        lines += ["| Retailer | Country | Strategy | Title |", "|---|---|---|---|"]
        for r in rescued:
            lines.append(f"| {r['retailer']} | {r['country']} | {r['strategy']} | {(r.get('title') or '')[:50]} |")
    lines.append("\n## Still Failed\n")
    if failed:
        lines += ["| Retailer | Country | Reason |", "|---|---|---|"]
        for r in failed:
            lines.append(f"| {r['retailer']} | {r['country']} | {(r.get('failure_reason') or '')[:60]} |")
    lines.append("\n## Full Status\n")
    lines += ["| # | Target | Status | Strategy |", "|---|---|---|---|"]
    for i, (tid, data) in enumerate(sorted(all_ev.items()), 1):
        s = "✅" if data.get("can_scrape") == "YES" else "❌"
        lines.append(f"| {i} | {tid} | {s} | {data.get('strategy','N/A')} |")
    
    with open(REPORTS_DIR / "rescue_17_sdk_report.md", "w") as f:
        f.write("\n".join(lines))
    print(f"\n  📄 Report: reports/rescue_17_sdk_report.md", flush=True)


if __name__ == "__main__":
    main()
