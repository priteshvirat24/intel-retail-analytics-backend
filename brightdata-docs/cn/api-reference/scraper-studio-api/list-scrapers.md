> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 列出 Scraper Studio 爬虫

> 使用 GET /dca/collectors_list 获取账户中的 Scraper Studio 爬虫，包含每个爬虫的 ID、名称、活动状态、投递配置和输出模式。

使用 `GET /dca/collectors_list` 获取您账户中可用的 Bright Data Scraper Studio 爬虫。响应包含爬虫 ID、名称、活动状态、投递配置、最近运行时间，以及可用时的输出模式。

<Note>
  使用该端点发现账户中的爬虫 `id` 值，然后在[触发爬虫](./Trigger_a_scraper_for_batch_collection_method)时将某个 `id` 作为 `collector` 参数传入。
</Note>

## 搜索爬虫

使用 `search` 查询参数，仅返回名称与搜索词匹配的爬虫，例如 `?search=amazon`。省略 `search` 则返回账户中的所有爬虫。

## 何时使用该端点

* 在触发批量或实时作业前查找爬虫的 `id`
* 构建一个列出账户中所有爬虫的选择器
* 审计哪些爬虫处于 `active` 状态以及哪些已运行过（`last_run`）
* 读取 `output_schema`，在解析记录前映射返回的字段

## 错误

| 状态                 | 原因                   | 修复方法                                                   |
| ------------------ | -------------------- | ------------------------------------------------------ |
| `401 Unauthorized` | 令牌缺失、格式错误或已吊销        | 从[账户设置 → API 令牌](https://www.bright.cn/cp/setting)重新复制 |
| `5xx`              | Bright Data API 临时错误 | 使用指数退避重试，例如 1s、2s、4s                                   |

## 相关

* [列出作业](./list-jobs)：列出某个爬虫运行过的作业
* [异步触发批量采集](./Trigger_a_scraper_for_batch_collection_method)：将爬虫 `id` 作为 `collector` 参数传入
* [作业数据](./job-data)：已触发爬虫的作业级元数据
* [接收批量数据](./Receive_batch_data)：下载爬虫产生的记录


## OpenAPI

````yaml api-reference/web-scraper-ide-rest-api GET /dca/collectors_list
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
  /dca/collectors_list:
    get:
      summary: List Scraper Studio scrapers
      description: >-
        Retrieve the Bright Data Scraper Studio scrapers in your account. Each
        scraper is returned with its ID, name, active status, delivery
        configuration and output schema. Use the returned `id` as the
        `collector` parameter when triggering a scraper.
      parameters:
        - name: search
          in: query
          required: false
          schema:
            type: string
            example: amazon
          description: Filters the scraper list by the provided search term.
      responses:
        '200':
          description: A paginated list of Scraper Studio scrapers.
          content:
            application/json:
              schema:
                type: object
                properties:
                  total:
                    type: integer
                    description: Total number of scrapers matching the request.
                  offset:
                    type: integer
                    description: Zero-based index of the first scraper returned.
                  limit:
                    type: integer
                    description: Maximum number of scrapers returned in the response.
                  data:
                    type: array
                    description: List of scraper objects.
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          description: >-
                            Scraper ID. Use this value as the collector
                            parameter when triggering a scraper.
                        name:
                          type: string
                          description: Scraper name shown in Scraper Studio.
                        active:
                          type: boolean
                          description: >-
                            Indicates whether the scraper is active and
                            available for production runs.
                        last_run:
                          type: string
                          description: >-
                            Timestamp of the latest run, in ISO 8601 format.
                            Present when the scraper has run before.
                        deliver:
                          type: object
                          description: Delivery configuration for the scraper.
                          properties:
                            type:
                              type: string
                              description: Delivery type, such as api_pull.
                        output_schema:
                          type:
                            - object
                            - 'null'
                          description: >-
                            Output schema configured for the scraper. Can be
                            null if no output schema is available.
                          properties:
                            type:
                              type: string
                              description: Schema root type, usually object.
                            fields:
                              type: object
                              description: >-
                                Field definitions returned by the scraper, keyed
                                by field name.
                              additionalProperties:
                                type: object
                                properties:
                                  type:
                                    type: string
                                    description: >-
                                      Field type, such as text, number, price,
                                      url, array, input, error or warning.
                                  active:
                                    type: boolean
                                    description: >-
                                      Indicates whether the field is active in
                                      the scraper output.
                                  items:
                                    type: object
                                    description: Item definition for array fields.
              examples:
                response:
                  value:
                    total: 5
                    offset: 0
                    limit: 50
                    data:
                      - id: c_example1234567890
                        name: example.com
                        active: false
                        deliver:
                          type: api_pull
                        output_schema: null
                      - id: c_example0987654321
                        name: example.com
                        active: true
                        last_run: '2026-06-22T11:41:56.660Z'
                        deliver:
                          type: api_pull
                        output_schema:
                          type: object
                          fields:
                            product_title:
                              type: text
                              active: true
                            brand:
                              type: text
                              active: true
                            rating:
                              type: number
                              active: true
                            image_urls:
                              type: array
                              active: true
                              items:
                                type: url
                            input:
                              type: input
                              active: true
                            warning:
                              type: warning
                              active: true
                            error:
                              type: error
                              active: true
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