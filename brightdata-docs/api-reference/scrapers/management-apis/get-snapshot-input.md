> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get snapshot input

> Use Bright Data Web Scraper API management endpoints to get Snapshot Input. GET /datasets/v3/snapshot/{id}/input returns snapshot or job status as JSON.



## OpenAPI

````yaml api-reference/dca-api get /datasets/v3/snapshot/{snapshot_id}/input
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
  /datasets/v3/snapshot/{snapshot_id}/input:
    get:
      description: Get the inputs that were used to trigger the collection
      parameters:
        - name: snapshot_id
          in: path
          required: true
          schema:
            type: string
            example: s_m4x7enmven8djfqak
            description: The ID that was returned when the collection was triggered
      responses:
        '200':
          description: Inputs in CSV format
          content:
            text/csv:
              schema:
                type: string
                example: |-
                  input1,input2
                  value1,value2
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

        Authorization: Bearer YOUR_API_KEY

        ```


        Learn how to get your Bright Data API key:
        https://docs.brightdata.com/api-reference/authentication
      bearerFormat: API Key

````