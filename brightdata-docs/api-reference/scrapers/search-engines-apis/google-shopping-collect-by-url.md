> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Collect Google Shopping Products by URL

> Use the Bright Data Web Scraper API to collect Google Shopping products by URL. POST /datasets/v3/scrape returns structured product records as JSON.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_ltppk50q18kdw67omz" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_ltppk50q18kdw67omz` to collect **Google Shopping products by URL**.
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
      The full URL of the Google Shopping product page.
    </ParamField>

    <ParamField body="country" type="string">
      ISO 3166-1 alpha-2 country code for localized pricing and availability.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {"url": "https://www.google.com/shopping/product/12345", "country": "US"}
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "product_id": "12345",
      "title": "Wireless Noise-Cancelling Headphones",
      "brand": "Acme",
      "rating": 4.5,
      "reviews_count": 1240,
      "price": "249.99",
      "currency": "USD",
      "sellers": [],
      "specifications": {},
      "url": "https://www.google.com/shopping/product/12345"
    }
  ]
  ```
</ResponseExample>
