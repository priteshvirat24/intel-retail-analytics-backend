> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 异步触发爬虫进行批量采集

> 使用 POST /dca/trigger 为 Scraper Studio 采集器启动异步批量采集。请求体是输入对象的 JSON 数组，并返回 collection_id 以便稍后获取结果。

使用 `POST /dca/trigger` 为已发布的 Bright Data Scraper Studio 采集器启动异步批量采集。请求体是输入对象的 JSON 数组，每个对象都必须与采集器的输入模式匹配。

该端点会立即返回一个 `collection_id`。采集完成后，使用该 ID 调用[接收批量数据](./Receive_batch_data)端点（`GET /dca/dataset`）来获取结果。

## 请求

请求体是输入对象的 JSON 数组。每个对象都必须与你在 [Scraper Studio](https://brightdata.com/cp/scrapers) 中为采集器定义的输入模式匹配。基于 URL 的采集器可能需要 `url` 字段，而其他采集器可能需要 `keyword`、`location`、`country` 等字段或自定义输入字段。

请求体必须是 JSON 数组。如果只有单个输入，请发送只包含一个对象的数组。

<CodeGroup>
  ```bash cURL theme={null}
  curl --request POST \
    --url 'https://api.brightdata.com/dca/trigger?collector=YOUR_COLLECTOR_ID&queue_next=1' \
    --header 'Authorization: Bearer YOUR_API_KEY' \
    --header 'Content-Type: application/json' \
    --data '[
      { "url": "https://example.com/product/1" },
      { "url": "https://example.com/product/2" }
    ]'
  ```

  ```python Python theme={null}
  import os, requests

  response = requests.post(
      "https://api.brightdata.com/dca/trigger",
      params={"collector": os.environ["BRIGHT_DATA_COLLECTOR_ID"], "queue_next": 1},
      headers={
          "Authorization": f"Bearer {os.environ['BRIGHT_DATA_API_TOKEN']}",
          "Content-Type": "application/json",
      },
      json=[
          {"url": "https://example.com/product/1"},
          {"url": "https://example.com/product/2"},
      ],
  )
  collection_id = response.json()["collection_id"]
  ```

  ```js Node.js theme={null}
  const url = new URL("https://api.brightdata.com/dca/trigger");
  url.searchParams.set("collector", process.env.BRIGHT_DATA_COLLECTOR_ID);
  url.searchParams.set("queue_next", "1");

  const response = await fetch(url, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${process.env.BRIGHT_DATA_API_TOKEN}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify([
      { url: "https://example.com/product/1" },
      { url: "https://example.com/product/2" },
    ]),
  });
  const { collection_id } = await response.json();
  ```
</CodeGroup>

## 响应

```json theme={null}
{
  "collection_id": "j_abc123def456",
  "start_eta": "2026-05-22T13:26:22.702Z"
}
```

`collection_id` 标识本次采集运行。调用 `GET /dca/dataset` 时，将它作为 `id` 的值来获取结果。

```bash theme={null}
curl --request GET \
  --url 'https://api.brightdata.com/dca/dataset?id=j_abc123def456' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

| 字段              | 类型     | 说明                                      |
| --------------- | ------ | --------------------------------------- |
| `collection_id` | string | 采集运行的 ID。使用该值从 `GET /dca/dataset` 获取结果。 |
| `start_eta`     | string | 采集的预计开始时间，采用 ISO 8601 格式。               |

## 在采集完成时发送通知

使用 `notify` 查询参数，在批量采集完成时发送 webhook 或邮件通知。该参数接受一个 JSON 对象，以 URL 查询参数的形式传递，因此值必须经过 URL 编码。单独使用 `notify`（不带 `deliver`）时，通知在采集作业完成后发送。

以下 cURL 示例触发批量采集，并在作业完成时发送 webhook 通知。`--url-query` 选项（curl 7.87.0 起可用）会自动对 JSON 值进行 URL 编码：

```bash theme={null}
curl --request POST "https://api.brightdata.com/dca/trigger" \
  --url-query "collector=YOUR_COLLECTOR_ID" \
  --url-query 'notify={"type":"webhook","endpoint":"https://example.com/webhook"}' \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '[{ "url": "https://example.com/product/1" }]'
```

响应与上文所示的标准 `collection_id` 响应相同。采集作业完成后，Bright Data 会向配置的端点发送通知。

`notify` 对象包含以下字段：

| 字段         | 类型     | 必填             | 说明                        |
| ---------- | ------ | -------------- | ------------------------- |
| `type`     | string | 是              | 通知类型：`webhook` 或 `email`。 |
| `endpoint` | string | `webhook` 类型必填 | 接收通知的 webhook URL。        |

## 为单个请求覆盖交付设置

使用 `deliver` 查询参数，为特定请求覆盖爬虫的默认交付设置。这样可以将采集结果交付到与控制面板**交付偏好**中配置的目标不同的目的地，而无需修改爬虫配置。与 `notify` 相同，该参数接受一个经 URL 编码的 JSON 对象。

以下示例触发批量采集，将结果交付到 Amazon S3，并在交付完成后发送 webhook 通知：

```bash theme={null}
COLLECTOR=YOUR_COLLECTOR_ID

DELIVER='{
  "type": "s3",
  "bucket": "YOUR_BUCKET",
  "credentials": {
    "aws-access-key": "YOUR_AWS_ACCESS_KEY",
    "aws-secret-key": "YOUR_AWS_SECRET_KEY"
  },
  "region": "YOUR_REGION",
  "directory": "brightdata/YOUR_DIRECTORY",
  "filename": {
    "template": "results_{[datetime]}",
    "extension": "json"
  },
  "delivery_type": "deliver_results"
}'

NOTIFY='{
  "type": "webhook",
  "endpoint": "https://example.com/webhook"
}'

curl --request POST "https://api.brightdata.com/dca/trigger" \
  --url-query "collector=$COLLECTOR" \
  --url-query "deliver=$DELIVER" \
  --url-query "notify=$NOTIFY" \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '[{ "url": "https://example.com/product/1" }]'
```

`deliver` 对象支持与**交付偏好**相同的目标类型，包括 `s3`、`gcs`、`azure`、`sftp`、`webhook` 和 `email`。

## notify 与 deliver 的组合行为

| 配置                        | 行为                          |
| ------------------------- | --------------------------- |
| 不使用 `notify` 和 `deliver`  | 使用爬虫的默认交付设置，不发送请求级通知。       |
| 仅使用 `notify`              | 在采集作业完成时发送通知。               |
| 仅使用 `deliver`             | 使用请求级交付配置交付结果。              |
| `deliver` 与 `notify` 同时使用 | 使用请求级交付配置交付结果，然后在交付完成时发送通知。 |

## 何时使用批量采集

在以下情况下使用批量采集（`POST /dca/trigger`）：

* 你需要在一次运行中处理多个输入。
* 你可以等待采集完成后再获取结果。
* 你希望稍后通过 `collection_id` 获取结果。
* 你正在构建数据集或定时采集工作流。

当你需要为单个输入立即获取结果，或在较短的请求窗口内获取结果时，请使用[实时采集](./initiate-a-realtime-job/sync-realtime-job)。

## 错误

| 状态码                        | 原因                    | 解决方法                                                                  |
| -------------------------- | --------------------- | --------------------------------------------------------------------- |
| `401 Unauthorized`         | 令牌缺失、格式错误或已撤销         | 从[账户设置 → API 令牌](https://brightdata.com/cp/setting)重新复制               |
| `404 Not Found`            | 采集器 ID 不存在，或你的账户无访问权限 | 在 [Scraper Studio](https://brightdata.com/cp/scrapers) 中打开采集器并重新复制 ID |
| `422 Unprocessable Entity` | 请求体中的对象与采集器的输入模式不匹配   | 对照采集器的**输入**选项卡确认字段名称                                                 |
| `5xx`                      | Bright Data API 临时错误  | 使用指数退避重试，例如 1s、2s、4s                                                  |

## 重试行为

使用相同的输入重新触发会创建一个带有新 `collection_id` 的新采集运行。该端点不是幂等的，也不会在多次运行之间对输入去重。如果只想重试失败的输入，请使用[获取作业错误](./get-errors-for-job)识别本次运行中失败的输入，然后仅用这些输入触发一次新的采集。


## OpenAPI

````yaml api-reference/web-scraper-ide-rest-api POST /dca/trigger
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
  /dca/trigger:
    post:
      description: >-
        Start an asynchronous batch collection for a published Scraper Studio
        collector.


        The request body is a JSON array of input objects, and each object must
        match the input schema defined for the collector. The endpoint returns a
        `collection_id` immediately. Use this ID with [GET
        /dca/dataset](/api-reference/scraper-studio-api/Receive_batch_data) to
        retrieve the results when the collection is complete.


        Use batch collection to process multiple inputs in one run. For a single
        input returned immediately, use the [real-time
        endpoints](/api-reference/scraper-studio-api/initiate-a-realtime-job/sync-realtime-job).
      parameters:
        - name: collector
          in: query
          required: true
          schema:
            type: string
            example: c_abc123
          description: >-
            Collector ID of the Scraper Studio scraper to run. The ID starts
            with `c_`.
        - name: version
          in: query
          schema:
            type: string
          description: Set to `dev` to trigger the development version of the scraper
        - name: name
          in: query
          schema:
            type: string
          description: Human-readable name for the batch collection.
        - name: queue_next
          in: query
          schema:
            type: integer
            default: 1
          description: >-
            If another collection is already running, queue this collection to
            run after it.
        - name: queue
          in: query
          schema:
            type: string
          description: >-
            Queue name used to group related collection runs. Runs that share a
            queue start one after another.
        - name: confirm_cancel
          in: query
          schema:
            type: integer
            default: 1
          description: >-
            Cancels a running collection for this collector and runs this one
            instead.
        - name: no_downloads
          in: query
          schema:
            type: integer
            default: 1
          description: Disables media file downloads for this collection.
        - name: deadline
          in: query
          schema:
            type: string
            example: 1h
          description: >-
            Sets the maximum time the collection can run. When the deadline is
            reached, Bright Data terminates the collection. Use `h` for hours,
            `m` for minutes or `s` for seconds, for example `1h`, `30m` or
            `45s`.
        - name: notify
          in: query
          schema:
            type: string
            example: '{"type":"webhook","endpoint":"https://example.com/webhook"}'
          description: >-
            Notification configuration for this request as a URL-encoded JSON
            object. Used alone, the notification is sent when the collection job
            completes. Used together with `deliver`, the notification is sent
            after delivery completes.
        - name: deliver
          in: query
          schema:
            type: string
            example: >-
              {"type":"s3","bucket":"YOUR_BUCKET","credentials":{"aws-access-key":"YOUR_AWS_ACCESS_KEY","aws-secret-key":"YOUR_AWS_SECRET_KEY"},"region":"YOUR_REGION","directory":"brightdata/YOUR_DIRECTORY","filename":{"template":"results_{[datetime]}","extension":"json"},"delivery_type":"deliver_results"}
          description: >-
            Request-level delivery configuration as a URL-encoded JSON object.
            Overrides the scraper's default Delivery preferences for this
            collection only.
      requestBody:
        required: true
        description: >-
          A JSON array of input objects. Each object must match the input schema
          defined for the collector. A URL-based collector may require a `url`
          field, while other collectors may require fields such as `keyword`,
          `location` or `country`. For a single input, send an array with one
          object.
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                additionalProperties: true
                description: >-
                  Single input object whose fields match the collector input
                  schema.
                properties:
                  url:
                    type: string
                    format: uri
                    description: >-
                      Example field for collectors that take a target URL.
                      Replace with the fields your collector expects.
            examples:
              request:
                value:
                  - url: https://example.com/product/1
                  - url: https://example.com/product/2
      responses:
        '200':
          description: Returns a `collection_id` for the new collection run.
          content:
            application/json:
              schema:
                type: object
                properties:
                  collection_id:
                    type: string
                    description: >-
                      ID of the collection run. Use this value as the `id` when
                      calling GET /dca/dataset to retrieve results.
                  start_eta:
                    type: string
                    description: >-
                      Estimated start time for the collection, in ISO 8601
                      format.
              examples:
                response:
                  value:
                    collection_id: j_abc123def456
                    start_eta: '2026-05-22T13:26:22.702Z'
      x-codeSamples:
        - lang: py
          label: Python SDK
          source: |-
            # Install: pip install brightdata-sdk
            from brightdata import BrightDataClient

            async with BrightDataClient(api_key="YOUR_API_KEY") as client:
                # Trigger an async job, then wait for results
                job = await client.scraper_studio.trigger(
                    "c_abc123", {"url": "https://example.com/product/1"}
                )
                data = await job.wait_and_fetch(timeout=120)
                print(data)
        - lang: js
          label: JavaScript SDK
          source: >-
            // Install: npm install @brightdata/sdk

            import { bdclient } from '@brightdata/sdk';


            const client = new bdclient({ apiKey: 'YOUR_API_KEY' });


            // Trigger an async job, then wait for results

            const job = await
            client.scraperStudio.trigger('c_your_collector_id', {
              url: 'https://example.com/product/1',
            });

            const data = await job.waitAndFetch();


            console.log(data);


            await client.close();
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