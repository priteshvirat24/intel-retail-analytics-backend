> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Pause a Scraper Studio job

> POST /dca/jobs/{job_id}/pause temporarily stops a running Bright Data Scraper Studio job. The job moves to paused and returns the plain text response OK.

Temporarily stop a running Bright Data Scraper Studio job. The job stops processing new inputs and moves to `paused`, and you can restart it later with [Resume a Scraper Studio job](./resume-job).

This endpoint takes no request body and returns the plain text body `OK` on success, not JSON. Read the response as text rather than calling a JSON parser on it.

## Job state behavior

| Action | Use when                                   | Result                      |
| ------ | ------------------------------------------ | --------------------------- |
| Pause  | You want to temporarily stop a running job | Job moves to `paused`       |
| Resume | You want to continue a paused job          | Job moves back to `running` |
| Cancel | You want to stop a job permanently         | Job moves to `canceled`     |

Completed jobs cannot be paused, resumed or canceled.

## How to find a job ID

Use the jobs list endpoint to find the ID of the job you want to pause:

```bash theme={null}
curl "https://api.brightdata.com/dca/collector/jobs?from_date=2026-06-01&to_date=2026-07-13" \
  -H "Authorization: Bearer $BRIGHT_DATA_API_TOKEN"
```

Use the returned `id` value as the `job_id` path parameter. See [List Scraper Studio jobs](./list-jobs) for the full parameter list.

## When to use this endpoint

* Hold a large batch during a target site incident, then resume once the site recovers
* Free concurrency for higher-priority work during a maintenance window
* Stop a job that is returning a high rate of `blocked` or `detect_block` errors while you adjust country, session or rate settings

To stop a job permanently instead, use [Cancel a Scraper Studio job](./cancel-job).

## Related

* [Resume a Scraper Studio job](./resume-job): restart a job paused with this endpoint
* [Cancel a Scraper Studio job](./cancel-job): stop a job permanently instead of temporarily
* [List Scraper Studio jobs](./list-jobs): find the `job_id` to pass to this endpoint
* [Get job metadata](./job-data): confirm the job status after pausing


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