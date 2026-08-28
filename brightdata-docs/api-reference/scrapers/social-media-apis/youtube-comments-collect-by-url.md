> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Collect YouTube comments by URL

> Use the Bright Data Web Scraper API to collect YouTube comments by URL. Calls the POST /datasets/v3/scrape endpoint and returns a snapshot ID.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_lk9q0ew71spt1mxywf" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_lk9q0ew71spt1mxywf` to collect **YouTube comments** data.
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
      The YouTube video URL to collect comments from.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"},
      {"url": "https://www.youtube.com/watch?v=4L_m0m3bEtE"}
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "comment_id": "UgxtjoPOlwN1r91t6OF4AaABAg",
      "comment_text": "Great video!",
      "likes": 2,
      "replies": 0,
      "username": "@username",
      "user_channel": "https://www.youtube.com/@username",
      "date": "1 year ago",
      "url": "https://www.youtube.com/watch?v=abc123",
      "video_id": "abc123",
      "user_id": "UCRmKhm9d3FuhiU6SqW4mbDA"
    }
  ]
  ```
</ResponseExample>
