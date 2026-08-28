> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Discover posts by profiles array

> Use the Bright Data Web Scraper API to discover Posts by Profiles Array. Calls the POST /datasets/v3/scrape endpoint and returns a snapshot ID.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_lwxkxvnf1cynvib9co" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_lwxkxvnf1cynvib9co` to collect **Discover by Profiles Array** data.
  </Warning>
</ParamField>

<ParamField query="type" type="string" default="discover_new">
  Must be set to `discover_new`.
</ParamField>

<ParamField query="discover_by" type="string" default="profiles_array">
  Must be set to `profiles_array`.
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
      The URL of the X.com profile to discover posts from.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {"url": "https://x.com/elonmusk"},
      {"url": "https://x.com/OpenAI"}
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "id": "2039126434510418303",
      "user_posted": "CozHealsSEN",
      "name": "SENQ Breakfast",
      "description": "LISTEN: North Queensland Cowboys front rower Matt Lodge joins Corey Parker and Andrew McCullough to discuss this weekend's match up against the Dragons",
      "date_posted": "2026-03-31T23:43:21.000Z",
      "photos": ["https://pbs.twimg.com/..."],
      "url": "https://x.com/CozHealsSEN/status/2039126434510418303",
      "quoted_post": null,
      "tagged_users": null,
      "replies": 0,
      "reposts": 4,
      "likes": 7,
      "views": 726,
      "external_url": "https://...",
      "hashtags": null,
      "followers": 814,
      "biography": "QLD brekkie show with Corey Parker & Ian Healy.",
      "posts_count": 4862,
      "profile_image_link": "https://pbs.twimg.com/...",
      "following": 430,
      "is_verified": null,
      "quotes": 0,
      "bookmarks": 0,
      "parent_post_details": {
        "date_posted": "2026-03-31T23:43:21.000Z",
        "post_id": "2039126434510418303",
        "profile_id": "889656535722360833",
        "profile_name": "SENQ Breakfast"
      },
      "videos": null,
      "verification_type": null,
      "user_id": "889656535722360833"
    }
  ]
  ```
</ResponseExample>
