> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 Lindy.ai 中设置 Bright Data

> 通过将 Bright Data 与 Lindy.ai 集成，实现网页数据工作流自动化。学习如何连接 API、触发实时数据采集，并提升业务自动化效率。

<Accordion title="展开以获取您的 Bright Data 代理访问信息">
  ### 您的代理访问信息

  Bright Data 代理按“代理区域”（Proxy zones）进行分组。每个区域包含其对应的代理配置。&#x20;

  要获取代理区域的访问权限：&#x20;

  1. 登录 Bright Data 控制面板
  2. 选择现有代理区域或新建一个代理区域
  3. 点击新的区域名称，并选择 **概览（Overview）** 选项卡
  4. 在概览选项卡中，找到 **访问详情（Access details）**，并单击复制图标将代理访问信息复制到剪贴板&#x20;
  5. 您需要以下信息：代理主机（Proxy Host）、代理端口（Proxy Port）、代理区域用户名（Proxy Zone username）和代理区域密码（Proxy Zone password）
  6. 点击复制图标，将文本复制到剪贴板，并粘贴到您的工具的代理配置中&#x20;

  ### 访问详情示例

  <img src="https://mintcdn.com/brightdata/w0SvUEkwL-1dGVtS/snippets/accessdetails.png?fit=max&auto=format&n=w0SvUEkwL-1dGVtS&q=85&s=a3d4e920631ae105cb2f388c63bc5b5d" alt="" width="597" height="508" data-path="snippets/accessdetails.png" />

  ### 住宅代理访问

  要使用 Bright Data 的 **住宅代理（Residential Proxies）**，您必须是经过 KYC 验证的企业账户。请与 Bright Data 合规团队完成 KYC 验证；不存在自动或无需 KYC 的访问方式。尚未完成 KYC 时，请使用 ISP 或数据中心代理。[了解更多...](/proxy-networks/residential/network-access)

  ### 目标是搜索引擎？

  如果您的目标是 Google、Bing 或 Yandex 等搜索引擎，则需要使用专门的搜索引擎结果页（**SERP**）代理 API。请使用 Bright Data SERP API 来访问搜索引擎。\
  [点击此处了解 Bright Data SERP 代理 API。](/scraping-automation/serp-api/introduction)

  ### 避免工具中的 `PROXY ERROR`

  一些工具会使用搜索引擎作为代理测试目标：如果您的代理测试失败，这可能就是原因。请确保您的测试目标域名不是搜索引擎（此设置在工具配置中，而非 Bright Data 代理的控制范围内）。
</Accordion>

## 什么是 Lindy.ai？

Lindy.ai 是一个无代码 AI 自动化平台，使用户能够创建并部署 AI 驱动的代理，通常被称为“AI 员工”，以自动化各种业务任务。这些代理可处理电子邮件管理、客户支持、日程安排、CRM 数据录入、潜在客户生成等功能，并可与超过 200 个应用（包括 Gmail、Slack、Zoom 和 HubSpot）无缝集成。

## 为什么要在 Lindy.ai 中使用 Bright Data？

**自动化网页数据采集工作流**

* Bright Data 可从网站（如电商、招聘网站、社交媒体）抓取实时数据。
* Lindy.ai 可自动化数据使用的时间、方式和位置（例如每日摘要、警报、CRM 更新）。

**无代码集成复杂数据管道**

* 无需开发人员或手动脚本。
* 在 Lindy.ai 中使用 HTTP 块可可视化构建调用 Bright Data API 的工作流。

**基于实时数据触发动作**

* **示例**：抓取竞争对手网站价格 → 如果产品价格低于您 → 触发 Slack 通知或邮件给团队。
* **示例**：监控职位发布 → 如果新职位符合条件 → 添加到 Google Sheet 或通过 SMS 通知。

**提升运营效率**

* 消除重复任务，如手动监控或复制粘贴抓取数据。
* Lindy 代理可自动 24/7 基于网页数据执行操作。

**可扩展且可靠**

* Bright Data 负责代理管理、反爬虫绕过和数据质量。
* Lindy 负责逻辑处理、调度以及与 200+ 应用（CRM、Notion、Airtable 等）的集成。

## 如何将 Bright Data 与 Lindy.ai 集成？

<Steps>
  <Step title="前置条件">
    开始前，请确保您已具备：

    * 拥有 **Bright Data** 账户并可访问 API（如 Browser API、Web Unlocker API 或 DCA）
    * 您的 **Bright Data API Key**
    * **Lindy.ai** 账户
    * 对 API 和 HTTP 请求的基础理解
  </Step>

  <Step title="选择并配置 Bright Data API">
    根据使用场景，选择合适的 Bright Data API：

    * **Browser API** – 用于渲染 JavaScript 密集页面
    * **Data Collector API (DCA)** – 使用预构建爬虫
    * **Web Unlocker API** – 绕过反爬虫机制

    > 🔗 示例 API 端点（DCA）：

    ```

    POST [https://api.brightdata.com/dca/trigger](https://api.brightdata.com/dca/trigger)

    ```
  </Step>

  <Step title="获取 Bright Data API Key">
    1. 登录您的 [Bright Data 控制面板](https://www.bright.cn/)。
    2. 转到 **API 设置**。
    3. 复制您的 **API Key**。
  </Step>

  <Step title="在 Lindy.ai 中创建新工作流">
    1. 登录 [Lindy.ai](https://lindy.ai)。
    2. 点击 **创建代理** 或 **新建工作流**。
    3. 选择 **空白工作流** 或使用用例模板开始。
  </Step>

  <Step title="添加 HTTP 请求块">
    1. 点击“+”添加工作流块。
    2. 选择 **HTTP 请求**。

    > 配置如下：
    >
    > * **方法**：`POST` 或 `GET`（取决于 API）
    > * **URL**：Bright Data API 端点（如 DCA 触发端点）
    > * **Headers**：
    >   * `Authorization`: `Bearer <your_api_key>`
    >   * `Content-Type`: `application/json`
    > * **Body**（如果为 POST）：API 的 JSON 请求体

    ### 示例：触发 Data Collector

    **HTTP 请求 Body:**

    ```json theme={null}
    {
      "collector_id": "clt_123456789",
      "start_url": "https://example.com/products"
    }
    ```

    **响应**：Bright Data 返回 `collection_id`，可在后续步骤中使用以获取结果。
  </Step>

  <Step title="添加处理 API 响应的逻辑">
    * 使用 Lindy 内置块来：
      * 存储响应
      * 解析数据（例如 JSON 提取）
      * 触发下一步操作（如发送邮件、更新 CRM、Slack 通知）
  </Step>

  <Step title="测试与部署">
    * 使用测试数据运行工作流。
    * 检查响应日志，并根据需要调整 Headers 或 Body。
    * 成功后，激活工作流或设置定时执行。
  </Step>
</Steps>

<Tip>
  ### 🎯 额外示例：抓取 + 通知

  1. 使用 Bright Data 抓取职位信息。
  2. 使用 Lindy 过滤符合关键词的职位（如 “remote”、"Python"）。
  3. 自动将相关职位每日发送邮件给招聘团队。
</Tip>
