> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 触发完整请求

> 根据预览或详细规格执行完整研究。

<Note>
  `steps` 数组包含详细的处理阶段信息，但通常仅用于内部调试。
</Note>


## OpenAPI

````yaml cn-deep-lookup POST /trigger
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
  /trigger:
    post:
      summary: 触发完整请求
      description: 根据预览或详细规格执行完整研究。
      requestBody:
        required: true
        content:
          application/json:
            schema:
              oneOf:
                - $ref: '#/components/schemas/TriggerFromPreview'
                - $ref: '#/components/schemas/DirectTriggerWithSpecifications'
      responses:
        '200':
          description: 研究请求已成功触发
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TriggerResponse'
components:
  schemas:
    TriggerFromPreview:
      type: array
      items:
        type: object
        required:
          - preview_id
        properties:
          preview_id:
            type: string
            description: 要触发的预览请求 ID
            examples:
              - dld_meu4lhla1lj08i6p30
          result_limit:
            type: integer
            description: 限制返回结果的数量
            examples:
              - 100
    DirectTriggerWithSpecifications:
      type: array
      items:
        type: object
        required:
          - query
          - spec
        properties:
          query:
            type: string
            description: 研究的高级查询
            examples:
              - 查找以色列的所有 AI 初创公司
          spec:
            type: object
            required:
              - name
              - query
              - title
              - columns
            properties:
              name:
                type: string
                examples:
                  - companies
              query:
                type: string
                examples:
                  - 查找在以色列开发 AI 产品的所有初创公司
              title:
                type: string
                examples:
                  - 以色列的 AI 初创公司
              columns:
                type: array
                items:
                  type: object
                  required:
                    - name
                    - description
                    - type
                  properties:
                    name:
                      type: string
                    description:
                      type: string
                    type:
                      type: string
                      enum:
                        - enrichment
                        - constraint
                examples:
                  - name: founding_date
                    description: 公司的成立日期
                    type: enrichment
                  - name: is_startup_check
                    description: 公司必须是初创公司（早期公司，通常为私人持有，最近成立）
                    type: constraint
                  - name: employee_count
                    description: 员工数量
                    type: enrichment
          result_limit:
            type: integer
            description: 限制返回结果的数量
            examples:
              - 50
    TriggerResponse:
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
          enum:
            - queued
            - running
          examples:
            - queued
        max_cost:
          type: string
          example: $50.00
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