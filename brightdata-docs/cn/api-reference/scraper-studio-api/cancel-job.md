> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 取消 Scraper Studio 作业

> 使用 POST /dca/jobs/{job_id}/cancel 永久停止 Bright Data Scraper Studio 作业。作业转为 canceled 状态，之后无法恢复。

永久停止 Bright Data Scraper Studio 作业。作业将转为 `canceled` 状态并停止处理其余输入。

该端点不接受请求体，成功时返回纯文本响应体 `OK`，而非 JSON。请按文本读取响应，不要对其调用 JSON 解析器。

<Warning>
  取消操作是永久性的。已取消的作业无法恢复。已采集的数据可能仍然可用，具体取决于运行状态和交付设置。如需临时停止作业，请使用[暂停 Scraper Studio 作业](/cn/api-reference/scraper-studio-api/pause-job)。
</Warning>

## 作业状态行为

| 操作 | 使用场景          | 结果              |
| -- | ------------- | --------------- |
| 暂停 | 需要临时停止正在运行的作业 | 作业转为 `paused`   |
| 恢复 | 需要继续已暂停的作业    | 作业恢复为 `running` |
| 取消 | 需要永久停止作业      | 作业转为 `canceled` |

已完成的作业无法暂停、恢复或取消。

## 如何查找作业 ID

使用作业列表端点查找您要取消的作业 ID：

```bash theme={null}
curl "https://api.brightdata.com/dca/collector/jobs?from_date=2026-06-01&to_date=2026-07-13" \
  -H "Authorization: Bearer $BRIGHT_DATA_API_TOKEN"
```

将返回的 `id` 值用作 `job_id` 路径参数。完整参数列表请参见[列出 Scraper Studio 作业](/cn/api-reference/scraper-studio-api/list-jobs)。

## 何时使用该端点

* 停止使用错误输入集触发的作业，避免为整次运行付费
* 取消生成的子页面远超预期的失控作业，无需等待出现 `too_many_pages` 错误
* 在重新触发同一爬虫的修正运行之前清除卡住的作业

作业被取消时仍在队列中的页面会报告 `aborted_page` 错误代码。完整目录请参见 [Scraper Studio 错误代码](/cn/datasets/scraper-studio/error-codes)。

## 相关

* [暂停 Scraper Studio 作业](/cn/api-reference/scraper-studio-api/pause-job)：临时停止作业，而非永久停止
* [恢复 Scraper Studio 作业](/cn/api-reference/scraper-studio-api/resume-job)：重新启动已暂停的作业，取消后则无法执行此操作
* [IDE 作业数据 API](/cn/api-reference/scraper-studio-api/job-data)：取消后确认作业状态
* [异步触发爬虫进行批量采集](/cn/api-reference/scraper-studio-api/Trigger_a_scraper_for_batch_collection_method)：启动修正后的运行


## OpenAPI

````yaml api-reference/web-scraper-ide-rest-api POST /dca/jobs/{job_id}/cancel
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
  /dca/jobs/{job_id}/cancel:
    post:
      summary: Cancel a Scraper Studio job
      description: >-
        Cancels an existing Bright Data Scraper Studio job. The job moves to
        `canceled`. Canceling is permanent and a canceled job cannot be resumed.
        Completed jobs cannot be paused, resumed or canceled. Find the `job_id`
        with the `GET /dca/collector/jobs` endpoint.
      operationId: cancelScraperStudioJob
      parameters:
        - name: job_id
          in: path
          required: true
          description: ID of the job to cancel
          schema:
            type: string
          example: j_ma13y9ay1piehrso8r
      responses:
        '200':
          description: Job canceled successfully
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