> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Discover by profile URL

> Use the Bright Data Web Scraper API to discover by Profile URL. POST /datasets/v3/scrape starts a scraping job that returns the data as structured JSON records.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_lu702nij2f790tmv9h" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_lu702nij2f790tmv9h` to collect **Discover by Profile URL** data.
  </Warning>
</ParamField>

<ParamField query="type" type="string" default="discover_new">
  Must be set to `discover_new`.
</ParamField>

<ParamField query="discover_by" type="string" default="profile_url">
  Must be set to `profile_url`.
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
      The URL of the TikTok profile to discover posts from.
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

    <ParamField body="posts_to_not_include" type="string[]">
      Post IDs to exclude from the results.
    </ParamField>

    <ParamField body="what_to_collect" type="string">
      Specifies what data to collect from each post.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {
        "url": "https://www.tiktok.com/@mrbeast",
        "num_of_posts": 10,
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
      "description": "You won't believe what happened next #challenge",
      "create_time": "2025-01-20T18:00:00.000Z",
      "share_count": 120000,
      "collect_count": 45000,
      "comment_count": 32000,
      "play_count": 85000000,
      "video_duration": 120,
      "hashtags": [
        "#challenge"
      ],
      "video_url": "https://v16-webapp-prime.tiktok.com/video/example.mp4",
      "profile_username": "examplecreator",
      "profile_url": "https://www.tiktok.com/@examplecreator",
      "is_verified": true
    }
  ]
  ```
</ResponseExample>
