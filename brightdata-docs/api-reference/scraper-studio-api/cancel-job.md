> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cancel a Scraper Studio job

> POST /dca/jobs/{job_id}/cancel permanently stops a Bright Data Scraper Studio job. The job moves to canceled and cannot be resumed afterward.

Permanently stop a Bright Data Scraper Studio job. The job moves to `canceled` and stops processing its remaining inputs.

This endpoint takes no request body and returns the plain text body `OK` on success, not JSON. Read the response as text rather than calling a JSON parser on it.

<Warning>
  Canceling is permanent. A canceled job cannot be resumed. Data already collected may still be available, depending on the run status and delivery settings. To stop a job temporarily instead, use [Pause a Scraper Studio job](./pause-job).
</Warning>

## Job state behavior

| Action | Use when                                   | Result                      |
| ------ | ------------------------------------------ | --------------------------- |
| Pause  | You want to temporarily stop a running job | Job moves to `paused`       |
| Resume | You want to continue a paused job          | Job moves back to `running` |
| Cancel | You want to stop a job permanently         | Job moves to `canceled`     |

Completed jobs cannot be paused, resumed or canceled.

## How to find a job ID

Use the jobs list endpoint to find the ID of the job you want to cancel:

```bash theme={null}
curl "https://api.brightdata.com/dca/collector/jobs?from_date=2026-06-01&to_date=2026-07-13" \
  -H "Authorization: Bearer $BRIGHT_DATA_API_TOKEN"
```

Use the returned `id` value as the `job_id` path parameter. See [List Scraper Studio jobs](./list-jobs) for the full parameter list.

## When to use this endpoint

* Stop a job triggered with the wrong input set instead of paying for the full run
* Cancel a runaway job generating far more child pages than expected, rather than waiting for a `too_many_pages` error
* Clear a stuck job before triggering a corrected run of the same scraper

Pages that were still queued when the job was canceled report the `aborted_page` error code. See [Scraper Studio error codes](/datasets/scraper-studio/error-codes) for the full catalog.

## Related

* [Pause a Scraper Studio job](./pause-job): stop a job temporarily instead of permanently
* [Resume a Scraper Studio job](./resume-job): restart a paused job, which is not possible after canceling
* [Get job metadata](./job-data): confirm the job status after canceling
* [Trigger async batch collection](./Trigger_a_scraper_for_batch_collection_method): start a corrected run


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