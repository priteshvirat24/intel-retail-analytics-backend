> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get job metadata

> GET /dca/log/{job_id} returns metadata for a Bright Data Scraper Studio job: status, input counts, output line counts, failures and run timestamps.

Retrieve metadata for a [triggered](./Trigger_a_scraper_for_batch_collection_method) Bright Data Scraper Studio job: status, input counts, success and failure counts, page counts and run timestamps. Use this endpoint when you need observability into a job, for example to track how many inputs succeeded, how many failed or how long the job took.

This endpoint returns metadata only. To download the actual scraped data, use [Receive batch data](./Receive_batch_data).

## Request

The `job_id` is the `collection_id` returned by [POST /dca/trigger](./Trigger_a_scraper_for_batch_collection_method).

<CodeGroup>
  ```bash cURL theme={null}
  curl "https://api.brightdata.com/dca/log/$JOB_ID" \
    -H "Authorization: Bearer $BRIGHT_DATA_API_TOKEN"
  ```

  ```python Python theme={null}
  response = requests.get(
      f"https://api.brightdata.com/dca/log/{job_id}",
      headers={"Authorization": f"Bearer {API_TOKEN}"},
  )
  metadata = response.json()
  ```

  ```js Node.js theme={null}
  const response = await fetch(
    `https://api.brightdata.com/dca/log/${jobId}`,
    { headers: { Authorization: `Bearer ${process.env.BRIGHT_DATA_API_TOKEN}` } }
  );
  const metadata = await response.json();
  ```
</CodeGroup>

## Response

```json theme={null}
{
  "id": "j_ma13y9ay1piehrso8r",
  "status": "done",
  "collector": "c_m9im5n7v82p2y35la",
  "template": "t_m9jty150kxgwtzcgi.3",
  "inputs": 1,
  "dup_inputs": 0,
  "lines": 60,
  "fails": 0,
  "pages": 1,
  "pages_left": 0,
  "success": 1,
  "navigations": 2,
  "created": "2025-04-28T13:22:16.857Z",
  "started": "2025-04-28T13:22:17.502Z",
  "finished": "2025-04-28T13:23:28.961Z",
  "trigger": "user@example.com",
  "success_rate": 1,
  "job_time": 71459,
  "queue_time": 645
}
```

Common `status` values: `building`, `running`, `done`, `failed`, `cancelled`.

## When to use this endpoint

* Track job progress for a dashboard or monitor
* Read the success rate directly from `success_rate`
* Identify which jobs deduplicated inputs (`dup_inputs > 0`)
* Read job duration directly from `job_time` (milliseconds), and queue wait from `queue_time`

For the actual scraped records, see [Receive batch data](./Receive_batch_data). For per-input error details, see [Get errors for a job](./get-errors-for-job).

## Errors

| Status             | Cause                                | Fix                                                                             |
| ------------------ | ------------------------------------ | ------------------------------------------------------------------------------- |
| `401 Unauthorized` | Token missing, malformed or revoked  | Re-copy from [Account Settings → API Tokens](https://brightdata.com/cp/setting) |
| `404 Not Found`    | Job ID does not exist or has expired | Confirm the ID matches a recent `collection_id` from `/dca/trigger`             |
| `5xx`              | Transient Bright Data API error      | Retry with exponential backoff, for example 1s, 2s, 4s                          |

## Related

* [Trigger async batch collection](./Trigger_a_scraper_for_batch_collection_method): the endpoint that creates the job
* [Receive batch data](./Receive_batch_data): download the dataset itself, not metadata
* [Get errors for a job](./get-errors-for-job): per-input error details for debugging


## OpenAPI

````yaml api-reference/web-scraper-ide-rest-api GET /dca/log/{job_id}
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
  /dca/log/{job_id}:
    get:
      description: Get job data by job ID
      parameters:
        - name: job_id
          in: path
          required: true
          schema:
            type: string
          description: The ID of the job to retrieve.
      responses:
        '200':
          description: OK
          content:
            application/json:
              examples:
                response:
                  value:
                    id: j_ma13y9ay1piehrso8r
                    status: done
                    collector: c_m9im5n7v82p2y35la
                    template: t_m9jty150kxgwtzcgi.3
                    inputs: 1
                    dup_inputs: 0
                    lines: 60
                    fails: 0
                    pages: 1
                    pages_left: 0
                    success: 1
                    navigations: 2
                    created: '2025-04-28T13:22:16.857Z'
                    started: '2025-04-28T13:22:17.502Z'
                    finished: '2025-04-28T13:23:28.961Z'
                    trigger: user@example.com
                    success_rate: 1
                    job_time: 71459
                    queue_time: 645
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