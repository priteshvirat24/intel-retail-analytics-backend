> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 解锁网站

> Bright Data Web Unlocker API 可帮助您绕过反机器人措施、管理代理，并自动解决 CAPTCHA，让网页数据采集更加轻松。

相关指南：[Web Unlocker API Introduction](/cn/scraping-automation/web-unlocker/introduction)

<a href="https://www.postman.com/bright-data-api/bright-data-api/request/f0g939o/unlock-website" target="_blank">
  <img height="32" width="128" noZoom src="https://run.pstmn.io/button.svg" />
</a>

<Card title="Bright Data Python SDK" icon="python" href="/cn/api-reference/SDK" cta="Get Started">
  要快速开始使用我们的工具，请查看我们的新 Python SDK。
</Card>


## OpenAPI

````yaml cn-unlocker-rest-api POST /request
openapi: 3.0.1
info:
  title: Brightdata API
  description: 将 Bright Data API 集成到您的数据管道中，确保高精度抓取
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security:
  - bearerAuth: []
paths:
  /request:
    post:
      parameters:
        - in: query
          name: async
          description: 设置为 `true` 以进行异步请求
          required: false
          schema:
            type: boolean
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PostBody'
      responses:
        '200':
          description: 成功
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTP200'
        '400':
          description: 请求错误
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTP400'
        '401':
          description: 未授权
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTP401'
components:
  schemas:
    PostBody:
      required:
        - zone
        - url
        - format
      type: object
      properties:
        zone:
          description: |-
            定义您的 Bright Data 产品配置的区域标识符。每个区域包含目标规则、输出偏好和访问权限。
            管理区域：https://brightdata.com/cp/zones
          type: string
          example: web_unlocker1
        url:
          description: 要抓取的完整目标 URL，必须包含协议 (http/https) 并可公开访问。
          type: string
          example: https://example.com/page
        format:
          description: 响应格式：`raw` 返回 HTML 内容字符串，`json` 返回结构化数据。
          type: string
          enum:
            - raw
            - json
          example: json
        method:
          description: 通过代理请求 HTML 的方法为 `GET`。
          type: string
          default: GET
          example: GET
        country:
          description: >-
            代理所在国家的两字母 ISO 3166-1 代码（例如 `us`, `gb`, `de`, `ca`,
            `au`）。如果未指定，系统会根据区域配置自动选择最佳位置。

            国家代码列表：https://docs.brightdata.com/cn/general/faqs#where-can-i-see-the-list-of-country-codes
          type: string
          example: us
        data_format:
          description: >-
            额外响应格式转换：`markdown` 将 HTML 内容转换为干净的 markdown 格式，`screenshot` 捕获渲染页面的
            PNG 图片。
          type: string
          enum:
            - markdown
            - screenshot
          example: markdown
        render:
          description: >-
            设为 `true` 可强制使用浏览器进行 JavaScript
            渲染。由于该标志会强制使用浏览器，可能会显著增加响应时间，因此仅在页面需要 JavaScript 才能加载内容时使用。
          type: string
          enum:
            - 'true'
            - 'false'
          example: 'true'
    HTTP200:
      type: string
      example: 成功
    HTTP400:
      type: string
      example: 请求错误
    HTTP401:
      type: string
      example: 需要用户身份验证
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