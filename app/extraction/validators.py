import re
from typing import Dict, Any, List, Tuple, Optional
from app.models.product import FieldValidation, NormalizedProduct, FieldState


class ExtractionValidator:
    """Validates extracted product attributes, detects multi-source conflicts, and calculates quality scores."""

    ISO_CURRENCIES = {
        "USD", "EUR", "GBP", "INR", "JPY", "CAD", "AUD", "BRL", "MXN",
        "PLN", "TRY", "VND", "DKK", "NOK", "SEK", "CLP", "COP", "CNY", "KRW", "IDR"
    }

    INVALID_TITLE_PHRASES = [
        "access denied", "robot check", "captcha", "security check", "404 not found",
        "page not found", "just a moment", "attention required", "error 403",
        "enable javascript", "verify you are human", "blocked", "are you a human"
    ]

    @classmethod
    def validate_fields(
        cls,
        data: Dict[str, Any],
        expected_currency: str = "USD",
        field_conflicts: Optional[Dict[str, Any]] = None
    ) -> FieldValidation:
        val = FieldValidation()
        errors: List[str] = []
        states: Dict[str, FieldState] = {}
        conflicts = field_conflicts or {}

        # 1. Title Validation
        title = data.get("title")
        if title is None or (isinstance(title, str) and not title.strip()):
            states["title"] = FieldState.FIELD_NOT_OBSERVED
            val.title_valid = False
            errors.append("Title is missing (Required field)")
        elif "title" in conflicts:
            states["title"] = FieldState.FIELD_CONFLICT
            val.title_valid = False
            errors.append("Title conflict across extraction sources (Required field)")
        elif isinstance(title, str) and len(title.strip()) >= 3:
            lower_title = title.lower()
            if any(phrase in lower_title for phrase in cls.INVALID_TITLE_PHRASES):
                states["title"] = FieldState.FIELD_INVALID
                errors.append(f"Title contains bot/error block phrase: '{title[:40]}...' (Required field)")
                val.title_valid = False
            else:
                states["title"] = FieldState.FIELD_PRESENT_VALID
                val.title_valid = True
        else:
            states["title"] = FieldState.FIELD_INVALID
            errors.append("Title is too short or malformed (Required field)")

        # 2. Price Validation
        price = data.get("price")
        if price is None:
            states["price"] = FieldState.FIELD_NOT_OBSERVED
            val.price_valid = False
        elif "price" in conflicts:
            states["price"] = FieldState.FIELD_CONFLICT
            val.price_valid = False
            errors.append("Price conflict across extraction sources (Required field)")
        elif isinstance(price, (int, float)) and 0.01 <= price <= 10000000:
            states["price"] = FieldState.FIELD_PRESENT_VALID
            val.price_valid = True
        else:
            states["price"] = FieldState.FIELD_INVALID
            val.price_valid = False
            errors.append(f"Price out of realistic range or invalid: {price} (Required field)")

        # 3. Currency Validation
        currency = data.get("currency")
        if currency is None:
            states["currency"] = FieldState.FIELD_NOT_OBSERVED
            val.currency_valid = False
        elif isinstance(currency, str):
            clean_curr = currency.upper().strip()
            if clean_curr in cls.ISO_CURRENCIES:
                states["currency"] = FieldState.FIELD_PRESENT_VALID
                val.currency_valid = True
            else:
                states["currency"] = FieldState.FIELD_INVALID
                val.currency_valid = False
                errors.append(f"Invalid currency code: '{currency}' (Required field)")
        else:
            states["currency"] = FieldState.FIELD_INVALID
            val.currency_valid = False

        # 4. Availability Validation
        availability = data.get("availability")
        if availability is None:
            states["availability"] = FieldState.FIELD_NOT_OBSERVED
            val.availability_valid = False
        elif "availability" in conflicts:
            states["availability"] = FieldState.FIELD_CONFLICT
            val.availability_valid = False
        elif isinstance(availability, str) and availability.strip():
            states["availability"] = FieldState.FIELD_PRESENT_VALID
            val.availability_valid = True
        else:
            states["availability"] = FieldState.FIELD_INVALID
            val.availability_valid = False

        # 5. Brand Validation (Optional field)
        brand = data.get("brand")
        if brand is None:
            states["brand"] = FieldState.FIELD_NOT_OBSERVED
            val.brand_valid = False
        elif isinstance(brand, str) and len(brand.strip()) >= 2:
            states["brand"] = FieldState.FIELD_PRESENT_VALID
            val.brand_valid = True
        else:
            states["brand"] = FieldState.FIELD_INVALID
            val.brand_valid = False

        # 6. SKU / Product ID Validation
        sku = data.get("sku") or data.get("product_id")
        if sku is None:
            states["sku"] = FieldState.FIELD_NOT_OBSERVED
            val.sku_valid = False
        elif isinstance(sku, str) and len(sku.strip()) >= 2:
            states["sku"] = FieldState.FIELD_PRESENT_VALID
            val.sku_valid = True
        else:
            states["sku"] = FieldState.FIELD_INVALID
            val.sku_valid = False

        # 7. GTIN Validation (Strictly Optional)
        gtin = data.get("gtin")
        if gtin is None:
            states["gtin"] = FieldState.FIELD_NOT_OBSERVED
            val.gtin_valid = False
        elif isinstance(gtin, str):
            clean_gtin = re.sub(r"[^\d]", "", gtin)
            if len(clean_gtin) in (8, 12, 13, 14):
                states["gtin"] = FieldState.FIELD_PRESENT_VALID
                val.gtin_valid = True
            else:
                states["gtin"] = FieldState.FIELD_INVALID
                val.gtin_valid = False
                errors.append(f"GTIN digit length {len(clean_gtin)} invalid (Optional field)")
        else:
            states["gtin"] = FieldState.FIELD_INVALID
            val.gtin_valid = False

        # 8. Images Validation (Optional field)
        images = data.get("image_urls", [])
        if not images or not isinstance(images, list) or len(images) == 0:
            states["images"] = FieldState.FIELD_NOT_OBSERVED
            val.images_valid = False
        elif all(isinstance(img, str) and img.startswith("http") for img in images):
            states["images"] = FieldState.FIELD_PRESENT_VALID
            val.images_valid = True
        else:
            states["images"] = FieldState.FIELD_INVALID
            val.images_valid = False

        # 9. Description Validation (Optional field)
        desc = data.get("description")
        if desc is None or not str(desc).strip():
            states["description"] = FieldState.FIELD_NOT_OBSERVED
            val.description_valid = False
        elif isinstance(desc, str) and len(desc.strip()) >= 5:
            states["description"] = FieldState.FIELD_PRESENT_VALID
            val.description_valid = True
        else:
            states["description"] = FieldState.FIELD_INVALID
            val.description_valid = False

        val.field_states = states

        # Calculate Scores
        # Total tracked fields = 9
        tracked_fields = ["title", "price", "currency", "availability", "brand", "sku", "gtin", "images", "description"]
        present_fields = [f for f, s in states.items() if s != FieldState.FIELD_NOT_OBSERVED]
        valid_fields = [f for f, s in states.items() if s == FieldState.FIELD_PRESENT_VALID]

        val.field_completeness = round(len(present_fields) / len(tracked_fields), 3)
        # Validity: ratio of valid fields among fields that the retailer exposed (not penalized for non-exposed fields!)
        val.field_validity = round(len(valid_fields) / max(1, len(present_fields)), 3)
        val.schema_completeness = round((val.field_completeness * 0.4) + (val.field_validity * 0.6), 3)

        # Minimum viable SKU criteria:
        # 1. title_valid
        # 2. price_valid OR availability indicates out-of-stock/discontinued
        # 3. at least one identifier (sku_valid OR gtin_valid OR (brand_valid and title_valid))
        has_identity = val.sku_valid or val.gtin_valid or (val.brand_valid and val.title_valid)
        avail_str = str(data.get("availability") or "").lower()
        is_out_of_stock = any(term in avail_str for term in [
            "outofstock", "out of stock", "unavailable", "disponible", "verfügbar",
            "esgotado", "agotado", "rupture", "discontinued"
        ])
        has_pricing = val.price_valid or (val.availability_valid and is_out_of_stock)

        val.is_valid_sku = bool(val.title_valid and has_pricing and has_identity)
        val.validation_errors = errors
        val.field_conflicts = conflicts

        return val

    @classmethod
    def detect_conflicts(
        cls,
        source_extractions: Dict[str, Dict[str, Any]]
    ) -> Tuple[Dict[str, Dict[str, Any]], bool]:
        """
        Compares extractions from multiple sources (e.g. JSON-LD vs DOM) to find discrepancies.
        Returns (conflicts_dict, has_critical_conflict).
        """
        conflicts: Dict[str, Dict[str, Any]] = {}
        has_critical = False

        if len(source_extractions) < 2:
            return conflicts, False

        # Compare prices
        prices = {}
        for src, data in source_extractions.items():
            if data and data.get("price") is not None:
                prices[src] = data["price"]

        if len(prices) > 1:
            vals = list(prices.values())
            min_p, max_p = min(vals), max(vals)
            if min_p > 0 and ((max_p - min_p) / min_p) > 0.05:
                conflicts["price"] = prices
                has_critical = True

        # Compare availability
        avails = {}
        for src, data in source_extractions.items():
            if data and data.get("availability") is not None:
                avails[src] = data["availability"]

        if len(avails) > 1 and len(set(avails.values())) > 1:
            conflicts["availability"] = avails

        return conflicts, has_critical
