> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Rerun snapshot

> Use Bright Data Web Scraper API management endpoints to rerun Snapshot. POST /datasets/v3/snapshot/{id}/rerun returns snapshot or job status as JSON.



## OpenAPI

````yaml api-reference/dca-api post /datasets/v3/snapshot/{snapshot_id}/rerun
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
  /datasets/v3/snapshot/{snapshot_id}/rerun:
    post:
      description: Rerun previously created snapshot
      parameters:
        - name: snapshot_id
          in: path
          required: true
          schema:
            type: string
            example: s_m4x7enmven8djfqak
            description: The ID of previously triggered collection
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                properties:
                  snapshot_id:
                    type: string
        '400':
          description: Snapshots input is expired
          content:
            text/html:
              schema:
                type: string
                example: Snapshot's inputs storage is expired and no longer available
        '404':
          description: Snapshot not found
          content:
            text/html:
              schema:
                type: string
                example: snapshot not found
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

        Authorization: Bearer YOUR_API_KEY

        ```


        Learn how to get your Bright Data API key:
        https://docs.brightdata.com/api-reference/authentication
      bearerFormat: API Key

````