> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 删除 Scraper Studio 爬虫

> 使用 DELETE /dca/collector/{scraper_id} 从您的 Bright Data 账户中删除 Scraper Studio 爬虫，删除后爬虫将从 My Scrapers 中移除且无法再运行。

使用 `DELETE /dca/collector/{scraper_id}` 从您的账户中删除 Bright Data Scraper Studio 爬虫。删除爬虫会将其从 My Scrapers 中移除，并阻止新的手动、定时或 API 触发的运行。

该端点不接受请求体，成功时返回纯文本响应体 `OK`，而非 JSON。请按文本读取响应，不要对其调用 JSON 解析器。

<Warning>
  删除爬虫的操作无法撤销。请仅在不再需要该爬虫时使用此端点。
</Warning>

## 如何查找爬虫 ID

使用爬虫列表端点查找您要删除的爬虫 ID：

```bash theme={null}
curl "https://api.brightdata.com/dca/collectors_list" \
  -H "Authorization: Bearer $BRIGHT_DATA_API_TOKEN"
```

将返回的 `id` 值用作 `scraper_id` 路径参数。在 API 参数中，该 ID 有时也称为 `collector_id`。完整参数列表请参见[列出 Scraper Studio 爬虫](/cn/api-reference/scraper-studio-api/list-scrapers)。

## 记录删除原因

通过可选的 `reason` 查询参数记录删除爬虫的原因，用于跟踪或审计：

```bash theme={null}
curl -X DELETE "https://api.brightdata.com/dca/collector/c_mnvdqy7w1fyaku0uep?reason=no_longer_needed" \
  -H "Authorization: Bearer $BRIGHT_DATA_API_TOKEN"
```

省略 `reason` 即可在不记录原因的情况下删除爬虫。

## 何时使用该端点

* 移除不再运行的爬虫，使其不再出现在 My Scrapers 中
* 清理在 Scraper Studio 开发过程中创建的测试或重复爬虫
* 在将工作负载迁移到其他爬虫后停用原爬虫

## 相关

* [列出 Scraper Studio 爬虫](/cn/api-reference/scraper-studio-api/list-scrapers)：删除前查找 `scraper_id`
* [列出 Scraper Studio 作业](/cn/api-reference/scraper-studio-api/list-jobs)：查看爬虫已运行的作业
* [取消 Scraper Studio 作业](/cn/api-reference/scraper-studio-api/cancel-job)：停止单个作业而不删除爬虫


## OpenAPI

````yaml api-reference/web-scraper-ide-rest-api DELETE /dca/collector/{scraper_id}
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
  /dca/collector/{scraper_id}:
    delete:
      summary: Delete a Scraper Studio scraper
      description: >-
        Deletes a Scraper Studio scraper from your account. Deleting a scraper
        removes it from My Scrapers and prevents new manual, scheduled or
        API-triggered runs. This action cannot be undone. Find the `scraper_id`
        with the `GET /dca/collectors_list` endpoint.
      operationId: deleteScraperStudioScraper
      parameters:
        - name: scraper_id
          in: path
          required: true
          description: >-
            ID of the Scraper Studio scraper to delete. In API parameters, this
            ID may also be referred to as `collector_id`.
          schema:
            type: string
          example: c_mnvdqy7w1fyaku0uep
        - name: reason
          in: query
          required: false
          description: >-
            Reason for deleting the scraper. Used for tracking or audit
            purposes.
          schema:
            type: string
          example: no_longer_needed
      responses:
        '200':
          description: Scraper deleted successfully
          content:
            text/plain:
              schema:
                type: string
              example: OK
        '401':
          description: API key missing, malformed or revoked
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