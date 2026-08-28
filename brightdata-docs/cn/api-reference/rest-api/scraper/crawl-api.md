> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 爬取 API

> Bright Data Scrapers 使您能够触发采集以实现自动化网页数据提取。

相关指南： [爬取 API 简介](/cn/scraping-automation/crawl-api/overview)


## OpenAPI

````yaml api-reference/rest-api/scraper/cn-crawl-rest-api.json POST /datasets/v3/trigger
openapi: 3.1.0
info:
  title: Bright Data Scrapers
  description: 用于自动化网页数据收集与提取的 API，支持多种抓取场景与数据传输选项。
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security:
  - bearerAuth: []
paths:
  /datasets/v3/trigger:
    post:
      description: 根据提供的输入触发一次网页抓取任务。
      parameters:
        - name: dataset_id
          description: 您的 dataset ID。
          in: query
          required: true
          schema:
            type: string
            example: gd_m6gjtfmeh43we6cqc
        - name: include_errors
          in: query
          schema:
            type: boolean
            example: true
          description: 在结果中包含错误报告。若将 "include_errors" 设置为 `true`，您将收到有关数据收集过程中发生的所有错误的详细报告。
        - name: custom_output_fields
          description: >-
            "custom_output_fields" 参数用于筛选响应数据，仅返回指定字段。您可以使用竖线 (`|`) 分隔所需的输出列。


            例如，如果您只想在响应中包含 URL 和上次更新日期，可以将参数设置为
            "url|about.updated_on"。这允许您根据需求自定义返回的数据字段。
          in: query
          required: false
          schema:
            type: string
            example: url|about.updated_on
      requestBody:
        required: true
        description: 您可以使用 JSON 或 CSV 格式提供输入数据。输入内容指定抓取器所需的 URL 或其他参数。
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
                  description: 包含 URL 或抓取器所需其他输入项的 CSV 文件。
      responses:
        '200':
          description: 任务已成功启动。
          content:
            application/json:
              schema:
                type: object
                properties:
                  snapshot_id:
                    type: string
                    description: >-
                      Snapshot ID 是用于识别特定数据快照的唯一标识符，可用于获取通过 API
                      触发的抓取任务的结果。了解更多：[Snapshot
                      ID](/cn/api-reference/terminology#snapshot-id)。
                    example: s_m4x7enmven8djfqak
        '400':
          description: 错误请求 — 输入参数无效。
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: Invalid input format
        '401':
          description: 未授权 — API key 无效或缺失。
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: Unauthorized
components:
  schemas:
    TriggerInput:
      type: array
      description: 一个对象数组，包含抓取器所需的 URL 或其他参数。具体字段取决于所使用的 dataset。
      example:
        - url: https://www.airbnb.com/rooms/50122531
        - url: https://www.airbnb.com/rooms/50127677
      items:
        type: object
        additionalProperties:
          description: |-
            属性依据 dataset 的需求而变化。最常见的是 'url' 字段。
             示例：```[{"url":"https://www.airbnb.com/rooms/50122531"},{"url":"https://www.airbnb.com/rooms/50127677"}]```
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