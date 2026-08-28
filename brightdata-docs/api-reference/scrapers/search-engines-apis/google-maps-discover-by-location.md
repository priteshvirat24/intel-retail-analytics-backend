> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Discover Google Maps Places by Location

> Use the Bright Data Web Scraper API to discover Google Maps places by geographic location. POST /datasets/v3/scrape returns place records as JSON.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_m8ebnr0q2qlklc02fz" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_m8ebnr0q2qlklc02fz` to discover **Google Maps places by location**.
  </Warning>
</ParamField>

<ParamField query="type" type="string" default="discover_new" required>
  Must be set to `discover_new`.
</ParamField>

<ParamField query="discover_by" type="string" default="location" required>
  Must be set to `location`.
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
    <ParamField body="country" type="string" required>
      ISO 3166-1 alpha-2 country code (e.g., `US`, `GB`, `DE`).
    </ParamField>

    <ParamField body="lat" type="number" required>
      Latitude of the search center.
    </ParamField>

    <ParamField body="long" type="number" required>
      Longitude of the search center.
    </ParamField>

    <ParamField body="zoom_level" type="number" required>
      Google Maps zoom level (typically 10 to 18).
    </ParamField>

    <ParamField body="keyword" type="string" required>
      Search term to find nearby places (e.g., `coffee shop`, `pharmacy`).
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {"country": "US", "lat": 40.7484, "long": -73.9857, "zoom_level": 14, "keyword": "coffee shop"}
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "place_id": "ChIJExample123",
      "name": "Blue Bottle Coffee",
      "address": "54 W 40th St., New York, NY 10018",
      "rating": 4.4,
      "reviews_count": 520,
      "category": "Coffee shop",
      "latitude": 40.7525,
      "longitude": -73.984
    }
  ]
  ```
</ResponseExample>
