> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Scrapers - quick start

> Get started with the Bright Data Scrapers Library (1000+ pre-built scrapers): pick a target site, trigger a collection, and retrieve results in 3 steps.

<Steps>
  <Step title="Prerequisites" stepNumber="0">
    * A Bright Data account (Sign Up → 2 min)
    * An active API Key ([How to get an API Key](/api-reference/authentication))
  </Step>

  <Step title="Pick the target site" stepNumber="1">
    1. Go to the [Scraper Library](https://brightdata.com/cp/scrapers/browse)
    2. Browse the list and click the site you need.
    3. Can’t find it? Check out the [Managed Services](/datasets/scrapers/managed-services) or [Scraper Studio IDE](/datasets/scraper-studio/introduction) products for a solution tailored to your needs!
  </Step>

  <Step title="Choose the scraper endpoint" stepNumber="2">
    Inside a site you’ll see multiple Scraper Endpoints, for example:

    * LinkedIn
      * Profile by URL – supply profile URLs, get public data fields.
      * Profiles by Keyword – supply a search term, get matching profile URLs (+ optional full data).
      * Company Jobs – collect job postings from a company page.
    * Amazon
      * Product by ASIN, Search Results, Reviews, “Frequently Bought Together”, etc.

    Pick the endpoint that returns the information you need, then click it to open the scraper's Configuration tab.

    <Frame>
      <img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/datasets/scrapers/scraping-library/quickstart/collect-by-url.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=2d4cd92cc6ade8b76a6265f20990dc37" alt="collect-by-url" width="1507" height="1229" data-path="images/datasets/scrapers/scraping-library/quickstart/collect-by-url.png" />
    </Frame>
  </Step>

  <Step title="Build the request" stepNumber="3">
    The central panel now shows a form. Work through top-to-bottom:

    **A. Inputs**

    * "Single Input”: paste a URL/keyword right in the textbox.
    * “Bulk CSV”: upload a CSV according to the input parameters of the scraper

    **B. Scraper Settings (optional)**

    1. Output Schema – tick only the data fields you require (saves bandwidth & storage).
    2. External Storage – plug credentials for S3 / GCS / Azure / etc. Result files land there automatically.
    3. Webhook URL – we POST the job’s JSON to your endpoint once finished, great for real-time pipelines.
  </Step>

  <Step title="Pick run mode: /scrape vs /trigger" stepNumber="4">
    The Code Snippet panel (right side) updates live according to your configuration setup. To run the request you can choose between two endpoints:

    | Mode  | UI Label                | API endpoint                                                      | Behaviour                                                                                                                                      | Good For                                        |
    | :---- | :---------------------- | :---------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------- |
    | Sync  | Synchronous (Real-time) | [/scrape](/api-reference/scrapers/synchronous-requests)           | Return the data as a response to the API call in real time. This endpoint has a 1-minute timeout, If it runs longer it auto-switches to async. | Quick and light jobs with results in real time. |
    | Async | Asynchronous            | [/trigger](/api-reference/rest-api/scraper/asynchronous-requests) | Returns snapshot\_id instantly;   you poll `/snapshots/{id}` or wait for the results in your `logs/webhook/storage`.                           | Production & large jobs                         |
  </Step>

  <Step title="Copy the Code" stepNumber="5">
    * Language selector – choose your preferred programming language using the code block dropdown.
    * Snippet already contains: endpoint URL, your API key header, payload JSON (inputs + options).
    * Paste it into a terminal / IDE / serverless function.
  </Step>

  <Step title="Monitor & Retrieve Results" stepNumber="6">
    1. Scraper page → Logs tab

    <Frame>
      <img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/datasets/scrapers/scraping-library/quickstart/logs-tab.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=3f687a1bcb539d254bdc0339aaab581c" alt="logs-tab" width="624" height="191" data-path="images/datasets/scrapers/scraping-library/quickstart/logs-tab.png" />
    </Frame>

    * Real-time state (running, ready, failed).
    * Download JSON/CSV/etc with one click.

    2. Webhook (if set)
       * Your server receives `{snapshot_id, status, result_url}` payload.
    3. External Storage
       * The result file appears in the bucket path you configured.
    4. [Snapshot Management API](/api-reference/scrapers/management-apis/monitor-progress)
       * Use these endpoints to monitor the snapshot progress.
  </Step>
</Steps>

🎉 You’re now ready to scrape at scale, happy collecting!
