> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Discover by brand

> Use the Bright Data Web Scraper API to discover by Brand. POST /datasets/v3/scrape starts a job that returns structured product records as JSON.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_lwhideng15g8jg63s7" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_lwhideng15g8jg63s7` to collect **Discover by Brand** data.
  </Warning>
</ParamField>

<ParamField query="type" type="string" default="discover_new">
  Must be set to `discover_new`.
</ParamField>

<ParamField query="discover_by" type="string" default="brand">
  Must be set to `brand`.
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
    <ParamField body="brand_url" type="string" required>
      The URL of the Amazon brand page.
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
        "brand_url": "https://www.amazon.com/stores/BrandName/page/12345678-ABCD-1234-EFGH-123456789012",
        "num_of_products": 20
      }
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "title": "Smart Fitness Tracker with Heart Rate Monitor",
      "url": "https://www.amazon.com/dp/B0D55667AB",
      "asin": "B0D55667AB",
      "price": 49.99,
      "currency": "USD",
      "rating": 4.3,
      "reviews_count": 9800,
      "seller_name": "FitTech Official",
      "brand": "FitTech",
      "availability": "In Stock",
      "main_image": "https://m.media-amazon.com/images/I/example-brand.jpg",
      "description": "Slim fitness tracker with continuous heart rate monitoring and sleep tracking.",
      "category": "Electronics > Wearables > Fitness Trackers",
      "country_domain": "amazon.com"
    }
  ]
  ```
</ResponseExample>
