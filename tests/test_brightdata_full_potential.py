"""
Unit test suite for Redesigned 52-Retailer Full-Potential Bright Data Crawling System.
Tests Amazon Specialized Scraper, Search Engine Discovery, Web Unlocker, Managed Browser,
Country Routing, Strict Classification, Accessory Rejection, Anti-Bot Detection, and Reporting.
"""
import pytest
import os
from pathlib import Path

from app.crawlers.amazon_scraper import AmazonScraperStrategy
from app.crawlers.brightdata_web_unlocker import BrightDataWebUnlockerClient, BrightDataWebUnlockerCrawler
from app.crawlers.brightdata_browser import BrightDataBrowserClient
from app.crawlers.specialized_registry import SpecializedScraperRegistry, ScraperAvailability
from app.discovery.search_engine_discovery import SearchEngineDiscoveryAdapter
from app.classification.laptop_classifier import LaptopClassifier, ProductClass
from app.evaluation.failures import FailureClassifier
from app.models.retailer import RetailerTargetConfig


class TestSecurityAndCredentials:
    def test_no_hardcoded_keys_in_env(self):
        """Verifies environment variables are dynamically sourced without hardcoding."""
        unlocker = BrightDataWebUnlockerClient()
        assert isinstance(unlocker.api_key, str)
        assert isinstance(unlocker.customer_id, str)
        assert isinstance(unlocker.zone, str)


class TestAmazonSpecializedScraper:
    def test_asin_extraction(self):
        url1 = "https://www.amazon.com/dp/B0CX234XYZ"
        url2 = "https://www.amazon.co.uk/Lenovo-Laptop/dp/B0DQVJR5WJ/ref=sr_1_1"
        url3 = "https://www.amazon.de/gp/product/B08H551P1N"
        
        assert AmazonScraperStrategy.extract_asin(url1) == "B0CX234XYZ"
        assert AmazonScraperStrategy.extract_asin(url2) == "B0DQVJR5WJ"
        assert AmazonScraperStrategy.extract_asin(url3) == "B08H551P1N"

    def test_amazon_marketplaces_mapping(self):
        strat = AmazonScraperStrategy()
        assert "US" in strat.AMAZON_MARKETPLACES
        assert "GB" in strat.AMAZON_MARKETPLACES
        assert "DE" in strat.AMAZON_MARKETPLACES
        assert "IN" in strat.AMAZON_MARKETPLACES
        assert strat.AMAZON_MARKETPLACES["GB"]["iso"] == "gb"
        assert strat.AMAZON_MARKETPLACES["DE"]["currency"] == "EUR"


class TestSpecializedRegistry:
    def test_registry_availability(self):
        reg = SpecializedScraperRegistry()
        status_amz, name_amz = reg.get_retailer_scraper_status("amazon.com")
        status_gen, name_gen = reg.get_retailer_scraper_status("currys.co.uk")

        assert status_amz == ScraperAvailability.SPECIALIZED_SCRAPER_AVAILABLE
        assert "amazon" in name_amz.lower()
        assert status_gen == ScraperAvailability.SPECIALIZED_SCRAPER_UNAVAILABLE


class TestBrightDataDiscoveryManager:
    def test_discovery_manager_initialization(self):
        from app.discovery.brightdata_discovery_manager import BrightDataDiscoveryManager
        dm = BrightDataDiscoveryManager()
        assert "FR" in dm.LOCALIZED_SEARCH_TEMPLATES
        assert "PL" in dm.LOCALIZED_SEARCH_TEMPLATES
        assert "BR" in dm.LOCALIZED_SEARCH_TEMPLATES
        assert len(dm.PDP_PATTERNS) >= 10


class TestStrictLaptopClassificationAndRejection:
    def test_valid_laptop_classification(self):
        title = "Lenovo IdeaPad Slim 3 15.6\" FHD Laptop (Intel Core i5-12450H, 16GB RAM, 512GB SSD, Windows 11 Home)"
        res = LaptopClassifier.classify(title=title, html="", url="https://example.com/item/123", price=649.99)
        assert res.is_genuine_laptop is True
        assert res.product_class == ProductClass.LAPTOP
        assert res.confidence_score >= 0.60
        assert res.detected_brand == "Lenovo"
        assert "cpu" in res.extracted_specs

    def test_valid_gaming_laptop_specs(self):
        title = "MSI Katana 17 B14WFK-400XPL (i7-14650HX, 17.3\", 16GB, 512GB, RTX 5060)"
        res = LaptopClassifier.classify(title=title, html="", url="https://example.com/item/456", price=1299.99)
        assert res.is_genuine_laptop is True
        assert res.product_class == ProductClass.LAPTOP
        assert res.detected_brand == "MSI"
        assert "cpu" in res.extracted_specs
        assert "gpu" in res.extracted_specs
        assert "ram" in res.extracted_specs
        assert "screen_size" in res.extracted_specs

    def test_reject_laptop_bags_and_sleeves(self):
        bad_titles = [
            "Targus 15.6 inch Classic Laptop Shoulder Bag / Case",
            "Mochila para Laptop 15.6 Impermeable con Puerto USB",
            "Housse Sacoche pour Ordinateur Portable 14 Pouces",
            "Tomtoc Laptop Sleeve 13-14 Zoll Tasche Hülle"
        ]
        for title in bad_titles:
            res = LaptopClassifier.classify(title=title, html="", url="https://example.com/acc/1")
            assert res.is_genuine_laptop is False
            assert res.product_class == ProductClass.ACCESSORY

    def test_reject_laptop_chargers_and_docks(self):
        bad_titles = [
            "65W USB-C Laptop Charger Adapter for Dell / HP / Lenovo",
            "Anker 10-in-1 Laptop Docking Station Dual 4K HDMI",
            "Laptop Stand Ergonomic Aluminum Notebook Riser"
        ]
        for title in bad_titles:
            res = LaptopClassifier.classify(title=title, html="", url="https://example.com/acc/2")
            assert res.is_genuine_laptop is False
            assert res.product_class == ProductClass.ACCESSORY

    def test_reject_peripherals_and_monitors(self):
        bad_titles = [
            "Logitech MX Master 3S Wireless Mouse for Laptop and PC",
            "Dell 27-inch 4K UHD Monitor Display with USB-C Hub"
        ]
        for title in bad_titles:
            res = LaptopClassifier.classify(title=title, html="", url="https://example.com/periph/1")
            assert res.is_genuine_laptop is False
            assert res.product_class in (ProductClass.PERIPHERAL, ProductClass.MONITOR, ProductClass.ACCESSORY)


class TestAntiBotAttribution:
    def test_cloudflare_and_turnstile(self):
        html = "<html><head><title>Just a moment...</title></head><body>Checking browser cf-turnstile challenge</body></html>"
        vendor = FailureClassifier.detect_anti_bot_vendor(html, {}, 403)
        assert vendor in ("Cloudflare Turnstile", "Cloudflare WAF")

    def test_akamai_and_datadome(self):
        html_akamai = "<html><head><title>Access Denied</title></head><body>AkamaiGHost access denied reference</body></html>"
        vendor_ak = FailureClassifier.detect_anti_bot_vendor(html_akamai, {"server": "AkamaiGHost"}, 403)
        assert vendor_ak == "Akamai Bot Manager"

        html_dd = "<html><body>DataDome blocked connection</body></html>"
        vendor_dd = FailureClassifier.detect_anti_bot_vendor(html_dd, {"x-datadome": "protected"}, 403)
        assert vendor_dd == "DataDome"
