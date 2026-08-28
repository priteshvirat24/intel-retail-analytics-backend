> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 允许/拒绝域名

> 向区域允许列表或拒绝列表添加域名

<Warning> **警告:** 此 API 可能会修改您的账户设置、影响操作或产生费用。</Warning>

<Tip>
  将您的 API 密钥粘贴到授权字段。要获取 API 密钥，请[创建账户](https://www.bright.cn/?hs_signup=1\&utm_source=docs\&utm_campaign=playground)，并了解[如何生成新的 API 密钥](/cn/api-reference/authentication#how-do-i-generate-a-new-api-key%3F)
</Tip>


## OpenAPI

````yaml cn-openapi POST /zone/domain_perm
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
  /zone/domain_perm:
    post:
      description: 向区域允许列表或拒绝列表添加域名
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ZoneAndDomain'
      responses:
        '201':
          description: 成功
components:
  schemas:
    ZoneAndDomain:
      required:
        - zone
        - type
      type: object
      properties:
        zone:
          description: 区域名称
          type: string
        type:
          description: '`whitelist` 为允许列表域名，`blacklist` 为拒绝列表域名'
          type: string
          enum:
            - whitelist
            - blacklist
        domain:
          description: 空格分隔的域名列表
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