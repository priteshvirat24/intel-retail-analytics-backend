> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 每个区域可用的数据中心 & ISP IP

> 获取每个区域可用的数据中心/ISP IP

<Tip>
  将您的 API key 粘贴到授权字段中。要获取 API key，请[创建账号](https://www.bright.cn/?hs_signup=1\&utm_source=docs\&utm_campaign=playground)，并查看[如何生成新的 API key？](/cn/api-reference/authentication#如何生成新的-api-key？)
</Tip>


## OpenAPI

````yaml cn-openapi GET /zone/route_ips
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
  /zone/route_ips:
    get:
      tags:
        - Proxy
      description: 获取每个区域可用的数据中心/ISP IP
      parameters:
        - name: zone
          in: query
          description: 区域
          required: true
          schema:
            type: string
        - name: country
          in: query
          description: 2 字母国家代码
          schema:
            type: string
        - name: list_countries
          in: query
          description: 返回 `[{ip, country},..]` JSON 数组而非纯 IP 列表
          schema:
            type: boolean
      responses:
        '200':
          description: 当 `list_countries=true` 时，返回 JSON 数组；否则返回以换行分隔的 IP 列表
          content:
            application/json:
              schema:
                oneOf:
                  - type: object
                    description: 当 `list_countries=true` 时，返回 JSON 数组
                    properties:
                      ip:
                        type: string
                        description: IP 地址
                        example: 1.1.1.1
                      country:
                        type: string
                        description: 2 字母国家代码
                        example: us
                    example:
                      - ip: 10.0.0.0
                        country: us
                      - ip: 1.1.1.1
                        country: gb
                      - ip: 1.1.2.2
                        country: hk
                  - type: string
                    description: |-
                      当 `list_countries=false` 时，IP 将以换行符分隔的纯列表 

                       ## 示例： 

                       ```
                      1.1.1.1
                      1.1.2.2
                      10.0.0.0
                      ```
                    example: 10.0.0.0/24
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