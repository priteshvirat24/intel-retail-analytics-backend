> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom inputs

> Add custom fields to a Bright Data Web Scraper API input schema (1000+ pre-built scrapers); values you send are returned in each output record for tagging.

## Custom inputs

You can add custom fields to your input schema, and whatever you send in those fields will be **returned in the results** for each record/job. This is useful for:

* **Unified schema**: Keep the same output structure across different scrapers/datasets.
* **Index / reference fields**: Pass an `id`, `row_index`, or any internal key so you can easily match results back to the original input rows.


## OpenAPI

````yaml dca-custom-inputs POST /datasets/v3/scrape
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
  /datasets/v3/scrape:
    post:
      summary: Scrape data and return it directly in the response.
      description: >-
        This endpoint allows users to fetch data efficiently and ensures
        seamless integration with their applications or workflows.
      parameters:
        - name: dataset_id
          in: query
          description: Dataset ID for which data collection is triggered.
          required: true
          schema:
            type: string
        - name: custom_output_fields
          description: >-
            List of output columns, separated by `|` (e.g.,
            `url|about.updated_on`). Filters the response to include only the
            specified fields.
          in: query
          required: false
          schema:
            type: string
            example: url|about.updated_on
        - name: include_errors
          in: query
          description: Include errors report with the results.
          schema:
            type: boolean
        - name: format
          in: query
          description: 'Specifies the format of the response (default: ndjson).'
          schema:
            type: string
            enum:
              - ndjson
              - json
              - csv
            default: json
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ScrapeRequestWithFields'
      responses:
        '200':
          description: OK
          content:
            text/plain:
              schema:
                type: string
                example: OK
        '202':
          description: Request is still in progress, snapshot will be available later.
          headers:
            retry-after:
              description: Time in seconds before retrying the request.
              schema:
                type: integer
                example: 10
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                  message:
                    type: string
              example:
                status: starting
                message: Snapshot is not ready yet, try again in 30s
components:
  schemas:
    ScrapeRequestWithFields:
      type: object
      properties:
        custom_input_fields:
          type: array
          items:
            type: string
            description: >-
              The name of a custom input field to be accepted and returned in
              the results.
          description: >-
            List of custom input field names whose values are passed through and
            returned unchanged in the results for each record.
          example:
            - url
            - prompt
            - index_custom
        input:
          type: array
          items:
            type: object
            properties:
              url:
                type: string
                description: URL to scrape.
            required:
              - url
          description: List of input items to scrape.
          example:
            - url: https://chatgpt.com/
              prompt: Top hotels in New York
              index_custom: abd45424
        custom_output_fields:
          type: string
          description: >-
            List of output columns, separated by `|` (e.g.,
            `url|about.updated_on`). Filters the response to include only the
            specified fields.
          example: url|about.updated_on
      required:
        - input
      example:
        custom_input_fields:
          - url
          - prompt
          - index_custom
        input:
          - url: https://chatgpt.com/
            prompt: Top hotels in New York
            index_custom: abd45424
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