> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 可用数据中心和 ISP IP 数量

> 获取可用 IP 数量

<Tip>
  将您的 API key 粘贴到授权字段中。要获取 API key，请[创建账号](https://www.bright.cn/?hs_signup=1\&utm_source=docs\&utm_campaign=playground)，并查看[如何生成新的 API key？](/cn/api-reference/authentication#如何生成新的-api-key？)
</Tip>

<Accordion title="计划示例">
  * 当前区域计划的可用 IP：

  ```sh theme={null}
  curl "https://api.brightdata.com/count_available_ips?zone=ZONE" -H "Authorization: Bearer API_KEY"
  ```

  * 抽象计划，专用 IP：

  ```sh dedicated IPs theme={null}
  curl "https://api.brightdata.com/count_available_ips?plan=\{\"ips_type\":\"dedicated\"\}" -H "Authorization: Bearer API_KEY"
  ```

  * 抽象计划，共享 IP 位于美国：

  ```sh theme={null}
  curl "https://api.brightdata.com/count_available_ips?plan=\{\"country\":\"us\",\"ips_type\":\"shared\"\}" -H "Authorization: Bearer API_KEY"
  ```

  * 抽象计划，专用 IP 位于美国：

  ```sh theme={null}
  curl "https://api.brightdata.com/count_available_ips?plan=\{\"country\":\"us\",\"ips_type\":\"dedicated\"\}" -H "Authorization: Bearer API_KEY"
  ```

  * 抽象计划，共享 IP 位于美国丹佛：

  ```sh theme={null}
  curl "https://api.brightdata.com/count_available_ips?plan=\{\"ips_type\":\"shared\",\"country_city\":\"us-denver\",\"city\":true\}" -H "Authorization: Bearer API_KEY"
  ```

  * 抽象计划，共享 IP 位于美国，仅限特定域：amazon.com, fb.com：

  ```sh theme={null}
  curl "https://api.brightdata.com/count_available_ips?plan=\{\"ips_type\":\"selective\",\"country\":\"us\",\"domain_whitelist\":\"amazon.com%20fb.com\"\}" -H "Authorization: Bearer API_KEY"
  ```

  * 抽象计划，共享 IP 位于美国，地理 IP 数据库：同时保存在 maxmind 和 dbip：

  ```sh theme={null}
  curl "https://api.brightdata.com/count_available_ips?plan=\{\"ips_type\":\"shared\",\"country\":\"us\",\"geo_db\":\{\"maxmind\":true,\"dbip\":true\}\}" -H "Authorization: Bearer API_KEY"
  ```
</Accordion>


## OpenAPI

````yaml cn-openapi GET /zone/count_available_ips
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
  /zone/count_available_ips:
    get:
      description: 获取可用 IP 数量
      parameters:
        - in: query
          name: zone
          description: 区域名称
          required: false
          schema:
            type: string
        - in: query
          name: plan
          required: false
          schema:
            type: object
            properties:
              pool_ip_type:
                type: string
                description: 若想获取 ISP IP 的可用数量，默认值为数据中心对等 IP。
                default: static_res
              ips_type:
                type: string
                description: |-
                  IP 类型

                  `shared`: 共享

                  `selective`: 选择性

                  `dedicated`: 专用
              country:
                type: string
                description: IP 所在国家
              country_city:
                type: string
                description: 定义 IP 所在城市
              city:
                type: boolean
                description: 与 `country_city` 参数一起使用
              domain_whitelist:
                type: string
                description: |-
                  以空格分隔的域名列表

                  **注意**: curl 请求中空格需 URL 编码：`d1.com%20d2.com`
              geo_db:
                type: object
                description: 启用/禁用 IP 位置数据库
                properties:
                  maxmind:
                    type: boolean
                    default: true
                    description: 使用 MaxMind IP 位置数据库
                  dbip:
                    type: boolean
                    default: true
                    description: 使用 DB-IP IP 位置数据库
                  google:
                    type: boolean
                    default: true
                    description: 使用 Google IP 位置数据库
                  ip2location:
                    type: boolean
                    default: true
                    description: 使用 IP2Location IP 位置数据库
                  ipcn:
                    type: boolean
                    default: true
                    description: 使用 ip.cn IP 位置数据库
      responses:
        '200':
          description: 成功
          content:
            application/json:
              schema:
                type: object
                example:
                  count: 1234
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