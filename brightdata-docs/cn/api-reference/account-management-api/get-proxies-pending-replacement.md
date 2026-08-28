> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 获取待更换代理

> 获取指定区域中所有待替换的代理列表



## OpenAPI

````yaml cn-openapi GET /zone/proxies_pending_replacement
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
  /zone/proxies_pending_replacement:
    get:
      tags:
        - Proxy
      description: 获取指定区域中所有待替换的代理列表
      parameters:
        - name: zone
          in: query
          description: 区域
          schema:
            type: string
      responses:
        '200':
          description: 每个区域待替换 IP 的 JSON 列表
          content:
            application/json:
              schema:
                type: object
                properties:
                  ZoneName:
                    type: object
                    properties:
                      type:
                        type: string
                        example: zone1
                      ips_to_replace:
                        type: integer
                        example: 1
                      ips_list:
                        type: array
                        items:
                          type: object
                          properties:
                            due_date:
                              type: string
                              format: date
                            ips:
                              type: array
                              items:
                                type: object
                                properties:
                                  ip:
                                    type: string
                                    format: ipv4
                                  country:
                                    type: string
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