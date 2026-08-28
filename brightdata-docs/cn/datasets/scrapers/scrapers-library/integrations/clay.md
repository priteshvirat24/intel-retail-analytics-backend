> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Clay 集成

本文将向您介绍如何将 Clay 集成到 Bright Data 的 Scrapers 中。Clay 是一个功能强大的工具，用于管理和自动化工作流。通过将 Scrapers 集成到 Clay，您可以：

* 自动从目标网站抓取数据。
* 在 Clay 工作流中处理收集到的数据并生成洞察。
* 通过 Clay 简化将网页抓取数据交付到其他工具或服务的流程。

***

## 前置条件

在开始之前，请确保以下事项：

1. Clay 访问权限：您必须拥有具有管理员权限的 Clay 账户。
2. Scrapers 访问权限：您需要准备好 Bright Data API key，包括身份验证信息、所需的端点以及请求/响应结构。

***

## 集成步骤

### 第 1 步：设置 Scrapers

1. 从我们提供的 Bright Data API 选项中选择目标网站。
2. 选择您需要的具体爬虫。
3. 通过 JSON 或 CSV 更新所需的输入列表。
4. 启用“在结果中包含错误报告”切换按钮。
5. 根据您的偏好，启用“将结果交付到外部存储”切换或“发送到 webhook”切换按钮。

***

### 第 2 步：在 Clay 中创建 API 请求工作流

Clay 允许您使用其用户友好的界面创建自动化工作流。调用 Scrapers，请按以下步骤操作：

1. **登录 Clay**：

   * 登录您的 Clay 账户。
   * 导航到工作流（Workflows）部分。

2. **设置触发器**：

   * 选择触发工作流的方式（例如手动、定时或基于其他集成服务中的事件）。

3. **添加 HTTP 请求操作**：

   * 在工作流中添加 HTTP 请求模块。
   * 选择 Scrapers 支持的 HTTP 方法（POST "[触发采集](/api-reference/scrapers/delivery-apis/download-snapshot)")。

4. **配置请求**：

   * 在 HTTP 请求模块中输入以下内容：
     * URL：输入 API 端点（例如 [https://api.brightdata.com/datasets/v3/trigger](/api-reference/rest-api/scraper/asynchronous-requests)）。
     * Headers：包含任何必需的请求头，例如：
       ```JSON theme={null}
       {
           "Authorization": "Bearer YOUR_API_KEY",
           "Content-Type": "application/json"
       }
       ```
     * Body（如需要）：以 JSON 形式添加请求体中所需的参数。

5. **测试请求**：

   * 使用 Clay 的测试工具发送测试请求，确保 Scrapers 返回预期数据。

***

### 第 3 步：在 Clay 中处理响应

成功连接 Scrapers 后，您可以处理响应数据：

1. **与其他服务集成**：

   * 使用 Clay 将数据发送到数据库、Google 表格、电子邮件或其他服务。

2. **添加条件/逻辑**：

   * 在工作流中创建条件或筛选器。例如，仅处理价格高于某个阈值的条目。

***

### 第 4 步：安排或部署工作流

根据您的偏好安排工作流自动运行（例如每小时或每日），或者在需要时手动触发。
