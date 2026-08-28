> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Collect Google Maps Reviews by URL

> Use the Bright Data Web Scraper API to collect Google Maps reviews by URL. POST /datasets/v3/scrape returns structured review records as JSON.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_luzfs1dn2oa0teb81" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_luzfs1dn2oa0teb81` to collect **Google Maps reviews by URL**.
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
      The full URL of the Google Maps place whose reviews you want to scrape.
    </ParamField>

    <ParamField body="days_limit" type="number">
      Only return reviews posted within the last N days. Omit to retrieve all reviews.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {"url": "https://www.google.com/maps/place/Empire+State+Building", "days_limit": 30}
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "place_id": "ChIJaXQRs6lZwokRY6EFpJnhNNE",
      "place_name": "Empire State Building",
      "review_id": "ChZDSUhNMG9nS0VJQ0FnSURleDdtVURBEAE",
      "reviewer_name": "Jane Doe",
      "reviewer_url": "https://www.google.com/maps/contrib/123456789",
      "rating": 5,
      "review_text": "Great view of the city.",
      "review_date": "2026-03-28T14:12:00Z",
      "likes": 12,
      "photos": []
    }
  ]
  ```
</ResponseExample>
