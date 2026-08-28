> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SERP API configuration

> Configure the Bright Data SERP API (31 languages): choose JSON or raw HTML format, switch sync and async modes and enrich ad data with key request parameters.

## Default response format

When you configure your SERP API you can select between different default response formats:

1. Raw HTML: no parsing at all. Get the HTML response as is.
2. Full JSON: our full interpretation of Google's SERP HTML to JSON.
3. Light JSON: a subset of full JSON
4. Parsed Bing: our full interpretation of Bing's SERP HTML to JSON.
5. Markdown: our full interpretation of Google's and Bing's SERP HTML to markdown `*.md` file.
6. Screenshot: an image capture of the SERP HTML page as interpreted by a browser.

To read more on our response options and advanced response formats see: [Parsed JSON results](/scraping-automation/serp-api/parsed-json-results/parsing-search-results)

## Google Ads

Bright Data provides a special setting which brings more Google ads data. In your SERP API zone's Configuration tab, the **Google Ads** section offers two options:

1. **Standard** (default): fetches both organic search results and ads, encompassing a broad geographical scope.
2. **Maximized**: fetches an even greater variety of ads search results and ads, mimicking an incognito browsing scenario without cookies.

## How to configure advanced settings

### Custom Headers and Cookies

Bright Data enables you to send your custom headers and cookies. Once you do so, we will not override your settings and will relay your requests to the search engine. You can choose from a pre-approved list of headers and cookies or request a new one and go through an approval process.

Once custom headers and cookies are selected, Bright Data will charge you for **all** requests. When using the default setting without customized cookies, Bright Data charges for successful requests only.

### How to send asynchronous requests

You can work with Bright Data APIs using an asynchronous mode, where the request is sent immediately, and you will be notified when the response is ready. It usually takes a few minutes for the response to be posted back. For non real-time applications we recommend Async mode to assure a higher success rate.

When submitting an asynchronous request, Bright Data handles it in the background. You can either poll for the response or configure a webhook where we will notify you on request completion. This allows you to collect responses at a later, more convenient time via a designated endpoint, increasing stability and efficiency. [Learn more](/scraping-automation/serp-api/asynchronous-requests)

#### Webhook Configuration

Webhook has two configurable options:

1. Webhook address URL
2. Webhook method (GET/POST)

On your network you should add our webhook agent origin IPs.

<Tip>
  ### Allowlist our webhook IPs

  Our asynchronous webhook delivery sends notifications from a pair of stable IP addresses:

  1. `100.27.150.189`
  2. `18.214.10.85`

  Customers may need to allowlist these IPs on their side.
</Tip>
