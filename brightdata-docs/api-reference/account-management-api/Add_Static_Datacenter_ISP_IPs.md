> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add static IP(s)

> Use the Bright Data Account Management API to add Static IP(s). POST /zone/ips returns 200 OK with zone or account configuration data as JSON.

<Warning>Only users with **Admin** or **Ops** roles can perform this action.</Warning>

<Warning> **Warning:** This API can modify your account settings, damage your operations or incur charges.</Warning>

<Tip>
  Paste your API key to the authorization field. To get an API key, [Create an account](https://brightdata.com/?hs_signup=1\&utm_source=docs\&utm_campaign=playground) and learn [how to generate an API key](/api-reference/authentication#how-do-i-generate-a-new-api-key%3F)
</Tip>


## OpenAPI

````yaml api-reference/openapi POST /zone/ips
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
  /zone/ips:
    post:
      description: Add Static IPs for Datacenter and ISP
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - customer
                - zone
                - count
              properties:
                customer:
                  type: string
                  description: Customer
                zone:
                  description: Zone name
                  type: string
                count:
                  type: number
                  description: Number of IPs
                country:
                  type: string
                  description: new IPs' country (e.g. `us`)
                  example: us
                country_city:
                  type: string
                  description: new IPs' city (e.g. `us-chicago`)
                  example: us-chicago
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                properties:
                  ips:
                    type: array
                    items:
                      type: string
                    example:
                      - 1.1.1.1
                      - 1.1.1.2
                      - 1.1.1.3
                  new_ips:
                    type: array
                    items:
                      type: string
                    example:
                      - 1.1.1.1
                      - 1.1.1.3
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