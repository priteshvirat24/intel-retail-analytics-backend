> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 获取作业错误



## OpenAPI

````yaml api-reference/web-scraper-ide-rest-api GET /dca/jobs/{job_id}/hp_errors
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
  /dca/jobs/{job_id}/hp_errors:
    get:
      summary: Get errors for an job
      description: >-
        Retrieves a list of errors generated during execution of an batch
        scraper job. The job ID must be obtained from the `/trigger_hp`
        endpoint. If the `skip_normalize` query parameter is provided, full
        (non-normalized) error details are returned.
      parameters:
        - name: job_id
          in: path
          required: true
          description: Job ID returned from the `/trigger_hp` endpoint
          schema:
            type: string
        - name: skip_normalize
          in: query
          required: false
          description: Return full (non-normalized) error details
          schema:
            type: boolean
      responses:
        '200':
          description: List of errors for the specified job
          content:
            application/json:
              schema:
                type: object
                properties:
                  errors:
                    type: array
                    items:
                      type: object
                      properties:
                        url:
                          type: string
                          description: URL that failed during processing
                        error:
                          type: string
                          description: Error type or reason
                        consumer:
                          type: string
                          description: Internal consumer identifier
              example:
                errors:
                  - url: www.youtube.com/watch?v=GBaFv4O5H7g
                    error: aborted
                    consumer: dca-hp-so-szakh
                  - url: www.youtube.com/watch?v=dVSRDWxlWBg
                    error: aborted
                    consumer: dca-hp-so-sz5zu
                  - url: www.youtube.com/watch?v=1YrOL8ZqR4Q
                    error: aborted
                    consumer: dca-hp-so-sz6ga
        '400':
          description: Invalid job ID supplied
          content:
            text/plain:
              schema:
                type: string
                example: Invalid job ID supplied
        '404':
          description: Job not found
          content:
            text/plain:
              schema:
                type: string
                example: Job not found
        '500':
          description: Internal server error
          content:
            text/plain:
              schema:
                type: string
                example: Internal server error
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