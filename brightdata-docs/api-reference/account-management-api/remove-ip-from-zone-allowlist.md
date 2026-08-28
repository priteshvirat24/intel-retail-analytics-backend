> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Remove IP from zone allowlist

> Use the Bright Data Account Management API to remove IP from Zone allowlist. DELETE /zone/whitelist returns 200 OK with zone or account JSON.

<Warning>Only users with **Admin** or **Ops** roles can perform this action.</Warning>

<Warning> **Warning:** This API can modify your account settings, damage your operations or incur charges.</Warning>

<Tip>
  Paste your API key to the authorization field. To get an API key, [Create an account](https://brightdata.com/?hs_signup=1\&utm_source=docs\&utm_campaign=playground) and learn [how to generate an API key](/api-reference/authentication#how-do-i-generate-a-new-api-key%3F)
</Tip>


## OpenAPI

````yaml api-reference/openapi DELETE /zone/whitelist
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
  /zone/whitelist:
    delete:
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                zone:
                  type: string
                  description: |-
                    Zone name. 

                     **Note**: can be skipped to affect all your zones.
                ip:
                  type: string
                  description: |-
                    can be in one fo the following formats: 

                     + Delete a single IP - `ip="1.2.1.2"` 
                     + Delete a IP range - `ip="1.2.1.2-1.2.1.10"` 
                     + Delete a IP subnet - `ip="10.20.30.40/24"` 
                     + Delete a IP mask - `ip="10.20.30.40/255.255.255.0"`
      responses:
        '200':
          description: OK
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