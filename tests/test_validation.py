import pytest
from app.extraction.validators import ExtractionValidator
from app.models.product import FieldState


def test_validator_detects_valid_sku():
    data = {
        "title": "MacBook Pro 16-inch M3 Max",
        "price": 3499.00,
        "currency": "USD",
        "availability": "InStock",
        "brand": "Apple",
        "sku": "MBP16-M3MAX",
        "gtin": "195949012345",
        "image_urls": ["https://images.example.com/mbp.jpg"],
        "description": "Apple MacBook Pro 16 with 36GB unified memory."
    }
    val = ExtractionValidator.validate_fields(data, expected_currency="USD")
    assert val.title_valid is True
    assert val.price_valid is True
    assert val.currency_valid is True
    assert val.availability_valid is True
    assert val.brand_valid is True
    assert val.sku_valid is True
    assert val.gtin_valid is True
    assert val.images_valid is True
    assert val.description_valid is True
    assert val.is_valid_sku is True
    assert val.schema_completeness == 1.0
    assert val.field_states["title"] == FieldState.FIELD_PRESENT_VALID
    assert val.field_states["price"] == FieldState.FIELD_PRESENT_VALID


def test_validator_discriminates_not_present_vs_invalid():
    data = {
        "title": "MacBook Pro 16-inch M3 Max",
        "price": -10.0,  # Invalid
        # brand is omitted -> NOT_PRESENT
    }
    val = ExtractionValidator.validate_fields(data, expected_currency="USD")
    assert val.field_states["price"] == FieldState.FIELD_INVALID
    assert val.field_states["brand"] == FieldState.FIELD_NOT_PRESENT
    assert val.price_valid is False
    assert val.brand_valid is False


def test_validator_rejects_bot_titles():
    data = {
        "title": "Robot Check - Amazon.com",
        "price": 100.0,
        "sku": "123"
    }
    val = ExtractionValidator.validate_fields(data, expected_currency="USD")
    assert val.title_valid is False
    assert val.is_valid_sku is False
    assert val.field_states["title"] == FieldState.FIELD_INVALID


def test_validator_detects_price_and_availability_conflicts():
    sources = {
        "JSON_LD": {"price": 100.0, "availability": "InStock"},
        "DOM": {"price": 140.0, "availability": "OutOfStock"}
    }
    conflicts, is_critical = ExtractionValidator.detect_conflicts(sources)
    assert is_critical is True
    assert "price" in conflicts
    assert "availability" in conflicts
