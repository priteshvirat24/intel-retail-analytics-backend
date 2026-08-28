> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cancel request

> Use the Bright Data Deep Lookup API to cancel Request. POST /request/{id}/cancel returns enriched records as JSON with 200 OK on success.



## OpenAPI

````yaml api-reference/deep-lookup POST /request/{id}/cancel
openapi: 3.1.0
info:
  title: Bright Data Deep Lookup API
  description: >-
    The Bright Data Deep Lookup API lets you preview, refine, and execute
    research queries.

    Supports enrichment, cancellation, and exporting results in multiple
    formats.
  version: 1.0.0
servers:
  - url: https://api.brightdata.com/datasets/deep_lookup/v1
security:
  - bearerAuth: []
paths:
  /request/{id}/cancel:
    post:
      summary: Cancel Request
      description: Cancel an in-progress research request.
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
            examples:
              - ai_meu3z0171o8k9jc4dh
      responses:
        '200':
          description: Request cancelled
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CancelResponse'
components:
  schemas:
    CancelResponse:
      type: object
      properties:
        request_id:
          type: string
          examples:
            - ai_meu3z0171o8k9jc4dh
        status:
          type: string
          examples:
            - cancelled
        records_processed:
          type: integer
          examples:
            - 45
        charge:
          type: string
          examples:
            - $45.00
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