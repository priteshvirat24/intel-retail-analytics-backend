> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 运行搜索

> 使用 Bright Data Marketplace Archive API 运行搜索。POST /webarchive/search 管理网页存档快照，返回 200 OK 及 JSON 状态。

`POST /webarchive/search` 搜索 Bright Data Archive，返回完整的搜索结果对象或用于轮询状态的 `search_id`。

<Danger>
  **每次搜索都必须指定时间范围。** `filters` 对象为必填项，其中必须包含 `max_age`，或者同时包含 `min_date` 和 `max_date`。缺少 `filters` 对象的请求会返回 HTTP 400 及 `"filters" is required`。
</Danger>

## 如何设置搜索时间范围

使用 `max_age` 指定相对于当前时间的时间窗口。写法为数字加单位：

| 单位   | 含义 | 示例    |
| ---- | -- | ----- |
| `h`  | 小时 | `24h` |
| `d`  | 天  | `7d`  |
| `mo` | 月  | `3mo` |
| `y`  | 年  | `1y`  |

Bright Data 建议首次搜索时使用 `max_age` = `24h`，因为最新数据的交付速度最快。

```bash theme={null}
curl -X POST https://api.brightdata.com/webarchive/search \
  -H "Authorization: Bearer <YOUR_API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{
    "filters": {
      "max_age": "24h",
      "domain_whitelist": ["example.com"]
    }
  }'
```

使用 `min_date` 和 `max_date` 指定固定的日历范围。两个日期均采用 `YYYY-MM-DD` 格式，且必须同时提供。

```bash theme={null}
curl -X POST https://api.brightdata.com/webarchive/search \
  -H "Authorization: Bearer <YOUR_API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{
    "filters": {
      "min_date": "2026-08-01",
      "max_date": "2026-08-08",
      "domain_whitelist": ["example.com"]
    }
  }'
```

<Warning>
  只能使用其中一种方式，不能同时使用。在同一请求中将 `max_age` 与 `min_date`、`max_date` 一起发送属于冲突，结果不确定。
</Warning>

对于早于 24 小时的日期范围，请使用 `min_date` 和 `max_date`，而不是 `max_age`。有关请求范围如何影响交付速度，请参阅[数据范围与交付时间](/cn/datasets/archive/data-range-vs-delivery-time)。

<Note>
  如果搜索耗时超过 30 秒，响应将仅返回 `search_id`，您应该异步轮询状态。如果搜索在 30 秒内完成，响应将返回完整的搜索结果对象（与 `GET /webarchive/search/<search_id>` 相同）。
</Note>

<Note>
  您每天可以运行最多 100 次搜索而不触发转储。
  触发转储后，该搜索将不再计入您的限制。
</Note>

<Accordion title="LIKE 与正则表达式过滤器">
  * 对于简单的模式匹配，使用 LIKE 过滤器（`domain_like_*`、`url_like_*`），其中 `%` 表示任意序列，`_` 表示单个字符。
  * LIKE 模式不区分大小写，对于简单的前缀/后缀匹配（如 `%.com` 或 `amazon%`）通常比正则表达式更快。
  * 对于需要完整正则表达式语法的复杂模式，使用正则表达式过滤器（`domain_regex_*`、`url_regex_*`）。LIKE 模式使用反斜杠转义：`\%` 表示字面上的 `%`，`\_` 表示字面上的 `_`。
</Accordion>


## OpenAPI

````yaml api-reference/web-archive-api POST /webarchive/search
openapi: 3.1.0
info:
  title: BrightData Web Archive API
  version: 1.0.0
  description: API to search and retrieve archived web pages.
servers:
  - url: https://api.brightdata.com
security:
  - bearerAuth: []
paths:
  /webarchive/search:
    post:
      summary: Run a search
      description: >-
        To initiate a search of our Archive, use the following `/search`
        endpoint.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                filters:
                  type: object
                  description: >-
                    Filters that scope the search. The `filters` object is
                    required, and it must carry a time range: either `max_age`,
                    or both `min_date` and `max_date`.
                  properties:
                    max_age:
                      type: string
                      description: >-
                        Limits results to records collected within a relative
                        time window, written as a number followed by a unit: `h`
                        (hours), `d` (days), `mo` (months) or `y` (years). For
                        example `24h`, `7d`, `3mo`, `1y`. 


                        > **Time range is mandatory**: send either `max_age`, or
                        both `min_date` and `max_date`.
                      example: 24h
                    min_date:
                      description: >-
                        Returns records collected on or after the specified
                        date, in `YYYY-MM-DD` format. Must be sent together with
                        `max_date`. 


                        > **Time range is mandatory**: send either `max_age`, or
                        both `min_date` and `max_date`.
                      type: string
                      format: date
                      example: '2026-08-01'
                    max_date:
                      description: >-
                        Returns records collected on or before the specified
                        date, in `YYYY-MM-DD` format. Must be sent together with
                        `min_date`. 


                        > **Time range is mandatory**: send either `max_age`, or
                        both `min_date` and `max_date`.
                      type: string
                      format: date
                      example: '2026-08-08'
                    domain_whitelist:
                      description: >-
                        Includes results only from listed domains. 


                        > **Tip**:  Either use `domain_whitelist` OR
                        `domain_blacklist` for best results.
                      type: array
                      items:
                        type: string
                    domain_blacklist:
                      description: >-
                        Excludes results from listed domains. 


                        > **Tip**:  Either use `domain_whitelist` OR
                        `domain_blacklist` for best results.
                      type: array
                      items:
                        type: string
                    domain_regex_whitelist:
                      description: >-
                        Includes results only matching the specified domain
                        regex pattern.
                      type: array
                      items:
                        type: string
                    domain_regex_blacklist:
                      description: >-
                        Excludes results matching the specified domain regex
                        pattern.
                      type: array
                      items:
                        type: string
                    domain_like_whitelist:
                      description: >-
                        Includes domains matching LIKE pattern (% = any chars, _
                        = single char). Case-insensitive.
                      type: array
                      items:
                        type: string
                    domain_like_blacklist:
                      description: >-
                        Excludes domains matching LIKE pattern.
                        Case-insensitive.
                      type: array
                      items:
                        type: string
                    category_whitelist:
                      description: Includes results only from specified categories.
                      type: array
                      items:
                        type: string
                        enum:
                          - Ads
                          - Application Stores
                          - Artificial Intelligence
                          - Auctions
                          - Business and Economy
                          - Computer and Internet Info
                          - Content Delivery Networks
                          - Cryptocurrency News
                          - Entertainment and Arts
                          - Events/Tickets
                          - Financial Services
                          - Health and Medicine
                          - Home and Garden
                          - Internet Communications and Telephony
                          - Internet Portals
                          - Job Search
                          - Motor Vehicles
                          - News
                          - Personal Sites and Blogs
                          - Philosophy and Political Advocacy
                          - Real Estate
                          - Reference and Research
                          - Search Engines
                          - Shopping
                          - Social Networking
                          - Society
                          - Tracking Sites
                          - Travel
                          - Weapons
                          - Web Hosting
                          - Web Management Services
                    category_blacklist:
                      description: Excludes results from specified categories.
                      type: array
                      items:
                        type: string
                        enum:
                          - Ads
                          - Application Stores
                          - Artificial Intelligence
                          - Auctions
                          - Business and Economy
                          - Computer and Internet Info
                          - Content Delivery Networks
                          - Cryptocurrency News
                          - Entertainment and Arts
                          - Events/Tickets
                          - Financial Services
                          - Health and Medicine
                          - Home and Garden
                          - Internet Communications and Telephony
                          - Internet Portals
                          - Job Search
                          - Motor Vehicles
                          - News
                          - Personal Sites and Blogs
                          - Philosophy and Political Advocacy
                          - Real Estate
                          - Reference and Research
                          - Search Engines
                          - Shopping
                          - Social Networking
                          - Society
                          - Tracking Sites
                          - Travel
                          - Weapons
                          - Web Hosting
                          - Web Management Services
                    url_regex_whitelist:
                      description: >-
                        Includes results only matching the specified URL regex
                        pattern.
                      type: array
                      items:
                        type: string
                    url_regex_blacklist:
                      description: >-
                        Excludes results matching the specified URL regex
                        pattern.
                      type: array
                      items:
                        type: string
                    url_like_whitelist:
                      description: >-
                        Includes URLs matching LIKE pattern (% = any chars, _ =
                        single char). Case-insensitive.
                      type: array
                      items:
                        type: string
                    url_like_blacklist:
                      description: Excludes URLs matching LIKE pattern. Case-insensitive.
                      type: array
                      items:
                        type: string
                    language_whitelist:
                      description: >-
                        Includes results only for specific language codes (ISO
                        639-3).
                      type: array
                      items:
                        type: string
                    language_blacklist:
                      description: Excludes results for specific language codes.
                      type: array
                      items:
                        type: string
                    ip_country_whitelist:
                      description: >-
                        Includes results collected through IPs or peers only
                        from specified countries.
                      type: array
                      items:
                        type: string
                    ip_country_blacklist:
                      description: >-
                        Excludes results collected through IPs or peers from
                        specified countries.
                      type: array
                      items:
                        type: string
                    captcha:
                      description: Return only results with captcha triggered
                      type: boolean
                    robots_block:
                      description: Return only results with robots block
                      type: boolean
              required:
                - filters
              example:
                filters:
                  max_age: 24h
                  domain_whitelist:
                    - example.com
                  domain_like_whitelist:
                    - '%.example.%'
                    - example%
                  domain_regex_whitelist:
                    - .*example..*
                  category_whitelist:
                    - Motor Vehicles
                  url_like_whitelist:
                    - '%/products/%'
                    - '%/search%'
                  url_regex_whitelist:
                    - .*/products/.*
                  language_whitelist:
                    - eng
                  ip_country_whitelist:
                    - us
                    - ie
                    - in
                  captcha: true
                  robots_block: true
      responses:
        '200':
          description: Search initiated successfully
          content:
            application/json:
              schema:
                oneOf:
                  - title: Async (Still Running)
                    type: object
                    properties:
                      search_id:
                        type: string
                        description: Returned if search is async
                        example: ucd_abc123xyz
                    example:
                      search_id: ucd_abc123xyz
                  - title: Completed within 30s
                    type: object
                    properties:
                      search_id:
                        type: string
                        description: Unique identifier for the search
                      status:
                        type: string
                        description: 'Current status: `in_progress`, `done`, or `failed`'
                      filters:
                        type: object
                        description: The filters used for this search (echoed back)
                      files_count:
                        type: integer
                        description: Total number of matching files found
                      estimate_batch_count:
                        type: integer
                        description: Estimated number of batches for the dump
                      estimate_batch_size:
                        type: integer
                        description: Estimated total size in bytes
                      dump_cost_usd:
                        type: number
                        format: float
                        description: Estimated total cost to create a dump
                      cost_breakdown:
                        type: object
                        description: Breakdown of costs between cache and archive pages
                        properties:
                          archive_pages_count:
                            type: integer
                          archive_pages_cost:
                            type: number
                            format: float
                          cache_pages_count:
                            type: integer
                          cache_pages_cost:
                            type: number
                            format: float
                      estimate_dump_duration_sec:
                        type: integer
                        description: Estimated time to complete the dump in seconds
                      duration:
                        type: string
                        description: How long the search took to complete
                      error:
                        type: string
                        description: Error message (only present when status is `failed`)
                    example:
                      search_id: ucd_abc123xyz
                      status: done
                      filters:
                        domain_whitelist:
                          - example.com
                          - www.example.com
                        max_age: 1d
                        min_date: '2026-02-05T10:00:00.000Z'
                      files_count: 12341294
                      estimate_batch_count: 130
                      estimate_batch_size: 1073679195
                      dump_cost_usd: 2468.26
                      cost_breakdown:
                        archive_pages_count: 0
                        archive_pages_cost: 0
                        cache_pages_count: 12341294
                        cache_pages_cost: 2468.26
                      estimate_dump_duration_sec: 13000
                      duration: 4s210ms
              examples:
                Async (Still Running):
                  summary: 200 OK (async, search still running)
                  value:
                    search_id: ucd_abc123xyz
                Completed within 30s:
                  summary: 200 OK (completed within 30s)
                  value:
                    search_id: ucd_abc123xyz
                    status: done
                    filters:
                      domain_whitelist:
                        - example.com
                        - www.example.com
                      max_age: 1d
                      min_date: '2026-02-05T10:00:00.000Z'
                    files_count: 12341294
                    estimate_batch_count: 130
                    estimate_batch_size: 1073679195
                    dump_cost_usd: 2468.26
                    cost_breakdown:
                      archive_pages_count: 0
                      archive_pages_cost: 0
                      cache_pages_count: 12341294
                      cache_pages_cost: 2468.26
                    estimate_dump_duration_sec: 13000
                    duration: 4s210ms
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: >-
                      domain_blacklist cannot be used along with
                      domain_whitelist
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