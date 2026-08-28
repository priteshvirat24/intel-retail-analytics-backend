> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Collect company reviews by URL

> Use the Bright Data Web Scraper API to collect Company Reviews by URL. Calls the POST /datasets/v3/scrape endpoint and returns a snapshot ID.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_m0dtqpiu1mbcyc2g86" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_m0dtqpiu1mbcyc2g86` to collect **Facebook company reviews** data.
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
      The URL of the Facebook page reviews to collect.
    </ParamField>

    <ParamField body="num_of_reviews" type="number">
      The number of reviews to collect. Missing value indicates no limit.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {"url": "https://www.facebook.com/PepsiCo/reviews/", "num_of_reviews": 50},
      {"url": "https://www.facebook.com/CocaCola/reviews/"}
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "url": "https://www.facebook.com/PepsiCo/reviews/",
      "review_id": "pfbid02abc123def456",
      "reviewer_name": "John Smith",
      "reviewer_url": "https://www.facebook.com/john.smith.123",
      "rating": 5,
      "review_text": "Great company with excellent products and customer service.",
      "date_posted": "2026-03-15T14:30:00.000Z",
      "num_likes": 3,
      "company_name": "PepsiCo",
      "company_url": "https://www.facebook.com/PepsiCo",
      "company_rating": 4.2,
      "total_reviews": 1250
    }
  ]
  ```
</ResponseExample>
