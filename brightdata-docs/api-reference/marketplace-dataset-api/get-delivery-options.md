> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get delivery options

> List the supported delivery destinations, filename templates and batch settings you can use when configuring delivery for a dataset view. Covers 250+ domains.

Use this endpoint before configuring a dataset view delivery to discover which destination types are supported and which fields the filename and batch parameters accept. The response is the canonical source of truth. Supported destinations currently include `api_pull`, `webhook`, `email`, `gcs`, `gcp_pubsub`, `s3`, `snowflake`, `ali_oss`, `sftp` and `azure`.

Call [Get destination type schema](/api-reference/marketplace-dataset-api/get-destination-type-schema) next to retrieve the required fields for the specific destination you want to use.


## OpenAPI

````yaml api-reference/dca-api GET /datasets/delivery_settings/options
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
  /datasets/delivery_settings/options:
    get:
      description: >-
        Returns the options available for configuring delivery settings on a
        dataset view, including supported destination types, filename templates,
        and batch size.
      responses:
        '200':
          description: Delivery settings options
          content:
            application/json:
              schema:
                type: object
                properties:
                  deliver:
                    type: object
                    properties:
                      required:
                        type: boolean
                      type:
                        type: string
                      deliver_types:
                        type: array
                        items:
                          type: string
                        example:
                          - api_pull
                          - webhook
                          - email
                          - gcs
                          - gcp_pubsub
                          - s3
                          - snowflake
                          - ali_oss
                          - sftp
                          - azure
                  flatten_csv:
                    type: object
                    properties:
                      required:
                        type: boolean
                      type:
                        type: string
                  delivery_type:
                    type: object
                    properties:
                      required:
                        type: boolean
                      type:
                        type: string
                      default:
                        type: string
                  filename:
                    type: object
                    properties:
                      required:
                        type: boolean
                      template:
                        type: object
                        properties:
                          type:
                            type: string
                          default:
                            type: string
                      extension:
                        type: object
                        properties:
                          values:
                            type: array
                            items:
                              type: string
                            example:
                              - json
                              - csv
                              - xlsx
                              - ndjson
                              - parquet
                              - jsonl
                          default:
                            type: string
                      tz_offset:
                        type: object
                        properties:
                          type:
                            type: string
                          pattern:
                            type: string
                          default:
                            type: string
                  batch_size:
                    type: object
                    properties:
                      required:
                        type: boolean
                      type:
                        type: string
              example:
                deliver:
                  required: true
                  type: object
                  deliver_types:
                    - api_pull
                    - webhook
                    - email
                    - gcs
                    - gcp_pubsub
                    - s3
                    - snowflake
                    - ali_oss
                    - sftp
                    - azure
                flatten_csv:
                  required: false
                  type: boolean
                delivery_type:
                  required: false
                  type: string
                  default: deliver_results
                filename:
                  required: false
                  template:
                    type: string
                    default: bd_{[datetime]}
                  extension:
                    values:
                      - json
                      - csv
                      - xlsx
                      - ndjson
                      - parquet
                      - jsonl
                    default: json
                  tz_offset:
                    type: string
                    pattern: '[+-](0\d|1[01]):[0-5]\d+'
                    default: '+00:00'
                batch_size:
                  required: true
                  type: number
        '401':
          description: Unauthorized - Invalid or missing API key
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: Unauthorized
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

        Authorization: Bearer YOUR_API_KEY

        ```


        Learn how to get your Bright Data API key:
        https://docs.brightdata.com/api-reference/authentication
      bearerFormat: API Key

````