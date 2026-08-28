> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get started with Google SERP API

> Start using Bright Data's Google SERP API in 3 steps: Sign in, create a SERP zone, get your API key, and begin collecting Google search data.

## Make your first request in minutes

Test the Google SERP API in minutes with this ready-to-use code example.

<CardGroup cols={3}>
  <Card title="Postman Example" icon="user-astronaut" iconType="regular" href="https://www.postman.com/bright-data-api/bright-data-api/request/kpq952m/google-search" cta="Try Google SERP API in less than 1 minute" />

  <Card title="Node.js Example" icon="code" iconType="regular" href="https://github.com/luminati-io/bright-data-serp-api-nodejs-project" cta="Try Google SERP API in less than 2 minutes" />

  <Card title="Python Example" icon="code" iconType="regular" href="https://github.com/brightdata/bright-data-serp-api-python-project" cta="Try Google SERP API in less than 5 minutes" />
</CardGroup>

## Google SERP API Quick Start Examples

Run these basic examples to check that your Google SERP API is working (remember to update in your API key and query):

<CodeGroup>
  ```shell cURL theme={null}
    curl -X POST https://api.brightdata.com/request \
    --header "Content-Type: application/json" \
    --header "Authorization: Bearer API_KEY" \
    --data '{
      "zone": "serp_api1",
      "url": "https://www.google.com/search?q=pizza",
      "format": "raw"
    }'
  ```

  ```javascript google-serp.js theme={null}
  (async () => {
    const response = await fetch('https://api.brightdata.com/request', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer API_KEY'
      },
      body: JSON.stringify({
        zone: 'serp_api1',
        url: 'https://www.google.com/search?q=pizza',
        format: 'raw'
      })
    });
    
    const data = await response.text();
    console.log(data);
  })();
  ```

  ```python google_serp.py theme={null}
  import requests

  # API Configuration
  headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer API_KEY',
  }

  payload = {
      'zone': 'serp_api1',
      'url': 'https://www.google.com/search?q=pizza',
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

## Links to get started with Google SERP API

* [SERP API introduction](/scraping-automation/serp-api/introduction)
* [Get API key](/api-reference/authentication)
* [Google query parameters](/scraping-automation/serp-api/query-parameters/google)
