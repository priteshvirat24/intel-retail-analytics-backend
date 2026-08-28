> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# All classification data

> Use the Bright Data Scraping Shield API to retrieve all Classification Data. GET /shield/class returns 200 OK with site classification data as JSON.



## OpenAPI

````yaml api-reference/scraping-shield-rest-api GET /shield/class
openapi: 3.1.0
info:
  title: Bright Data API
  description: >-
    API for Bright Data Scraping Shield - retrieve domain classification and
    usage data for outgoing proxy traffic
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security:
  - bearerAuth: []
paths:
  /shield/class:
    get:
      description: Get all classification data
      parameters:
        - name: from
          in: query
          schema:
            type: string
          description: >-
            start time frame of requested data. Example:
            `from=2018-07-01T00:00:00`
        - name: to
          in: query
          schema:
            type: string
          description: 'end time frame of requested data. Example: `to=2018-07-02T00:00:00`'
        - name: cn
          in: query
          schema:
            type: string
          description: 'country of the request origin. Example: `cn=uk`'
        - name: peer_cn
          in: query
          schema:
            type: string
          description: 'country of the peer IP. Example: `peer_cn=us`'
        - name: categories
          in: query
          schema:
            type: string
          description: 'returns only specific classifications. Example: `categories=ads`'
      responses:
        '200':
          description: OK
          content:
            application/json:
              examples:
                response:
                  value:
                    - class: Shopping
                      req: 1139485
                      bw: 61138544246
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