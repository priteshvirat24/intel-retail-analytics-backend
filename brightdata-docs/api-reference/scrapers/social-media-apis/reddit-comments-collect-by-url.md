> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Collect Reddit comments by URL

> Use the Bright Data Web Scraper API to collect Reddit comments by URL. Calls the POST /datasets/v3/scrape endpoint and returns a snapshot ID.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_lvzdpsdlw09j6t702" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_lvzdpsdlw09j6t702` to collect **Comments by URL** data.
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
      The URL of the Reddit post or comment thread to collect comments from.
    </ParamField>

    <ParamField body="days_back" type="number">
      Limit results to comments published within this number of days.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {"url": "https://www.reddit.com/r/learnpython/comments/1asdf12/", "days_back": 7},
      {"url": "https://www.reddit.com/r/python/comments/1bsdf34/"}
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "comment_id": "k5f7a9b",
      "url": "https://www.reddit.com/r/learnpython/comments/1asdf12/comment/k5f7a9b/",
      "user_posted": "helpful_dev",
      "comment": "Start with the official Python tutorial, it covers the basics well.",
      "date_posted": "2026-03-15T08:42:00Z",
      "num_upvotes": 24,
      "num_replies": 3,
      "replies": [],
      "post_url": "https://www.reddit.com/r/learnpython/comments/1asdf12/",
      "post_id": "1asdf12",
      "post_language": "en",
      "post_state": "active",
      "post_type": "text",
      "images": [],
      "community_name": "learnpython",
      "community_url": "https://www.reddit.com/r/learnpython",
      "community_description": "Subreddit for posting questions and asking for general advice about your Python code.",
      "community_members_num": 1120000,
      "community_rank": null,
      "is_moderator": false,
      "is_pinned": false,
      "has_bot_in_username": false,
      "is_locked": false,
      "is_admin_post": false,
      "is_archived_post": false,
      "is_moderator_post": false,
      "is_quarantined_post": false,
      "is_not_safe_for_work_post": false,
      "is_eligible_for_content_blocking_post": false,
      "is_promoted_post": false
    }
  ]
  ```
</ResponseExample>
