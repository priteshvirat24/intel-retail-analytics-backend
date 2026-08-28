> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Collect pages and profiles by URL

> Use the Bright Data Web Scraper API to collect Pages and Profiles by URL. Calls the POST /datasets/v3/scrape endpoint and returns a snapshot ID.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_mf124a0511bauquyow" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_mf124a0511bauquyow` to collect **Facebook pages and profiles** data.
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
      The URL of the Facebook page or profile to collect.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {"url": "https://www.facebook.com/zuck"},
      {"url": "https://www.facebook.com/NASA"}
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "id": "100063743733252",
      "url": "https://www.facebook.com/tgfightsport",
      "page_name": "TG-Fight Sport",
      "username": "tgfightsport",
      "entity_type": "PAGE",
      "summary_text": "Martial arts training for all levels...",
      "primary_category": "Martial Arts School",
      "address": { "formatted": "Alleestrasse 1, Beckum, Germany" },
      "phones": ["+49 176 68576249"],
      "emails": ["tg-fightsport@hotmail.com"],
      "websites": null,
      "rating": null,
      "contact_and_basic_info": {
        "basic_info": {
          "hours": { "open_now": true },
          "rating": { "count": 4, "value": 0 }
        },
        "categories": ["Martial Arts School"],
        "contact_info": {
          "address": { "formatted": "Alleestrasse 1, Beckum, Germany, 59269" },
          "emails": ["tg-fightsport@hotmail.com"],
          "websites": ["https://www.tg-fightsport.com/"]
        }
      },
      "followers": 870,
      "logo": "https://...",
      "is_verified": false
    }
  ]
  ```
</ResponseExample>
