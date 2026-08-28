> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Scraper Studio jobs

> GET /dca/collector/jobs returns the Scraper Studio jobs in your account. Filter by scraper ID and date range, and paginate with offset and limit.

Use `GET /dca/collector/jobs` to retrieve the Bright Data Scraper Studio jobs in your account. Filter the list by scraper ID and date range, and control pagination with `offset` and `limit`.

`from_date` and `to_date` are required. Use a narrower date range for faster responses and easier pagination.

<Note>
  Pass a scraper ID as the `collector` parameter to return only that scraper's jobs. Get scraper IDs from [List Scrapers](./list-scrapers).
</Note>

## Filter, paginate and sort

* **Filter by scraper.** Pass a scraper ID as the `collector` parameter to return only that scraper's jobs. Get IDs from [List Scrapers](./list-scrapers).
* **Paginate.** Use `offset` and `limit` to page through jobs. To retrieve the next page, increase `offset` by the previous `limit`, for example `offset=0&limit=100`, then `offset=100&limit=100`. `limit` must be between 0 and 500.
* **Sort.** Use `sort_asc=1` for ascending order or `sort_asc=-1` for descending order. The default is `-1`.

## When to use this endpoint

* Build a dashboard that lists recent jobs for a scraper across a date range
* Audit job history and compute success rates from `inputs`, `data_lines` and `failed_pages`
* Look up job IDs, then fetch per-job metadata with [Job data](./job-data)
* Spot scrapers that need attention by watching `failed_pages`

## Errors

| Status             | Cause                                         | Fix                                                                             |
| ------------------ | --------------------------------------------- | ------------------------------------------------------------------------------- |
| `400 Bad Request`  | Missing or malformed `from_date` or `to_date` | Send both dates in `YYYY-MM-DD` format                                          |
| `401 Unauthorized` | Token missing, malformed or revoked           | Re-copy from [Account Settings → API Tokens](https://brightdata.com/cp/setting) |
| `5xx`              | Transient Bright Data API error               | Retry with exponential backoff, for example 1s, 2s, 4s                          |

## Related

* [List Scrapers](./list-scrapers): find the scraper `id` to pass as the `collector` parameter
* [Job data](./job-data): job-level metadata for a single job
* [Receive batch data](./Receive_batch_data): download the records a job produced
* [Trigger async batch collection](./Trigger_a_scraper_for_batch_collection_method): the endpoint that creates jobs


## OpenAPI

````yaml api-reference/web-scraper-ide-rest-api GET /dca/collector/jobs
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
  /dca/collector/jobs:
    get:
      summary: List Scraper Studio jobs
      description: >-
        Retrieve a paginated list of Bright Data Scraper Studio jobs for your
        account. `from_date` and `to_date` are required. Filter by scraper ID
        with `collector`, and paginate with `offset` and `limit`.
      parameters:
        - name: from_date
          in: query
          required: true
          schema:
            type: string
            format: date
            example: '2026-06-01'
          description: Start date for the jobs list, in YYYY-MM-DD format.
        - name: to_date
          in: query
          required: true
          schema:
            type: string
            format: date
            example: '2026-07-13'
          description: End date for the jobs list, in YYYY-MM-DD format.
        - name: collector
          in: query
          required: false
          schema:
            type: string
            example: c_example1234567890
          description: >-
            Scraper ID used to filter jobs for a specific scraper. Get IDs from
            the List Scrapers endpoint.
        - name: offset
          in: query
          required: false
          schema:
            type: integer
            default: 0
          description: >-
            Number of jobs to skip before returning results. Used for
            pagination.
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            default: 50
            minimum: 0
            maximum: 500
          description: Maximum number of jobs to return. Must be between 0 and 500.
        - name: sort_asc
          in: query
          required: false
          schema:
            type: integer
            default: -1
            enum:
              - 1
              - -1
          description: >-
            Sort direction. Use 1 for ascending order or -1 for descending
            order.
      responses:
        '200':
          description: A paginated list of Scraper Studio jobs.
          content:
            application/json:
              schema:
                type: object
                properties:
                  total:
                    type: integer
                    description: Total number of jobs matching the request.
                  offset:
                    type: integer
                    description: Zero-based index of the first job returned.
                  limit:
                    type: integer
                    description: Maximum number of jobs returned in the response.
                  data:
                    type: array
                    description: List of job objects.
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          description: Job ID.
                        status:
                          type: string
                          description: >-
                            Current job status, such as running, done, failed or
                            canceled.
                        queued:
                          type: string
                          description: >-
                            Timestamp when the job entered the queue, in ISO
                            8601 format.
                        started:
                          type: string
                          description: Timestamp when the job started, in ISO 8601 format.
                        finished:
                          type: string
                          description: >-
                            Timestamp when the job finished, in ISO 8601 format.
                            Present only for completed jobs.
                        inputs:
                          type: integer
                          description: Number of input rows submitted to the job.
                        page_loads:
                          type: integer
                          description: Number of page loads used by the job.
                        total_pages:
                          type: integer
                          description: >-
                            Total number of pages discovered or processed by the
                            job.
                        failed_pages:
                          type: integer
                          description: Number of pages that failed during the job.
                        data_lines:
                          type: integer
                          description: Number of output records produced by the job.
                        trigger:
                          type: object
                          description: Information about how the job was triggered.
                          properties:
                            type:
                              type: string
                              description: >-
                                Trigger source, such as CP for the control
                                panel.
                            user:
                              type: string
                              description: User or system that triggered the job.
                            ip:
                              type: string
                              description: IP address associated with the trigger request.
                        expired:
                          type: string
                          description: >-
                            Timestamp when the job data expires and is no longer
                            available, in ISO 8601 format.
              examples:
                response:
                  value:
                    total: 3
                    offset: 0
                    limit: 50
                    data:
                      - id: j_example1234567890
                        status: done
                        queued: '2026-07-02T12:21:04.121Z'
                        started: '2026-07-02T12:21:04.387Z'
                        finished: '2026-07-02T12:21:09.566Z'
                        inputs: 1
                        page_loads: 1
                        total_pages: 1
                        failed_pages: 0
                        data_lines: 50
                        trigger:
                          type: CP
                          user: user@example.com
                          ip: 192.0.2.10
                        expired: '2026-07-19T00:00:00.000Z'
                      - id: j_example0987654321
                        status: done
                        queued: '2026-07-02T12:14:17.941Z'
                        started: '2026-07-02T12:14:18.098Z'
                        finished: '2026-07-02T12:14:25.122Z'
                        inputs: 1
                        page_loads: 1
                        total_pages: 1
                        failed_pages: 0
                        data_lines: 50
                        trigger:
                          type: CP
                          user: user@example.com
                          ip: 192.0.2.10
                        expired: '2026-07-19T00:00:00.000Z'
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