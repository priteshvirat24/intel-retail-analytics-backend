> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Discover Google Shopping by keyword

> Use the Bright Data Web Scraper API to discover Google Shopping products by keyword. POST /datasets/v3/scrape returns product records as JSON.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_ltppk50q18kdw67omz" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_ltppk50q18kdw67omz` to discover **Google Shopping products by keyword**.
  </Warning>
</ParamField>

<ParamField query="type" type="string" default="discover_new" required>
  Must be set to `discover_new`.
</ParamField>

<ParamField query="discover_by" type="string" default="keyword" required>
  Must be set to `keyword`.
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
    <ParamField body="keyword" type="string" required>
      The search term to find matching Google Shopping products.
    </ParamField>

    <ParamField body="country" type="string">
      ISO 3166-1 alpha-2 country code for localized results.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {"keyword": "wireless headphones", "country": "US"}
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "product_id": "54321",
      "title": "Sony WH-1000XM5 Wireless Headphones",
      "brand": "Sony",
      "rating": 4.7,
      "reviews_count": 8400,
      "price": "349.99",
      "currency": "USD",
      "url": "https://www.google.com/shopping/product/54321"
    }
  ]
  ```
</ResponseExample>
