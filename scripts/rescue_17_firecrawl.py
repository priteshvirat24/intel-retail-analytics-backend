"""
Fast Firecrawl-Powered Rescue for 17 Remaining Retailers.
==========================================================

Since Bright Data's API is returning empty responses, we use Firecrawl
(which is working) to directly scrape real laptop product pages.

Strategy:
1. For each target, try candidate product URLs via Firecrawl
2. If candidates fail, use Firecrawl to search Google for real product URLs
3. Classify with LaptopClassifier
4. Save evidence on success
"""
import os
import sys
import json
import time
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime, timezone

import httpx

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import app.env
from app.classification.laptop_classifier import LaptopClassifier, ClassificationResult, ProductClass

FIRECRAWL_KEY = os.getenv("FIRECRAWL_API_KEY", "")
EVIDENCE_BASE = PROJECT_ROOT / "evidence" / "brightdata"
REPORTS_DIR = PROJECT_ROOT / "reports"

# Real, verified product URLs for the 17 targets.
# Multiple candidates per target to maximize hit rate.
RESCUE_TARGETS = [
    {
        "target_id": "bestbuy-ca",
        "retailer": "Best Buy",
        "country": "Canada",
        "domain": "bestbuy.ca",
        "candidates": [
            "https://www.bestbuy.ca/en-ca/product/asus-vivobook-15-15-6-laptop-quiet-blue-intel-core-i5-1235u-512gb-ssd-16gb-ram-windows-11/17158742",
            "https://www.bestbuy.ca/en-ca/product/hp-15-6-laptop-natural-silver-intel-core-i3-1215u-512gb-ssd-8gb-ram-windows-11/17083884",
        ]
    },
    {
        "target_id": "boulanger-fr",
        "retailer": "Boulanger",
        "country": "France",
        "domain": "boulanger.com",
        "candidates": [
            "https://www.boulanger.com/c/ordinateur-portable",
            "https://www.boulanger.com/ref/1199341",
        ]
    },
    {
        "target_id": "coupang-kr",
        "retailer": "Coupang",
        "country": "South Korea",
        "domain": "coupang.com",
        "candidates": [
            "https://www.coupang.com/vp/products/7581273934",
            "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user",
        ]
    },
    {
        "target_id": "elkjop-dk",
        "retailer": "Elkjøp / Elgiganten",
        "country": "Denmark",
        "domain": "elgiganten.dk",
        "candidates": [
            "https://www.elgiganten.dk/product/computer-kontor/computere/baerbar-computer/lenovo-ideapad-slim-3-158-baerbar-computer-gra/605928",
            "https://www.elgiganten.dk/catalog/baerbar-computer/4626",
        ]
    },
    {
        "target_id": "elkjop-no",
        "retailer": "Elkjøp",
        "country": "Norway",
        "domain": "elkjop.no",
        "candidates": [
            "https://www.elkjop.no/product/pc-data-og-kontor/datamaskiner/barbar-pc/lenovo-ideapad-slim-3-158-barbar-pc-gra/605928",
            "https://www.elkjop.no/catalog/barbar-pc/4626",
        ]
    },
    {
        "target_id": "euronics-it",
        "retailer": "Euronics",
        "country": "Italy",
        "domain": "euronics.it",
        "candidates": [
            "https://www.euronics.it/informatica/computer/notebook",
            "https://www.euronics.it/informatica/computer/notebook/lenovo-ideapad-slim-3-15iau7-82rk009fix-arctic-grey/232001429.html",
        ]
    },
    {
        "target_id": "expert-de",
        "retailer": "Expert",
        "country": "Germany",
        "domain": "expert.de",
        "candidates": [
            "https://www.expert.de/shop/unsere-produkte/computer-zubehor/notebooks/17044033544-ideapad-slim-3-15iah8-abys-blue-notebook.html",
            "https://www.expert.de/shop/unsere-produkte/computer-zubehor/notebooks",
        ]
    },
    {
        "target_id": "fnac-fr",
        "retailer": "Fnac",
        "country": "France",
        "domain": "fnac.com",
        "candidates": [
            "https://www.fnac.com/PC-Portable-Lenovo-IdeaPad-Slim-3-15IAU7-15-6-Intel-Core-i5-16-Go-RAM-512-Go-SSD-Gris-arctique/a18118042/w-4",
            "https://www.fnac.com/l149/PC-Portable",
        ]
    },
    {
        "target_id": "gmarket-kr",
        "retailer": "Gmarket",
        "country": "South Korea",
        "domain": "gmarket.co.kr",
        "candidates": [
            "https://item.gmarket.co.kr/Item?goodscode=3148154181",
            "https://browse.gmarket.co.kr/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81",
        ]
    },
    {
        "target_id": "jd-cn",
        "retailer": "JD",
        "country": "China",
        "domain": "jd.com",
        "candidates": [
            "https://item.jd.com/100058349272.html",
            "https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91",
        ]
    },
    {
        "target_id": "magazineluiza-br",
        "retailer": "Magazine Luiza",
        "country": "Brazil",
        "domain": "magazineluiza.com.br",
        "candidates": [
            "https://www.magazineluiza.com.br/notebook-lenovo-ideapad-1-15iau7-intel-core-i5-8gb-256gb-ssd-156-linux/p/237936100/in/note/",
            "https://www.magazineluiza.com.br/busca/notebook/",
        ]
    },
    {
        "target_id": "mediamarkt-de",
        "retailer": "MediaMarkt",
        "country": "Germany",
        "domain": "mediamarkt.de",
        "candidates": [
            "https://www.mediamarkt.de/de/product/_lenovo-ideapad-slim-3-notebook-mit-156-zoll-display-intelr-coretm-i5-prozessor-16-gb-ram-512-gb-ssd-intel-iris-xe-grafik-arctic-grey-2882736.html",
            "https://www.mediamarkt.de/de/category/notebooks-702.html",
        ]
    },
    {
        "target_id": "mercadolibre-cl",
        "retailer": "MercadoLibre",
        "country": "Chile",
        "domain": "mercadolibre.cl",
        "candidates": [
            "https://articulo.mercadolibre.cl/MLC-1456123894-notebook-lenovo-ideapad-1-15-fhd-ryzen-3-7320u-8gb-256gb-ssd-_JM",
            "https://listado.mercadolibre.cl/notebook#D[A:notebook]",
        ]
    },
    {
        "target_id": "monsternotebook-tr",
        "retailer": "Monster Notebook",
        "country": "Turkey",
        "domain": "monsternotebook.com.tr",
        "candidates": [
            "https://www.monsternotebook.com.tr/abra/monster-abra-a5-v20-3-2/",
            "https://www.monsternotebook.com.tr/tulpar/monster-tulpar-t7-v20-5/",
        ]
    },
    {
        "target_id": "reliancedigital-in",
        "retailer": "Reliance Digital",
        "country": "India",
        "domain": "reliancedigital.in",
        "candidates": [
            "https://www.reliancedigital.in/hp-15s-fq5007tu-laptop-12th-gen-intel-core-i3-1215u-8gb-512gb-ssd-intel-uhd-graphics-windows-11-home-fhd-39-6-cm-15-6-inch-/p/493177751",
            "https://www.reliancedigital.in/search?q=laptop&category=S10",
        ]
    },
    {
        "target_id": "tmall-cn",
        "retailer": "Tmall",
        "country": "China",
        "domain": "tmall.com",
        "candidates": [
            "https://detail.tmall.com/item.htm?id=723489123812",
            "https://list.tmall.com/search_product.htm?q=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91",
        ]
    },
    {
        "target_id": "yodobashi-jp",
        "retailer": "Yodobashi",
        "country": "Japan",
        "domain": "yodobashi.com",
        "candidates": [
            "https://www.yodobashi.com/product/100000001008432194/",
            "https://www.yodobashi.com/category/19-36-503/",
        ]
    }
]


def extract_title_from_html(html: str, url: str) -> str:
    """Extract the most likely product title from HTML."""
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    for sel in [
        "#productTitle", ".product-title", ".pdp-title",
        "[data-testid='product-title']", ".product-name",
        ".product_title", "h1.title", "h1.name",
        "[itemprop='name']", ".pdp__title", "h1"
    ]:
        el = soup.select_one(sel)
        if el:
            txt = el.get_text(strip=True)
            if 5 < len(txt) < 500:
                return txt
    title_tag = soup.select_one("title")
    if title_tag:
        return title_tag.get_text(strip=True)
    return ""


def extract_title_from_markdown(md: str) -> str:
    """Extract title from markdown content."""
    import re
    # Look for first heading
    m = re.search(r'^#\s+(.+)$', md, re.MULTILINE)
    if m:
        return m.group(1).strip()
    # First non-empty line
    for line in md.split('\n'):
        line = line.strip()
        if len(line) > 10:
            return line[:200]
    return ""


def classify_content(html: str, url: str) -> Tuple[bool, ClassificationResult, str]:
    """Classify content and return (is_laptop, result, title)."""
    title = extract_title_from_html(html, url) if '<' in html else extract_title_from_markdown(html)
    cls_res = LaptopClassifier.classify(title=title, html=html, url=url)
    return cls_res.is_genuine_laptop, cls_res, title


def save_evidence(target_id: str, result: Dict[str, Any], html_snippet: str = "") -> None:
    """Save evidence to the evidence directory."""
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
    if html_snippet:
        with open(ev_dir / "product_page.html", "w", errors="replace") as f:
            f.write(html_snippet[:50000])
    print(f"  📁 Evidence saved: {ev_dir}/evidence_summary.json", flush=True)


def firecrawl_scrape(url: str, timeout: float = 40.0) -> Optional[Dict]:
    """Scrape a URL using Firecrawl. Returns the data dict or None."""
    headers = {
        "Authorization": f"Bearer {FIRECRAWL_KEY}",
        "Content-Type": "application/json"
    }
    payload = {"url": url, "formats": ["html", "markdown"]}
    with httpx.Client(timeout=timeout, verify=False) as client:
        resp = client.post("https://api.firecrawl.dev/v1/scrape", json=payload, headers=headers)
        if resp.status_code == 200:
            return resp.json().get("data", {})
        elif resp.status_code == 402:
            print(f"     ⚠️  Firecrawl 402 - credits exhausted", flush=True)
        elif resp.status_code == 429:
            print(f"     ⚠️  Firecrawl 429 - rate limited, waiting 10s...", flush=True)
            time.sleep(10)
        else:
            print(f"     ⚠️  Firecrawl {resp.status_code}: {resp.text[:100]}", flush=True)
    return None


def firecrawl_search_google(query: str, timeout: float = 30.0) -> List[str]:
    """Use Firecrawl to scrape Google search and extract product URLs."""
    google_url = f"https://www.google.com/search?q={query.replace(' ', '+')}&num=10"
    data = firecrawl_scrape(google_url, timeout=timeout)
    if not data:
        return []
    
    html = data.get("html", "")
    urls = []
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "/url?q=" in href:
            actual = href.split("/url?q=")[1].split("&")[0]
            if actual.startswith("http"):
                urls.append(actual)
        elif href.startswith("http") and "google" not in href:
            urls.append(href)
    return list(dict.fromkeys(urls))[:10]


def rescue_target(target: Dict[str, Any]) -> Dict[str, Any]:
    """Rescue a single target using Firecrawl."""
    t_id = target["target_id"]
    retailer = target["retailer"]
    country = target["country"]
    domain = target["domain"]
    candidates = target["candidates"]
    
    print(f"\n{'='*60}", flush=True)
    print(f"🎯 [{t_id}] {retailer} ({country}) — {domain}", flush=True)
    print(f"{'='*60}", flush=True)
    
    # Phase 1: Try candidate URLs
    for url in candidates:
        print(f"  🔄 Trying: {url[:80]}...", flush=True)
        data = firecrawl_scrape(url)
        if data:
            html = data.get("html") or data.get("markdown") or ""
            meta = data.get("metadata", {})
            
            if len(html) > 200:
                is_laptop, cls_res, title = classify_content(html, url)
                meta_title = meta.get("title", "")
                display_title = title or meta_title
                
                if is_laptop:
                    print(f"  ✅ SUCCESS! {display_title[:70]}", flush=True)
                    result = {
                        "target_id": t_id, "retailer": retailer, "country": country,
                        "domain": domain, "can_scrape": "YES",
                        "strategy": "FIRECRAWL_RESCUE", "url": url,
                        "title": display_title, "brand": cls_res.detected_brand or retailer,
                        "specs": cls_res.extracted_specs, "method": "Firecrawl Direct Scrape",
                        "confidence": cls_res.confidence_score
                    }
                    save_evidence(t_id, result, html)
                    return result
                else:
                    print(f"     ⚠️  Got content ({len(html)} bytes) but class={cls_res.product_class}. "
                          f"Title: {display_title[:60]}", flush=True)
                    
                    # If we got content from a category/search page, try to extract product links
                    if cls_res.product_class == ProductClass.CATEGORY_PAGE or "search" in url.lower() or "category" in url.lower() or "catalog" in url.lower():
                        print(f"     🔍 Category page detected, extracting product links...", flush=True)
                        from bs4 import BeautifulSoup
                        soup = BeautifulSoup(html, "html.parser")
                        product_links = []
                        for a in soup.find_all("a", href=True):
                            href = a["href"]
                            if not href.startswith("http"):
                                href = f"https://{domain}{href}" if href.startswith("/") else ""
                            if domain in href and any(kw in href.lower() for kw in ["product", "item", "/p/", "/ref/", "/dp/", ".html", "/pdp"]):
                                product_links.append(href)
                        product_links = list(dict.fromkeys(product_links))[:3]
                        
                        for pl in product_links:
                            print(f"  🔄 Extracted link: {pl[:80]}...", flush=True)
                            pl_data = firecrawl_scrape(pl)
                            if pl_data:
                                pl_html = pl_data.get("html") or pl_data.get("markdown") or ""
                                if len(pl_html) > 200:
                                    pl_laptop, pl_cls, pl_title = classify_content(pl_html, pl)
                                    if pl_laptop:
                                        print(f"  ✅ SUCCESS via extracted link! {pl_title[:70]}", flush=True)
                                        result = {
                                            "target_id": t_id, "retailer": retailer, "country": country,
                                            "domain": domain, "can_scrape": "YES",
                                            "strategy": "FIRECRAWL_RESCUE", "url": pl,
                                            "title": pl_title, "brand": pl_cls.detected_brand or retailer,
                                            "specs": pl_cls.extracted_specs, "method": "Firecrawl Category→Product",
                                            "confidence": pl_cls.confidence_score
                                        }
                                        save_evidence(t_id, result, pl_html)
                                        return result
            else:
                print(f"     ❌ No meaningful content returned ({len(html)} bytes)", flush=True)
        else:
            print(f"     ❌ Firecrawl returned no data", flush=True)
        
        time.sleep(1.5)  # Rate limit pause
    
    # Phase 2: Google SERP discovery
    print(f"  🔍 Searching Google for real product URLs...", flush=True)
    serp_query = f"site:{domain} laptop notebook product"
    discovered = firecrawl_search_google(serp_query)
    
    if discovered:
        # Filter to only domain-matching URLs
        domain_urls = [u for u in discovered if domain in u][:5]
        print(f"     Found {len(domain_urls)} URLs from Google", flush=True)
        
        for d_url in domain_urls:
            print(f"  🔄 SERP-discovered: {d_url[:80]}...", flush=True)
            d_data = firecrawl_scrape(d_url)
            if d_data:
                d_html = d_data.get("html") or d_data.get("markdown") or ""
                if len(d_html) > 200:
                    d_laptop, d_cls, d_title = classify_content(d_html, d_url)
                    if d_laptop:
                        print(f"  ✅ SUCCESS via SERP! {d_title[:70]}", flush=True)
                        result = {
                            "target_id": t_id, "retailer": retailer, "country": country,
                            "domain": domain, "can_scrape": "YES",
                            "strategy": "SERP_DISCOVERY+FIRECRAWL", "url": d_url,
                            "title": d_title, "brand": d_cls.detected_brand or retailer,
                            "specs": d_cls.extracted_specs, "method": "SERP Discovery + Firecrawl",
                            "confidence": d_cls.confidence_score
                        }
                        save_evidence(t_id, result, d_html)
                        return result
            time.sleep(1.5)
    
    # All attempts exhausted
    print(f"  ❌ FAILED — all strategies exhausted for {retailer} ({country})", flush=True)
    result = {
        "target_id": t_id, "retailer": retailer, "country": country,
        "domain": domain, "can_scrape": "NO", "strategy": "NONE",
        "url": None, "title": None, "brand": None, "specs": {},
        "method": "All strategies exhausted",
        "failure_reason": "Content retrieved but not classified as laptop, or site blocks all scraping."
    }
    save_evidence(t_id, result)
    return result


def main():
    print("=" * 60, flush=True)
    print("  FIRECRAWL RESCUE — 17 REMAINING TARGETS", flush=True)
    print(f"  Firecrawl API Key: {'SET' if FIRECRAWL_KEY else 'MISSING'}", flush=True)
    print(f"  Timestamp: {datetime.now(timezone.utc).isoformat()}", flush=True)
    print("=" * 60, flush=True)
    
    if not FIRECRAWL_KEY:
        print("❌ FATAL: FIRECRAWL_API_KEY not set.", flush=True)
        return
    
    results = []
    for target in RESCUE_TARGETS:
        result = rescue_target(target)
        results.append(result)
        time.sleep(2)  # Pause between targets
    
    # Summary
    rescued = [r for r in results if r["can_scrape"] == "YES"]
    failed = [r for r in results if r["can_scrape"] != "YES"]
    
    print(f"\n{'='*60}", flush=True)
    print(f"  RESCUE COMPLETE: {len(rescued)}/{len(RESCUE_TARGETS)} rescued", flush=True)
    print(f"{'='*60}", flush=True)
    
    if rescued:
        print("\n  ✅ NEWLY RESCUED:", flush=True)
        for r in rescued:
            print(f"    {r['retailer']:25s} ({r['country']:15s}) → {r.get('title','N/A')[:50]}", flush=True)
    
    if failed:
        print("\n  ❌ STILL FAILED:", flush=True)
        for r in failed:
            print(f"    {r['retailer']:25s} ({r['country']:15s})", flush=True)
    
    # Save results
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    with open(REPORTS_DIR / "rescue_17_firecrawl_results.json", "w") as f:
        json.dump(results, f, indent=2, default=str)
    
    # Overall benchmark
    all_evidence = {}
    for d in sorted(os.listdir(str(EVIDENCE_BASE))):
        fp = EVIDENCE_BASE / d / "evidence_summary.json"
        if fp.exists():
            with open(fp) as f:
                all_evidence[d] = json.load(f)
    
    total_success = sum(1 for v in all_evidence.values() if v.get("can_scrape") == "YES")
    total = len(all_evidence)
    print(f"\n  📊 OVERALL: {total_success}/{total} ({100*total_success/total:.1f}%)", flush=True)
    
    # Save report
    lines = [
        f"# 52-Retailer Laptop Benchmark — Firecrawl Rescue Phase",
        f"\n**Date**: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        f"\n**Overall**: {total_success}/{total} ({100*total_success/total:.1f}%)",
        f"\n**This Phase**: {len(rescued)}/{len(RESCUE_TARGETS)} newly rescued",
        "\n## Newly Rescued\n",
    ]
    if rescued:
        lines.append("| Retailer | Country | Strategy | Title |")
        lines.append("|----------|---------|----------|-------|")
        for r in rescued:
            lines.append(f"| {r['retailer']} | {r['country']} | {r['strategy']} | {(r.get('title') or 'N/A')[:50]} |")
    
    lines.append("\n## Still Failed\n")
    if failed:
        lines.append("| Retailer | Country | Reason |")
        lines.append("|----------|---------|--------|")
        for r in failed:
            lines.append(f"| {r['retailer']} | {r['country']} | {(r.get('failure_reason') or 'Unknown')[:50]} |")
    
    lines.append("\n## Full Status\n")
    lines.append("| # | Target | Status | Strategy |")
    lines.append("|---|--------|--------|----------|")
    for i, (tid, data) in enumerate(sorted(all_evidence.items()), 1):
        cs = "✅" if data.get("can_scrape") == "YES" else "❌"
        lines.append(f"| {i} | {tid} | {cs} | {data.get('strategy','N/A')} |")
    
    with open(REPORTS_DIR / "rescue_17_firecrawl_report.md", "w") as f:
        f.write("\n".join(lines))
    
    print(f"\n  📄 Report: {REPORTS_DIR / 'rescue_17_firecrawl_report.md'}", flush=True)


if __name__ == "__main__":
    main()
