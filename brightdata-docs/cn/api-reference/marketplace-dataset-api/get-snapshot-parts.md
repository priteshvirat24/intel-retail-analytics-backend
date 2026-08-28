> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 获取快照部分

> 获取数据集快照传输部分。此处使用的所有查询参数需要与下载快照时使用的参数匹配，以获取准确的部分



## OpenAPI

````yaml cn-dca-api GET /datasets/snapshots/{id}/parts
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
  /datasets/snapshots/{id}/parts:
    get:
      description: 获取数据集快照传输部分。此处使用的所有查询参数需要与下载快照时使用的参数匹配，以获取准确的部分
      parameters:
        - in: path
          name: id
          description: >-
            快照 ID 是特定数据快照的唯一标识符，用于通过 API 触发的数据采集任务中获取结果。更多信息请参阅 [Snapshot
            ID](/cn/api-reference/terminology#snapshot-id)。
          required: true
          schema:
            type: string
            example: s_m4x7enmven8djfqak
        - in: query
          name: format
          description: 响应格式
          schema:
            type: string
            enum:
              - json
              - ndjson
              - jsonl
              - csv
            default: json
        - in: query
          name: compress
          description: 响应是否使用 gzip 格式压缩
          schema:
            type: boolean
            default: false
        - in: query
          name: batch_size
          description: 每个响应批次中包含的记录数量
          schema:
            type: integer
            minimum: 1000
      responses:
        '200':
          description: 成功
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DatasetSnapshotParts'
        '400':
          description: 快照未准备好
          content:
            text/html:
              schema:
                type: string
                example: 快照未准备好
        '404':
          description: 未找到快照
          content:
            text/html:
              schema:
                type: string
                example: 未找到快照
components:
  schemas:
    DatasetSnapshotParts:
      type: object
      properties:
        parts:
          type: number
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