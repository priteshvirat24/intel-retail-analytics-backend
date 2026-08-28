> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Discover TikTok posts by keyword

> Use the Bright Data Web Scraper API to discover TikTok posts by keyword. Calls the POST /datasets/v3/scrape endpoint and returns a snapshot ID.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_lu702nij2f790tmv9h" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_lu702nij2f790tmv9h` to collect **Discover by Keyword** data.
  </Warning>
</ParamField>

<ParamField query="type" type="string" default="discover_new">
  Must be set to `discover_new`.
</ParamField>

<ParamField query="discover_by" type="string" default="keyword">
  Must be set to `keyword`.
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
    <ParamField body="search_keyword" type="string" required>
      The keyword to search for TikTok posts.
    </ParamField>

    <ParamField body="num_of_posts" type="number">
      The number of posts to collect. Missing value indicates no limit.
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
        "search_keyword": "cooking recipes",
        "num_of_posts": 20
      }
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "post_id": "7500000000000000000",
      "description": "Easy pasta recipe you need to try #cooking #recipes #foodtok",
      "create_time": "2025-02-10T09:15:00.000Z",
      "share_count": 3200,
      "collect_count": 8900,
      "comment_count": 1500,
      "play_count": 5200000,
      "video_duration": 60,
      "hashtags": [
        "#cooking",
        "#recipes",
        "#foodtok"
      ],
      "video_url": "https://v16-webapp-prime.tiktok.com/video/example.mp4",
      "profile_username": "homechef",
      "profile_url": "https://www.tiktok.com/@homechef",
      "is_verified": false
    }
  ]
  ```
</ResponseExample>
