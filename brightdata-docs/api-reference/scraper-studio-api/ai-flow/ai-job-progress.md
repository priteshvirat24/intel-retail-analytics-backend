> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# AI job progress

> Use the Bright Data Scraper Studio AI Flow API to get AI job progress. Returns 200 OK with AI scraper template or job progress data as JSON.



## OpenAPI

````yaml api-reference/web-scraper-ide-rest-api GET /dca/collectors/{collector_id}/automate_template/progress
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
  /dca/collectors/{collector_id}/automate_template/progress:
    get:
      summary: Get AI Job Progress
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
      responses:
        '200':
          description: AI job progress status
          content:
            application/json:
              example:
                step: collector_maintainer
                completed_steps:
                  - prepare_intent_analyzer
                  - planner
                  - collector_maintainer
                  - output_schema_generator
                  - code_generator
                  - input_schema_generator
                  - preview_runner
                  - preview_picker
                status: done
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

        Authorization: Bearer
        b5648e1096c6442f60a6c4bbbe73f8d2234d3d8324554bd6a7ec8f3f251f07df

        ```


        Learn how to get your Bright Data API key:
        https://docs.brightdata.com/api-reference/authentication
      bearerFormat: API Key

````