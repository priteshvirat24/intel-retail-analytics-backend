> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Monitor delivery

> Use Bright Data Web Scraper API management endpoints to monitor Delivery. GET /datasets/v3/delivery/{delivery_id} returns snapshot or job status as JSON.



## OpenAPI

````yaml api-reference/dca-api get /datasets/v3/delivery/{delivery_id}
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
  /datasets/v3/delivery/{delivery_id}:
    get:
      description: The call returns the delivery status
      parameters:
        - name: delivery_id
          in: path
          description: The unique delivery id returned from the delivery API endpoint
          required: true
          schema:
            type: string
          example: d_lysxl9vf2dobrb6h31
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    description: The delivery job ID
                  delivery_files:
                    type: array
                    description: List of delivered files
                    items:
                      type: object
                      properties:
                        filename:
                          type: string
                        delivery_ts:
                          type: integer
                  status:
                    type: string
                    enum:
                      - done
                      - canceled
                      - failed
                    description: Status of the delivery
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