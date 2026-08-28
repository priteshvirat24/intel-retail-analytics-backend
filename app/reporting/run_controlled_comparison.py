import asyncio
import time
import json
import os
import statistics
from app.crawlers.http import HttpCrawler
from app.crawlers.playwright import PlaywrightCrawler
from app.models.retailer import RetailerTargetConfig
from app.extraction.engine import ProductExtractionEngine
from app.extraction.template import ProductTemplateIdentifier
from app.retailers.registry import RetailerAdapterRegistry
from app.models.failure import CrawlStage, StageStatus

test_urls = [
    ("reliancedigital-in", "https://www.reliancedigital.in/product/sku_0012"),
    ("elkjop-no", "https://www.elkjop.no/product/sku_0001"),
    ("elkjop-se", "https://www.elgiganten.se/product/sku_0001"),
    ("elkjop-dk", "https://www.elgiganten.dk/product/sku_0001"),
    ("magazineluiza-br", "https://www.magazineluiza.com.br/product/sku_0001"),
    ("expert-de", "https://www.expert.de/product/sku_0018"),
    ("euronics-it", "https://www.euronics.it/product/sku_0010"),
    ("amazon-de", "https://www.amazon.de/dp/B09G91LXFP"),
    ("amazon-br", "https://www.amazon.com.br/dp/B09G9FPHY6"),
    ("boulanger-fr", "https://www.boulanger.com/product/sku_0001"),
]

async def run_comparison():
    out_dir = "reports/runs/run_20260823_phase3a_forensic"
    os.makedirs(out_dir, exist_ok=True)
    
    results = {
        "HTTP": {
            "attempts": 0,
            "successful_content": 0,
            "product_identification": 0,
            "extraction_success": 0,
            "validation_success": 0,
            "latencies": [],
            "bytes_received": 0,
            "browser_seconds": 0.0,
            "per_sku": []
        },
        "PLAYWRIGHT": {
            "attempts": 0,
            "successful_content": 0,
            "product_identification": 0,
            "extraction_success": 0,
            "validation_success": 0,
            "latencies": [],
            "bytes_received": 0,
            "browser_seconds": 0.0,
            "per_sku": []
        }
    }

    # 1. Run HTTP-only
    print("--- Running HTTP-Only Controlled Test (10 URLs) ---")
    for tid, url in test_urls:
        results["HTTP"]["attempts"] += 1
        ret_name = tid.split("-")[0]
        cfg = RetailerTargetConfig(
            target_id=tid,
            retailer=ret_name,
            brand_name=ret_name.title(),
            base_url=f"https://www.{ret_name}.com",
            country="Global",
            iso_country=tid.split("-")[1].upper(),
            domain=f"{ret_name}.com",
            locale="en-US",
            currency="USD",
            timezone="UTC",
            discovery_methods=[],
            category_seeds=[],
            sitemap_urls=[],
            seed_urls=[],
            max_concurrency=1,
            rate_limit=1.0
        )
        http_crawler = HttpCrawler(cfg)
        t0 = time.time()
        resp = await http_crawler.fetch(url)
        elapsed_ms = (time.time() - t0) * 1000
        results["HTTP"]["latencies"].append(elapsed_ms)
        bytes_len = len(resp.html.encode("utf-8")) if resp.html else 0
        results["HTTP"]["bytes_received"] += bytes_len
        
        is_content = resp.status_code == 200 and not resp.is_blocked and not resp.is_captcha and len((resp.html or "").strip()) >= 200
        if is_content:
            results["HTTP"]["successful_content"] += 1
        
        tmpl_id = ProductTemplateIdentifier.identify_template(resp.html) if is_content else "tmpl_empty_shell"
        is_identified = is_content and tmpl_id != "tmpl_empty_shell"
        if is_identified:
            results["HTTP"]["product_identification"] += 1
            
        adapter = RetailerAdapterRegistry.get_adapter(cfg)
        custom_res = None
        if adapter and resp.html:
            try:
                custom_res = adapter.extract_custom(resp.html, resp.final_url)
            except Exception:
                pass
                
        engine = ProductExtractionEngine(cfg)
        prod, _ = engine.extract_product(resp.html, resp.final_url, crawler_strategy="HTTP", custom_adapter_result=custom_res) if is_content else (None, "No content")
        is_extracted = bool(prod)
        if is_extracted:
            results["HTTP"]["extraction_success"] += 1
            
        is_validated = bool(prod and prod.validation and prod.validation.is_valid_sku)
        if is_validated:
            results["HTTP"]["validation_success"] += 1

        results["HTTP"]["per_sku"].append({
            "target_id": tid,
            "url": url,
            "status_code": resp.status_code,
            "bytes": bytes_len,
            "latency_ms": elapsed_ms,
            "content_ok": is_content,
            "identified": is_identified,
            "extracted": is_extracted,
            "validated": is_validated
        })
        print(f"  [HTTP] {tid:18s} -> Status: {resp.status_code:3d} | Bytes: {bytes_len:6d} | Content: {is_content} | Validated: {is_validated}")

    # 2. Run Playwright-Only
    print("\n--- Running Playwright-Only Controlled Test (10 URLs) ---")
    for tid, url in test_urls:
        results["PLAYWRIGHT"]["attempts"] += 1
        ret_name = tid.split("-")[0]
        cfg = RetailerTargetConfig(
            target_id=tid,
            retailer=ret_name,
            brand_name=ret_name.title(),
            base_url=f"https://www.{ret_name}.com",
            country="Global",
            iso_country=tid.split("-")[1].upper(),
            domain=f"{ret_name}.com",
            locale="en-US",
            currency="USD",
            timezone="UTC",
            discovery_methods=[],
            category_seeds=[],
            sitemap_urls=[],
            seed_urls=[],
            max_concurrency=1,
            rate_limit=1.0
        )
        pw_crawler = PlaywrightCrawler(cfg, headless=True)
        t0 = time.time()
        resp = await pw_crawler.fetch(url)
        browser_sec = time.time() - t0
        elapsed_ms = browser_sec * 1000
        results["PLAYWRIGHT"]["browser_seconds"] += browser_sec
        results["PLAYWRIGHT"]["latencies"].append(elapsed_ms)
        bytes_len = len(resp.html.encode("utf-8")) if resp.html else 0
        results["PLAYWRIGHT"]["bytes_received"] += bytes_len
        
        is_content = resp.status_code == 200 and not resp.is_blocked and not resp.is_captcha and len((resp.html or "").strip()) >= 200
        if is_content:
            results["PLAYWRIGHT"]["successful_content"] += 1
        
        tmpl_id = ProductTemplateIdentifier.identify_template(resp.html) if is_content else "tmpl_empty_shell"
        is_identified = is_content and tmpl_id != "tmpl_empty_shell"
        if is_identified:
            results["PLAYWRIGHT"]["product_identification"] += 1
            
        adapter = RetailerAdapterRegistry.get_adapter(cfg)
        custom_res = None
        if adapter and resp.html:
            try:
                custom_res = adapter.extract_custom(resp.html, resp.final_url)
            except Exception:
                pass
                
        engine = ProductExtractionEngine(cfg)
        prod, _ = engine.extract_product(resp.html, resp.final_url, crawler_strategy="PLAYWRIGHT", custom_adapter_result=custom_res) if is_content else (None, "No content")
        is_extracted = bool(prod)
        if is_extracted:
            results["PLAYWRIGHT"]["extraction_success"] += 1
            
        is_validated = bool(prod and prod.validation and prod.validation.is_valid_sku)
        if is_validated:
            results["PLAYWRIGHT"]["validation_success"] += 1

        results["PLAYWRIGHT"]["per_sku"].append({
            "target_id": tid,
            "url": url,
            "status_code": resp.status_code,
            "bytes": bytes_len,
            "latency_ms": elapsed_ms,
            "browser_seconds": browser_sec,
            "content_ok": is_content,
            "identified": is_identified,
            "extracted": is_extracted,
            "validated": is_validated
        })
        print(f"  [PLAYWRIGHT] {tid:18s} -> Status: {resp.status_code:3d} | Bytes: {bytes_len:6d} | Content: {is_content} | Validated: {is_validated}")

    # Summary metrics
    for strat in ["HTTP", "PLAYWRIGHT"]:
        lats = results[strat]["latencies"]
        if lats:
            results[strat]["average_latency_ms"] = float(statistics.mean(lats))
            sorted_lats = sorted(lats)
            p95_idx = int(len(sorted_lats) * 0.95)
            results[strat]["p95_latency_ms"] = float(sorted_lats[min(p95_idx, len(sorted_lats)-1)])
        else:
            results[strat]["average_latency_ms"] = 0.0
            results[strat]["p95_latency_ms"] = 0.0

    summary_file = os.path.join(out_dir, "controlled_comparison.json")
    with open(summary_file, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved controlled comparison to {summary_file}")

if __name__ == "__main__":
    asyncio.run(run_comparison())
