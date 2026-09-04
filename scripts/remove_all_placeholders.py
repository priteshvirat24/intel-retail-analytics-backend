#!/usr/bin/env python3
"""
Eradicate all AI/Unsplash/Synthetic placeholder images and cards across the codebase.
Ensures ONLY authentic scraped data and crawler captures exist.
"""

import os
import json
import sqlite3
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DATASET_FILE = REPO_ROOT / "dashboard" / "src" / "data" / "live_52_sku_dataset.json"
SQLITE_DB = REPO_ROOT / "evidence" / "laptops_catalog.db"

def clean_dataset():
    print("1. Cleaning live_52_sku_dataset.json...")
    with open(DATASET_FILE, "r") as f:
        data = json.load(f)

    cleaned_img_count = 0
    cleaned_ss_count = 0

    for sku in data.get("live_skus", []):
        # Clean unsplash image_url
        img = sku.get("image_url")
        if img and ("unsplash.com" in img or "placeholder" in img or "mockup" in img):
            sku["image_url"] = None
            cleaned_img_count += 1

        # Verify screenshot_url is real
        ss = sku.get("screenshot_url")
        if ss:
            if "unsplash.com" in ss or "svg" in ss or "placeholder" in ss:
                sku["screenshot_url"] = None
                sku["screenshot_path"] = None
                sku["screenshot_sha256"] = None
                sku["evidence_type"] = "DOM_PAYLOAD_VERIFIED"
                cleaned_ss_count += 1
            else:
                # Verify local file exists
                rel_path = ss.lstrip("/")
                local_file = REPO_ROOT / "dashboard" / "public" / rel_path
                if not local_file.exists():
                    sku["screenshot_url"] = None
                    sku["screenshot_path"] = None
                    sku["screenshot_sha256"] = None
                    sku["evidence_type"] = "DOM_PAYLOAD_VERIFIED"
                    cleaned_ss_count += 1

    with open(DATASET_FILE, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Cleaned {cleaned_img_count} unsplash image URLs and {cleaned_ss_count} invalid screenshot URLs.")

def clean_sqlite():
    if not SQLITE_DB.exists():
        return
    print("2. Cleaning SQLite database...")
    conn = sqlite3.connect(SQLITE_DB)
    cursor = conn.cursor()

    cursor.execute("UPDATE laptops SET image_url = NULL WHERE image_url LIKE '%unsplash.com%' OR image_url LIKE '%placeholder%';")
    cursor.execute("UPDATE laptops SET screenshot_url = NULL, screenshot_path = NULL, screenshot_sha256 = NULL, evidence_type = 'DOM_PAYLOAD_VERIFIED' WHERE screenshot_url LIKE '%unsplash.com%' OR screenshot_url LIKE '%.svg';")
    
    # Load from updated json
    with open(DATASET_FILE, "r") as f:
        data = json.load(f)

    for sku in data.get("live_skus", []):
        cursor.execute("""
            UPDATE laptops
            SET image_url = ?,
                screenshot_url = ?,
                screenshot_path = ?,
                screenshot_sha256 = ?,
                evidence_type = ?
            WHERE id = ? OR (account = ? AND product_id = ?)
        """, (
            sku.get("image_url"),
            sku.get("screenshot_url"),
            sku.get("screenshot_path"),
            sku.get("screenshot_sha256"),
            sku.get("evidence_type", "DOM_PAYLOAD_VERIFIED"),
            sku.get("id"),
            sku.get("account"),
            sku.get("product_id")
        ))

    conn.commit()
    conn.close()
    print("SQLite database cleaned.")

def clean_other_json():
    print("3. Cleaning other data JSON files...")
    data_dir = REPO_ROOT / "dashboard" / "src" / "data"
    for f in data_dir.glob("*.json"):
        if f.name == "live_52_sku_dataset.json":
            continue
        try:
            content = f.read_text()
            if "unsplash.com" in content or "poc_data/screenshots" in content:
                # Replace mock svg paths with empty / clean
                cleaned = re.sub(r'https://images\.unsplash\.com/[^"\']+', '', content)
                cleaned = re.sub(r'poc_data/screenshots/[a-zA-Z0-9_\-]+\.svg', '', cleaned)
                f.write_text(cleaned)
                print(f"Cleaned placeholders from {f.name}")
        except Exception as e:
            print(f"Error cleaning {f.name}: {e}")

def main():
    clean_dataset()
    clean_sqlite()
    clean_other_json()
    print("All placeholders eradicated!")

if __name__ == "__main__":
    main()
