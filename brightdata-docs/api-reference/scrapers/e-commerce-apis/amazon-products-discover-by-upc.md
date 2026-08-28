> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Discover Amazon products by UPC

> Use the Bright Data Web Scraper API to discover by UPC. POST /datasets/v3/scrape starts a job that returns structured product records as JSON.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_l7q7dkf244hwjntr0" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_l7q7dkf244hwjntr0` to collect **Discover by UPC** data.
  </Warning>
</ParamField>

<ParamField query="type" type="string" default="discover_new">
  Must be set to `discover_new`.
</ParamField>

<ParamField query="discover_by" type="string" default="upc">
  Must be set to `upc`.
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
    <ParamField body="upc" type="string" required>
      The UPC code of the product to look up.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {"upc": "012345678901"},
      {"upc": "098765432109"}
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "title": "Stainless Steel Water Bottle 32oz",
      "url": "https://www.amazon.com/dp/B0D11223AB",
      "asin": "B0D11223AB",
      "price": 19.99,
      "currency": "USD",
      "rating": 4.8,
      "reviews_count": 42300,
      "seller_name": "HydroGear",
      "brand": "HydroGear",
      "availability": "In Stock",
      "main_image": "https://m.media-amazon.com/images/I/example-bottle.jpg",
      "description": "Double-wall vacuum insulated water bottle that keeps drinks cold for 24 hours.",
      "category": "Sports & Outdoors > Water Bottles"
    }
  ]
  ```
</ResponseExample>
