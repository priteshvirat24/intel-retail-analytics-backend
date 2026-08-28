> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 按分类划分的域名

> 返回所选分类下的每个域名的使用数据



## OpenAPI

````yaml cn-scraping-shield-rest-api GET /shield/domains_by_class
openapi: 3.1.0
info:
  title: Bright Data API
  description: 用于与数据集市场交互的 API
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security:
  - bearerAuth: []
paths:
  /shield/domains_by_class:
    get:
      description: 返回所选分类下的每个域名的使用数据
      parameters:
        - name: from
          in: query
          schema:
            type: string
          description: 请求数据的开始时间范围。例如：`from=2018-07-01T00:00:00`
        - name: to
          in: query
          schema:
            type: string
          description: 请求数据的结束时间范围。例如：`to=2018-07-02T00:00:00`
        - name: cn
          in: query
          schema:
            type: string
          description: 请求来源国家。例如：`cn=uk`
        - name: peer_cn
          in: query
          schema:
            type: string
          description: 对端 IP 的国家。例如：`peer_cn=us`
        - name: categories
          in: query
          schema:
            type: string
          description: 仅返回特定分类。例如：`categories=ads`
        - name: order_by
          in: query
          schema:
            type: string
          description: 按带宽/请求数排序结果。`order_by=bw` 或 `order_by=req`
        - name: order
          in: query
          schema:
            type: string
          description: 按大小升序/降序排序。`order=asc` 或 `order=desc`
      responses:
        '200':
          description: OK
          content:
            application/json:
              examples:
                response:
                  value:
                    - domain: static.addtoany.com
                      req: 16370
                      bw: 200590537
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