> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Collect Google Hotels by URL

> Use the Bright Data Web Scraper API to collect Google Hotels listings by URL. POST /datasets/v3/scrape returns structured hotel records as JSON.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_mg3gjfmg12tc2n5d4d" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_mg3gjfmg12tc2n5d4d` to collect **Google Hotels by URL**.
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
      The full Google Hotels listing URL to scrape.
    </ParamField>

    <ParamField body="country" type="string">
      ISO 3166-1 alpha-2 country code for localized pricing.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {"url": "https://www.google.com/travel/hotels/entity/...", "country": "US"}
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "hotel_id": "CgoI_example",
      "name": "The Plaza",
      "address": "768 5th Ave, New York, NY 10019",
      "rating": 4.5,
      "reviews_count": 8200,
      "price_per_night": "795.00",
      "currency": "USD",
      "amenities": ["Pool", "Spa", "Free Wi-Fi"],
      "latitude": 40.7644,
      "longitude": -73.9745
    }
  ]
  ```
</ResponseExample>
