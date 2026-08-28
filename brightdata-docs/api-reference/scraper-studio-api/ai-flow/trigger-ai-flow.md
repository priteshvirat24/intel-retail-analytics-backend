> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Trigger AI Flow

> Use the Bright Data Scraper Studio AI Flow API to trigger AI Flow. Returns 200 OK with AI scraper template or job progress data as JSON.



## OpenAPI

````yaml api-reference/web-scraper-ide-rest-api POST /dca/collectors/{collector_id}/automate_template
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
  /dca/collectors/{collector_id}/automate_template:
    post:
      summary: Trigger AI Flow
      description: Triggers AI flow to generate working scraper code.
      parameters:
        - name: collector_id
          in: path
          description: >-
            Collector ID returned by the [Create Scraper
            Template](/api-reference/scraper-studio-api/ai-flow/create-scraper-template)
            API endpoint.
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AutomateTemplateRequest'
      responses:
        '200':
          description: AI flow triggered
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    description: Unique identifier for the AI job
                  queued:
                    type: boolean
                    description: Indicates whether the job is queued or currently running
              example:
                id: ia_mnvfxano29hv58t24o
                queued: false
components:
  schemas:
    AutomateTemplateRequest:
      type: object
      required:
        - description
        - urls
      properties:
        description:
          type: string
          maxLength: 500
          example: Extract product data from this page
        urls:
          type: array
          maxItems: 1
          items:
            type: string
            format: uri
            example: https://example.com
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