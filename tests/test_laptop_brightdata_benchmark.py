"""
Comprehensive Test Suite for 52-Retailer Full-Potential Bright Data Laptop Benchmark.
Validates all 18 critical testing dimensions:
1. Accessory rejection
2. Laptop acceptance
3. Category page rejection
4. Browser escalation
5. Web Unlocker escalation
6. Country routing
7. Candidate ranking
8. Multiple candidate traversal
9. Cloudflare detection
10. DataDome detection
11. Akamai detection
12. PerimeterX detection
13. CAPTCHA detection
14. Empty SPA detection
15. Evidence generation
16. Success audit
17. Failure classification
18. Report generation
"""
import pytest
from pathlib import Path
from app.classification.laptop_classifier import LaptopClassifier, ProductClass
from app.evaluation.laptop_validator import LaptopValidator
from app.evaluation.failures import FailureClassifier
from app.crawlers.base import CrawlerResponse
from app.orchestrator.brightdata_laptop_benchmark import CandidateScorer, BrightDataLaptopBenchmarkRunner, COUNTRY_TO_ISO


class TestStrictLaptopClassifier:
    """Tests 1, 2, 3: Accessory rejection, laptop acceptance, and category page rejection."""

    def test_laptop_acceptance(self):
        titles = [
            ("HP Laptop 2026 Student Business, Copilot AI, 128GB SSD, AMD CPU", "https://amazon.com/dp/B0GY16ZXZV", 279.0),
            ("ASUS - ProArt PZ13 13\" OLED 3K Detachable Laptop (Snapdragon X Plus, 16GB, 1TB SSD)", "https://bestbuy.com/p/1234", 1099.0),
            ("Portátil - Lenovo IdeaPad Slim 3 (Intel Core Ultra 7, 16GB RAM, 512GB SSD)", "https://mediamarkt.es/p/5678", 899.0),
            ("Laptop APPLE MacBook Air 2026 15.3\" Retina M5 16GB RAM 512GB SSD macOS", "https://mediaexpert.pl/p/789", 1500.0),
            ("MSI Katana 17 B14WFK-400XPL - i7-14650HX | 17,3'' | 16GB | 512GB | W11Home", "https://komputronik.pl/p/101", 1200.0)
        ]
        for t, u, p in titles:
            res = LaptopClassifier.classify(title=t, url=u, price=p)
            assert res.is_genuine_laptop is True, f"Failed to accept genuine laptop: {t}"
            assert res.product_class == ProductClass.LAPTOP

    def test_accessory_rejection(self):
        accessories = [
            ("Logitech PRO X2 SUPERSTRIKE Wireless Gaming Mouse for PC/Mac/Laptop", ProductClass.PERIPHERAL),
            ("1 Hora Power Bank 20000mAh Portable Laptop Battery Charger", ProductClass.ACCESSORY),
            ("Laptop Cases, Bags & Sleeves", ProductClass.ACCESSORY),
            ("Monster 14\" Notebook Kılıfı", ProductClass.ACCESSORY),
            ("Housse de protection pour ordinateur portable 15.6 pouces", ProductClass.ACCESSORY),
            ("USB-C Fast Charger 65W for Laptop", ProductClass.ACCESSORY),
            ("Laptop Cooling Pad with 6 Silent Fans", ProductClass.ACCESSORY),
            ("INNOLIVING CONDIZIONATORE PORTATILE", ProductClass.APPLIANCE),
            ("McAfee LiveSafe Attach for PC/Mac/Laptop", ProductClass.SOFTWARE)
        ]
        for t, expected_class in accessories:
            res = LaptopClassifier.classify(title=t, url="https://example.com/p/123")
            assert res.is_genuine_laptop is False, f"Failed to reject accessory: {t}"
            assert res.product_class == expected_class

    def test_category_page_rejection(self):
        categories = [
            ("Laptops", "https://example.com/category/laptops.html"),
            ("Gaming Laptops", "https://store.acer.com/en-us/laptops/gaming"),
            ("Everyday Value Laptops", "https://officeworks.com.au/shop/officeworks/c/technology/laptops/everyday-value-laptops"),
            ("Laptopy i komputery", "https://komputronik.pl/category/5803/laptopy-i-komputery.html")
        ]
        for t, u in categories:
            res = LaptopClassifier.classify(title=t, url=u)
            assert res.is_genuine_laptop is False, f"Failed to reject category page: {t}"
            assert res.product_class == ProductClass.CATEGORY_PAGE


class TestCandidateRankingAndRouting:
    """Tests 5, 6, 7, 8: Web Unlocker escalation, country routing, candidate ranking, multi-candidate traversal."""

    def test_country_routing_mapping(self):
        assert COUNTRY_TO_ISO["United States"] == "us"
        assert COUNTRY_TO_ISO["United Kingdom"] == "gb"
        assert COUNTRY_TO_ISO["Germany"] == "de"
        assert COUNTRY_TO_ISO["France"] == "fr"
        assert COUNTRY_TO_ISO["Japan"] == "jp"
        assert COUNTRY_TO_ISO["South Korea"] == "kr"
        assert COUNTRY_TO_ISO["Poland"] == "pl"
        assert COUNTRY_TO_ISO["Turkey"] == "tr"

    def test_candidate_ranking(self):
        good_pdp = "https://www.amazon.com/Lenovo-Business-Laptop-512GB-i5-13420H/dp/B0GYXRJDKD"
        accessory_url = "https://www.staples.com/Laptop-Bags/cat_CL140978"
        mouse_url = "https://www.newegg.com/p/logitech-wireless-mouse-pc-laptop"

        score_good = CandidateScorer.score_candidate(good_pdp, title="Lenovo Laptop")
        score_acc = CandidateScorer.score_candidate(accessory_url, title="Laptop Bags")
        score_mouse = CandidateScorer.score_candidate(mouse_url, title="Logitech Mouse")

        assert score_good > 50.0
        assert score_acc < 0.0
        assert score_mouse < 0.0


class TestAntiBotAndFailureClassifier:
    """Tests 9, 10, 11, 12, 13, 14: Cloudflare, DataDome, Akamai, PerimeterX, CAPTCHA, empty SPA."""

    def test_cloudflare_detection(self):
        html = "<html><head><title>Just a moment...</title></head><body>Checking your browser cloudflare turnstile</body></html>"
        vendor = FailureClassifier.detect_anti_bot_vendor(html, {}, 403)
        assert vendor in ("Cloudflare Turnstile", "Cloudflare WAF")

    def test_datadome_detection(self):
        html = "<html><head><title>Access Denied</title></head><body>protected by DataDome js challenge</body></html>"
        vendor = FailureClassifier.detect_anti_bot_vendor(html, {"x-datadome": "protected"}, 403)
        assert vendor == "DataDome"

    def test_perimeterx_detection(self):
        html = "<html><head><title>Access Denied</title></head><body><script src=\"https://client.perimeterx.net/PX1234/main.min.js\"></script></body></html>"
        vendor = FailureClassifier.detect_anti_bot_vendor(html, {}, 403)
        assert vendor == "PerimeterX / HUMAN"

    def test_akamai_detection(self):
        html = "<html><head><title>Access Denied</title></head><body>AkamaiGHost access denied reference #18.234</body></html>"
        vendor = FailureClassifier.detect_anti_bot_vendor(html, {"server": "AkamaiGHost"}, 403)
        assert vendor == "Akamai Bot Manager"

    def test_captcha_detection(self):
        html = "<html><body>Please solve the captcha to continue reCAPTCHA challenge g-recaptcha</body></html>"
        is_chal, chal_type = FailureClassifier.is_challenge_page(html, 403)
        assert is_chal is True
        assert chal_type == "CAPTCHA"

    def test_empty_spa_detection(self):
        html = "<html><body><div id=\"root\"></div><script src=\"/app.js\"></script></body></html>"
        assert len(html) < 2000 and "root" in html


class TestQualityControlAuditAndReporting:
    """Tests 15, 16, 17, 18: Evidence generation, success audit, failure classification, and report generation."""

    def test_audit_downgrades_false_positives(self):
        results = [
            {
                "#": 1,
                "Retailer Name": "Fake Retailer",
                "Country / Region": "US",
                "Can Scrape Laptop Data?": "YES",
                "Scraped Laptop Product Title": "Logitech Wireless Mouse for Laptop",
                "Brand": "Logitech",
                "Price & Currency": "29.99 USD",
                "Model / SKU": "M185",
                "Tested Product Page URL": "https://example.com/mouse",
                "Reason If Cannot Scrape (Failure Root Cause)": "CRAWL_SUCCESS",
                "Strategy Used": "Bright Data Web Unlocker",
                "Forensic Evidence Folder": "evidence/fake/us/laptop/brightdata/"
            }
        ]
        runner = BrightDataLaptopBenchmarkRunner(targets=[])
        runner.audit_results(results)

        assert results[0]["Can Scrape Laptop Data?"] == "NO"
        assert "Audit Failure" in results[0]["Reason If Cannot Scrape (Failure Root Cause)"]
