> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deliver snapshot to S3, Azure Blob or GCP

> Deliver a Bright Data Archive API snapshot to Amazon S3, Azure Blob Storage, Google Cloud Storage or a webhook. POST /webarchive/dump returns a dump_id.

`POST /webarchive/dump` delivers the snapshot from a completed search to Amazon S3, Azure Blob Storage, Google Cloud Storage or a webhook, and returns a `dump_id`.

<Note>
  To use S3 storage delivery, you will first need to do the following:

  * Create an [AWS role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html) which gives Bright Data access to your system.
    * During this setup, you will be asked by Amazon for an “external ID” that is used with the role.
    * Your external ID for S3 is your Bright Data **Account ID** that can be found within [Account Settings](https://brightdata.com/cp/setting/customer_details)
  * Once a role is created, you will need to allow the Bright Data delivery role to `AssumeRole` that role.
    * The Bright Data delivery role is: `arn:aws:iam::422310177405:role/brd.ec2.zs-dca-delivery`
</Note>

<Note>
  To use Google Cloud Storage delivery, create a bucket and provide the required GCP delivery settings.
</Note>

<Warning>
  The **webhook** delivery strategy is **not suitable for large dumps** unless you
  are hosting the webhook on your own infrastructure. Third-party inspection
  tools such as [webhook.site](https://webhook.site) impose strict request body
  size limits and will fail to receive payloads that can reach up to **1 GB** in
  size. For large deliveries, use **Amazon S3**,  **Azure Blob Storage**
  or **Google Cloud Storage** instead.
</Warning>

<Note>
  **Common dump parameters:**

  * `search_id` (required): The search ID from a completed search
  * `max_entries` (optional): Limit the number of files to include in the dump
  * `delivery` (required): Delivery configuration (S3, Azure, GCP, or webhook)
</Note>

<Tip>
  If you’re running a linux/macos machine, you can simulate one of our delivery webhooks with the code on [this page](/datasets/archive/webhook-test).
</Tip>

## What causes a 400 response

`POST /webarchive/dump` returns HTTP 400 when the request body fails validation. The response carries an `error` summary and a `details` array naming each field that failed. Common causes:

* `search_id` is missing.
* `delivery` is missing.
* The `delivery.settings` block does not match the chosen `delivery.strategy`. Each strategy has its own required settings: `bucket` plus `assume_role` for Amazon S3, `bucket` for Google Cloud Storage, `container` plus `credentials` for Azure Blob Storage and `url` for a webhook.

Fix the field named in `details[].path` and resend the request.


## OpenAPI

````yaml api-reference/web-archive-api POST /webarchive/dump
openapi: 3.1.0
info:
  title: BrightData Web Archive API
  version: 1.0.0
  description: API to search and retrieve archived web pages.
servers:
  - url: https://api.brightdata.com
security:
  - bearerAuth: []
paths:
  /webarchive/dump:
    post:
      summary: Deliver a snapshot to Amazon S3, Azure Blob Storage or a Webhook
      description: >-
        Delivers a snapshot from a completed search to cloud storage using the
        specified delivery strategy.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DumpCreateRequest'
      responses:
        '200':
          description: Dump created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DumpCreateResponse'
              examples:
                Success:
                  summary: Dump created successfully
                  value:
                    dump_id: ucd_abc123-1234567890
        '400':
          description: >-
            Bad Request. The request body failed validation, for example a
            missing `search_id` or `delivery` object, or a `delivery` block
            whose settings do not match the chosen `strategy`.
          content:
            application/json:
              schema:
                type: object
                required:
                  - error
                properties:
                  error:
                    type: string
                    description: Human-readable summary of the failure
                  error_code:
                    type: string
                    description: Machine-readable error category
                    example: validation
                  details:
                    type: array
                    description: Per-field validation failures
                    items:
                      type: object
                      properties:
                        message:
                          type: string
                          description: Why the field failed validation
                        path:
                          type: array
                          description: Path to the offending field in the request body
                          items:
                            type: string
                        type:
                          type: string
                          description: Validation rule that failed
              examples:
                Missing search_id:
                  summary: Required field missing from the request body
                  value:
                    error: Request validation failed
                    error_code: validation
                    details:
                      - message: '"search_id" is required'
                        path:
                          - search_id
                        type: any.required
components:
  schemas:
    DumpCreateRequest:
      type: object
      required:
        - search_id
        - delivery
      properties:
        search_id:
          type: string
          description: Search ID from a completed search
        max_entries:
          type: integer
          description: Maximum number of files to include in the dump
        delivery:
          $ref: '#/components/schemas/DumpDelivery'
    DumpCreateResponse:
      type: object
      required:
        - dump_id
      properties:
        dump_id:
          type: string
          description: ID of the created dump
          example: ucd_abc123-1234567890
    DumpDelivery:
      oneOf:
        - $ref: '#/components/schemas/S3Delivery'
          title: Amazon S3
        - $ref: '#/components/schemas/AzureDelivery'
          title: Azure Blob
        - $ref: '#/components/schemas/GcpDelivery'
          title: Google Cloud Storage
        - $ref: '#/components/schemas/WebhookDelivery'
          title: Webhook
    S3Delivery:
      type: object
      required:
        - strategy
        - settings
      properties:
        strategy:
          type: string
          enum:
            - s3
        settings:
          $ref: '#/components/schemas/S3DeliverySettings'
    AzureDelivery:
      type: object
      required:
        - strategy
        - settings
      properties:
        strategy:
          type: string
          enum:
            - azure
        settings:
          $ref: '#/components/schemas/AzureDeliverySettings'
    GcpDelivery:
      type: object
      required:
        - strategy
        - settings
      properties:
        strategy:
          type: string
          enum:
            - gcp
        settings:
          type: object
          required:
            - bucket
          properties:
            bucket:
              type: string
            prefix:
              type: string
    WebhookDelivery:
      type: object
      required:
        - strategy
        - settings
      properties:
        strategy:
          type: string
          enum:
            - webhook
        settings:
          $ref: '#/components/schemas/WebhookDeliverySettings'
    S3DeliverySettings:
      type: object
      required:
        - bucket
        - assume_role
      properties:
        bucket:
          type: string
          description: Target S3 bucket name
        prefix:
          type: string
          description: Optional prefix path inside the bucket
        assume_role:
          $ref: '#/components/schemas/S3AssumeRole'
    AzureDeliverySettings:
      type: object
      required:
        - container
        - credentials
      properties:
        container:
          type: string
          description: Azure Blob Storage container name
        prefix:
          type: string
          description: Optional prefix path inside the container
        credentials:
          $ref: '#/components/schemas/AzureCredentials'
    WebhookDeliverySettings:
      type: object
      required:
        - url
      properties:
        url:
          type: string
          description: Webhook URL to receive notifications about dump delivery status
        auth:
          type: string
          description: Bearer your-optional-auth-token
    S3AssumeRole:
      type: object
      required:
        - role_arn
      properties:
        role_arn:
          type: string
          description: AWS IAM role ARN to assume for delivery
    AzureCredentials:
      type: object
      required:
        - account
        - key
      properties:
        account:
          type: string
          description: Azure storage account name
        key:
          type: string
          description: Azure storage account access key
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