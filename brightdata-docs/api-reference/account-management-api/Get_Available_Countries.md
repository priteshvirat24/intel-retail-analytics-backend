> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get account available countries

> Use the Bright Data Account Management API to get account available countries. GET /countrieslist returns 200 OK with zone or account JSON.

<Tip>
  Paste your API key to the authorization field. To get an API key, [Create an account](https://brightdata.com/?hs_signup=1\&utm_source=docs\&utm_campaign=playground) and learn [how to generate an API key](/api-reference/authentication#how-do-i-generate-a-new-api-key%3F)
</Tip>


## OpenAPI

````yaml api-reference/openapi GET /countrieslist
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
  /countrieslist:
    get:
      description: 'List all available countries per zone type '
      operationId: listAllAvailableCountriesPerZoneType
      responses:
        '200':
          description: OK - Successful request with response body
          content:
            application/json:
              schema:
                type: object
                properties:
                  zone_types:
                    type: object
                    properties:
                      DC_shared:
                        type: object
                        properties:
                          country_codes:
                            type: array
                            items:
                              type: string
                        required:
                          - country_codes
                      DC_dedicated_ip:
                        type: object
                        properties:
                          country_codes:
                            type: array
                            items:
                              type: string
                        required:
                          - country_codes
                      DC_dedicated_host:
                        type: object
                        properties:
                          country_codes:
                            type: array
                            items:
                              type: string
                        required:
                          - country_codes
                      ISP_shared:
                        type: object
                        properties:
                          country_codes:
                            type: array
                            items:
                              type: string
                        required:
                          - country_codes
                      ISP_dedicated_ip:
                        type: object
                        properties:
                          country_codes:
                            type: array
                            items:
                              type: string
                        required:
                          - country_codes
                      ISP_dedicated_host:
                        type: object
                        properties:
                          country_codes:
                            type: array
                            items:
                              type: string
                        required:
                          - country_codes
                    required:
                      - DC_shared
                      - DC_dedicated_ip
                      - DC_dedicated_host
                      - ISP_shared
                      - ISP_dedicated_ip
                      - ISP_dedicated_host
                required:
                  - data
                  - zone_types
                title: ListAllAvailableCountriesPerZoneTypeOk
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