> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 同步请求

> 该端点允许用户高效获取数据，并确保与其应用程序或工作流的无缝集成。

## 工作原理

此同步 API 端点允许用户在发送抓取请求时，实时直接在响应中获取结果，例如在终端或应用程序中，无需外部存储或手动下载。此方式通过消除额外的结果获取步骤，使数据采集过程更加高效。

你可以使用 `format` 参数指定所需的输出格式。如果未提供格式，响应将默认使用 JSON。

## 超时限制

请注意，此同步请求受 1 分钟超时限制。如果数据获取过程超过此限制，API 将返回 HTTP 202 响应，表示请求仍在处理中。在这种情况下，你将收到一个快照 ID，可通过“监控快照（Monitor Snapshot）”和“下载快照（Download Snapshot）”端点以异步方式监控并获取结果。

超时情况下的示例响应：

```JSON 202 theme={null}
{
  "snapshot_id": "s_xxx",
  "message": "Your request is still in progress and cannot be retrieved in this call. Use the provided Snapshot ID to track progress via the Monitor Snapshot endpoint and download it once ready via the Download Snapshot endpoint."
}
```


## OpenAPI

````yaml cn-dca-api POST /datasets/v3/scrape
openapi: 3.1.0
info:
  title: Brightdata API
  description: 用于与数据集市场交互的 API
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security:
  - bearerAuth: []
paths:
  /datasets/v3/scrape:
    post:
      summary: 抓取数据并直接在响应中返回。
      description: 该端点允许用户高效获取数据，并确保与其应用程序或工作流的无缝集成。
      parameters:
        - name: dataset_id
          in: query
          description: 触发数据采集的数据集 ID
          required: true
          schema:
            type: string
        - name: custom_output_fields
          description: 输出列列表，用 `|` 分隔（例如：`url|about.updated_on`）。仅包含指定字段的响应。
          in: query
          required: false
          schema:
            type: string
            example: url|about.updated_on
        - name: include_errors
          in: query
          description: 在结果中包含错误报告
          schema:
            type: boolean
        - name: format
          in: query
          description: '指定响应格式（默认: ndjson）'
          schema:
            type: string
            enum:
              - ndjson
              - json
              - csv
            default: json
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ScrapeRequestWithFields'
      responses:
        '200':
          description: 成功
          content:
            text/plain:
              schema:
                type: string
                example: OK
        '202':
          description: 请求仍在处理中，快照将在稍后可用
          headers:
            retry-after:
              description: 再次请求前的秒数
              schema:
                type: integer
                example: 10
          content:
            application/json:
              schema:
                type: object
                properties:
                  snapshot_id:
                    type: string
                  message:
                    type: string
              example:
                snapshot_id: s_xxx
                message: >-
                  您的请求仍在处理中，无法在此调用中检索。请使用提供的 Snapshot ID
                  通过监控快照端点跟踪进度，并在准备好后通过下载快照端点获取数据。
components:
  schemas:
    ScrapeRequestWithFields:
      type: object
      properties:
        input:
          type: array
          items:
            type: object
            properties:
              url:
                type: string
                description: 要抓取的 URL。
            required:
              - url
          description: 要抓取的输入项列表。
        custom_output_fields:
          type: string
          description: 输出列列表，用 `|` 分隔（例如，`url|about.updated_on`）。筛选响应，仅包含指定字段。
          example: url|about.updated_on
      required:
        - input
      example:
        input:
          - url: www.linkedin.com/in/bulentakar
        custom_output_fields: url|about.updated_on
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