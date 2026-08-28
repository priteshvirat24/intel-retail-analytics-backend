> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Discover by keywords

> Use the Bright Data Web Scraper API to discover by Keywords. POST /datasets/v3/scrape starts a job that returns structured product records as JSON.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_lwhideng15g8jg63s7" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_lwhideng15g8jg63s7` to collect **Discover by Keywords** data.
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
      The keyword to search for products.
    </ParamField>

    <ParamField body="url" type="string" required>
      The Amazon domain to search on (e.g. [https://www.amazon.com](https://www.amazon.com)).
    </ParamField>

    <ParamField body="pages_to_search" type="number">
      The number of search result pages to collect.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {
        "keyword": "laptop stand",
        "url": "https://www.amazon.com",
        "pages_to_search": 3
      }
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "title": "Adjustable Laptop Stand for Desk",
      "url": "https://www.amazon.com/dp/B0B77889EF",
      "asin": "B0B77889EF",
      "price": 34.99,
      "currency": "USD",
      "rating": 4.7,
      "reviews_count": 15200,
      "seller_name": "DeskPro Accessories",
      "brand": "DeskPro",
      "availability": "In Stock",
      "main_image": "https://m.media-amazon.com/images/I/example-stand.jpg",
      "description": "Ergonomic aluminum laptop stand with adjustable height and angle.",
      "category": "Office Products > Desk Accessories > Laptop Stands",
      "country_domain": "amazon.com"
    }
  ]
  ```
</ResponseExample>
