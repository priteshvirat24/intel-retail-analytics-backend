> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 取消请求

> 取消正在进行中的研究请求。



## OpenAPI

````yaml cn-deep-lookup POST /request/{id}/cancel
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
  /request/{id}/cancel:
    post:
      summary: 取消请求
      description: 取消正在进行中的研究请求。
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
          description: 请求已取消
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CancelResponse'
components:
  schemas:
    CancelResponse:
      type: object
      properties:
        request_id:
          type: string
          examples:
            - ai_meu3z0171o8k9jc4dh
        status:
          type: string
          examples:
            - cancelled
        records_processed:
          type: integer
          examples:
            - 45
        charge:
          type: string
          examples:
            - $45.00
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