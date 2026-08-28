> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# IDE 作业数据 API



## OpenAPI

````yaml api-reference/web-scraper-ide-rest-api GET /dca/log/{job_id}
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
  /dca/log/{job_id}:
    get:
      description: Get job data by job ID
      parameters:
        - name: job_id
          in: path
          required: true
          schema:
            type: string
          description: The ID of the job to retrieve.
      responses:
        '200':
          description: OK
          content:
            application/json:
              examples:
                response:
                  value:
                    id: j_ma13y9ay1piehrso8r
                    status: done
                    collector: c_m9im5n7v82p2y35la
                    template: t_m9jty150kxgwtzcgi.3
                    inputs: 1
                    dup_inputs: 0
                    lines: 60
                    fails: 0
                    pages: 1
                    pages_left: 0
                    success: 1
                    navigations: 2
                    created: '2025-04-28T13:22:16.857Z'
                    started: '2025-04-28T13:22:17.502Z'
                    finished: '2025-04-28T13:23:28.961Z'
                    trigger: user@example.com
                    success_rate: 1
                    job_time: 71459
                    queue_time: 645
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