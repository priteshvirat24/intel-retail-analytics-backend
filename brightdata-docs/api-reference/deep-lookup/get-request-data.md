> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get request data

> Use the Bright Data Deep Lookup API to get Request Data. GET /request/{id} returns enriched records as JSON with 200 OK on success.



## OpenAPI

````yaml api-reference/deep-lookup GET /request/{id}
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
  /request/{id}:
    get:
      summary: Get Request Data
      description: Retrieve the full results of your research.
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
          description: Request data
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RequestDataResponse'
components:
  schemas:
    RequestDataResponse:
      type: object
      properties:
        request_id:
          type: string
          examples:
            - ai_meu3z0171o8k9jc4dh
        query:
          type: string
          examples:
            - Find all AI startups in Israel
        status:
          type: string
          examples:
            - completed
        title:
          type: string
          examples:
            - AI startups in Isreal
        step:
          type: string
          description: |-
            - `identifying` - Understanding and analyzing the query
            - `generating_schema` - Creating the data structure
            - `generating` - Collecting and processing data
            - `done` - Research completed
          examples:
            - done
        matched_records:
          type: integer
          examples:
            - 73
        skipped_records:
          type: integer
          description: >-
            **Note:** `skipped_records` indicates entities that didn't match
            filter criteria
          examples:
            - 27
        pages_read:
          type: integer
          examples:
            - 892
        pages_considered:
          type: integer
          examples:
            - 3421
        total_cost:
          type: string
          description: >-
            **Note:** `total_cost` shows current cost (for running requests,
            this reflects collected records so far)
          examples:
            - $73.00
        columns:
          type: array
          items:
            type: object
            required:
              - name
              - description
              - type
            properties:
              name:
                type: string
              description:
                type: string
              type:
                type: string
                enum:
                  - enrichment
                  - constraint
          examples:
            - - name: company_name
                description: Company name
                type: enrichment
        data:
          type: array
          items:
            type: object
          examples:
            - - company_name: Run:ai
                website: run.ai
                founding_date: '2018'
                employee_count: 120
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