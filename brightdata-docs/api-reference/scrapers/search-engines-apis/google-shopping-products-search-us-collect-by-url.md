> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Shopping search (US) by URL

> Use the Bright Data Web Scraper API to collect US Google Shopping search results by URL. POST /datasets/v3/scrape returns product records as JSON.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_m31f2k0d2m1bah4f3b" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_m31f2k0d2m1bah4f3b` to collect **Google Shopping Products Search US by URL**.
  </Warning>
</ParamField>

<ParamField query="notify" type="boolean" default={false}>
  Whether to send notifications when the request is completed.
</ParamField>

<ParamField query="include_errors" type="boolean" default={true}>
  Whether to include errors in the response.
</ParamField>

## Request Body

<ParamField body="input" type="object[]" required>
  An array of input objects.

  <Expandable title="properties">
    <ParamField body="url" type="string" required>
      The Google Shopping search URL to scrape (e.g., `https://www.google.com/search?tbm=shop&q=...`).
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {"url": "https://www.google.com/search?tbm=shop&q=wireless+headphones"}
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "query": "wireless headphones",
      "position": 1,
      "title": "Sony WH-1000XM5 Wireless Headphones",
      "merchant": "Best Buy",
      "price": "349.99",
      "currency": "USD",
      "rating": 4.7,
      "reviews_count": 1820,
      "product_url": "https://www.google.com/shopping/product/54321"
    }
  ]
  ```
</ResponseExample>
