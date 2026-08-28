> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Discover posts by subreddit URL

> Use the Bright Data Web Scraper API to discover Posts by Subreddit URL. Calls the POST /datasets/v3/scrape endpoint and returns a snapshot ID.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_lvz8ah06191smkebj4" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_lvz8ah06191smkebj4` to collect **Discover by subreddit URL** data.
  </Warning>
</ParamField>

<ParamField query="type" type="string" default="discover_new">
  Must be set to `discover_new`.
</ParamField>

<ParamField query="discover_by" type="string" default="subreddit_url">
  Must be set to `subreddit_url`.
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
      The URL of the subreddit to collect posts from.
    </ParamField>

    <ParamField body="sort_by" type="string">
      The sort order for returned posts.

      One of: `new`, `top`, `hot`
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {"url": "https://www.reddit.com/r/learnpython/", "sort_by": "hot"},
      {"url": "https://www.reddit.com/r/datascience/", "sort_by": "top"}
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "post_id": "1csdf56",
      "url": "https://www.reddit.com/r/learnpython/comments/1csdf56/",
      "user_posted": "newbie_dev",
      "title": "Best resources for learning pandas?",
      "description": "I'm about two weeks into Python...",
      "num_upvotes": 312,
      "num_comments": 41,
      "date_posted": "2026-04-05T14:05:00Z",
      "tag": "Help",
      "community_name": "learnpython",
      "community_url": "https://www.reddit.com/r/learnpython",
      "community_description": "Subreddit for posting questions and asking for general advice about your Python code.",
      "community_members_num": 1120000,
      "community_rank": null,
      "related_posts": [],
      "comments": [],
      "photos": [],
      "videos": []
    }
  ]
  ```
</ResponseExample>
