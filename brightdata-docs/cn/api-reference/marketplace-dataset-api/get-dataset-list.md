> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 数据集列表

> 列出所有 Scraper API 的数据集 ID，您可以使用此 API 端点检索可用数据集列表。

<a href="https://www.postman.com/bright-data-api/bright-data-api/request/1o6iob0/dataset-list" target="_blank">
  <img height="32" width="128" noZoom src="https://run.pstmn.io/button.svg" />
</a>


## OpenAPI

````yaml cn-dca-api GET /datasets/list
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
  /datasets/list:
    get:
      tags:
        - Datasets
      description: 获取可用数据集列表
      operationId: listDatasets
      responses:
        '200':
          description: 可用数据集列表
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/DatasetListItem'
                example:
                  - id: gd_l1vijqt9jfj7olije
                    name: Crunchbase 公司信息
                    size: 2300000
                  - id: gd_l1vikfch901nx3by4
                    name: Instagram - 个人资料
                    size: 620000000
        '401':
          description: 未授权 - API 密钥无效或缺失
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: Unauthorized
        '500':
          description: 服务器内部错误
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: Internal server error
components:
  schemas:
    DatasetListItem:
      type: object
      required:
        - id
        - name
        - size
      properties:
        id:
          type: string
          description: 数据集的唯一标识符
          example: gd_l1vijqt9jfj7olije
        name:
          type: string
          description: 数据集的人类可读名称
          example: Crunchbase companies information
        size:
          type: integer
          description: 数据集中的记录数量
          example: 2300000
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