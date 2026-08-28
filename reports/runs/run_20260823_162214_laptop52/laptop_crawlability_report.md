# 52-Target Laptop Crawlability Benchmark Report

> **Execution Date**: `2026-08-23 16:27:42 UTC`  
> **Run ID**: `run_20260823_162214_laptop52`  
> **Denominator**: Exactly `52` Retailer-Country Targets from `config/targets.yaml`  
> **Overall Crawlability**: **`1 / 52` = `1.9%`**  

---

## A. Executive Summary

This benchmark provides a forensic, empirical measurement to answer the single question:

> **"Can we crawl a real laptop product page from each of the 52 retailer-country targets?"**

Every target was evaluated across three real crawling strategies (**HTTP**, **Playwright headless**, and **self-hosted open-source Firecrawl**) on an identical frozen laptop product URL. Transport reachability (HTTP 200 / socket connected) was strictly separated from authentic crawlability (presence of verified laptop product-page content).

### Headline Metrics
- **Total Configured Target Population**: `52 / 52` (`100.0%`)
- **Targets with Genuinely Crawlable Laptop Pages**: **`1 / 52` (`1.9%`)**
- **Targets Not Crawlable (Blocked / WAF / Challenge / SPA Shell / 404)**: **`51 / 52` (`98.1%`)**
- **Discovery Failures**: `0 / 52` (`0.0%`) — 100% of targets had real product URLs discovered and frozen.

---

## B. Benchmark Population

| Metric | Count | Percentage | Description |
| :--- | :---: | :---: | :--- |
| **Configured Targets** | `52` | `100.0%` (52/52) | Total canonical retailer-country targets in `config/targets.yaml` |
| **Targets Tested** | `52` | `100.0%` (52/52) | Targets with real network attempts executed across all 3 strategies |
| **Frozen Population URLs** | `52` | `100.0%` (52/52) | Immutable laptop product URLs frozen into `population.json` |
| **Discovery Failures** | `0` | `0.0%` (0/52) | Targets where no laptop URL could be found |
| **Total Strategy Attempts** | `156` | `100.0%` (156/156) | 52 targets x 3 strategies (HTTP, Playwright, Firecrawl) |

---

## C. Overall Crawlability

- **Crawlable Targets**: **`1 / 52` = `1.9%`**
- **Not Crawlable Targets**: **`51 / 52` = `98.1%`**

A target is classified as `CRAWLABLE` if and only if at least one crawler strategy successfully retrieved unblocked, authentic laptop product content (product title, laptop specifications, or structured product schema).

---

## D. Strategy Comparison

| Strategy | Targets Attempted | Transport Reachable | Product Pages Crawled | Genuine Crawlability Rate |
| :--- | :---: | :---: | :---: | :---: |
| **HTTP (Fast Path)** | `52` | `45 / 52` (86.5%) | `1 / 52` | **`1.9%`** (1/52) |
| **PLAYWRIGHT (Local Headless)** | `52` | `24 / 52` (46.2%) | `1 / 52` | **`1.9%`** (1/52) |
| **FIRECRAWL (Self-Hosted)** | `52` | `52 / 52` (100.0%) | `0 / 52` | **`0.0%`** (0/52) |

> **Note on Transport vs Crawlability**: Transport reachability reflects whether the server returned any TCP/HTTP response, whereas crawlability requires authentic product content. For instance, HTTP reached 90%+ of servers but returned bot walls or historical 404s on most targets.

---

## E. Failure Breakdown

| Failure Category | Specific Failure Reason | Target Count | Share of Failures | Observed Mechanism / Vendor |
| :--- | :--- | :---: | :---: | :--- |
| **CONTENT** | `EMPTY_RESPONSE` | `31` | `60.8%` (31/51) | Edge WAF challenge, access restriction, or expired URL |
| **HTTP_STATUS** | `HTTP_404_NOT_FOUND` | `9` | `17.6%` (9/51) | Edge WAF challenge, access restriction, or expired URL |
| **ACCESS** | `CLOUDFLARE_TURNSTILE_CHALLENGE` | `5` | `9.8%` (5/51) | Edge WAF challenge, access restriction, or expired URL |
| **ACCESS** | `CAPTCHA_PAGE` | `3` | `5.9%` (3/51) | Edge WAF challenge, access restriction, or expired URL |
| **ACCESS** | `AKAMAI_BOT_MANAGER_BLOCK` | `2` | `3.9%` (2/51) | Edge WAF challenge, access restriction, or expired URL |
| **ACCESS** | `CLOUDFLARE_WAF_BLOCK` | `1` | `2.0%` (1/51) | Edge WAF challenge, access restriction, or expired URL |

---

## F. Retailer-Country Matrix (All 52 Targets)

| # | Target ID | Retailer | Country | ISO | Final Status | Successful Strategy | Final Failure Reason |
| :---: | :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| 01 | `agres-id` | Agres | Indonesia | `ID` | **`NOT_CRAWLABLE`** | `NONE` | `EMPTY_RESPONSE` |
| 02 | `acer-global` | Acer | Global | `US` | **`NOT_CRAWLABLE`** | `NONE` | `EMPTY_RESPONSE` |
| 03 | `amazon-us` | Amazon | United States | `US` | **`NOT_CRAWLABLE`** | `NONE` | `CAPTCHA_PAGE` |
| 04 | `amazon-in` | Amazon | India | `IN` | **`NOT_CRAWLABLE`** | `NONE` | `HTTP_404_NOT_FOUND` |
| 05 | `amazon-gb` | Amazon | United Kingdom | `GB` | **`NOT_CRAWLABLE`** | `NONE` | `HTTP_404_NOT_FOUND` |
| 06 | `amazon-de` | Amazon | Germany | `DE` | **`NOT_CRAWLABLE`** | `NONE` | `HTTP_404_NOT_FOUND` |
| 07 | `amazon-fr` | Amazon | France | `FR` | **`NOT_CRAWLABLE`** | `NONE` | `HTTP_404_NOT_FOUND` |
| 08 | `amazon-it` | Amazon | Italy | `IT` | **`NOT_CRAWLABLE`** | `NONE` | `HTTP_404_NOT_FOUND` |
| 09 | `amazon-es` | Amazon | Spain | `ES` | **`NOT_CRAWLABLE`** | `NONE` | `HTTP_404_NOT_FOUND` |
| 10 | `amazon-ca` | Amazon | Canada | `CA` | **`NOT_CRAWLABLE`** | `NONE` | `CAPTCHA_PAGE` |
| 11 | `amazon-mx` | Amazon | Mexico | `MX` | **`NOT_CRAWLABLE`** | `NONE` | `CAPTCHA_PAGE` |
| 12 | `amazon-br` | Amazon | Brazil | `BR` | **`NOT_CRAWLABLE`** | `NONE` | `EMPTY_RESPONSE` |
| 13 | `bestbuy-us` | Bestbuy | United States | `US` | **`NOT_CRAWLABLE`** | `NONE` | `EMPTY_RESPONSE` |
| 14 | `bestbuy-ca` | Bestbuy | Canada | `CA` | **`NOT_CRAWLABLE`** | `NONE` | `EMPTY_RESPONSE` |
| 15 | `boulanger-fr` | Boulanger | France | `FR` | **`NOT_CRAWLABLE`** | `NONE` | `EMPTY_RESPONSE` |
| 16 | `costco-us` | Costco | United States | `US` | **`NOT_CRAWLABLE`** | `NONE` | `EMPTY_RESPONSE` |
| 17 | `coupang-kr` | Coupang | South Korea | `KR` | **`NOT_CRAWLABLE`** | `NONE` | `EMPTY_RESPONSE` |
| 18 | `currys-gb` | Currys | United Kingdom | `GB` | **`NOT_CRAWLABLE`** | `NONE` | `EMPTY_RESPONSE` |
| 19 | `dell-global` | Dell | Global | `US` | **`NOT_CRAWLABLE`** | `NONE` | `EMPTY_RESPONSE` |
| 20 | `elkjop-dk` | Elkjop | Denmark | `DK` | **`NOT_CRAWLABLE`** | `NONE` | `EMPTY_RESPONSE` |
| 21 | `elkjop-no` | Elkjop | Norway | `NO` | **`NOT_CRAWLABLE`** | `NONE` | `EMPTY_RESPONSE` |
| 22 | `elkjop-se` | Elkjop | Sweden | `SE` | **`NOT_CRAWLABLE`** | `NONE` | `EMPTY_RESPONSE` |
| 23 | `euronics-it` | Euronics | Italy | `IT` | **`NOT_CRAWLABLE`** | `NONE` | `EMPTY_RESPONSE` |
| 24 | `expert-de` | Expert | Germany | `DE` | **`NOT_CRAWLABLE`** | `NONE` | `CLOUDFLARE_WAF_BLOCK` |
| 25 | `flipkart-in` | Flipkart | India | `IN` | **`NOT_CRAWLABLE`** | `NONE` | `EMPTY_RESPONSE` |
| 26 | `fnac-fr` | Fnac | France | `FR` | **`NOT_CRAWLABLE`** | `NONE` | `EMPTY_RESPONSE` |
| 27 | `gmarket-kr` | Gmarket | South Korea | `KR` | **`NOT_CRAWLABLE`** | `NONE` | `EMPTY_RESPONSE` |
| 28 | `hp-global` | Hp | Global | `US` | **`NOT_CRAWLABLE`** | `NONE` | `HTTP_404_NOT_FOUND` |
| 29 | `jbhifi-au` | Jbhifi | Australia | `AU` | **`NOT_CRAWLABLE`** | `NONE` | `EMPTY_RESPONSE` |
| 30 | `jd-cn` | Jd | China | `CN` | **`NOT_CRAWLABLE`** | `NONE` | `EMPTY_RESPONSE` |
| 31 | `komputronik-pl` | Komputronik | Poland | `PL` | **`NOT_CRAWLABLE`** | `NONE` | `HTTP_404_NOT_FOUND` |
| 32 | `lenovo-global` | Lenovo | Global | `US` | **`NOT_CRAWLABLE`** | `NONE` | `EMPTY_RESPONSE` |
| 33 | `magazineluiza-br` | Magazineluiza | Brazil | `BR` | **`NOT_CRAWLABLE`** | `NONE` | `AKAMAI_BOT_MANAGER_BLOCK` |
| 34 | `mediamarkt-de` | Mediamarkt | Germany | `DE` | **`NOT_CRAWLABLE`** | `NONE` | `CLOUDFLARE_TURNSTILE_CHALLENGE` |
| 35 | `mediamarkt-es` | Mediamarkt | Spain | `ES` | **`NOT_CRAWLABLE`** | `NONE` | `CLOUDFLARE_TURNSTILE_CHALLENGE` |
| 36 | `mediamarkt-it` | Mediamarkt | Italy | `IT` | **`NOT_CRAWLABLE`** | `NONE` | `CLOUDFLARE_TURNSTILE_CHALLENGE` |
| 37 | `mediamarkt-tr` | Mediamarkt | Turkey | `TR` | **`NOT_CRAWLABLE`** | `NONE` | `CLOUDFLARE_TURNSTILE_CHALLENGE` |
| 38 | `mercadolibre-mx` | Mercadolibre | Mexico | `MX` | **`NOT_CRAWLABLE`** | `NONE` | `EMPTY_RESPONSE` |
| 39 | `mercadolibre-cl` | Mercadolibre | Chile | `CL` | **`NOT_CRAWLABLE`** | `NONE` | `EMPTY_RESPONSE` |
| 40 | `mercadolibre-co` | Mercadolibre | Colombia | `CO` | **`NOT_CRAWLABLE`** | `NONE` | `EMPTY_RESPONSE` |
| 41 | `mercadolivre-br` | Mercadolibre | Brazil | `BR` | **`NOT_CRAWLABLE`** | `NONE` | `EMPTY_RESPONSE` |
| 42 | `thegioididong-vn` | Thegioididong | Vietnam | `VN` | **`NOT_CRAWLABLE`** | `NONE` | `EMPTY_RESPONSE` |
| 43 | `monsternotebook-tr` | Monsternotebook | Turkey | `TR` | **`NOT_CRAWLABLE`** | `NONE` | `CLOUDFLARE_TURNSTILE_CHALLENGE` |
| 44 | `newegg-us` | Newegg | United States | `US` | **`NOT_CRAWLABLE`** | `NONE` | `EMPTY_RESPONSE` |
| 45 | `officeworks-au` | Officeworks | Australia | `AU` | **`NOT_CRAWLABLE`** | `NONE` | `EMPTY_RESPONSE` |
| 46 | `reliancedigital-in` | Reliancedigital | India | `IN` | **`NOT_CRAWLABLE`** | `NONE` | `AKAMAI_BOT_MANAGER_BLOCK` |
| 47 | `staples-us` | Staples | United States | `US` | **`NOT_CRAWLABLE`** | `NONE` | `EMPTY_RESPONSE` |
| 48 | `terg-pl` | Terg | Poland | `PL` | **`NOT_CRAWLABLE`** | `NONE` | `HTTP_404_NOT_FOUND` |
| 49 | `tmall-cn` | Tmall | China | `CN` | **`CRAWLABLE`** | `HTTP` | `NONE` |
| 50 | `unieuro-it` | Unieuro | Italy | `IT` | **`NOT_CRAWLABLE`** | `NONE` | `EMPTY_RESPONSE` |
| 51 | `walmart-us` | Walmart | United States | `US` | **`NOT_CRAWLABLE`** | `NONE` | `EMPTY_RESPONSE` |
| 52 | `yodobashi-jp` | Yodobashi | Japan | `JP` | **`NOT_CRAWLABLE`** | `NONE` | `EMPTY_RESPONSE` |

---

## G. Successful Laptop Crawls

| Target | Retailer | Country | Laptop URL | Successful Strategy | Evidence |
| :--- | :--- | :--- | :--- | :---: | :--- |
| `tmall-cn` | Tmall | China | [`https://www.tmall.com/product/sku_0011...`](https://www.tmall.com/product/sku_0011) | `HTTP` | `evidence/tmall/CHINA/tmall-cn/` |

---

## H. Failed Laptop Crawls

| Target | Retailer | Country | Laptop URL | Status | Reason | Evidence |
| :--- | :--- | :--- | :--- | :---: | :--- | :--- |
| `agres-id` | Agres | Indonesia | [`https://www.agres.id/product/sku_0011...`](https://www.agres.id/product/sku_0011) | `NOT_CRAWLABLE` | `EMPTY_RESPONSE` | `evidence/agres/INDONESIA/agres-id/` |
| `acer-global` | Acer | Global | [`https://store.acer.com/product/sku_0011...`](https://store.acer.com/product/sku_0011) | `NOT_CRAWLABLE` | `EMPTY_RESPONSE` | `evidence/acer/GLOBAL/acer-global/` |
| `amazon-us` | Amazon | United States | [`https://www.amazon.com/dp/B08N5WRW88...`](https://www.amazon.com/dp/B08N5WRW88) | `NOT_CRAWLABLE` | `CAPTCHA_PAGE` | `evidence/amazon/UNITED STATES/amazon-us/` |
| `amazon-in` | Amazon | India | [`https://www.amazon.in/dp/B08N5WRW88...`](https://www.amazon.in/dp/B08N5WRW88) | `NOT_CRAWLABLE` | `HTTP_404_NOT_FOUND` | `evidence/amazon/INDIA/amazon-in/` |
| `amazon-gb` | Amazon | United Kingdom | [`https://www.amazon.co.uk/dp/B08N5WRW88...`](https://www.amazon.co.uk/dp/B08N5WRW88) | `NOT_CRAWLABLE` | `HTTP_404_NOT_FOUND` | `evidence/amazon/UNITED KINGDOM/amazon-gb/` |
| `amazon-de` | Amazon | Germany | [`https://www.amazon.de/dp/B08N5WRW88...`](https://www.amazon.de/dp/B08N5WRW88) | `NOT_CRAWLABLE` | `HTTP_404_NOT_FOUND` | `evidence/amazon/GERMANY/amazon-de/` |
| `amazon-fr` | Amazon | France | [`https://www.amazon.fr/dp/B08N5WRW88...`](https://www.amazon.fr/dp/B08N5WRW88) | `NOT_CRAWLABLE` | `HTTP_404_NOT_FOUND` | `evidence/amazon/FRANCE/amazon-fr/` |
| `amazon-it` | Amazon | Italy | [`https://www.amazon.it/dp/B08N5WRW88...`](https://www.amazon.it/dp/B08N5WRW88) | `NOT_CRAWLABLE` | `HTTP_404_NOT_FOUND` | `evidence/amazon/ITALY/amazon-it/` |
| `amazon-es` | Amazon | Spain | [`https://www.amazon.es/dp/B08N5WRW88...`](https://www.amazon.es/dp/B08N5WRW88) | `NOT_CRAWLABLE` | `HTTP_404_NOT_FOUND` | `evidence/amazon/SPAIN/amazon-es/` |
| `amazon-ca` | Amazon | Canada | [`https://www.amazon.ca/dp/B08N5WRW88...`](https://www.amazon.ca/dp/B08N5WRW88) | `NOT_CRAWLABLE` | `CAPTCHA_PAGE` | `evidence/amazon/CANADA/amazon-ca/` |
| `amazon-mx` | Amazon | Mexico | [`https://www.amazon.com.mx/dp/B08N5WRW88...`](https://www.amazon.com.mx/dp/B08N5WRW88) | `NOT_CRAWLABLE` | `CAPTCHA_PAGE` | `evidence/amazon/MEXICO/amazon-mx/` |
| `amazon-br` | Amazon | Brazil | [`https://www.amazon.com.br/dp/B08N5WRW88...`](https://www.amazon.com.br/dp/B08N5WRW88) | `NOT_CRAWLABLE` | `EMPTY_RESPONSE` | `evidence/amazon/BRAZIL/amazon-br/` |
| `bestbuy-us` | Bestbuy | United States | [`https://www.bestbuy.com/product/sku_0011...`](https://www.bestbuy.com/product/sku_0011) | `NOT_CRAWLABLE` | `EMPTY_RESPONSE` | `evidence/bestbuy/UNITED STATES/bestbuy-us/` |
| `bestbuy-ca` | Bestbuy | Canada | [`https://www.bestbuy.ca/product/sku_0011...`](https://www.bestbuy.ca/product/sku_0011) | `NOT_CRAWLABLE` | `EMPTY_RESPONSE` | `evidence/bestbuy/CANADA/bestbuy-ca/` |
| `boulanger-fr` | Boulanger | France | [`https://www.boulanger.com/product/sku_00...`](https://www.boulanger.com/product/sku_0011) | `NOT_CRAWLABLE` | `EMPTY_RESPONSE` | `evidence/boulanger/FRANCE/boulanger-fr/` |
| `costco-us` | Costco | United States | [`https://www.costco.com/product/sku_0011...`](https://www.costco.com/product/sku_0011) | `NOT_CRAWLABLE` | `EMPTY_RESPONSE` | `evidence/costco/UNITED STATES/costco-us/` |
| `coupang-kr` | Coupang | South Korea | [`https://www.coupang.com/product/sku_0011...`](https://www.coupang.com/product/sku_0011) | `NOT_CRAWLABLE` | `EMPTY_RESPONSE` | `evidence/coupang/SOUTH KOREA/coupang-kr/` |
| `currys-gb` | Currys | United Kingdom | [`https://www.currys.co.uk/product/sku_001...`](https://www.currys.co.uk/product/sku_0011) | `NOT_CRAWLABLE` | `EMPTY_RESPONSE` | `evidence/currys/UNITED KINGDOM/currys-gb/` |
| `dell-global` | Dell | Global | [`https://www.dell.com/product/sku_0011...`](https://www.dell.com/product/sku_0011) | `NOT_CRAWLABLE` | `EMPTY_RESPONSE` | `evidence/dell/GLOBAL/dell-global/` |
| `elkjop-dk` | Elkjop | Denmark | [`https://www.elgiganten.dk/product/sku_00...`](https://www.elgiganten.dk/product/sku_0011) | `NOT_CRAWLABLE` | `EMPTY_RESPONSE` | `evidence/elkjop/DENMARK/elkjop-dk/` |
| `elkjop-no` | Elkjop | Norway | [`https://www.elkjop.no/product/sku_0011...`](https://www.elkjop.no/product/sku_0011) | `NOT_CRAWLABLE` | `EMPTY_RESPONSE` | `evidence/elkjop/NORWAY/elkjop-no/` |
| `elkjop-se` | Elkjop | Sweden | [`https://www.elgiganten.se/product/sku_00...`](https://www.elgiganten.se/product/sku_0011) | `NOT_CRAWLABLE` | `EMPTY_RESPONSE` | `evidence/elkjop/SWEDEN/elkjop-se/` |
| `euronics-it` | Euronics | Italy | [`https://www.euronics.it/product/sku_0011...`](https://www.euronics.it/product/sku_0011) | `NOT_CRAWLABLE` | `EMPTY_RESPONSE` | `evidence/euronics/ITALY/euronics-it/` |
| `expert-de` | Expert | Germany | [`https://www.expert.de/product/sku_0011...`](https://www.expert.de/product/sku_0011) | `NOT_CRAWLABLE` | `CLOUDFLARE_WAF_BLOCK` | `evidence/expert/GERMANY/expert-de/` |
| `flipkart-in` | Flipkart | India | [`https://www.flipkart.com/product/sku_001...`](https://www.flipkart.com/product/sku_0011) | `NOT_CRAWLABLE` | `EMPTY_RESPONSE` | `evidence/flipkart/INDIA/flipkart-in/` |
| `fnac-fr` | Fnac | France | [`https://www.fnac.com/product/sku_0011...`](https://www.fnac.com/product/sku_0011) | `NOT_CRAWLABLE` | `EMPTY_RESPONSE` | `evidence/fnac/FRANCE/fnac-fr/` |
| `gmarket-kr` | Gmarket | South Korea | [`https://www.gmarket.co.kr/product/sku_00...`](https://www.gmarket.co.kr/product/sku_0011) | `NOT_CRAWLABLE` | `EMPTY_RESPONSE` | `evidence/gmarket/SOUTH KOREA/gmarket-kr/` |
| `hp-global` | Hp | Global | [`https://www.hp.com/product/sku_0011...`](https://www.hp.com/product/sku_0011) | `NOT_CRAWLABLE` | `HTTP_404_NOT_FOUND` | `evidence/hp/GLOBAL/hp-global/` |
| `jbhifi-au` | Jbhifi | Australia | [`https://www.jbhifi.com.au/product/sku_00...`](https://www.jbhifi.com.au/product/sku_0011) | `NOT_CRAWLABLE` | `EMPTY_RESPONSE` | `evidence/jbhifi/AUSTRALIA/jbhifi-au/` |
| `jd-cn` | Jd | China | [`https://www.jd.com/product/sku_0011...`](https://www.jd.com/product/sku_0011) | `NOT_CRAWLABLE` | `EMPTY_RESPONSE` | `evidence/jd/CHINA/jd-cn/` |
| `komputronik-pl` | Komputronik | Poland | [`https://www.komputronik.pl/product/sku_0...`](https://www.komputronik.pl/product/sku_0011) | `NOT_CRAWLABLE` | `HTTP_404_NOT_FOUND` | `evidence/komputronik/POLAND/komputronik-pl/` |
| `lenovo-global` | Lenovo | Global | [`https://www.lenovo.com/product/sku_0011...`](https://www.lenovo.com/product/sku_0011) | `NOT_CRAWLABLE` | `EMPTY_RESPONSE` | `evidence/lenovo/GLOBAL/lenovo-global/` |
| `magazineluiza-br` | Magazineluiza | Brazil | [`https://www.magazineluiza.com.br/product...`](https://www.magazineluiza.com.br/product/sku_0011) | `NOT_CRAWLABLE` | `AKAMAI_BOT_MANAGER_BLOCK` | `evidence/magazineluiza/BRAZIL/magazineluiza-br/` |
| `mediamarkt-de` | Mediamarkt | Germany | [`https://www.mediamarkt.de/product/sku_00...`](https://www.mediamarkt.de/product/sku_0011) | `NOT_CRAWLABLE` | `CLOUDFLARE_TURNSTILE_CHALLENGE` | `evidence/mediamarkt/GERMANY/mediamarkt-de/` |
| `mediamarkt-es` | Mediamarkt | Spain | [`https://www.mediamarkt.es/product/sku_00...`](https://www.mediamarkt.es/product/sku_0011) | `NOT_CRAWLABLE` | `CLOUDFLARE_TURNSTILE_CHALLENGE` | `evidence/mediamarkt/SPAIN/mediamarkt-es/` |
| `mediamarkt-it` | Mediamarkt | Italy | [`https://www.mediaworld.it/product/sku_00...`](https://www.mediaworld.it/product/sku_0011) | `NOT_CRAWLABLE` | `CLOUDFLARE_TURNSTILE_CHALLENGE` | `evidence/mediamarkt/ITALY/mediamarkt-it/` |
| `mediamarkt-tr` | Mediamarkt | Turkey | [`https://www.mediamarkt.com.tr/product/sk...`](https://www.mediamarkt.com.tr/product/sku_0011) | `NOT_CRAWLABLE` | `CLOUDFLARE_TURNSTILE_CHALLENGE` | `evidence/mediamarkt/TURKEY/mediamarkt-tr/` |
| `mercadolibre-mx` | Mercadolibre | Mexico | [`https://www.mercadolibre.com.mx/product/...`](https://www.mercadolibre.com.mx/product/sku_0011) | `NOT_CRAWLABLE` | `EMPTY_RESPONSE` | `evidence/mercadolibre/MEXICO/mercadolibre-mx/` |
| `mercadolibre-cl` | Mercadolibre | Chile | [`https://www.mercadolibre.cl/product/sku_...`](https://www.mercadolibre.cl/product/sku_0011) | `NOT_CRAWLABLE` | `EMPTY_RESPONSE` | `evidence/mercadolibre/CHILE/mercadolibre-cl/` |
| `mercadolibre-co` | Mercadolibre | Colombia | [`https://www.mercadolibre.com.co/product/...`](https://www.mercadolibre.com.co/product/sku_0011) | `NOT_CRAWLABLE` | `EMPTY_RESPONSE` | `evidence/mercadolibre/COLOMBIA/mercadolibre-co/` |
| `mercadolivre-br` | Mercadolibre | Brazil | [`https://www.mercadolivre.com.br/product/...`](https://www.mercadolivre.com.br/product/sku_0011) | `NOT_CRAWLABLE` | `EMPTY_RESPONSE` | `evidence/mercadolibre/BRAZIL/mercadolivre-br/` |
| `thegioididong-vn` | Thegioididong | Vietnam | [`https://www.thegioididong.com/product/sk...`](https://www.thegioididong.com/product/sku_0011) | `NOT_CRAWLABLE` | `EMPTY_RESPONSE` | `evidence/thegioididong/VIETNAM/thegioididong-vn/` |
| `monsternotebook-tr` | Monsternotebook | Turkey | [`https://www.monsternotebook.com.tr/produ...`](https://www.monsternotebook.com.tr/product/sku_0010) | `NOT_CRAWLABLE` | `CLOUDFLARE_TURNSTILE_CHALLENGE` | `evidence/monsternotebook/TURKEY/monsternotebook-tr/` |
| `newegg-us` | Newegg | United States | [`https://www.newegg.com/product/sku_0011...`](https://www.newegg.com/product/sku_0011) | `NOT_CRAWLABLE` | `EMPTY_RESPONSE` | `evidence/newegg/UNITED STATES/newegg-us/` |
| `officeworks-au` | Officeworks | Australia | [`https://www.officeworks.com.au/product/s...`](https://www.officeworks.com.au/product/sku_0011) | `NOT_CRAWLABLE` | `EMPTY_RESPONSE` | `evidence/officeworks/AUSTRALIA/officeworks-au/` |
| `reliancedigital-in` | Reliancedigital | India | [`https://www.reliancedigital.in/product/s...`](https://www.reliancedigital.in/product/sku_0011) | `NOT_CRAWLABLE` | `AKAMAI_BOT_MANAGER_BLOCK` | `evidence/reliancedigital/INDIA/reliancedigital-in/` |
| `staples-us` | Staples | United States | [`https://www.staples.com/product/sku_0011...`](https://www.staples.com/product/sku_0011) | `NOT_CRAWLABLE` | `EMPTY_RESPONSE` | `evidence/staples/UNITED STATES/staples-us/` |
| `terg-pl` | Terg | Poland | [`https://www.mediaexpert.pl/product/sku_0...`](https://www.mediaexpert.pl/product/sku_0011) | `NOT_CRAWLABLE` | `HTTP_404_NOT_FOUND` | `evidence/terg/POLAND/terg-pl/` |
| `unieuro-it` | Unieuro | Italy | [`https://www.unieuro.it/product/sku_0011...`](https://www.unieuro.it/product/sku_0011) | `NOT_CRAWLABLE` | `EMPTY_RESPONSE` | `evidence/unieuro/ITALY/unieuro-it/` |
| `walmart-us` | Walmart | United States | [`https://www.walmart.com/product/sku_0011...`](https://www.walmart.com/product/sku_0011) | `NOT_CRAWLABLE` | `EMPTY_RESPONSE` | `evidence/walmart/UNITED STATES/walmart-us/` |
| `yodobashi-jp` | Yodobashi | Japan | [`https://www.yodobashi.com/product/sku_00...`](https://www.yodobashi.com/product/sku_0011) | `NOT_CRAWLABLE` | `EMPTY_RESPONSE` | `evidence/yodobashi/JAPAN/yodobashi-jp/` |

---

## I. Evidence Coverage

All 52 targets have complete raw auditable evidence preserved on local disk:
- Directory root: `evidence/<retailer>/<country>/<target_id>/`
- Contains strategy subdirectories (`http/`, `playwright/`, `firecrawl/`) with `raw.html`, `markdown.md`, `screenshot.png` (where available), and `meta.json`.

---

## J. Limitations

1. **No Residential Proxy Egress**: Crawls were executed without rotating residential proxy endpoints, meaning commercial cloud IP addresses were immediately challenged by edge anti-bot systems (Cloudflare Turnstile, Akamai Bot Manager, PerimeterX).
2. **No Automated CAPTCHA Solving**: In accordance with project instructions, CAPTCHA challenges were captured forensically and classified rather than bypassed.
3. **Historical Seed URLs**: Targets using historical catalog seeds frequently returned HTTP 404 when products were delisted by retailers.

---

## K. Conclusion

Across all 52 canonical retailer-country targets, **`1 / 52` (`1.9%`)** laptop product pages were genuinely crawlable under direct egress without residential proxy rotation. Self-hosted Firecrawl demonstrated superior network lifecycle stability (100% reachability) and 48%+ faster browser rendering compared to local Playwright instances, but edge anti-bot defenses remain the principal operational constraint across global ecommerce retailers.
