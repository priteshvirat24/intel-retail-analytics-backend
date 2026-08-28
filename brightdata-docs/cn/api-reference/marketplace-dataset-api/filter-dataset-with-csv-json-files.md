> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 筛选数据集（JSON 或文件上传）

> 根据提供的筛选条件创建数据集快照

Bright Data 市场数据集 API 的 Filter 端点可以按存储在 CSV 或 JSON 文件中的成千上万个值对数据集进行筛选。以 multipart 模式上传一个或多个文件，并在筛选中引用每个文件名。

<Tip>
  将您的 API Key 粘贴到授权字段。要获取 API Key，请[创建账户](https://www.bright.cn/?hs_signup=1\&utm_source=docs\&utm_campaign=playground)并了解[如何生成 API Key](/cn/api-reference/authentication#如何生成新的-api-key？)。
</Tip>

## 基于文件的筛选如何工作？

当您需要按大型值列表筛选时使用文件上传，例如包含或排除 10 万以上的公司 ID：

* 以 `multipart/form-data` 模式上传 CSV 或 JSON 文件，并在筛选中引用每个文件名。
* 每个文件最多包含 10,000 行数据，整个请求最大为 200 MiB。
* Filter 任务以异步方式运行，并返回一个 `snapshot_id`，可在任务完成后下载。

有关异步任务流程、限制、定价和错误码，请参阅 [Filter 数据集（异步）](/cn/api-reference/marketplace-dataset-api/filter-dataset)。

## 如何格式化 CSV 或 JSON 文件？

<Tabs>
  <Tab title="CSV">
    * 第一行必须是与筛选字段名称匹配的表头。
    * 后续每行包含单个值。

    ```csv Example: industries.csv theme={null}
    industries:value
    Accounting
    Ad Network
    Advertising
    ```
  </Tab>

  <Tab title="JSON">
    * 必须是对象数组，每个对象的键与筛选字段名称匹配。

    ```json Example industries.json theme={null}
    [
      {"industries:value": "Accounting"},
      {"industries:value": "Ad Network"},
      {"industries:value": "Advertising"}
    ]
    ```
  </Tab>
</Tabs>

***

## 如何在筛选中引用文件？

使用文件上传时，将筛选的 `value` 字段设为文件名：

```json Example theme={null}
{
  "operator": "and",
  "filters": [
    {
      "name": "industries:value",
      "operator": "includes",
      "value": "industries.csv"
    }
  ]
}
```

文件引用仅可与 `in`、`not_in`、`includes`、`not_includes`、`array_includes` 和 `not_array_includes` 运算符配合使用。完整的运算符表和字段类型，请参阅[筛选语法参考](/cn/api-reference/marketplace-dataset-api/filter-syntax#哪些运算符可读取-csv-或-json-文件？)。

***

## 使用多个文件进行筛选

```bash theme={null}
curl \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: multipart/form-data" \
  -F "files[]=@/path/to/industries.csv" \
  -F "files[]=@/path/to/regions.csv" \
  -F "filter={\"operator\":\"and\",\"filters\":[{\"name\":\"industries:value\",\"operator\":\"includes\",\"value\":\"industries.csv\"},{\"name\":\"region\",\"operator\":\"in\",\"value\":\"regions.csv\"}]}" \
  "api.brightdata.com/datasets/filter?dataset_id=gd_l1vijqt9jfj7olije"
```

## 排查文件上传问题

| 问题                        | 可能解决方案                                                                                       |
| :------------------------ | :------------------------------------------------------------------------------------------- |
| **"File not found"**      | 确保筛选中引用的文件名与上传文件名完全匹配。                                                                       |
| **"Invalid file format"** | 检查 CSV 表头是否与筛选字段名称匹配，或确保 JSON 是对象数组。                                                         |
| **"Field not found"**     | 验证字段是否存在于数据集中。使用 [获取数据集元数据](/cn/api-reference/marketplace-dataset-api/get-dataset-metadata)。 |

## 相关文档

* [获取数据集列表](/cn/api-reference/marketplace-dataset-api/get-dataset-list)
* [获取数据集元数据](/cn/api-reference/marketplace-dataset-api/get-dataset-metadata)
* [数据集下载 API](/cn/datasets/scrapers/custom-scrapers/custom-dataset-api)


## OpenAPI

````yaml cn-filter-csv-json POST /datasets/filter
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
  /datasets/filter:
    post:
      description: 根据提供的筛选条件创建数据集快照
      parameters:
        - name: dataset_id
          required: true
          in: query
          description: 要筛选的数据集 ID（在 multipart/form-data 模式下为必填）
          schema:
            type: string
            example: gd_l1viktl72bvl7bjuj0
        - name: records_limit
          description: 限制包含在快照中的记录数量
          in: query
          required: false
          schema:
            type: integer
            example: 1000
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/FilterDatasetBody'
      responses:
        '200':
          description: 创建快照的任务已成功启动
          content:
            application/json:
              schema:
                type: object
                properties:
                  snapshot_id:
                    type: string
                    description: 快照 ID
        '400':
          description: 错误请求
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ValidationErrorBody'
              example:
                validation_errors:
                  - '"filter.filters[0].invalid_prop" 不允许'
                  - '"records_limit" 必须为正数'
        '402':
          description: 余额不足，无法创建快照
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorBody'
              example:
                error: 您当前的余额不足以处理此数据收集请求。请向您的账户充值或调整请求以继续。 ($1 缺失)
        '422':
          description: 提供的筛选条件未匹配任何记录
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorBody'
              example:
                error: 提供的筛选条件未匹配任何记录
        '429':
          description: 并行任务过多
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorBody'
              example:
                error: 每个数据集的最大任务限制 100 已超出
components:
  schemas:
    FilterDatasetBody:
      type: object
      required:
        - filter
      properties:
        filter:
          $ref: '#/components/schemas/DatasetFilter'
    ValidationErrorBody:
      type: object
      properties:
        validation_errors:
          type: array
          items:
            type: string
    ErrorBody:
      type: object
      properties:
        error:
          type: string
    DatasetFilter:
      anyOf:
        - $ref: '#/components/schemas/DatasetFilterItem'
          title: 单字段筛选器
        - $ref: '#/components/schemas/DatasetFilterGroup'
          title: 筛选器组
        - $ref: '#/components/schemas/DatasetFilterItemNoVal'
          title: 无值单字段筛选器
    DatasetFilterItem:
      type: object
      required:
        - name
        - operator
        - value
      additionalProperties: false
      properties:
        name:
          type: string
          description: 用于筛选的字段名称
        operator:
          type: string
          enum:
            - '='
            - '!='
            - '>'
            - <
            - '>='
            - <=
            - in
            - not_in
            - includes
            - not_includes
            - array_includes
            - not_array_includes
        value:
          description: 筛选值
          oneOf:
            - type: string
            - type: number
            - type: boolean
            - type: object
            - type: array
              items:
                oneOf:
                  - type: string
                  - type: number
                  - type: boolean
      example:
        name: name
        operator: '='
        value: John
    DatasetFilterGroup:
      type: object
      required:
        - operator
        - filters
      additionalProperties: false
      properties:
        operator:
          type: string
          enum:
            - and
            - or
        combine_nested_fields:
          type: boolean
          description: 对于对象数组：如果为 true，则所有筛选器必须在同一个对象中匹配
        filters:
          type: array
          items:
            $ref: '#/components/schemas/DatasetFilter'
      example:
        operator: and
        filters:
          - name: name
            operator: '='
            value: John
          - name: age
            operator: '>'
            value: '30'
    DatasetFilterItemNoVal:
      type: object
      required:
        - name
        - operator
      additionalProperties: false
      properties:
        name:
          type: string
          description: 用于筛选的字段名称
        operator:
          type: string
          enum:
            - is_null
            - is_not_null
      example:
        name: reviews_count
        operator: is_not_null
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