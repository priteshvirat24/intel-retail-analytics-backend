> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Switch automatic failover

> Use the Bright Data Account Management API to switch Automatic Failover. POST /zone/switch_100uptime returns the requested zone or account configuration data.

<Warning> **Warning:** This API can modify your account settings, damage your operations or incur charges. </Warning>

<Tip>
  Paste your API key to the authorization field. To get an API key, [Create an account](https://brightdata.com/?hs_signup=1\&utm_source=docs\&utm_campaign=playground) and learn [how to generate an API key](/api-reference/authentication#how-do-i-generate-a-new-api-key%3F)
</Tip>


## OpenAPI

````yaml api-reference/openapi POST /zone/switch_100uptime
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
  /zone/switch_100uptime:
    post:
      description: Switch automatic failover ON/OFF in a Static zone
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ZoneAndActive'
      responses:
        '200':
          description: OK
components:
  schemas:
    ZoneAndActive:
      required:
        - ip
      type: object
      properties:
        zone:
          description: Zone name
          type: string
        active:
          description: '`0`: Disable automatic failover, `1`: Enable automatic failover'
          type: integer
          enum:
            - 0
            - 1
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