> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a Scraper Studio scraper

> DELETE /dca/collector/{scraper_id} removes a Scraper Studio scraper from your Bright Data account, taking it out of My Scrapers and preventing future runs.

Use `DELETE /dca/collector/{scraper_id}` to delete a Bright Data Scraper Studio scraper from your account. Deleting a scraper removes it from My Scrapers and prevents new manual, scheduled or API-triggered runs.

This endpoint takes no request body and returns the plain text body `OK` on success, not JSON. Read the response as text rather than calling a JSON parser on it.

<Warning>
  Deleting a scraper cannot be undone. Use this endpoint only when the scraper is no longer needed.
</Warning>

## How to find a scraper ID

Use the scrapers list endpoint to find the ID of the scraper you want to delete:

```bash theme={null}
curl "https://api.brightdata.com/dca/collectors_list" \
  -H "Authorization: Bearer $BRIGHT_DATA_API_TOKEN"
```

Use the returned `id` value as the `scraper_id` path parameter. In API parameters, this ID may also be referred to as `collector_id`. See [List Scraper Studio scrapers](./list-scrapers) for the full parameter list.

## Record a deletion reason

Pass the optional `reason` query parameter to record why the scraper was deleted, for tracking or audit purposes:

```bash theme={null}
curl -X DELETE "https://api.brightdata.com/dca/collector/c_mnvdqy7w1fyaku0uep?reason=no_longer_needed" \
  -H "Authorization: Bearer $BRIGHT_DATA_API_TOKEN"
```

Omit `reason` to delete the scraper without recording one.

## When to use this endpoint

* Remove a scraper you no longer run, so it stops appearing in My Scrapers
* Clean up test or duplicate scrapers created while developing in Scraper Studio
* Decommission a scraper after migrating its workload to another scraper

## Related

* [List Scraper Studio scrapers](./list-scrapers): find the `scraper_id` before deleting
* [List Scraper Studio jobs](./list-jobs): review the jobs a scraper has run
* [Cancel a Scraper Studio job](./cancel-job): stop a single job without deleting the scraper


## OpenAPI

````yaml api-reference/web-scraper-ide-rest-api DELETE /dca/collector/{scraper_id}
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
  /dca/collector/{scraper_id}:
    delete:
      summary: Delete a Scraper Studio scraper
      description: >-
        Deletes a Scraper Studio scraper from your account. Deleting a scraper
        removes it from My Scrapers and prevents new manual, scheduled or
        API-triggered runs. This action cannot be undone. Find the `scraper_id`
        with the `GET /dca/collectors_list` endpoint.
      operationId: deleteScraperStudioScraper
      parameters:
        - name: scraper_id
          in: path
          required: true
          description: >-
            ID of the Scraper Studio scraper to delete. In API parameters, this
            ID may also be referred to as `collector_id`.
          schema:
            type: string
          example: c_mnvdqy7w1fyaku0uep
        - name: reason
          in: query
          required: false
          description: >-
            Reason for deleting the scraper. Used for tracking or audit
            purposes.
          schema:
            type: string
          example: no_longer_needed
      responses:
        '200':
          description: Scraper deleted successfully
          content:
            text/plain:
              schema:
                type: string
              example: OK
        '401':
          description: API key missing, malformed or revoked
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