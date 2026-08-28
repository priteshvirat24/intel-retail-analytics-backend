> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Collect posts by profile Fast API

> Use the Bright Data Web Scraper API to collect Posts by Profile Fast API. Calls the POST /datasets/v3/scrape endpoint and returns a snapshot ID.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_m7n5v2gq296pex2f5m" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_m7n5v2gq296pex2f5m` to collect **Posts by Profile Fast API** data.
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
      The URL of the TikTok profile to collect posts from.
    </ParamField>

    <ParamField body="num_of_posts" type="number">
      The number of recent posts to collect. Missing value indicates no limit.
    </ParamField>

    <ParamField body="start_date" type="string">
      Start date filter in `MM-DD-YYYY` format (should be earlier than `end_date`).
    </ParamField>

    <ParamField body="end_date" type="string">
      End date filter in `MM-DD-YYYY` format (should be later than `start_date`).
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {
        "url": "https://www.tiktok.com/@mrbeast",
        "num_of_posts": 20,
        "start_date": "01-01-2025",
        "end_date": "03-01-2025"
      }
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "post_id": "7553300000000000000",
      "description": "New challenge video is here #challenge #viral",
      "create_time": "2025-02-01T10:00:00.000Z",
      "share_count": 95000,
      "collect_count": 28000,
      "comment_count": 18000,
      "play_count": 42000000,
      "video_duration": 90,
      "hashtags": [
        "#challenge",
        "#viral"
      ],
      "video_url": "https://v16-webapp-prime.tiktok.com/video/example.mp4",
      "profile_username": "examplecreator",
      "profile_url": "https://www.tiktok.com/@examplecreator",
      "is_verified": true
    }
  ]
  ```
</ResponseExample>
