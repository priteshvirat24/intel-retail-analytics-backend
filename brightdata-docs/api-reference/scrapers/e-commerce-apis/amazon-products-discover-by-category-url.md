> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Discover Amazon products by category URL

> Use the Bright Data Web Scraper API to discover Amazon products by category URL. Calls the POST /datasets/v3/scrape endpoint.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_l7q7dkf244hwjntr0" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_l7q7dkf244hwjntr0` to collect **Discover by Category URL** data.
  </Warning>
</ParamField>

<ParamField query="type" type="string" default="discover_new">
  Must be set to `discover_new`.
</ParamField>

<ParamField query="discover_by" type="string" default="category_url">
  Must be set to `category_url`.
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
      The URL of the Amazon category page.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {"url": "https://www.amazon.com/s?bbn=172282&rh=n%3A172282"}
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "title": "USB-C Fast Charging Cable 6ft",
      "url": "https://www.amazon.com/dp/B0B12345AB",
      "asin": "B0B12345AB",
      "price": 12.99,
      "currency": "USD",
      "rating": 4.5,
      "reviews_count": 34500,
      "seller_name": "CablePro",
      "brand": "CablePro",
      "availability": "In Stock",
      "main_image": "https://m.media-amazon.com/images/I/example-category.jpg",
      "description": "Durable braided USB-C cable with fast charging support up to 100W.",
      "category": "Electronics > Accessories > Cables"
    }
  ]
  ```
</ResponseExample>
