# Bright Data Complete Documentation Suite

Welcome to the locally downloaded and structured repository of Bright Data's complete documentation.

## Summary of Contents

- **Total Documentation Pages**: 1249 individual markdown files
- **Total Categories**: 10 distinct functional categories
- **All-In-One Full Dump**: [`llms-full.txt`](llms-full.txt) (5.4MB comprehensive text/markdown dump)
- **Agent & LLM Index**: [`llms.txt`](llms.txt) (curated task-based navigation index)
- **Table of Contents**: [`toc.md`](toc.md) and [`toc.json`](toc.json)
- **Official Sitemap**: [`sitemap.xml`](sitemap.xml)

## Documentation Category Overview

| Category | Description | Pages | Quick Link |
|---|---|---|---|
| **Ai** | AI Agents, Bright Data MCP server, agent skills, LLM references, and cookbooks. | `42` | [Browse](ai/agents.md) |
| **Api Reference** | Complete REST API endpoints for scrapers, unblockers, SERP, accounts, and SDKs. | `347` | [Browse](api-reference/SDK.md) |
| **Cli** | Bright Data CLI installation, commands, zone management, and script automation. | `5` | [Browse](cli/commands.md) |
| **Cn** | Documentation pages under `cn/`. | `475` | [Browse](cn/ai/agents.md) |
| **Datasets** | 1300+ pre-built scrapers (LinkedIn, Amazon, Instagram, etc.) and Marketplace feeds. | `124` | [Browse](datasets/archive/api-reference.md) |
| **General** | Billing, pricing, free tier (5K credits/mo), security, compliance, and accounts. | `41` | [Browse](general/account/billing-and-pricing/billing.md) |
| **Integrations** | Documentation pages under `integrations/`. | `91` | [Browse](integrations/adspower.md) |
| **Proxy Networks** | Residential, ISP, Datacenter, and Mobile proxy configurations & routing. | `35` | [Browse](proxy-networks/browser-extension/configuration.md) |
| **Core / Root** | Introduction, product selector, release notes, and high-level platform overview. | `21` | [Browse](account-management-quickstart.md) |
| **Scraping Automation** | Web Unlocker, Scraping Browser, SERP API, and automated crawl engines. | `68` | [Browse](scraping-automation/bright-shield/asset-shield.md) |

## Key Entry Points

- [Introduction](introduction.md) - Overview of the Bright Data web data platform
- [Product Selector](product-selector.md) - Decision matrix across scrapers, APIs, and proxies
- [MCP Server Overview](ai/mcp-server/overview.md) - Model Context Protocol for AI agents
- [AI Agents Overview](ai/for-agents/overview.md) - LLM agent integrations and workflows
- [Web Scraper API](datasets/scrapers/overview.md) - 1,300+ pre-built scrapers for major web services
- [Web Unlocker API](api-reference/rest-api/unlocker/unlock-website.md) - Real-time website unblocking API
- [SERP API](api-reference/rest-api/serp/serp-api.md) - Search Engine Result Page API
- [Proxy Networks](proxy-networks/overview.md) - 400M+ residential and mobile IP infrastructure
- [CLI Installation & Reference](cli/installation.md) - Command-line interface setup
- [Authentication & API Keys](api-reference/authentication.md) - Zone and bearer token auth guide
- [Free Tier Details](general/account/billing-and-pricing/free-tier.md) - 5,000 free monthly credits

## File Organization

Each page is saved as a clean, stand-alone `.md` (Markdown) file mirroring the URL structure of `docs.brightdata.com`.

```
brightdata-docs/
├── README.md               # This master index
├── toc.md                  # Comprehensive Table of Contents
├── toc.json                # Machine-readable page catalog with metadata
├── llms.txt                # Task-oriented LLM index
├── llms-full.txt           # Consolidated 5.4MB full documentation dump
├── sitemap.xml             # Upstream sitemap
├── introduction.md         # Welcome & platform overview
├── ai/                     # AI agents, MCP server, integrations
├── api-reference/          # REST APIs & SDK documentation
├── datasets/               # Pre-built scraper library & feeds
├── scraping-automation/    # Web Unlocker, Scraping Browser, SERP API
├── proxy-networks/         # Proxy types, integration guides, architectures
├── cli/                    # Bright Data CLI documentation
└── general/                # Account, billing, security, compliance
```
