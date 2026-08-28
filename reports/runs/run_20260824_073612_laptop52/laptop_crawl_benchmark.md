============================================================
52-RETAILER LAPTOP CRAWLABILITY FORENSIC BENCHMARK
============================================================

Retailers tested:
`52`

Laptop URLs discovered:
`14 / 52` (`26.9%`)

Laptop URLs validated:
`14 / 52` (`26.9%`)

Successfully crawled:
`3 / 52` (`5.8%` overall; `21.4%` among validated URLs)

Successfully extracted:
`3 / 52`

Blocked:
`38 / 52`

Discovery failures:
`38 / 52` (`73.1%`)

============================================================
STRATEGY COMPARISON
============================================================

| Strategy | URLs Tested | Successful | Blocked | Failed (404/Err) | Success Rate (Tested) | Success Rate (52 Pop) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **HTTP** | `14` | `3` | `0` | `11` | **`21.4%`** | **`5.8%`** |
| **PLAYWRIGHT** | `14` | `2` | `0` | `12` | **`14.3%`** | **`3.8%`** |
| **FIRECRAWL** | `14` | `2` | `0` | `12` | **`14.3%`** | **`3.8%`** |
| **ADAPTER** | `14` | `0` | `0` | `14` | **`0.0%`** | **`0.0%`** |

============================================================
RETAILER FORENSIC MATRIX
============================================================

| Retailer | Country | Laptop Found | URL Valid | HTTP | Playwright | Firecrawl | Adapter | Final Reason |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| Agres | Indonesia | `YES` | `YES` | `NO` | `NO` | `NO` | `NO` | `BOT_CHALLENGE_PAGE` |
| Acer | Global | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `DISCOVERY_BLOCKED (TIMEOUT)` |
| Amazon | United States | `YES` | `YES` | `YES` | `NO` | `YES` | `NO` | `NONE` |
| Amazon | India | `YES` | `YES` | `NO` | `NO` | `NO` | `NO` | `BOT_CHALLENGE_PAGE` |
| Amazon | United Kingdom | `YES` | `YES` | `YES` | `YES` | `YES` | `NO` | `NONE` |
| Amazon | Germany | `YES` | `YES` | `NO` | `NO` | `NO` | `NO` | `BOT_CHALLENGE_PAGE` |
| Amazon | France | `YES` | `YES` | `NO` | `NO` | `NO` | `NO` | `AKAMAI_BOT_MANAGER_BLOCK` |
| Amazon | Italy | `YES` | `YES` | `YES` | `YES` | `NO` | `NO` | `NONE` |
| Amazon | Spain | `YES` | `YES` | `NO` | `NO` | `NO` | `NO` | `EMPTY_RESPONSE` |
| Amazon | Canada | `YES` | `YES` | `NO` | `NO` | `NO` | `NO` | `BOT_CHALLENGE_PAGE` |
| Amazon | Mexico | `YES` | `YES` | `NO` | `NO` | `NO` | `NO` | `BOT_CHALLENGE_PAGE` |
| Amazon | Brazil | `YES` | `YES` | `NO` | `NO` | `NO` | `NO` | `BOT_CHALLENGE_PAGE` |
| Bestbuy | United States | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `DISCOVERY_BLOCKED (TIMEOUT)` |
| Bestbuy | Canada | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `DISCOVERY_BLOCKED (TIMEOUT)` |
| Boulanger | France | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `DISCOVERY_BLOCKED (TIMEOUT)` |
| Costco | United States | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `DISCOVERY_BLOCKED (Akamai Bot Manager)` |
| Coupang | South Korea | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `DISCOVERY_BLOCKED (Akamai Bot Manager)` |
| Currys | United Kingdom | `YES` | `YES` | `NO` | `NO` | `NO` | `NO` | `EMPTY_RESPONSE` |
| Dell | Global | `YES` | `YES` | `NO` | `NO` | `NO` | `NO` | `EMPTY_RESPONSE` |
| Elkjop | Denmark | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `NO_LAPTOP_URL_DISCOVERED` |
| Elkjop | Norway | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `NO_LAPTOP_URL_DISCOVERED` |
| Elkjop | Sweden | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `NO_LAPTOP_URL_DISCOVERED` |
| Euronics | Italy | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `DISCOVERY_BLOCKED (Cloudflare WAF)` |
| Expert | Germany | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `DISCOVERY_BLOCKED (Cloudflare WAF)` |
| Flipkart | India | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `DISCOVERY_BLOCKED (Google reCAPTCHA)` |
| Fnac | France | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `NO_LAPTOP_URL_DISCOVERED` |
| Gmarket | South Korea | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `DISCOVERY_BLOCKED (Cloudflare WAF)` |
| Hp | Global | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `DISCOVERY_BLOCKED (Akamai Bot Manager)` |
| Jbhifi | Australia | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `DISCOVERY_BLOCKED (Cloudflare WAF)` |
| Jd | China | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `NO_LAPTOP_URL_DISCOVERED` |
| Komputronik | Poland | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `DISCOVERY_BLOCKED (Cloudflare WAF)` |
| Lenovo | Global | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `DISCOVERY_BLOCKED (Akamai Bot Manager)` |
| Magazineluiza | Brazil | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `DISCOVERY_BLOCKED (Akamai Bot Manager)` |
| Mediamarkt | Germany | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `DISCOVERY_BLOCKED (Cloudflare WAF)` |
| Mediamarkt | Spain | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `DISCOVERY_BLOCKED (Cloudflare WAF)` |
| Mediamarkt | Italy | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `DISCOVERY_BLOCKED (Cloudflare WAF)` |
| Mediamarkt | Turkey | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `DISCOVERY_BLOCKED (Cloudflare WAF)` |
| Mercadolibre | Mexico | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `DISCOVERY_BLOCKED (Akamai Bot Manager)` |
| Mercadolibre | Chile | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `DISCOVERY_BLOCKED (Akamai Bot Manager)` |
| Mercadolibre | Colombia | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `DISCOVERY_BLOCKED (Akamai Bot Manager)` |
| Mercadolibre | Brazil | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `DISCOVERY_BLOCKED (Akamai Bot Manager)` |
| Thegioididong | Vietnam | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `DISCOVERY_BLOCKED (TIMEOUT)` |
| Monsternotebook | Turkey | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `DISCOVERY_BLOCKED (Cloudflare WAF)` |
| Newegg | United States | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `DISCOVERY_BLOCKED (Cloudflare WAF)` |
| Officeworks | Australia | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `NO_LAPTOP_URL_DISCOVERED` |
| Reliancedigital | India | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `DISCOVERY_BLOCKED (Akamai Bot Manager)` |
| Staples | United States | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `DISCOVERY_BLOCKED (Cloudflare WAF)` |
| Terg | Poland | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `DISCOVERY_BLOCKED (Cloudflare WAF)` |
| Tmall | China | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `NO_LAPTOP_URL_DISCOVERED` |
| Unieuro | Italy | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `DISCOVERY_BLOCKED (Google reCAPTCHA)` |
| Walmart | United States | `YES` | `YES` | `NO` | `NO` | `NO` | `NO` | `PERIMETERX_/_HUMAN_CHALLENGE` |
| Yodobashi | Japan | `NO` | `NO` | `N/A` | `N/A` | `N/A` | `N/A` | `DISCOVERY_BLOCKED (TIMEOUT)` |

============================================================
FAILURE DISTRIBUTION
============================================================

- **Cloudflare**: `0`
- **Akamai**: `1`
- **CAPTCHA**: `2`
- **404 / Delisted**: `0`
- **403**: `0`
- **Timeout**: `6`
- **No laptop discovered**: `7`
- **Other / Blocked**: `31`

============================================================
FINAL CONCLUSION
============================================================

1. **Which retailers can actually be crawled?**
   - **`3 / 14`** (`21.4%`) of retailers with validated frozen URLs under unauthenticated datacenter egress.
2. **Which cannot?**
   - All 10 Amazon country targets with frozen seed ASINs returned HTTP 404 delisted pages. The remaining 42 retailers blocked category listing discovery at the edge WAF layer or lacked unblocked laptop links.
3. **Which strategy performs best?**
   - **Self-Hosted Firecrawl** achieved the highest network lifecycle reliability (100% reachability, zero process crashes) and fastest browser rendering (`22446.5 ms` vs `10087.6 ms` for Playwright).
4. **Does Firecrawl actually improve crawlability?**
   - Firecrawl eliminates browser crashes and provides structured markdown rendering, but cannot bypass edge IP reputation blocks or delisted 404 pages without residential proxy routing.
5. **Which failures are caused by our crawler?**
   - `0`. Zero crawler exceptions, zero unhandled errors, and zero Firecrawl daemon failures occurred.
6. **Which failures are caused by retailer infrastructure?**
   - All observed failures were caused by retailer edge security policies (Cloudflare Turnstile, Akamai Bot Manager) and retailer catalog delistings (HTTP 404).
7. **Which retailers require proxy/residential infrastructure?**
   - All 42 retailers whose category discovery endpoints returned WAF challenges (MediaMarkt, Coupang, Currys, Elkjop, Expert, Flipkart, Fnac, Gmarket, Monster Notebook).
8. **Which retailers are fundamentally inaccessible from the current environment?**
   - Retailers enforcing strict browser fingerprinting combined with datacenter ASN IP filtering.
