> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get the statuses of all data snapshots

> Use the Bright Data Marketplace Archive API to get statuses of all Data Snapshots. Manages web archive snapshots; returns 200 OK with JSON job status.



## OpenAPI

````yaml api-reference/web-archive-api GET /webarchive/dumps
openapi: 3.1.0
info:
  title: BrightData Web Archive API
  version: 1.0.0
  description: API to search and retrieve archived web pages.
servers:
  - url: https://api.brightdata.com
security:
  - bearerAuth: []
paths:
  /webarchive/dumps:
    get:
      summary: Get all data snapshot statuses
      description: Retrieve the status and metadata of all data snapshots (dumps).
      responses:
        '200':
          description: List of data snapshot statuses
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/DumpStatus'
              examples:
                MixedDumpStatuses:
                  summary: List containing multiple dump statuses
                  value:
                    - dump_id: ucd_abc123-1234567890
                      id: ucd_abc123-1234567890
                      status: done
                      created: '2026-02-05T07:57:50.947Z'
                      done: '2026-02-05T08:21:55.245Z'
                      readiness: 100.00%
                      search_id: ucd_xyz789
                      filters:
                        max_age: 2h
                        min_date: '2026-02-05T05:00:00.000Z'
                      batches_total: 1
                      batches_uploaded: 1
                      files_total: 10
                      files_uploaded: 10
                    - dump_id: ucd_def456-9876543210
                      id: ucd_def456-9876543210
                      status: in_progress
                      created: '2026-02-04T13:35:54.607Z'
                      readiness: 50.00%
                      search_id: ucd_qwe321
                      filters:
                        max_age: 1d
                        domain_whitelist:
                          - example.com
                      batches_total: 10
                      batches_uploaded: 5
                      files_total: 1000
                      files_uploaded: 500
        '401':
          description: Unauthorized
        '500':
          description: Internal server error
components:
  schemas:
    DumpStatus:
      oneOf:
        - $ref: '#/components/schemas/DumpStatusInProgress'
          title: In Progress
        - $ref: '#/components/schemas/DumpStatusDone'
          title: Finished
        - $ref: '#/components/schemas/DumpStatusFailed'
          title: Failed
    DumpStatusInProgress:
      allOf:
        - $ref: '#/components/schemas/DumpStatusBase'
        - required:
            - readiness
            - batches_total
            - batches_uploaded
            - files_total
            - files_uploaded
          properties:
            status:
              type: string
              enum:
                - in_progress
              description: Current status of the dump
            readiness:
              type: string
              description: Percentage of completion (e.g., "22.31%")
            batches_total:
              type: integer
              description: Total number of batches to process
            batches_uploaded:
              type: integer
              description: Number of batches uploaded so far
            files_total:
              type: integer
              description: Total number of files in the dump
            files_uploaded:
              type: integer
              description: Number of files uploaded so far
    DumpStatusDone:
      allOf:
        - $ref: '#/components/schemas/DumpStatusBase'
        - required:
            - status
            - done
            - readiness
            - batches_total
            - batches_uploaded
            - files_total
            - files_uploaded
          properties:
            status:
              type: string
              enum:
                - done
              description: Current status of the dump
            done:
              type: string
              format: date-time
              description: Timestamp when the dump completed
            readiness:
              type: string
              example: 100.00%
              description: Percentage of completion (e.g., "100.00%")
            batches_total:
              type: integer
              description: Total number of batches processed
            batches_uploaded:
              type: integer
              description: Number of batches uploaded
            files_total:
              type: integer
              description: Total number of files in the dump
            files_uploaded:
              type: integer
              description: Number of files uploaded
    DumpStatusFailed:
      allOf:
        - $ref: '#/components/schemas/DumpStatusBase'
        - required:
            - error
          properties:
            status:
              type: string
              enum:
                - failed
              description: Current status of the dump
            error:
              type: string
              description: Error message (only present when status is failed)
    DumpStatusBase:
      type: object
      required:
        - dump_id
        - id
        - status
        - created
        - search_id
      properties:
        dump_id:
          type: string
          description: Unique identifier for the dump
        id:
          type: string
          description: Same as dump_id (included for compatibility)
        status:
          type: string
          enum:
            - in_progress
            - done
            - failed
            - canceled
          description: Current status of the dump
        created:
          type: string
          format: date-time
          description: Timestamp when the dump was created
        search_id:
          type: string
          description: ID of the search this dump is based on
        filters:
          type: object
          description: Filters used to create the dump (present in list endpoint)
          additionalProperties: true
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