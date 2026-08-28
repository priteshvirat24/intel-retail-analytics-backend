> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Discover Google Hotels by Search

> Use the Bright Data Web Scraper API to discover Google Hotels listings by search parameters. POST /datasets/v3/scrape returns hotel records as JSON.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_mg3gjfmg12tc2n5d4d" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_mg3gjfmg12tc2n5d4d` to discover **Google Hotels by search**.
  </Warning>
</ParamField>

<ParamField query="type" type="string" default="discover_new" required>
  Must be set to `discover_new`.
</ParamField>

<ParamField query="discover_by" type="string" default="search" required>
  Must be set to `search`.
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
    <ParamField body="search_term" type="string" required>
      The destination or location to search (e.g., `New York`, `Tokyo`).
    </ParamField>

    <ParamField body="check_in_date" type="string" required>
      Check-in date in `YYYY-MM-DD` format.
    </ParamField>

    <ParamField body="check_out_date" type="string" required>
      Check-out date in `YYYY-MM-DD` format.
    </ParamField>

    <ParamField body="guest_number" type="number" required>
      Number of guests.
    </ParamField>

    <ParamField body="country" type="string">
      ISO 3166-1 alpha-2 country code for localized results.
    </ParamField>

    <ParamField body="currency" type="string">
      ISO 4217 currency code (e.g., `USD`, `EUR`).
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {
        "search_term": "New York",
        "check_in_date": "2026-06-15",
        "check_out_date": "2026-06-18",
        "guest_number": 2,
        "country": "US",
        "currency": "USD"
      }
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
      "total_price": "2385.00",
      "currency": "USD",
      "check_in_date": "2026-06-15",
      "check_out_date": "2026-06-18"
    }
  ]
  ```
</ResponseExample>
