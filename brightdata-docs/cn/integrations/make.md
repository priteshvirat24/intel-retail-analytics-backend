> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 Make.com 中设置 Bright Data

> 学习如何将 Bright Data 集成到 Make.com 中，构建自动化无代码数据工作流。

## 什么是 Make.com？

[Make](https://www.make.com/en/integrations/brightdata)（原 Integromat）是一个可视化自动化平台，让您无需编写代码即可连接各种应用和服务，创建强大的工作流。

Bright Data 与 Make 的集成使网页数据收集和处理变得无缝。通过该集成，您可以自动化任务，例如抓取网站、获取数据集和调用 API。

Bright Data 在 Make 中提供以下六个模块：

1. **运行 Web Unlocker API** – 访问并提取被反爬虫保护的网站数据。
2. **下载快照内容** – 获取之前捕获的数据集的完整内容。
3. **筛选数据集** – 对数据集应用筛选器，生成精炼快照。
4. **获取快照元数据** – 获取快照的详细元数据。
5. **获取快照部分内容** – 提取快照的特定部分。
6. **执行 API 调用** – 执行任何经过授权的 Bright Data API 请求。

## 为什么在 Make.com 中使用 Bright Data？

将 Bright Data 与 [Make](https://www.make.com/en/integrations/brightdata) 集成，可构建复杂的网页数据管道——无需编写任何代码。

您可以可视化设计并自动化工作流，将 Bright Data 与 2000+ 其他应用和服务连接。例如，您可以：

* 使用 **Web Unlocker API** 提取网站数据。
* 下载并存储快照内容。
* 动态筛选数据集。
* 获取快照元数据或特定部分。
* 触发授权的 Bright Data API 调用。

这些功能让您可以构建端到端的数据流，将 Bright Data 与 Google Sheets、Airtable、Notion、Slack 或内部系统连接。

## 如何将 Bright Data 与 Make.com 集成

<Steps>
  <Step title="获取 Bright Data API Key">
    * 登录您的 [Bright Data 控制面板](https://www.bright.cn/cp)。
    * 转到 [账户设置](https://www.bright.cn/cp/setting/users)。
    * 如果尚未生成，请 [生成 API Key](/cn/api-reference/authentication#如何生成新的-api-key？)。
  </Step>

  <Step title="创建新场景">
    * 登录您的 Make.com 账户。
    * 点击左上角的 **Create a new scenario**。
    * 选择 **Build from scratch** 选项。
  </Step>

  <Step title="将 Bright Data 模块添加到场景">
    * 点击 **+** 按钮添加模块。
    * 搜索并选择列表中的 **Bright Data**。
  </Step>

  <Step title="配置“运行 Web Unlocker API”模块">
    * 选择 **Run an Web Unlocker API** 模块。
    * 点击 **Create a connection**。
    * 输入描述性连接名称。
    * 将 Bright Data API Key 粘贴到 **API Token** 字段。
    * 设置参数，如 `zone`、`url`、`format`、`method`、`country` 和 `async`。
    * 点击 **Save**。
  </Step>

  <Step title="等待任务完成">
    * 添加延迟或使用调度机制，以确保 Web Unlocker API 任务完成后再继续操作。
  </Step>

  <Step title="下载快照内容">
    * 添加 **Download a Snapshot Content** 模块。
    * 配置以获取已完成 Web Unlocker API 任务的结果。
  </Step>

  <Step title="将数据存储到 Google Sheets">
    * 添加 **Google Sheets** 模块。
    * 使用该模块将提取的数据插入到您的电子表格中。
  </Step>
</Steps>

该设置构建了一个无代码数据提取管道，实现自动化收集和存储数据——非常适合价格监控或竞争对手追踪等用例。
