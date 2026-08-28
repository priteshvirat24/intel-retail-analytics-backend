> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Discover TikTok Shop products by keyword

> Use the Bright Data Web Scraper API to discover TikTok Shop products by keyword. Calls the POST /datasets/v3/scrape endpoint.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_m45m1u911dsa4274pi" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_m45m1u911dsa4274pi` to collect **Discover by Keyword** data.
  </Warning>
</ParamField>

<ParamField query="type" type="string" default="discover_new">
  Must be set to `discover_new`.
</ParamField>

<ParamField query="discover_by" type="string" default="keyword">
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
      The keyword to search for TikTok Shop products.
    </ParamField>

    <ParamField body="num_of_products" type="number">
      The number of products to collect. Missing value indicates no limit.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {
        "keyword": "wireless earbuds",
        "num_of_products": 15
      }
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "url": "https://www.tiktok.com/view/product/1731000000000000000",
      "title": "Wireless Earbuds with Charging Case",
      "price": 24.99,
      "currency": "USD",
      "rating": 4.3,
      "reviews_count": 2100,
      "seller_name": "EarTech Store",
      "seller_url": "https://www.tiktok.com/@eartechstore",
      "description": "True wireless earbuds with touch controls and 24-hour total battery life.",
      "images": [
        "https://p16-oec-ttp.tiktokcdn-us.com/example-product-1.jpeg"
      ],
      "category": "Electronics > Audio > Earbuds"
    }
  ]
  ```
</ResponseExample>
