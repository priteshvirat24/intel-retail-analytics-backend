> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Receive batch data

> Use GET /dca/dataset?id=<collection_id> to fetch results of an async Scraper Studio batch job. Returns a status object while running, a JSON array when ready.

Use `GET /dca/dataset?id=<collection_id>` to retrieve the results of an asynchronous Bright Data Scraper Studio batch collection. While the collection is still running, the endpoint returns a status object. When the collection is ready, it returns a JSON array of records.

For the full trigger, poll and parse walkthrough in cURL, Python and Node.js, see the [Quickstart](./Getting_started_with_the_API).

<Note>
  Use the `collection_id` returned by [POST /dca/trigger](./Trigger_a_scraper_for_batch_collection_method) as the `id` query parameter in this endpoint.
</Note>

<Note>
  Batch collection results are available for download for 16 days after collection. To avoid expiration, download the data within 16 days or configure a [push delivery method](./Choose_a_delivery_type_on_request_level) to send it to your storage automatically.
</Note>

## Request

<CodeGroup>
  ```bash cURL theme={null}
  curl "https://api.brightdata.com/dca/dataset?id=$COLLECTION_ID" \
    -H "Authorization: Bearer $BRIGHT_DATA_API_TOKEN"
  ```

  ```python Python theme={null}
  response = requests.get(
      "https://api.brightdata.com/dca/dataset",
      params={"id": collection_id},
      headers={"Authorization": f"Bearer {API_TOKEN}"},
  )
  ```

  ```js Node.js theme={null}
  const response = await fetch(
    `https://api.brightdata.com/dca/dataset?id=${collectionId}`,
    { headers: { Authorization: `Bearer ${process.env.BRIGHT_DATA_API_TOKEN}` } }
  );
  ```
</CodeGroup>

## Response

While the collection is still building (HTTP 202):

```json theme={null}
{
  "status": "building",
  "message": "Dataset is not ready yet, try again in XXs"
}
```

When the collection is ready (HTTP 200):

```json theme={null}
[
  {
    "url": "https://www.dm.de/p/d/3133774/babylove-teller-silikon-mit-trennschale-regenbogen-orange-creme",
    "title": "babylove Teller Silikon mit Trennschale Regenbogen orange/creme",
    "price": 8.45,
    "availability": "in stock",
    "input": {
      "url": "https://www.dm.de/p/d/3133774/babylove-teller-silikon-mit-trennschale-regenbogen-orange-creme"
    }
  }
]
```

The exact field set depends on the output schema you defined when you built the collector. One row per successful input by default.

## Retrieving results

While the collection is still running, the endpoint returns `202 Accepted` with a status object. When the collection is ready, it returns `200 OK` with a JSON array of records.

For long-running collections, which can take minutes or hours, avoid frequent polling. Use one of these options instead:

* Check the collection status periodically with longer intervals.
* Configure a [push delivery method](./Choose_a_delivery_type_on_request_level), such as webhook, Amazon S3, Google Cloud Storage, Azure Blob Storage, SFTP/FTP or email.
* Use the [dashboard](https://brightdata.com/cp/scrapers) to monitor run progress.

Batch collection results are retained for 16 days. Download the data within the retention window or configure push delivery to store results automatically.

The [Node.js](https://github.com/brightdata/bright-data-scraper-studio-nodejs-project/blob/main/index.js) and [Python](https://github.com/brightdata/bright-data-scraper-studio-python-project/blob/main/index.py) starters implement status checks with exponential-backoff retry on transient errors.

## Errors

| Status             | Cause                                                              | Fix                                                                             |
| ------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| `401 Unauthorized` | Token missing, malformed or revoked                                | Re-copy from [Account Settings → API Tokens](https://brightdata.com/cp/setting) |
| `404 Not Found`    | Collection ID does not exist, was deleted or has expired (16 days) | Re-trigger the collector if the data is still needed                            |
| `[]` (empty array) | Collection completed but produced no rows                          | Check the input URLs and the collector's output schema                          |
| `5xx`              | Transient Bright Data API error                                    | Retry with exponential backoff, for example 1s, 2s, 4s                          |

## Related

* [Trigger async batch collection](./Trigger_a_scraper_for_batch_collection_method): the endpoint that creates the collection
* [Job data](./job-data): job-level metadata (status, page counts, error counts)
* [Get errors for a job](./get-errors-for-job): per-input error details
* [Choose a delivery type](./Choose_a_delivery_type_on_request_level): alternative to polling (webhook, S3, GCS, etc.)


## OpenAPI

````yaml api-reference/web-scraper-ide-rest-api GET /dca/dataset
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
  /dca/dataset:
    get:
      description: >-
        Retrieve the results of an asynchronous Scraper Studio batch collection.


        While the collection is still running, the endpoint returns `202
        Accepted` with a status object. When the collection is ready, it returns
        `200 OK` with a JSON array of records. Use the `collection_id` returned
        by [POST
        /dca/trigger](/api-reference/scraper-studio-api/Trigger_a_scraper_for_batch_collection_method)
        as the `id` query parameter.
      parameters:
        - name: id
          in: query
          required: true
          schema:
            type: string
            example: j_abc123def456
          description: >-
            Collection ID returned by `POST /dca/trigger`. Use this value as the
            `id` query parameter.
      responses:
        '200':
          description: Dataset (Ready)
          content:
            application/json:
              examples:
                response:
                  value:
                    - Image: https://targetwebsite.com/product_id.png
                      Title: product_name
                      Price: product_price
                      input:
                        url: https://targetwebsite.com/product_id/
        '202':
          description: Waiting for Dataset
          content:
            application/json:
              examples:
                response:
                  value:
                    status: building
                    message: Dataset is not ready yet, try again in XXs
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