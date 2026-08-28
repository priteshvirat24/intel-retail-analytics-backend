> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Discover Google Maps Places by place_id

> Use the Bright Data Web Scraper API to discover Google Maps places by place_id. POST /datasets/v3/scrape returns structured place records as JSON.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_m8ebnr0q2qlklc02fz" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_m8ebnr0q2qlklc02fz` to discover **Google Maps places by place\_id**.
  </Warning>
</ParamField>

<ParamField query="type" type="string" default="discover_new" required>
  Must be set to `discover_new`.
</ParamField>

<ParamField query="discover_by" type="string" default="place_id" required>
  Must be set to `place_id`.
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
    <ParamField body="place_id" type="string" required>
      The Google Maps place ID for the location.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {"place_id": "ChIJS5WVcqWh9YgRHU08rJqLNsQ"}
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "place_id": "ChIJS5WVcqWh9YgRHU08rJqLNsQ",
      "name": "Example Place",
      "address": "123 Example St., New York, NY",
      "rating": 4.5,
      "reviews_count": 1200,
      "latitude": 40.7128,
      "longitude": -74.006
    }
  ]
  ```
</ResponseExample>
