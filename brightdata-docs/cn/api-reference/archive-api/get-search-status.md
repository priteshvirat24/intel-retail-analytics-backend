> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 获取搜索状态

> 使用 Bright Data Archive API 获取搜索状态。GET /webarchive/search/{search_id} 返回 200 OK，包含匹配文件数、快照大小和预估费用。

当成功时，它将检索：

* 您查询的条目数量
* 完整数据快照的估计大小和成本

<Note>
  **定价和大小：** `estimate_batch_size` 以字节为单位。`dump_cost_usd` 是基于 `files_count` 和您当前缓存/存档定价层的估计总成本。`cost_breakdown` 对象显示缓存和存档页面的单独成本。
</Note>


## OpenAPI

````yaml api-reference/web-archive-api GET /webarchive/search/{search_id}
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
  /webarchive/search/{search_id}:
    get:
      summary: Get search status
      description: >-
        Check the status and results of a previously submitted web archive
        search query.
      parameters:
        - name: search_id
          in: path
          required: true
          description: Unique identifier for the search
          schema:
            type: string
            example: ucd_abc123xyz
      responses:
        '200':
          description: Search status response
          content:
            application/json:
              schema:
                oneOf:
                  - title: Success
                    type: object
                    properties:
                      search_id:
                        type: string
                        description: Unique identifier for the search
                      status:
                        type: string
                        description: 'Current status: `in_progress`, `done`, or `failed`'
                        enum:
                          - done
                      filters:
                        type: object
                        description: The filters used for this search (echoed back)
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
                        description: Breakdown of costs between cache and archive pages
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
                      error:
                        type: string
                        description: Error message (only present when status is `failed`)
                    example:
                      search_id: ucd_abc123xyz
                      status: done
                      filters:
                        domain_whitelist:
                          - example.com
                          - www.example.com
                        max_age: 1d
                        min_date: '2026-02-05T10:00:00.000Z'
                      files_count: 12341294
                      estimate_batch_count: 130
                      estimate_batch_size: 1073679195
                      dump_cost_usd: 2468.26
                      cost_breakdown:
                        archive_pages_count: 0
                        archive_pages_cost: 0
                        cache_pages_count: 12341294
                        cache_pages_cost: 2468.26
                      estimate_dump_duration_sec: 13000
                      duration: 4s210ms
                  - title: Pending
                    type: object
                    properties:
                      search_id:
                        type: string
                        description: Unique identifier for the search
                        example: ucd_abc123xyz
                      status:
                        type: string
                        description: 'Current status: `in_progress`, `done`, or `failed`'
                        enum:
                          - in_progress
                    example:
                      search_id: ucd_abc123xyz
                      status: in_progress
                  - title: Failed
                    type: object
                    properties:
                      search_id:
                        type: string
                        description: Unique identifier for the search
                        example: ucd_abc123xyz
                      status:
                        type: string
                        description: 'Current status: `in_progress`, `done`, or `failed`'
                        enum:
                          - failed
                      error:
                        type: string
                        description: Error message explaining the failure
                        example: Path regex filter caused non-retryable error
                    example:
                      search_id: ucd_abc123xyz
                      status: failed
                      error: Path regex filter caused non-retryable error
              examples:
                Pending:
                  summary: Search is still running
                  value:
                    search_id: ucd_abc123xyz
                    status: in_progress
                Success:
                  summary: Search completed successfully
                  value:
                    search_id: ucd_abc123xyz
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
                Failed:
                  summary: Search failed
                  value:
                    search_id: ucd_abc123xyz
                    status: failed
                    error: Path regex filter caused non-retryable error
        '401':
          description: Unauthorized
          content:
            application/json:
              example: Unauthorized
        '404':
          description: Search ID not found
          content:
            application/json:
              example: Search ID not found
        '500':
          description: Internal server error
          content:
            application/json:
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