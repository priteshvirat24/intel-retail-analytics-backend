> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Trigger Self-Healing

> Use the Bright Data Scraper Studio AI Flow API to trigger self-healing. Returns 200 OK with AI scraper template or job progress data as JSON.



## OpenAPI

````yaml api-reference/web-scraper-ide-rest-api POST /dca/collectors/{collector_id}/refactor_template
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
  /dca/collectors/{collector_id}/refactor_template:
    post:
      summary: Trigger Self-Healing
      description: Triggers the self-healing tool to refactor the scraper template.
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
              $ref: '#/components/schemas/RefactorTemplateRequest'
      responses:
        '200':
          description: Self-healing triggered
components:
  schemas:
    RefactorTemplateRequest:
      type: object
      required:
        - prompt
      properties:
        prompt:
          type: string
          description: '> Maximum string length: 1000'
          example: Fix selector issues
        custom_input:
          type: array
          items:
            type: object
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