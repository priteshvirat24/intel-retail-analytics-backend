> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何将 Bright Data 与 Dify 集成

> 在 Dify 中添加 Bright Data 网页抓取插件，从 50+ 平台（包括 Amazon、LinkedIn 和 Instagram）提取数据，并支持搜索和 markdown。

<Card title="Building an AI startup?" cta="Learn more" href="https://brightdata.com/ai/ai-startups-program" icon="rocket-launch" iconType="duotone" arrow="true">
  You might be eligible for our Startup Program. Get fully funded access to the infrastructure you're reading about right now (up to \$20K value).
</Card>

Bright Data 的 Dify 插件可将结构化网页数据、搜索结果和页面 markdown 引入你的 Dify 工作流。从 Dify Marketplace 安装该插件，添加你的 Bright Data API 密钥，然后将抓取工具拖入任意工作流。它覆盖 50+ 平台，包括 Amazon、LinkedIn、Instagram 和 YouTube。

<Frame>
  ![在 Dify 工作流中使用 Bright Data 插件提取 Amazon 商品数据并通过 LLM 节点生成摘要](https://github.com/user-attachments/assets/5825d274-d47b-4fed-950f-65e6b7c63e58)
</Frame>

<Note>
  如需查看最新的插件更新，请访问 [Bright Data Dify 插件仓库](https://github.com/brightdata/brightdata-dify-plugin/blob/main/BrightData/brightdata-dify-plugin/README.md)。
</Note>

## 前提条件

* 一个拥有 [API 密钥](/cn/api-reference/authentication#api-key) 的 [Bright Data 账户](https://www.bright.cn/cp)
* 一个可访问 Dify Studio 的 Dify 账户

## 如何将 Bright Data 插件添加到 Dify

<Steps>
  <Step title="安装插件">
    从 [Dify Marketplace](https://marketplace.dify.ai/plugins/idanvilenski/brightdata) 安装 Bright Data 插件。
  </Step>

  <Step title="获取你的 Bright Data API 密钥">
    * 登录你的 [Bright Data 仪表盘](https://www.bright.cn/cp)。
    * 前往 [账户设置](https://www.bright.cn/cp/setting/users)。
    * 如果还没有创建，请 [生成一个 API 密钥](/cn/api-reference/authentication#api-key)。
  </Step>

  <Step title="将抓取工具添加到工作流">
    1. 进入 **Dify Studio** 并打开一个 **Workflow**。
    2. 添加任意一个 Bright Data 工具：
       * **Structured Data Feeds**（结构化数据源）：从 50+ 平台提取结构化数据
       * **Scrape As Markdown**（抓取为 Markdown）：将任意网页转换为干净的 markdown
       * **Search Engine**（搜索引擎）：从 Google、Bing 或 Yandex 获取搜索结果
    3. 在提示时输入你的 Bright Data API 密钥。
    4. 连接一个 **LLM 节点** 来处理或总结抓取到的数据。
  </Step>

  <Step title="运行示例工作流">
    上方的横幅图片展示了该工作流。要提取 Amazon 商品信息并生成摘要：

    1. **START**：输入商品 URL
    2. **Structured Data Feeds**：提取商品详情
    3. **LLM**：总结为易读文本
    4. **END**：输出干净的商品摘要

    <Note>
      构建可靠工作流的两个提示：

      * 每一步都引用上一步的输出
      * 在输入字段中设置较高的字符限制（URL 字段请选择 “short paragraph” 变量类型）
    </Note>
  </Step>
</Steps>

## 可用工具

该插件为 Dify 添加了三个工具。

### 结构化数据源

从热门平台提取结构化数据：

* **电商**：Amazon、eBay、Walmart、Best Buy、Etsy、Zara
* **社交媒体**：Instagram、Facebook、TikTok、YouTube、X（Twitter）
* **职场**：LinkedIn 个人资料、公司、招聘信息
* **商业**：Crunchbase、ZoomInfo
* **地图与评论**：Google Maps、预订网站
* **新闻**：新闻来源和文章

### 抓取为 Markdown

将任意网页转换为干净、可阅读的 markdown，适用于：

* 内容分析
* 文档提取
* 文章处理

### 跨引擎搜索

从主要搜索引擎获取搜索结果：

* Google
* Bing
* Yandex 等

## 使用场景

* **电商监控**：跟踪商品价格和库存
* **潜在客户开发**：从 LinkedIn 提取商业信息
* **内容研究**：收集文章与新闻用于分析
* **市场调研**：监控竞争对手网站与社交媒体
* **SEO 分析**：跟踪搜索引擎结果与排名

## 高级：使用 Bright Data MCP

Dify 插件使用托管 API。对于高级工作流，你还可以集成 [Bright Data MCP 服务器](/cn/ai/mcp-server/overview)，它通过 Model Context Protocol 公开 Bright Data 全套抓取与自动化工具。

在 Dify 中通过自定义 HTTP 请求或外部服务节点调用 MCP 工具，以添加浏览器自动化和实时抓取等能力。

* [在 GitHub 上探索 MCP](https://github.com/brightdata/brightdata-mcp/tree/main)
* [在 Smithery Playground 中试用 MCP](https://smithery.ai/server/@luminati-io/brightdata-mcp/tools)
