> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Trigger async batch collection

> Use POST /dca/trigger to start an async batch collection for a Scraper Studio collector. Send a JSON array of inputs; returns a collection_id to fetch results.

Use `POST /dca/trigger` to start an asynchronous batch collection for a published Bright Data Scraper Studio collector. The request body is a JSON array of input objects, and each object must match the collector's input schema.

The endpoint returns a `collection_id` immediately. Use that ID with the [Receive batch data](./Receive_batch_data) endpoint (`GET /dca/dataset`) to retrieve the results when the collection is complete.

For the full happy-path walkthrough (auth, trigger, poll, parse) in cURL, Python and Node.js, see the [Quickstart](./Getting_started_with_the_API). This page is the parameter and error reference.

## Request

The request body is a JSON array of input objects. Each object must match the input schema defined for the collector in [Scraper Studio](https://brightdata.com/cp/scrapers). A URL-based collector may require a `url` field, while other collectors may require fields such as `keyword`, `location`, `country` or custom input fields.

The body must be a JSON array. For a single input, send an array with one object.

<CodeGroup>
  ```bash cURL theme={null}
  curl --request POST \
    --url 'https://api.brightdata.com/dca/trigger?collector=YOUR_COLLECTOR_ID&queue_next=1' \
    --header 'Authorization: Bearer YOUR_API_KEY' \
    --header 'Content-Type: application/json' \
    --data '[
      { "url": "https://example.com/product/1" },
      { "url": "https://example.com/product/2" }
    ]'
  ```

  ```python Python theme={null}
  import os, requests

  response = requests.post(
      "https://api.brightdata.com/dca/trigger",
      params={"collector": os.environ["BRIGHT_DATA_COLLECTOR_ID"], "queue_next": 1},
      headers={
          "Authorization": f"Bearer {os.environ['BRIGHT_DATA_API_TOKEN']}",
          "Content-Type": "application/json",
      },
      json=[
          {"url": "https://example.com/product/1"},
          {"url": "https://example.com/product/2"},
      ],
  )
  collection_id = response.json()["collection_id"]
  ```

  ```js Node.js theme={null}
  const url = new URL("https://api.brightdata.com/dca/trigger");
  url.searchParams.set("collector", process.env.BRIGHT_DATA_COLLECTOR_ID);
  url.searchParams.set("queue_next", "1");

  const response = await fetch(url, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${process.env.BRIGHT_DATA_API_TOKEN}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify([
      { url: "https://example.com/product/1" },
      { url: "https://example.com/product/2" },
    ]),
  });
  const { collection_id } = await response.json();
  ```
</CodeGroup>

## Response

```json theme={null}
{
  "collection_id": "j_abc123def456",
  "start_eta": "2026-05-22T13:26:22.702Z"
}
```

The `collection_id` identifies this collection run. Use it as the `id` value when calling `GET /dca/dataset` to retrieve the results.

```bash theme={null}
curl --request GET \
  --url 'https://api.brightdata.com/dca/dataset?id=j_abc123def456' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

| Field           | Type   | Description                                                                           |
| --------------- | ------ | ------------------------------------------------------------------------------------- |
| `collection_id` | string | ID of the collection run. Use this value to retrieve results from `GET /dca/dataset`. |
| `start_eta`     | string | Estimated start time for the collection, in ISO 8601 format.                          |

See the [Quickstart](./Getting_started_with_the_API#what-do-the-ids-mean) for how the IDs relate to one another.

## Send a notification when a collection finishes

Use the `notify` query parameter to send a webhook or email notification when a batch collection finishes. The parameter accepts a JSON object passed as a URL query parameter, so the value must be URL-encoded. When `notify` is used without `deliver`, the notification is sent when the collection job completes.

The following cURL example triggers a batch collection and sends a webhook notification when the job completes. The `--url-query` option, available since curl 7.87.0, URL-encodes the JSON value for you:

```bash theme={null}
curl --request POST "https://api.brightdata.com/dca/trigger" \
  --url-query "collector=YOUR_COLLECTOR_ID" \
  --url-query 'notify={"type":"webhook","endpoint":"https://example.com/webhook"}' \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '[{ "url": "https://example.com/product/1" }]'
```

The response is the standard `collection_id` response shown above. When the collection job completes, Bright Data sends the notification to the configured endpoint.

The `notify` object has the following fields:

| Field      | Type   | Required               | Description                                 |
| ---------- | ------ | ---------------------- | ------------------------------------------- |
| `type`     | string | Yes                    | Notification type: `webhook` or `email`.    |
| `endpoint` | string | Required for `webhook` | Webhook URL that receives the notification. |

## Override delivery settings for one request

Use the `deliver` query parameter to override the scraper's default delivery settings for a specific request. This delivers the collection result to a destination different from the one configured under **Delivery preferences** in the control panel, without changing the scraper configuration. Like `notify`, the parameter accepts a JSON object passed as a URL-encoded query parameter.

The following example triggers a batch collection, delivers the result to Amazon S3 and sends a webhook notification after delivery completes:

```bash theme={null}
COLLECTOR=YOUR_COLLECTOR_ID

DELIVER='{
  "type": "s3",
  "bucket": "YOUR_BUCKET",
  "credentials": {
    "aws-access-key": "YOUR_AWS_ACCESS_KEY",
    "aws-secret-key": "YOUR_AWS_SECRET_KEY"
  },
  "region": "YOUR_REGION",
  "directory": "brightdata/YOUR_DIRECTORY",
  "filename": {
    "template": "results_{[datetime]}",
    "extension": "json"
  },
  "delivery_type": "deliver_results"
}'

NOTIFY='{
  "type": "webhook",
  "endpoint": "https://example.com/webhook"
}'

curl --request POST "https://api.brightdata.com/dca/trigger" \
  --url-query "collector=$COLLECTOR" \
  --url-query "deliver=$DELIVER" \
  --url-query "notify=$NOTIFY" \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '[{ "url": "https://example.com/product/1" }]'
```

The `deliver` object supports the same destination types as **Delivery preferences**, including `s3`, `gcs`, `azure`, `sftp`, `webhook`, `snowflake` and `email`.

## How notify and deliver interact

| Configuration                  | Behavior                                                                                                               |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| Neither `notify` nor `deliver` | Uses the scraper's default delivery settings. No request-level notification is sent.                                   |
| `notify` only                  | Sends a notification when the collection job completes.                                                                |
| `deliver` only                 | Delivers the result using the request-level delivery configuration.                                                    |
| `deliver` and `notify`         | Delivers the result using the request-level delivery configuration, then sends a notification when delivery completes. |

## When to use batch collection

Use batch collection (`POST /dca/trigger`) when:

* You need to process multiple inputs in one run.
* You can wait until the collection finishes before receiving results.
* You want to retrieve results later by `collection_id`.
* You are building a dataset or a scheduled collection workflow.

Use [real-time collection](./initiate-a-realtime-job/sync-realtime-job) when you need a result for a single input immediately or within a short request window.

## Errors

| Status                     | Cause                                                                      | Fix                                                                                           |
| -------------------------- | -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `401 Unauthorized`         | Token missing, malformed or revoked                                        | Re-copy from [Account Settings → API Tokens](https://brightdata.com/cp/setting)               |
| `404 Not Found`            | Collector ID does not exist or your account does not have access           | Open the collector in [Scraper Studio](https://brightdata.com/cp/scrapers) and re-copy the ID |
| `422 Unprocessable Entity` | The objects in your request body do not match the collector's input schema | Confirm field names against the **Inputs** tab of your collector                              |
| `5xx`                      | Transient Bright Data API error                                            | Retry with exponential backoff, for example 1s, 2s, 4s                                        |

## Retry behavior

Re-triggering the same inputs creates a new collection with a new `collection_id`. The endpoint is not idempotent and does not deduplicate inputs across runs. To retry only the failed inputs, use [Get errors for a job](./get-errors-for-job) to identify the failed inputs from the run, then trigger a new collection with only those inputs.

## Related

* [Quickstart](./Getting_started_with_the_API): full trigger, poll and parse walkthrough in cURL, Python and Node.js
* [Receive batch data](./Receive_batch_data): poll for the dataset
* [Choose a delivery type on request level](./Choose_a_delivery_type_on_request_level): collection modes and delivery preference compatibility
* [Node.js starter](https://github.com/brightdata/bright-data-scraper-studio-nodejs-project): production-grade client that calls this endpoint
* [Python starter](https://github.com/brightdata/bright-data-scraper-studio-python-project): same, in Python


## OpenAPI

````yaml api-reference/web-scraper-ide-rest-api POST /dca/trigger
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
  /dca/trigger:
    post:
      description: >-
        Start an asynchronous batch collection for a published Scraper Studio
        collector.


        The request body is a JSON array of input objects, and each object must
        match the input schema defined for the collector. The endpoint returns a
        `collection_id` immediately. Use this ID with [GET
        /dca/dataset](/api-reference/scraper-studio-api/Receive_batch_data) to
        retrieve the results when the collection is complete.


        Use batch collection to process multiple inputs in one run. For a single
        input returned immediately, use the [real-time
        endpoints](/api-reference/scraper-studio-api/initiate-a-realtime-job/sync-realtime-job).
      parameters:
        - name: collector
          in: query
          required: true
          schema:
            type: string
            example: c_abc123
          description: >-
            Collector ID of the Scraper Studio scraper to run. The ID starts
            with `c_`.
        - name: version
          in: query
          schema:
            type: string
          description: Set to `dev` to trigger the development version of the scraper
        - name: name
          in: query
          schema:
            type: string
          description: Human-readable name for the batch collection.
        - name: queue_next
          in: query
          schema:
            type: integer
            default: 1
          description: >-
            If another collection is already running, queue this collection to
            run after it.
        - name: queue
          in: query
          schema:
            type: string
          description: >-
            Queue name used to group related collection runs. Runs that share a
            queue start one after another.
        - name: confirm_cancel
          in: query
          schema:
            type: integer
            default: 1
          description: >-
            Cancels a running collection for this collector and runs this one
            instead.
        - name: no_downloads
          in: query
          schema:
            type: integer
            default: 1
          description: Disables media file downloads for this collection.
        - name: deadline
          in: query
          schema:
            type: string
            example: 1h
          description: >-
            Sets the maximum time the collection can run. When the deadline is
            reached, Bright Data terminates the collection. Use `h` for hours,
            `m` for minutes or `s` for seconds, for example `1h`, `30m` or
            `45s`.
        - name: notify
          in: query
          schema:
            type: string
            example: '{"type":"webhook","endpoint":"https://example.com/webhook"}'
          description: >-
            Notification configuration for this request as a URL-encoded JSON
            object. Used alone, the notification is sent when the collection job
            completes. Used together with `deliver`, the notification is sent
            after delivery completes.
        - name: deliver
          in: query
          schema:
            type: string
            example: >-
              {"type":"s3","bucket":"YOUR_BUCKET","credentials":{"aws-access-key":"YOUR_AWS_ACCESS_KEY","aws-secret-key":"YOUR_AWS_SECRET_KEY"},"region":"YOUR_REGION","directory":"brightdata/YOUR_DIRECTORY","filename":{"template":"results_{[datetime]}","extension":"json"},"delivery_type":"deliver_results"}
          description: >-
            Request-level delivery configuration as a URL-encoded JSON object.
            Overrides the scraper's default Delivery preferences for this
            collection only.
      requestBody:
        required: true
        description: >-
          A JSON array of input objects. Each object must match the input schema
          defined for the collector. A URL-based collector may require a `url`
          field, while other collectors may require fields such as `keyword`,
          `location` or `country`. For a single input, send an array with one
          object.
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                additionalProperties: true
                description: >-
                  Single input object whose fields match the collector input
                  schema.
                properties:
                  url:
                    type: string
                    format: uri
                    description: >-
                      Example field for collectors that take a target URL.
                      Replace with the fields your collector expects.
            examples:
              request:
                value:
                  - url: https://example.com/product/1
                  - url: https://example.com/product/2
      responses:
        '200':
          description: Returns a `collection_id` for the new collection run.
          content:
            application/json:
              schema:
                type: object
                properties:
                  collection_id:
                    type: string
                    description: >-
                      ID of the collection run. Use this value as the `id` when
                      calling GET /dca/dataset to retrieve results.
                  start_eta:
                    type: string
                    description: >-
                      Estimated start time for the collection, in ISO 8601
                      format.
              examples:
                response:
                  value:
                    collection_id: j_abc123def456
                    start_eta: '2026-05-22T13:26:22.702Z'
      x-codeSamples:
        - lang: py
          label: Python SDK
          source: |-
            # Install: pip install brightdata-sdk
            from brightdata import BrightDataClient

            async with BrightDataClient(api_key="YOUR_API_KEY") as client:
                # Trigger an async job, then wait for results
                job = await client.scraper_studio.trigger(
                    "c_abc123", {"url": "https://example.com/product/1"}
                )
                data = await job.wait_and_fetch(timeout=120)
                print(data)
        - lang: js
          label: JavaScript SDK
          source: >-
            // Install: npm install @brightdata/sdk

            import { bdclient } from '@brightdata/sdk';


            const client = new bdclient({ apiKey: 'YOUR_API_KEY' });


            // Trigger an async job, then wait for results

            const job = await
            client.scraperStudio.trigger('c_your_collector_id', {
              url: 'https://example.com/product/1',
            });

            const data = await job.waitAndFetch();


            console.log(data);


            await client.close();
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