# Phase 3A: Forensic Recovery & Diagnostic Benchmark Report

> **Execution Date**: `2026-08-23 10:35:00 UTC`  
> **Run ID**: `run_20260823_phase3a_forensic`  
> **Referenced Baseline**: `run_20260823_082231_88e466` (Phase 2 Benchmark)  
> **Evaluation Mode**: 100% Real-World Empirical Audit (Zero Mocks / Zero Synthetic Data)

---

## 1. Phase 2 Baseline Summary

The Phase 2 full benchmark evaluated **52 targets** across **23 countries** with up to **1,040 requested SKU attempts**. The empirical results observed were:

- **Total SKU Attempts**: `1,040` actual attempts
- **Initial Validated Product Success**: `0` products (`0.0%`)
- **Initial Failure Distribution**:
  - `EMPTY_RESPONSE`: `718 / 1,040` (`69.04%`)
  - `HTTP_404_NOT_FOUND`: `132 / 1,040` (`12.69%`)
  - `CAPTCHA_CHALLENGE`: `74 / 1,040` (`7.12%`)
  - `BOT_PROTECTION`: `64 / 1,040` (`6.15%`)
  - `DNS_RESOLUTION_FAILED / TIMEOUT`: `44 / 1,040` (`4.23%`)
  - `REQUIRED_FIELD_MISSING`: `8 / 1,040` (`0.77%`)
- **Recovered Usable Structural HTML Responses**: `13` products
- **Candidate Products Reaching Extraction**: `8` products
- **Products Passing Initial Product Validation**: `0` products

---

## 2. Empty Response & HTML Forensics (Audit of 13 Responses)

A forensic audit was performed across all **13 SKU responses** where structural HTML was captured during Phase 2. Detailed audit data is preserved in [`html_forensic_audit.csv`](file:///Users/priteshhome/crawl/reports/runs/run_20260823_phase3a_forensic/html_forensic_audit.csv).

### Forensic Breakdown of the 13 Responses:
| Target ID | Retailer | SKU ID | Content Length | DOM Template | Diagnosis | Root Cause Analysis |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| `amazon-br` | Amazon | `B09G9FPHY6` | 615,769 B | Yes (`#dp-container`) | `PRODUCT_DOM_ACCESSIBLE` | Real Apple iPad page. Contained Portuguese price formatting (`R$ 2.690,00`) and out-of-stock availability text. |
| `amazon-es` | Amazon | `B0CL6LMC9N` | 1,045,898 B | Yes (`#dp-container`) | `PRODUCT_DOM_ACCESSIBLE` | Real Cowhide Rug page. Out-of-stock item ("No disponible") without price element. |
| `amazon-de` | Amazon | `B0CL6LMC9N` | 878,102 B | Yes (`#dp-container`) | `PRODUCT_DOM_ACCESSIBLE` | Real Cowhide Rug page. Out-of-stock item ("Derzeit nicht verfügbar") without price element. |
| `amazon-de` | Amazon | `B09G91LXFP` | 1,065,464 B | Yes (`#dp-container`) | `PRODUCT_DOM_ACCESSIBLE` | Real Apple iPad Mini page. Out-of-stock item ("Derzeit nicht verfügbar") with full description & ASIN. |
| `reliancedigital-in` | Reliance Digital | `sku_0012` | 63,701 B | No | `SPA_ROOT_SHELL` | Angular/React root client container; redirected to generic homepage. |
| `tmall-cn` | Tmall | `sku_0020` | 161,727 B | No | `PRODUCT_NOT_FOUND` | Chinese 404 error redirect page (`您查看的页面找不到了`). |
| `tmall-cn` | Китай | `sku_0016` | 162,014 B | No | `PRODUCT_NOT_FOUND` | Chinese 404 error redirect page (`您查看的页面找不到了`). |
| `tmall-cn` | Tmall | `sku_0015` | 162,013 B | No | `PRODUCT_NOT_FOUND` | Chinese 404 error redirect page (`您查看的页面找不到了`). |
| `amazon-es` | Amazon | `B09BRF4N2V` | 468,417 B | No | `SPA_ROOT_SHELL` | Partial dynamic render shell missing product container. |
| `flipkart-in` | Flipkart | `itm00000005` | 354,419 B | No | `BOT_CHALLENGE` | CSRF challenge with generic search header. |
| `flipkart-in` | Flipkart | `itm00000003` | 354,419 B | No | `BOT_CHALLENGE` | CSRF challenge with generic search header. |
| `flipkart-in` | Flipkart | `itm00000020` | 354,818 B | No | `BOT_CHALLENGE` | CSRF challenge with generic search header. |
| `flipkart-in` | Flipkart | `itm00000018` | 354,818 B | No | `BOT_CHALLENGE` | CSRF challenge with generic search header. |

---

## 3. Validation False-Negative Analysis

An audit of the **8 extracted products** from Phase 2 revealed a significant **Validator-Induced False Negative** defect:

1. **International Decimal Formats**: European and Brazilian prices (e.g. `R$ 2.690,00` or `349,00 €`) were converted to `2.690.00` by English-only string replacement, failing float casting silently.
2. **International Out-of-Stock Statuses**: Amazon DE, ES, and BR returned valid out-of-stock catalog products ("Derzeit nicht verfügbar", "No disponible", "Não disponível"). The initial validator only checked English `"out of stock"` and rejected valid out-of-stock items for missing prices.
3. **GTIN Rule Inspection**: The schema contract defines GTIN as **optional** because global retailers rarely expose GTIN in public DOM. The validator was updated to never invalidate products missing GTIN.

### Revalidation Results (Without Recrawling):
- **Previously Validated**: `0 / 8` (`0.0%`)
- **Newly Validated**: `4 / 8` (`50.0%`)
- **Still Failed (True Negatives - 404s/Homepages)**: `4 / 8` (`50.0%`)
- **Validator-Induced False Negatives Identified & Corrected**: **`4` products** (`B09G9FPHY6`, `B0CL6LMC9N` ES, `B0CL6LMC9N` DE, `B09G91LXFP` DE)

Preserved audit data: [`validation_audit.csv`](file:///Users/priteshhome/crawl/reports/runs/run_20260823_phase3a_forensic/validation_audit.csv).

---

## 4. HTTP vs Playwright Controlled Test

A controlled benchmark was executed on **10 identical real product URLs** across diverse retailers comparing HTTP-only vs Playwright-only execution:

| Metric | HTTP-Only Strategy | Playwright-Only Strategy | Delta / Observation |
| :--- | :---: | :---: | :--- |
| **Total Attempts** | `10` | `10` | Exact same population |
| **Successful Content Availability** | `4 / 10` (`40.0%`) | `3 / 10` (`30.0%`) | HTTP successfully received raw HTML on Amazon & Reliance |
| **Product Identification** | `4 / 10` (`40.0%`) | `3 / 10` (`30.0%`) | Template identified on accessible pages |
| **Extraction Success** | `4 / 10` (`40.0%`) | `3 / 10` (`30.0%`) | Extracted structured product records |
| **Validation Success** | **`2 / 10` (`20.0%`)** | **`2 / 10` (`20.0%`)** | `amazon-de` and `amazon-br` passed validation |
| **Average Latency** | `3,135 ms` | `5,806 ms` | Playwright took 1.85x longer |
| **P95 Latency** | `7,735 ms` | `11,165 ms` | Playwright p95 due to browser start |
| **Total Bytes Received** | `3,630,058 B` | `2,147,132 B` | HTTP downloaded complete assets |
| **Total Browser Rendering Time** | `0.0 s` | `58.06 s` | 58.1 seconds of Chromium execution |

Controlled test dataset: [`controlled_comparison.json`](file:///Users/priteshhome/crawl/reports/runs/run_20260823_phase3a_forensic/controlled_comparison.json).

---

## 5. Custom Adapter Implementation & Unit Tests

Two custom target adapters were implemented under `app/adapters/`:
1. **`AmazonAdapter`** ([`amazon.py`](file:///Users/priteshhome/crawl/app/adapters/amazon.py)): Extracts title, brand, price, currency, availability, ASIN, ratings, review counts, and high-res imagery across global Amazon domains with multilingual support.
2. **`BoulangerAdapter`** ([`boulanger.py`](file:///Users/priteshhome/crawl/app/adapters/boulanger.py)): Extracts microdata and DOM selectors for Boulanger France.

### Unit Test Verification:
**27 tests** in `tests/test_adapters.py` and test suite passed with 100% success rate (`pytest tests/ -v` in 25.70s), testing valid products, missing prices, invalid prices, and missing optional fields.

---

## 6. Ground-Truth Field Accuracy

A manual ground-truth audit of extracted product data against visible source HTML was conducted.

Preserved in [`ground_truth.csv`](file:///Users/priteshhome/crawl/reports/runs/run_20260823_phase3a_forensic/ground_truth.csv):
- **Total Fields Verified**: 28 fields across 4 verified SKUs
- **Matches**: `28 / 28` (`100.0%`)
- **Mismatches**: `0 / 28` (`0.0%`)
- **Field Accuracy**: **`100.0%` field precision** on extracted attributes.

---

## 7. Seven-Stage Pipeline Results on Targeted Live Benchmarks

Live benchmarks with **limit = 20 real SKUs** were executed against the two selected targets:

### Target 1: `amazon-de` (Germany)
- **1. DISCOVERY**: `20 / 20` (`100.0%`)
- **2. URL REACHABILITY**: `20 / 20` (`100.0%`)
- **3. CONTENT AVAILABILITY**: `6 / 20` (`30.0%`) — 14 URLs returned 404 (non-stocked ASINs)
- **4. PRODUCT IDENTIFICATION**: `6 / 20` (`30.0%`)
- **5. EXTRACTION**: `6 / 20` (`30.0%`)
- **6. FIELD VALIDATION**: `5 / 20` (`25.0%`)
- **7. PRODUCT VALIDATION**: **`5 / 20` (`25.0%`)** (Grade E, EXTRACTION_LIMITED)

### Target 2: `amazon-br` (Brazil)
- **1. DISCOVERY**: `20 / 20` (`100.0%`)
- **2. URL REACHABILITY**: `20 / 20` (`100.0%`)
- **3. CONTENT AVAILABILITY**: `4 / 20` (`20.0%`) — 16 URLs returned 404 (non-stocked ASINs)
- **4. PRODUCT IDENTIFICATION**: `4 / 20` (`20.0%`)
- **5. EXTRACTION**: `4 / 20` (`20.0%`)
- **6. FIELD VALIDATION**: `4 / 20` (`20.0%`)
- **7. PRODUCT VALIDATION**: **`4 / 20` (`20.0%`)** (Grade E, EXTRACTION_LIMITED)

---

## 8. Failure Distribution Analysis

Across the live targeted benchmark:
1. **`HTTP_404_NOT_FOUND`**: `30 / 40` (`75.0%`) — Regional catalog differences where global ASINs are not listed in DE or BR marketplaces.
2. **`REQUIRED_FIELD_MISSING`**: `1 / 40` (`2.5%`) — Accessory listing without standard identity fields.
3. **`SUCCESS`**: `9 / 40` (`22.5%`) — Fully validated SKU extractions.

---

## 9. Strategy Cost Analysis

| Strategy | Requests | Retries | Bytes Received | Browser Seconds | Validated SKUs | Latency Avg |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **HTTP-First Standard** | 40 | 0 | 14,892,104 B | 0.0 s | 9 | 26,557 ms |
| **Playwright Browser** | 10 (controlled) | 0 | 2,147,132 B | 58.06 s | 2 | 5,806 ms |

---

## 10. Remaining Limitations

1. **WAF / Bot Protection on European/Asian Retailers**: Retailers using Akamai Bot Manager (e.g. Boulanger) or Cloudflare Turnstile return 400/403/429 without residential proxy rotation.
2. **Regional Catalog SKU Fragmentation**: Global ASINs/SKUs are not uniformly stocked across all localized country stores. Real product discovery directly from live category sitemaps is required for complete catalog breadth.

---

## 11. Recommended Next Engineering Step

1. **Implement Dynamic Live Category Crawler**: Feed sitemaps and live category listing pages directly into the discovery queue rather than static cross-country seed lists.
2. **Residential Proxy Rotation Integration**: Connect authorized residential proxy egress IPs for targets guarded by Akamai/Cloudflare bot protection.
