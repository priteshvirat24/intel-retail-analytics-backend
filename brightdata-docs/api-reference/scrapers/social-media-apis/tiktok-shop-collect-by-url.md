> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Collect Shop by URL

> Use the Bright Data Web Scraper API to collect Shop by URL. POST /datasets/v3/scrape starts a scraping job that returns the data as structured JSON records.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_m45m1u911dsa4274pi" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_m45m1u911dsa4274pi` to collect **Shop by URL** data.
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
      The URL of the TikTok Shop product to collect.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {"url": "https://www.tiktok.com/view/product/1729000000000000000"}
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "url": "https://www.tiktok.com/view/product/1729000000000000000",
      "title": "Wireless Bluetooth Headphones with Noise Cancellation",
      "price": 29.99,
      "currency": "USD",
      "rating": 4.7,
      "reviews_count": 1250,
      "seller_name": "TechGadgets Official",
      "seller_url": "https://www.tiktok.com/@techgadgets",
      "description": "High-quality wireless headphones with active noise cancellation and 30-hour battery life.",
      "images": [
        "https://p16-oec-ttp.tiktokcdn-us.com/example-product-1.jpeg",
        "https://p16-oec-ttp.tiktokcdn-us.com/example-product-2.jpeg"
      ],
      "category": "Electronics > Audio > Headphones"
    }
  ]
  ```
</ResponseExample>
