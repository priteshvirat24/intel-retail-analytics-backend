> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Receive data from real-time work scraper

> Use the Bright Data Scraper Studio API to receive data from a real-time scraper. Triggers a custom collector job; returns 200 OK with JSON results.

<Tip>
  **Recommended:** We strongly recommend using the `timeout` parameter on polling requests to reduce unnecessary API calls and help avoid rate limits.
</Tip>

<Note>
  Result data is available for download for 7 days after collection. To avoid expiration, make sure to download the data within 7 days or configure a delivery method to get it automatically to your storage.
</Note>

## Rate limits

* 165,000 requests per minute


## OpenAPI

````yaml api-reference/web-scraper-ide-rest-api GET /dca/get_result
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
  /dca/get_result:
    get:
      description: Receive data from real-time work scraper
      parameters:
        - name: response_id
          in: query
          required: true
          schema:
            type: string
          description: A unique identification of response
        - name: timeout
          in: query
          required: false
          schema:
            type: string
            example: 50s
          description: >-
            Enables long-polling. The request waits up to this duration for the
            result to become available instead of returning `202` immediately.
            Format is `Xs` where X is an integer between 25 and 50 (for example,
            `25s`, `30s`, `50s`). If no result is available within the timeout,
            the response returns `202` as usual. Use this to reduce polling
            calls and avoid hitting rate limits.
      responses:
        '200':
          description: OK
          content:
            application/json:
              examples:
                Sample (old scrapers):
                  value:
                    input:
                      url: https://targetwebsite.com/product_id/
                    line_1: Lorem ipsum dolor sit amet
                    line_2: consectetur adipisicing elit
                Sample (new scrapers):
                  value:
                    - line_1: Lorem ipsum dolor sit amet
                      line_2: consectetur adipisicing elit
        '202':
          description: >-
            Result not ready yet. Returned when no result is available,
            including when a `timeout` is set and the result does not become
            available within the timeout window. Poll again with the same
            `response_id`.
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