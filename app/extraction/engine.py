from typing import Dict, Any, Optional, List, Tuple
from bs4 import BeautifulSoup
from app.models.retailer import RetailerTargetConfig
from app.models.product import NormalizedProduct, FieldValidation
from app.extraction.jsonld import JsonLdExtractor
from app.extraction.embedded_json import EmbeddedJsonExtractor
from app.extraction.opengraph import OpenGraphExtractor
from app.extraction.dom import DomExtractor
from app.extraction.validators import ExtractionValidator
from app.extraction.template import ProductTemplateIdentifier
from app.discovery.deduplicator import ProductDeduplicator


class ProductExtractionEngine:
    """Multi-source extraction engine that combines JSON-LD, Embedded JSON, OpenGraph, DOM, and Adapters."""

    def __init__(self, target_config: RetailerTargetConfig):
        self.target_config = target_config
        self.jsonld_extractor = JsonLdExtractor(target_config)
        self.embedded_extractor = EmbeddedJsonExtractor(target_config)
        self.opengraph_extractor = OpenGraphExtractor(target_config)
        self.dom_extractor = DomExtractor(target_config)

    def extract_product(
        self,
        html: str,
        url: str,
        crawler_strategy: str = "HTTP",
        custom_adapter_result: Optional[Dict[str, Any]] = None,
        markdown: Optional[str] = None
    ) -> Tuple[Optional[NormalizedProduct], Optional[str]]:
        """
        Extracts product data from all available sources, detects conflicts,
        identifies structural templates, validates the schema, and builds a NormalizedProduct.
        """
        if not html and not markdown:
            return None, "HTML and Markdown content are both empty"

        soup = BeautifulSoup(html, "html.parser") if html else None
        source_extractions: Dict[str, Dict[str, Any]] = {}

        # 0. Template identification
        template_profile = ProductTemplateIdentifier.analyze_template(html) if html else None

        if soup:
            # 1. JSON-LD extraction
            jsonld_data = self.jsonld_extractor.extract(html, url, soup=soup)
            if jsonld_data:
                source_extractions["JSON_LD"] = jsonld_data

            # 2. Embedded App JSON extraction (__NEXT_DATA__, __NUXT__, Apollo, Redux)
            embedded_data = self.embedded_extractor.extract(html, url, soup=soup)
            if embedded_data:
                source_extractions["EMBEDDED_JSON"] = embedded_data

            # 3. OpenGraph / Meta extraction
            og_data = self.opengraph_extractor.extract(html, url, soup=soup)
            if og_data:
                source_extractions["OPENGRAPH"] = og_data

            # 4. DOM extraction
            dom_data = self.dom_extractor.extract(html, url, soup=soup)
            if dom_data:
                source_extractions["DOM"] = dom_data

        # 5. Markdown extraction (e.g. from Firecrawl dual output)
        if markdown and markdown.strip():
            md_data = {}
            import re
            lines = markdown.split("\n")
            for line in lines:
                line_str = line.strip()
                if line_str.startswith("# ") and not md_data.get("title"):
                    md_data["title"] = line_str[2:].strip()
                price_match = re.search(r"(?:Price|Precio|Preis|Preço|Prix)[:\s]+([\d.,]+)\s*([€$£¥₹]|\w{3})?", line_str, re.I)
                if price_match and not md_data.get("price"):
                    raw_p = price_match.group(1).replace(",", ".")
                    try:
                        md_data["price"] = float(raw_p)
                    except ValueError:
                        pass
                brand_match = re.search(r"(?:Brand|Marca|Marke|Marque)[:\s]+([^\n|]+)", line_str, re.I)
                if brand_match and not md_data.get("brand"):
                    md_data["brand"] = brand_match.group(1).strip()

            if md_data:
                source_extractions["FIRECRAWL_MARKDOWN"] = md_data

        # 6. Retailer custom adapter
        if custom_adapter_result:
            source_extractions["ADAPTER"] = custom_adapter_result

        if not source_extractions:
            return None, "No product data could be extracted by any extractor"

        # Multi-source conflict detection
        conflicts, has_critical_conflict = ExtractionValidator.detect_conflicts(source_extractions)

        # Merge extracted fields in priority: ADAPTER -> JSON_LD -> EMBEDDED_JSON -> DOM -> OPENGRAPH -> FIRECRAWL_MARKDOWN
        priority_order = ["ADAPTER", "JSON_LD", "EMBEDDED_JSON", "DOM", "OPENGRAPH", "FIRECRAWL_MARKDOWN"]
        merged: Dict[str, Any] = {}
        primary_method = "GENERIC"

        for source in reversed(priority_order):
            if source in source_extractions:
                merged.update({k: v for k, v in source_extractions[source].items() if v is not None})
                primary_method = source

        # Extract/normalize product identifier
        extracted_sku = merged.get("sku") or merged.get("product_id")
        if not extracted_sku:
            extracted_sku = ProductDeduplicator.extract_product_key(url, self.target_config)
            merged["sku"] = extracted_sku

        # Validate extracted fields with strict 5-state discriminator
        expected_curr = getattr(self.target_config, "currency", "USD")
        validation = ExtractionValidator.validate_fields(merged, expected_currency=expected_curr, field_conflicts=conflicts)

        # Build NormalizedProduct entity
        product = NormalizedProduct(
            retailer=self.target_config.retailer,
            country=self.target_config.country,
            source_url=url,
            canonical_url=merged.get("canonical_url") or url,
            product_id=merged.get("product_id") or extracted_sku,
            sku=extracted_sku,
            gtin=merged.get("gtin"),
            brand=merged.get("brand"),
            model=merged.get("model"),
            title=merged.get("title"),
            category=merged.get("category"),
            description=merged.get("description"),
            price=merged.get("price"),
            currency=merged.get("currency") or expected_curr,
            availability=merged.get("availability"),
            stock_status=merged.get("stock_status"),
            rating=merged.get("rating"),
            review_count=merged.get("review_count"),
            image_urls=merged.get("image_urls") or ([merged["image_url"]] if merged.get("image_url") else []),
            seller=merged.get("seller"),
            shipping_information=merged.get("shipping_information"),
            product_template_id=template_profile.template_id if template_profile else None,
            product_template_signature=template_profile.template_signature if template_profile else None,
            product_template_framework=template_profile.framework_detected if template_profile else None,
            extraction_method=primary_method,
            crawler_strategy=crawler_strategy,
            confidence=validation.schema_completeness,
            validation=validation
        )

        return product, None
