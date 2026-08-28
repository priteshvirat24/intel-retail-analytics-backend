> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Resume a Scraper Studio job

> POST /dca/jobs/{job_id}/resume restarts a paused Bright Data Scraper Studio job. The job moves back to running and returns the plain text response OK.

Restart a paused Bright Data Scraper Studio job. The job continues processing its remaining inputs and moves back to `running`.

This endpoint takes no request body and returns the plain text body `OK` on success, not JSON. Read the response as text rather than calling a JSON parser on it.

<Note>
  Resume works only on a job in the `paused` state, which means a job stopped with [Pause a Scraper Studio job](./pause-job). A canceled job cannot be resumed, and neither can a completed one.
</Note>

## Job state behavior

| Action | Use when                                   | Result                      |
| ------ | ------------------------------------------ | --------------------------- |
| Pause  | You want to temporarily stop a running job | Job moves to `paused`       |
| Resume | You want to continue a paused job          | Job moves back to `running` |
| Cancel | You want to stop a job permanently         | Job moves to `canceled`     |

Completed jobs cannot be paused, resumed or canceled.

## How to find a job ID

Use the jobs list endpoint to find the ID of the job you want to resume:

```bash theme={null}
curl "https://api.brightdata.com/dca/collector/jobs?from_date=2026-06-01&to_date=2026-07-13" \
  -H "Authorization: Bearer $BRIGHT_DATA_API_TOKEN"
```

Use the returned `id` value as the `job_id` path parameter. See [List Scraper Studio jobs](./list-jobs) for the full parameter list.

## When to use this endpoint

* Continue a batch you paused during a target site incident, once the site is stable again
* Restart paused jobs at the end of a maintenance window
* Resume after adjusting country, session or concurrency settings in response to blocking

## Related

* [Pause a Scraper Studio job](./pause-job): the endpoint that puts a job into the `paused` state
* [Cancel a Scraper Studio job](./cancel-job): stop a paused job permanently instead of resuming it
* [List Scraper Studio jobs](./list-jobs): find the `job_id` to pass to this endpoint
* [Get job metadata](./job-data): confirm the job returned to `running`


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