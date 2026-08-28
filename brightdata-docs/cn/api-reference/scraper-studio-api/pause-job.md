> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 暂停 Scraper Studio 作业

> 使用 POST /dca/jobs/{job_id}/pause 临时停止正在运行的 Bright Data Scraper Studio 作业。作业转为 paused 状态，并返回纯文本响应 OK。

临时停止正在运行的 Bright Data Scraper Studio 作业。作业将停止处理新的输入并转为 `paused` 状态，之后可通过[恢复 Scraper Studio 作业](/cn/api-reference/scraper-studio-api/resume-job)重新启动。

该端点不接受请求体，成功时返回纯文本响应体 `OK`，而非 JSON。请按文本读取响应，不要对其调用 JSON 解析器。

## 作业状态行为

| 操作 | 使用场景          | 结果              |
| -- | ------------- | --------------- |
| 暂停 | 需要临时停止正在运行的作业 | 作业转为 `paused`   |
| 恢复 | 需要继续已暂停的作业    | 作业恢复为 `running` |
| 取消 | 需要永久停止作业      | 作业转为 `canceled` |

已完成的作业无法暂停、恢复或取消。

## 如何查找作业 ID

使用作业列表端点查找您要暂停的作业 ID：

```bash theme={null}
curl "https://api.brightdata.com/dca/collector/jobs?from_date=2026-06-01&to_date=2026-07-13" \
  -H "Authorization: Bearer $BRIGHT_DATA_API_TOKEN"
```

将返回的 `id` 值用作 `job_id` 路径参数。完整参数列表请参见[列出 Scraper Studio 作业](/cn/api-reference/scraper-studio-api/list-jobs)。

## 何时使用该端点

* 在目标网站发生故障期间暂停大批量作业，待网站恢复后再继续
* 在维护窗口期间释放并发资源，用于优先级更高的工作
* 当作业返回大量 `blocked` 或 `detect_block` 错误时先停止作业，以便调整国家、会话或速率设置

如需永久停止作业，请使用[取消 Scraper Studio 作业](/cn/api-reference/scraper-studio-api/cancel-job)。

## 相关

* [恢复 Scraper Studio 作业](/cn/api-reference/scraper-studio-api/resume-job)：重新启动通过该端点暂停的作业
* [取消 Scraper Studio 作业](/cn/api-reference/scraper-studio-api/cancel-job)：永久停止作业，而非临时停止
* [列出 Scraper Studio 作业](/cn/api-reference/scraper-studio-api/list-jobs)：查找传入该端点的 `job_id`
* [IDE 作业数据 API](/cn/api-reference/scraper-studio-api/job-data)：暂停后确认作业状态


## OpenAPI

````yaml api-reference/web-scraper-ide-rest-api POST /dca/jobs/{job_id}/pause
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
  /dca/jobs/{job_id}/pause:
    post:
      summary: Pause a Scraper Studio job
      description: >-
        Pauses an existing Bright Data Scraper Studio job. The job moves to
        `paused`. Completed jobs cannot be paused, resumed or canceled. Find the
        `job_id` with the `GET /dca/collector/jobs` endpoint.
      operationId: pauseScraperStudioJob
      parameters:
        - name: job_id
          in: path
          required: true
          description: ID of the job to pause
          schema:
            type: string
          example: j_ma13y9ay1piehrso8r
      responses:
        '200':
          description: Job paused successfully
          content:
            text/plain:
              schema:
                type: string
              example: OK
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