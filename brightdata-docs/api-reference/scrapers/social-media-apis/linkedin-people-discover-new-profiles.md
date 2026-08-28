> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Discover new LinkedIn profiles

> Discover new LinkedIn profiles by first and last name using the Bright Data Web Scraper API with dataset ID gd_m8d03he47z8nwb5xc for prospect research.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_m8d03he47z8nwb5xc" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_m8d03he47z8nwb5xc` to collect **Discover New Profiles** data.
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
      Must be set to `https://www.linkedin.com`.
    </ParamField>

    <ParamField body="first_name" type="string">
      First name to search by
    </ParamField>

    <ParamField body="last_name" type="string">
      Last name to search by
    </ParamField>
  </Expandable>

  #### Example

  ```json theme={null}
  {
    "input":[
      {
        "url":"https://www.linkedin.com",
        "first_name":"james",
        "last_name":"smith"
      },
      {
        "url":"https://www.linkedin.com",
        "first_name":"Lisa",
        "last_name":"Ledger"
      }
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "url": "https://linkedin.com/in/muge-ozlutiras",
      "name": "Muge O*******s",
      "subtitle": null,
      "location": "Netherlands",
      "experience": null,
      "education": "ETH Zurich",
      "avatar": "htt***//m***a.l*********dms*********************6XV******************************************************************************************************************************************************************"
    }
  ]
  ```
</ResponseExample>
