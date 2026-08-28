> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Web Archive 概览

> Web Archive 让您访问 Bright Data 存储的网络流量（覆盖 3.8 亿\+ 域名），这是一个通过 Unlocker 和 SERP API 持续采集页面而不断增长的仓库。

## 功能说明

无需运行自己的爬虫，您可以直接在 Web Archive 中搜索，按需筛选（时间范围、域名、URL 模式、语言、拦截信号），并以 HTML 文件 + 元数据的形式导出即用型数据集。

## 常见用例

* **LLM 训练与 RAG 管道**：基于目标网络片段构建或刷新训练语料
* **搜索与索引**：使用大型域名集合的历史内容回填索引
* **搜索产品增强**：改善具有高级反爬拦截的网站覆盖率，支持大规模可靠的页面检索

## 工作原理

<Card title="运行搜索" icon="search" href="/cn/api-reference/archive-api/run-a-search" iconType="duotone" arrow="true" horizontal>
  按时间范围、域名、URL 模式、语言或信号（CAPTCHA、robots 拦截等）进行筛选
</Card>

<Card title="查看预估" icon="clipboard-list" href="/cn/api-reference/archive-api/get-search-status" iconType="duotone" arrow="true" horizontal>
  查看匹配的文件数、快照大小、预计时长和费用
</Card>

<Card title="创建并传送快照" icon="file-export" href="/cn/api-reference/archive-api/deliver-to-cloud" iconType="duotone" arrow="true" horizontal>
  将快照以 HTML 文件 + 元数据（URL、时间戳、采集属性）的形式导出至 Amazon S3、Azure Blob Storage、Google Cloud Storage 或通过 webhook 传送
</Card>
