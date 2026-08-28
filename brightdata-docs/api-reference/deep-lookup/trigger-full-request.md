> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Trigger full request

> Use the Bright Data Deep Lookup API to trigger Full Request. POST /trigger returns enriched records as JSON with 200 OK on success.

<Note>
  The `steps` array with detailed processing stages is available but typically used for internal debugging.
</Note>


## OpenAPI

````yaml api-reference/deep-lookup POST /trigger
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
  /trigger:
    post:
      summary: Trigger Full Request
      description: >-
        Execute the full research based on preview or with detailed
        specifications.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              oneOf:
                - $ref: '#/components/schemas/TriggerFromPreview'
                - $ref: '#/components/schemas/DirectTriggerWithSpecifications'
      responses:
        '200':
          description: Research triggered successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TriggerResponse'
components:
  schemas:
    TriggerFromPreview:
      type: array
      items:
        type: object
        required:
          - preview_id
        properties:
          preview_id:
            type: string
            description: ID of the preview request to trigger
            examples:
              - dld_meu4lhla1lj08i6p30
          result_limit:
            type: integer
            description: Limit the number of results returned
            examples:
              - 100
    DirectTriggerWithSpecifications:
      type: array
      items:
        type: object
        required:
          - query
          - spec
        properties:
          query:
            type: string
            description: High-level query for the research
            examples:
              - Find all AI startups in Israel
          spec:
            type: object
            required:
              - name
              - query
              - title
              - columns
            properties:
              name:
                type: string
                examples:
                  - companies
              query:
                type: string
                examples:
                  - Find all startups developing AI products in Israel
              title:
                type: string
                examples:
                  - AI startups in Israel
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
                  - name: founding_date
                    description: Founding date of the company
                    type: enrichment
                  - name: is_startup_check
                    description: >-
                      Company must be a startup (early-stage company, typically
                      privately held and recently founded)
                    type: constraint
                  - name: employee_count
                    description: Number of employees
                    type: enrichment
          result_limit:
            type: integer
            description: Limit the number of results returned
            examples:
              - 50
    TriggerResponse:
      type: object
      properties:
        request_id:
          type: string
          examples:
            - ai_meu3z0171o8k9jc4dh
        status:
          type: string
          description: |-
            - `queued` - Request is waiting to be processed
            - `running` - Research in progress
          enum:
            - queued
            - running
          examples:
            - queued
        max_cost:
          type: string
          example: $50.00
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