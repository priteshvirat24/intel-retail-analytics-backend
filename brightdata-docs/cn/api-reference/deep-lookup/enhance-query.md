> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 优化查询

> 根据额外要求优化您的研究查询。



## OpenAPI

````yaml cn-deep-lookup POST /enhance_query
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
  /enhance_query:
    post:
      summary: 优化查询
      description: 根据额外要求优化您的研究查询。
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                required:
                  - query
                properties:
                  query:
                    type: string
                    examples:
                      - 查找所有 AI 初创公司
      responses:
        '200':
          description: 查询优化成功
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EnhanceQueryResponse'
components:
  schemas:
    EnhanceQueryResponse:
      type: object
      properties:
        enhanced_query:
          type: string
          examples:
            - 查找在美国的所有 AI 初创公司，这些公司已获得 A 轮及以上融资，总部位于主要科技中心
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