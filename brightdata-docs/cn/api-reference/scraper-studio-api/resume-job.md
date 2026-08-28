> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 恢复 Scraper Studio 作业

> 使用 POST /dca/jobs/{job_id}/resume 重新启动已暂停的 Bright Data Scraper Studio 作业。作业恢复为 running 状态，并返回纯文本响应 OK。

重新启动已暂停的 Bright Data Scraper Studio 作业。作业将继续处理其余输入，并恢复为 `running` 状态。

该端点不接受请求体，成功时返回纯文本响应体 `OK`，而非 JSON。请按文本读取响应，不要对其调用 JSON 解析器。

<Note>
  恢复操作仅对处于 `paused` 状态的作业有效，即通过[暂停 Scraper Studio 作业](/cn/api-reference/scraper-studio-api/pause-job)停止的作业。已取消的作业无法恢复，已完成的作业同样无法恢复。
</Note>

## 作业状态行为

| 操作 | 使用场景          | 结果              |
| -- | ------------- | --------------- |
| 暂停 | 需要临时停止正在运行的作业 | 作业转为 `paused`   |
| 恢复 | 需要继续已暂停的作业    | 作业恢复为 `running` |
| 取消 | 需要永久停止作业      | 作业转为 `canceled` |

已完成的作业无法暂停、恢复或取消。

## 如何查找作业 ID

使用作业列表端点查找您要恢复的作业 ID：

```bash theme={null}
curl "https://api.brightdata.com/dca/collector/jobs?from_date=2026-06-01&to_date=2026-07-13" \
  -H "Authorization: Bearer $BRIGHT_DATA_API_TOKEN"
```

将返回的 `id` 值用作 `job_id` 路径参数。完整参数列表请参见[列出 Scraper Studio 作业](/cn/api-reference/scraper-studio-api/list-jobs)。

## 何时使用该端点

* 在目标网站恢复稳定后，继续此前因网站故障而暂停的批量作业
* 在维护窗口结束时重新启动已暂停的作业
* 针对封锁问题调整国家、会话或并发设置后恢复作业

## 相关

* [暂停 Scraper Studio 作业](/cn/api-reference/scraper-studio-api/pause-job)：将作业置为 `paused` 状态的端点
* [取消 Scraper Studio 作业](/cn/api-reference/scraper-studio-api/cancel-job)：永久停止已暂停的作业，而非恢复它
* [列出 Scraper Studio 作业](/cn/api-reference/scraper-studio-api/list-jobs)：查找传入该端点的 `job_id`
* [IDE 作业数据 API](/cn/api-reference/scraper-studio-api/job-data)：确认作业已恢复为 `running`


## OpenAPI

````yaml api-reference/web-scraper-ide-rest-api POST /dca/jobs/{job_id}/resume
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
  /dca/jobs/{job_id}/resume:
    post:
      summary: Resume a Scraper Studio job
      description: >-
        Resumes an existing Bright Data Scraper Studio job. The job moves to
        `running`. Completed jobs cannot be paused, resumed or canceled. Find
        the `job_id` with the `GET /dca/collector/jobs` endpoint.
      operationId: resumeScraperStudioJob
      parameters:
        - name: job_id
          in: path
          required: true
          description: ID of the job to resume
          schema:
            type: string
          example: j_ma13y9ay1piehrso8r
      responses:
        '200':
          description: Job resumed successfully
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