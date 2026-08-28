> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Discover Amazon products by keyword

> Use the Bright Data Web Scraper API to discover Amazon products by keyword. Calls the POST /datasets/v3/scrape endpoint.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_l7q7dkf244hwjntr0" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_l7q7dkf244hwjntr0` to collect **Discover by Keyword** data.
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
      The keyword to search for Amazon products.
    </ParamField>

    <ParamField body="zipcode" type="string">
      The ZIP code to use for location-based results.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {
        "keyword": "wireless mouse",
        "zipcode": "10001"
      }
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "title": "Ergonomic Wireless Mouse with USB Receiver",
      "url": "https://www.amazon.com/dp/B0C98765XY",
      "asin": "B0C98765XY",
      "price": 24.99,
      "currency": "USD",
      "rating": 4.4,
      "reviews_count": 18700,
      "seller_name": "PeripheralsDirect",
      "brand": "ErgoClick",
      "availability": "In Stock",
      "main_image": "https://m.media-amazon.com/images/I/example-mouse.jpg",
      "description": "Lightweight ergonomic wireless mouse with adjustable DPI and silent clicks.",
      "category": "Electronics > Computers > Mice"
    }
  ]
  ```
</ResponseExample>
