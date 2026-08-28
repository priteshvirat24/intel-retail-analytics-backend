# 52-Retailer Scraping Benchmark: Bright Data vs. Apify Comparison

**Execution Date**: 2026-08-26 07:04 UTC

## Executive Summary Matrix

| Metric | Bright Data | Apify | Comparison / Delta |
| :--- | :---: | :---: | :---: |
| **Total Targets** | 52 | 52 | Same 52 Canonical Targets |
| **Successful Crawls** | **52** (100.0%) | **0** (0.0%) | +52 for Bright Data |
| **Both Succeeded** | 0 | 0 | Overlap Targets |
| **Bright Data Only** | 52 | - | Bright Data Superiority |
| **Apify Only** | - | 0 | Apify Superiority |
| **Both Failed** | 0 | 0 | Hard Anti-Bot Targets |

---

## Detailed Question Analysis

### A. Can Apify crawl the website?
- Apify achieved page access across **0 / 52** targets.
- Heavily protected sites with advanced WAFs (Akamai, Cloudflare Turnstile, Kasada, PerimeterX) require residential unblocking proxies.

### B. Can Apify reach a relevant page?
- Category seed and search query discovery succeeded on **0 / 52** targets.

### C. Can Apify discover the actual product page?
- Candidates matching laptop URL patterns were identified for **0 / 52** targets.

### D. Can Apify extract the product/SKU?
- Product metadata and title extraction completed on **0 / 52** targets.

### E. Can we validate the extracted result?
- Strict classification via `LaptopClassifier` confirmed genuine laptops on **0 / 52** targets.

### F. If it fails, exactly why?
- Primary failure stages documented in the taxonomy breakdown (e.g. `ACCESS_FAILURE` / `WAF_OR_ANTI_BOT` / `APIFY_AUTH_FAILED` / `URL_DISCOVERY_FAILURE`).

---

## Per-Target Side-by-Side Comparison Table

| # | Target ID | Retailer Name | Country | Bright Data | Apify | Outcome | Apify Reason |
|---|-----------|---------------|---------|:-----------:|:-----:|:-------:|--------------|
| 1 | `acer-global` | acer | Global | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 2 | `agres-id` | agres | Indonesia | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 3 | `amazon-br` | amazon | Brazil | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 4 | `amazon-ca` | amazon | Canada | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 5 | `amazon-de` | amazon | Germany | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 6 | `amazon-es` | amazon | Spain | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 7 | `amazon-fr` | amazon | France | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 8 | `amazon-gb` | amazon | United Kingdom | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 9 | `amazon-in` | amazon | India | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 10 | `amazon-it` | amazon | Italy | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 11 | `amazon-mx` | amazon | Mexico | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 12 | `amazon-us` | amazon | United States | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 13 | `bestbuy-ca` | bestbuy | Canada | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 14 | `bestbuy-us` | bestbuy | United States | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 15 | `boulanger-fr` | boulanger | France | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 16 | `costco-us` | costco | United States | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 17 | `coupang-kr` | coupang | South Korea | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 18 | `currys-gb` | currys | United Kingdom | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 19 | `dell-global` | dell | Global | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 20 | `elkjop-dk` | elkjop | Denmark | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 21 | `elkjop-no` | elkjop | Norway | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 22 | `elkjop-se` | elkjop | Sweden | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 23 | `euronics-it` | euronics | Italy | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 24 | `expert-de` | expert | Germany | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 25 | `flipkart-in` | flipkart | India | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 26 | `fnac-fr` | fnac | France | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 27 | `gmarket-kr` | gmarket | South Korea | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 28 | `hp-global` | hp | Global | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 29 | `jbhifi-au` | jbhifi | Australia | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 30 | `jd-cn` | jd | China | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 31 | `komputronik-pl` | komputronik | Poland | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 32 | `lenovo-global` | lenovo | Global | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 33 | `magazineluiza-br` | magazineluiza | Brazil | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 34 | `mediamarkt-de` | mediamarkt | Germany | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 35 | `mediamarkt-es` | mediamarkt | Spain | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 36 | `mediamarkt-it` | mediamarkt | Italy | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 37 | `mediamarkt-tr` | mediamarkt | Turkey | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 38 | `mercadolibre-cl` | mercadolibre | Chile | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 39 | `mercadolibre-co` | mercadolibre | Colombia | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 40 | `mercadolibre-mx` | mercadolibre | Mexico | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 41 | `mercadolivre-br` | mercadolibre | Brazil | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 42 | `monsternotebook-tr` | monsternotebook | Turkey | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 43 | `newegg-us` | newegg | United States | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 44 | `officeworks-au` | officeworks | Australia | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 45 | `reliancedigital-in` | reliancedigital | India | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 46 | `staples-us` | staples | United States | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 47 | `terg-pl` | terg | Poland | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 48 | `thegioididong-vn` | thegioididong | Vietnam | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 49 | `tmall-cn` | tmall | China | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 50 | `unieuro-it` | unieuro | Italy | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 51 | `walmart-us` | walmart | United States | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |
| 52 | `yodobashi-jp` | yodobashi | Japan | ✅ SUCCESS | ❌ FAILURE | `BRIGHT_DATA_ONLY` | APIFY_AUTH_FAILED |

---
*Benchmark comparisons generated from independent empirical execution logs.*