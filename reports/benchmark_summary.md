# Global Retailer Multi-Site SKU Crawl & Extraction Capability Benchmark

> **Execution Date**: `2026-08-23 10:33:02 UTC`  
> **Scope**: `34` Unique Retailer Brands | `52` Retailer-Country Targets across `23` Countries  
> **Total Empirical SKU Attempts**: `20` attempts | **Validated SKUs**: `4`  
> **Overall Empirical Catalog SKU Coverage**: **`20.0%`** (`4 / 20` tested SKUs)

---

## A. Executive Summary

This report documents an empirical, evidence-generating benchmark to measure the extractability of product/SKU catalog data across global ecommerce platforms. The system uses a multi-tier adaptive crawling pipeline (HTTP/2 fast path, Playwright headless browser rendering, and custom DOM adapters) and rigorously validates extraction quality field-by-field.

### Empirical Capability Distribution
| Grade | Classification Threshold | Target Count | Population Percentage | Target IDs |
| :---: | :--- | :---: | :---: | :--- |
| **A** | Excellent (>=95% Coverage) | `0` | `0.0%` (0/1) | _None_ |
| **B** | Good (85-94% Coverage) | `0` | `0.0%` (0/1) | _None_ |
| **C** | Partial (70-84% Coverage) | `0` | `0.0%` (0/1) | _None_ |
| **D** | Poor (50-69% Coverage) | `0` | `0.0%` (0/1) | _None_ |
| **E** | Not Practically Crawlable (<50% Coverage) | `1` | `100.0%` (1/1) | `amazon-br` |

---

## B. Canonical Target Registry

All target metrics and aggregations are derived programmatically from `config/targets.yaml`:
- **Unique Retailer Brands (`unique_retailers`)**: `34` (acer, agres, amazon, bestbuy, boulanger, costco, coupang, currys, dell, elkjop, euronics, expert, flipkart, fnac, gmarket, hp, jbhifi, jd, komputronik, lenovo, magazineluiza, mediamarkt, mercadolibre, monsternotebook, newegg, officeworks, reliancedigital, staples, terg, thegioididong, tmall, unieuro, walmart, yodobashi)
- **Retailer-Country Targets (`retailer_country_targets`)**: `52` target configurations
- **Distinct Countries (`countries`)**: `23` (AU, BR, CA, CL, CN, CO, DE, DK, ES, FR, GB, ID, IN, IT, JP, KR, MX, NO, PL, SE, TR, US, VN)

| Target ID | Retailer | Country | ISO | Domain | Locale | Currency | Timezone | Rate Limit | Concurrency |
| :--- | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :---: | :---: |
| `agres-id` | Agres | Indonesia | `ID` | `agres.id` | `id-ID` | `IDR` | `Asia/Jakarta` | `2.0/s` | `3` |
| `acer-global` | Acer | Global | `US` | `store.acer.com` | `en-US` | `USD` | `America/New_York` | `2.0/s` | `3` |
| `amazon-us` | Amazon | United States | `US` | `amazon.com` | `en-US` | `USD` | `America/New_York` | `0.5/s` | `1` |
| `amazon-in` | Amazon | India | `IN` | `amazon.in` | `en-IN` | `INR` | `Asia/Kolkata` | `0.5/s` | `1` |
| `amazon-gb` | Amazon | United Kingdom | `GB` | `amazon.co.uk` | `en-GB` | `GBP` | `Europe/London` | `0.5/s` | `1` |
| `amazon-de` | Amazon | Germany | `DE` | `amazon.de` | `de-DE` | `EUR` | `Europe/Berlin` | `0.5/s` | `1` |
| `amazon-fr` | Amazon | France | `FR` | `amazon.fr` | `fr-FR` | `EUR` | `Europe/Paris` | `0.5/s` | `1` |
| `amazon-it` | Amazon | Italy | `IT` | `amazon.it` | `it-IT` | `EUR` | `Europe/Rome` | `0.5/s` | `1` |
| `amazon-es` | Amazon | Spain | `ES` | `amazon.es` | `es-ES` | `EUR` | `Europe/Madrid` | `0.5/s` | `1` |
| `amazon-ca` | Amazon | Canada | `CA` | `amazon.ca` | `en-CA` | `CAD` | `America/Toronto` | `0.5/s` | `1` |
| `amazon-mx` | Amazon | Mexico | `MX` | `amazon.com.mx` | `es-MX` | `MXN` | `America/Mexico_City` | `0.5/s` | `1` |
| `amazon-br` | Amazon | Brazil | `BR` | `amazon.com.br` | `pt-BR` | `BRL` | `America/Sao_Paulo` | `0.5/s` | `1` |
| `bestbuy-us` | Bestbuy | United States | `US` | `bestbuy.com` | `en-US` | `USD` | `America/New_York` | `0.5/s` | `1` |
| `bestbuy-ca` | Bestbuy | Canada | `CA` | `bestbuy.ca` | `en-CA` | `CAD` | `America/Toronto` | `0.5/s` | `1` |
| `boulanger-fr` | Boulanger | France | `FR` | `boulanger.com` | `fr-FR` | `EUR` | `Europe/Paris` | `1.5/s` | `2` |
| `costco-us` | Costco | United States | `US` | `costco.com` | `en-US` | `USD` | `America/New_York` | `1.0/s` | `2` |
| `coupang-kr` | Coupang | South Korea | `KR` | `coupang.com` | `ko-KR` | `KRW` | `Asia/Seoul` | `1.0/s` | `2` |
| `currys-gb` | Currys | United Kingdom | `GB` | `currys.co.uk` | `en-GB` | `GBP` | `Europe/London` | `1.5/s` | `2` |
| `dell-global` | Dell | Global | `US` | `dell.com` | `en-US` | `USD` | `America/New_York` | `1.5/s` | `2` |
| `elkjop-dk` | Elkjop | Denmark | `DK` | `elgiganten.dk` | `da-DK` | `DKK` | `Europe/Copenhagen` | `1.5/s` | `2` |
| `elkjop-no` | Elkjop | Norway | `NO` | `elkjop.no` | `no-NO` | `NOK` | `Europe/Oslo` | `1.5/s` | `2` |
| `elkjop-se` | Elkjop | Sweden | `SE` | `elgiganten.se` | `sv-SE` | `SEK` | `Europe/Stockholm` | `1.5/s` | `2` |
| `euronics-it` | Euronics | Italy | `IT` | `euronics.it` | `it-IT` | `EUR` | `Europe/Rome` | `1.5/s` | `2` |
| `expert-de` | Expert | Germany | `DE` | `expert.de` | `de-DE` | `EUR` | `Europe/Berlin` | `1.5/s` | `2` |
| `flipkart-in` | Flipkart | India | `IN` | `flipkart.com` | `en-IN` | `INR` | `Asia/Kolkata` | `1.0/s` | `2` |
| `fnac-fr` | Fnac | France | `FR` | `fnac.com` | `fr-FR` | `EUR` | `Europe/Paris` | `1.5/s` | `2` |
| `gmarket-kr` | Gmarket | South Korea | `KR` | `gmarket.co.kr` | `ko-KR` | `KRW` | `Asia/Seoul` | `1.5/s` | `2` |
| `hp-global` | Hp | Global | `US` | `hp.com` | `en-US` | `USD` | `America/New_York` | `1.5/s` | `2` |
| `jbhifi-au` | Jbhifi | Australia | `AU` | `jbhifi.com.au` | `en-AU` | `AUD` | `Australia/Sydney` | `1.5/s` | `2` |
| `jd-cn` | Jd | China | `CN` | `jd.com` | `zh-CN` | `CNY` | `Asia/Shanghai` | `1.0/s` | `2` |
| `komputronik-pl` | Komputronik | Poland | `PL` | `komputronik.pl` | `pl-PL` | `PLN` | `Europe/Warsaw` | `1.5/s` | `2` |
| `lenovo-global` | Lenovo | Global | `US` | `lenovo.com` | `en-US` | `USD` | `America/New_York` | `1.5/s` | `2` |
| `magazineluiza-br` | Magazineluiza | Brazil | `BR` | `magazineluiza.com.br` | `pt-BR` | `BRL` | `America/Sao_Paulo` | `1.5/s` | `2` |
| `mediamarkt-de` | Mediamarkt | Germany | `DE` | `mediamarkt.de` | `de-DE` | `EUR` | `Europe/Berlin` | `1.5/s` | `2` |
| `mediamarkt-es` | Mediamarkt | Spain | `ES` | `mediamarkt.es` | `es-ES` | `EUR` | `Europe/Madrid` | `1.5/s` | `2` |
| `mediamarkt-it` | Mediamarkt | Italy | `IT` | `mediaworld.it` | `it-IT` | `EUR` | `Europe/Rome` | `1.5/s` | `2` |
| `mediamarkt-tr` | Mediamarkt | Turkey | `TR` | `mediamarkt.com.tr` | `tr-TR` | `TRY` | `Europe/Istanbul` | `1.5/s` | `2` |
| `mercadolibre-mx` | Mercadolibre | Mexico | `MX` | `mercadolibre.com.mx` | `es-MX` | `MXN` | `America/Mexico_City` | `1.5/s` | `2` |
| `mercadolibre-cl` | Mercadolibre | Chile | `CL` | `mercadolibre.cl` | `es-CL` | `CLP` | `America/Santiago` | `1.5/s` | `2` |
| `mercadolibre-co` | Mercadolibre | Colombia | `CO` | `mercadolibre.com.co` | `es-CO` | `COP` | `America/Bogota` | `1.5/s` | `2` |
| `mercadolivre-br` | Mercadolibre | Brazil | `BR` | `mercadolivre.com.br` | `pt-BR` | `BRL` | `America/Sao_Paulo` | `1.5/s` | `2` |
| `thegioididong-vn` | Thegioididong | Vietnam | `VN` | `thegioididong.com` | `vi-VN` | `VND` | `Asia/Ho_Chi_Minh` | `1.5/s` | `2` |
| `monsternotebook-tr` | Monsternotebook | Turkey | `TR` | `monsternotebook.com.tr` | `tr-TR` | `TRY` | `Europe/Istanbul` | `1.5/s` | `2` |
| `newegg-us` | Newegg | United States | `US` | `newegg.com` | `en-US` | `USD` | `America/New_York` | `0.5/s` | `1` |
| `officeworks-au` | Officeworks | Australia | `AU` | `officeworks.com.au` | `en-AU` | `AUD` | `Australia/Sydney` | `1.5/s` | `2` |
| `reliancedigital-in` | Reliancedigital | India | `IN` | `reliancedigital.in` | `en-IN` | `INR` | `Asia/Kolkata` | `1.5/s` | `2` |
| `staples-us` | Staples | United States | `US` | `staples.com` | `en-US` | `USD` | `America/New_York` | `1.5/s` | `2` |
| `terg-pl` | Terg | Poland | `PL` | `mediaexpert.pl` | `pl-PL` | `PLN` | `Europe/Warsaw` | `1.5/s` | `2` |
| `tmall-cn` | Tmall | China | `CN` | `tmall.com` | `zh-CN` | `CNY` | `Asia/Shanghai` | `1.0/s` | `2` |
| `unieuro-it` | Unieuro | Italy | `IT` | `unieuro.it` | `it-IT` | `EUR` | `Europe/Rome` | `1.5/s` | `2` |
| `walmart-us` | Walmart | United States | `US` | `walmart.com` | `en-US` | `USD` | `America/New_York` | `0.5/s` | `1` |
| `yodobashi-jp` | Yodobashi | Japan | `JP` | `yodobashi.com` | `ja-JP` | `JPY` | `Asia/Tokyo` | `1.5/s` | `2` |

---

## C. Overall Statistics

Every reported metric exposes its exact numerator, denominator, and target population:

| Pipeline Stage | Observed Stage Success Rate | Numerator | Denominator | Stage Definition |
| :--- | :---: | :---: | :---: | :--- |
| **1. DISCOVERY** | `100.0%` | 20 | 20 | Product candidate URLs identified and normalized |
| **2. URL_REACHABILITY** | `100.0%` | 20 | 20 | Network reached target domain without DNS/TCP connection drops |
| **3. CONTENT_AVAILABILITY** | `20.0%` | 4 | 20 | Server returned valid HTML (>200B) without block/challenge barriers |
| **4. PRODUCT_IDENTIFICATION** | `20.0%` | 4 | 20 | Structural DOM template successfully identified |
| **5. EXTRACTION** | `20.0%` | 4 | 20 | Candidate structured product attributes extracted |
| **6. FIELD_VALIDATION** | `20.0%` | 4 | 20 | Individual core fields (title, price, brand) passed validation |
| **7. PRODUCT_VALIDATION** | `20.0%` | 4 | 20 | Composite SKU passed all minimum viable threshold checks |

### Global Security Barriers Encountered
| Security Barrier | Incidence Rate | Targets Affected | Total Targets |
| :--- | :---: | :---: | :---: |
| **Anti-Bot WAF Blocking / 403 / 429** | `0.0%` | 0 | 1 |
| **Interactive CAPTCHA Challenges** | `0.0%` | 0 | 1 |

---

## D. Retailer-Country Capability Matrix

| Retailer | Country | ISO | Grade | Category | Tested | Valid | Observed Coverage | Best Strategy | Avg Latency | Main Failure |
| :--- | :--- | :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Amazon** | Brazil | `BR` | `E` | `EXTRACTION_LIMITED` | `20` | `4` | **`20.0%`** (4/20) | `HTTP` | `27923ms` | `HTTP_404_NOT_FOUND` |

---

## E. Strategy Benchmarking & Comparison

Empirical comparison of achievable coverage and resource trade-offs by crawler strategy:

| Target ID | HTTP Coverage | Playwright Coverage | Adapter Coverage | Best Strategy | Cost Per Valid SKU (ms) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `amazon-br` | `20.0%` (4/20) | `0.0%` (0/20) | `0.0%` (0/20) | **`HTTP`** | `139.62s` |

---

## F. Hierarchical Failure Taxonomy

Failures classified by high-level category, specific diagnostic reason, and pipeline stage:

### Failures by Category
| Category | Failure Count | Percentage | Primary Stage |
| :--- | :---: | :---: | :--- |
| **`HTTP_STATUS`** | `16` | `100.0%` (16/16) | `URL_REACHABILITY / CONTENT_AVAILABILITY` |

### Failures by Specific Reason
| Specific Reason | Category | Count | Percentage |
| :--- | :---: | :---: | :---: |
| `HTTP_404_NOT_FOUND` | `ACCESS / HTTP` | `16` | `100.0%` (16/16) |

---

## G. Field-Level Extraction & Validity Statistics

Field state discrimination (`FIELD_PRESENT_VALID`, `FIELD_NOT_PRESENT`, `FIELD_EXTRACTION_FAILED`, `FIELD_INVALID`, `FIELD_CONFLICT`):

| Field Name | Valid Count | Not Present in Source | Extraction Failed | Invalid Content | Conflicts | Validity Rate (Among Exposed) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **`title`** | `4` | `0` | `0` | `0` | `0` | `100.0%` (4/4) |
| **`price`** | `4` | `0` | `0` | `0` | `0` | `100.0%` (4/4) |
| **`currency`** | `4` | `0` | `0` | `0` | `0` | `100.0%` (4/4) |
| **`availability`** | `4` | `0` | `0` | `0` | `0` | `100.0%` (4/4) |
| **`brand`** | `4` | `0` | `0` | `0` | `0` | `100.0%` (4/4) |
| **`sku`** | `4` | `0` | `0` | `0` | `0` | `100.0%` (4/4) |
| **`gtin`** | `0` | `0` | `0` | `0` | `0` | `N/A` (0 exposed) |
| **`images`** | `4` | `0` | `0` | `0` | `0` | `100.0%` (4/4) |
| **`description`** | `4` | `0` | `0` | `0` | `0` | `100.0%` (4/4) |

---

## H. Category & Structural Template Analysis

### Category Diversity Distribution
| Category | Tested SKUs | Validated SKUs | Category Observed Coverage |
| :--- | :---: | :---: | :---: |
| **Smartphones & Mobile** | `5` | `1` | `20.0%` (1/5) |
| **Audio & Headphones** | `4` | `0` | `0.0%` (0/4) |
| **Laptops & Notebooks** | `3` | `1` | `33.3%` (1/3) |
| **Tablets & E-Readers** | `3` | `2` | `66.7%` (2/3) |
| **Monitors & Displays** | `2` | `0` | `0.0%` (0/2) |
| **Smartwatches & Wearables** | `1` | `0` | `0.0%` (0/1) |
| **Storage & Memory** | `1` | `0` | `0.0%` (0/1) |
| **Home & Electronics** | `1` | `0` | `0.0%` (0/1) |

### Structural Product Template Breakdown
| Product Template ID | Tested Pages | Validated Products | Template Extraction Yield |
| :--- | :---: | :---: | :---: |
| `tmpl_unknown` | `16` | `0` | `0.0%` (0/16) |
| `tmpl_generic_2e6a7f301576` | `4` | `4` | `100.0%` (4/4) |

---

## I. Crawl Cost & Performance Telemetry

| Telemetry Metric | Measured Value | Unit / Breakdown |
| :--- | :---: | :--- |
| **Total HTTP/Browser Requests** | `20` | Total network requests issued |
| **Successful Requests (2xx)** | `4` | `20.0%` of all requests |
| **Failed / Blocked Requests** | `16` | `80.0%` of all requests |
| **Total Headless Browser Compute** | `0.0s` | Chromium execution duration |
| **Total Response Volume** | `4.11 MB` | `4312858` raw bytes transferred |
| **Cumulative Pipeline Latency** | `558463ms` | Wall-clock execution sum |

---

## J. Auditable Evidence Store

Every SKU attempt is persisted with raw evidence in the `evidence/` directory:
```
evidence/
  ├── <retailer_slug>/
  │     ├── <iso_country>/
  │     │     ├── sku_001/
  │     │     │     ├── attempt_1_snapshot.html     # Raw HTML payload
  │     │     │     ├── attempt_1_screenshot.png    # Rendered browser capture (if browser used)
  │     │     │     ├── attempt_1_meta.json        # Telemetry, headers, response code
  │     │     │     ├── failure_diagnosis.json     # Hierarchical category, reason, stage
  │     │     │     ├── normalized_product.json    # Validated schema payload
  │     │     │     └── crawl_result.json          # Complete 7-stage attempt telemetry
```

---

## K. Empirical Limitations & Technical Constraints

1. **Anti-Bot Defenses**: Retailers employing Cloudflare Turnstile, Kasada, PerimeterX, or Akamai Bot Manager reject direct datacenter IP requests. In accordance with benchmark methodology, no bypass or CAPTCHA-solving was attempted; these barriers are recorded as verified empirical limitations.
2. **Client-Side Rendering (SPA)**: Modern single-page applications return an empty HTML shell (`<div id="root"></div>`) over plain HTTP. While headless Chromium can render DOMs, high-concurrency browser automation requires dedicated rendering pools.
3. **Geo-Fencing**: Regional platforms (e.g. Coupang Korea, The Gioi Di Dong Vietnam) enforce strict IP geolocation filtering and drop foreign connections.
4. **Sample Size & Confidence**: All observed metrics represent empirical sample observations over $N$ tested SKUs. Results should not be generalized to 100% catalog crawlability without large-scale distributed sampling.
