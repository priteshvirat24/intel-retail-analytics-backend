> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# AI 模型的训练数据：技术指南

> Bright Data 用于构建和管理 AI 训练数据采集管道的全面技术概述。

<Card title="正在构建 AI 初创公司？" cta="了解更多" href="https://brightdata.com/ai/ai-startups-program" icon="rocket-launch" iconType="duotone" arrow="true">
  您可能符合我们的初创计划资格。获得本文所介绍基础设施的全额资助访问权限（最高价值 \$20,000）。
</Card>

# AI 模型的训练数据：技术指南

获取高质量、大规模的训练数据是 AI 工程师面临的关键挑战。本指南提供了 Bright Data 基础设施的全面技术概述，用于构建和管理数据采集管道，旨在帮助您做出明智决策并快速开始。

## 技术快速参考

| 特性        | 规格                                                                                        |
| --------- | ----------------------------------------------------------------------------------------- |
| **数据格式**  | `JSON`、`NDJSON`、`CSV`、`XLSX` 和 `Parquet`。在 API 请求中指定您所需的格式。                               |
| **身份验证**  | 所有 API 请求都使用 bearer 令牌进行身份验证。在 `Authorization` 标头中包含您的 API 密钥。                            |
| **数据新鲜度** | **存档：** 历史数据。**预收集：** 每天、每周或每月更新。**自定义：** 按需、近实时。                                         |
| **合规性**   | 符合 GDPR、CCPA 和 SOC2。我们遵守所有数据收集的严格伦理框架。查看我们的 [信任中心](https://www.bright.cn/trustcenter)。    |
| **开发者工具** | 我们为 [**Python**](/api-reference/SDK-PY) 和 [**Javascript**](/api-reference/SDK-JS) 提供 SDK。 |
| **免费试用**  | 注册并获得测试平台的抵用额。在购买前下载任何数据集的样本。                                                             |

## 数据采集策略

您的数据采集策略取决于您的模型需求。选择最适合您使用场景的方法，从基础训练到专门的实时数据收集。

<Tabs>
  <Tab title="Web 存档">
    **最适合：** 基础、大规模的模型训练。

    Web 存档提供对拍字节级规模历史网络数据存储库的访问，是训练需要全面了解数字世界的大型语言模型和扩散模型的理想来源。

    * **使用场景：** LLM 预训练、历史分析、构建基础模型。
    * **下一步：** [联系我们的数据专家](https://www.bright.cn/ai/video-data#popup-170970) 获取访问权限和定价。
    * **了解更多：** [Web 存档文档](/datasets/archive/overview)
  </Tab>

  <Tab title="预收集数据集">
    **最适合：** 在特定领域对模型进行微调。

    我们的精选数据集在众多行业中提供结构化、高质量的数据，使您能够高效地专门为特定任务调整模型，而无需数据收集的开销。

    * **使用场景：** 微调、行业特定模型、市场研究。
    * **定价：** 从 **每 100,000 条记录 \$250** 开始。
    * **质量：** 严格验证。可获得免费样本进行评估。
    * **下一步：** [探索数据集](/datasets/marketplace/dataset-view)
  </Tab>

  <Tab title="自定义收集">
    **最适合：** 来自特定来源的新鲜、按需数据。

    启动程序化数据收集任务，从任何公共 URL 获取实时、结构化的数据。这使您能够完全控制训练数据的新鲜度和特异性。

    * **使用场景：** 实时应用、追踪动态数据、自定义知识库。
    * **定价：** 根据请求的复杂性和规模。
    * **下一步：** [联系我们获取自定义报价](https://www.bright.cn/ai/video-data#popup-170970)。
    * **了解更多：** [自定义数据集 API 文档](/cn/datasets/scrapers/custom-scrapers/custom-dataset-api)

    **API 示例：**

    ```bash theme={null}
    curl "https://api.brightdata.com/datasets/initiate?dataset_id=YOUR_DATASET_ID&type=url_collection&view=YOUR_VIEW_ID" \
      -H "Authorization: Bearer YOUR_API_KEY" \
      -H "Content-Type: application/json" \
      -d '[{"url":"https://example.com"}]'
    ```
  </Tab>

  <Tab title="视频和媒体">
    **最适合：** 大规模训练多模态模型。

    通过使用我们的弹性基础设施，克服 `yt-dlp` 等工具的局限性。Web Unlocker API 处理速率限制、地理限制和机器人检测，确保可靠的视频数据管道。

    * **使用场景：** 训练视频、音频和图像模型。
    * **需要 KYC：** 访问需要 Know Your Customer 流程，以确保因媒体内容的敏感性而进行的合乎伦理和合规的数据采集。
    * **下一步：** [与我们的数据专家预订会议](https://www.bright.cn/ai/video-data#popup-170970) 开始审批流程。
  </Tab>
</Tabs>

## 数据交付

一旦收集到数据，可以将其交付到各种目标位置，以与您现有的云基础设施无缝集成。

**支持的交付选项：**

* Amazon S3
* Google Cloud Storage
* Microsoft Azure Storage
* Webhook
* SFTP/FTP
* Snowflake
* API 下载

有关设置您首选交付方法的详细说明，请参阅我们的 [交付选项文档](/cn/datasets/scrapers/scrapers-library/delivery-options)。
