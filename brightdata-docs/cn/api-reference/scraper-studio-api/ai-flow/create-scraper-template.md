> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 创建爬虫模板



## OpenAPI

````yaml api-reference/web-scraper-ide-rest-api POST /dca/collector
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
  /dca/collector:
    post:
      summary: Create Scraper Template
      description: Creates a Scraper Studio scraper with a sample template.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateScraperRequest'
      responses:
        '200':
          description: Scraper created successfully
          content:
            application/json:
              example:
                name: test collector
                deliver:
                  type: webhook
                  endpoint: https://webhook.site11111
                  flatten_csv: false
                  delivery_type: deliver_results
                active: false
                created: '2026-04-12T06:25:47.708Z'
                user: test@example.com
                customer: customer
                customer_id: ID
                output_format_ver: 1
                require_all_success: false
                default_queue_behavior: parallel
                strict_input_normalize: true
                request_cmd_behavior: send_ajax_request
                strict_url_validate: true
                no_strange_input_normalize: true
                allow_wait_ms: false
                id: c_mnvdqy7w1fyaku0uep
                zone: v__dca_test_collector_15
                notifications:
                  success_rate:
                    addresses: test@example.com
                    frequency: 1
                history:
                  - date: '2026-04-12T06:25:47.715Z'
                    user: user
                    comment: Collector was created
                output_fields: []
                fields: {}
                template:
                  stub: true
                has_output_fields_mapping: false
                account_id: ID
                is_under_dataset_migration: false
                under_sla: false
                output_schema_incompatible: false
                beta_output_schema_incompatible: false
                is_scheduled: false
components:
  schemas:
    CreateScraperRequest:
      type: object
      required:
        - name
        - deliver
      properties:
        name:
          type: string
          example: Test
        deliver:
          $ref: '#/components/schemas/DeliverConfig'
    DeliverConfig:
      description: Deliver configuration
      oneOf:
        - $ref: '#/components/schemas/DeliverConfigAzure'
          title: Microsoft Azure
          description: Microsoft Azure
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
          email:
            $ref: '#/components/schemas/DeliverConfigEmail'
          gcs:
            $ref: '#/components/schemas/DeliverConfigGCS'
          gcs_pubsub:
            $ref: '#/components/schemas/DeliverConfigGCSPubSub'
          s3:
            $ref: '#/components/schemas/DeliverConfigS3'
          sftp:
            $ref: '#/components/schemas/DeliverConfigSFTP'
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
                  title: Acess key
                - required:
                    - sas_token
                  title: Shared access token
            directory:
              type: string
          required:
            - container
            - credentials
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
                - gcs_pubsub
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
        - gcs_pubsub
        - s3
        - sftp
        - snowflake
        - webhook
        - ali_oss
    DeliveredFileExt:
      type: string
      enum:
        - json
        - jsonl
        - csv
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