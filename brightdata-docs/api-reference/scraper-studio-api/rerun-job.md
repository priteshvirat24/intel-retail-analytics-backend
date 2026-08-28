> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Rerun a Scraper Studio job

> POST /dca/jobs/{job_id}/rerun starts a new run from an existing Bright Data Scraper Studio job. Rerun everything, or send failed_only to retry failures.

Start a new run from an existing Bright Data Scraper Studio job. Send no request body to rerun the full job from the beginning, or send `failed_only: 1` to rerun only the steps that failed.

A successful request starts a **new** job and returns its `collection_id`. The original job is left untouched.

<Warning>
  Only jobs whose data has not expired can be rerun. Check the job's `expired` timestamp in [List Scraper Studio jobs](./list-jobs) or [Get job metadata](./job-data) before calling this endpoint. If the data has expired, the rerun fails and you must trigger a new job with the original inputs.

  Scraper Studio retains batch collection results for 16 days and real-time results for 7 days. See [Scraper Studio specifications](/datasets/scraper-studio/specifications).
</Warning>

## Rerun behavior

| Request body           | Behavior                                           | Use when                                                               |
| ---------------------- | -------------------------------------------------- | ---------------------------------------------------------------------- |
| No body                | Reruns the full job from the beginning             | You want to collect all inputs again                                   |
| `{ "failed_only": 1 }` | Reruns only the failed steps from the selected job | The job completed with failures and you want to retry just those parts |

## Request

Send the request without a body to rerun everything:

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

Add `failed_only: 1` to retry only the failed steps:

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

## Response

```json theme={null}
{
  "collection_id": "j_mdb7x2kq93nfytra1",
  "start_eta": "2026-07-20T12:10:12.301Z"
}
```

Use the returned `collection_id` as the `job_id` for [Get job metadata](./job-data) and [Receive batch data](./Receive_batch_data). It identifies the new rerun job, not the original one.

## How to find a job ID

Use the jobs list endpoint to find the ID of the job you want to rerun:

```bash theme={null}
curl "https://api.brightdata.com/dca/collector/jobs?from_date=2026-06-01&to_date=2026-07-13" \
  -H "Authorization: Bearer $BRIGHT_DATA_API_TOKEN"
```

Use the returned `id` value as the `job_id` path parameter. See [List Scraper Studio jobs](./list-jobs) for the full parameter list.

## When to use this endpoint

* Retry the failed inputs from a batch after fixing a selector or parser, without recollecting the inputs that already succeeded
* Recollect a full job on a schedule to refresh data that changes over time
* Rerun after a target site incident that caused a burst of `blocked` or `detect_block` errors

To see which inputs failed and why before deciding between a full rerun and `failed_only`, use [Get errors for a job](./get-errors-for-job).

## Related

* [Get errors for a job](./get-errors-for-job): identify which inputs failed before rerunning
* [Get job metadata](./job-data): check the `expired` timestamp and failure count of the original job
* [List Scraper Studio jobs](./list-jobs): find the `job_id` to pass to this endpoint
* [Cancel a Scraper Studio job](./cancel-job): stop a rerun that was started by mistake


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