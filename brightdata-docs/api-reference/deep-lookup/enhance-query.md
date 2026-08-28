> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Enhance query

> Use the Bright Data Deep Lookup API to enhance Query. POST /enhance_query returns enriched records as JSON with 200 OK on success.



## OpenAPI

````yaml api-reference/deep-lookup POST /enhance_query
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
  /enhance_query:
    post:
      summary: Enhance Query
      description: Refine your research query with additional requirements.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                required:
                  - query
                properties:
                  query:
                    type: string
                    examples:
                      - Find all AI startups
      responses:
        '200':
          description: Query enhanced successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EnhanceQueryResponse'
components:
  schemas:
    EnhanceQueryResponse:
      type: object
      properties:
        enhanced_query:
          type: string
          examples:
            - >-
              Find all AI startups in United States that raised Series A funding
              or later with headquarters in major tech hubs
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