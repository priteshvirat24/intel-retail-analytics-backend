> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 获取快照元数据

> 获取数据集快照元数据



## OpenAPI

````yaml cn-dca-api GET /datasets/snapshots/{id}
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
  /datasets/snapshots/{id}:
    get:
      description: 获取数据集快照元数据
      parameters:
        - in: path
          name: id
          description: >-
            快照 ID 是特定数据快照的唯一标识符，用于通过 API 触发的数据采集任务中获取结果。更多信息请参阅 [Snapshot
            ID](/cn/api-reference/terminology#snapshot-id)。
          required: true
          schema:
            type: string
            example: snap_m2bxug4e2o352v1jv1
      responses:
        '200':
          description: 成功
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DatasetSnapshotMeta'
        '404':
          description: 未找到快照
          content:
            text/html:
              schema:
                type: string
                example: 未找到快照
components:
  schemas:
    DatasetSnapshotMeta:
      type: object
      properties:
        id:
          type: string
        created:
          type: string
          format: date-time
        status:
          type: string
          enum:
            - 已安排
            - 构建中
            - 就绪
            - 失败
        dataset_id:
          type: string
        customer_id:
          type: string
        dataset_size:
          type: integer
          description: 快照中的记录数量
        file_size:
          type: integer
          description: 快照文件的字节大小
        cost:
          type: number
        error:
          type: string
        error_code:
          type: string
        warning:
          type: string
        warning_code:
          type: string
        initiation_type:
          type: string
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