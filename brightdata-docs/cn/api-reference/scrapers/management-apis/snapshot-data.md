> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 获取快照数据

> 获取特定数据集快照的日志



## OpenAPI

````yaml cn-dca-api get /datasets/v3/log/{snapshot_id}
openapi: 3.1.0
info:
  title: Brightdata API
  description: 用于与数据集市场交互的 API
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security:
  - bearerAuth: []
paths:
  /datasets/v3/log/{snapshot_id}:
    get:
      description: 获取特定数据集快照的日志
      parameters:
        - name: snapshot_id
          in: path
          required: true
          schema:
            type: string
            example: s_mcd3rc6l2md984eoij
      responses:
        '200':
          description: 成功
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SnapshotDataResponse'
        '404':
          description: 未找到快照
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: 未找到快照
components:
  schemas:
    SnapshotDataResponse:
      type: object
      examples:
        - id: s_mcd3rc6l2md984eoij
          created: '2025-06-26T08:09:32.781Z'
          Status: ready
          dataset_name: Apple App Store
          scraper_name: Apple App Store - collect by URL
          Dataset_size: 2
          Inputs_count: 2
          Dataset_id: gd_lsk9ki3u2iishmwrui
          Discovery_collector_id: null
          file_size: 65381
          trigger:
            type: CP
            user: amite@brightdata.com
            ip: 130.41.220.17
            trigger_url: >-
              /trigger?customer=hl_dacd97fb&type=url_collection&dataset_id=gd_lsk9ki3u2iishmwrui&include_errors=true&discover_only=false
            ts: '2025-06-26T08:09:32.074Z'
          Duration: 6
          Duration_per_input: 3
          Success_rate: 1
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