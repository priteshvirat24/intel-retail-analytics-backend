> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get snapshot log

> Get a Bright Data Web Scraper API snapshot log: GET /datasets/v3/log/{id} returns snapshot or job status as JSON. Use Download snapshot for the records.



## OpenAPI

````yaml api-reference/dca-api get /datasets/v3/log/{snapshot_id}
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
  /datasets/v3/log/{snapshot_id}:
    get:
      description: Retrieve the logs for a specific dataset snapshot
      parameters:
        - name: snapshot_id
          in: path
          required: true
          schema:
            type: string
            example: s_mcd3rc6l2md984eoij
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SnapshotDataResponse'
        '404':
          description: Snapshot not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: Snapshot not found
components:
  schemas:
    SnapshotDataResponse:
      type: object
      examples:
        - id: s_mcd3rc6l2md984eoij
          created: '2025-06-26T08:09:32.781Z'
          status: ready
          dataset_name: Apple App Store
          scraper_name: Apple App Store - collect by URL
          dataset_size: 2
          inputs_count: 2
          dataset_id: gd_lsk9ki3u2iishmwrui
          discovery_collector_id: null
          file_size: 65381
          trigger:
            type: CP
            user: user@example.com
            ip: 203.0.113.10
            trigger_url: >-
              /trigger?customer=hl_dacd97fb&type=url_collection&dataset_id=gd_lsk9ki3u2iishmwrui&include_errors=true&discover_only=false
            ts: '2025-06-26T08:09:32.074Z'
          duration: 6
          duration_per_input: 3
          success_rate: 1
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

        Authorization: Bearer YOUR_API_KEY

        ```


        Learn how to get your Bright Data API key:
        https://docs.brightdata.com/api-reference/authentication
      bearerFormat: API Key

````