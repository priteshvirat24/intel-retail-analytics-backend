> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 n8n 中设置 Bright Data

> 学习如何将 Bright Data 集成到 n8n 中，构建自动化无代码数据工作流。

## 什么是 n8n？

[n8n](https://n8n.io) 是一个强大的工作流自动化工具，通过可视化界面轻松连接应用和 API。它支持自定义逻辑、API 集成，并且借助社区贡献，现在可以使用 Bright Data 的 Web Unlocker API。

通过新的 [n8n-nodes-brightdata](https://www.npmjs.com/package/n8n-nodes-brightdata) 节点，您可以在 n8n 工作流中直接使用 Bright Data 的高级代理和 CAPTCHA 解决基础设施自动化网页抓取管道。

对于高级用例，也可以通过自定义 HTTP 请求节点集成 [**Bright Data MCP**](/cn/mcp-server/overview) 来访问结构化数据工具、浏览器自动化和实时抓取功能。

## 为什么在 n8n 中使用 Bright Data？

将 Bright Data 与 n8n 集成，让您无需编写代码即可创建高级、可靠的网页抓取器。优势包括：

* 抓取网站而不被封锁
* 通过头信息、IP 轮换和指纹仿真模拟真实用户行为
* 自动绕过 CAPTCHA
* 可靠运行无头抓取任务
* 将数据链入 n8n 支持的 350+ 服务（如 Google Sheets、Airtable、Notion 等）

对于没有代理基础设施或需要抓取受限/反爬虫网站的团队，这个集成非常有用。

## 如何将 Bright Data 与 n8n 集成

以下示例展示了一个 n8n 工作流，该工作流自动收集并发送 MediaMarkt 的“每日优惠”，并根据用户偏好发送邮件。

<Frame>
  <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/n8n-workflow-sample.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=62d01ccbe68c5c5f36f7f3c3f105bb8f" alt="n8n-workflow-sample" width="1373" height="543" data-path="images/integrations/n8n-workflow-sample.png" />
</Frame>

**工作流结构：**

1. Webhook 触发（用户表单提交）
2. Bright Data（数据抓取）
3. HTML 提取（内容解析）
4. OpenAI（推荐生成）
5. Split Out（优惠拆分）
6. Document Generator（HTML 文档生成）
7. SMTP 邮件发送（邮件发送）

<Steps>
  <Step title="前置条件">
    * [Bright Data API key](/cn/api-reference/authentication#api-key)：用于抓取 MediaMarkt 数据。
    * **OpenAI API**：使用 GPT-4o-mini 生成推荐优惠列表。
    * **SMTP 凭据**：用于发送包含优惠的邮件。
    * 安装以下社区节点：
      * `n8n-nodes-base.brightdata`
      * `n8n-nodes-base.documentGenerator`
  </Step>

  <Step title="表单提交（Webhook）">
    此节点是工作流的入口，由表单提交触发。

    * 将 Webhook 节点拖到画布上。
    * 请求体包含：
      * `email`：用户邮箱
      * `categories`：如 `"phones"`、`"appliances"` 的分类数组

    **Webhook 设置**

    * HTTP 方法：`POST`
    * 路径：`recommend-deals`
  </Step>

  <Step title="使用 Bright Data 抓取优惠">
    该节点连接 Bright Data，抓取 MediaMarkt 网站。

    * 将 **Bright Data** 社区节点拖到画布上并连接到 Webhook 节点。
    * 设置服务为 `Web Unlocker API`
    * 使用 `GET` 方法，配置如下：
      * URL: `https://www.mediamarkt.es/es/campaign/campanas-y-ofertas`
      * Zone: 您的 Bright Data 区域
      * Country: 如 `es`（西班牙）
      * API Token: 您的 Bright Data API key
  </Step>

  <Step title="提取 HTML 内容">
    该节点从 Bright Data 返回的原始数据中提取特定 HTML 内容。

    * 将 HTML Extract 节点拖到画布上并连接到 Bright Data 节点。
    * 使用 **Set** 或 **Function** 节点提取 `title` 和 `body`。

    可选使用 **HTML Extract** 节点解析特定部分。
  </Step>

  <Step title="使用 OpenAI 生成推荐">
    该节点使用 GPT-4o-mini 处理提取的数据，生成推荐优惠。

    * 将 OpenAI 节点拖到画布上并连接到 HTML Extract 节点。
    * 认证：
      * Credential Type: 选择 "API Key"
      * API Key: 输入 OpenAI API Key
      * Model: 选择 `gpt-4o-mini`
      * Temperature: 0.7（可调整）
    * 提示示例：

    ```
    你是 AI 助手。根据以下 HTML 内容，提取并推荐与类别 {{ $json["categories"].join(", ") }} 相关的最佳优惠。

    输出 JSON 数组，键包括：name, description, price, link。

    内容: {{ $json["html"] }}
    ```
  </Step>

  <Step title="拆分推荐">
    该节点将 OpenAI 生成的优惠 JSON 数组拆分为单个项目以便进一步处理。

    * 将 Split Out 节点拖到画布上并连接到 OpenAI 节点。
    * 设置 **Split Type**：数组中的项目
    * 输入路径：`$.json.deals`
  </Step>

  <Step title="创建 HTML 文档">
    该节点根据模板生成 HTML 文档，并填充推荐优惠。

    * 将 Document Generator 社区节点拖到画布上并连接到 Split Out 节点。

    **输入**

    * 标题："您的 MediaMarkt 个性化优惠"
    * 模板：自定义 HTML，包含优惠卡（名称、描述、价格和链接）

    **可选**

    * 遍历拆分的项目，每个优惠生成一张卡片
  </Step>

  <Step title="发送包含优惠的邮件">
    该节点将生成的 HTML 文档作为邮件发送给用户。

    * 将 SMTP Email Send 节点拖到画布上并连接到 Document Generator 节点。

    **设置**

    * 收件人: `{{$json["email"]}}`
    * 主题: "🔥 您的 MediaMarkt 个性化优惠"
    * 邮件内容: 嵌入生成的 HTML 文档
  </Step>
</Steps>

<Note>
  * n8n 中的 Bright Data 社区节点专为集成 Web Unlocker API 设计
  * 该节点不是 Bright Data 官方开发，而是社区贡献
  * 更多信息与社区支持，请访问: [n8n 社区讨论](https://community.n8n.io/t/bright-data-community-node-for-scrapping-anything/92011)
</Note>
