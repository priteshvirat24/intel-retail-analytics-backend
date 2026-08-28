> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Discover posts by keyword

> Use the Bright Data Web Scraper API to discover Posts by Keyword. Calls the POST /datasets/v3/scrape endpoint and returns a snapshot ID.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_lvz8ah06191smkebj4" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_lvz8ah06191smkebj4` to collect **Discover by keyword** data.
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
      The search term to find relevant posts.
    </ParamField>

    <ParamField body="date" type="string" required>
      The date filter to apply to the search.

      One of: `Past hour`, `Past day`, `Past week`, `Past month`, `Past year`, `All time`
    </ParamField>

    <ParamField body="num_of_posts" type="number">
      The number of posts to collect. Omit to retrieve all matching posts.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {"keyword": "machine learning", "date": "Past week", "num_of_posts": 100},
      {"keyword": "python tips", "date": "Past month", "num_of_posts": 50}
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "post_id": "1bsdf34",
      "url": "https://www.reddit.com/r/MachineLearning/comments/1bsdf34/",
      "user_posted": "ml_researcher",
      "title": "New paper on transformer efficiency",
      "description": "Sharing a recent paper...",
      "num_upvotes": 842,
      "num_comments": 54,
      "date_posted": "2026-04-03T09:14:00Z",
      "tag": "Research",
      "community_name": "MachineLearning",
      "community_url": "https://www.reddit.com/r/MachineLearning",
      "community_description": "Beginners to experts.",
      "community_members_num": 2900000,
      "community_rank": null,
      "related_posts": [],
      "comments": [],
      "photos": [],
      "videos": []
    }
  ]
  ```
</ResponseExample>
