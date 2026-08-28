> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get snapshots

> Use Bright Data Web Scraper API management endpoints to get Snapshots. GET /datasets/v3/snapshots returns snapshot or job status as JSON.



## OpenAPI

````yaml api-reference/dca-api get /datasets/v3/snapshots
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
  /datasets/v3/snapshots:
    get:
      description: >-
        Get a list of triggered collections, the list contains only snapshots
        created for a specific dataset
      parameters:
        - name: dataset_id
          in: query
          description: The dataset identifier (can be found in the specific API page)
          required: true
          schema:
            type: string
          example: gd_l1vikfnt1wgvvqz95w
        - name: status
          in: query
          description: List only snapshots with a specific status
          required: false
          schema:
            type: string
            enum:
              - starting
              - running
              - ready
              - failed
              - canceled
          example: ready
        - name: skip
          in: query
          description: Skip the first `x` snapshots
          required: false
          schema:
            type: integer
            default: 0
          example: 0
        - name: limit
          in: query
          description: Limit the number of snapshots to return
          required: false
          schema:
            type: integer
            default: 1000
            maximum: 5000
          example: 0
        - name: from_date
          in: query
          description: List only snapshots that were created after a specific date
          required: false
          schema:
            type: string
            format: date
          example: '2024-01-01'
        - name: to_date
          in: query
          description: List only snapshots that were created before a specific date
          required: false
          schema:
            type: string
            format: date
          example: '2024-04-01'
        - name: with_total
          in: query
          description: Returns the total number of snapshots if this parameter is included
          required: false
          schema:
            type: boolean
        - name: trigger_type
          in: query
          description: Filter snapshots by type
          required: false
          schema:
            type: string
            enum:
              - ALL
              - CP
              - API
          example: ALL
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: string
                      description: Snapshot ID returned by trigger API
                    created:
                      type: string
                      format: date-time
                      description: When the collection was requested
                    status:
                      type: string
                      enum:
                        - starting
                        - running
                        - ready
                        - failed
                        - canceled
                      description: Status of the collection
                    dataset_id:
                      type: string
                      description: ID of the dataset for which collection was triggered
                    dataset_size:
                      type: integer
                      description: Amount of records collected
                    trigger:
                      type: object
                      properties:
                        type:
                          type: string
                          description: Snapshot creation method, CP(no code) or API
              examples:
                collection_status:
                  value:
                    - id: <string>
                      created: '2023-11-07T05:31:56Z'
                      status: running
                      dataset_id: <string>
                      dataset_size: 123
                      trigger:
                        type: <string>
        '404':
          description: Snapshot not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: Error message when snapshot is not found
              examples:
                not_found:
                  value:
                    error: Snapshot not found
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