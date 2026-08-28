> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Domain consumption

> Retrieve per-domain usage metrics including bandwidth and request count from the Bright Data Domain Consumption API. Returns 200 OK with JSON results.

## Sample Requests

<CodeGroup>
  ```sh All zones theme={null}
  curl --request GET \
    --url 'api.brightdata.com/domains/bw?from=2025-12-01&to=2025-12-10' \
    --header 'Authorization: Bearer API_KEY'
  ```

  ```sh Bandwidth by zone theme={null}
  curl --request GET \
    --url 'api.brightdata.com/domains/bw?from=2025-12-01&to=2025-12-10&zones=zone_name' \
    --header 'Authorization: Bearer API_KEY'
  ```

  ```sh Requests by zone theme={null}
  curl --request GET \
    --url 'api.brightdata.com/domains/req?from=2025-12-01&to=2025-12-10&zones=zone_name' \
    --header 'Authorization: Bearer API_KEY'
  ```
</CodeGroup>


## OpenAPI

````yaml api-reference/proxy-manager GET /domains/{metric}
openapi: 3.1.0
info:
  title: Brightdata API
  description: API for interaction with datasets marketplace
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security:
  - bearerAuth: []
paths:
  /domains/{metric}:
    get:
      summary: Domain usage metrics
      description: >-
        Returns domain usage metrics from Bright Data. Supported metrics: bw
        (Bandwidth consumption), req (Request count).
      operationId: getDomainMetrics
      parameters:
        - name: metric
          in: path
          required: true
          description: |-
            Metric type to query:
            #### Available Metrics 
            - `/bw` - Bandwidth consumption 
            - `/req` - Request count
          schema:
            type: string
            enum:
              - bw
              - req
          example: bw
        - name: from
          in: query
          required: true
          description: Start date (YYYY-MM-DD)
          schema:
            type: string
            format: date
            example: '2025-12-01'
        - name: to
          in: query
          required: true
          description: End date (YYYY-MM-DD)
          schema:
            type: string
            format: date
            example: '2025-12-10'
        - name: zones
          in: query
          required: false
          description: Zone name filter. Omit to include all zones.
          schema:
            type: string
            example: zone_name
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                additionalProperties: true
        '400':
          description: Invalid request parameters
        '401':
          description: Unauthorized
        '500':
          description: Internal server error
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