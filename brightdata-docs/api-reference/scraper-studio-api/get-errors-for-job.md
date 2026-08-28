> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get errors for a job

> GET /dca/jobs/{job_id}/hp_errors returns per-input error details for a Bright Data Scraper Studio batch job. Identify which inputs failed and why.

Retrieve per-input error details for a Bright Data Scraper Studio batch job. Use this endpoint to identify which inputs in a batch failed, what the error code was and how to remediate.

<Note>
  Per the OpenAPI spec, the `job_id` for this endpoint is the one returned by the `/dca/trigger_hp` (high-priority) endpoint. Jobs created via the regular `/dca/trigger` endpoint may use a different error-retrieval path. If the response is empty for a regular trigger job, contact [Bright Data support](https://brightdata.com/contact-us) to confirm the right endpoint for your workflow.
</Note>

## Request

<CodeGroup>
  ```bash cURL theme={null}
  curl "https://api.brightdata.com/dca/jobs/$JOB_ID/hp_errors" \
    -H "Authorization: Bearer $BRIGHT_DATA_API_TOKEN"
  ```

  ```python Python theme={null}
  response = requests.get(
      f"https://api.brightdata.com/dca/jobs/{job_id}/hp_errors",
      headers={"Authorization": f"Bearer {API_TOKEN}"},
  )
  errors = response.json()
  ```

  ```js Node.js theme={null}
  const response = await fetch(
    `https://api.brightdata.com/dca/jobs/${jobId}/hp_errors`,
    { headers: { Authorization: `Bearer ${process.env.BRIGHT_DATA_API_TOKEN}` } }
  );
  const errors = await response.json();
  ```
</CodeGroup>

### Query parameters

| Name             | Type    | Required | Description                                                                                |
| ---------------- | ------- | -------- | ------------------------------------------------------------------------------------------ |
| `skip_normalize` | boolean | No       | When `true`, returns full non-normalized error details. Default returns normalized errors. |

## Errors

| Status            | Cause                                                   | Fix                                                                        |
| ----------------- | ------------------------------------------------------- | -------------------------------------------------------------------------- |
| `400 Bad Request` | Invalid job ID format                                   | Verify the job ID matches the `j_` prefix returned by the trigger endpoint |
| `404 Not Found`   | Job does not exist or your account does not have access | Confirm the job ID is current and from a job you triggered                 |
| `500`             | Internal server error                                   | Retry with exponential backoff, for example 1s, 2s, 4s                     |

## When to use this endpoint

* Build a re-trigger workflow that retries only the failed inputs from a previous batch
* Surface user-actionable error messages in a UI or admin console
* Track failure trends over time (which collectors fail most often, which input shapes cause 422s)

## Related

* [Trigger async batch collection](./Trigger_a_scraper_for_batch_collection_method): the endpoint that creates the job
* [Job data](./job-data): job-level metadata (status, fails count, etc.)
* [Receive batch data](./Receive_batch_data): download the successful records


## OpenAPI

````yaml api-reference/web-scraper-ide-rest-api GET /dca/jobs/{job_id}/hp_errors
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
  /dca/jobs/{job_id}/hp_errors:
    get:
      summary: Get errors for an job
      description: >-
        Retrieves a list of errors generated during execution of an batch
        scraper job. The job ID must be obtained from the `/trigger_hp`
        endpoint. If the `skip_normalize` query parameter is provided, full
        (non-normalized) error details are returned.
      parameters:
        - name: job_id
          in: path
          required: true
          description: Job ID returned from the `/trigger_hp` endpoint
          schema:
            type: string
        - name: skip_normalize
          in: query
          required: false
          description: Return full (non-normalized) error details
          schema:
            type: boolean
      responses:
        '200':
          description: List of errors for the specified job
          content:
            application/json:
              schema:
                type: object
                properties:
                  errors:
                    type: array
                    items:
                      type: object
                      properties:
                        url:
                          type: string
                          description: URL that failed during processing
                        error:
                          type: string
                          description: Error type or reason
                        consumer:
                          type: string
                          description: Internal consumer identifier
              example:
                errors:
                  - url: www.youtube.com/watch?v=GBaFv4O5H7g
                    error: aborted
                    consumer: dca-hp-so-szakh
                  - url: www.youtube.com/watch?v=dVSRDWxlWBg
                    error: aborted
                    consumer: dca-hp-so-sz5zu
                  - url: www.youtube.com/watch?v=1YrOL8ZqR4Q
                    error: aborted
                    consumer: dca-hp-so-sz6ga
        '400':
          description: Invalid job ID supplied
          content:
            text/plain:
              schema:
                type: string
                example: Invalid job ID supplied
        '404':
          description: Job not found
          content:
            text/plain:
              schema:
                type: string
                example: Job not found
        '500':
          description: Internal server error
          content:
            text/plain:
              schema:
                type: string
                example: Internal server error
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