> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Scraper Studio scrapers

> GET /dca/collectors_list returns the Scraper Studio scrapers in your account, with each scraper's ID, name, active status, delivery config and output schema.

Use `GET /dca/collectors_list` to retrieve the Bright Data Scraper Studio scrapers available in your account. The response includes scraper IDs, names, active status, delivery configuration, last run time and the output schema when available.

<Note>
  Use this endpoint to discover the scraper `id` values in your account, then pass an `id` as the `collector` parameter when you [trigger a scraper](./Trigger_a_scraper_for_batch_collection_method).
</Note>

## Search scrapers

Use the `search` query parameter to return only scrapers whose name matches a search term, for example `?search=amazon`. Omit `search` to return every scraper in the account.

## When to use this endpoint

* Look up the `id` of a scraper before triggering a batch or real-time job
* Build a picker that lists every scraper in your account
* Audit which scrapers are `active` and which have run before (`last_run`)
* Read the `output_schema` to map returned fields before parsing records

## Errors

| Status             | Cause                               | Fix                                                                             |
| ------------------ | ----------------------------------- | ------------------------------------------------------------------------------- |
| `401 Unauthorized` | Token missing, malformed or revoked | Re-copy from [Account Settings → API Tokens](https://brightdata.com/cp/setting) |
| `5xx`              | Transient Bright Data API error     | Retry with exponential backoff, for example 1s, 2s, 4s                          |

## Related

* [List Jobs](./list-jobs): list the jobs a scraper has run
* [Trigger async batch collection](./Trigger_a_scraper_for_batch_collection_method): pass the scraper `id` as the `collector` parameter
* [Job data](./job-data): job-level metadata for a triggered scraper
* [Receive batch data](./Receive_batch_data): download the records a scraper produced


## OpenAPI

````yaml api-reference/web-scraper-ide-rest-api GET /dca/collectors_list
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
  /dca/collectors_list:
    get:
      summary: List Scraper Studio scrapers
      description: >-
        Retrieve the Bright Data Scraper Studio scrapers in your account. Each
        scraper is returned with its ID, name, active status, delivery
        configuration and output schema. Use the returned `id` as the
        `collector` parameter when triggering a scraper.
      parameters:
        - name: search
          in: query
          required: false
          schema:
            type: string
            example: amazon
          description: Filters the scraper list by the provided search term.
      responses:
        '200':
          description: A paginated list of Scraper Studio scrapers.
          content:
            application/json:
              schema:
                type: object
                properties:
                  total:
                    type: integer
                    description: Total number of scrapers matching the request.
                  offset:
                    type: integer
                    description: Zero-based index of the first scraper returned.
                  limit:
                    type: integer
                    description: Maximum number of scrapers returned in the response.
                  data:
                    type: array
                    description: List of scraper objects.
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          description: >-
                            Scraper ID. Use this value as the collector
                            parameter when triggering a scraper.
                        name:
                          type: string
                          description: Scraper name shown in Scraper Studio.
                        active:
                          type: boolean
                          description: >-
                            Indicates whether the scraper is active and
                            available for production runs.
                        last_run:
                          type: string
                          description: >-
                            Timestamp of the latest run, in ISO 8601 format.
                            Present when the scraper has run before.
                        deliver:
                          type: object
                          description: Delivery configuration for the scraper.
                          properties:
                            type:
                              type: string
                              description: Delivery type, such as api_pull.
                        output_schema:
                          type:
                            - object
                            - 'null'
                          description: >-
                            Output schema configured for the scraper. Can be
                            null if no output schema is available.
                          properties:
                            type:
                              type: string
                              description: Schema root type, usually object.
                            fields:
                              type: object
                              description: >-
                                Field definitions returned by the scraper, keyed
                                by field name.
                              additionalProperties:
                                type: object
                                properties:
                                  type:
                                    type: string
                                    description: >-
                                      Field type, such as text, number, price,
                                      url, array, input, error or warning.
                                  active:
                                    type: boolean
                                    description: >-
                                      Indicates whether the field is active in
                                      the scraper output.
                                  items:
                                    type: object
                                    description: Item definition for array fields.
              examples:
                response:
                  value:
                    total: 5
                    offset: 0
                    limit: 50
                    data:
                      - id: c_example1234567890
                        name: example.com
                        active: false
                        deliver:
                          type: api_pull
                        output_schema: null
                      - id: c_example0987654321
                        name: example.com
                        active: true
                        last_run: '2026-06-22T11:41:56.660Z'
                        deliver:
                          type: api_pull
                        output_schema:
                          type: object
                          fields:
                            product_title:
                              type: text
                              active: true
                            brand:
                              type: text
                              active: true
                            rating:
                              type: number
                              active: true
                            image_urls:
                              type: array
                              active: true
                              items:
                                type: url
                            input:
                              type: input
                              active: true
                            warning:
                              type: warning
                              active: true
                            error:
                              type: error
                              active: true
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