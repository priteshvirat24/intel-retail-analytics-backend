> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Collect products search by URL

> Use the Bright Data Web Scraper API to collect Products Search by URL. POST /datasets/v3/scrape starts a job that returns structured product records as JSON.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_lwdb4vjm1ehb499uxs" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_lwdb4vjm1ehb499uxs` to collect **Products Search by URL** data.
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
        "keyword": "X-box",
        "url": "https://www.amazon.com",
        "pages_to_search": 2
      }
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "title": "Wireless Gaming Controller for Console",
      "url": "https://www.amazon.com/dp/B0D22334IJ",
      "asin": "B0D22334IJ",
      "price": 59.99,
      "currency": "USD",
      "rating": 4.6,
      "reviews_count": 28400,
      "seller_name": "GameTech Store",
      "brand": "GameTech",
      "availability": "In Stock",
      "main_image": "https://m.media-amazon.com/images/I/example-controller.jpg",
      "description": "Ergonomic wireless controller with custom button mapping and vibration feedback.",
      "category": "Video Games > Accessories > Controllers"
    }
  ]
  ```
</ResponseExample>
