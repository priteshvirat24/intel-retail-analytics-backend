> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 获取快照

> 获取已触发采集的列表，该列表仅包含为特定数据集创建的快照



## OpenAPI

````yaml cn-dca-api get /datasets/v3/snapshots
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
  /datasets/v3/snapshots:
    get:
      description: 获取已触发采集的列表，该列表仅包含为特定数据集创建的快照
      parameters:
        - name: dataset_id
          in: query
          description: 数据集标识符（可在具体 API 页面找到）
          required: true
          schema:
            type: string
          example: gd_l1vikfnt1wgvvqz95w
        - name: status
          in: query
          description: 仅列出具有特定状态的快照
          required: false
          schema:
            type: string
            enum:
              - starting
              - running
              - ready
              - failed
          example: ready
        - name: skip
          in: query
          description: 跳过前 `x` 个快照
          required: false
          schema:
            type: integer
            default: 0
          example: 0
        - name: limit
          in: query
          description: 限制返回的快照数量
          required: false
          schema:
            type: integer
            default: 1000
            maximum: 5000
          example: 0
        - name: from_date
          in: query
          description: 仅列出在特定日期之后创建的快照
          required: false
          schema:
            type: string
            format: date
          example: '2024-01-01'
        - name: to_date
          in: query
          description: 仅列出在特定日期之前创建的快照
          required: false
          schema:
            type: string
            format: date
          example: '2024-04-01'
        - name: with_total
          in: query
          description: 如果包含此参数，则返回快照总数
          required: false
          schema:
            type: boolean
        - name: trigger_type
          in: query
          description: 按类型筛选快照
          required: false
          schema:
            type: string
            enum:
              - ALL
              - CP
              - API
          example: ALL
      responses:
        '200':
          description: 成功
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: string
                      description: 触发 API 返回的快照 ID
                    created:
                      type: string
                      format: date-time
                      description: 请求采集的时间
                    status:
                      type: string
                      enum:
                        - starting
                        - running
                        - ready
                        - failed
                      description: 采集状态
                    dataset_id:
                      type: string
                      description: 触发采集的数据集 ID
                    dataset_size:
                      type: integer
                      description: 收集的记录数量
                    trigger:
                      type: object
                      properties:
                        type:
                          type: string
                          description: 快照创建方式，CP（无代码）或 API
components:
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