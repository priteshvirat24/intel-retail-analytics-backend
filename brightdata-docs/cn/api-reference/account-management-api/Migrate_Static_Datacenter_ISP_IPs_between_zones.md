> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 在区域之间迁移静态 IP

> 在区域之间迁移静态 IP（数据中心/ISP）

<Warning> **警告：** 此 API 可能会修改您的账户设置、影响您的业务操作或产生费用。</Warning>

<Tip>
  将您的 API key 粘贴到授权字段中。要获取 API key，请[创建账号](https://www.bright.cn/?hs_signup=1\&utm_source=docs\&utm_campaign=playground)，并查看[如何生成新的 API key？](/cn/api-reference/authentication#如何生成新的-api-key？)
</Tip>


## OpenAPI

````yaml cn-openapi POST /zone/ips/migrate
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
  /zone/ips/migrate:
    post:
      description: 在区域之间迁移静态 IP（数据中心/ISP）
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - from
                - to
                - ips
              properties:
                from:
                  type: string
                  description: IP 将从该区域迁出
                  example: zone1
                to:
                  type: string
                  description: IP 将迁入的区域
                  example: zone2
                ips:
                  type: array
                  description: 要迁移的 IP 列表
                  example:
                    - 1.1.1.1
                    - 2.1.1.5
                    - 3.1.1.100
      responses:
        '200':
          description: 成功
          content:
            application/json:
              schema:
                type: object
                example:
                  from: zone1
                  to: zone2
                  count: 3
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