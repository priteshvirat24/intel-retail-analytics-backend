> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 获取请求状态

> 检查研究请求的当前状态。



## OpenAPI

````yaml cn-deep-lookup GET /request/{id}/status
openapi: 3.1.0
info:
  title: Bright Data 深度查询 API
  description: |-
    Bright Data 深度查询 API 允许您预览、优化并执行研究查询。
    支持数据丰富、取消操作以及多种格式的结果导出。
  version: 1.0.0
servers:
  - url: https://api.brightdata.com/datasets/deep_lookup/v1
security:
  - bearerAuth: []
paths:
  /request/{id}/status:
    get:
      summary: 获取请求状态
      description: 检查研究请求的当前状态。
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
            examples:
              - ai_meu3z0171o8k9jc4dh
      responses:
        '200':
          description: 请求状态
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RequestStatusResponse'
components:
  schemas:
    RequestStatusResponse:
      type: object
      properties:
        request_id:
          type: string
          examples:
            - ai_meu3z0171o8k9jc4dh
        status:
          type: string
          description: |-
            - `queued` - 请求排队等待处理
            - `running` - 研究进行中
            - `completed` - 结果已准备好
            - `failed` - 出现错误
            - `cancelled` - 请求已取消
          enum:
            - queued
            - running
            - completed
            - failed
            - cancelled
          examples:
            - running
        progress:
          type: integer
          description: 进度百分比 (0-100)
          examples:
            - 65
        pages_read:
          type: integer
          examples:
            - 342
        pages_considered:
          type: integer
          examples:
            - 1250
        matched_records:
          type: integer
          examples:
            - 31
        is_trial:
          type: boolean
          examples:
            - false
        result_limit:
          type: integer
          examples:
            - 50
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