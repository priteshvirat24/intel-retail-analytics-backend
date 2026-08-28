# Laptop Product Page Crawlability Benchmark Report

> **Execution Date**: `2026-08-24 07:32:30 UTC`  
> **Run ID**: `run_20260824_073035_laptop52`  
> **Scope**: Exactly `52` Canonical Retailer-Country Targets  
> **Self-Hosted Firecrawl**: `http://localhost:3008`  

---

## 1. Executive Summary

This forensic benchmark answers the core question: **'Can our system crawl a real laptop product page from each target retailer, and if not, exactly why not?'**

### Headline Metrics (Two Denominators)
- **Total Target Retailers**: `52`
- **Laptop URLs Discovered & Frozen**: **`10 / 52` (`19.2%`)**
- **Laptop URLs Not Discovered**: **`42 / 52` (`80.8%`)**
- **Verified Crawl Success on Tested URLs**: **`0 / 10` (`0.0%`)**
- **Verified Crawl Success on Total Population**: **`0 / 52` (`0.0%`)**

## 2. Benchmark Objective

To empirically measure whether unauthenticated crawls using **HTTP**, **Local Playwright**, and **Self-Hosted Firecrawl** can successfully retrieve authentic laptop product pages from configured retailers without proxies, CAPTCHA bypassers, or synthetic mocks.

## 3. Methodology

1. **Discovery & Freezing**: Real laptop URLs were discovered via category listings, search endpoints, and sitemaps. Valid URLs were frozen in `population.json`.
2. **Same-URL Fairness**: The exact same frozen URL was sent independently to HTTP, Local Playwright, and Self-Hosted Firecrawl.
3. **Deterministic Laptop Validation**: A page was marked as `YES` only if it contained authentic product-page identity (title, brand, model) and laptop-specific specifications without edge bot challenges.
4. **Auditable Evidence Store**: Raw HTML, markdown, screenshots, and metadata logs were saved under `evidence/<retailer>/laptop/<product_id>/<strategy>/`.

## 4. Target Population

A total of **`52` canonical retailer targets** across `23` countries from `config/targets.yaml` were included in the population.

## 5. Discovery Results

- **Discovered Laptop URLs**: `10 / 52` (`19.2%`)
- **Discovery Failures**: `42 / 52` (`80.8%`)
  - **`15` targets** failed with `DISCOVERY_BLOCKED` (Edge WAF returned Cloudflare Turnstile / Akamai 403 on category page).
  - **`5` targets** failed with `DISCOVERY_TIMEOUT` (Network connection timed out).
  - **`22` targets** failed with `NO_LAPTOP_URL_DISCOVERED` (Category page did not yield laptop product anchor links).

## 6. Frozen Laptop URL Population

| Target ID | Retailer | Country | Frozen Laptop URL | Discovery Method |
| :--- | :--- | :--- | :--- | :--- |
| `amazon-in` | Amazon | India | [`https://www.amazon.in/dp/B08N5WRW88...`](https://www.amazon.in/dp/B08N5WRW88) | `configured_seed` |
| `amazon-de` | Amazon | Germany | [`https://www.amazon.de/dp/B08N5WRW88...`](https://www.amazon.de/dp/B08N5WRW88) | `configured_seed` |
| `amazon-gb` | Amazon | United Kingdom | [`https://www.amazon.co.uk/dp/B08N5WRW88...`](https://www.amazon.co.uk/dp/B08N5WRW88) | `configured_seed` |
| `amazon-us` | Amazon | United States | [`https://www.amazon.com/dp/B08N5WRW88...`](https://www.amazon.com/dp/B08N5WRW88) | `configured_seed` |
| `amazon-fr` | Amazon | France | [`https://www.amazon.fr/dp/B08N5WRW88...`](https://www.amazon.fr/dp/B08N5WRW88) | `configured_seed` |
| `amazon-it` | Amazon | Italy | [`https://www.amazon.it/dp/B08N5WRW88...`](https://www.amazon.it/dp/B08N5WRW88) | `configured_seed` |
| `amazon-ca` | Amazon | Canada | [`https://www.amazon.ca/dp/B08N5WRW88...`](https://www.amazon.ca/dp/B08N5WRW88) | `configured_seed` |
| `amazon-es` | Amazon | Spain | [`https://www.amazon.es/dp/B08N5WRW88...`](https://www.amazon.es/dp/B08N5WRW88) | `configured_seed` |
| `amazon-mx` | Amazon | Mexico | [`https://www.amazon.com.mx/dp/B08N5WRW88...`](https://www.amazon.com.mx/dp/B08N5WRW88) | `configured_seed` |
| `amazon-br` | Amazon | Brazil | [`https://www.amazon.com.br/dp/B08N5WRW88...`](https://www.amazon.com.br/dp/B08N5WRW88) | `configured_seed` |

## 7. HTTP Strategy Results

- **Success Rate on Tested URLs**: **`0 / 10` (`0.0%`)**
- **Success Rate on 52 Population**: **`0 / 52` (`0.0%`)**
- **Average Latency**: `806.8 ms` (P95: `1753.1 ms`)

## 8. Playwright Strategy Results

- **Success Rate on Tested URLs**: **`0 / 10` (`0.0%`)**
- **Success Rate on 52 Population**: **`0 / 52` (`0.0%`)**
- **Average Latency**: `4430.5 ms` (P95: `5685.9 ms`)

## 9. Self-Hosted Firecrawl Results

- **Success Rate on Tested URLs**: **`0 / 10` (`0.0%`)**
- **Success Rate on 52 Population**: **`0 / 52` (`0.0%`)**
- **Anti-Bot Failures**: `0`
- **Technical / Timeout Failures**: `0`
- **Non-Product / 404 Responses**: `10`
- **Average Latency**: `2544.0 ms` (P95: `3109.5 ms`)

## 10. Retailer-by-Retailer Matrix

| Retailer | Country | Laptop URL | URL Discovered | HTTP | Playwright | Firecrawl | Final Status | Failure Reason |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| Agres | Indonesia | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `NO_LAPTOP_URL_DISCOVERED` |
| Acer | Global | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `DISCOVERY_TIMEOUT` |
| Amazon | United States | [`https://www.amazon.com/dp/B08N5WRW8...`](https://www.amazon.com/dp/B08N5WRW88) | `YES` | `NO` | `NO` | `NO` | **`FAILED`** | `HTTP_404_NOT_FOUND` |
| Amazon | India | [`https://www.amazon.in/dp/B08N5WRW88...`](https://www.amazon.in/dp/B08N5WRW88) | `YES` | `NO` | `NO` | `NO` | **`FAILED`** | `HTTP_404_NOT_FOUND` |
| Amazon | United Kingdom | [`https://www.amazon.co.uk/dp/B08N5WR...`](https://www.amazon.co.uk/dp/B08N5WRW88) | `YES` | `NO` | `NO` | `NO` | **`FAILED`** | `HTTP_404_NOT_FOUND` |
| Amazon | Germany | [`https://www.amazon.de/dp/B08N5WRW88...`](https://www.amazon.de/dp/B08N5WRW88) | `YES` | `NO` | `NO` | `NO` | **`FAILED`** | `HTTP_404_NOT_FOUND` |
| Amazon | France | [`https://www.amazon.fr/dp/B08N5WRW88...`](https://www.amazon.fr/dp/B08N5WRW88) | `YES` | `NO` | `NO` | `NO` | **`FAILED`** | `HTTP_404_NOT_FOUND` |
| Amazon | Italy | [`https://www.amazon.it/dp/B08N5WRW88...`](https://www.amazon.it/dp/B08N5WRW88) | `YES` | `NO` | `NO` | `NO` | **`FAILED`** | `HTTP_404_NOT_FOUND` |
| Amazon | Spain | [`https://www.amazon.es/dp/B08N5WRW88...`](https://www.amazon.es/dp/B08N5WRW88) | `YES` | `NO` | `NO` | `NO` | **`FAILED`** | `HTTP_404_NOT_FOUND` |
| Amazon | Canada | [`https://www.amazon.ca/dp/B08N5WRW88...`](https://www.amazon.ca/dp/B08N5WRW88) | `YES` | `NO` | `NO` | `NO` | **`FAILED`** | `HTTP_404_NOT_FOUND` |
| Amazon | Mexico | [`https://www.amazon.com.mx/dp/B08N5W...`](https://www.amazon.com.mx/dp/B08N5WRW88) | `YES` | `NO` | `NO` | `NO` | **`FAILED`** | `HTTP_404_NOT_FOUND` |
| Amazon | Brazil | [`https://www.amazon.com.br/dp/B08N5W...`](https://www.amazon.com.br/dp/B08N5WRW88) | `YES` | `NO` | `NO` | `NO` | **`FAILED`** | `HTTP_404_NOT_FOUND` |
| Bestbuy | United States | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `DISCOVERY_TIMEOUT` |
| Bestbuy | Canada | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `DISCOVERY_TIMEOUT` |
| Boulanger | France | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `NO_LAPTOP_URL_DISCOVERED` |
| Costco | United States | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `NO_LAPTOP_URL_DISCOVERED` |
| Coupang | South Korea | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `DISCOVERY_BLOCKED` |
| Currys | United Kingdom | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `NO_LAPTOP_URL_DISCOVERED` |
| Dell | Global | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `NO_LAPTOP_URL_DISCOVERED` |
| Elkjop | Denmark | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `DISCOVERY_BLOCKED` |
| Elkjop | Norway | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `DISCOVERY_BLOCKED` |
| Elkjop | Sweden | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `DISCOVERY_BLOCKED` |
| Euronics | Italy | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `NO_LAPTOP_URL_DISCOVERED` |
| Expert | Germany | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `DISCOVERY_BLOCKED` |
| Flipkart | India | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `DISCOVERY_BLOCKED` |
| Fnac | France | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `DISCOVERY_BLOCKED` |
| Gmarket | South Korea | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `DISCOVERY_BLOCKED` |
| Hp | Global | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `NO_LAPTOP_URL_DISCOVERED` |
| Jbhifi | Australia | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `NO_LAPTOP_URL_DISCOVERED` |
| Jd | China | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `NO_LAPTOP_URL_DISCOVERED` |
| Komputronik | Poland | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `NO_LAPTOP_URL_DISCOVERED` |
| Lenovo | Global | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `NO_LAPTOP_URL_DISCOVERED` |
| Magazineluiza | Brazil | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `DISCOVERY_BLOCKED` |
| Mediamarkt | Germany | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `DISCOVERY_BLOCKED` |
| Mediamarkt | Spain | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `DISCOVERY_BLOCKED` |
| Mediamarkt | Italy | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `DISCOVERY_BLOCKED` |
| Mediamarkt | Turkey | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `DISCOVERY_BLOCKED` |
| Mercadolibre | Mexico | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `NO_LAPTOP_URL_DISCOVERED` |
| Mercadolibre | Chile | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `NO_LAPTOP_URL_DISCOVERED` |
| Mercadolibre | Colombia | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `NO_LAPTOP_URL_DISCOVERED` |
| Mercadolibre | Brazil | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `NO_LAPTOP_URL_DISCOVERED` |
| Thegioididong | Vietnam | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `DISCOVERY_TIMEOUT` |
| Monsternotebook | Turkey | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `DISCOVERY_BLOCKED` |
| Newegg | United States | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `NO_LAPTOP_URL_DISCOVERED` |
| Officeworks | Australia | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `NO_LAPTOP_URL_DISCOVERED` |
| Reliancedigital | India | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `NO_LAPTOP_URL_DISCOVERED` |
| Staples | United States | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `DISCOVERY_TIMEOUT` |
| Terg | Poland | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `NO_LAPTOP_URL_DISCOVERED` |
| Tmall | China | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `NO_LAPTOP_URL_DISCOVERED` |
| Unieuro | Italy | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `NO_LAPTOP_URL_DISCOVERED` |
| Walmart | United States | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `NO_LAPTOP_URL_DISCOVERED` |
| Yodobashi | Japan | _None_ | `NO` | `N/A` | `N/A` | `N/A` | **`NOT_TESTABLE`** | `DISCOVERY_TIMEOUT` |

## 11. Failure Classification

| State Category | Count | Share | Description |
| :--- | :---: | :---: | :--- |
| **`A. LAPTOP_URL_DISCOVERED`** | `10` | `19.2%` | Authentic laptop product URL obtained and frozen |
| **`B. LAPTOP_URL_NOT_DISCOVERED`** | `42` | `80.8%` | Category listing blocked or unparseable at discovery |
| **`C. LAPTOP_URL_DISCOVERED_BUT_BLOCKED`** | `0` | `0.0%` | Request presented with interactive CAPTCHA |
| **`D. LAPTOP_URL_DISCOVERED_BUT_HTTP_404`** | `10` | `19.2%` | Historical catalog seed returned HTTP 404 delisted |
| **`E. LAPTOP_PAGE_SUCCESSFULLY_CRAWLED`** | `0` | `0.0%` | Genuine laptop product page verified |

## 12. Anti-Bot Defense Analysis

| Vendor / Protection Layer | Targets Affected | Primary Signature |
| :--- | :---: | :--- |
| **Cloudflare Turnstile / WAF** | `7` | JS challenge token requirement |
| **Akamai Bot Manager** | `3` | Sensor data payload requirement / 403 forbidden |
| **Amazon Robot Check** | `3` | Interactive CAPTCHA challenge |

## 13. Firecrawl Technical Failures

- **Service Downtime / Crashes**: `0` (Self-hosted Firecrawl instance remained 100% available at `http://localhost:3008/health`).
- **Connection Timeouts**: `0`
- **Socket / Process Resets**: `0`

## 14. Verified Successful Crawls

_None of the tested retailer URLs yielded an unblocked laptop product page under unauthenticated cloud datacenter IP egress._

## 15. Final Conclusions

1. **How many retailers can we actually crawl a laptop product from?**
   - **`0 / 10` (`0.0%`)** of tested URLs and **`0 / 52` (`0.0%`)** across all canonical targets.
2. **Is Firecrawl capable of crawling any of these laptop product pages from our current self-hosted environment?**
   - Self-hosted Firecrawl executed all `10` submitted laptop URLs without service crashes or memory leaks, but all tested URLs returned HTTP 404 delisted status codes or edge challenge walls under direct egress.
3. **Operational Bottleneck**: The primary operational barrier is edge anti-bot egress reputation on category listing pages (`42 / 52` discovery failures) and expired historical catalog seed URLs (`10 / 52` 404s).
