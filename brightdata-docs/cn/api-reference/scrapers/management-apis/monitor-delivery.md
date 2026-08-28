> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 监控交付

> 该调用返回交付状态



## OpenAPI

````yaml cn-dca-api get /datasets/v3/delivery/{delivery_id}
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
  /datasets/v3/delivery/{delivery_id}:
    get:
      description: 该调用返回交付状态
      parameters:
        - name: delivery_id
          in: path
          description: 从交付 API 端点返回的唯一交付 ID
          required: true
          schema:
            type: string
          example: d_lysxl9vf2dobrb6h31
      responses:
        '200':
          description: 成功
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                  delivery_files:
                    type: array
                    description: 已交付文件列表
                    items:
                      type: object
                      properties:
                        filename:
                          type: string
                        delivery_ts:
                          type: integer
                  status:
                    type: string
                    enum:
                      - done
                      - canceled
                      - failed
                    description: 交付状态
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