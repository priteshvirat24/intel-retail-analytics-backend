> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 允许列表 IP

> 将 IP 添加到区域白名单

<Warning> **警告：** 此 API 可能会修改您的账户设置、影响您的业务操作或产生费用。</Warning>

<Tip>
  将您的 API key 粘贴到授权字段中。要获取 API key，请[创建账号](https://www.bright.cn/?hs_signup=1\&utm_source=docs\&utm_campaign=playground)，并查看[如何生成新的 API key？](/cn/api-reference/authentication#如何生成新的-api-key？)
</Tip>


## OpenAPI

````yaml cn-openapi POST /zone/whitelist
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
  /zone/whitelist:
    post:
      description: 将 IP 添加到区域白名单
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ZoneAndIP'
      responses:
        '201':
          description: 成功
components:
  schemas:
    ZoneAndIP:
      required:
        - ip
      type: object
      properties:
        zone:
          description: 区域名称，可省略以影响所有区域
          type: string
        ip:
          description: |-
            `string` 或 `array of strings` 

             单个 IP、IP 数组、IP 范围、IP 子网或 IP 掩码  

             ### 示例 

             - 单个 IP: 10.20.30.40 

             - IP 数组: ["10.20.30.40", "50.60.70.80",...] 

             - 范围: 10.20.30.40-10.20.30.50 

             - 子网: 10.20.30.0/24 

             - 子网掩码: 10.20.30.0/255.255.252.0 

             **注意** IP 数组语法要求数组中每个 IP 字符串使用引号 `"`
          oneOf:
            - type: string
            - type: array
              items:
                type: string
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