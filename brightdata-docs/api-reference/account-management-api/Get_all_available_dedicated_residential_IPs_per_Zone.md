> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get available dedicated IPs per zone

> Use the Bright Data Account Management API to get available dedicated IPs per Zone via GET /zone/route_vips, returning JSON zone or account data with 200 OK.

<Tip>
  Paste your API key to the authorization field. To get an API key, [Create an account](https://brightdata.com/?hs_signup=1\&utm_source=docs\&utm_campaign=playground) and learn [how to generate an API key](/api-reference/authentication#how-do-i-generate-a-new-api-key%3F)
</Tip>

<Warning>Only works with residential dedicated zone</Warning>


## OpenAPI

````yaml api-reference/openapi GET /zone/route_vips
openapi: 3.0.1
info:
  title: Bright Data API
  description: >-
    Integrate Bright Data APIs to your pipeline and secure high-end scraping
    precision
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security:
  - bearerAuth: []
paths:
  /zone/route_vips:
    get:
      description: Get all available residential dedicated IPs per Zone
      parameters:
        - in: query
          name: zone
          description: Zone Info
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
        '403':
          description: Vip routes not found
        '422':
          description: >-
            This endpoint is not available with the chosen zone. Please use it
            only with active Dedicated Residential zones with allocated gIPs
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        Use your Bright Data API Key as a Bearer token in the Authorization
        header.


        **How to authenticate:**

        1. Obtain your API Key from the Bright Data account settings at
        https://brightdata.com/cp/setting/users

        2. Include the API Key in the Authorization header of your requests

        3. Format: `Authorization: Bearer YOUR_API_KEY`


        **Example:**

        ```

        Authorization: Bearer
        b5648e1096c6442f60a6c4bbbe73f8d2234d3d8324554bd6a7ec8f3f251f07df

        ```


        Learn how to get your Bright Data API key:
        https://docs.brightdata.com/api-reference/authentication
      bearerFormat: API Key

````