> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deliver snapshot

> Use the Bright Data Marketplace Dataset API to deliver a Snapshot. POST /datasets/snapshots/{id}/deliver returns 200 OK with metadata as JSON.

<AccordionGroup>
  <Accordion title="Before you begin" icon="circle-info" iconType="duotone">
    You need a **Snapshot ID** to use this endpoint. A Snapshot ID (e.g., `snap_m2bxug4e2o352v1jv1`) is a unique identifier created each time a data collection is triggered or a dataset is filtered.

    ### Where do Snapshot IDs come from?

    | Source                                                                                      | Endpoint                       | What it returns                              |
    | :------------------------------------------------------------------------------------------ | :----------------------------- | :------------------------------------------- |
    | [Filter Dataset](/api-reference/marketplace-dataset-api/filter-dataset-with-csv-json-files) | `POST` `/datasets/filter`      | `snapshot_id` in the response body           |
    | [Trigger Collection](/api-reference/rest-api/scraper/asynchronous-requests)                 | `POST` `/datasets/v3/trigger`  | `snapshot_id` in the response body           |
    | Dataset Subscription                                                                        | Automatic delivery schedule    | Snapshot IDs are generated per scheduled run |
    | [Snapshot List](/api-reference/scrapers/management-apis/get-snapshots)                      | `GET` `/datasets/v3/snapshots` | List of all snapshots with their IDs         |

    <Tip>
      If you don't have a Snapshot ID yet, start by filtering a dataset [Filter Dataset](/api-reference/marketplace-dataset-api/filter-dataset) or [triggering a collection](/api-reference/rest-api/scraper/asynchronous-requests) first. The response will include the `snapshot_id` you need.
    </Tip>

    You can check snapshot status before delivering:

    ```sh theme={null}
    curl "https://api.brightdata.com/datasets/snapshots/snap_m2bxug4e2o352v1jv1" \
      -H "Authorization: Bearer YOUR_API_KEY"
    ```

    The snapshot must be in `ready` status before delivery.

    > See [Get Snapshot Metadata](/api-reference/marketplace-dataset-api/get-snapshot-meta) for full documentation.
  </Accordion>

  <Accordion title="Tracking delivery status" icon="clock" iconType="duotone">
    The `id` returned in the response is a **delivery job ID**. Use it to monitor whether your delivery has completed, failed, or been canceled.

    <CodeGroup>
      ```sh Endpoint theme={null}
      GET https://api.brightdata.com/datasets/v3/delivery/{delivery_id}
      ```

      ```sh Example theme={null}
      curl "https://api.brightdata.com/datasets/v3/delivery/del_abc123xyz" \
        -H "Authorization: Bearer YOUR_API_KEY"
      ```

      ```json Response theme={null}
      {
        "id": "del_abc123xyz",
        "status": "done",
        "delivery_files": [
          {
            "filename": "my-data.json",
            "delivery_ts": 1709000000
          }
        ]
      }
      ```
    </CodeGroup>

    | Field            | Type   | Description                                                  |
    | ---------------- | ------ | ------------------------------------------------------------ |
    | `id`             | string | The delivery job ID                                          |
    | `status`         | string | Delivery status: done, canceled, or failed                   |
    | `delivery_files` | array  | List of delivered files with filename and delivery timestamp |

    <Tip>
      Poll this endpoint until status is "done". For large snapshots with `batch_size` set, `delivery_files` will contain multiple entries, one per batch file.
    </Tip>

    > See [Monitor Delivery](/api-reference/scrapers/management-apis/monitor-delivery) for full documentation.
  </Accordion>

  <Accordion title="End-to-end workflow" icon="arrows-left-right" iconType="duotone">
    Here's the complete flow from triggering a collection to receiving your data:

    <Steps>
      <Step title="Trigger a collection or filter a dataset">
        This creates a snapshot and returns a `snapshot_id`.

        <CodeGroup>
          ```sh Request theme={null}
          curl -X POST "https://api.brightdata.com/datasets/v3/trigger?dataset_id=gd_l1viktl72bvl7bjuj0" \
            -H "Authorization: Bearer YOUR_API_KEY" \
            -H "Content-Type: application/json" \
            -d '[{"url": "https://example.com/product/123"}]'
          ```

          ```Response theme={null}
          {"snapshot_id": "snap_m2bxug4e2o352v1jv1"}
          ```
        </CodeGroup>
      </Step>

      <Step title="Wait for the snapshot to be ready">
        Poll the snapshot metadata endpoint until status is "ready".

        <CodeGroup>
          ```sh Request theme={null}
          curl "https://api.brightdata.com/datasets/snapshots/snap_m2bxug4e2o352v1jv1" \
            -H "Authorization: Bearer YOUR_API_KEY"
          ```

          ```json Response theme={null}
          {
            "status": "ready",
            "dataset_size": 50000,
            "file_size": 250000000
          }
          ```
        </CodeGroup>
      </Step>

      <Step title="Deliver the snapshot">
        Call this endpoint with the snapshot ID and your delivery configuration.

        <CodeGroup>
          ```sh Request theme={null}
          curl -X POST "https://api.brightdata.com/datasets/snapshots/snap_m2bxug4e2o352v1jv1/deliver" \
            -H "Authorization: Bearer YOUR_API_KEY" \
            -H "Content-Type: application/json" \
            -d '{
                "deliver": {
                  "type": "webhook",
                  "filename": {"template": "my-data", "extension": "json"},
                  "endpoint": "https://example.com/webhook"
                }
            }'
          ```

          ```json Response theme={null}
          {
            "id": "del_abc123xyz"
          }
          ```
        </CodeGroup>
      </Step>

      <Step title="Track the delivery">
        Use the delivery job ID to monitor progress.

        <CodeGroup>
          ```sh Request theme={null}
          curl "https://api.brightdata.com/datasets/v3/delivery/del_abc123xyz" \
            -H "Authorization: Bearer YOUR_API_KEY"
          ```

          ```json Response theme={null}
          {
            "id": "del_abc123xyz",
            "status": "done",
            "delivery_files": [...]
          }
          ```
        </CodeGroup>
      </Step>
    </Steps>
  </Accordion>
</AccordionGroup>


## OpenAPI

````yaml api-reference/dca-api POST /datasets/snapshots/{id}/deliver
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
  /datasets/snapshots/{id}/deliver:
    post:
      description: Deliver the dataset snapshot
      parameters:
        - in: path
          name: id
          description: >-
            The Snapshot ID to deliver. This is the unique identifier returned
            when you trigger a collection, filter a dataset, or run a
            subscription. 


            > Learn more about [Snapshot
            ID](/api-reference/terminology#snapshot-id).
          required: true
          schema:
            type: string
            example: snap_m2bxug4e2o352v1jv1
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DeliverSnapshotBody'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    description: >-
                      The delivery job ID. Use this ID to track the delivery
                      status (see [Tracking delivery
                      status](/api-reference/marketplace-dataset-api/deliver-snapshot#tracking-delivery-status)).
              example:
                id: del_abc123xyz
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: Batch size exceeds 5GB limit
        '404':
          description: Snapshot not found or isn't in ready status.
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: Snapshot not found
components:
  schemas:
    DeliverSnapshotBody:
      type: object
      properties:
        deliver:
          $ref: '#/components/schemas/DeliverConfig'
        compress:
          type: boolean
          description: Deliver file compressed in gzip format
          default: false
        batch_size:
          type: integer
          description: >-
            Number of records per file. Use this to split large snapshots into
            multiple smaller files. Files are split by record count. Recommended
            for snapshots with more than 1 million records. Note: Maximum batch
            size is 5GB.
          examples:
            - 100000
    DeliverConfig:
      description: Deliver configuration
      oneOf:
        - $ref: '#/components/schemas/DeliverConfigAzure'
          title: Microsoft Azure
          description: Microsoft Azure
        - $ref: '#/components/schemas/DeliverConfigBuild'
          title: Build
          description: Build delivery
        - $ref: '#/components/schemas/DeliverConfigEmail'
          title: Email
          description: Email delivery
        - $ref: '#/components/schemas/DeliverConfigGCS'
          title: Google Cloud
          description: Google Cloud
        - $ref: '#/components/schemas/DeliverConfigGCSPubSub'
          title: Google Cloud PubSub
          description: Google Cloud PubSub
        - $ref: '#/components/schemas/DeliverConfigS3'
          title: Amazon S3
          description: Amazon S3
        - $ref: '#/components/schemas/DeliverConfigSFTP'
          title: SFTP
          description: SFTP
        - $ref: '#/components/schemas/DeliverConfigSnowflake'
          title: Snowflake
          description: Snowflake
        - $ref: '#/components/schemas/DeliverConfigWebhook'
          title: Webhook
          description: Webhook
        - $ref: '#/components/schemas/DeliverConfigAliOSS'
          title: Aliyun Object Storage Service
          description: Aliyun Object Storage Service
      discriminator:
        propertyName: type
        mapping:
          azure:
            $ref: '#/components/schemas/DeliverConfigAzure'
          build:
            $ref: '#/components/schemas/DeliverConfigBuild'
          email:
            $ref: '#/components/schemas/DeliverConfigEmail'
          gcs:
            $ref: '#/components/schemas/DeliverConfigGCS'
          gcp_pubsub:
            $ref: '#/components/schemas/DeliverConfigGCSPubSub'
          s3:
            $ref: '#/components/schemas/DeliverConfigS3'
          sftp:
            $ref: '#/components/schemas/DeliverConfigSFTP'
          snowflake:
            $ref: '#/components/schemas/DeliverConfigSnowflake'
          webhook:
            $ref: '#/components/schemas/DeliverConfigWebhook'
          ali_oss:
            $ref: '#/components/schemas/DeliverConfigAliOSS'
    DeliverConfigAzure:
      allOf:
        - $ref: '#/components/schemas/DeliverConfigBase'
        - type: object
          properties:
            type:
              enum:
                - azure
            container:
              type: string
              minLength: 3
              pattern: ^[a-z0-9](-?[a-z0-9])*$
            credentials:
              type: object
              additionalProperties: false
              properties:
                account:
                  type: string
                  pattern: ^[a-zA-Z0-9]+$
                key:
                  type: string
                  format: byte
                sas_token:
                  type: string
              required:
                - account
              oneOf:
                - required:
                    - key
                  title: Access key
                - required:
                    - sas_token
                  title: Shared access token
            directory:
              type: string
          required:
            - container
            - credentials
    DeliverConfigBuild:
      allOf:
        - $ref: '#/components/schemas/DeliverConfigBase'
        - type: object
          properties:
            type:
              enum:
                - build
            endpoint:
              type: string
              format: uri
              description: The endpoint URL for the webhook.
    DeliverConfigEmail:
      allOf:
        - $ref: '#/components/schemas/DeliverConfigBase'
        - type: object
          properties:
            type:
              enum:
                - email
            address:
              type: string
              format: email
              description: The recipient email address.
    DeliverConfigGCS:
      allOf:
        - $ref: '#/components/schemas/DeliverConfigBase'
        - type: object
          properties:
            type:
              enum:
                - gcs
            bucket:
              type: string
              description: Name of the bucket.
            credentials:
              type: object
              additionalProperties: false
              description: Credentials for authentication
              properties:
                client_email:
                  type: string
                private_key:
                  type: string
              required:
                - client_email
                - private_key
            directory:
              type: string
              description: Target path
          required:
            - bucket
            - credentials
    DeliverConfigGCSPubSub:
      allOf:
        - $ref: '#/components/schemas/DeliverConfigBase'
        - type: object
          properties:
            type:
              enum:
                - gcp_pubsub
            topic_id:
              type: string
            attributes:
              type: array
              items:
                type: object
            credentials:
              type: object
              additionalProperties: false
              properties:
                client_email:
                  type: string
                private_key:
                  type: string
              required:
                - client_email
                - private_key
          required:
            - topic_id
            - credentials
    DeliverConfigS3:
      allOf:
        - $ref: '#/components/schemas/DeliverConfigBase'
        - type: object
          properties:
            type:
              enum:
                - s3
            bucket:
              type: string
            endpoint_url:
              type: string
              description: S3 like host url, available only with Access Key auth
            credentials:
              type: object
              additionalProperties: false
              minProperties: 2
              properties:
                aws-access-key:
                  type: string
                aws-secret-key:
                  type: string
                role_arn:
                  type: string
                external_id:
                  type: string
              oneOf:
                - title: Role ARN
                  required:
                    - role_arn
                    - external_id
                - title: Access Key
                  required:
                    - aws-access-key
                    - aws-secret-key
            region:
              type: string
            directory:
              type: string
          required:
            - bucket
            - credentials
    DeliverConfigSFTP:
      allOf:
        - $ref: '#/components/schemas/DeliverConfigBase'
        - type: object
          properties:
            type:
              enum:
                - sftp
            path:
              type: string
              format: hostname
            port:
              type: integer
              minimum: 0
              maximum: 65535
            credentials:
              type: object
              additionalProperties: false
              properties:
                username:
                  type: string
                password:
                  type: string
                ssh_key:
                  type: string
                passphrase:
                  type: string
              required:
                - username
            directory:
              type: string
          required:
            - path
            - credentials
    DeliverConfigSnowflake:
      allOf:
        - $ref: '#/components/schemas/DeliverConfigBase'
        - type: object
          properties:
            type:
              enum:
                - snowflake
            database:
              type: string
            schema:
              type: string
            stage:
              type: string
            role:
              type: string
            warehouse:
              type: string
            credentials:
              type: object
              additionalProperties: false
              properties:
                account:
                  type: string
                user:
                  type: string
                password:
                  type: string
              required:
                - account
                - user
                - password
          required:
            - database
            - schema
            - stage
            - role
            - warehouse
            - credentials
    DeliverConfigWebhook:
      allOf:
        - $ref: '#/components/schemas/DeliverConfigBase'
        - type: object
          properties:
            type:
              enum:
                - webhook
            endpoint:
              type: string
              format: uri
              description: The endpoint URL for the webhook.
    DeliverConfigAliOSS:
      allOf:
        - $ref: '#/components/schemas/DeliverConfigBase'
        - type: object
          properties:
            type:
              enum:
                - ali_oss
            bucket:
              type: string
            credentials:
              type: object
              additionalProperties: false
              properties:
                access-key:
                  type: string
                secret-key:
                  type: string
              required:
                - access-key
                - secret-key
            region:
              type: string
            directory:
              type: string
          required:
            - bucket
            - credentials
            - region
    DeliverConfigBase:
      type: object
      additionalProperties: false
      properties:
        type:
          $ref: '#/components/schemas/DatasetDeliveryType'
        filename:
          type: object
          additionalProperties: false
          properties:
            template:
              type: string
              description: Template for the filename, including placeholders.
            extension:
              $ref: '#/components/schemas/DeliveredFileExt'
          required:
            - template
            - extension
      required:
        - type
        - filename
    DatasetDeliveryType:
      type: string
      description: Type of the delivery target
      enum:
        - azure
        - build
        - email
        - gcs
        - gcp_pubsub
        - s3
        - sftp
        - snowflake
        - webhook
        - ali_oss
    DeliveredFileExt:
      type: string
      enum:
        - json
        - csv
        - xlsx
        - ndjson
        - parquet
        - jsonl
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