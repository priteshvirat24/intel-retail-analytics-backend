> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Collect channels by URL

> Use the Bright Data Web Scraper API to collect Channels by URL. POST /datasets/v3/scrape starts a scraping job that returns the data as structured JSON records.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_lk538t2k2p1k3oos71" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_lk538t2k2p1k3oos71` to collect **YouTube channels** data.
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
      The YouTube channel URL to collect data from.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {"url": "https://www.youtube.com/@MrBeast"},
      {"url": "https://www.youtube.com/@PewDiePie"}
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
