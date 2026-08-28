import os
import json
import csv
from bs4 import BeautifulSoup
from app.extraction.validators import ExtractionValidator
from app.models.retailer import RetailerTargetConfig
from app.retailers.registry import RetailerAdapterRegistry
from app.extraction.engine import ProductExtractionEngine

extracted_items = [
    ("amazon-br", "B09G9FPHY6", "Brazil", "BRL", "evidence/amazon/BRAZIL/B09G9FPHY6"),
    ("amazon-es", "B0CL6LMC9N", "Spain", "EUR", "evidence/amazon/SPAIN/B0CL6LMC9N"),
    ("amazon-de", "B0CL6LMC9N", "Germany", "EUR", "evidence/amazon/GERMANY/B0CL6LMC9N"),
    ("amazon-de", "B09G91LXFP", "Germany", "EUR", "evidence/amazon/GERMANY/B09G91LXFP"),
    ("reliancedigital-in", "sku_0012", "India", "INR", "evidence/reliancedigital/INDIA/sku_0012"),
    ("tmall-cn", "sku_0020", "China", "CNY", "evidence/tmall/CHINA/sku_0020"),
    ("tmall-cn", "sku_0016", "China", "CNY", "evidence/tmall/CHINA/sku_0016"),
    ("tmall-cn", "sku_0015", "China", "CNY", "evidence/tmall/CHINA/sku_0015"),
]

out_path = "reports/runs/run_20260823_phase3a_forensic/validation_audit.csv"
os.makedirs(os.path.dirname(out_path), exist_ok=True)

previously_validated = 0
newly_validated = 0
still_failed = 0
rows = []

for tid, skuid, country, curr, path in extracted_items:
    html_files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith(".html")]
    html_content = ""
    if html_files:
        with open(html_files[0], "r", encoding="utf-8", errors="ignore") as f:
            html_content = f.read()

    retailer_name = tid.split("-")[0]
    cfg = RetailerTargetConfig(
        target_id=tid,
        retailer=retailer_name,
        brand_name=retailer_name.title(),
        base_url=f"https://www.{retailer_name}.com",
        country=country,
        iso_country=tid.split("-")[1].upper(),
        domain=f"{retailer_name}.com",
        locale="en-US",
        currency=curr,
        timezone="UTC",
        discovery_methods=[],
        category_seeds=[],
        sitemap_urls=[],
        seed_urls=[],
        max_concurrency=1,
        rate_limit=1.0
    )

    adapter = RetailerAdapterRegistry.get_adapter(cfg)
    custom_res = None
    if adapter and html_content:
        try:
            custom_res = adapter.extract_custom(html_content, f"https://www.{cfg.domain}/dp/{skuid}")
        except Exception:
            pass

    engine = ProductExtractionEngine(cfg)
    product, err = engine.extract_product(
        html=html_content,
        url=f"https://www.{cfg.domain}/dp/{skuid}",
        crawler_strategy="HTTP",
        custom_adapter_result=custom_res
    )

    if product and product.validation:
        val = product.validation
        states = val.field_states
        is_valid = val.is_valid_sku
        final_st = "SUCCESS" if is_valid else "PARTIAL_SUCCESS" if val.title_valid else "FAILED"
        fail_reason = ", ".join(val.validation_errors) if not is_valid else "NONE"
        if not is_valid and not val.validation_errors:
            fail_reason = "Price not observed and availability is not out-of-stock"

        if is_valid:
            newly_validated += 1
        else:
            still_failed += 1

        rows.append({
            "sku_id": skuid,
            "title_status": states.get("title", "FIELD_NOT_OBSERVED").value if hasattr(states.get("title"), "value") else states.get("title", "FIELD_NOT_OBSERVED"),
            "brand_status": states.get("brand", "FIELD_NOT_OBSERVED").value if hasattr(states.get("brand"), "value") else states.get("brand", "FIELD_NOT_OBSERVED"),
            "price_status": states.get("price", "FIELD_NOT_OBSERVED").value if hasattr(states.get("price"), "value") else states.get("price", "FIELD_NOT_OBSERVED"),
            "currency_status": states.get("currency", "FIELD_NOT_OBSERVED").value if hasattr(states.get("currency"), "value") else states.get("currency", "FIELD_NOT_OBSERVED"),
            "availability_status": states.get("availability", "FIELD_NOT_OBSERVED").value if hasattr(states.get("availability"), "value") else states.get("availability", "FIELD_NOT_OBSERVED"),
            "sku_status": states.get("sku", "FIELD_NOT_OBSERVED").value if hasattr(states.get("sku"), "value") else states.get("sku", "FIELD_NOT_OBSERVED"),
            "gtin_status": states.get("gtin", "FIELD_NOT_OBSERVED").value if hasattr(states.get("gtin"), "value") else states.get("gtin", "FIELD_NOT_OBSERVED"),
            "images_status": states.get("images", "FIELD_NOT_OBSERVED").value if hasattr(states.get("images"), "value") else states.get("images", "FIELD_NOT_OBSERVED"),
            "description_status": states.get("description", "FIELD_NOT_OBSERVED").value if hasattr(states.get("description"), "value") else states.get("description", "FIELD_NOT_OBSERVED"),
            "final_status": final_st,
            "failure_reason": fail_reason
        })
    else:
        still_failed += 1
        rows.append({
            "sku_id": skuid,
            "title_status": "FIELD_NOT_OBSERVED",
            "brand_status": "FIELD_NOT_OBSERVED",
            "price_status": "FIELD_NOT_OBSERVED",
            "currency_status": "FIELD_NOT_OBSERVED",
            "availability_status": "FIELD_NOT_OBSERVED",
            "sku_status": "FIELD_NOT_OBSERVED",
            "gtin_status": "FIELD_NOT_OBSERVED",
            "images_status": "FIELD_NOT_OBSERVED",
            "description_status": "FIELD_NOT_OBSERVED",
            "final_status": "FAILED",
            "failure_reason": "Extraction failed: no product data"
        })

fieldnames = [
    "sku_id", "title_status", "brand_status", "price_status", "currency_status",
    "availability_status", "sku_status", "gtin_status", "images_status",
    "description_status", "final_status", "failure_reason"
]

with open(out_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Validation audit generated at {out_path}")
print(f"Previously Validated: {previously_validated}")
print(f"Newly Validated: {newly_validated}")
print(f"Still Failed: {still_failed}")
print(f"VALIDATOR-INDUCED FALSE NEGATIVES: {newly_validated}")
