> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Enrich column

> Use the Bright Data Deep Lookup API to enrich Column. POST /request/{id}/enrich returns enriched records as JSON with 200 OK on success.



## OpenAPI

````yaml api-reference/deep-lookup POST /request/{id}/enrich
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
  /request/{id}/enrich:
    post:
      summary: Enrich Column
      description: Add additional data columns to existing results.
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
            examples:
              - ai_meu3z0171o8k9jc4dh
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  column_name:
                    type: string
                    examples:
                      - cto_name
                  query:
                    type: string
                    examples:
                      - CTO or head of engineering name
      responses:
        '200':
          description: Enrichment triggered
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EnrichResponse'
components:
  schemas:
    EnrichResponse:
      type: object
      properties:
        column_name:
          type: string
          examples:
            - cto_name
        status:
          type: string
          description: |-
            - `processing` - Enrichment in progress
            - `completed` - Enrichment finished
          enum:
            - processing
            - completed
          examples:
            - processing
        max_additional_cost:
          type: string
          description: >-
            **Note:** `max_additional_cost` shows the maximum possible cost.
            Final cost is calculated based only on matched records.
          examples:
            - $3.65
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