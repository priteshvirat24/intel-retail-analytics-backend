> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 重新运行 Scraper Studio 作业

> 使用 POST /dca/jobs/{job_id}/rerun 从已有的 Bright Data Scraper Studio 作业启动新运行。可重新运行全部内容，或发送 failed_only 仅重试失败部分。

从已有的 Bright Data Scraper Studio 作业启动新的运行。不发送请求体时，将从头重新运行整个作业；发送 `failed_only: 1` 时，仅重新运行失败的步骤。

请求成功后会启动一个**新**作业并返回其 `collection_id`。原作业保持不变。

<Warning>
  只有数据尚未过期的作业才能重新运行。调用该端点前，请在[列出 Scraper Studio 作业](/cn/api-reference/scraper-studio-api/list-jobs)或 [IDE 作业数据 API](/cn/api-reference/scraper-studio-api/job-data) 中查看作业的 `expired` 时间戳。如果数据已过期，重新运行将失败，您必须使用原始输入触发新作业。

  Scraper Studio 保留批量采集结果 16 天，保留实时结果 7 天。请参见 [Scraper Studio 规格说明](/cn/datasets/scraper-studio/specifications)。
</Warning>

## 重新运行行为

| 请求体                    | 行为              | 使用场景                 |
| ---------------------- | --------------- | -------------------- |
| 无请求体                   | 从头重新运行整个作业      | 需要重新采集全部输入           |
| `{ "failed_only": 1 }` | 仅重新运行所选作业中失败的步骤 | 作业已完成但存在失败项，只需重试这些部分 |

## 请求

不发送请求体即可重新运行全部内容：

<CodeGroup>
  ```bash cURL theme={null}
  curl -X POST "https://api.brightdata.com/dca/jobs/$JOB_ID/rerun" \
    -H "Authorization: Bearer $BRIGHT_DATA_API_TOKEN"
  ```

  ```python Python theme={null}
  response = requests.post(
      f"https://api.brightdata.com/dca/jobs/{job_id}/rerun",
      headers={"Authorization": f"Bearer {API_TOKEN}"},
  )
  rerun = response.json()
  print(rerun["collection_id"])
  ```

  ```js Node.js theme={null}
  const response = await fetch(
    `https://api.brightdata.com/dca/jobs/${jobId}/rerun`,
    {
      method: 'POST',
      headers: { Authorization: `Bearer ${process.env.BRIGHT_DATA_API_TOKEN}` },
    }
  );
  const rerun = await response.json();
  console.log(rerun.collection_id);
  ```
</CodeGroup>

添加 `failed_only: 1` 可仅重试失败的步骤：

<CodeGroup>
  ```bash cURL theme={null}
  curl -X POST "https://api.brightdata.com/dca/jobs/$JOB_ID/rerun" \
    -H "Authorization: Bearer $BRIGHT_DATA_API_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{"failed_only": 1}'
  ```

  ```python Python theme={null}
  response = requests.post(
      f"https://api.brightdata.com/dca/jobs/{job_id}/rerun",
      headers={
          "Authorization": f"Bearer {API_TOKEN}",
          "Content-Type": "application/json",
      },
      json={"failed_only": 1},
  )
  rerun = response.json()
  ```

  ```js Node.js theme={null}
  const response = await fetch(
    `https://api.brightdata.com/dca/jobs/${jobId}/rerun`,
    {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${process.env.BRIGHT_DATA_API_TOKEN}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ failed_only: 1 }),
    }
  );
  const rerun = await response.json();
  ```
</CodeGroup>

## 响应

```json theme={null}
{
  "collection_id": "j_mdb7x2kq93nfytra1",
  "start_eta": "2026-07-20T12:10:12.301Z"
}
```

在 [IDE 作业数据 API](/cn/api-reference/scraper-studio-api/job-data) 和[接收批量数据](/cn/api-reference/scraper-studio-api/Receive_batch_data)中，将返回的 `collection_id` 用作 `job_id`。它标识的是新的重新运行作业，而非原作业。

## 如何查找作业 ID

使用作业列表端点查找您要重新运行的作业 ID：

```bash theme={null}
curl "https://api.brightdata.com/dca/collector/jobs?from_date=2026-06-01&to_date=2026-07-13" \
  -H "Authorization: Bearer $BRIGHT_DATA_API_TOKEN"
```

将返回的 `id` 值用作 `job_id` 路径参数。完整参数列表请参见[列出 Scraper Studio 作业](/cn/api-reference/scraper-studio-api/list-jobs)。

## 何时使用该端点

* 修复选择器或解析器后，重试批量作业中失败的输入，无需重新采集已成功的输入
* 按计划重新采集完整作业，以刷新会随时间变化的数据
* 在目标网站发生故障并导致大量 `blocked` 或 `detect_block` 错误后重新运行

如需在决定完整重新运行还是使用 `failed_only` 之前，查看哪些输入失败及其原因，请使用[获取作业错误](/cn/api-reference/scraper-studio-api/get-errors-for-job)。

## 相关

* [获取作业错误](/cn/api-reference/scraper-studio-api/get-errors-for-job)：重新运行前确认哪些输入失败
* [IDE 作业数据 API](/cn/api-reference/scraper-studio-api/job-data)：查看原作业的 `expired` 时间戳和失败数量
* [列出 Scraper Studio 作业](/cn/api-reference/scraper-studio-api/list-jobs)：查找传入该端点的 `job_id`
* [取消 Scraper Studio 作业](/cn/api-reference/scraper-studio-api/cancel-job)：停止误启动的重新运行


## OpenAPI

````yaml api-reference/web-scraper-ide-rest-api POST /dca/jobs/{job_id}/rerun
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
  /dca/jobs/{job_id}/rerun:
    post:
      summary: Rerun a Scraper Studio job
      description: >-
        Starts a new run from an existing Bright Data Scraper Studio job. Send
        no request body to rerun the full job from the beginning, or send
        `failed_only: 1` to rerun only the failed steps. Only jobs whose data
        has not expired can be rerun: check the job's `expired` timestamp in the
        jobs list or job metadata first. If the data has expired, trigger a new
        job with the original inputs instead. Find the `job_id` with the `GET
        /dca/collector/jobs` endpoint.
      operationId: rerunScraperStudioJob
      parameters:
        - name: job_id
          in: path
          required: true
          description: ID of the job to rerun
          schema:
            type: string
          example: j_ma13y9ay1piehrso8r
      requestBody:
        required: false
        description: >-
          Omit the body to rerun the full job. Send `failed_only: 1` to rerun
          only the failed steps.
        content:
          application/json:
            schema:
              type: object
              properties:
                failed_only:
                  type: number
                  description: >-
                    Set to 1 to rerun only the failed steps. Omit to rerun the
                    full job.
                  example: 1
            example:
              failed_only: 1
      responses:
        '200':
          description: Rerun job started
          content:
            application/json:
              schema:
                type: object
                properties:
                  collection_id:
                    type: string
                    description: ID of the new rerun job
                  start_eta:
                    type: string
                    format: date-time
                    description: Estimated start time of the rerun job
              example:
                collection_id: j_mdb7x2kq93nfytra1
                start_eta: '2026-07-20T12:10:12.301Z'
        '401':
          description: API key missing, malformed or revoked
        '404':
          description: Job ID does not exist, has expired or belongs to another account
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