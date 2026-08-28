> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 刷新专用住宅 IP

> 刷新区域的静态 IP

<Warning> **警告：** 此 API 可能会修改您的账户设置、影响您的业务操作或产生费用。</Warning>

<Tip>
  将您的 API key 粘贴到授权字段中。要获取 API key，请[创建账号](https://www.bright.cn/?hs_signup=1\&utm_source=docs\&utm_campaign=playground)，并查看[如何生成新的 API key？](/cn/api-reference/authentication#如何生成新的-api-key？)
</Tip>

<Warning>
  每次刷新每个专用住宅 IP 的费用为 \$0.02/次/IP
</Warning>


## OpenAPI

````yaml cn-openapi POST /zone/ips/refresh
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
  /zone/ips/refresh:
    post:
      description: 刷新区域的静态 IP
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - zone
              properties:
                zone:
                  type: string
                  description: 区域名称
                  example: zone1
                vips:
                  type: array
                  description: |-
                    要刷新的 VIP 

                     **注意**：若需刷新所有已分配的 IP，请省略 `vips` 参数。

                     **注意**：仅适用于专用住宅 IP
                  items:
                    type: string
                  example:
                    - vip1
                    - vip2
                ips:
                  type: array
                  description: |-
                    要刷新的 IP 

                     **注意**：若需刷新所有已分配的 IP，请省略 `ips` 参数
                  items:
                    type: string
                  example:
                    - ip1
                    - ip2
                country:
                  type: string
                  description: 新 IP 的国家（例如 `us`）
                country_city:
                  type: string
                  description: 新 IP 的城市（例如 `us-chicago`）
      responses:
        '200':
          description: 成功
          content:
            application/json:
              schema:
                type: object
                example:
                  vips:
                    - vip: tr_9121_07_antalya_10
                      country: tr
                    - vip: tr_9121_07_antalya_17
                      country: tr
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