> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 接收批量数据

> 使用 GET /dca/dataset?id=<collection_id> 获取异步 Scraper Studio 批量采集的结果。采集进行中返回状态对象，采集就绪后返回 JSON 记录数组。

使用 `GET /dca/dataset?id=<collection_id>` 获取异步 Bright Data Scraper Studio 批量采集的结果。当采集仍在运行时，该端点返回一个状态对象。当采集就绪后，它会返回一个 JSON 记录数组。

<Note>
  请将 [POST /dca/trigger](./Trigger_a_scraper_for_batch_collection_method) 返回的 `collection_id` 用作本端点的 `id` 查询参数。
</Note>

<Note>
  批量采集结果在采集后 16 天内可供下载。为了避免过期，请在 16 天内下载数据，或配置[推送递送方式](./Choose_a_delivery_type_on_request_level)以将其自动发送到您的存储。
</Note>

## 请求

<CodeGroup>
  ```bash cURL theme={null}
  curl --request GET \
    --url 'https://api.brightdata.com/dca/dataset?id=YOUR_COLLECTION_ID' \
    --header 'Authorization: Bearer YOUR_API_KEY'
  ```

  ```python Python theme={null}
  response = requests.get(
      "https://api.brightdata.com/dca/dataset",
      params={"id": collection_id},
      headers={"Authorization": f"Bearer {API_TOKEN}"},
  )
  ```

  ```js Node.js theme={null}
  const response = await fetch(
    `https://api.brightdata.com/dca/dataset?id=${collectionId}`,
    { headers: { Authorization: `Bearer ${process.env.BRIGHT_DATA_API_TOKEN}` } }
  );
  ```
</CodeGroup>

## 响应

当采集仍在构建中时（HTTP 202）：

```json theme={null}
{
  "status": "building",
  "message": "Dataset is not ready yet, try again in XXs"
}
```

当采集就绪后（HTTP 200）：

```json theme={null}
[
  {
    "url": "https://example.com/product/1",
    "title": "product_name",
    "price": 8.45,
    "availability": "in stock",
    "input": {
      "url": "https://example.com/product/1"
    }
  }
]
```

具体的字段集取决于您在构建采集器时定义的输出模式。默认情况下，每个成功的输入对应一行。

## 获取结果

当采集仍在运行时，该端点返回 `202 Accepted` 以及一个状态对象。当采集就绪后，它返回 `200 OK` 以及一个 JSON 记录数组。

对于可能耗时数分钟或数小时的长时间采集，请避免频繁轮询。请改用以下方式之一：

* 以较长的时间间隔定期检查采集状态。
* 配置[推送递送方式](./Choose_a_delivery_type_on_request_level)，例如 webhook、Amazon S3、Google Cloud Storage、Azure Blob Storage、SFTP/FTP 或电子邮件。
* 使用[控制面板](https://brightdata.com/cp/scrapers)监控运行进度。

批量采集结果保留 16 天。请在保留期内下载数据，或配置推送递送以自动存储结果。

## 错误

| 状态码                | 原因                      | 解决方法                                                    |
| ------------------ | ----------------------- | ------------------------------------------------------- |
| `401 Unauthorized` | 令牌缺失、格式错误或已撤销           | 从[账户设置 → API 令牌](https://brightdata.com/cp/setting)重新复制 |
| `404 Not Found`    | 采集 ID 不存在、已删除或已过期（16 天） | 如果仍需要数据，请重新触发采集器                                        |
| `[]`（空数组）          | 采集已完成但没有产生任何行           | 检查输入 URL 和采集器的输出模式                                      |
| `5xx`              | Bright Data API 临时错误    | 使用指数退避重试，例如 1s、2s、4s                                    |


## OpenAPI

````yaml api-reference/web-scraper-ide-rest-api GET /dca/dataset
openapi: 3.1.0
info:
  title: Brightdata API
  description: API for interaction with datasets marketplace
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security:
  - bearerAuth: []
paths:
  /dca/dataset:
    get:
      description: >-
        Retrieve the results of an asynchronous Scraper Studio batch collection.


        While the collection is still running, the endpoint returns `202
        Accepted` with a status object. When the collection is ready, it returns
        `200 OK` with a JSON array of records. Use the `collection_id` returned
        by [POST
        /dca/trigger](/api-reference/scraper-studio-api/Trigger_a_scraper_for_batch_collection_method)
        as the `id` query parameter.
      parameters:
        - name: id
          in: query
          required: true
          schema:
            type: string
            example: j_abc123def456
          description: >-
            Collection ID returned by `POST /dca/trigger`. Use this value as the
            `id` query parameter.
      responses:
        '200':
          description: Dataset (Ready)
          content:
            application/json:
              examples:
                response:
                  value:
                    - Image: https://targetwebsite.com/product_id.png
                      Title: product_name
                      Price: product_price
                      input:
                        url: https://targetwebsite.com/product_id/
        '202':
          description: Waiting for Dataset
          content:
            application/json:
              examples:
                response:
                  value:
                    status: building
                    message: Dataset is not ready yet, try again in XXs
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        Use your Bright Data API Key as a Bearer token in the Authorization
        header.


        **How to authenticate:**

        1. Obtain your API Key from the Bright Data account settings at
        https://brightdata.com/cp/setting/users

        2. Include the API Key in the Authorization header of your requests

        3. Format: `Authorization: Bearer YOUR_API_KEY`


        **Example:**

        ```

        Authorization: Bearer
        b5648e1096c6442f60a6c4bbbe73f8d2234d3d8324554bd6a7ec8f3f251f07df

        ```


        Learn how to get your Bright Data API key:
        https://docs.brightdata.com/api-reference/authentication
      bearerFormat: API Key

````