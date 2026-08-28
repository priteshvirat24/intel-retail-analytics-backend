> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Collect products global by URL

> Use the Bright Data Web Scraper API to collect Products Global by URL. POST /datasets/v3/scrape starts a job that returns structured product records as JSON.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_lwhideng15g8jg63s7" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_lwhideng15g8jg63s7` to collect **Products Global by URL** data.
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
      The URL of the Amazon product from any country domain.
    </ParamField>

    <ParamField body="bought_past_month" type="number">
      Filter by the number of units bought in the past month.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {"url": "https://www.amazon.de/-/en/dp/B078TNNZK3"},
      {"url": "https://www.amazon.co.jp/dp/B0CWV9YTLV"}
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "title": "Bluetooth Portable Speaker Waterproof",
      "url": "https://www.amazon.de/-/en/dp/B078TNNZK3",
      "asin": "B078TNNZK3",
      "price": 59.99,
      "currency": "EUR",
      "rating": 4.5,
      "reviews_count": 23400,
      "seller_name": "AudioWorld DE",
      "brand": "SoundMax",
      "availability": "In Stock",
      "main_image": "https://m.media-amazon.com/images/I/example-global.jpg",
      "description": "Waterproof portable speaker with 360-degree sound and 12-hour battery.",
      "category": "Electronics > Audio > Speakers",
      "country_domain": "amazon.de"
    }
  ]
  ```
</ResponseExample>
