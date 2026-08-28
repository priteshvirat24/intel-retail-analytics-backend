> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Bandwidth stats for a zone

> Use the Bright Data Account Management API to bandwidth stats for a zone. GET /zone/bw returns 200 OK with zone or account configuration data as JSON.

<Tip>
  Paste your API key to the authorization field. To get an API key, [Create an account](https://brightdata.com/?hs_signup=1\&utm_source=docs\&utm_campaign=playground) and learn [how to generate an API key](/api-reference/authentication#how-do-i-generate-a-new-api-key%3F)
</Tip>


## OpenAPI

````yaml api-reference/openapi GET /zone/bw
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
  /zone/bw:
    get:
      description: Get the bandwidth stats for a Zone
      parameters:
        - in: query
          name: zone
          description: Zone name
          required: true
          schema:
            type: string
          example: resi-zone-1
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
                  'ID:':
                    customer_id: customer_id
                    from: '2022-10-01T00:00:00.000Z'
                    to: '2022-11-23T00:00:00.000Z'
                    data:
                      static:
                        bw_sum:
                          - 0
                          - 745
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 6960
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                        bw_dn:
                          - 0
                          - 525
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 5990
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                        bw_up:
                          - 0
                          - 220
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 970
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                        http_direct_req:
                          - 0
                          - 1
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                        bw_sum_dc:
                          - 0
                          - 745
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 6960
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                        bw_api:
                          - 0
                          - 745
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 6960
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                        https_direct_req:
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 1
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                          - 0
                    last_value_ts: >-
                      2022-11-19T19:1* Connection #0 to host brightdata.com left
                      intact 8:51.546Z
                    last_update_ts: '2022-11-22T11:35:32.122Z'
                    sums:
                      static:
                        back_m1:
                          bw_sum: 745
                          bw_dn: 525
                          bw_up: 220
                          http_direct_req: 1
                          bw_sum_dc: 745
                          bw_api: 745
                          https_direct_req: 0
                        back_m0:
                          bw_sum: 6960
                          bw_dn: 5990
                          bw_up: 970
                          http_direct_req: 0
                          bw_sum_dc: 6960
                          bw_api: 6960
                          https_direct_req: 1
                        back_d2:
                          bw_sum: 0
                          bw_dn: 0
                          bw_up: 0
                          http_direct_req: 0
                          bw_sum_dc: 0
                          bw_api: 0
                          https_direct_req: 0
                        back_d1:
                          bw_sum: 0
                          bw_dn: 0
                          bw_up: 0
                          http_direct_req: 0
                          bw_sum_dc: 0
                          bw_api: 0
                          https_direct_req: 0
                        back_d0:
                          bw_sum: 0
                          bw_dn: 0
                          bw_up: 0
                          http_direct_req: 0
                          bw_sum_dc: 0
                          bw_api: 0
                          https_direct_req: 0
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