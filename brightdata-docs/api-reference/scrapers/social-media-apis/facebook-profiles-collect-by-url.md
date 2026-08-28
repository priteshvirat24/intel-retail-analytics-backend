> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Collect Facebook profiles by URL

> Use the Bright Data Web Scraper API to collect Facebook profiles by URL. Calls the POST /datasets/v3/scrape endpoint and returns a snapshot ID.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_mf0urb782734ik94dz" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_mf0urb782734ik94dz` to collect **Facebook profiles** data.
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
      The URL of the Facebook profile to collect.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {"url": "https://www.facebook.com/zuck"},
      {"url": "https://www.facebook.com/sheryl"}
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "url": "https://www.facebook.com/GoramHomes/mentions/",
      "name": "Goram Homes",
      "id": "100090557460648",
      "profile_photo": "https://...",
      "cover_photo": "https://...",
      "work": null,
      "college": null,
      "high_school": null,
      "photos": null
    }
  ]
  ```
</ResponseExample>
