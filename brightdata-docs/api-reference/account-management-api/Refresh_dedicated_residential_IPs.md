> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Refresh dedicated residential IPs

> Use the Bright Data Account Management API to refresh dedicated residential IPs via POST /zone/ips/refresh, returning JSON zone or account data with 200 OK.

<Warning>Only users with **Admin** or **Ops** roles can perform this action.</Warning>

<Warning> **Warning:** This API can modify your account settings, damage your operations or incur charges.</Warning>

<Tip>
  Paste your API key to the authorization field. To get an API key, [Create an account](https://brightdata.com/?hs_signup=1\&utm_source=docs\&utm_campaign=playground) and learn [how to generate an API key](/api-reference/authentication#how-do-i-generate-a-new-api-key%3F)
</Tip>

<Warning>
  Each dedicated residential IP refreshed costs \$0.02/refresh/IP
</Warning>


## OpenAPI

````yaml api-reference/openapi POST /zone/ips/refresh
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
  /zone/ips/refresh:
    post:
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - zone
              properties:
                zone:
                  type: string
                  description: Zone name
                  example: zone1
                vips:
                  type: array
                  description: |-
                    IPs to refresh 

                     **Note**: If refresh is needed for all allocated IPs, then `vips` parameter should be omitted. 

                     **Note**: Only works for Dedicated Residential IPs
                  items:
                    type: string
                  example:
                    - vip1
                    - vip2
                ips:
                  type: array
                  description: |-
                    IPs to refresh 

                     **Note**: If refresh is needed for all allocated IPs, then `ips` parameter should be omitted
                  items:
                    type: string
                  example:
                    - ip1
                    - ip2
                country:
                  type: string
                  description: new IPs' country (e.g. `us`)
                country_city:
                  type: string
                  description: new IPs' city (e.g. `us-chicago`)
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                example:
                  vips:
                    - vip: tr_9121_07_antalya_10
                      country: tr
                    - vip: tr_9121_07_antalya_17
                      country: tr
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