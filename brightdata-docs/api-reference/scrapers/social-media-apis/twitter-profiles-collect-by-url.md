> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Collect X (Twitter) profiles by URL

> Use the Bright Data Web Scraper API to collect X (Twitter) profiles by URL. Calls the POST /datasets/v3/scrape endpoint.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_lwxmeb2u1cniijd7t4" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_lwxmeb2u1cniijd7t4` to collect **Profiles by URL** data.
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
      The URL of the X.com profile to collect.
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
