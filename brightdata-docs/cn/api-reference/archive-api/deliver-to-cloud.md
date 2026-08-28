> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 将快照传送到 S3、Azure Blob 或 GCP

> 将 Bright Data Archive API 快照传送到 Amazon S3、Azure Blob Storage、Google Cloud Storage 或 webhook。POST /webarchive/dump 返回 dump_id。

`POST /webarchive/dump` 将已完成搜索的快照传送到 Amazon S3、Azure Blob Storage、Google Cloud Storage 或 webhook，并返回 `dump_id`。

<Note>
  要使用 S3 存储传递，您首先需要执行以下操作：

  * 创建一个 [AWS 角色](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html)，为 Bright Data 授予访问您系统的权限。
    * 在此设置期间，Amazon 会要求您提供一个与角色一起使用的"外部 ID"。
    * 您的 S3 外部 ID 是您的 Bright Data **账户 ID**，可在 [账户设置](https://www.bright.cn/cp/setting/customer_details) 中找到
  * 创建角色后，您需要允许 Bright Data 传递角色 `AssumeRole` 该角色。
    * Bright Data 传递角色是：`arn:aws:iam::422310177405:role/brd.ec2.zs-dca-delivery`
</Note>

<Note>
  要使用 Google Cloud Storage 传递，请创建一个存储桶并提供所需的 GCP 传递设置。
</Note>

<Warning>
  **webhook** 传递策略**不适合大型数据转储**，除非您在自己的基础设施上托管 webhook。第三方检查工具（如 [webhook.site](https://webhook.site)）施加了严格的请求体大小限制，将无法接收可能达到 **1 GB** 大小的有效负载。对于大型传递，请改用 **Amazon S3**、**Azure Blob Storage** 或 **Google Cloud Storage**。
</Warning>

<Note>
  **常见数据转储参数：**

  * `search_id`（必需）：来自已完成搜索的搜索 ID
  * `max_entries`（可选）：限制要包含在数据转储中的文件数量
  * `delivery`（必需）：传递配置（S3、Azure、GCP 或 webhook）
</Note>

<Tip>
  如果您运行的是 linux/macos 机器，可以使用[此页面](/cn/datasets/archive/webhook-test)上的代码模拟 Bright Data 的传递 webhook 之一。
</Tip>

## 什么情况会返回 400

当请求体未通过校验时，`POST /webarchive/dump` 返回 HTTP 400。响应包含 `error` 摘要和列出每个校验失败字段的 `details` 数组。常见原因：

* 缺少 `search_id`。
* 缺少 `delivery`。
* `delivery.settings` 与所选的 `delivery.strategy` 不匹配。每种策略有各自的必需设置：Amazon S3 需要 `bucket` 和 `assume_role`，Google Cloud Storage 需要 `bucket`，Azure Blob Storage 需要 `container` 和 `credentials`，webhook 需要 `url`。

请修正 `details[].path` 中指出的字段后重新发送请求。


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