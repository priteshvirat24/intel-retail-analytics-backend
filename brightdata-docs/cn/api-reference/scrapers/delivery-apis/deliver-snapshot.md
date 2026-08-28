> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 交付快照

> 将快照内容交付到指定存储



## OpenAPI

````yaml cn-dca-api POST /datasets/v3/deliver/{snapshot_id}
openapi: 3.1.0
info:
  title: Brightdata API
  description: 用于与数据集市场交互的 API
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security:
  - bearerAuth: []
paths:
  /datasets/v3/deliver/{snapshot_id}:
    post:
      description: 将快照内容交付到指定存储
      parameters:
        - name: snapshot_id
          in: path
          required: true
          schema:
            type: string
            example: s_m4x7enmven8djfqak
            description: 触发采集时返回的 ID
        - name: notify
          in: query
          schema:
            type: string
            example: https://notify-me.com/
          description: 交付完成后将发送通知的 URL
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DeliverSnapshotBody'
      responses:
        '200':
          description: 成功
          content:
            application/json:
              schema:
                type: object
                properties:
                  delivery_id:
                    type: string
                    description: 可在 Monitor Delivery API 中使用的交付请求 ID
components:
  schemas:
    DeliverSnapshotBody:
      type: object
      properties:
        deliver:
          $ref: '#/components/schemas/DeliverConfig'
        compress:
          type: boolean
          description: 以 gzip 格式压缩传输文件
          default: false
    DeliverConfig:
      description: Deliver configuration
      oneOf:
        - $ref: '#/components/schemas/DeliverConfigWebhook'
          description: Webhook
        - $ref: '#/components/schemas/DeliverConfigGCS'
          description: Google Cloud
        - $ref: '#/components/schemas/DeliverConfigGCSPubSub'
          description: Google Cloud PubSub
        - $ref: '#/components/schemas/DeliverConfigS3'
          description: Amazon S3
        - $ref: '#/components/schemas/DeliverConfigSnowflake'
          description: Snowflake
        - $ref: '#/components/schemas/DeliverConfigAliOSS'
          description: Aliyun Object Storage Service
        - $ref: '#/components/schemas/DeliverConfigSFTP'
          description: SFTP
        - $ref: '#/components/schemas/DeliverConfigAzure'
          description: Microsoft Azure
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
              description: Webhook 的端点 URL。
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
              description: 存储桶名称。
            credentials:
              type: object
              additionalProperties: false
              description: 认证凭据
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
              description: 目标路径
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
              description: 类似 S3 的主机 URL，仅在使用 Access Key 认证时可用
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
              description: 数据库名称
            schema:
              type: string
              description: 数据库模式
            stage:
              type: string
              description: Snowflake 阶段名称
            role:
              type: string
              description: 用户角色
            warehouse:
              type: string
              description: 仓库名称
            credentials:
              type: object
              additionalProperties: false
              description: 认证凭据
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
                  title: 访问密钥
                - required:
                    - sas_token
                  title: 共享访问令牌
            directory:
              type: string
          required:
            - container
            - credentials
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
              description: 文件名模板，包括占位符。
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
      description: 交付目标类型
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
        在 Authorization 头中使用您的 Bright Data API Key 作为 Bearer token。


        **认证方法:**

        1. 从 Bright Data 账户设置获取您的 API Key:
        https://brightdata.com/cp/setting/users

        2. 在请求的 Authorization 头中包含 API Key

        3. 格式: `Authorization: Bearer YOUR_API_KEY`


        **示例:**

        ```

        Authorization: Bearer
        b5648e1096c6442f60a6c4bbbe73f8d2234d3d8324554bd6a7ec8f3f251f07df

        ```


        了解如何获取 Bright Data API Key:
        https://docs.brightdata.com/cn/api-reference/authentication#如何生成新的-api-key？
      bearerFormat: API Key

````