> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to select the best product

> Describe your goal and get the right Bright Data product: Web Scraper API, Scraper Studio, Web Unlocker API, SERP API, Browser API or proxies.

This guide helps you pick the right Bright Data product for your goal. For most data collection tasks, start with the Web Scraper API's 1300+ pre-built scrapers and use Scraper Studio when no pre-built scraper covers your target site.

## Use cases

* Structured data from a popular site: getting profiles, posts, products or reviews from sites like LinkedIn, Amazon, Instagram or TikTok. The correct product is the Web Scraper API.
* Structured data from any other site: collecting structured data from a site that has no pre-built scraper. The correct product is Scraper Studio.
* Search engine data: getting results from search engines like Google, Bing, Yandex. Results from the search engine can be ads, hotels, trends, flights or search results. The correct product is SERP API.
* Social account management: managing multiple profiles on social networks like Facebook, TikTok, Instagram. The correct product is ISP proxies with a static IP address.

## Which product to choose

The following is a list of products with a description of when it makes sense to use them.

### When to use the Web Scraper API

The Web Scraper API is the default choice for structured data collection. It is most suitable when:

* the target is a popular site covered by one of the 1300+ pre-built scrapers, including LinkedIn, Amazon, Instagram, TikTok, Facebook, X (Twitter), YouTube, Reddit, Google and ChatGPT
* structured JSON output is needed rather than raw HTML
* Bright Data should handle proxies, unblocking and scraper maintenance

Browse the [Scrapers Library](/datasets/scrapers/scrapers-library/overview) to check whether a pre-built scraper exists for your target site.

### When to use Scraper Studio

Scraper Studio is the choice when the target site has no pre-built scraper. It is most suitable when:

* you want to build a custom scraper from a natural-language prompt with the [AI Agent](/datasets/scraper-studio/ai-agent), or write one in the JavaScript IDE
* the scraper should keep working when the target site changes, using the [Self-Healing tool](/datasets/scraper-studio/self-healing-tool)
* you want Bright Data to host and run the scraper, with no infrastructure to maintain

### When to use the SERP API

The SERP API is most suitable when you need structured results from search engines like Google, Bing, Yandex or DuckDuckGo, including ads, hotels, trends, flights and organic listings.

### When to use the Web Unlocker API

The Web Unlocker API is most suitable when:

* you need to simply GET HTML pages, without doing any interactions on the page. Just download HTML content for given URLs.
* the page has CAPTCHA and CAPTCHA needs to be solved in order to enter the website
* custom cookies or fingerprints are needed in order to unblock the page

If you have these needs, the Web Unlocker API is usually the best fit.

### When to use the Browser API

The Browser API is most suitable when:

* you are using tools like Puppeteer, Playwright or Selenium. In that case, you can easily adjust existing code to use the Browser API.
* you need to take actions on the page, like clicking buttons, filling forms
* you want to take a screenshot of the website

If you have these needs, the Browser API is usually the best fit.

### When to use Residential proxies

Residential proxies route traffic through 400M+ real residential IPs across 195+ countries. They are most suitable for accessing sophisticated, highly protected sites that block datacenter and automated traffic, and for geo-targeted access as a real local user.

### When to use ISP proxies

ISP proxies combine residential trust with datacenter speed, using static residential-grade IPs. They are most suitable for managing social or e-commerce accounts, ad verification, QA and bypassing datacenter blocks.

### When to use Datacenter proxies

Datacenter proxies offer 1.6M+ IPs from 98+ countries and are the fastest and most cost-effective option. They are most suitable for high-volume collection from sites with light bot protection.

## Which domains need a dataset

* shopee.my, shopee.ph: these domains are available as a dataset. It is not possible to scrape these sites using proxies or the Web Unlocker API. The dataset is updated regularly on an ongoing basis. Browse the [Dataset Marketplace](/datasets/marketplace/overview).
