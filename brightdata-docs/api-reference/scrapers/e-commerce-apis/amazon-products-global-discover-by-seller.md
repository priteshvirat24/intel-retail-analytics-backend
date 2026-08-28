> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Discover by seller

> Use the Bright Data Web Scraper API to discover by Seller. POST /datasets/v3/scrape starts a job that returns structured product records as JSON.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_lwhideng15g8jg63s7" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_lwhideng15g8jg63s7` to collect **Discover by Seller** data.
  </Warning>
</ParamField>

<ParamField query="type" type="string" default="discover_new">
  Must be set to `discover_new`.
</ParamField>

<ParamField query="discover_by" type="string" default="seller">
  Must be set to `seller`.
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
    <ParamField body="seller_url" type="string" required>
      The URL of the Amazon seller page.
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
        "seller_url": "https://www.amazon.com/sp?ie=UTF8&seller=A2FE2Y3KEQLBV7",
        "num_of_products": 30
      }
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "title": "Wireless Charging Pad 15W Fast Charge",
      "url": "https://www.amazon.com/dp/B0C99887GH",
      "asin": "B0C99887GH",
      "price": 18.99,
      "currency": "USD",
      "rating": 4.4,
      "reviews_count": 7300,
      "seller_name": "Electronics Hub",
      "brand": "ChargeFast",
      "availability": "In Stock",
      "main_image": "https://m.media-amazon.com/images/I/example-charger.jpg",
      "description": "Slim wireless charging pad compatible with all Qi-enabled devices.",
      "category": "Electronics > Accessories > Chargers",
      "country_domain": "amazon.com"
    }
  ]
  ```
</ResponseExample>
