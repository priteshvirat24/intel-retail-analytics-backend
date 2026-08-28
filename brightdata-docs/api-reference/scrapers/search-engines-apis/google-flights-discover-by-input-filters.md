> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Discover Google Flights by Input Filters

> Use the Bright Data Web Scraper API to discover Google Flights listings by input filters. POST /datasets/v3/scrape returns flight records as JSON.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_mhng7wen1rw0a3gvpf" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_mhng7wen1rw0a3gvpf` to discover **Google Flights by input filters**.
  </Warning>
</ParamField>

<ParamField query="type" type="string" default="discover_new" required>
  Must be set to `discover_new`.
</ParamField>

<ParamField query="discover_by" type="string" default="input_filters" required>
  Must be set to `input_filters`.
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
    <ParamField body="origin" type="string" required>
      Origin airport IATA code (e.g., `JFK`).
    </ParamField>

    <ParamField body="destination" type="string" required>
      Destination airport IATA code (e.g., `LAX`).
    </ParamField>

    <ParamField body="departure" type="string" required>
      Departure date in `YYYY-MM-DD` format.
    </ParamField>

    <ParamField body="return" type="string">
      Return date in `YYYY-MM-DD` format. Omit for one-way trips.
    </ParamField>

    <ParamField body="trip_type" type="string" required>
      One of: `one_way`, `round_trip`, `multi_city`.
    </ParamField>

    <ParamField body="adults" type="number" required>
      Number of adult passengers.
    </ParamField>

    <ParamField body="children" type="number">
      Number of child passengers.
    </ParamField>

    <ParamField body="infants_in_seat" type="number">
      Number of infants in their own seat.
    </ParamField>

    <ParamField body="infants_on_lap" type="number">
      Number of infants on lap.
    </ParamField>

    <ParamField body="cabin" type="string">
      Cabin class. One of: `economy`, `premium_economy`, `business`, `first`.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {
        "origin": "JFK",
        "destination": "LAX",
        "departure": "2026-06-15",
        "return": "2026-06-22",
        "trip_type": "round_trip",
        "adults": 1,
        "children": 0,
        "infants_in_seat": 0,
        "infants_on_lap": 0,
        "cabin": "economy"
      }
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
      "cabin": "economy",
      "flights": [
        {
          "airline": "Delta",
          "flight_number": "DL 1234",
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
