> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Discover channels by keyword

> Use the Bright Data Web Scraper API to discover Channels by Keyword. Calls the POST /datasets/v3/scrape endpoint and returns a snapshot ID.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_lk538t2k2p1k3oos71" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_lk538t2k2p1k3oos71` to collect **Discover Channels by Keyword** data.
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
    <ParamField body="keyword" type="string" required>
      The keyword to search for YouTube channels.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {
        "keyword": "cooking tutorials"
      }
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "url": "https://www.youtube.com/@channelname",
      "handle": "@channelname",
      "banner_img": "https://...",
      "profile_image": "https://...",
      "name": "Channel Name",
      "subscribers": 299,
      "Description": "Channel description...",
      "videos_count": 21,
      "created_date": "2024-11-25T00:00:00.000Z",
      "views": 98723,
      "Details": {"location": "United States"},
      "Links": ["youtube.com/@channelname"],
      "identifier": "UC...",
      "id": "UC...",
      "has_podcast": false,
      "top_videos": [
        {
          "Image_url": "https://...",
          "posted_time": "3 weeks ago",
          "title": "Video Title",
          "video_url": "https://www.youtube.com/watch?v=abc",
          "views": 11
        }
      ]
    }
  ]
  ```
</ResponseExample>
