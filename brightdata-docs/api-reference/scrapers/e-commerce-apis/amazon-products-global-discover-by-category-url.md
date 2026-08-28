> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Discover Amazon global by category URL

> Use the Bright Data Web Scraper API to discover Amazon global by category URL. Calls the POST /datasets/v3/scrape endpoint.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_lwhideng15g8jg63s7" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_lwhideng15g8jg63s7` to collect **Discover by Category URL** data.
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
    <ParamField body="category_url" type="string" required>
      The URL of the Amazon category page.
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
        "category_url": "https://www.amazon.de/-/en/b?node=340843031",
        "num_of_products": 25
      }
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "title": "Mechanical Gaming Keyboard RGB Backlit",
      "url": "https://www.amazon.de/dp/B0C44556CD",
      "asin": "B0C44556CD",
      "price": 79.99,
      "currency": "EUR",
      "rating": 4.6,
      "reviews_count": 5600,
      "seller_name": "GamerGear EU",
      "brand": "KeyMaster",
      "availability": "In Stock",
      "main_image": "https://m.media-amazon.com/images/I/example-keyboard.jpg",
      "description": "Full-size mechanical keyboard with customizable RGB and hot-swappable switches.",
      "category": "Computers & Accessories > Keyboards",
      "country_domain": "amazon.de"
    }
  ]
  ```
</ResponseExample>
