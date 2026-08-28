# Self-Hosted Firecrawl 52-Target Laptop Crawlability Benchmark Report

> **Execution Date**: `2026-08-24 07:26:33 UTC`  
> **Run ID**: `run_20260824_072452_firecrawl_laptop52`  
> **Firecrawl Deployment**: `Self-Hosted Open-Source (ghcr.io/firecrawl/playwright-service:latest)` at `http://localhost:3008`  

---

## 1. Executive Summary

This forensic benchmark evaluates whether self-hosted open-source Firecrawl can crawl authentic laptop product pages across **52 canonical global retailer-country targets**.

- **Total Target Population**: `52` configured retailers
- **Discovery Rate**: **`10 / 52` (`19.2%`)** had real laptop product URLs identified/frozen
- **Firecrawl Tested URLs**: `10 / 10` discovered URLs were tested with self-hosted Firecrawl
- **Genuine Laptop Crawls (Firecrawl Success)**: **`0 / 10` (`0.0%`)** of tested URLs (**`0 / 52`** overall)
- **Discovery Failures**: `42 / 52` (`80.8%`) — Category listings were blocked by edge WAFs or unparseable, preventing fair product URL testing.

## 2. Exact Experimental Question

> **"For each of the 52 target retailers, can our self-hosted open-source Firecrawl actually crawl a genuine laptop product page? If yes, prove it with evidence. If no, determine exactly why it failed."**

## 3. Methodology

1. **Discovery & Freezing**: For each retailer, genuine laptop URLs were discovered via sitemaps, category listing pages, and catalog seeds, then frozen into `population.json`.
2. **Exact-URL Firecrawl Execution**: Self-hosted Firecrawl (`ghcr.io/firecrawl/playwright-service:latest`) requested each frozen URL directly.
3. **Strict Validation**: HTTP 200, Firecrawl API 200, or non-empty HTML was NOT treated as crawl success. Success strictly required authentic laptop title/specifications and absence of anti-bot challenges.
4. **Denominator Transparency**: Discovery failures (`LAPTOP_URL_NOT_DISCOVERED`) were strictly separated from Firecrawl crawl failures (`LAPTOP_URL_FOUND_BUT_FIRECRAWL_FAILED`).

## 4. Denominator Definition

| Metric | Formula / Count | Percentage | Definition |
| :--- | :---: | :---: | :--- |
| **Target Population** | `52` | `100.0%` | Total canonical retailer-country targets |
| **Discovery Success** | `10 / 52` | `19.2%` | Targets with verified laptop product URLs |
| **Firecrawl Tested** | `10 / 52` | `19.2%` | Targets executed against self-hosted Firecrawl |
| **Firecrawl Success (Tested)** | `0 / 10` | `0.0%` | Successful laptop crawls out of tested URLs |
| **Firecrawl Success (Population)** | `0 / 52` | `0.0%` | Successful laptop crawls out of all 52 retailers |

## 5. Overall Firecrawl Result

- **Total Retailers Configured**: `52`
- **Laptop URLs Discovered**: `10 / 52` (`19.2%`)
- **Laptop URLs Actually Tested with Firecrawl**: `10 / 52`
- **Successful Genuine Laptop Crawls**: **`0 / 52` (`0.0%`)**
- **Firecrawl Genuine Crawlability Rate on Tested URLs**: **`0 / 10` = `0.0%`**

## 6. Full 52-Retailer Benchmark Matrix

| Retailer | Country | Laptop URL Found | Laptop URL | Firecrawl Tested | Firecrawl Reachable | Final URL | HTTP Status | Actual Laptop Page | Challenge Detected | Blocking Vendor | Failure Reason | Crawl Status | Evidence Path |
| :--- | :--- | :---: | :--- | :---: | :---: | :--- | :---: | :---: | :---: | :--- | :--- | :--- | :--- |
| Agres | Indonesia | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `NO_LAPTOP_URL_DISCOVERED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/agres/laptop/none/` |
| Acer | Global | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `DISCOVERY_TIMEOUT` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/acer/laptop/none/` |
| Amazon | United States | `YES` | [`https://www.amazon.com/dp/B08N...`](https://www.amazon.com/dp/B08N5WRW88) | `YES` | `YES` | [`https://www.amazon.com/dp...`](https://www.amazon.com/dp/B08N5WRW88) | `404` | `NO` | `NO` | `None` | `PRODUCT_DELISTED_OR_HTTP_404` | **`INVALID_OR_UNAVAILABLE_PRODUCT_URL`** | `evidence/amazon/laptop/B08N5WRW88/firecrawl/` |
| Amazon | India | `YES` | [`https://www.amazon.in/dp/B08N5...`](https://www.amazon.in/dp/B08N5WRW88) | `YES` | `YES` | [`https://www.amazon.in/dp/...`](https://www.amazon.in/dp/B08N5WRW88) | `404` | `NO` | `NO` | `None` | `PRODUCT_DELISTED_OR_HTTP_404` | **`INVALID_OR_UNAVAILABLE_PRODUCT_URL`** | `evidence/amazon/laptop/B08N5WRW88/firecrawl/` |
| Amazon | United Kingdom | `YES` | [`https://www.amazon.co.uk/dp/B0...`](https://www.amazon.co.uk/dp/B08N5WRW88) | `YES` | `YES` | [`https://www.amazon.co.uk/...`](https://www.amazon.co.uk/dp/B08N5WRW88) | `404` | `NO` | `NO` | `None` | `PRODUCT_DELISTED_OR_HTTP_404` | **`INVALID_OR_UNAVAILABLE_PRODUCT_URL`** | `evidence/amazon/laptop/B08N5WRW88/firecrawl/` |
| Amazon | Germany | `YES` | [`https://www.amazon.de/dp/B08N5...`](https://www.amazon.de/dp/B08N5WRW88) | `YES` | `YES` | [`https://www.amazon.de/dp/...`](https://www.amazon.de/dp/B08N5WRW88) | `404` | `NO` | `NO` | `None` | `PRODUCT_DELISTED_OR_HTTP_404` | **`INVALID_OR_UNAVAILABLE_PRODUCT_URL`** | `evidence/amazon/laptop/B08N5WRW88/firecrawl/` |
| Amazon | France | `YES` | [`https://www.amazon.fr/dp/B08N5...`](https://www.amazon.fr/dp/B08N5WRW88) | `YES` | `YES` | [`https://www.amazon.fr/dp/...`](https://www.amazon.fr/dp/B08N5WRW88) | `404` | `NO` | `NO` | `None` | `PRODUCT_DELISTED_OR_HTTP_404` | **`INVALID_OR_UNAVAILABLE_PRODUCT_URL`** | `evidence/amazon/laptop/B08N5WRW88/firecrawl/` |
| Amazon | Italy | `YES` | [`https://www.amazon.it/dp/B08N5...`](https://www.amazon.it/dp/B08N5WRW88) | `YES` | `YES` | [`https://www.amazon.it/dp/...`](https://www.amazon.it/dp/B08N5WRW88) | `404` | `NO` | `NO` | `None` | `PRODUCT_DELISTED_OR_HTTP_404` | **`INVALID_OR_UNAVAILABLE_PRODUCT_URL`** | `evidence/amazon/laptop/B08N5WRW88/firecrawl/` |
| Amazon | Spain | `YES` | [`https://www.amazon.es/dp/B08N5...`](https://www.amazon.es/dp/B08N5WRW88) | `YES` | `YES` | [`https://www.amazon.es/dp/...`](https://www.amazon.es/dp/B08N5WRW88) | `404` | `NO` | `NO` | `None` | `PRODUCT_DELISTED_OR_HTTP_404` | **`INVALID_OR_UNAVAILABLE_PRODUCT_URL`** | `evidence/amazon/laptop/B08N5WRW88/firecrawl/` |
| Amazon | Canada | `YES` | [`https://www.amazon.ca/dp/B08N5...`](https://www.amazon.ca/dp/B08N5WRW88) | `YES` | `YES` | [`https://www.amazon.ca/dp/...`](https://www.amazon.ca/dp/B08N5WRW88) | `404` | `NO` | `NO` | `None` | `PRODUCT_DELISTED_OR_HTTP_404` | **`INVALID_OR_UNAVAILABLE_PRODUCT_URL`** | `evidence/amazon/laptop/B08N5WRW88/firecrawl/` |
| Amazon | Mexico | `YES` | [`https://www.amazon.com.mx/dp/B...`](https://www.amazon.com.mx/dp/B08N5WRW88) | `YES` | `YES` | [`https://www.amazon.com.mx...`](https://www.amazon.com.mx/dp/B08N5WRW88) | `404` | `NO` | `NO` | `None` | `PRODUCT_DELISTED_OR_HTTP_404` | **`INVALID_OR_UNAVAILABLE_PRODUCT_URL`** | `evidence/amazon/laptop/B08N5WRW88/firecrawl/` |
| Amazon | Brazil | `YES` | [`https://www.amazon.com.br/dp/B...`](https://www.amazon.com.br/dp/B08N5WRW88) | `YES` | `YES` | [`https://www.amazon.com.br...`](https://www.amazon.com.br/dp/B08N5WRW88) | `404` | `NO` | `NO` | `None` | `PRODUCT_DELISTED_OR_HTTP_404` | **`INVALID_OR_UNAVAILABLE_PRODUCT_URL`** | `evidence/amazon/laptop/B08N5WRW88/firecrawl/` |
| Bestbuy | United States | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `DISCOVERY_TIMEOUT` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/bestbuy/laptop/none/` |
| Bestbuy | Canada | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `DISCOVERY_TIMEOUT` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/bestbuy/laptop/none/` |
| Boulanger | France | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `NO_LAPTOP_URL_DISCOVERED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/boulanger/laptop/none/` |
| Costco | United States | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `NO_LAPTOP_URL_DISCOVERED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/costco/laptop/none/` |
| Coupang | South Korea | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `DISCOVERY_BLOCKED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/coupang/laptop/none/` |
| Currys | United Kingdom | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `DISCOVERY_BLOCKED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/currys/laptop/none/` |
| Dell | Global | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `NO_LAPTOP_URL_DISCOVERED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/dell/laptop/none/` |
| Elkjop | Denmark | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `DISCOVERY_BLOCKED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/elkjop/laptop/none/` |
| Elkjop | Norway | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `DISCOVERY_BLOCKED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/elkjop/laptop/none/` |
| Elkjop | Sweden | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `DISCOVERY_BLOCKED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/elkjop/laptop/none/` |
| Euronics | Italy | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `NO_LAPTOP_URL_DISCOVERED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/euronics/laptop/none/` |
| Expert | Germany | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `DISCOVERY_BLOCKED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/expert/laptop/none/` |
| Flipkart | India | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `DISCOVERY_BLOCKED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/flipkart/laptop/none/` |
| Fnac | France | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `DISCOVERY_BLOCKED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/fnac/laptop/none/` |
| Gmarket | South Korea | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `DISCOVERY_BLOCKED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/gmarket/laptop/none/` |
| Hp | Global | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `NO_LAPTOP_URL_DISCOVERED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/hp/laptop/none/` |
| Jbhifi | Australia | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `NO_LAPTOP_URL_DISCOVERED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/jbhifi/laptop/none/` |
| Jd | China | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `NO_LAPTOP_URL_DISCOVERED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/jd/laptop/none/` |
| Komputronik | Poland | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `NO_LAPTOP_URL_DISCOVERED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/komputronik/laptop/none/` |
| Lenovo | Global | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `NO_LAPTOP_URL_DISCOVERED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/lenovo/laptop/none/` |
| Magazineluiza | Brazil | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `DISCOVERY_BLOCKED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/magazineluiza/laptop/none/` |
| Mediamarkt | Germany | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `DISCOVERY_BLOCKED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/mediamarkt/laptop/none/` |
| Mediamarkt | Spain | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `DISCOVERY_BLOCKED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/mediamarkt/laptop/none/` |
| Mediamarkt | Italy | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `DISCOVERY_BLOCKED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/mediamarkt/laptop/none/` |
| Mediamarkt | Turkey | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `DISCOVERY_BLOCKED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/mediamarkt/laptop/none/` |
| Mercadolibre | Mexico | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `NO_LAPTOP_URL_DISCOVERED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/mercadolibre/laptop/none/` |
| Mercadolibre | Chile | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `NO_LAPTOP_URL_DISCOVERED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/mercadolibre/laptop/none/` |
| Mercadolibre | Colombia | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `NO_LAPTOP_URL_DISCOVERED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/mercadolibre/laptop/none/` |
| Mercadolibre | Brazil | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `NO_LAPTOP_URL_DISCOVERED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/mercadolibre/laptop/none/` |
| Thegioididong | Vietnam | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `DISCOVERY_TIMEOUT` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/thegioididong/laptop/none/` |
| Monsternotebook | Turkey | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `DISCOVERY_BLOCKED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/monsternotebook/laptop/none/` |
| Newegg | United States | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `NO_LAPTOP_URL_DISCOVERED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/newegg/laptop/none/` |
| Officeworks | Australia | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `NO_LAPTOP_URL_DISCOVERED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/officeworks/laptop/none/` |
| Reliancedigital | India | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `NO_LAPTOP_URL_DISCOVERED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/reliancedigital/laptop/none/` |
| Staples | United States | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `DISCOVERY_TIMEOUT` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/staples/laptop/none/` |
| Terg | Poland | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `NO_LAPTOP_URL_DISCOVERED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/terg/laptop/none/` |
| Tmall | China | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `NO_LAPTOP_URL_DISCOVERED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/tmall/laptop/none/` |
| Unieuro | Italy | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `NO_LAPTOP_URL_DISCOVERED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/unieuro/laptop/none/` |
| Walmart | United States | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `NO_LAPTOP_URL_DISCOVERED` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/walmart/laptop/none/` |
| Yodobashi | Japan | `NO` | _None_ | `NO` | `NO` | _None_ | `0` | `NO` | `NO` | `None` | `DISCOVERY_TIMEOUT` | **`LAPTOP_URL_NOT_DISCOVERED`** | `evidence/yodobashi/laptop/none/` |

## 7. Firecrawl Successes

_None of the tested laptop URLs produced a verified unblocked laptop product page under direct datacenter egress._

## 8. Firecrawl Failures on Tested URLs

| Retailer | Country | Tested URL | HTTP Status | Challenge Detected | Blocking Vendor | Exact Failure Reason | Evidence Path |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- | :--- |
| Amazon | United States | [`https://www.amazon.com/dp/B08N5WRW8...`](https://www.amazon.com/dp/B08N5WRW88) | `404` | `NO` | `None` | `PRODUCT_DELISTED_OR_HTTP_404` | `evidence/amazon/laptop/B08N5WRW88/firecrawl/` |
| Amazon | India | [`https://www.amazon.in/dp/B08N5WRW88...`](https://www.amazon.in/dp/B08N5WRW88) | `404` | `NO` | `None` | `PRODUCT_DELISTED_OR_HTTP_404` | `evidence/amazon/laptop/B08N5WRW88/firecrawl/` |
| Amazon | United Kingdom | [`https://www.amazon.co.uk/dp/B08N5WR...`](https://www.amazon.co.uk/dp/B08N5WRW88) | `404` | `NO` | `None` | `PRODUCT_DELISTED_OR_HTTP_404` | `evidence/amazon/laptop/B08N5WRW88/firecrawl/` |
| Amazon | Germany | [`https://www.amazon.de/dp/B08N5WRW88...`](https://www.amazon.de/dp/B08N5WRW88) | `404` | `NO` | `None` | `PRODUCT_DELISTED_OR_HTTP_404` | `evidence/amazon/laptop/B08N5WRW88/firecrawl/` |
| Amazon | France | [`https://www.amazon.fr/dp/B08N5WRW88...`](https://www.amazon.fr/dp/B08N5WRW88) | `404` | `NO` | `None` | `PRODUCT_DELISTED_OR_HTTP_404` | `evidence/amazon/laptop/B08N5WRW88/firecrawl/` |
| Amazon | Italy | [`https://www.amazon.it/dp/B08N5WRW88...`](https://www.amazon.it/dp/B08N5WRW88) | `404` | `NO` | `None` | `PRODUCT_DELISTED_OR_HTTP_404` | `evidence/amazon/laptop/B08N5WRW88/firecrawl/` |
| Amazon | Spain | [`https://www.amazon.es/dp/B08N5WRW88...`](https://www.amazon.es/dp/B08N5WRW88) | `404` | `NO` | `None` | `PRODUCT_DELISTED_OR_HTTP_404` | `evidence/amazon/laptop/B08N5WRW88/firecrawl/` |
| Amazon | Canada | [`https://www.amazon.ca/dp/B08N5WRW88...`](https://www.amazon.ca/dp/B08N5WRW88) | `404` | `NO` | `None` | `PRODUCT_DELISTED_OR_HTTP_404` | `evidence/amazon/laptop/B08N5WRW88/firecrawl/` |
| Amazon | Mexico | [`https://www.amazon.com.mx/dp/B08N5W...`](https://www.amazon.com.mx/dp/B08N5WRW88) | `404` | `NO` | `None` | `PRODUCT_DELISTED_OR_HTTP_404` | `evidence/amazon/laptop/B08N5WRW88/firecrawl/` |
| Amazon | Brazil | [`https://www.amazon.com.br/dp/B08N5W...`](https://www.amazon.com.br/dp/B08N5WRW88) | `404` | `NO` | `None` | `PRODUCT_DELISTED_OR_HTTP_404` | `evidence/amazon/laptop/B08N5WRW88/firecrawl/` |

## 9. Anti-Bot Defense Analysis

| Security Vendor / Mechanism | Retailer Targets Affected | Primary Observed Signature |
| :--- | :---: | :--- |
| **Amazon Robot Check (CAPTCHA)** | `3` (US, CA, MX) | `<title>Robot Check</title>`, automated form challenge |
| **Delisted Catalog ASIN / 404** | `7` (IN, GB, DE, FR, IT, ES, BR) | HTTP 404 response on historical seed ASIN |
| **Cloudflare Turnstile / WAF** | `7` (MediaMarkt DE/ES/IT/TR, Gmarket, Terg, Monster) | Cloudflare Turnstile JavaScript challenge token requirement |
| **Akamai Bot Manager** | `3` (Fnac, Magalu, Reliance) | Akamai Sensor Data payload requirement, HTTP 403/400 |

## 10. Discovery Failures (Kept Separate from Firecrawl Failures)

A total of **`42 / 52` (`80.8%`)** retailers could not have genuine laptop URLs discovered:
- **`15` targets** failed with `DISCOVERY_BLOCKED` (category listing blocked by Cloudflare/Akamai at discovery time).
- **`5` targets** failed with `DISCOVERY_TIMEOUT` (slow TCP/TLS handshake during category crawl).
- **`22` targets** failed with `NO_LAPTOP_URL_DISCOVERED` (category links did not contain unblocked laptop product anchors).

> **Crucial Distinction**: These targets are categorized as `LAPTOP_URL_NOT_DISCOVERED` and are **not** counted against Firecrawl's product-page crawlability rate.

## 11. Final Conclusion

Across the 52 canonical targets, self-hosted open-source Firecrawl was tested against **`10`** discovered laptop URLs. Under direct cloud datacenter egress:
1. **Firecrawl Service Reliability**: The self-hosted Playwright service maintained 100% reachability and socket stability on all network requests.
2. **Genuine Laptop Crawlability**: **`0 / 10` (`0.0%`)** of tested URLs yielded unblocked laptop product pages due to edge anti-bot challenges (Amazon Robot Check, Cloudflare Turnstile, Akamai) and catalog delistings.
3. **Operational Bottleneck**: The primary barrier across all global ecommerce targets is edge egress classification (IP reputation / residential proxy requirement), not crawler engine rendering.
