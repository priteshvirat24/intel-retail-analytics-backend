> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Discover TikTok posts by URL

> Use the Bright Data Web Scraper API to discover TikTok posts by URL. Calls the POST /datasets/v3/scrape endpoint and returns a snapshot ID.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_lu702nij2f790tmv9h" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_lu702nij2f790tmv9h` to collect **Discover by URL** data.
  </Warning>
</ParamField>

<ParamField query="type" type="string" default="discover_new">
  Must be set to `discover_new`.
</ParamField>

<ParamField query="discover_by" type="string" default="url">
  Must be set to `url`.
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
      The TikTok discover URL to collect posts from.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {"url": "https://www.tiktok.com/tag/cooking"}
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "post_id": "7480000000000000000",
      "description": "5-minute meal prep ideas #cooking #mealprep",
      "create_time": "2025-03-05T12:00:00.000Z",
      "share_count": 8700,
      "collect_count": 15000,
      "comment_count": 2300,
      "play_count": 9800000,
      "video_duration": 55,
      "hashtags": [
        "#cooking",
        "#mealprep"
      ],
      "video_url": "https://v16-webapp-prime.tiktok.com/video/example.mp4",
      "profile_username": "quickmeals",
      "profile_url": "https://www.tiktok.com/@quickmeals",
      "is_verified": false
    }
  ]
  ```
</ResponseExample>
