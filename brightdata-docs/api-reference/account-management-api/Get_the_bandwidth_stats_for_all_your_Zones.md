> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Bandwidth stats for all your zones

> Retrieve bandwidth consumption stats for every Bright Data API across your account in 1 request, with totals returned per product and time window as JSON.

<Tip>
  Paste your API key to the authorization field. To get an API key, [Create an account](https://brightdata.com/?hs_signup=1\&utm_source=docs\&utm_campaign=playground) and learn [how to generate an API key](/api-reference/authentication#how-do-i-generate-a-new-api-key%3F)
</Tip>

<Note>Sample response redacted</Note>


## OpenAPI

````yaml api-reference/openapi GET /customer/bw
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
  /customer/bw:
    get:
      description: Get the bandwidth stats for all your Zones
      parameters:
        - in: query
          name: from
          description: Start
          required: false
          schema:
            type: string
          example: '2018-07-01T00:00:00'
        - in: query
          name: to
          description: End
          required: false
          schema:
            type: string
          example: '2018-07-02T00:00:00'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                example:
                  ID:
                    customer_id: CUST_ID
                    from: '2022-10-01T00:00:00.000Z'
                    to: '2022-11-24T00:00:00.000Z'
                    data:
                      data_center: {}
                      isp: {}
                      residential: {}
                      mobile: {}
                      unlocker: {}
                      v__ub_browser: {}
                      serp: {}
                      dc_elastic: {}
                      isp1: {}
                      test_zone: {}
                      test_zone2: {}
                      japan: {}
                      zone1_res_ex: {}
                      zone5_isp: {}
                      zone1: {}
                      zone2: {}
                      zum_rails_res_canada: {}
                      zone3: {}
                      elastic_log_test: {}
                      google_async: {}
                      last_value_ts: '2022-11-23T13:41:20.099Z'
                      last_update_ts: '2022-11-23T14:05:55.108Z'
                      sums: {}
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