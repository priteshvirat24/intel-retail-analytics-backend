> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Active zones

> Use the Bright Data Account Management API to active Zones. GET /zone/get_active_zones returns 200 OK with zone or account configuration data as JSON.

<Tip>
  Paste your API key to the authorization field. To get an API key, [Create an account](https://brightdata.com/?hs_signup=1\&utm_source=docs\&utm_campaign=playground) and learn [how to generate an API key](/api-reference/authentication#how-do-i-generate-a-new-api-key%3F)
</Tip>


## OpenAPI

````yaml api-reference/openapi GET /zone/get_active_zones
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
  /zone/get_active_zones:
    get:
      description: Return all active zones
      responses:
        '200':
          description: Zone response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Zone'
        '401':
          description: Customer not found
components:
  schemas:
    Zone:
      required:
        - name
      type: object
      properties:
        name:
          description: The name of the zone
          type: string
        type:
          description: Zone Type, e.g. serp, isp, mobile, etc.
          type: string
      example:
        name: zone-name
        type: serp
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