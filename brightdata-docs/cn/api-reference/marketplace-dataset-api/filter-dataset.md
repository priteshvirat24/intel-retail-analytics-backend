> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 筛选数据集 (BETA)

> 对 250+ 个 Bright Data 市场数据集运行异步筛选任务。返回可下载的 snapshot_id，支持最大 200 MiB 的 CSV/JSON 上传。

Bright Data 市场数据集 API 的 Filter 端点针对 250+ 个市场数据集中的任意一个运行大体量或基于文件的筛选任务，并返回一个 `snapshot_id`，您可在任务完成后下载。

<Tip>
  将您的 API Key 粘贴到授权字段。要获取 API Key，请[创建账户](https://www.bright.cn/?hs_signup=1\&utm_source=docs\&utm_campaign=playground)并了解[如何生成 API Key](/cn/api-reference/authentication#如何生成新的-api-key？)。
</Tip>

## 何时使用 Filter？

对于可接受异步处理的批量或基于文件的任务，使用 Filter：

* 超过 1,000 条记录的批量导出。
* 按 CSV 或 JSON 文件中的大型值列表筛选，例如排除 10 万以上的公司 ID。
* Search 尚不支持的数据集。
* 可接受异步的计划任务或后台管道。

如需对受支持数据集进行亚秒级实时查询，请改用 [Search](/cn/api-reference/marketplace-dataset-api/search-dataset)。

## Filter 如何工作？

* 调用 Filter 端点会启动一个异步任务，并在您的账户中创建一份筛选数据的快照。
* 任务最长运行时间为 5 分钟。运行超时的任务将被取消。
* 按快照中的每条记录计费，采用标准市场费率 \$2.5 CPM。
* Filter 适用于全部 250+ 个市场数据集。
* 筛选组的最大嵌套深度为 3 层。

## 如何进行身份验证？

Filter 使用 Bearer token 身份验证。在 `Authorization` 请求头中传入您的 API Key：

```bash theme={null}
Authorization: Bearer YOUR_API_KEY
```

从[账户设置](/cn/api-reference/authentication#如何生成新的-api-key？)获取您的 Key。

## 限制

| 限制            | 值           | 说明                                              |
| ------------- | ----------- | ----------------------------------------------- |
| **每个文件最大行数**  | 10,000      | 每个上传的 CSV/JSON 文件最多可包含 10,000 行数据。表头行不计入。       |
| **每次请求最大文件数** | 无限制         | 一次 multipart 请求中可附加任意数量的文件，只要总大小不超过 200 MiB 上限。 |
| **最大请求大小**    | 200 MiB     | 所有上传文件和表单数据的总大小。超过 200 MiB 的请求会被拒绝。             |
| **任务超时**      | 5 分钟        | 如果筛选在 5 分钟内未完成，任务将被取消。                          |
| **筛选嵌套深度**    | 3 层         | 使用 `and`/`or` 的嵌套筛选组的最大深度。                      |
| **最大并行任务数**   | 每个数据集 100 个 | 每个数据集最多可同时运行 100 个 Filter 任务。                   |
| **速率限制**      | 120 次/小时    | 每小时最多的 Filter API 调用次数。                         |

## 如何调用 Filter？

Filter 有两种模式：JSON 用于普通筛选，multipart 用于文件上传。

### JSON 模式（无需上传文件）

将所有参数（`dataset_id`、`records_limit` 和 `filter`）放在 JSON 请求体中。将 `Content-Type` 设为 `application/json`：

```bash theme={null}
curl -X POST "https://api.brightdata.com/datasets/filter" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "dataset_id": "gd_l1viktl72bvl7bjuj0",
    "records_limit": 100,
    "filter": {
      "name": "name",
      "operator": "=",
      "value": "John"
    }
  }'
```

Filter 返回一个 `snapshot_id`：

```json theme={null}
{ "snapshot_id": "s_abc123..." }
```

### Multipart 模式（文件上传）

将 `dataset_id` 和 `records_limit` 作为查询参数发送，将 `filter` 和上传的文件放在 form-data 请求体中。将 `Content-Type` 设为 `multipart/form-data`：

```bash theme={null}
curl -X POST "https://api.brightdata.com/datasets/filter?dataset_id=gd_l1vijqt9jfj7olije&records_limit=100" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: multipart/form-data" \
  -F 'filter={"operator":"and","filters":[{"name":"industries:value","operator":"includes","value":"industries.csv"}]}' \
  -F 'files[]=@/path/to/industries.csv'
```

要排除 10 万以上的值，将它们拆分为每个最多 10,000 行的文件，并在一次请求中全部附加：

```bash theme={null}
curl -X POST "https://api.brightdata.com/datasets/filter?dataset_id=gd_l1vijqt9jfj7olije&records_limit=5000" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: multipart/form-data" \
  -F 'filter={"operator":"and","filters":[{"name":"company_id","operator":"not_in","value":"exclude1.csv"},{"name":"company_id","operator":"not_in","value":"exclude2.csv"},{"name":"company_id","operator":"not_in","value":"exclude3.csv"}]}' \
  -F 'files[]=@exclude1.csv' \
  -F 'files[]=@exclude2.csv' \
  -F 'files[]=@exclude3.csv'
```

有关 CSV 和 JSON 文件格式规则、文件引用以及上传故障排除，请参阅[使用 CSV/JSON 文件筛选数据集](/cn/api-reference/marketplace-dataset-api/filter-dataset-with-csv-json-files)。

## Filter 返回什么？

Filter 返回一个 `snapshot_id`。在任务完成后，使用它通过快照 API 下载筛选后的记录：

* [获取快照元数据](/cn/api-reference/marketplace-dataset-api/get-snapshot-meta)
* [通过 snapshot\_id 下载文件](/cn/api-reference/marketplace-dataset-api/download-the-file-by-snapshot_id)

## Filter 的费用是多少？

Filter 的费用为 \$2.5 CPM（每返回 1,000 条记录），与市场价格相同。筛选返回 0 条记录时不收费。

## Filter 可能返回哪些错误？

| 状态码   | 含义                                     | 处理方式                                                                               |
| ----- | -------------------------------------- | ---------------------------------------------------------------------------------- |
| `400` | 筛选或参数有误                                | 使用[获取数据集元数据](/cn/api-reference/marketplace-dataset-api/get-dataset-metadata)核对字段名。 |
| `401` | API Key 错误或缺失                          | 检查您的 Bearer token。                                                                 |
| `402` | 余额不足                                   | 充值或减小 `records_limit`。                                                             |
| `404` | 未知的 `dataset_id`                       | 确认数据集 ID。                                                                          |
| `422` | 筛选未匹配任何记录                              | 放宽筛选条件或检查字段值。                                                                      |
| `429` | 并行任务过多（每个数据集最多 100 个）或触发速率限制（120 次/小时） | 退避后重试。                                                                             |

## 筛选语法

`filter` 对象及其运算符、筛选组和嵌套规则与 [Search 端点](/cn/api-reference/marketplace-dataset-api/search-dataset)共享，并集中记录在一处。完整的运算符列表、筛选组、最多 3 层嵌套以及 CSV/JSON 文件引用，请参阅[筛选语法参考](/cn/api-reference/marketplace-dataset-api/filter-syntax)。

## 相关文档

* [Dataset API 概述](/cn/api-reference/marketplace-dataset-api/overview)
* [Search 数据集（同步）](/cn/api-reference/marketplace-dataset-api/search-dataset)
* [筛选语法参考](/cn/api-reference/marketplace-dataset-api/filter-syntax)
* [使用 CSV/JSON 文件筛选数据集](/cn/api-reference/marketplace-dataset-api/filter-dataset-with-csv-json-files)
* [获取数据集元数据](/cn/api-reference/marketplace-dataset-api/get-dataset-metadata)


## OpenAPI

````yaml cn-dca-api POST /datasets/filter
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
      description: 基于提供的过滤条件创建数据集快照
      parameters:
        - name: dataset_id
          in: query
          description: 要过滤的数据集 ID（在 multipart/form-data 模式下为必填）
          required: false
          schema:
            type: string
            example: gd_l1viktl72bvl7bjuj0
        - name: records_limit
          description: 限制快照中包含的记录数量
          in: query
          required: false
          schema:
            type: integer
            example: 1000
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - dataset_id
                - filter
              properties:
                dataset_id:
                  type: string
                  description: 要过滤的数据集 ID
                  example: gd_l1viktl72bvl7bjuj0
                records_limit:
                  type: integer
                  description: 限制快照中包含的记录数量
                  example: 1000
                filter:
                  $ref: '#/components/schemas/DatasetFilter'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/FilterDatasetBody'
      responses:
        '200':
          description: 快照创建任务已成功启动
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
                  - '"filter.filters[0].invalid_prop" 不被允许'
                  - '"records_limit" 必须是正数'
        '402':
          description: 余额不足，无法创建快照
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorBody'
              example:
                error: 您当前的余额不足以处理此数据采集请求。请向账户添加资金或调整请求以继续。($1 缺失)
        '422':
          description: 提供的过滤条件未匹配到任何记录
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorBody'
              example:
                error: 提供的过滤条件未匹配到任何记录
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
    DatasetFilter:
      anyOf:
        - $ref: '#/components/schemas/DatasetFilterItem'
          title: 单字段过滤器
        - $ref: '#/components/schemas/DatasetFilterGroup'
          title: 过滤器组
        - $ref: '#/components/schemas/DatasetFilterItemNoVal'
          title: 无值单字段过滤器
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
          description: 要过滤的字段名称
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
          description: 用于过滤的值
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
          description: 针对对象数组：如果为 true，则所有过滤器必须在单个对象内匹配
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
          description: 要过滤的字段名称
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