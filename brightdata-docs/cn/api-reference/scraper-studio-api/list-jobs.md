> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 列出 Scraper Studio 作业

> 使用 GET /dca/collector/jobs 获取账户中的 Scraper Studio 作业。可按爬虫 ID 和日期范围过滤，并使用 offset 和 limit 分页。

使用 `GET /dca/collector/jobs` 获取您账户中的 Bright Data Scraper Studio 作业。可按爬虫 ID 和日期范围过滤列表，并使用 `offset` 和 `limit` 控制分页。

`from_date` 和 `to_date` 为必填项。使用较窄的日期范围可获得更快的响应并更便于分页。

<Note>
  将爬虫 ID 作为 `collector` 参数传入，仅返回该爬虫的作业。爬虫 ID 可从[列出爬虫](./list-scrapers)获取。
</Note>

## 过滤、分页和排序

* **按爬虫过滤。** 将爬虫 ID 作为 `collector` 参数传入，仅返回该爬虫的作业。ID 可从[列出爬虫](./list-scrapers)获取。
* **分页。** 使用 `offset` 和 `limit` 分页浏览作业。要获取下一页，请将 `offset` 增加上一页的 `limit` 值，例如 `offset=0&limit=100`，然后 `offset=100&limit=100`。`limit` 必须介于 0 和 500 之间。
* **排序。** 使用 `sort_asc=1` 表示升序，`sort_asc=-1` 表示降序。默认值为 `-1`。

## 何时使用该端点

* 构建一个按日期范围列出某个爬虫近期作业的仪表盘
* 审计作业历史，并根据 `inputs`、`data_lines` 和 `failed_pages` 计算成功率
* 查找作业 ID，然后通过[作业数据](./job-data)获取每个作业的元数据
* 通过关注 `failed_pages` 发现需要处理的爬虫

## 错误

| 状态                 | 原因                              | 修复方法                                                   |
| ------------------ | ------------------------------- | ------------------------------------------------------ |
| `400 Bad Request`  | `from_date` 或 `to_date` 缺失或格式错误 | 以 `YYYY-MM-DD` 格式发送这两个日期                               |
| `401 Unauthorized` | 令牌缺失、格式错误或已吊销                   | 从[账户设置 → API 令牌](https://www.bright.cn/cp/setting)重新复制 |
| `5xx`              | Bright Data API 临时错误            | 使用指数退避重试，例如 1s、2s、4s                                   |

## 相关

* [列出爬虫](./list-scrapers)：查找作为 `collector` 参数传入的爬虫 `id`
* [作业数据](./job-data)：单个作业的作业级元数据
* [接收批量数据](./Receive_batch_data)：下载作业产生的记录
* [异步触发批量采集](./Trigger_a_scraper_for_batch_collection_method)：创建作业的端点


## OpenAPI

````yaml api-reference/web-scraper-ide-rest-api GET /dca/collector/jobs
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
  /dca/collector/jobs:
    get:
      summary: List Scraper Studio jobs
      description: >-
        Retrieve a paginated list of Bright Data Scraper Studio jobs for your
        account. `from_date` and `to_date` are required. Filter by scraper ID
        with `collector`, and paginate with `offset` and `limit`.
      parameters:
        - name: from_date
          in: query
          required: true
          schema:
            type: string
            format: date
            example: '2026-06-01'
          description: Start date for the jobs list, in YYYY-MM-DD format.
        - name: to_date
          in: query
          required: true
          schema:
            type: string
            format: date
            example: '2026-07-13'
          description: End date for the jobs list, in YYYY-MM-DD format.
        - name: collector
          in: query
          required: false
          schema:
            type: string
            example: c_example1234567890
          description: >-
            Scraper ID used to filter jobs for a specific scraper. Get IDs from
            the List Scrapers endpoint.
        - name: offset
          in: query
          required: false
          schema:
            type: integer
            default: 0
          description: >-
            Number of jobs to skip before returning results. Used for
            pagination.
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            default: 50
            minimum: 0
            maximum: 500
          description: Maximum number of jobs to return. Must be between 0 and 500.
        - name: sort_asc
          in: query
          required: false
          schema:
            type: integer
            default: -1
            enum:
              - 1
              - -1
          description: >-
            Sort direction. Use 1 for ascending order or -1 for descending
            order.
      responses:
        '200':
          description: A paginated list of Scraper Studio jobs.
          content:
            application/json:
              schema:
                type: object
                properties:
                  total:
                    type: integer
                    description: Total number of jobs matching the request.
                  offset:
                    type: integer
                    description: Zero-based index of the first job returned.
                  limit:
                    type: integer
                    description: Maximum number of jobs returned in the response.
                  data:
                    type: array
                    description: List of job objects.
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          description: Job ID.
                        status:
                          type: string
                          description: >-
                            Current job status, such as running, done, failed or
                            canceled.
                        queued:
                          type: string
                          description: >-
                            Timestamp when the job entered the queue, in ISO
                            8601 format.
                        started:
                          type: string
                          description: Timestamp when the job started, in ISO 8601 format.
                        finished:
                          type: string
                          description: >-
                            Timestamp when the job finished, in ISO 8601 format.
                            Present only for completed jobs.
                        inputs:
                          type: integer
                          description: Number of input rows submitted to the job.
                        page_loads:
                          type: integer
                          description: Number of page loads used by the job.
                        total_pages:
                          type: integer
                          description: >-
                            Total number of pages discovered or processed by the
                            job.
                        failed_pages:
                          type: integer
                          description: Number of pages that failed during the job.
                        data_lines:
                          type: integer
                          description: Number of output records produced by the job.
                        trigger:
                          type: object
                          description: Information about how the job was triggered.
                          properties:
                            type:
                              type: string
                              description: >-
                                Trigger source, such as CP for the control
                                panel.
                            user:
                              type: string
                              description: User or system that triggered the job.
                            ip:
                              type: string
                              description: IP address associated with the trigger request.
                        expired:
                          type: string
                          description: >-
                            Timestamp when the job data expires and is no longer
                            available, in ISO 8601 format.
              examples:
                response:
                  value:
                    total: 3
                    offset: 0
                    limit: 50
                    data:
                      - id: j_example1234567890
                        status: done
                        queued: '2026-07-02T12:21:04.121Z'
                        started: '2026-07-02T12:21:04.387Z'
                        finished: '2026-07-02T12:21:09.566Z'
                        inputs: 1
                        page_loads: 1
                        total_pages: 1
                        failed_pages: 0
                        data_lines: 50
                        trigger:
                          type: CP
                          user: user@example.com
                          ip: 192.0.2.10
                        expired: '2026-07-19T00:00:00.000Z'
                      - id: j_example0987654321
                        status: done
                        queued: '2026-07-02T12:14:17.941Z'
                        started: '2026-07-02T12:14:18.098Z'
                        finished: '2026-07-02T12:14:25.122Z'
                        inputs: 1
                        page_loads: 1
                        total_pages: 1
                        failed_pages: 0
                        data_lines: 50
                        trigger:
                          type: CP
                          user: user@example.com
                          ip: 192.0.2.10
                        expired: '2026-07-19T00:00:00.000Z'
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