> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Collect Google Flights by URL

> Use the Bright Data Web Scraper API to collect Google Flights listings by URL. POST /datasets/v3/scrape returns structured flight records as JSON.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_mhng7wen1rw0a3gvpf" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_mhng7wen1rw0a3gvpf` to collect **Google Flights by URL**.
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
      The full Google Flights URL to scrape.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {"url": "https://www.google.com/travel/flights?tfs=..."}
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "origin": "JFK",
      "destination": "LAX",
      "departure_date": "2026-06-15",
      "return_date": "2026-06-22",
      "flights": [
        {
          "airline": "Delta",
          "flight_number": "DL 1234",
          "departure_time": "08:15",
          "arrival_time": "11:45",
          "duration_minutes": 390,
          "stops": 0,
          "price": "328.00",
          "currency": "USD"
        }
      ]
    }
  ]
  ```
</ResponseExample>
