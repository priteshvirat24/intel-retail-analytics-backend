> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Collect Google AI Mode Search by URL

> Use the Bright Data Web Scraper API to collect Google AI Mode search answers and citations by URL. POST /datasets/v3/scrape returns records as JSON.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_mcswdt6z2elth3zqr2" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_mcswdt6z2elth3zqr2` to collect **Google AI Mode Search by URL**.
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
      The Google AI Mode Search URL to scrape (includes the `udm=50` parameter).
    </ParamField>

    <ParamField body="prompt" type="string" required>
      The prompt used in the AI Mode Search query.
    </ParamField>

    <ParamField body="country" type="string">
      ISO 3166-1 alpha-2 country code for localized results.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {
        "url": "https://www.google.com/search?udm=50&q=how+to+train+for+a+marathon",
        "prompt": "how to train for a marathon",
        "country": "US"
      }
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "prompt": "how to train for a marathon",
      "answer": "A typical marathon training plan runs 16 to 20 weeks...",
      "citations": [
        {
          "title": "Marathon Training Plan for Beginners",
          "url": "https://example.com/marathon-plan"
        }
      ],
      "url": "https://www.google.com/search?udm=50&q=how+to+train+for+a+marathon"
    }
  ]
  ```
</ResponseExample>
