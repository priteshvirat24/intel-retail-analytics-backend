"""
Script: run_pc_intel_poc_scraper.py
Entrypoint for running the one-time, strictly capped Bright Data scraper for the PC Intelligence POC.
"""
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from poc_scraping.brightdata_collector import BrightDataPocCollector


def main():
    print("=" * 80)
    print(" 🚀 INITIATING ONE-TIME POC BATCH SCRAPE")
    print("=" * 80)
    dataset = BrightDataPocCollector.collect_dataset()
    print("\n✅ Scrape complete! All products, search SOV data, and banners cached locally.")


if __name__ == "__main__":
    main()
