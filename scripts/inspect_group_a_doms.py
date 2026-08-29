"""
Inspect exact DOM structures of Group A SPA sites via Scraping Browser CDP.
Finds exact selectors for titles, prices, links, and hardware specs.
"""
import os
import re
import json
import httpx
import asyncio
from pathlib import Path
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

env_vars = {}
for line in open(".env"):
    if "=" in line and not line.startswith("#"):
        k, v = line.strip().split("=", 1)
        env_vars[k] = v

api_key = env_vars.get("BRIGHTDATA_API_KEY")
customer = env_vars.get("BRIGHTDATA_CUSTOMER_ID")

headers = {"Authorization": f"Bearer {api_key}"}
r = httpx.get("https://api.brightdata.com/zone?zone=palash_manil_partner_program", headers=headers)
pw = r.json().get("password")
if isinstance(pw, list): pw = pw[0]
elif isinstance(pw, dict): pw = pw.get("password")
browser_auth = f"brd-customer-{customer}-zone-palash_manil_partner_program:{pw}"
browser_ws_url = f"wss://{browser_auth}@brd.superproxy.io:9222"

TARGETS = [
    ("Best Buy US", "https://www.bestbuy.com/site/laptop-computers/all-laptops/pcmcat138500050001.c?id=pcmcat138500050001"),
    ("Lenovo Direct US", "https://www.lenovo.com/us/en/d/deals/laptops/"),
    ("Expert DE", "https://www.expert.de/shop/unsere-produkte/computer-zubehor/notebooks"),
    ("MediaWorld IT", "https://www.mediaworld.it/it/category/notebook-100.html"),
    ("Agres ID", "https://agres.id/products?category=laptop"),
    ("JD.com CN", "https://channel.jd.com/computer.html")
]

async def inspect_doms():
    print("=" * 80)
    print("🔬 INSPECTING REAL RENDERED DOMs FOR GROUP A SPA SITES")
    print("=" * 80)

    async with async_playwright() as pw_eng:
        for name, url in TARGETS:
            print(f"\n--- {name} ---")
            print(f"URL: {url}")
            try:
                browser = await pw_eng.chromium.connect_over_cdp(browser_ws_url, timeout=45000)
                page = await browser.new_page()
                await page.goto(url, timeout=45000, wait_until="domcontentloaded")
                await page.wait_for_timeout(6000)
                for _ in range(3):
                    await page.evaluate("window.scrollBy(0, 800)")
                    await page.wait_for_timeout(1000)

                html = await page.content()
                soup = BeautifulSoup(html, "html.parser")
                print(f"Rendered HTML Size: {len(html):,} bytes")

                # Sample candidate tags
                links = soup.find_all("a", href=True)
                product_links = []
                for a in links:
                    h = a["href"]
                    t = a.get_text().strip()
                    if any(k in h.lower() for k in ["product", "item", "pdp", ".p?sku", "/p/", "/pd/"]) and len(t) > 15:
                        product_links.append((t, h))

                print(f"Found {len(product_links)} potential product links with text.")
                for t, h in product_links[:5]:
                    print(f"  • Link text: {t[:60]}... | href: {h[:60]}...")

                # Look for price spans
                prices = []
                for el in soup.find_all(["span", "div", "p"], class_=re.compile(r"price|amount|val|cost", re.I)):
                    txt = el.get_text().strip()
                    if re.search(r"[\$€£¥₹]\s*\d+|\d+[\.,]\d{2}", txt) and len(txt) < 30:
                        prices.append((el.name, el.get("class"), txt))
                print(f"Found {len(prices)} potential price elements.")
                for tag, cls, txt in prices[:5]:
                    print(f"  • Tag: <{tag} class='{' '.join(cls) if cls else ''}'>: {txt}")

                await browser.close()
            except Exception as e:
                print(f"Error inspecting {name}: {e}")

asyncio.run(inspect_doms())
