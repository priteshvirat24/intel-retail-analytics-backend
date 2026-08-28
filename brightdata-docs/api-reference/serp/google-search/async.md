> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SERP async request

> Use the Bright Data SERP API async endpoint (31 languages). POST /serp/req submits or retrieves a queued SERP request and returns 200 OK as JSON.



## OpenAPI

````yaml async-api-reference POST /serp/req
openapi: 3.1.0
info:
  title: Bright Data Unblocker and SERP API (Async)
  description: API for asynchronous web data collection using Unblocker and SERP engines.
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security:
  - bearerAuth: []
paths:
  /serp/req:
    post:
      parameters:
        - in: query
          name: zone
          description: The name of your Bright Data Unlocker zone.
          required: true
          schema:
            type: string
          example: web_unlocker1
        - in: query
          name: customer
          description: Your Bright Data account ID.
          schema:
            type: string
          example: hl_xxxxxxxx
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - query
              properties:
                country:
                  description: Defines country to be used for request (2-letters code)
                  type: string
                  example: US
                query:
                  description: ''
                  type: object
                  required:
                    - q
                  properties:
                    q:
                      description: >-
                        The search query parameter. Specifies the keyword or
                        phrase you want to search for on Google.
                      type: string
                      example: pizza
                    gl:
                      description: >-
                        Two-letter country code used to define the country of
                        search
                      type: string
                      example: au
                    hl:
                      description: >-
                        Two-letter language code used to define the page
                        languages
                      type: string
                      example: en
                    start:
                      description: >-
                        Define the result offset - results to start from the
                        selected value. Used for managing pagination.
                      type: integer
                      example: 20
                brd_json:
                  description: Defines the response format
                  type: string
                  enum:
                    - json
                    - html
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/JobResponse'
components:
  schemas:
    JobResponse:
      type: object
      properties:
        response_id:
          description: Defines the job id.
          type: string
          example: s4t7w3619285042ra9dke1m8qx
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        Use your Bright Data API Key as a Bearer token in the Authorization
        header.


        **How to authenticate:**

        1. Obtain your API Key from the [Bright Data account
        settings](https://brightdata.com/cp/setting/users)

        2. Include the API Key in the Authorization header of your requests

        3. Format: `Authorization: Bearer YOUR_API_KEY`


        **Example:**

        ```

        Authorization: Bearer b5648e1096c6442f60a6c4bbbe73f8d2234d3d8324554bd...

        ```


        > [Learn how to get your Bright Data API
        key](https://docs.brightdata.com/api-reference/authentication)
      bearerFormat: API Key

````