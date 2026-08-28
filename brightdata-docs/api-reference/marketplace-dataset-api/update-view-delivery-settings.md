> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update view delivery settings

> Set the delivery destination, credentials, filename template and batch options for a single dataset view. Returns the updated view id. Covers 250+ domains.

Replaces the delivery configuration for a dataset view. The `deliver.type` field selects the destination and the remaining fields inside `deliver` must match the schema returned by [Get destination type schema](/api-reference/marketplace-dataset-api/get-destination-type-schema) for that destination.

## How to update a view

1. Call [Get delivery options](/api-reference/marketplace-dataset-api/get-delivery-options) to confirm the destination type is supported.
2. Call [Get destination type schema](/api-reference/marketplace-dataset-api/get-destination-type-schema) with that destination type to get the required fields.
3. Send the `PUT` request documented on this page with the `deliver` object populated.

<Note>
  Setting `tar: true` bundles all output files into a single TAR archive. Setting `compress: true` gzips each delivered file. Both can be combined.
</Note>

<Note>
  `batch_size` is the maximum number of records per output file. Use it to split large deliveries into smaller files. The maximum per-batch size is 5 GB.
</Note>

To apply the same configuration to many views at once, use [Bulk update view delivery settings](/api-reference/marketplace-dataset-api/bulk-update-view-delivery-settings) instead.


## OpenAPI

````yaml api-reference/dca-api PUT /datasets/views/{view_id}/delivery_settings
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
  /datasets/views/{view_id}/delivery_settings:
    put:
      description: >-
        Updates the delivery configuration for a specific dataset view. Returns
        the id of the updated view.
      parameters:
        - name: view_id
          in: path
          description: Unique identifier for the dataset view.
          required: true
          schema:
            type: string
            example: v_id1
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ViewDeliverySettings'
            example:
              filename:
                extension: json
                template: bd_{[datetime]}
                tz_offset: '+00:00'
              flatten_csv: false
              deliver:
                type: s3
                bucket: my-bucket
                credentials:
                  aws-access-key: AKIAIOSFODNN7
                  aws-secret-key: wJalrXUtnFEMI
                region: us-east-1
                directory: my/directory
              tar: true
              compress: true
              batch_size: 1000
      responses:
        '200':
          description: View delivery settings updated
          content:
            application/json:
              schema:
                type: object
                properties:
                  view_id:
                    type: string
              example:
                view_id: v_id1
        '400':
          description: Invalid delivery settings payload
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: Invalid delivery settings
        '404':
          description: View not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: View not found
components:
  schemas:
    ViewDeliverySettings:
      type: object
      description: >-
        Delivery configuration for a dataset view. Used by the view delivery
        settings GET, PUT and bulk PUT endpoints.
      properties:
        deliver:
          $ref: '#/components/schemas/DeliverConfig'
          description: >-
            Delivery destination configuration. The `type` field selects the
            destination (for example `s3`, `sftp`, `webhook`) and the remaining
            fields depend on the destination schema returned by
            `/datasets/delivery_settings/{destination_type}/schema`.
        filename:
          type: object
          description: Configuration for the output file name and format.
          properties:
            extension:
              type: string
              description: The output file extension.
              enum:
                - json
                - csv
                - xlsx
                - ndjson
                - parquet
                - jsonl
              example: json
            template:
              type: string
              description: Filename template. Supports `{[datetime]}` placeholder.
              example: bd_{[datetime]}
            tz_offset:
              type: string
              description: >-
                Timezone offset applied when rendering the `{[datetime]}`
                placeholder.
              example: '+00:00'
        flatten_csv:
          type: boolean
          description: When `true`, nested fields are flattened for CSV output.
          default: false
        tar:
          type: boolean
          description: When `true`, delivered files are bundled into a TAR archive.
          default: false
        compress:
          type: boolean
          description: When `true`, delivered files are gzip compressed.
          default: false
        batch_size:
          type: integer
          description: >-
            Maximum records per batch file. Use to split large deliveries into
            smaller files. Maximum batch size is 5GB.
          example: 1000
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