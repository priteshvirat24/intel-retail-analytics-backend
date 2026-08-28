# Intel Scorecards Online Tracking Platform POC (2024-2025 Architecture) — Full Walkthrough

## Executive Summary

The **Intel Scorecards Online Tracking Platform POC** has been fully extended and structured according to the official **Intel Scorecards Program 2024-2025** documentation and data definitions.

The application models the core analytical structure:
$$\text{ACCOUNT} \longrightarrow \text{COUNTRY} \longrightarrow \text{DATE} \longrightarrow \text{SOS / SOV} \longrightarrow \text{PRODUCT} \longrightarrow \text{LISTING / SEARCH RESULT} \longrightarrow \text{PDP} \longrightarrow \text{EVIDENCE} \longrightarrow \text{S1 / S2} \longrightarrow \text{P1..P5} \longrightarrow \text{LISTING / PDP SCORE} \longrightarrow \text{OVERALL SCORE}$$

---

## 1. Information Architecture & Navigation Hierarchy

```
OVERVIEW
  ├── Core Scorecards Program Purpose (Benchmarking, Presence Score, Content Quality, Badges, Rich Media)
  ├── Current Live POC Metrics (11 Top KPIs, Stacked SOS, Segment Mix)
  ├── Historical Program Reference Card (2024 vs 2025)
  └── Account Coverage Summary Table

SCORECARDS
  ├── Account Scorecards (Table with drilldown: Account → Product Count → Product Table → Product → Evidence → Scores)
  ├── Product Scorecards (Product cards with Header, Price, Specs, Device, Classification, S1..P5 Scoring)
  ├── Score Distribution (Distribution histogram across 0-100 numeric scores)
  └── Score Trends (Month-over-month account compliance score evolution)

SHARE OF SHELF (SOS)
  ├── SOS Overview (First 2 Category Pages Only, Stacked Platform Distribution, Overall Shelf Mix)
  ├── Retailer (Account-level first-2-page SOS % breakdown)
  ├── Country (Geographic market SOS)
  ├── OEM (OEM manufacturer shelf volume rankings)
  ├── Product (SOS Product Eligibility: YES / NO on every product)
  └── Trend (Quarterly SOS progression)

SHARE OF VOICE (SOV)
  ├── SOV Overview (Account × Keyword Intel Presence Heatmap)
  ├── Keywords (Top keywords by search volume, Intel presence %, competitor-dominant queries)
  ├── Retailer (Account-level search visibility)
  ├── Country (Geographic search visibility)
  ├── Product (Top-ranked SKUs in keyword search)
  ├── Search Results (Detailed table with ALL Harvested: 12,842 vs Scoring Eligible: 1,946 filter)
  └── Trend (Monthly SOV trajectory)

PRODUCTS
  ├── Product Explorer (Master 40+ column catalog table with live search, sorting, and CSV export)
  ├── Product Detail (Detailed hardware spec cards)
  ├── Product Comparison (Head-to-head like-for-like matching)
  └── Price Intelligence (In-season price corridors & historical price tracking)

RETAILERS
  ├── Account Explorer (Channel overview cards)
  ├── Account Detail (Deep account workspace with S1..P5 scoreboards and monitored inventory)
  ├── Account Performance (Rankings by Overall, Listing, PDP, S1..P5, SOS, SOV)
  └── Account History (2024 Account Changes vs 2025 Account Changes with addition/removal records)

BANNERS
  ├── Banner Overview (Hero placement gallery with $-off tags, destination links, EVO/Gaming/Premier flags)
  ├── Banner Explorer (Channel placement breakdown)
  └── Banner Evidence (Captured screenshot assets)

EVO
  ├── EVO Overview (55.6% adoption rate, +33.7% price premium)
  ├── EVO Products (Certified SKU gallery)
  ├── EVO by Retailer (Adoption rate by channel)
  └── EVO by OEM (Adoption rate by manufacturer)

EVIDENCE
  ├── Screenshots (Visual screenshot inspector for Category Listings, PDPs, and Hero Banners)
  ├── Source Pages (Listing page vs PDP vs Search result source URLs)
  └── Audit Evidence (Direct attachment to score components: click S1, S2, P1, P2, P3, P4, P5 to view raw DOM evidence)

DATA QUALITY
  └── 18-Attribute Field Completeness Matrix (100%), Duplicate Detection (0 Dupes), URL Health

SCRAPE CENTER
  └── Request Queue with failure taxonomy, Cost Guardrails summary, "Run Sample" (Max 3)

BRIGHT DATA USAGE (COST CENTER)
  └── Extraction Fallback Waterfall (1,000 URLs → 740 cached → 180 existing → 55 SDK → 20 SERP → 5 Bright Data)

REPORTS
  └── 8 Program Deliverables with On-Demand Preview & CSV, XLSX, PDF Export

PROGRAM HISTORY
  ├── 2024 vs 2025 Comparison (Factual metrics comparison table & volume charts)
  ├── 2024 Account History (49 initial, 52 March onward; additions & removals)
  ├── 2025 Account History (50 accounts tiered; OEM stores removed; BIC Camera, Harvey Norman, NBB added)
  └── Tracking Frequency Model (22 Monthly, 28 Mid-Quarter, 50 Quarterly)
```

---

## 2. Core Methodology Verifications

1. **Share of Shelf (SOS)**:
   - Evaluates **strictly the first two category pages**.
   - Explicitly displays `"Share of Shelf: First two category pages"`.
   - Every product has an `"SOS Eligible: YES / NO"` indicator.

2. **Share of Voice (SOV)**:
   - Preserves all harvested results (`12,842`).
   - Restricts scoring eligibility to `page_rank 1-2` AND `keyword_rank 1-20` (`1,946` scoring-eligible results).
   - Allows toggling between all harvested search results and scoring-eligible results.

3. **Scoring Breakdown & Aggregation**:
   - `s1`: Listing page title (0-100)
   - `s2`: Listing page badge (0-100)
   - `p1`: PDP title (0-100)
   - `p2`: PDP badge (0-100)
   - `p3`: Specification presence (0-100)
   - `p4`: Intel-led Rich Media / A+ content (0-100)
   - `p5`: OEM Rich Media (0-100)
   - `listing_s = round((s1 + s2) / 2)`
   - `details_p = round((p1 + p2 + p3 + p4 + p5) / 5)`
   - `Overall = round((listing_s + details_p) / 2)`

4. **Evidence Attachment**:
   - Clicking any score component (S1, S2, P1, P2, P3, P4, P5) opens the exact extracted DOM evidence string, screenshot, live URL, timestamp, and acquisition method.

5. **Historical Program Separation**:
   - 2024 and 2025 historical program totals are clearly labeled with `"HISTORICAL PROGRAM DATA"` and never mixed with `"CURRENT POC DATA"`.

---

## 3. Live Server Endpoint

The application is running live locally:
* **[http://localhost:5173/](http://localhost:5173/)**
