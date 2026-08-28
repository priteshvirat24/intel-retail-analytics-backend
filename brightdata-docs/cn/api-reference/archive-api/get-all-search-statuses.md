> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 获取所有搜索状态

> 使用 Bright Data Archive API 获取所有搜索状态。GET /webarchive/searches 返回 200 OK，包含每次搜索的 JSON 状态。热存储保留期为 24 小时。

<Info>
  从 **2026 年 3 月 26 日**开始，热存储保留期从 48 小时更改为 24 小时。
</Info>


## OpenAPI

````yaml api-reference/web-archive-api GET /webarchive/searches
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
  /webarchive/searches:
    get:
      summary: Get all search statuses
      description: Retrieve the status and metadata of all current web archive searches.
      responses:
        '200':
          description: List of search statuses
          content:
            application/json:
              schema:
                type: array
                items:
                  oneOf:
                    - $ref: '#/components/schemas/SearchStatusPending'
                      title: Pending
                    - $ref: '#/components/schemas/SearchStatusSuccess'
                      title: Success
                    - $ref: '#/components/schemas/SearchStatusFailed'
                      title: Failed
              examples:
                MixedStatuses:
                  summary: List containing multiple search statuses
                  value:
                    - search_id: ucd_abc123xyz
                      status: in_progress
                    - search_id: ucd_def456xyz
                      status: done
                      filters:
                        max_age: 1d
                        domain_whitelist:
                          - example.com
                        min_date: '2026-02-05T11:00:00.000Z'
                      files_count: 2885
                      estimate_batch_count: 1
                      estimate_batch_size: 1132300
                      dump_cost_usd: 0.58
                      cost_breakdown:
                        archive_pages_count: 0
                        archive_pages_cost: 0
                        cache_pages_count: 2885
                        cache_pages_cost: 0.58
                      estimate_dump_duration_sec: 38
                      duration: 2s425ms
                    - search_id: ucd_ghi789xyz
                      status: failed
                      error: Path regex filter caused non-retryable error
        '401':
          description: Unauthorized
          content:
            application/json:
              example: Unauthorized
        '500':
          description: Internal server error
          content:
            application/json:
              example: Internal server error
components:
  schemas:
    SearchStatusPending:
      allOf:
        - $ref: '#/components/schemas/SearchStatusBase'
        - properties:
            status:
              type: string
              enum:
                - in_progress
    SearchStatusSuccess:
      allOf:
        - $ref: '#/components/schemas/SearchStatusBase'
        - required:
            - filters
            - files_count
            - estimate_batch_count
            - estimate_batch_size
            - dump_cost_usd
            - cost_breakdown
            - estimate_dump_duration_sec
            - duration
          properties:
            status:
              type: string
              enum:
                - done
            filters:
              type: object
              description: Filters used for the search (echoed back)
              additionalProperties: true
            files_count:
              type: integer
              description: Total number of matching files found
            estimate_batch_count:
              type: integer
              description: Estimated number of batches for the dump
            estimate_batch_size:
              type: integer
              description: Estimated total size in bytes
            dump_cost_usd:
              type: number
              format: float
              description: Estimated total cost to create a dump
            cost_breakdown:
              type: object
              required:
                - archive_pages_count
                - archive_pages_cost
                - cache_pages_count
                - cache_pages_cost
              properties:
                archive_pages_count:
                  type: integer
                archive_pages_cost:
                  type: number
                  format: float
                cache_pages_count:
                  type: integer
                cache_pages_cost:
                  type: number
                  format: float
            estimate_dump_duration_sec:
              type: integer
              description: Estimated time to complete the dump in seconds
            duration:
              type: string
              description: How long the search took to complete
    SearchStatusFailed:
      allOf:
        - $ref: '#/components/schemas/SearchStatusBase'
        - required:
            - error
          properties:
            status:
              type: string
              enum:
                - failed
            error:
              type: string
              description: Error message explaining the failure
    SearchStatusBase:
      type: object
      required:
        - search_id
        - status
      properties:
        search_id:
          type: string
          description: Unique identifier for the search
        status:
          type: string
          enum:
            - in_progress
            - done
            - failed
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