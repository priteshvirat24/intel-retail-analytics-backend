> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Available Datacenter & ISP IPs/zone

> Use the Bright Data Account Management API to available Datacenter & ISP IPs/Zone. GET /zone/route_ips returns 200 OK with zone or account JSON.

<Tip>
  Paste your API key to the authorization field. To get an API key, [Create an account](https://brightdata.com/?hs_signup=1\&utm_source=docs\&utm_campaign=playground) and learn [how to generate an API key](/api-reference/authentication#how-do-i-generate-a-new-api-key%3F)
</Tip>


## OpenAPI

````yaml api-reference/openapi GET /zone/route_ips
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
  /zone/route_ips:
    get:
      tags:
        - Proxy
      description: Get the available Data center/ISP IPs per Zone
      parameters:
        - name: zone
          in: query
          description: Zone
          required: true
          schema:
            type: string
        - name: country
          in: query
          description: 2-letter Country code
          schema:
            type: string
        - name: list_countries
          in: query
          description: >-
            Return `JSON` array of `[{ip, country},..]` instead of plain list of
            IPs
          schema:
            type: boolean
      responses:
        '200':
          description: >-
            Successful response with plain IPs list separated by new line, or
            JSON array of `[{ip, country},..]` in case `list_countries=true`
          content:
            application/json:
              schema:
                oneOf:
                  - type: object
                    description: >-
                      Return `JSON` array of `[{ip, country},..]` when
                      `list_countries=true` 

                       ## Example: 

                       ```
                      [
                        {"ip": "1.1.1.1", "country": "us"},
                        {"ip": "1.1.2.2", "country": "hk"},
                      ]
                    properties:
                      ip:
                        type: string
                        description: IP address
                        example: 1.1.1.1
                      country:
                        type: string
                        description: 2-letter Country code
                        example: us
                    example:
                      - ip: 10.0.0.0
                        country: us
                      - ip: 1.1.1.1
                        country: gb
                      - ip: 1.1.2.2
                        country: hk
                  - type: string
                    description: >-
                      Plain list of IPs separated by new line when
                      `list_countries=false` 

                       ## Example: 

                       ```
                      1.1.1.1

                      1.1.2.2

                      10.0.0.0

                      ```
                    example: 10.0.0.0/24
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