> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 列出所有可用国家的城市（静态网络）

> 获取每个国家静态网络可用城市列表

<Tip>
  将您的 API key 粘贴到授权字段中。要获取 API key，请[创建账号](https://www.bright.cn/?hs_signup=1\&utm_source=docs\&utm_campaign=playground)，并查看[如何生成新的 API key？](/cn/api-reference/authentication#如何生成新的-api-key？)
</Tip>


## OpenAPI

````yaml cn-openapi GET /zone/static/cities
openapi: 3.0.1
info:
  title: Bright Data API
  description: 将 Bright Data API 集成到您的流程中，以实现高端的爬取精度
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security:
  - bearerAuth: []
paths:
  /zone/static/cities:
    get:
      description: 获取每个国家静态网络可用城市列表
      parameters:
        - in: query
          name: country
          description: 国家
          required: true
          schema:
            type: string
        - in: query
          name: pool_ip_type
          description: |-
            网络类型: 

             `dc`: 数据中心, 

             `static_res`: ISP
          required: false
          schema:
            type: string
            default: dc
            enum:
              - dc
              - static_res
      responses:
        '200':
          description: 成功
          content:
            application/json:
              schema:
                type: array
                items:
                  type: string
                example:
                  - us-chicago
                  - us-ashburn
                  - us-siouxfalls
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