> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get preview data

> Use the Bright Data Deep Lookup API to get Preview Data. GET /preview/{id} returns enriched records as JSON with 200 OK on success.



## OpenAPI

````yaml api-reference/deep-lookup GET /preview/{id}
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
  /preview/{id}:
    get:
      summary: Get Preview Data
      description: Retrieve the preview results and metadata.
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
            examples:
              - dld_meu4lhla1lj08i6p30
      responses:
        '200':
          description: Preview details
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetPreviewResponse'
components:
  schemas:
    GetPreviewResponse:
      type: object
      properties:
        preview_id:
          type: string
          examples:
            - dld_meu4lhla1lj08i6p30
        query:
          type: string
          examples:
            - >-
              Find all AI startups founded after 2020 with more than 50
              employees
        status:
          type: string
          description: |-
            - `queued` - Request is waiting to be processed
            - `running` - Preview is being generated
            - `completed` - Results ready
            - `failed` - Error occurred
          enum:
            - pending
            - processing
            - completed
            - failed
          examples:
            - completed
        sample_data:
          type: array
          items:
            type: object
          examples:
            - company_name: Anthropic
              website: anthropic.com
              founded_year: 2021
              employee_count: 160
        columns:
          type: array
          items:
            type: object
          examples:
            - - company_name: Anthropic
                website: anthropic.com
                founded_year: 2021
                employee_count: 160
        result_limit:
          type: integer
          examples:
            - 10
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