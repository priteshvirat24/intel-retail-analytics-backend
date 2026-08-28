> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Trigger async real-time scrape

> Trigger an async real-time Scraper Studio scrape. POST /dca/trigger_immediate returns a response_id to fetch the result from the Real-time data endpoint.

<Note>
  This endpoint does not return the scrape data. It returns a `response_id`. Use that `response_id` with the [Realtime Data endpoint](/api-reference/scraper-studio-api/Receive_data_from_real_time_work_scraper) to retrieve the result when the scrape is complete.
</Note>


## OpenAPI

````yaml api-reference/web-scraper-ide-rest-api POST /dca/trigger_immediate
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
  /dca/trigger_immediate:
    post:
      description: >-
        Trigger an asynchronous real-time run of a Scraper Studio collector.


        The endpoint returns immediately with a `response_id`. Use this
        `response_id` with the [Realtime Data
        endpoint](/api-reference/scraper-studio-api/Receive_data_from_real_time_work_scraper)
        to retrieve the result when the scrape is complete.


        Use this endpoint when you want to start a real-time scrape without
        keeping the original HTTP request open while the scraper runs. For a
        request that waits and returns the result directly, use the [synchronous
        real-time
        endpoint](/api-reference/scraper-studio-api/initiate-a-realtime-job/sync-realtime-job).
      parameters:
        - name: collector
          in: query
          required: true
          schema:
            type: string
            example: COLLECTOR_ID
          description: A unique identification of the collector to run
        - name: version
          in: query
          schema:
            type: string
          description: Set to `dev` to trigger the development version of the scraper
      requestBody:
        required: true
        description: >-
          A single input object. The fields must match the input schema defined
          for the collector. Some collectors take `url`, others take fields such
          as `keyword`, `location` or `state`.
        content:
          application/json:
            schema:
              type: object
              additionalProperties: true
              description: >-
                Single input object whose fields match the collector input
                schema.
              properties:
                url:
                  type: string
                  format: uri
                  description: >-
                    Example field for collectors that take a target URL. Replace
                    with the fields your collector expects.
            examples:
              request:
                value:
                  url: https://targetwebsite.com/product_id/
      responses:
        '200':
          description: >-
            Returns immediately with a `response_id`. Use this ID with the
            [Realtime Data
            endpoint](/api-reference/scraper-studio-api/Receive_data_from_real_time_work_scraper)
            to retrieve the result.
          content:
            application/json:
              schema:
                type: object
                properties:
                  response_id:
                    type: string
                    description: >-
                      ID of the asynchronous real-time job. Use this value to
                      retrieve the result from the Realtime Data endpoint.
              examples:
                response:
                  value:
                    response_id: d2t1786372370082rjv3f11k9v18
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