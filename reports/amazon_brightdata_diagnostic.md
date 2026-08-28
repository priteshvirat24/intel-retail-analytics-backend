# Dedicated Amazon Specialized Scraper & Marketplace Diagnostic Report

**Diagnostic Suite**: Dedicated Multi-Marketplace Amazon Laptop Benchmark
**Execution Timestamp**: 2026-08-25 09:30:15 UTC
**Infrastructure**: Bright Data Web Unlocker, Managed Browser, Regional Egress Routing

---

## 1. Executive Summary Table

| Marketplace | Country ISO | Search Discovery | Top ASIN | Product Scrape | Specs Extracted | Classification | Genuine Laptop? | Web Unlocker | Browser API |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Amazon United States** | `US` | `SUCCESS` (4 found) | `B0GQB1C381` | `SUCCESS` | 74 fields | Score: 1.0 | **YES** | HTTP 200 (OK) | HTTP 200 (OK) |
| **Amazon United Kingdom** | `GB` | `SUCCESS` (5 found) | `B0C9LZFN32` | `SUCCESS` | 79 fields | Score: 1.0 | **YES** | HTTP 200 (OK) | HTTP 200 (OK) |
| **Amazon Germany** | `DE` | `SUCCESS` (4 found) | `B0H7JDLNCR` | `SUCCESS` | 51 fields | Score: 1.0 | **YES** | HTTP 200 (OK) | HTTP 200 (OK) |
| **Amazon India** | `IN` | `SUCCESS` (5 found) | `B0G2MT8YVV` | `SUCCESS` | 66 fields | Score: 1.0 | **YES** | HTTP 200 (OK) | HTTP 200 (OK) |

---

## 2. Detailed Marketplace Diagnostics

### Amazon United States (`US`)
- **Domain**: `https://www.amazon.com`
- **Search Discovery Status**: SUCCESS
- **Candidates Identified**: 4
- **Top Candidate URL**: https://www.amazon.com/HP-OmniBook-Touchscreen-Windows-16-by0199nr/dp/B0GQB1C381/ref=sr_1_2
- **Top ASIN**: `B0GQB1C381`
- **Extracted Title**: HP OmniBook 3 16 inch Laptop PC, 2K Touchscreen, AMD Ryzen 3 30, 8 GB RAM, 256 GB SSD, AMD Radeon 610M GPU, Windows 11 Home, Mica Silver, 16-by0199nr
- **Brand**: HP
- **Price**: 549.99
- **Hardware Specs Extracted**: 74 attributes
- **Strict Laptop Validation**: **VERIFIED GENUINE LAPTOP** (Score: 1.0)
- **Web Unlocker Verification**: HTTP 200 (OK)
- **Browser API Verification**: HTTP 200 (OK)
- **Total Round-Trip Latency**: 47414.08 ms

### Amazon United Kingdom (`GB`)
- **Domain**: `https://www.amazon.co.uk`
- **Search Discovery Status**: SUCCESS
- **Candidates Identified**: 5
- **Top Candidate URL**: https://www.amazon.co.uk/Lenovo-IdeaPad-Slim-Chromebook-Laptop/dp/B0C9LZFN32/ref=sr_1_2
- **Top ASIN**: `B0C9LZFN32`
- **Extracted Title**: Lenovo IdeaPad Slim 3 Chromebook | 14 Inch FHD Laptop | MediaTek Kompanio 520 | 4GB RAM | 64GB eMMC | Chrome OS | Abyss Blue
- **Brand**: Lenovo
- **Price**: 149.97
- **Hardware Specs Extracted**: 79 attributes
- **Strict Laptop Validation**: **VERIFIED GENUINE LAPTOP** (Score: 1.0)
- **Web Unlocker Verification**: HTTP 200 (OK)
- **Browser API Verification**: HTTP 200 (OK)
- **Total Round-Trip Latency**: 52072.56 ms

### Amazon Germany (`DE`)
- **Domain**: `https://www.amazon.de`
- **Search Discovery Status**: SUCCESS
- **Candidates Identified**: 4
- **Top Candidate URL**: https://www.amazon.de/Dell-Latitude-i5-1135G7-Antiviren-Software-General%C3%BCberholt/dp/B0H7JDLNCR/ref=sr_1_9
- **Top ASIN**: `B0H7JDLNCR`
- **Extracted Title**: Dell Latitude 5320 2-in-1 13,3 Zoll Full HD Laptop Intel Core i5-1135G7@ bis zu 4,2 GHz 16 GB 512 GB SSD mit Windows 11 Pro & GRATIS Antiviren-Software inkl. 12 Monate Garantie (Generalüberholt)
- **Brand**: Besuche den Amazon Renewed-Store
- **Price**: 29990.0
- **Hardware Specs Extracted**: 51 attributes
- **Strict Laptop Validation**: **VERIFIED GENUINE LAPTOP** (Score: 1.0)
- **Web Unlocker Verification**: HTTP 200 (OK)
- **Browser API Verification**: HTTP 200 (OK)
- **Total Round-Trip Latency**: 48156.84 ms

### Amazon India (`IN`)
- **Domain**: `https://www.amazon.in`
- **Search Discovery Status**: SUCCESS
- **Candidates Identified**: 5
- **Top Candidate URL**: https://www.amazon.in/Neopticon-Student-Celeron-Expandable-Graphics/dp/B0G2MT8YVV/ref=sr_1_5
- **Top ASIN**: `B0G2MT8YVV`
- **Extracted Title**: EBook 11.6" HD Laptop | Best Student & Office Work Laptop | Celeron N4020 | 4GB DDR4 | 128GB eMMC + M.2 SSD Expandable Slot | Win 11 Home |31Wh Battery | UHD Graphics 600 | Black
- **Brand**: Neopticon Store
- **Price**: 14800.0
- **Hardware Specs Extracted**: 66 attributes
- **Strict Laptop Validation**: **VERIFIED GENUINE LAPTOP** (Score: 1.0)
- **Web Unlocker Verification**: HTTP 200 (OK)
- **Browser API Verification**: HTTP 200 (OK)
- **Total Round-Trip Latency**: 52998.45 ms

---

## 3. Failure Mode & Root Cause Attribution Matrix

| Area | Potential Failure Mode | Diagnostic Result & Fix |
| :--- | :--- | :--- |
| **Credentials** | Missing or invalid `BRIGHTDATA_API_KEY` | Cleanly read from environment; masked across all telemetry. |
| **Country Routing** | Geoblock / Non-local marketplace redirect | Native ISO flags (`country-us`, `country-gb`, `country-de`, `country-in`) ensure local regional landing pages. |
| **ASIN Relevance** | Accessories or non-laptop items in search | Strict negative keyword filters reject bags, cases, chargers, and keyboards at candidate discovery. |
| **Specs Parsing** | Dynamic Amazon DOM layout variants | Multi-table selectors inspect `#productDetails_techSpec_section_1` and `.po-table` to extract CPU, RAM, and Storage. |
