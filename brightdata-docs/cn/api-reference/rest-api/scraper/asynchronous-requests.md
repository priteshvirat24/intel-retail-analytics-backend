> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 异步请求

> Bright Data Scrapers 使您能够触发数据收集，以实现自动化网页数据提取。

相关指南：[Scrapers 介绍](/datasets/scrapers/scrapers-library/overview)

<a href="https://www.postman.com/bright-data-api/bright-data-api/request/1z189u8/trigger-chatgpt-search-scraping" target="_blank">
  <img height="32" width="128" noZoom={true} src="https://run.pstmn.io/button.svg" />
</a>


## OpenAPI

````yaml api-reference/rest-api/scraper/cn-scraper-rest-api.json POST /datasets/v3/trigger
openapi: 3.1.0
info:
  title: Bright Data Scrapers
  description: 用于自动化网页数据收集与提取的 API，支持多种抓取场景和交付选项
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security:
  - bearerAuth: []
paths:
  /datasets/v3/trigger:
    post:
      description: 根据提供的输入触发网页抓取任务
      parameters:
        - name: dataset_id
          description: >-
            用于触发数据收集的数据集 ID。更多信息请参阅 [数据集
            ID](/cn/api-reference/terminology#dataset-id)。
          in: query
          required: true
          schema:
            type: string
            example: gd_l1vikfnt1wgvvqz95w
        - name: custom_output_fields
          description: >-
            "custom_output_fields" 参数用于筛选响应数据，仅包含指定字段。你可以用管道符 (`|`) 列出所需输出列。


            例如，如果你只希望响应包含 URL 和最后更新时间，可以将参数设置为
            "url|about.updated_on"。这允许你自定义数据输出，仅包含与你需求相关的字段。
          in: query
          required: false
          schema:
            type: string
            example: url|about.updated_on
        - name: type
          in: query
          schema:
            type: string
            enum:
              - discover_new
          description: >-
            设置为 "discover_new" 以触发包含发现阶段的收集。


            启用发现阶段，用于通过搜索、分类或关键词等方式查找新实体或产品。当收集数据时，如果特定目标未知，请使用此选项。它会根据提供的输入发现新信息，而不是使用预定义数据点。
        - name: discover_by
          in: query
          schema:
            type: string
          description: >-
            指定收集过程中发现新数据的方法，可用选项如下：


            - `keyword`：通过关键词发现新实体或产品。例如 "smartphones" - 将触发收集以发现新的智能手机产品或实体。

            - `best_sellers_url`：使用列出畅销商品的 URL 发现新产品。例如
            "https://example.com/best-sellers" - 用于发现网站上的畅销产品。

            - `category_url`：使用列出类别的 URL 发现该类别下的新实体。例如
            "https://example.com/electronics" - 用于发现电子类别下的新产品。

            - `location`：基于位置发现与该位置相关的实体。例如 "New York" - 将触发收集以发现指定位置相关的数据。
        - name: include_errors
          in: query
          schema:
            type: boolean
            example: true
          description: 在结果中包含错误报告。将 "include_errors" 设置为 `true`，可以收到数据收集过程中发生的任何错误的详细报告。
        - name: limit_per_input
          in: query
          schema:
            type: number
            minimum: 1
          description: 限制每个输入的结果数量
        - name: limit_multiple_results
          in: query
          schema:
            type: number
            minimum: 1
          description: 限制总结果数量
        - name: notify
          in: query
          schema:
            type: string
            example: true
          description: 指定数据收集任务完成后是否发送通知。设置为 `true` 时，将向指定的 webhook 发送通知，告知收集状态或完成情况。
        - name: endpoint
          in: query
          schema:
            type: string
            example: https://example.com/webhook
          description: 指定用于数据收集过程的 Webhook URL。
        - name: format
          in: query
          schema:
            type: string
            enum:
              - json
              - ndjson
              - jsonl
              - csv
            example: json
          description: 指定要交付的数据格式
        - name: auth_header
          in: query
          schema:
            type: string
          description: Webhook 交付使用的授权头
        - name: uncompressed_webhook
          in: query
          schema:
            type: boolean
            example: true
          description: 默认情况下，数据将以压缩形式发送。传入 true 可发送未压缩的数据
      requestBody:
        required: true
        description: 你可以使用 JSON 或 CSV 格式提供输入数据。输入指定抓取器所需的 URL 或其他参数。
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TriggerInput'
            example:
              - url: https://www.airbnb.com/rooms/50122531
              - url: https://www.airbnb.com/rooms/50127677
          multipart/form-data:
            schema:
              type: object
              properties:
                data:
                  type: string
                  format: binary
                  description: 包含抓取器所需 URL 或其他输入的 CSV 文件
      responses:
        '200':
          description: 收集任务成功启动
          content:
            application/json:
              schema:
                type: object
                properties:
                  snapshot_id:
                    type: string
                    description: >-
                      Snapshot ID 是特定数据快照的唯一标识符，用于通过 API 触发的数据收集任务获取结果。更多信息请参阅
                      [Snapshot ID](/cn/api-reference/terminology#snapshot-id)。
                    example: s_m4x7enmven8djfqak
        '400':
          description: 错误请求 - 输入参数无效
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: 输入格式无效
        '401':
          description: 未授权 - API 密钥无效或缺失
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: 未授权
components:
  schemas:
    TriggerInput:
      type: array
      description: 包含 URL 或抓取器所需的其他参数对象的数组。具体字段取决于使用的数据集。
      example:
        - url: https://www.airbnb.com/rooms/50122531
        - url: https://www.airbnb.com/rooms/50127677
      items:
        type: object
        additionalProperties:
          description: |-
            属性因数据集要求而异。最常见的是包含 'url' 字段。
             示例: ```[{"url":"https://www.airbnb.com/rooms/50122531"},{"url":"https://www.airbnb.com/rooms/50127677"}]```
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        在 Authorization 头中使用您的 Bright Data API Key 作为 Bearer token。


        **认证方法:**

        1. 从 Bright Data 账户设置获取您的 API Key:
        https://brightdata.com/cp/setting/users

        2. 在请求的 Authorization 头中包含 API Key

        3. 格式: `Authorization: Bearer YOUR_API_KEY`


        **示例:**

        ```

        Authorization: Bearer
        b5648e1096c6442f60a6c4bbbe73f8d2234d3d8324554bd6a7ec8f3f251f07df

        ```


        了解如何获取 Bright Data API Key:
        https://docs.brightdata.com/cn/api-reference/authentication#如何生成新的-api-key？
      bearerFormat: API Key

````