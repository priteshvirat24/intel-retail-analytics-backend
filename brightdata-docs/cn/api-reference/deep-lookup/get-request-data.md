> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 获取请求数据

> 检索研究的完整结果。



## OpenAPI

````yaml cn-deep-lookup GET /request/{id}
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
  /request/{id}:
    get:
      summary: 获取请求数据
      description: 检索研究的完整结果。
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
          description: 请求数据
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RequestDataResponse'
components:
  schemas:
    RequestDataResponse:
      type: object
      properties:
        request_id:
          type: string
          examples:
            - ai_meu3z0171o8k9jc4dh
        query:
          type: string
          examples:
            - 查找以色列的所有 AI 初创公司
        status:
          type: string
          examples:
            - completed
        title:
          type: string
          examples:
            - 以色列的 AI 初创公司
        step:
          type: string
          description: |-
            - `identifying` - 理解并分析查询
            - `generating_schema` - 创建数据结构
            - `generating` - 收集并处理数据
            - `done` - 研究完成
          examples:
            - done
        matched_records:
          type: integer
          examples:
            - 73
        skipped_records:
          type: integer
          description: '**注意:** `skipped_records` 表示未匹配筛选条件的实体'
          examples:
            - 27
        pages_read:
          type: integer
          examples:
            - 892
        pages_considered:
          type: integer
          examples:
            - 3421
        total_cost:
          type: string
          description: '**注意:** `total_cost` 显示当前费用（对于进行中的请求，此值反映迄今收集的记录）'
          examples:
            - $73.00
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
            - - name: company_name
                description: 公司名称
                type: enrichment
        data:
          type: array
          items:
            type: object
          examples:
            - - company_name: Run:ai
                website: run.ai
                founding_date: '2018'
                employee_count: 120
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