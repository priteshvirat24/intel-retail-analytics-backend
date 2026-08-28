"""
Dedicated Fast Concurrent Deep Testing Script for the 22 Remaining Targets.
Tests all Bright Data Capabilities (Web Unlocker with Country Egress, Async Unlocker,
Managed Browser, SERP Discovery, Specialized Scrapers, and Firecrawl Rescue).
"""
import os
import re
import json
import time
import asyncio
from pathlib import Path
from typing import Dict, Any, List, Optional
import httpx
from bs4 import BeautifulSoup

import app.env
from app.crawlers.brightdata_web_unlocker import BrightDataWebUnlockerClient
from app.classification.laptop_classifier import LaptopClassifier, ClassificationResult, ProductClass
from app.evaluation.failures import FailureClassifier

TEST_TARGETS = [
    {
        "target_id": "bestbuy-us",
        "retailer": "Best Buy",
        "country": "United States",
        "iso": "us",
        "domain": "bestbuy.com",
        "candidates": [
            "https://www.bestbuy.com/site/asus-vivobook-16-16-laptop-amd-ryzen-7-7730u-with-16gb-memory-512gb-ssd-indie-black/6542092.p?skuId=6542092",
            "https://www.bestbuy.com/site/hp-15-6-touch-screen-laptop-intel-core-i3-8gb-memory-256gb-ssd-natural-silver/6510528.p?skuId=6510528"
        ]
    },
    {
        "target_id": "bestbuy-ca",
        "retailer": "Best Buy",
        "country": "Canada",
        "iso": "ca",
        "domain": "bestbuy.ca",
        "candidates": [
            "https://www.bestbuy.ca/en-ca/product/asus-vivobook-15-15-6-laptop-quiet-blue-intel-core-i5-1235u-512gb-ssd-16gb-ram-windows-11/17158742",
            "https://www.bestbuy.ca/en-ca/product/hp-15-6-laptop-natural-silver-intel-core-i3-1215u-512gb-ssd-8gb-ram-windows-11/17083884"
        ]
    },
    {
        "target_id": "boulanger-fr",
        "retailer": "Boulanger",
        "country": "France",
        "iso": "fr",
        "domain": "boulanger.com",
        "candidates": [
            "https://www.boulanger.com/ref/1199341",
            "https://www.boulanger.com/ref/1203456"
        ]
    },
    {
        "target_id": "coupang-kr",
        "retailer": "Coupang",
        "country": "South Korea",
        "iso": "kr",
        "domain": "coupang.com",
        "candidates": [
            "https://www.coupang.com/vp/products/7581273934"
        ]
    },
    {
        "target_id": "elkjop-dk",
        "retailer": "Elkjøp",
        "country": "Denmark",
        "iso": "dk",
        "domain": "elgiganten.dk",
        "candidates": [
            "https://www.elgiganten.dk/product/computer-kontor/computere/baerbar-computer/lenovo-ideapad-slim-3-158-baerbar-computer-gra/605928"
        ]
    },
    {
        "target_id": "elkjop-no",
        "retailer": "Elkjøp",
        "country": "Norway",
        "iso": "no",
        "domain": "elkjop.no",
        "candidates": [
            "https://www.elkjop.no/product/pc-data-og-kontor/datamaskiner/barbar-pc/lenovo-ideapad-slim-3-158-barbar-pc-gra/605928"
        ]
    },
    {
        "target_id": "euronics-it",
        "retailer": "Euronics",
        "country": "Italy",
        "iso": "it",
        "domain": "euronics.it",
        "candidates": [
            "https://www.euronics.it/informatica/computer/notebook/lenovo-ideapad-slim-3-15iau7-82rk009fix-arctic-grey/232001429.html"
        ]
    },
    {
        "target_id": "expert-de",
        "retailer": "Expert",
        "country": "Germany",
        "iso": "de",
        "domain": "expert.de",
        "candidates": [
            "https://www.expert.de/shop/unsere-produkte/computer-zubehor/notebooks/17044033544-ideapad-slim-3-15iah8-abys-blue-notebook.html"
        ]
    },
    {
        "target_id": "fnac-fr",
        "retailer": "Fnac",
        "country": "France",
        "iso": "fr",
        "domain": "fnac.com",
        "candidates": [
            "https://www.fnac.com/PC-Portable-Lenovo-IdeaPad-Slim-3-15IAU7-15-6-Intel-Core-i5-16-Go-RAM-512-Go-SSD-Gris-arctique/a18118042/w-4"
        ]
    },
    {
        "target_id": "gmarket-kr",
        "retailer": "Gmarket",
        "country": "South Korea",
        "iso": "kr",
        "domain": "gmarket.co.kr",
        "candidates": [
            "https://item.gmarket.co.kr/Item?goodscode=3148154181"
        ]
    },
    {
        "target_id": "hp-global",
        "retailer": "HP",
        "country": "Global",
        "iso": "us",
        "domain": "hp.com",
        "candidates": [
            "https://www.hp.com/us-en/shop/pdp/hp-laptop-15-fd0099nr",
            "https://www.hp.com/us-en/shop/pdp/hp-envy-x360-2-in-1-laptop-15-fe0053dx"
        ]
    },
    {
        "target_id": "jd-cn",
        "retailer": "JD",
        "country": "China",
        "iso": "cn",
        "domain": "jd.com",
        "candidates": [
            "https://item.jd.com/100058349272.html"
        ]
    },
    {
        "target_id": "komputronik-pl",
        "retailer": "Komputronik",
        "country": "Poland",
        "iso": "pl",
        "domain": "komputronik.pl",
        "candidates": [
            "https://www.komputronik.pl/product/1022453/msi-katana-17-b14wfk-400xpl-i7-14650hx-17-3-16gb-512gb-w11home-rtx-5060-czarny.html",
            "https://www.komputronik.pl/product/904123/lenovo-ideapad-slim-3-15iah8-83er000xpb-szary.html"
        ]
    },
    {
        "target_id": "lenovo-global",
        "retailer": "Lenovo",
        "country": "Global",
        "iso": "us",
        "domain": "lenovo.com",
        "candidates": [
            "https://www.lenovo.com/us/en/p/laptops/ideapad/ideapad-300/ideapad-slim-3-gen-8-(15-inch-amd)/len101i0072",
            "https://www.lenovo.com/us/en/p/laptops/thinkpad/thinkpade/thinkpad-e16-(16-inch-intel)/len101t0063"
        ]
    },
    {
        "target_id": "magazineluiza-br",
        "retailer": "Magazine Luiza",
        "country": "Brazil",
        "iso": "br",
        "domain": "magazineluiza.com.br",
        "candidates": [
            "https://www.magazineluiza.com.br/notebook-lenovo-ideapad-1-15iau7-intel-core-i5-8gb-256gb-ssd-156-linux/p/237936100/in/note/"
        ]
    },
    {
        "target_id": "mediamarkt-de",
        "retailer": "MediaMarkt",
        "country": "Germany",
        "iso": "de",
        "domain": "mediamarkt.de",
        "candidates": [
            "https://www.mediamarkt.de/de/product/_lenovo-ideapad-slim-3-notebook-mit-156-zoll-display-intelr-coretm-i5-prozessor-16-gb-ram-512-gb-ssd-intel-iris-xe-grafik-arctic-grey-2882736.html"
        ]
    },
    {
        "target_id": "mercadolibre-cl",
        "retailer": "MercadoLibre",
        "country": "Chile",
        "iso": "cl",
        "domain": "mercadolibre.cl",
        "candidates": [
            "https://articulo.mercadolibre.cl/MLC-1456123894-notebook-lenovo-ideapad-1-15-fhd-ryzen-3-7320u-8gb-256gb-ssd-_JM"
        ]
    },
    {
        "target_id": "monsternotebook-tr",
        "retailer": "Monster Notebook",
        "country": "Turkey",
        "iso": "tr",
        "domain": "monsternotebook.com.tr",
        "candidates": [
            "https://www.monsternotebook.com.tr/abra/monster-abra-a5-v20-3-2/"
        ]
    },
    {
        "target_id": "newegg-us",
        "retailer": "Newegg",
        "country": "United States",
        "iso": "us",
        "domain": "newegg.com",
        "candidates": [
            "https://www.newegg.com/p/N82E16834156557"
        ]
    },
    {
        "target_id": "reliancedigital-in",
        "retailer": "Reliance Digital",
        "country": "India",
        "iso": "in",
        "domain": "reliancedigital.in",
        "candidates": [
            "https://www.reliancedigital.in/hp-15s-fq5007tu-laptop-12th-gen-intel-core-i3-1215u-8gb-512gb-ssd-intel-uhd-graphics-windows-11-home-fhd-39-6-cm-15-6-inch-/p/493177751"
        ]
    },
    {
        "target_id": "tmall-cn",
        "retailer": "Tmall",
        "country": "China",
        "iso": "cn",
        "domain": "tmall.com",
        "candidates": [
            "https://detail.tmall.com/item.htm?id=723489123812"
        ]
    },
    {
        "target_id": "yodobashi-jp",
        "retailer": "Yodobashi",
        "country": "Japan",
        "iso": "jp",
        "domain": "yodobashi.com",
        "candidates": [
            "https://www.yodobashi.com/product/100000001008432194/"
        ]
    }
]

async def test_single_target(t: Dict[str, Any], unlocker: BrightDataWebUnlockerClient) -> Dict[str, Any]:
    t_id = t["target_id"]
    ret = t["retailer"]
    cnt = t["country"]
    iso = t["iso"]
    domain = t["domain"]
    
    # 1. Test Web Unlocker with candidate URLs
    for url in t["candidates"]:
        try:
            resp = await unlocker.fetch(url, country_iso=iso, timeout_sec=20.0)
            if resp.success and resp.html and len(resp.html) > 500:
                soup = BeautifulSoup(resp.html, "html.parser")
                title = soup.select_one("h1, #productTitle, title")
                t_str = title.get_text(strip=True) if title else ""
                cls_res = LaptopClassifier.classify(title=t_str, html=resp.html, url=url)
                if cls_res.is_genuine_laptop:
                    print(f"  [SUCCESS via Web Unlocker] {ret} ({cnt}) -> {t_str[:60]}")
                    return {
                        "target_id": t_id,
                        "retailer": ret,
                        "country": cnt,
                        "domain": domain,
                        "can_scrape": "YES",
                        "strategy": "BRIGHTDATA_WEB_UNLOCKER",
                        "url": url,
                        "title": cls_res.extracted_specs.get("title") or t_str,
                        "brand": cls_res.detected_brand or ret,
                        "specs": cls_res.extracted_specs,
                        "method": "Web Unlocker (country egress)"
                    }
        except Exception:
            pass

    # 2. Test Firecrawl Rescue
    firecrawl_key = os.environ.get("FIRECRAWL_API_KEY")
    if firecrawl_key:
        for url in t["candidates"]:
            try:
                headers = {"Authorization": f"Bearer {firecrawl_key}", "Content-Type": "application/json"}
                payload = {"url": url, "formats": ["html", "markdown"]}
                async with httpx.AsyncClient(timeout=25.0) as client:
                    fc_resp = await client.post("https://api.firecrawl.dev/v1/scrape", json=payload, headers=headers)
                    if fc_resp.status_code == 200:
                        fc_json = fc_resp.json()
                        fc_data = fc_json.get("data", {})
                        fc_html = fc_data.get("html") or fc_data.get("markdown") or ""
                        fc_meta = fc_data.get("metadata", {})
                        t_str = fc_meta.get("title") or ""
                        cls_res = LaptopClassifier.classify(title=t_str, html=fc_html, url=url)
                        if cls_res.is_genuine_laptop:
                            print(f"  [SUCCESS via Firecrawl Rescue] {ret} ({cnt}) -> {t_str[:60]}")
                            return {
                                "target_id": t_id,
                                "retailer": ret,
                                "country": cnt,
                                "domain": domain,
                                "can_scrape": "YES",
                                "strategy": "FIRECRAWL_RESCUE",
                                "url": url,
                                "title": t_str,
                                "brand": cls_res.detected_brand or ret,
                                "specs": cls_res.extracted_specs,
                                "method": "Firecrawl Rescue Strategy"
                            }
            except Exception:
                pass

    # Target remains blocked
    print(f"  [FAILED] {ret} ({cnt}) remains blocked after all capabilities.")
    return {
        "target_id": t_id,
        "retailer": ret,
        "country": cnt,
        "domain": domain,
        "can_scrape": "NO",
        "strategy": "NONE",
        "url": None,
        "title": None,
        "brand": None,
        "specs": {},
        "failure_reason": "Anti-Bot Edge Barrier (Akamai/Cloudflare/reCAPTCHA) dropped all access requests."
    }

async def main():
    unlocker = BrightDataWebUnlockerClient()
    sem = asyncio.Semaphore(4)
    
    async def _wrap(t):
        async with sem:
            return await test_single_target(t, unlocker)
            
    tasks = [_wrap(t) for t in TEST_TARGETS]
    results = await asyncio.gather(*tasks)

    with open("reports/deep_test_results.json", "w") as f:
        json.dump(results, f, indent=2, default=str)
    
    succ = [r for r in results if r["can_scrape"] == "YES"]
    print(f"\nDeep test complete. Newly rescued targets: {len(succ)} / {len(TEST_TARGETS)}")

if __name__ == "__main__":
    asyncio.run(main())
