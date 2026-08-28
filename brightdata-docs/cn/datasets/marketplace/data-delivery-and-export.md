> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 数据集市场数据交付

> 以 JSON、NDJSON、CSV、XLSX 或 Parquet 格式接收 Bright Data 数据集市场数据，可通过电子邮件、API、Webhook 或 S3、Snowflake 等云服务交付。

购买或订阅数据集后，Bright Data 会将数据直接交付到您选择的目的地。可从 9 种交付方式与 5 种输出格式中选择，匹配您现有的基础设施与工作流。

## 输出格式

数据集提供以下格式：

| 格式      | 说明                 |
| ------- | ------------------ |
| JSON    | 标准结构化格式            |
| NDJSON  | 以换行分隔的 JSON，适合流式处理 |
| CSV     | 兼容电子表格的格式          |
| XLSX    | Microsoft Excel 格式 |
| Parquet | 面向分析场景优化的列式格式      |

<Tip>
  您也可以接收压缩格式（gzip）的数据，以减小文件体积。
</Tip>

## 交付方式

选择数据交付的方式与目的地：

| 方式                   | 说明                                   |
| -------------------- | ------------------------------------ |
| 电子邮件                 | 数据集直接发送到您的邮箱                         |
| API 下载               | 通过 Bright Data API 使用 snapshot ID 下载 |
| Webhook              | 数据自动推送到您的端点                          |
| Amazon S3            | 直接交付到您的 S3 存储桶                       |
| Google Cloud Storage | 交付到您的 GCS 存储桶                        |
| Google Cloud Pub/Sub | 通过 GCP Pub/Sub 进行流式传输                |
| Microsoft Azure      | 交付到您的 Azure Blob Storage 容器          |
| Snowflake            | 直接加载到您的 Snowflake 数据仓库               |
| SFTP                 | 通过安全文件传输协议交付                         |

## 如何配置交付

<Steps>
  <Step title="打开 My Datasets">
    购买数据集后，进入 **Control Panel → My Datasets**。
  </Step>

  <Step title="打开 Delivery Settings">
    选择您的数据集，点击 **Delivery Settings**。
  </Step>

  <Step title="选择方式和格式">
    选择您偏好的交付方式与输出格式。
  </Step>

  <Step title="配置凭据">
    输入目的地的凭据（存储桶名称、Webhook URL、SFTP 主机等）。
  </Step>

  <Step title="保存">
    点击 **Save**。每次数据刷新后将自动交付。
  </Step>
</Steps>

## 相关页面

* [购买选项](/cn/datasets/marketplace/purchase-options)
* [定价](/cn/datasets/marketplace/pricing)
* [按 API 筛选数据集](/cn/datasets/marketplace/filter-dataset-by-api)
