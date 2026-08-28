> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Discover profiles by username

> Use the Bright Data Web Scraper API to discover Profiles by Username. Calls the POST /datasets/v3/scrape endpoint and returns a snapshot ID.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_lwxmeb2u1cniijd7t4" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_lwxmeb2u1cniijd7t4` to collect **Discover by Username** data.
  </Warning>
</ParamField>

<ParamField query="type" type="string" default="discover_new">
  Must be set to `discover_new`.
</ParamField>

<ParamField query="discover_by" type="string" default="user_name">
  Must be set to `user_name`.
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
    <ParamField body="user_name" type="string" required>
      The username of the X.com profile.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {"user_name": "elonmusk"}
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "x_id": "1077446982",
      "url": "https://x.com/RepRWilliams",
      "id": "RepRWilliams",
      "profile_name": "Rep. Roger Williams",
      "biography": "Chairman of @HouseSmallBiz. Conservative fighting for lower taxes, less regulations, and more freedom for Texans.",
      "is_verified": true,
      "profile_image_link": "https://pbs.twimg.com/...",
      "external_link": "https://williams.house.gov/",
      "date_joined": "2013-01-10T19:21:22.000Z",
      "following": 910,
      "followers": 24746,
      "subscriptions": 0,
      "location": "North Texas",
      "birth_date": null,
      "posts_count": 10434,
      "posts": [
        {
          "date_posted": "2026-04-07T19:10:38.000Z",
          "description": "As Chairman of @HouseSmallBiz, I have seen the positive impact the Working Families Tax Cuts have had on small businesses.",
          "likes": 6,
          "post_id": "2041594516373700624",
          "post_url": "https://x.com/RepRWilliams/status/2041594516373700624",
          "replies": 3,
          "reposts": 3,
          "views": 449
        }
      ],
      "is_business_account": false,
      "is_government_account": false,
      "banner_image": "https://pbs.twimg.com/..."
    }
  ]
  ```
</ResponseExample>
