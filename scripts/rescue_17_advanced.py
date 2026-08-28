"""
Advanced Rescue Script for the 17 Remaining Failed Retailers.
============================================================

Implements a multi-strategy cascade using ALL documented Bright Data capabilities:

Strategy 1: Web Unlocker Direct API (sync /request) with render=true (browser JS rendering)
Strategy 2: Web Unlocker Direct API with data_format=markdown
Strategy 3: Web Unlocker Native Proxy Interface (port 44445) with country geolocation
Strategy 4: SERP API Discovery — Google search for "site:domain laptop" to find real product URLs
Strategy 5: Web Unlocker with mobile user-agent (-ua-mobile)
Strategy 6: Firecrawl Rescue fallback

Each strategy is tried in order. On first genuine laptop SKU found, we persist evidence and move on.
"""
import os
import re
import sys
import json
import time
import asyncio
import hashlib
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime, timezone

import httpx

# Ensure project root is on sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import app.env
from app.classification.laptop_classifier import LaptopClassifier, ClassificationResult, ProductClass

# ─── Configuration ───────────────────────────────────────────────────────
API_KEY = os.getenv("BRIGHTDATA_API_KEY", "")
CUSTOMER_ID = os.getenv("BRIGHTDATA_CUSTOMER_ID", "")
ZONE = os.getenv("BRIGHTDATA_ZONE", "web_unlocker1")
PASSWORD = os.getenv("BRIGHTDATA_PASSWORD", "")
FIRECRAWL_KEY = os.getenv("FIRECRAWL_API_KEY", "")

DIRECT_API_URL = "https://api.brightdata.com/request"
PROXY_HOST = "brd.superproxy.io"
PROXY_PORT = 44445

EVIDENCE_BASE = PROJECT_ROOT / "evidence" / "brightdata"
REPORTS_DIR = PROJECT_ROOT / "reports"

# ─── 17 Remaining Failed Targets ────────────────────────────────────────
RESCUE_TARGETS = [
    {
        "target_id": "bestbuy-ca",
        "retailer": "Best Buy",
        "country": "Canada",
        "iso": "ca",
        "domain": "bestbuy.ca",
        "candidates": [
            "https://www.bestbuy.ca/en-ca/product/asus-vivobook-15-15-6-laptop-quiet-blue-intel-core-i5-1235u-512gb-ssd-16gb-ram-windows-11/17158742",
            "https://www.bestbuy.ca/en-ca/product/hp-15-6-laptop-natural-silver-intel-core-i3-1215u-512gb-ssd-8gb-ram-windows-11/17083884",
            "https://www.bestbuy.ca/en-ca/product/lenovo-ideapad-slim-3-15-6-laptop-arctic-grey-amd-ryzen-5-7520u-512gb-ssd-8gb-ram/17158741"
        ],
        "serp_query": "site:bestbuy.ca laptop notebook buy"
    },
    {
        "target_id": "boulanger-fr",
        "retailer": "Boulanger",
        "country": "France",
        "iso": "fr",
        "domain": "boulanger.com",
        "candidates": [
            "https://www.boulanger.com/ref/1199341",
            "https://www.boulanger.com/ref/1203456",
            "https://www.boulanger.com/ref/1188567"
        ],
        "serp_query": "site:boulanger.com ordinateur portable laptop"
    },
    {
        "target_id": "coupang-kr",
        "retailer": "Coupang",
        "country": "South Korea",
        "iso": "kr",
        "domain": "coupang.com",
        "candidates": [
            "https://www.coupang.com/vp/products/7581273934",
            "https://www.coupang.com/vp/products/7335866794",
            "https://www.coupang.com/vp/products/7936491632"
        ],
        "serp_query": "site:coupang.com 노트북 laptop"
    },
    {
        "target_id": "elkjop-dk",
        "retailer": "Elkjøp",
        "country": "Denmark",
        "iso": "dk",
        "domain": "elgiganten.dk",
        "candidates": [
            "https://www.elgiganten.dk/product/computer-kontor/computere/baerbar-computer/lenovo-ideapad-slim-3-158-baerbar-computer-gra/605928",
            "https://www.elgiganten.dk/product/computer-kontor/computere/baerbar-computer/hp-laptop-15-fd0019no-baerbar-computer-156/620731"
        ],
        "serp_query": "site:elgiganten.dk bærbar computer laptop"
    },
    {
        "target_id": "elkjop-no",
        "retailer": "Elkjøp",
        "country": "Norway",
        "iso": "no",
        "domain": "elkjop.no",
        "candidates": [
            "https://www.elkjop.no/product/pc-data-og-kontor/datamaskiner/barbar-pc/lenovo-ideapad-slim-3-158-barbar-pc-gra/605928",
            "https://www.elkjop.no/product/pc-data-og-kontor/datamaskiner/barbar-pc/hp-laptop-15-fd0019no-barbar-pc-156/620731"
        ],
        "serp_query": "site:elkjop.no bærbar PC laptop"
    },
    {
        "target_id": "euronics-it",
        "retailer": "Euronics",
        "country": "Italy",
        "iso": "it",
        "domain": "euronics.it",
        "candidates": [
            "https://www.euronics.it/informatica/computer/notebook/lenovo-ideapad-slim-3-15iau7-82rk009fix-arctic-grey/232001429.html",
            "https://www.euronics.it/informatica/computer/notebook/hp-15s-fq5090nl-15-6-i5-1235u-8-512-w11h/232004123.html"
        ],
        "serp_query": "site:euronics.it notebook portatile laptop"
    },
    {
        "target_id": "expert-de",
        "retailer": "Expert",
        "country": "Germany",
        "iso": "de",
        "domain": "expert.de",
        "candidates": [
            "https://www.expert.de/shop/unsere-produkte/computer-zubehor/notebooks/17044033544-ideapad-slim-3-15iah8-abys-blue-notebook.html",
            "https://www.expert.de/shop/unsere-produkte/computer-zubehor/notebooks/17000123456-hp-15s-notebook.html"
        ],
        "serp_query": "site:expert.de notebook laptop kaufen"
    },
    {
        "target_id": "fnac-fr",
        "retailer": "Fnac",
        "country": "France",
        "iso": "fr",
        "domain": "fnac.com",
        "candidates": [
            "https://www.fnac.com/PC-Portable-Lenovo-IdeaPad-Slim-3-15IAU7-15-6-Intel-Core-i5-16-Go-RAM-512-Go-SSD-Gris-arctique/a18118042/w-4",
            "https://www.fnac.com/PC-Portable-HP-15s-fq5071nf-15-6-Intel-Core-i5-16-Go-RAM-512-Go-SSD/a18234567/w-4"
        ],
        "serp_query": "site:fnac.com PC portable laptop ordinateur"
    },
    {
        "target_id": "gmarket-kr",
        "retailer": "Gmarket",
        "country": "South Korea",
        "iso": "kr",
        "domain": "gmarket.co.kr",
        "candidates": [
            "https://item.gmarket.co.kr/Item?goodscode=3148154181",
            "https://item.gmarket.co.kr/Item?goodscode=3267890123"
        ],
        "serp_query": "site:gmarket.co.kr 노트북 laptop notebook"
    },
    {
        "target_id": "jd-cn",
        "retailer": "JD",
        "country": "China",
        "iso": "cn",
        "domain": "jd.com",
        "candidates": [
            "https://item.jd.com/100058349272.html",
            "https://item.jd.com/100056789123.html"
        ],
        "serp_query": "site:jd.com 笔记本电脑 laptop"
    },
    {
        "target_id": "magazineluiza-br",
        "retailer": "Magazine Luiza",
        "country": "Brazil",
        "iso": "br",
        "domain": "magazineluiza.com.br",
        "candidates": [
            "https://www.magazineluiza.com.br/notebook-lenovo-ideapad-1-15iau7-intel-core-i5-8gb-256gb-ssd-156-linux/p/237936100/in/note/",
            "https://www.magazineluiza.com.br/notebook-samsung-book-intel-core-i5-8gb-256gb-ssd-tela-156-windows-11/p/237456789/in/note/"
        ],
        "serp_query": "site:magazineluiza.com.br notebook laptop"
    },
    {
        "target_id": "mediamarkt-de",
        "retailer": "MediaMarkt",
        "country": "Germany",
        "iso": "de",
        "domain": "mediamarkt.de",
        "candidates": [
            "https://www.mediamarkt.de/de/product/_lenovo-ideapad-slim-3-notebook-mit-156-zoll-display-intelr-coretm-i5-prozessor-16-gb-ram-512-gb-ssd-intel-iris-xe-grafik-arctic-grey-2882736.html",
            "https://www.mediamarkt.de/de/product/_hp-15s-notebook-mit-156-zoll-display-2889123.html"
        ],
        "serp_query": "site:mediamarkt.de notebook laptop kaufen"
    },
    {
        "target_id": "mercadolibre-cl",
        "retailer": "MercadoLibre",
        "country": "Chile",
        "iso": "cl",
        "domain": "mercadolibre.cl",
        "candidates": [
            "https://articulo.mercadolibre.cl/MLC-1456123894-notebook-lenovo-ideapad-1-15-fhd-ryzen-3-7320u-8gb-256gb-ssd-_JM",
            "https://articulo.mercadolibre.cl/MLC-1567890123-notebook-hp-15-intel-core-i5-8gb-256gb-ssd-_JM"
        ],
        "serp_query": "site:mercadolibre.cl notebook laptop"
    },
    {
        "target_id": "monsternotebook-tr",
        "retailer": "Monster Notebook",
        "country": "Turkey",
        "iso": "tr",
        "domain": "monsternotebook.com.tr",
        "candidates": [
            "https://www.monsternotebook.com.tr/abra/monster-abra-a5-v20-3-2/",
            "https://www.monsternotebook.com.tr/tulpar/monster-tulpar-t7-v20-5/"
        ],
        "serp_query": "site:monsternotebook.com.tr laptop notebook"
    },
    {
        "target_id": "reliancedigital-in",
        "retailer": "Reliance Digital",
        "country": "India",
        "iso": "in",
        "domain": "reliancedigital.in",
        "candidates": [
            "https://www.reliancedigital.in/hp-15s-fq5007tu-laptop-12th-gen-intel-core-i3-1215u-8gb-512gb-ssd-intel-uhd-graphics-windows-11-home-fhd-39-6-cm-15-6-inch-/p/493177751",
            "https://www.reliancedigital.in/lenovo-ideapad-slim-3-laptop-amd-ryzen-5-7520u-8gb-512gb-ssd/p/493456789"
        ],
        "serp_query": "site:reliancedigital.in laptop notebook buy"
    },
    {
        "target_id": "tmall-cn",
        "retailer": "Tmall",
        "country": "China",
        "iso": "cn",
        "domain": "tmall.com",
        "candidates": [
            "https://detail.tmall.com/item.htm?id=723489123812",
            "https://detail.tmall.com/item.htm?id=745678901234"
        ],
        "serp_query": "site:tmall.com 笔记本电脑 laptop"
    },
    {
        "target_id": "yodobashi-jp",
        "retailer": "Yodobashi",
        "country": "Japan",
        "iso": "jp",
        "domain": "yodobashi.com",
        "candidates": [
            "https://www.yodobashi.com/product/100000001008432194/",
            "https://www.yodobashi.com/product/100000001007892345/"
        ],
        "serp_query": "site:yodobashi.com ノートパソコン laptop"
    }
]


def extract_title_from_html(html: str, url: str) -> str:
    """Extract the most likely product title from HTML."""
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    
    # Try standard product title selectors
    for sel in [
        "#productTitle", ".product-title", ".pdp-title", 
        "[data-testid='product-title']", ".product-name",
        ".product_title", "h1.title", "h1.name",
        "[itemprop='name']", ".pdp__title",
        "h1"
    ]:
        el = soup.select_one(sel)
        if el:
            txt = el.get_text(strip=True)
            if len(txt) > 5 and len(txt) < 500:
                return txt
    
    # Fallback to <title> tag
    title_tag = soup.select_one("title")
    if title_tag:
        return title_tag.get_text(strip=True)
    
    return ""


def is_laptop_content(html: str, url: str) -> Tuple[bool, ClassificationResult]:
    """Check if HTML contains a genuine laptop product."""
    title = extract_title_from_html(html, url)
    cls_res = LaptopClassifier.classify(title=title, html=html, url=url)
    return cls_res.is_genuine_laptop, cls_res


def save_evidence(target_id: str, result: Dict[str, Any], html_snippet: str = "") -> None:
    """Save evidence to the evidence directory."""
    ev_dir = EVIDENCE_BASE / target_id
    ev_dir.mkdir(parents=True, exist_ok=True)
    
    # Save evidence summary
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
    
    # Save HTML snippet (first 50KB)
    if html_snippet:
        with open(ev_dir / "product_page.html", "w", errors="replace") as f:
            f.write(html_snippet[:50000])
    
    print(f"  📁 Evidence saved: {ev_dir}/evidence_summary.json")


# ─── Strategy Implementations ───────────────────────────────────────────

async def strategy_direct_api_render(url: str, iso: str, timeout: float = 45.0) -> Optional[str]:
    """
    Strategy 1: Web Unlocker Direct API (/request) with render=true.
    Forces JavaScript rendering using a real browser on the Bright Data side.
    This is the most powerful unblocking strategy per the documentation.
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "zone": ZONE,
        "url": url,
        "format": "raw",
        "render": "true",
        "country": iso.lower()
    }
    
    async with httpx.AsyncClient(timeout=timeout + 10, verify=False) as client:
        resp = await client.post(DIRECT_API_URL, headers=headers, json=payload, timeout=timeout)
        if resp.status_code == 200 and len(resp.text) > 500:
            return resp.text
    return None


async def strategy_direct_api_markdown(url: str, iso: str, timeout: float = 40.0) -> Optional[str]:
    """
    Strategy 2: Web Unlocker Direct API with data_format=markdown.
    Returns clean markdown, which can still be classified.
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "zone": ZONE,
        "url": url,
        "format": "raw",
        "data_format": "markdown",
        "country": iso.lower()
    }
    
    async with httpx.AsyncClient(timeout=timeout + 10, verify=False) as client:
        resp = await client.post(DIRECT_API_URL, headers=headers, json=payload, timeout=timeout)
        if resp.status_code == 200 and len(resp.text) > 200:
            return resp.text
    return None


async def strategy_proxy_access(url: str, iso: str, timeout: float = 35.0) -> Optional[str]:
    """
    Strategy 3: Native proxy-based access through brd.superproxy.io:44445.
    Uses the proxy interface with country geolocation.
    """
    if not PASSWORD:
        return None
    
    proxy_user = f"brd-customer-{CUSTOMER_ID}-zone-{ZONE}-country-{iso.lower()}"
    proxy_url = f"http://{proxy_user}:{PASSWORD}@{PROXY_HOST}:{PROXY_PORT}"
    
    async with httpx.AsyncClient(
        proxy=proxy_url,
        timeout=timeout,
        verify=False,
        follow_redirects=True
    ) as client:
        resp = await client.get(url)
        if resp.status_code == 200 and len(resp.text) > 500:
            return resp.text
    return None


async def strategy_serp_discovery(domain: str, query: str, iso: str, timeout: float = 30.0) -> List[str]:
    """
    Strategy 4: Use SERP API to discover real product URLs via Google search.
    Returns a list of discovered product URLs.
    """
    # Use the direct API with a Google search URL
    google_url = f"https://www.google.com/search?q={query.replace(' ', '+')}&gl={iso.lower()}&num=10"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "zone": ZONE,
        "url": google_url,
        "format": "raw",
        "country": iso.lower()
    }
    
    discovered_urls = []
    
    async with httpx.AsyncClient(timeout=timeout + 10, verify=False) as client:
        resp = await client.post(DIRECT_API_URL, headers=headers, json=payload, timeout=timeout)
        if resp.status_code == 200 and len(resp.text) > 500:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(resp.text, "html.parser")
            
            # Extract URLs from Google search results
            for a_tag in soup.find_all("a", href=True):
                href = a_tag["href"]
                # Google wraps URLs in /url?q=...
                if "/url?q=" in href:
                    actual_url = href.split("/url?q=")[1].split("&")[0]
                    if domain in actual_url and "search" not in actual_url.lower():
                        discovered_urls.append(actual_url)
                elif domain in href and href.startswith("http"):
                    if "search" not in href.lower() and "category" not in href.lower():
                        discovered_urls.append(href)
    
    return list(dict.fromkeys(discovered_urls))[:5]  # Unique, max 5


async def strategy_mobile_ua(url: str, iso: str, timeout: float = 35.0) -> Optional[str]:
    """
    Strategy 5: Web Unlocker with mobile user-agent.
    Some sites serve lighter/less-blocked mobile versions.
    """
    if not PASSWORD:
        return None
    
    proxy_user = f"brd-customer-{CUSTOMER_ID}-zone-{ZONE}-country-{iso.lower()}-ua-mobile"
    proxy_url = f"http://{proxy_user}:{PASSWORD}@{PROXY_HOST}:{PROXY_PORT}"
    
    async with httpx.AsyncClient(
        proxy=proxy_url,
        timeout=timeout,
        verify=False,
        follow_redirects=True
    ) as client:
        resp = await client.get(url)
        if resp.status_code == 200 and len(resp.text) > 500:
            return resp.text
    return None


async def strategy_firecrawl(url: str, timeout: float = 30.0) -> Optional[str]:
    """
    Strategy 6: Firecrawl rescue fallback.
    """
    if not FIRECRAWL_KEY:
        return None
    
    headers = {
        "Authorization": f"Bearer {FIRECRAWL_KEY}",
        "Content-Type": "application/json"
    }
    payload = {"url": url, "formats": ["html", "markdown"]}
    
    async with httpx.AsyncClient(timeout=timeout + 5, verify=False) as client:
        resp = await client.post("https://api.firecrawl.dev/v1/scrape", json=payload, headers=headers)
        if resp.status_code == 200:
            data = resp.json().get("data", {})
            html = data.get("html") or data.get("markdown") or ""
            if len(html) > 200:
                return html
    return None


async def strategy_direct_api_no_render(url: str, iso: str, timeout: float = 30.0) -> Optional[str]:
    """
    Strategy 0: Web Unlocker Direct API (/request) WITHOUT render (plain HTTP).
    Cheapest and fastest. Try first.
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "zone": ZONE,
        "url": url,
        "format": "raw",
        "country": iso.lower()
    }
    
    async with httpx.AsyncClient(timeout=timeout + 10, verify=False) as client:
        resp = await client.post(DIRECT_API_URL, headers=headers, json=payload, timeout=timeout)
        if resp.status_code == 200 and len(resp.text) > 500:
            return resp.text
    return None


# ─── Main Orchestration ─────────────────────────────────────────────────

async def rescue_single_target(target: Dict[str, Any]) -> Dict[str, Any]:
    """Run all strategies on a single target until success or exhaustion."""
    t_id = target["target_id"]
    retailer = target["retailer"]
    country = target["country"]
    iso = target["iso"]
    domain = target["domain"]
    candidates = target["candidates"]
    serp_query = target.get("serp_query", f"site:{domain} laptop")
    
    print(f"\n{'='*60}")
    print(f"🎯 Rescuing: {retailer} ({country}) [{t_id}]")
    print(f"   Domain: {domain} | ISO: {iso}")
    print(f"   Candidates: {len(candidates)} URLs")
    print(f"{'='*60}")
    
    strategies = [
        ("Direct API (no render)", strategy_direct_api_no_render, "BRIGHTDATA_WEB_UNLOCKER"),
        ("Direct API (render=true)", strategy_direct_api_render, "BRIGHTDATA_WEB_UNLOCKER_RENDER"),
        ("Direct API (markdown)", strategy_direct_api_markdown, "BRIGHTDATA_WEB_UNLOCKER_MARKDOWN"),
        ("Proxy Access (country)", strategy_proxy_access, "BRIGHTDATA_PROXY_ACCESS"),
        ("Mobile UA", strategy_mobile_ua, "BRIGHTDATA_MOBILE_UA"),
        ("Firecrawl Rescue", strategy_firecrawl, "FIRECRAWL_RESCUE"),
    ]
    
    # Phase 1: Try each strategy with candidate URLs
    for strat_name, strat_fn, strat_code in strategies:
        for url in candidates:
            try:
                print(f"  🔄 [{strat_name}] Trying: {url[:80]}...")
                
                if strat_fn == strategy_firecrawl:
                    html = await strat_fn(url)
                else:
                    html = await strat_fn(url, iso)
                
                if html:
                    is_laptop, cls_res = is_laptop_content(html, url)
                    title = cls_res.extracted_specs.get("title") or extract_title_from_html(html, url)
                    
                    if is_laptop:
                        print(f"  ✅ [SUCCESS via {strat_name}] {retailer} ({country})")
                        print(f"     Title: {title[:80]}")
                        result = {
                            "target_id": t_id,
                            "retailer": retailer,
                            "country": country,
                            "domain": domain,
                            "can_scrape": "YES",
                            "strategy": strat_code,
                            "url": url,
                            "title": title,
                            "brand": cls_res.detected_brand or retailer,
                            "specs": cls_res.extracted_specs,
                            "method": strat_name,
                            "confidence": cls_res.confidence_score
                        }
                        save_evidence(t_id, result, html)
                        return result
                    else:
                        # Got content but not classified as laptop — log why
                        print(f"     ⚠️  Content received ({len(html)} bytes) but not a laptop. "
                              f"Class: {cls_res.product_class}, Reason: {cls_res.rejection_reason or 'N/A'}")
                else:
                    print(f"     ❌ No content returned.")
            except Exception as e:
                print(f"     ❌ Error: {str(e)[:80]}")
    
    # Phase 2: SERP Discovery — find new product URLs via Google
    print(f"  🔍 [SERP Discovery] Searching: {serp_query[:60]}...")
    try:
        discovered = await strategy_serp_discovery(domain, serp_query, iso)
        if discovered:
            print(f"     Found {len(discovered)} URLs via SERP:")
            for d_url in discovered:
                print(f"       → {d_url[:80]}")
            
            # Try discovered URLs with the best strategies
            for d_url in discovered:
                for strat_name, strat_fn, strat_code in strategies[:3]:  # Top 3 strategies only
                    try:
                        print(f"  🔄 [{strat_name}] SERP-discovered: {d_url[:80]}...")
                        
                        if strat_fn == strategy_firecrawl:
                            html = await strat_fn(d_url)
                        else:
                            html = await strat_fn(d_url, iso)
                        
                        if html:
                            is_laptop, cls_res = is_laptop_content(html, d_url)
                            title = cls_res.extracted_specs.get("title") or extract_title_from_html(html, d_url)
                            
                            if is_laptop:
                                print(f"  ✅ [SUCCESS via SERP+{strat_name}] {retailer} ({country})")
                                print(f"     Title: {title[:80]}")
                                result = {
                                    "target_id": t_id,
                                    "retailer": retailer,
                                    "country": country,
                                    "domain": domain,
                                    "can_scrape": "YES",
                                    "strategy": f"SERP_DISCOVERY+{strat_code}",
                                    "url": d_url,
                                    "title": title,
                                    "brand": cls_res.detected_brand or retailer,
                                    "specs": cls_res.extracted_specs,
                                    "method": f"SERP Discovery + {strat_name}",
                                    "confidence": cls_res.confidence_score
                                }
                                save_evidence(t_id, result, html)
                                return result
                    except Exception as e:
                        print(f"     ❌ Error: {str(e)[:80]}")
        else:
            print(f"     ⚠️  No URLs discovered via SERP.")
    except Exception as e:
        print(f"     ❌ SERP Error: {str(e)[:80]}")
    
    # All strategies exhausted
    print(f"  ❌ [FAILED] {retailer} ({country}) — all strategies exhausted.")
    result = {
        "target_id": t_id,
        "retailer": retailer,
        "country": country,
        "domain": domain,
        "can_scrape": "NO",
        "strategy": "NONE",
        "url": None,
        "title": None,
        "brand": None,
        "specs": {},
        "method": "All strategies exhausted",
        "failure_reason": "Anti-bot barriers survived all 6 strategies + SERP discovery."
    }
    save_evidence(t_id, result)
    return result


async def main():
    """Main orchestrator for the 17-target rescue."""
    print("=" * 70)
    print("  BRIGHT DATA ADVANCED RESCUE — 17 REMAINING TARGETS")
    print(f"  API Key: {'SET' if API_KEY else 'MISSING'}")
    print(f"  Zone: {ZONE}")
    print(f"  Firecrawl: {'SET' if FIRECRAWL_KEY else 'MISSING'}")
    print(f"  Proxy Password: {'SET' if PASSWORD else 'MISSING'}")
    print(f"  Timestamp: {datetime.now(timezone.utc).isoformat()}")
    print("=" * 70)
    
    if not API_KEY:
        print("❌ FATAL: BRIGHTDATA_API_KEY is not set. Aborting.")
        return
    
    results = []
    sem = asyncio.Semaphore(2)  # Conservative concurrency to avoid rate limiting
    
    async def _wrap(target):
        async with sem:
            return await rescue_single_target(target)
    
    # Process targets sequentially for better logging readability
    for target in RESCUE_TARGETS:
        result = await rescue_single_target(target)
        results.append(result)
        # Brief pause between targets to avoid rate limiting
        await asyncio.sleep(2.0)
    
    # ─── Generate Report ────────────────────────────────────────────────
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    
    rescued = [r for r in results if r["can_scrape"] == "YES"]
    failed = [r for r in results if r["can_scrape"] != "YES"]
    
    print("\n" + "=" * 70)
    print(f"  RESCUE COMPLETE")
    print(f"  Rescued: {len(rescued)} / {len(RESCUE_TARGETS)}")
    print(f"  Still Failed: {len(failed)} / {len(RESCUE_TARGETS)}")
    print("=" * 70)
    
    if rescued:
        print("\n  ✅ NEWLY RESCUED:")
        for r in rescued:
            print(f"    {r['retailer']:25s} ({r['country']:15s}) via {r['strategy']}")
            print(f"      → {r.get('title', 'N/A')[:70]}")
    
    if failed:
        print("\n  ❌ STILL FAILED:")
        for r in failed:
            print(f"    {r['retailer']:25s} ({r['country']:15s}) — {r.get('failure_reason', 'Unknown')[:60]}")
    
    # Save raw results
    with open(REPORTS_DIR / "rescue_17_results.json", "w") as f:
        json.dump(results, f, indent=2, default=str)
    
    # Calculate overall benchmark
    all_evidence = {}
    for d in sorted(os.listdir(str(EVIDENCE_BASE))):
        fp = EVIDENCE_BASE / d / "evidence_summary.json"
        if fp.exists():
            with open(fp) as f:
                data = json.load(f)
                all_evidence[d] = data
    
    total_success = sum(1 for v in all_evidence.values() if v.get("can_scrape") == "YES")
    total = len(all_evidence)
    
    print(f"\n  📊 OVERALL BENCHMARK: {total_success} / {total} ({100*total_success/total:.1f}%)")
    
    # Save markdown report
    report_lines = [
        "# Bright Data 52-Retailer Laptop Benchmark — Rescue Phase",
        f"\n**Date**: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        f"\n**Overall Score**: {total_success} / {total} ({100*total_success/total:.1f}%)",
        f"\n**This Phase**: {len(rescued)} / {len(RESCUE_TARGETS)} newly rescued",
        "\n## Newly Rescued Retailers\n",
    ]
    
    if rescued:
        report_lines.append("| Retailer | Country | Strategy | Title |")
        report_lines.append("|----------|---------|----------|-------|")
        for r in rescued:
            title = (r.get("title") or "N/A")[:60]
            report_lines.append(f"| {r['retailer']} | {r['country']} | {r['strategy']} | {title} |")
    else:
        report_lines.append("*No new rescues in this phase.*")
    
    report_lines.append("\n## Still Failed\n")
    if failed:
        report_lines.append("| Retailer | Country | Reason |")
        report_lines.append("|----------|---------|--------|")
        for r in failed:
            reason = (r.get("failure_reason") or "Unknown")[:60]
            report_lines.append(f"| {r['retailer']} | {r['country']} | {reason} |")
    
    report_lines.append("\n## Full Benchmark Status\n")
    report_lines.append("| # | Target ID | Retailer | Country | Status | Strategy |")
    report_lines.append("|---|-----------|----------|---------|--------|----------|")
    for i, (tid, data) in enumerate(sorted(all_evidence.items()), 1):
        cs = "✅" if data.get("can_scrape") == "YES" else "❌"
        strat = data.get("strategy", "N/A")
        ret = data.get("retailer", tid)
        cnt = data.get("country", "?")
        report_lines.append(f"| {i} | {tid} | {ret} | {cnt} | {cs} | {strat} |")
    
    with open(REPORTS_DIR / "rescue_17_report.md", "w") as f:
        f.write("\n".join(report_lines))
    
    print(f"\n  📄 Report saved: {REPORTS_DIR / 'rescue_17_report.md'}")
    print(f"  📄 Results saved: {REPORTS_DIR / 'rescue_17_results.json'}")


if __name__ == "__main__":
    asyncio.run(main())
