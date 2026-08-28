> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Collect Marketplace listings by URL

> Use the Bright Data Web Scraper API to collect Marketplace Listings by URL. Calls the POST /datasets/v3/scrape endpoint.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_lvt9iwuh6fbcwmx1a" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_lvt9iwuh6fbcwmx1a` to collect **Facebook Marketplace listings** data.
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
      The URL of the Facebook Marketplace listing to collect.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {"url": "https://www.facebook.com/marketplace/item/1234567890"},
      {"url": "https://www.facebook.com/marketplace/item/9876543210"}
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "url": "https://www.facebook.com/marketplace/item/1259177466401495",
      "title": "2018 Mercedes-Benz C 300 Convertible 27k miles",
      "initial_price": 35995,
      "final_price": 35995,
      "currency": "USD",
      "product_id": "1259177466401495",
      "condition": "USED",
      "description": "1 owner, 2.0 turbo all wheel drive, leather seating pkg...",
      "location": "Knoxville, TN",
      "country_code": "US",
      "images": ["https://..."],
      "seller_description": "1 owner, 2.0 turbo...",
      "color": "grey",
      "brand": null,
      "videos": null,
      "profile_id": "34591790377134943",
      "listing_date": "2026-04-02T11:25:00.000Z"
    }
  ]
  ```
</ResponseExample>
