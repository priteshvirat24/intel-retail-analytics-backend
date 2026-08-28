> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 获取所有采集器

> 获取您账户中所有可用采集器的列表。每个采集器都由一个数据集 ID 和一个显示名称标识。将返回的 `id` 用作触发和管理端点中的 `dataset_id` 参数。



## OpenAPI

````yaml cn-dca-api get /datasets/v3/scrapers
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
  /datasets/v3/scrapers:
    get:
      description: >-
        获取您账户中所有可用采集器的列表。每个采集器都由一个数据集 ID 和一个显示名称标识。将返回的 `id` 用作触发和管理端点中的
        `dataset_id` 参数。
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: string
                      description: 采集器的数据集 ID，用作触发和管理端点中的 `dataset_id` 参数
                    name:
                      type: string
                      description: 采集器的可读名称
              examples:
                scrapers:
                  value:
                    - id: gd_mq5dtosp2eq0rjny2e
                      name: Ergobaby Products
                    - id: gd_mq5hrug82ex2tzuad
                      name: Primally Pure Products
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