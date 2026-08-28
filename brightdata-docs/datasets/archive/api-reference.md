> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Run a search

> Use the Bright Data Marketplace Archive API to run a Search. POST /webarchive/search manages web archive snapshots; returns 200 OK with JSON status.

`POST /webarchive/search` searches the Bright Data Archive and returns either the full search result object or a `search_id` you poll for status.

<Danger>
  **Every search needs a time range.** The `filters` object is required, and it must carry either `max_age`, or both `min_date` and `max_date`. A request with no `filters` object returns HTTP 400 with `"filters" is required`.
</Danger>

## How to set the search time range

Use `max_age` for a window relative to now. Write it as a number followed by a unit:

| Unit | Meaning | Example |
| ---- | ------- | ------- |
| `h`  | Hours   | `24h`   |
| `d`  | Days    | `7d`    |
| `mo` | Months  | `3mo`   |
| `y`  | Years   | `1y`    |

Bright Data recommends `max_age` of `24h` for a first search, because recent data is delivered fastest.

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

Use `min_date` and `max_date` for a fixed calendar range. Both dates use `YYYY-MM-DD` format and both must be sent together.

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
  Send one form or the other, never both. `max_age` combined with `min_date` and `max_date` in the same request is a conflict, and the results are undefined.
</Warning>

For date ranges older than 24 hours, use `min_date` and `max_date` rather than `max_age`. See [Data range vs delivery time](/datasets/archive/data-range-vs-delivery-time) for how the requested range affects delivery speed.

<Note>
  If the search takes longer than 30 seconds, the response returns only a `search_id` and you should poll the status asynchronously. If the search completes within 30 seconds, the response returns the full search result object (same as `GET /webarchive/search/<search_id>`).
</Note>

<Note>
  You can run up to 100 searches per day without triggering a dump.
  Once you trigger a dump, that search no longer counts against your limit.
</Note>

<Accordion title="LIKE vs Regex Filters">
  * Use LIKE filters (`domain_like_*`, `url_like_*`) for simple pattern matching with `%` (any sequence) and `_` (single character).
  * LIKE patterns are case-insensitive and often faster than regex for simple prefix/suffix matching like `%.com` or `amazon%`.
  * Use regex filters (`domain_regex_*`, `url_regex_*`) for complex patterns requiring full regex syntax. LIKE patterns use backslash escaping: `\%` for literal `%`, `\_` for literal `_`.
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