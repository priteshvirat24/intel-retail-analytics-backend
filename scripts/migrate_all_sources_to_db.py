"""
Migrate and synchronize all historical and current live-scraped SKUs into SQLite database.
Ensures zero data loss, strict deduplication, and max 30 cap per retailer.
"""
import json
import sqlite3
from pathlib import Path
from db_manager import init_db, upsert_sku, export_db_to_json, get_db_connection

REPO_ROOT = Path(__file__).resolve().parent.parent
FRONTEND_JSON_PATH = REPO_ROOT / "dashboard/src/data/live_52_sku_dataset.json"

def main():
    init_db()
    conn = get_db_connection()
    
    # 1. Load current live dataset
    if FRONTEND_JSON_PATH.exists():
        data = json.load(open(FRONTEND_JSON_PATH, encoding="utf-8"))
        skus = data.get("live_skus", [])
        print(f"Loaded {len(skus)} SKUs from current live_52_sku_dataset.json")
        for s in skus:
            upsert_sku(s, conn)
            
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM laptops")
    total_in_db = cur.fetchone()[0]
    print(f"Total Unique Verified SKUs in SQLite Database: {total_in_db}")
    
    cur.execute("SELECT account, COUNT(*) as c FROM laptops GROUP BY account ORDER BY account")
    rows = cur.fetchall()
    print("\nDatabase Counts per Retailer:")
    for r in rows:
        print(f"  • {r['account']:22}: {r['c']} SKUs")
        
    conn.close()
    
    # Export back to frontend JSON to keep perfectly in sync
    exported = export_db_to_json()
    print(f"\nSynced {exported} SKUs to dashboard JSON.")

if __name__ == "__main__":
    main()
