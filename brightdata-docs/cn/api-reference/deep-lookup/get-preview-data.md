> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 获取预览数据

> 检索预览结果及元数据。



## OpenAPI

````yaml cn-deep-lookup GET /preview/{id}
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
  /preview/{id}:
    get:
      summary: 获取预览数据
      description: 检索预览结果及元数据。
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
            examples:
              - dld_meu4lhla1lj08i6p30
      responses:
        '200':
          description: 预览详情
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetPreviewResponse'
components:
  schemas:
    GetPreviewResponse:
      type: object
      properties:
        preview_id:
          type: string
          examples:
            - dld_meu4lhla1lj08i6p30
        query:
          type: string
          examples:
            - 查找所有 2020 年后成立且员工超过 50 人的 AI 初创公司
        status:
          type: string
          description: |-
            - `queued` - 请求排队等待处理
            - `running` - 正在生成预览
            - `completed` - 结果已准备好
            - `failed` - 出现错误
          enum:
            - pending
            - processing
            - completed
            - failed
          examples:
            - completed
        sample_data:
          type: array
          items:
            type: object
          examples:
            - company_name: Anthropic
              website: anthropic.com
              founded_year: 2021
              employee_count: 160
        columns:
          type: array
          items:
            type: object
          examples:
            - - company_name: Anthropic
                website: anthropic.com
                founded_year: 2021
                employee_count: 160
        result_limit:
          type: integer
          examples:
            - 10
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