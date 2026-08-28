> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get started with Bing SERP API

> Start using Bright Data's Bing SERP API in 3 steps: Sign in, create a SERP zone, get your API key, and begin collecting Bing search data.

## Make your first request in minutes

Test the Bing SERP API in minutes with this ready-to-use code example.

<CardGroup cols={3}>
  <Card title="Postman Example" icon="user-astronaut" iconType="regular" href="https://www.postman.com/bright-data-api/bright-data-api/request/uzaea2u/bing-search" cta="Try Bing SERP API in less than 1 minute" />

  <Card title="Node.js Example" icon="code" iconType="regular" href="https://github.com/brightdata/bright-data-bing-serp-api-nodejs-project" cta="Try Bing SERP API in less than 2 minutes" />

  <Card title="Python Example" icon="code" iconType="regular" href="https://github.com/brightdata/bright-data-bing-serp-api-python-project" cta="Try Bing SERP API in less than 5 minutes" />
</CardGroup>

## Bing SERP API Quick Start Examples

Run these basic examples to check that your Bing SERP API is working (remember to update in your API key and query):

<CodeGroup>
  ```shell cURL theme={null}
    curl -X POST https://api.brightdata.com/request \
    --header "Content-Type: application/json" \
    --header "Authorization: Bearer API_KEY" \
    --data '{
      "zone": "serp_api1",
      "url": "https://www.bing.com/search?q=pizza",
      "format": "raw"
    }'
  ```

  ```javascript bing-serp.js theme={null}
  (async () => {
    const response = await fetch('https://api.brightdata.com/request', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer API_KEY'
      },
      body: JSON.stringify({
        zone: 'serp_api1',
        url: 'https://www.bing.com/search?q=pizza',
        format: 'raw'
      })
    });
    
    const data = await response.text();
    console.log(data);
  })();
  ```

  ```python bing_serp.py theme={null}
  import requests

  # API Configuration
  headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer API_KEY',
  }

  payload = {
      'zone': 'serp_api1',
      'url': 'https://www.bing.com/search?q=pizza',
      'format': 'raw'
  }

  # Make the request
  response = requests.post(
      'https://api.brightdata.com/request', 
      json=payload, 
      headers=headers
  )

  print(response.text)
  ```
</CodeGroup>

## Links to get started with Bing SERP API

* [SERP API introduction](/scraping-automation/serp-api/introduction)
* [Get API key](/api-reference/authentication)
* [Bing query parameters](/scraping-automation/serp-api/query-parameters/bing)

## Microsoft Bing API to Bright Data SERP API migration guide

[Bing API to Bright Data SERP API migration guide](/scraping-automation/serp-api/parsed-json-results/bing-to-bright-data-serp-migration-guide)
