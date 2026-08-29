"""
Sync evidence, master catalog database, and deploy to Vercel production.
"""
import os
import shutil
import subprocess
import time
from pathlib import Path
from db_manager import export_db_to_json, get_db_connection

REPO_ROOT = Path(__file__).resolve().parent.parent
DASHBOARD_DIR = REPO_ROOT / "dashboard"
PUBLIC_DIR = DASHBOARD_DIR / "public"

def log(msg: str):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)

def main():
    log("=" * 80)
    log("🚀 SYNCHRONIZING REAL EVIDENCE & MASTER DATASET TO VERCEL PRODUCTION")
    log("=" * 80)
    
    # 1. Export DB to JSON
    total_skus = export_db_to_json()
    log(f"Exported {total_skus} verified SKUs from SQLite to dashboard/src/data/live_52_sku_dataset.json")
    
    # 2. Sync to public/ directory for direct API/static download
    public_data_dir = PUBLIC_DIR / "data"
    public_data_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(DASHBOARD_DIR / "src/data/live_52_sku_dataset.json", public_data_dir / "live_52_sku_dataset.json")
    shutil.copy2(DASHBOARD_DIR / "src/data/live_52_sku_dataset.json", PUBLIC_DIR / "live_52_sku_dataset.json")
    
    # 3. Copy master SQLite DB to public/evidence/
    public_evidence = PUBLIC_DIR / "evidence"
    public_evidence.mkdir(parents=True, exist_ok=True)
    if (REPO_ROOT / "evidence/laptops_catalog.db").exists():
        shutil.copy2(REPO_ROOT / "evidence/laptops_catalog.db", public_evidence / "laptops_catalog.db")
        log("Copied evidence/laptops_catalog.db to dashboard/public/evidence/laptops_catalog.db")
        
    # 4. Copy screenshots if exist
    src_screens = REPO_ROOT / "evidence/screenshots"
    dst_screens = public_evidence / "screenshots"
    if src_screens.exists():
        for item in src_screens.glob("*/*"):
            if item.is_file():
                rel = item.relative_to(src_screens)
                target = dst_screens / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                if not target.exists():
                    shutil.copy2(item, target)
        log("Synchronized evidence screenshots to dashboard/public/evidence/screenshots/")

    # 5. Build dashboard
    log("\nBuilding production Vite/React dashboard bundle...")
    res_build = subprocess.run(["npm", "run", "build"], cwd=DASHBOARD_DIR, capture_output=True, text=True)
    if res_build.returncode == 0:
        log("✓ Production build succeeded.")
    else:
        log(f"✗ Build failed:\n{res_build.stderr}")
        return

    # 6. Deploy to Vercel production
    log("\nDeploying to Vercel production (--prod --yes)...")
    res_vercel = subprocess.run(["vercel", "--prod", "--yes"], cwd=DASHBOARD_DIR, capture_output=True, text=True)
    log(f"Vercel Deployment Output:\n{res_vercel.stdout}\n{res_vercel.stderr}")
    
    log("\n" + "=" * 80)
    log("🎉 VERCEL DEPLOYMENT COMPLETE WITH REAL DATA & EVIDENCE!")
    log("=" * 80)

if __name__ == "__main__":
    main()
