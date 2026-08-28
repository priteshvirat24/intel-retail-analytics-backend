# Global Retailer Multi-Site Crawl & SKU Extraction Capability Report

> **Generated at**: `2026-08-23 05:44:28 UTC`  
> **Scope**: `1` Retailer-Country Targets | `20` Total Target SKUs  
> **Overall Empirical SKU Coverage**: **`100.0%`** (`20/20` valid SKUs across catalog)

---

## 1. Executive Summary & Capability Classification

| Grade | Level | Description | Target Count | Targets |
| :---: | :--- | :--- | :---: | :--- |
| **A** | Excellent (>=95% Coverage) | High confidence extraction | 1 | `Mock Store Testbed (US)` |
| **B** | Good (85-94% Coverage) | High confidence extraction | 0 | _None_ |
| **C** | Partial (70-84% Coverage) | High confidence extraction | 0 | _None_ |
| **D** | Poor (50-69% Coverage) | High confidence extraction | 0 | _None_ |
| **E** | Not Practically Crawlable (<50% Coverage) | High confidence extraction | 0 | _None_ |

---

## 2. Retailer-by-Retailer Capability Matrix

| Retailer | Country | Grade | Category | Target | Discovered | HTTP | Browser | Extracted | Validated | Coverage | Block % | Latency | Primary Strategy | Main Failure |
| :--- | :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Mock Store Testbed** | US | `A` | `HTTP_ONLY` | 20 | 20 | 20 | 0 | 20 | 20 | **100%** | 0% | 6545ms | HTTP | None |

---

## 3. Failure Root Cause Analysis & Empirical Diagnosis

Detailed analysis for retailers achieving below 90% coverage threshold:

_All tested retailer targets achieved >= 90% SKU extraction coverage._

---

## 4. Auditable Evidence Directory Structure

Evidence for every attempted SKU is stored in the local evidence store:
```
evidence/
  ├── <retailer_slug>/
  │     ├── <country_code>/
  │     │     ├── sku_001/
  │     │     │     ├── attempt_1_snapshot.html
  │     │     │     ├── attempt_1_screenshot.png (if browser used)
  │     │     │     ├── attempt_1_meta.json
  │     │     │     ├── normalized_product.json
  │     │     │     └── crawl_result.json
  │     │     └── ...
```
