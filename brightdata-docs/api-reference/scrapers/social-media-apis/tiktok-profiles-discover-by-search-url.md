> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Discover by search URL

> Use the Bright Data Web Scraper API to discover by Search URL. POST /datasets/v3/scrape starts a scraping job that returns the data as structured JSON records.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_l1villgoiiidt09ci" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_l1villgoiiidt09ci` to collect **Discover by Search URL** data.
  </Warning>
</ParamField>

<ParamField query="type" type="string" default="discover_new">
  Must be set to `discover_new`.
</ParamField>

<ParamField query="discover_by" type="string" default="search_url">
  Must be set to `search_url`.
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
    <ParamField body="search_url" type="string" required>
      The TikTok search URL to discover profiles from.
    </ParamField>

    <ParamField body="country" type="string" required>
      The country from which to perform the search.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {
        "search_url": "https://www.tiktok.com/search/user?q=cooking",
        "country": "us"
      }
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "account_id": "987654321",
      "nickname": "Cooking Daily",
      "biography": "Easy recipes for busy people",
      "bio_link": "https://example.com/recipes",
      "is_verified": false,
      "followers": 2500000,
      "following": 150,
      "likes": 45000000,
      "videos_count": 320,
      "create_time": "2020-03-15T00:00:00.000Z",
      "url": "https://www.tiktok.com/@cookingdaily",
      "profile_pic_url": "https://p16-sign-sg.tiktokcdn.com/example-avatar~100x100.jpeg",
      "profile_pic_url_hd": "https://p16-sign-sg.tiktokcdn.com/example-avatar~720x720.jpeg",
      "awg_engagement_rate": 0.0521,
      "is_private": false,
      "region": "US"
    }
  ]
  ```
</ResponseExample>
