> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Discover videos by podcast URL

> Use the Bright Data Web Scraper API to discover Videos by Podcast URL. Calls the POST /datasets/v3/scrape endpoint and returns a snapshot ID.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_lk56epmy2i5g7lzu0k" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_lk56epmy2i5g7lzu0k` to collect **Discover Videos by Podcast URL** data.
  </Warning>
</ParamField>

<ParamField query="type" type="string" default="discover_new">
  Must be set to `discover_new`.
</ParamField>

<ParamField query="discover_by" type="string" default="podcast_url">
  Must be set to `podcast_url`.
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
      The YouTube podcast URL to discover videos from.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {"url": "https://www.youtube.com/playlist?list=PLrAXtmErZgOeiKm4sgNOknGvNjby9efdf"}
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "url": "https://www.youtube.com/watch?v=4L_m0m3bEtE",
      "title": "Video Title Here",
      "youtuber": "@channelname",
      "video_url": "https://...",
      "video_length": 96,
      "likes": 18,
      "views": 1648,
      "date_posted": "2025-04-18T05:26:16.000Z",
      "description": "Video description...",
      "num_comments": 0,
      "subscribers": 4810000,
      "video_id": "4L_m0m3bEtE",
      "channel_url": "https://www.youtube.com/@channelname",
      "preview_image": "https://i.ytimg.com/vi/4L_m0m3bEtE/maxresdefault.jpg",
      "shortcode": "4L_m0m3bEtE",
      "verified": true,
      "handle_name": "Channel Name",
      "is_sponsored": false,
      "quality": "hd1080",
      "transcript": "...",
      "tags": ["tag1", "tag2"],
      "is_age_restricted": false
    }
  ]
  ```
</ResponseExample>
