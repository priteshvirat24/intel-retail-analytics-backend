# Production-Grade Multi-Site Crawl Orchestrator

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Architecture: Adaptive Crawling](https://img.shields.io/badge/architecture-adaptive_crawling-emerald.svg)](#core-architecture)
[![Evidence: Auditable Traces](https://img.shields.io/badge/evidence-auditable_traces-purple.svg)](#evidence-preservation)
[![Coverage: Honest Benchmark](https://img.shields.io/badge/benchmark-honest_measurement-amber.svg)](#most-important-rule)

A production-grade **Multi-Site Crawl Orchestrator** engineered to empirically determine, measure, and audit product/SKU data extraction capabilities across **35 global retailer brands spanning 50+ country-specific targets**.

---

## The Core Philosophy

> [!IMPORTANT]
> **NO FAKE SUCCESS**: A 200 OK without valid extracted product attributes is **never** marked as success. Missing data is preserved as `null`, conflicts between extraction sources are flagged, and bot protections/CAPTCHAs are diagnosed accurately.
> The goal is **maximum achievable coverage** and an **honest measurement** of what works and what does not.

---

## Core Architecture

```
                                  CLI / Runner
                                       │
                         ┌─────────────┴─────────────┐
                         ▼                           ▼
               Test-All Orchestrator         Targeted SKU Runner
                         │                           │
                         └─────────────┬─────────────┘
                                       ▼
                             Crawl Orchestrator
                                       │
            ┌──────────────────────────┼──────────────────────────┐
            ▼                          ▼                          ▼
     Product Discovery          Crawl Strategies          Session Manager
   - Sitemap Index / XML      - Adaptive HTTP (HTTPX)    - Per-Retailer State
   - Category / Listing Pages - Playwright (Chromium)    - User Agent / Locale
   - Direct Search API / DOM  - Scrapy Bridge (Opt)      - Rate Limiter / Delays
   - Pattern Regex Dedupe     - Retailer Adapters        - Cookie / Context Isolation
            │                          │                          │
            └──────────────────────────┼──────────────────────────┘
                                       ▼
                               Extraction Engine
                  ┌────────────────────┴────────────────────┐
                  ▼                                         ▼
         Multi-Source Extractors                   Field Conflict Engine
         - JSON-LD (Product Schema)                - Discrepancy Detection
         - Microdata / OpenGraph                   - Normalization (ISO Currencies,
         - Embedded App JSON (__NEXT_DATA__)         Strict Types, Clean Text)
         - DOM / XPath Selectors                   - Confidence Calculation
         - Visible Rendered Text Fallback
         - Retailer Custom Adapters
                                       │
                                       ▼
                         Validation & Classification
                  ┌────────────────────┴────────────────────┐
                  ▼                                         ▼
          Schema Validator                         Failure Classifier
          - Field Completeness                     - 28+ Machine Categories
          - Validity Checks (Price,                - Root-Cause Stage Tracker
            Title, Stock, Identifier)              - Retry Decision Engine
                                       │
                                       ▼
                                Evidence Store
                  ┌────────────────────┴────────────────────┐
                  ▼                                         ▼
            Raw Evidence                             Processed Results
            - Raw HTML / DOM Snaps                   - Normalized JSON
            - Playwright Screenshots                - Request / Response Logs
            - Audit Metadata                         - Retry Traces
                                       │
                                       ▼
                          Evaluation & Reporting
                  ┌────────────────────┴────────────────────┐
                  ▼                    ▼                    ▼
             JSON Report          Markdown Report      HTML Dashboard
            (Auditable Data)     (Executive Summary)  (Interactive Matrix)
```

---

## Target Retailer Coverage (35 Brands / 52 Country Targets)

| Retailer Brand | Countries / Target IDs | Primary Strategy |
| :--- | :--- | :--- |
| **Agres** | `agres-id` (ID) | HTTP-first |
| **Acer** | `acer-global` (Global) | HTTP-first |
| **Amazon** | `amazon-br`, `amazon-ca`, `amazon-de`, `amazon-es`, `amazon-fr`, `amazon-gb`, `amazon-in`, `amazon-it`, `amazon-mx`, `amazon-us` | Adaptive Escalation + Adapter |
| **Best Buy** | `bestbuy-ca`, `bestbuy-us` | Adaptive Escalation + Adapter |
| **Boulanger** | `boulanger-fr` (FR) | HTTP-first |
| **Costco** | `costco-us` (US) | HTTP-first |
| **Coupang** | `coupang-kr` (KR) | Playwright Chromium |
| **Currys Group** | `currys-gb` (GB) | HTTP-first |
| **Dell** | `dell-global` (Global) | HTTP-first |
| **Elkjop** | `elkjop-dk` (DK), `elkjop-no` (NO), `elkjop-se` (SE) | HTTP-first |
| **Euronics** | `euronics-it` (IT) | HTTP-first |
| **EXPERT** | `expert-de` (DE) | HTTP-first |
| **Flipkart** | `flipkart-in` (IN) | Adaptive Escalation + Adapter |
| **FNAC** | `fnac-fr` (FR) | HTTP-first |
| **Gmarket** | `gmarket-kr` (KR) | HTTP-first |
| **HP** | `hp-global` (Global) | HTTP-first |
| **JB Hi-Fi** | `jbhifi-au` (AU) | HTTP-first |
| **JD.com** | `jd-cn` (CN) | HTTP-first |
| **Komputronik** | `komputronik-pl` (PL) | HTTP-first |
| **Lenovo** | `lenovo-global` (Global) | HTTP-first |
| **Magazine Luiza**| `magazineluiza-br` (BR) | HTTP-first |
| **MediaMarkt** | `mediamarkt-de`, `mediamarkt-es`, `mediamarkt-it`, `mediamarkt-tr` | Adaptive Escalation + Adapter |
| **Mercado Libre**| `mercadolibre-cl`, `mercadolibre-co`, `mercadolibre-mx` | Adaptive Escalation + Adapter |
| **Mercado Livre**| `mercadolivre-br` (BR) | Adaptive Escalation + Adapter |
| **Mobile World** | `mobileworld-vn` (VN) | HTTP-first |
| **Monster Focus**| `monsterfocus-tr` (TR) | HTTP-first |
| **Newegg** | `newegg-us` (US) | HTTP-first |
| **Officeworks** | `officeworks-au` (AU) | HTTP-first |
| **Reliance Digital** | `reliancedigital-in` (IN) | HTTP-first |
| **Staples** | `staples-us` (US) | HTTP-first |
| **TERG** | `terg-pl` (PL) | HTTP-first |
| **Tmall** | `tmall-cn` (CN) | Playwright Chromium |
| **UNIEURO** | `unieuro-it` (IT) | HTTP-first |
| **Walmart** | `walmart-us` (US) | Next.js Hydration Adapter |
| **Yodobashi** | `yodobashi-jp` (JP) | HTTP-first |

---

## Quickstart & Installation

```bash
# 1. Clone repository
git clone https://github.com/your-org/crawl-orchestrator.git
cd crawl-orchestrator

# 2. Setup Virtual Environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install --upgrade pip
pip install -e .
```

---

## CLI Usage

### 1. List All Configured Targets
```bash
python -m orchestrator list-retailers
```

### 2. Test a Single Retailer Target (e.g. Amazon India)
```bash
python -m orchestrator test amazon-in --limit 20
```

### 3. Test Flipkart India
```bash
python -m orchestrator test flipkart-in --limit 20
```

### 4. Test All Configured Retailers
```bash
python -m orchestrator test-all --limit 20 --save-evidence --report
```

---

## Automated Test Suite

Run unit and integration tests (including local mock server):
```bash
pytest tests/ -v
```

---

## Evidence & Reports

- **Auditable Evidence**: Stored in `evidence/<retailer>/<country>/<sku_id>/`
- **JSON Audit Report**: `reports/crawl_report.json`
- **CSV Matrix**: `reports/retailer_matrix.csv`
- **Markdown Summary**: `reports/crawl_report.md`
- **Interactive HTML Dashboard**: `reports/dashboard.html`

---

## Docker Deployment

```bash
# Build and run full benchmark in Docker
docker compose up --build
```
Open `http://localhost:8080/dashboard.html` to view the live dashboard.
