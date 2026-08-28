"""
Daily Price & Promotion Feed Exporter.
Generates comprehensive SKU-level CSV/JSON data feeds matching the SOW §1.5 Product Data Attributes schema.
"""
import csv
import json
import hashlib
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_DATASET_PATH = PROJECT_ROOT / "dashboard" / "src" / "data" / "live_52_sku_dataset.json"
DEFAULT_FEEDS_DIR = PROJECT_ROOT / "reports" / "daily_feeds"

# Comprehensive SOW §1.5 Canonical Attribute Columns
FEED_HEADERS = [
    "retailer",
    "country",
    "country_iso",
    "account",
    "site_type",
    "product_id",
    "product_title",
    "product_description",  # SOW-mandated attribute (Note: 0% populated in raw source)
    "oem",
    "model_and_series",
    "processor_brand",
    "processor_series",
    "processor_model",
    "processor_number",
    "processor_generation",
    "graphics_card",
    "form_factor",
    "screen_size",
    "screen_type",          # SOW-mandated attribute (Note: 0% populated in raw source)
    "ram_gb",
    "storage_gb",
    "storage_type",
    "operating_system",
    "original_price_local",
    "selling_price_local",
    "usd_original_price",
    "usd_selling_price",
    "discount_amount_local",
    "discount_pct",
    "currency",
    "price_history",        # SOW-mandated attribute (Note: 0% populated in raw source)
    "availability",
    "product_url",
    "feed_timestamp",
    "feed_date",
]


class DailyFeedExporter:
    """Exports raw SKU pricing, promotion, and hardware configuration into versioned daily feeds."""

    @classmethod
    def load_dataset(cls, dataset_path: Optional[Path] = None) -> List[Dict[str, Any]]:
        target_path = dataset_path or DEFAULT_DATASET_PATH
        if not target_path.exists():
            raise FileNotFoundError(f"Dataset not found at: {target_path}")
        with open(target_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict):
            return data.get("live_skus", data.get("products", []))
        if isinstance(data, list):
            return data
        return []

    @classmethod
    def normalize_sku_row(cls, sku: Dict[str, Any], timestamp_str: str, date_str: str) -> Dict[str, Any]:
        """Maps a raw SKU dictionary to the canonical SOW §1.5 schema."""
        orig_price = sku.get("original_price") or sku.get("price") or 0.0
        sell_price = sku.get("selling_price") or orig_price or 0.0
        disc_pct = sku.get("discount_pct")
        if disc_pct is None and orig_price > 0 and sell_price < orig_price:
            disc_pct = round(((orig_price - sell_price) / orig_price) * 100, 2)
        disc_amt = round(orig_price - sell_price, 2) if orig_price >= sell_price else 0.0

        usd_orig = sku.get("usd_original_price") or sku.get("price_usd") or orig_price
        usd_sell = sku.get("usd_selling_price") or usd_orig

        return {
            "retailer": sku.get("retailer") or sku.get("account") or "Unknown Retailer",
            "country": sku.get("country") or "Unknown Country",
            "country_iso": sku.get("country_iso") or sku.get("country", "")[:2].upper(),
            "account": sku.get("account") or sku.get("retailer") or "Unknown",
            "site_type": sku.get("site_type") or ("1P_RETAILER" if sku.get("3p_1p") == "1P" else "MARKETPLACE"),
            "product_id": sku.get("product_id") or sku.get("sku") or "",
            "product_title": sku.get("product_title") or sku.get("title") or "",
            "product_description": sku.get("product_description") or sku.get("description") or "",  # 0% populated
            "oem": sku.get("oem") or sku.get("brand") or "Unknown",
            "model_and_series": sku.get("model") or sku.get("model_series") or "",
            "processor_brand": sku.get("processor") or sku.get("processor_brand") or "",
            "processor_series": sku.get("processor_model") or "",
            "processor_model": sku.get("processor_model") or "",
            "processor_number": sku.get("number") or "",
            "processor_generation": sku.get("gen") or "",
            "graphics_card": sku.get("graphic_card") or sku.get("graphics_card") or "",
            "form_factor": sku.get("form_factor") or "Laptop",
            "screen_size": sku.get("screen_size") or "",
            "screen_type": sku.get("screen_type") or "",  # 0% populated
            "ram_gb": sku.get("ram") or "",
            "storage_gb": sku.get("storage") or "",
            "storage_type": sku.get("storage_type") or "",
            "operating_system": sku.get("operating_system") or "",
            "original_price_local": orig_price,
            "selling_price_local": sell_price,
            "usd_original_price": usd_orig,
            "usd_selling_price": usd_sell,
            "discount_amount_local": disc_amt,
            "discount_pct": disc_pct if disc_pct is not None else 0.0,
            "currency": sku.get("currency") or "USD",
            "price_history": json.dumps(sku.get("price_history", [])) if sku.get("price_history") else "",  # 0% populated
            "availability": sku.get("availability") or sku.get("stock_status") or "InStock",
            "product_url": sku.get("product_url") or sku.get("source_url") or "",
            "feed_timestamp": timestamp_str,
            "feed_date": date_str,
        }

    @classmethod
    def generate_daily_feed(
        cls,
        products: Optional[List[Dict[str, Any]]] = None,
        output_dir: Optional[Path] = None,
        timestamp: Optional[datetime] = None,
    ) -> Tuple[Path, str, int]:
        """
        Generates a versioned daily price and promotion CSV feed.
        Returns (feed_file_path, file_sha256, record_count).
        """
        now = timestamp or datetime.now(timezone.utc)
        ts_str = now.isoformat()
        date_str = now.strftime("%Y-%m-%d")
        ts_compact = now.strftime("%Y%m%d_%H%M%S")

        target_dir = output_dir or DEFAULT_FEEDS_DIR
        target_dir.mkdir(parents=True, exist_ok=True)

        filename = f"intel_daily_price_promotion_feed_{ts_compact}.csv"
        feed_path = target_dir / filename

        items = products if products is not None else cls.load_dataset()
        normalized_rows = [cls.normalize_sku_row(p, ts_str, date_str) for p in items]

        with open(feed_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FEED_HEADERS)
            writer.writeheader()
            writer.writerows(normalized_rows)

        # Also write / update latest symlink or copy
        latest_path = target_dir / "intel_daily_price_promotion_feed_latest.csv"
        try:
            if latest_path.exists() or latest_path.is_symlink():
                latest_path.unlink()
            latest_path.symlink_to(feed_path.name)
        except Exception:
            # Fallback for systems without symlink permissions
            with open(latest_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=FEED_HEADERS)
                writer.writeheader()
                writer.writerows(normalized_rows)

        # Compute SHA-256
        sha256 = hashlib.sha256(feed_path.read_bytes()).hexdigest()

        return feed_path, sha256, len(normalized_rows)
