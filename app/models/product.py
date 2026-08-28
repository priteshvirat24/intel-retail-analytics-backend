from enum import Enum
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime, timezone


class FieldState(str, Enum):
    FIELD_PRESENT_VALID = "FIELD_PRESENT_VALID"
    FIELD_NOT_PRESENT = "FIELD_NOT_PRESENT"
    FIELD_NOT_OBSERVED = "FIELD_NOT_PRESENT"  # Alias for backward compatibility
    FIELD_EXTRACTION_FAILED = "FIELD_EXTRACTION_FAILED"
    FIELD_INVALID = "FIELD_INVALID"
    FIELD_CONFLICT = "FIELD_CONFLICT"


# Explicit Schema Policy
REQUIRED_SCHEMA_FIELDS = ["title", "price", "currency", "availability", "sku"]
OPTIONAL_SCHEMA_FIELDS = ["brand", "gtin", "images", "description", "model", "rating", "review_count", "seller"]


class FieldValidation(BaseModel):
    title_valid: bool = False
    price_valid: bool = False
    currency_valid: bool = False
    availability_valid: bool = False
    brand_valid: bool = False
    sku_valid: bool = False
    gtin_valid: bool = False
    images_valid: bool = False
    description_valid: bool = False

    # Granular 5-state status per field
    field_states: Dict[str, FieldState] = Field(default_factory=dict)

    # Score Metrics
    field_completeness: float = Field(default=0.0, description="Ratio of present fields (0.0 to 1.0)")
    field_validity: float = Field(default=0.0, description="Ratio of valid fields among exposed fields (0.0 to 1.0)")
    schema_completeness: float = Field(default=0.0, description="Overall schema completeness score (0.0 to 1.0)")
    is_valid_sku: bool = Field(default=False, description="Whether product meets minimum viable SKU requirements")
    validation_errors: List[str] = Field(default_factory=list)
    field_conflicts: Dict[str, Dict[str, Any]] = Field(default_factory=dict, description="Fields where multiple extractors disagreed")


class NormalizedProduct(BaseModel):
    retailer: str
    country: str
    source_url: str
    canonical_url: Optional[str] = None
    product_id: Optional[str] = None
    sku: Optional[str] = None
    gtin: Optional[str] = None
    brand: Optional[str] = None
    model: Optional[str] = None
    title: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    currency: Optional[str] = None
    availability: Optional[str] = None  # e.g., "InStock", "OutOfStock", "PreOrder", "Discontinued"
    stock_status: Optional[str] = None  # e.g., "In Stock", "Only 2 left", "Out of stock"
    rating: Optional[float] = None
    review_count: Optional[int] = None
    image_urls: List[str] = Field(default_factory=list)
    product_attributes: Dict[str, Any] = Field(default_factory=dict)
    seller: Optional[str] = None
    shipping_information: Optional[str] = None
    product_template_id: Optional[str] = Field(default=None, description="Deterministic structural DOM template identifier")
    product_template_signature: Optional[str] = Field(default=None, description="Detailed structural signature string")
    product_template_framework: Optional[str] = Field(default=None, description="Framework detected (nextjs, nuxtjs, etc.)")
    timestamp: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    extraction_method: str = Field(default="GENERIC", description="JSON_LD, EMBEDDED_JSON, DOM, ADAPTER, etc.")
    crawler_strategy: str = Field(default="HTTP", description="HTTP, PLAYWRIGHT, FIRECRAWL, ADAPTER")
    confidence: float = Field(default=0.0, ge=0.0, le=1.0)
    validation: Optional[FieldValidation] = None
