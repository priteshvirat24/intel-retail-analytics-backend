"""
Homepage Banner Tracker & Reference Screenshot Generator for PC-Industry Intelligence.
Captures banner content, promo flags, destination links, and stores reference screenshots.
"""
import os
import json
from pathlib import Path
from typing import Dict, List, Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SCREENSHOTS_DIR = PROJECT_ROOT / "poc_data" / "screenshots"


class BannerCollector:
    """Collects homepage banners and generates reference screenshot assets."""

    @classmethod
    def collect_sample_banners(cls) -> List[Dict[str, Any]]:
        """
        Collects curated sample banner records for the 6 target sites (3 1P, 1 Marketplace, 2 OEM).
        Strictly capped scope for the POC.
        """
        SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)

        banners = [
            {
                "banner_id": "ban_bestbuy_01",
                "site_id": "bestbuy-us",
                "retailer": "Best Buy",
                "site_type": "1P_RETAILER",
                "brand": "Intel Core Ultra",
                "headline": "Next-Gen AI PCs Powered by Intel Core Ultra",
                "subheadline": "Experience built-in AI acceleration, all-day battery life, and peak gaming performance.",
                "discount_text": "Save up to $300 on select Intel Core Ultra Laptops",
                "destination_link": "https://www.bestbuy.com/site/clp-computers-pcs/intel-core-ultra/pcmcat1704383408037.c",
                "has_destination_link": True,
                "flags": {
                    "evo_flag": True,
                    "gaming_flag": True,
                    "premier_sku_flag": True,
                    "ai_pc_flag": True
                },
                "position": "HERO_CAROUSEL_SLIDE_1",
                "screenshot_file": "banner_bestbuy_intel_ultra.png"
            },
            {
                "banner_id": "ban_walmart_01",
                "site_id": "walmart-us",
                "retailer": "Walmart",
                "site_type": "1P_RETAILER",
                "brand": "Intel",
                "headline": "Intel Core Powered Everyday Laptops for Back-to-School",
                "subheadline": "HP, Lenovo, and ASUS laptops starting under $499.",
                "discount_text": "Rollback: $150 Off HP Pavilion Intel Core i5",
                "destination_link": "https://www.walmart.com/browse/electronics/laptops/3944_3951_1089430?facet=processor_type%3AIntel+Core",
                "has_destination_link": True,
                "flags": {
                    "evo_flag": False,
                    "gaming_flag": False,
                    "premier_sku_flag": False,
                    "ai_pc_flag": False
                },
                "position": "DEPT_BANNER_ROW_1",
                "screenshot_file": "banner_walmart_intel_rollback.png"
            },
            {
                "banner_id": "ban_costco_01",
                "site_id": "costco-us",
                "retailer": "Costco",
                "site_type": "1P_RETAILER",
                "brand": "Intel Core Ultra",
                "headline": "Costco Members Exclusive: Intel Core Ultra Dell XPS & HP Envy Bundles",
                "subheadline": "Includes 2-Year Warranty + 32GB RAM Upgrade.",
                "discount_text": "$350 OFF Dell XPS 14 Intel Core Ultra 7",
                "destination_link": "https://www.costco.com/laptops.html?processor-type=intel-core-ultra",
                "has_destination_link": True,
                "flags": {
                    "evo_flag": True,
                    "gaming_flag": False,
                    "premier_sku_flag": True,
                    "ai_pc_flag": True
                },
                "position": "HOMEPAGE_OFFER_SLIDE_2",
                "screenshot_file": "banner_costco_xps_ultra.png"
            },
            {
                "banner_id": "ban_amazon_01",
                "site_id": "amazon-us",
                "retailer": "Amazon US",
                "site_type": "MARKETPLACE",
                "brand": "PC Mix",
                "headline": "Amazon PC Store — Top Brand Gaming & AI Laptops",
                "subheadline": "Shop ASUS ROG, Lenovo Legion, and Acer Predator with Intel & NVIDIA.",
                "discount_text": "Up to 25% Off Prime Deals on Gaming PCs",
                "destination_link": "https://www.amazon.com/b?node=565108",
                "has_destination_link": True,
                "flags": {
                    "evo_flag": False,
                    "gaming_flag": True,
                    "premier_sku_flag": True,
                    "ai_pc_flag": True
                },
                "position": "TOP_SPONSORED_STRIP",
                "screenshot_file": "banner_amazon_pc_store.png"
            },
            {
                "banner_id": "ban_dell_01",
                "site_id": "dell-us",
                "retailer": "Dell Technologies",
                "site_type": "OEM_DIRECT",
                "brand": "Intel Core Ultra",
                "headline": "New XPS 13 & 16 with Intel Core Ultra Series",
                "subheadline": "Smarter, faster AI experiences with dedicated Intel AI Boost NPU.",
                "discount_text": "Save $200 + Free Express Shipping",
                "destination_link": "https://www.dell.com/en-us/shop/dell-laptops/scr/laptops/xps",
                "has_destination_link": True,
                "flags": {
                    "evo_flag": True,
                    "gaming_flag": False,
                    "premier_sku_flag": True,
                    "ai_pc_flag": True
                },
                "position": "HERO_BANNER_DELL_MAIN",
                "screenshot_file": "banner_dell_xps_ultra.png"
            },
            {
                "banner_id": "ban_hp_01",
                "site_id": "hp-us",
                "retailer": "HP Direct",
                "site_type": "OEM_DIRECT",
                "brand": "AMD / Intel Mix",
                "headline": "HP OMEN & Envy — Creators & Gaming Powerhouses",
                "subheadline": "Custom configurable desktop towers and OLED laptops.",
                "discount_text": "Save up to $450 with code HPCOMMERCE",
                "destination_link": "https://www.hp.com/us-en/shop/vwa/laptops",
                "has_destination_link": True,
                "flags": {
                    "evo_flag": False,
                    "gaming_flag": True,
                    "premier_sku_flag": True,
                    "ai_pc_flag": False
                },
                "position": "HOMEPAGE_FEATURE_SLIDE_1",
                "screenshot_file": "banner_hp_omen_envy.png"
            }
        ]

        # Generate SVG mock screenshots for reference viewer
        for b in banners:
            svg_content = cls._generate_mock_banner_svg(b)
            svg_path = SCREENSHOTS_DIR / b["screenshot_file"].replace(".png", ".svg")
            with open(svg_path, "w", encoding="utf-8") as f:
                f.write(svg_content)
            b["screenshot_svg_path"] = str(svg_path.relative_to(PROJECT_ROOT))

        return banners

    @classmethod
    def _generate_mock_banner_svg(cls, banner: Dict[str, Any]) -> str:
        """Generates an aesthetic SVG reference banner image."""
        brand = banner["brand"]
        headline = banner["headline"]
        discount = banner["discount_text"]
        ret = banner["retailer"]

        bg_gradient = "linear-gradient(135deg, #0071C5 0%, #00C7FD 50%, #0F172A 100%)" if "Intel" in brand else "linear-gradient(135deg, #1E293B 0%, #334155 100%)"
        accent_color = "#00C7FD" if "Intel" in brand else "#E11D48"

        return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="50%" stop-color="#1E293B" />
      <stop offset="100%" stop-color="#003C71" />
    </linearGradient>
    <linearGradient id="intelGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0071C5" />
      <stop offset="100%" stop-color="#00C7FD" />
    </linearGradient>
  </defs>
  <rect width="1200" height="400" fill="url(#bg)" rx="16" />
  <rect x="20" y="20" width="1160" height="360" fill="none" stroke="#334155" stroke-width="2" rx="12" />
  
  <!-- Store Tag -->
  <rect x="50" y="50" width="160" height="36" rx="8" fill="#1E293B" />
  <text x="130" y="74" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">{ret}</text>
  
  <!-- Brand Badge -->
  <rect x="220" y="50" width="200" height="36" rx="8" fill="url(#intelGrad)" />
  <text x="320" y="74" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">{brand}</text>

  <!-- Headline -->
  <text x="50" y="160" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="34" font-weight="800">{headline[:45]}</text>
  <text x="50" y="200" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="18">{banner['subheadline'][:70]}</text>
  
  <!-- Discount Badge -->
  <rect x="50" y="250" width="450" height="60" rx="10" fill="#0071C5" opacity="0.9" />
  <text x="70" y="288" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="20" font-weight="bold">🏷️ {discount}</text>

  <!-- CTA Button -->
  <rect x="950" y="260" width="180" height="50" rx="10" fill="#00C7FD" />
  <text x="1040" y="292" fill="#0F172A" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">Shop Deals →</text>
  
  <!-- Footer Proof of Concept Label -->
  <text x="1130" y="365" fill="#64748B" font-family="system-ui, sans-serif" font-size="11" text-anchor="end">POC Benchmark Reference Capture • {banner['site_id']}</text>
</svg>"""
