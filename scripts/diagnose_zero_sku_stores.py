"""
Detailed Bright Data Diagnostic for 0-SKU Storefronts.
Tests each site via:
1. Bright Data Web Unlocker (HTTP with country targeting)
2. Bright Data Scraping Browser (Playwright CDP over WebSocket)
Outputs exact HTTP status, HTML size, bot barrier, and error codes.
"""
import os
import json
import httpx
import asyncio
from playwright.async_api import async_playwright
from brightdata import BrightDataClient

# Load .env
env_vars = {}
for line in open(".env"):
    if "=" in line and not line.startswith("#"):
        k, v = line.strip().split("=", 1)
        env_vars[k] = v

api_key = env_vars.get("BRIGHTDATA_API_KEY")
customer = env_vars.get("BRIGHTDATA_CUSTOMER_ID")

TARGETS = [
    ("Officeworks AU", "https://www.officeworks.com.au/shop/officeworks/c/technology/laptops", "au"),
    ("Expert DE", "https://www.expert.de/shop/unsere-produkte/computer-zubehor/notebooks", "de"),
    ("MediaWorld IT", "https://www.mediaworld.it/it/category/notebook-100.html", "it"),
    ("JD.com CN", "https://channel.jd.com/computer.html", "cn"),
    ("Coupang KR", "https://www.coupang.com/np/categories/414705", "kr"),
    ("Agres ID", "https://agres.id/products?category=laptop", "id"),
    ("Best Buy US", "https://www.bestbuy.com/site/laptop-computers/all-laptops/pcmcat138500050001.c?id=pcmcat138500050001", "us"),
    ("Costco US", "https://www.costco.com/laptops.html", "us"),
    ("Lenovo Direct", "https://www.lenovo.com/us/en/d/deals/laptops/", "us"),
    ("MercadoLibre CO", "https://listado.mercadolibre.com.co/laptop", "co"),
    ("MercadoLibre CL", "https://listado.mercadolibre.cl/laptop", "cl"),
    ("Magazine Luiza BR", "https://www.magazineluiza.com.br/busca/notebook/", "br"),
]

async def diagnose_all():
    print("=" * 80)
    print("🔬 BRIGHT DATA STOREFRONT DIAGNOSTIC & CAPABILITY AUDIT")
    print("=" * 80)

    # 1. Get Scraping Browser credentials
    headers = {"Authorization": f"Bearer {api_key}"}
    r = httpx.get("https://api.brightdata.com/zone?zone=palash_manil_partner_program", headers=headers)
    pw = r.json().get("password")
    if isinstance(pw, list): pw = pw[0]
    elif isinstance(pw, dict): pw = pw.get("password")
    browser_auth = f"brd-customer-{customer}-zone-palash_manil_partner_program:{pw}"
    browser_ws_url = f"wss://{browser_auth}@brd.superproxy.io:9222"

    async with BrightDataClient(token=api_key, web_unlocker_zone="web_unlocker1") as wu_client:
        for name, url, iso in TARGETS:
            print(f"\n--- Testing: {name} ({iso.upper()}) ---")
            print(f"Target URL: {url}")
            
            # Method 1: Web Unlocker
            wu_res = ""
            wu_err = ""
            wu_size = 0
            try:
                res = await wu_client.scrape_url(url, country=iso)
                wu_res = getattr(res, "data", "") or ""
                wu_size = len(wu_res)
            except Exception as e:
                wu_err = str(e)
            
            print(f"  [1. Web Unlocker] Size: {wu_size} bytes | Error: {wu_err if wu_err else 'None'}")
            if wu_size > 0:
                is_blocked = any(b in wu_res.lower() for b in ["captcha", "challenge", "turnstile", "robot check", "access denied", "perimeterx", "cloudflare"])
                print(f"      Contains Security Barrier: {is_blocked} | Links: {wu_res.count('href=')}")

            # Method 2: Scraping Browser (Isolated Session)
            sb_size = 0
            sb_err = ""
            try:
                async with async_playwright() as pw_eng:
                    browser = await pw_eng.chromium.connect_over_cdp(browser_ws_url, timeout=30000)
                    page = await browser.new_page()
                    await page.goto(url, timeout=30000, wait_until="domcontentloaded")
                    await page.wait_for_timeout(4000)
                    sb_content = await page.content()
                    sb_size = len(sb_content)
                    await browser.close()
            except Exception as e:
                sb_err = str(e)
                # Trim error message
                if "Protocol error" in sb_err:
                    sb_err = sb_err.split("Call log:")[0].strip()

            print(f"  [2. Scraping Browser] Size: {sb_size} bytes | Error: {sb_err if sb_err else 'None'}")

asyncio.run(diagnose_all())
