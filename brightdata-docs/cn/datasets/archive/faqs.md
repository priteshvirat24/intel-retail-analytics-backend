> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 常见问题：Archive API

> 关于 Bright Data Archive API 的常见问题：114 PB 存档数据、4 种交付目标，以及每千个页面 $0.2 至 $1 的 CPM 计费模式。

<AccordionGroup>
  <Accordion title="什么是 Archive API？">
    Archive API 是 Bright Data 提供的一个庞大、持续扩展的缓存存储库，旨在大规模捕获和提供公共网页数据。

    它提供完整的网页和元数据，非常适合用于 AI 训练、机器学习和大规模数据分析。

    与传统网页抓取不同，Archive API 更加注重**相关性**、**新鲜度**和**可用性**，让你能够访问每天抓取的互联网上最重要的内容。
  </Accordion>

  <Accordion title="可用的数据量有多少？">
    截至 2026 年 8 月，Bright Data Archive 已存储 **114 PB** 数据，涵盖来自**约 3.8 亿个域名**的**约 7950 亿个页面**。

    采集持续进行，总量每天都在增长：

    | 时间窗口     | 新增页面    |
    | -------- | ------- |
    | 最近 24 小时 | 约 16 亿  |
    | 最近 7 天   | 约 119 亿 |
    | 最近 30 天  | 约 482 亿 |

    这样的增长速度使 Archive 成为最大规模、最新的网页数据存储库，非常适合 AI 和数据驱动型应用。
  </Accordion>

  <Accordion title="我能多快访问这些数据？">
    你可以通过 [Archive API](/cn/datasets/archive/overview) 立即开始访问数据。Archive API 允许你搜索、检索和筛选 Archive 中的数据快照。

    * 最近 24 小时的数据：根据快照规模，从几分钟到数小时不等
    * 超过 24 小时的数据：根据快照规模，处理和交付最长需要 72 小时
  </Accordion>

  <Accordion title="Archive API 的费用是多少？">
    Archive API 按数据年龄定价，以 CPM（每千个页面的费用）计费。

    | 数据年龄     | 价格          |
    | -------- | ----------- |
    | 最近 24 小时 | \$0.2 / CPM |
    | 超过 24 小时 | \$1 / CPM   |

    在运行转储之前，`GET /webarchive/search/{search_id}` 会返回该搜索的 `dump_cost_usd`，以及将估算费用拆分为缓存页面和存档页面的 `cost_breakdown` 对象。
  </Accordion>

  <Accordion title="我的数据可以通过哪些方式交付？">
    Archive API 提供四种交付方式：

    * **Amazon S3 存储桶：** 将数据快照直接传输到你的 S3 存储桶。
    * **Azure Blob Storage：** 将数据快照直接传输到你的 Azure Blob 容器。
    * **Google Cloud Storage：** 将数据快照直接传输到你的 GCS 存储桶。
    * **Webhook：** 通过 webhook 获取，实现系统的实时集成。

    Webhook 交付不适用于大型转储（可达 1 GB）。各交付目标所需的设置，请参阅[传送到云存储](/cn/api-reference/archive-api/deliver-to-cloud)。
  </Accordion>

  <Accordion title="我可以筛选 Archive 的数据，只获取需要的内容吗？">
    当然可以！Archive API 支持按类别、域名、日期、语言和国家进行筛选，以确保你只获取真正需要的数据。
  </Accordion>

  <Accordion title="Bright Data 的 Archive 与 Common Crawl 有何不同？">
    在处理大规模网页数据时，**新鲜度**、**相关性**和**可访问性**至关重要。Common Crawl 提供的是广泛的网页历史快照，而 Bright Data 的 Archive API 则提供实时、持续更新的数据，并支持高级筛选和交付。以下是两者的对比：

    | **功能**        | **Bright Data 的 Archive**                                                                       | **Common Crawl**                |
    | ------------- | ----------------------------------------------------------------------------------------------- | ------------------------------- |
    | **数据采集方式**    | 持续实时采集公开网页数据，提供接近“现在”的结果。                                                                       | 定期抓取（非实时），按月或双月更新。数据可能已过时。      |
    | **数据量**       | 几年内收集 114 PB，覆盖约 3.8 亿域名的约 7950 亿页面。每周新增约 119 亿页面。                                              | 18 年共收集 2500 亿页面。               |
    | **网站覆盖率与相关性** | 聚焦高价值、真实抓取需求驱动的网站数据。                                                                            | 无差别抓取，包括过时或低质量页面。               |
    | **数据类型**      | 完整网页（含 JS 渲染）                                                                                   | 98.6% 为 HTML 与文本                |
    | **筛选与交付**     | 完整发现与交付平台——支持按类别、域名、语言、日期等筛选。通过 Amazon S3、Azure Blob Storage、Google Cloud Storage 或 webhook 交付。 | 无内置筛选或交付机制，需要手动处理庞大的 WARC 原始文件。 |
  </Accordion>
</AccordionGroup>
