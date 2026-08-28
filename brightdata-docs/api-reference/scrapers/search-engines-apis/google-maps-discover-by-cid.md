> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Discover Google Maps Places by CID

> Use the Bright Data Web Scraper API to discover Google Maps places by CID. POST /datasets/v3/scrape returns structured place records as JSON.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_m8ebnr0q2qlklc02fz" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_m8ebnr0q2qlklc02fz` to discover **Google Maps places by CID**.
  </Warning>
</ParamField>

<ParamField query="type" type="string" default="discover_new" required>
  Must be set to `discover_new`.
</ParamField>

<ParamField query="discover_by" type="string" default="cid" required>
  Must be set to `cid`.
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
    <ParamField body="CID" type="string" required>
      The Google Maps Customer ID (CID) for the place.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {"CID": "14408248692727049506"}
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "place_id": "ChIJaXQRs6lZwokRY6EFpJnhNNE",
      "name": "Empire State Building",
      "address": "20 W 34th St., New York, NY 10001",
      "rating": 4.7,
      "reviews_count": 98500,
      "latitude": 40.7484405,
      "longitude": -73.9856644,
      "url": "https://www.google.com/maps/place/?q=place_id:ChIJaXQRs6lZwokRY6EFpJnhNNE"
    }
  ]
  ```
</ResponseExample>
