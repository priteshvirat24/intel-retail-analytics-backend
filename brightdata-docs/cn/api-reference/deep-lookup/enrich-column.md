> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 丰富列

> 为现有结果添加额外数据列。



## OpenAPI

````yaml cn-deep-lookup POST /request/{id}/enrich
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
  /request/{id}/enrich:
    post:
      summary: 丰富列
      description: 为现有结果添加额外数据列。
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
            examples:
              - ai_meu3z0171o8k9jc4dh
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  column_name:
                    type: string
                    examples:
                      - cto_name
                  query:
                    type: string
                    examples:
                      - CTO 或工程负责人姓名
      responses:
        '200':
          description: 已触发数据丰富
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EnrichResponse'
components:
  schemas:
    EnrichResponse:
      type: object
      properties:
        column_name:
          type: string
          examples:
            - cto_name
        status:
          type: string
          description: |-
            - `processing` - 正在丰富数据
            - `completed` - 数据丰富完成
          enum:
            - processing
            - completed
          examples:
            - processing
        max_additional_cost:
          type: string
          description: '**注意:** `max_additional_cost` 显示可能的最高费用，最终费用仅基于匹配的记录计算'
          examples:
            - $3.65
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