"""
Scraper Scope Configuration for PC-Industry Pricing & Competitive Intelligence POC.

========================================================================================
CRITICAL COST CONTROL CONSTRAINTS & CAPPED SCOPE:
- 1P Retailers: 3 websites (Best Buy, Walmart, Costco) [Production: 173]
- Marketplaces: 1 website (Amazon US) [Production: 14]
- OEM.com sites: 2 websites (Dell, HP) [Production: 6]
- Countries: 1 (US) [Production: 23]
- SKUs per site: 3–4 SKUs per site, capped at 18–20 products total (Laptop/Desktop mix)
- SOV Keywords: 10 sample queries [Production: 80]
- Frequency: Exactly ONCE batch run — no cron, no recurring schedule
========================================================================================
"""
from typing import Dict, List, Any

# CAPPED: Only 1 Country (US)
TARGET_COUNTRY = "United States"
TARGET_COUNTRY_ISO = "us"
CURRENCY = "USD"

# CAPPED: 3 1P Retailers, 1 Marketplace, 2 OEM sites (Total 6 sites)
SITES_CONFIG = {
    # 1P Retailers (3)
    "bestbuy-us": {
        "name": "Best Buy",
        "type": "1P_RETAILER",
        "domain": "bestbuy.com",
        "url": "https://www.bestbuy.com",
        "laptop_hub": "https://www.bestbuy.com/site/laptop-computers/all-laptops/pcmcat138500050001.c",
        "desktop_hub": "https://www.bestbuy.com/site/desktop-computers/all-desktops/pcmcat143400050013.c",
        "max_skus_capped": 4  # CAPPED: max 4 SKUs
    },
    "walmart-us": {
        "name": "Walmart",
        "type": "1P_RETAILER",
        "domain": "walmart.com",
        "url": "https://www.walmart.com",
        "laptop_hub": "https://www.walmart.com/browse/electronics/laptops/3944_3951_1089430",
        "desktop_hub": "https://www.walmart.com/browse/electronics/desktop-computers/3944_3951_132982",
        "max_skus_capped": 3  # CAPPED: max 3 SKUs
    },
    "costco-us": {
        "name": "Costco",
        "type": "1P_RETAILER",
        "domain": "costco.com",
        "url": "https://www.costco.com",
        "laptop_hub": "https://www.costco.com/laptops.html",
        "desktop_hub": "https://www.costco.com/desktops.html",
        "max_skus_capped": 3  # CAPPED: max 3 SKUs
    },
    # Marketplaces (1)
    "amazon-us": {
        "name": "Amazon US",
        "type": "MARKETPLACE",
        "domain": "amazon.com",
        "url": "https://www.amazon.com",
        "laptop_hub": "https://www.amazon.com/s?k=laptop",
        "desktop_hub": "https://www.amazon.com/s?k=desktop+pc",
        "max_skus_capped": 4  # CAPPED: max 4 SKUs
    },
    # OEM.com Sites (2)
    "dell-us": {
        "name": "Dell Technologies",
        "type": "OEM_DIRECT",
        "domain": "dell.com",
        "url": "https://www.dell.com",
        "laptop_hub": "https://www.dell.com/en-us/shop/dell-laptops/scr/laptops",
        "desktop_hub": "https://www.dell.com/en-us/shop/desktop-computers/scr/desktops",
        "max_skus_capped": 3  # CAPPED: max 3 SKUs
    },
    "hp-us": {
        "name": "HP Direct",
        "type": "OEM_DIRECT",
        "domain": "hp.com",
        "url": "https://www.hp.com",
        "laptop_hub": "https://www.hp.com/us-en/shop/vwa/laptops",
        "desktop_hub": "https://www.hp.com/us-en/shop/vwa/desktops",
        "max_skus_capped": 3  # CAPPED: max 3 SKUs
    }
}

# CAPPED: Total SKU Cap Across All 6 Sites (Target: 18–20 SKUs total)
TOTAL_MAX_SKUS = 20

# CAPPED: Exactly 10 Sample SOV Keywords (Production: 80)
SOV_SAMPLE_KEYWORDS = [
    "intel core ultra laptop",
    "ai pc laptop",
    "gaming laptop",
    "intel evo laptop",
    "intel core i7 notebook",
    "business desktop pc",
    "oled laptop intel",
    "intel core i9 gaming desktop",
    "ultrabook intel core",
    "intel vpro business laptop"
]

# Audit Flag Definitions
AUDIT_FLAG_SCHEMA = {
    "S1": "Listing page title contains Intel / Intel Core / Intel Core Ultra / Competitor mention",
    "S2": "Listing page product badge presence (e.g. Intel EVO, Intel Inside, RTX Studio)",
    "P1": "PDP title contains Intel / Intel Core / Intel Core Ultra processor branding",
    "P2": "PDP official processor/platform badge present",
    "P3": "PDP technical specification section accurately lists processor series, gen, & clock",
    "P4": "Intel rich media module present (A+ content, Intel feature carousel, processor infographics)",
    "P5": "OEM rich media module present (OEM product video, 3D interactive, thermal design module)"
}
