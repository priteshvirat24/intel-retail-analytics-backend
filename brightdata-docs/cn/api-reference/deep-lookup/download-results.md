> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 下载结果

> 以 JSON、CSV 或 Excel 导出结果。

<Card title="查询参数">
  <ParamField query="format" type="string" default="json">
    输出格式: `json` (默认), `csv`, `excel`
  </ParamField>
</Card>

```bash theme={null}
curl -X GET "https://api.brightdata.com/deep-lookup/v1/request/ai_meu3z0171o8k9jc4dh/download?format=csv" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -o results.csv
```


## OpenAPI

````yaml cn-deep-lookup GET /request/{id}/download
openapi: 3.1.0
info:
  title: Bright Data 深度查询 API
  description: |-
    Bright Data 深度查询 API 允许您预览、优化并执行研究查询。
    支持数据丰富、取消操作以及多种格式的结果导出。
  version: 1.0.0
servers:
  - url: https://api.brightdata.com/datasets/deep_lookup/v1
security:
  - bearerAuth: []
paths:
  /request/{id}/download:
    get:
      summary: 下载结果
      description: 以 JSON、CSV 或 Excel 导出结果。
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
            examples:
              - ai_meu3z0171o8k9jc4dh
        - in: query
          name: format
          description: '**注意：** Excel 格式当前不可用。'
          required: false
          schema:
            type: string
            enum:
              - json
              - csv
            default: json
            examples:
              - csv
      responses:
        '200':
          description: 文件下载
          content:
            application/json: {}
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