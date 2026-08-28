> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 常见问题解答：MCP

> 查找有关集成、配置和使用 Bright Data MCP 服务器的常见问题解答。

<AccordionGroup>
  <Accordion title="什么是 Bright Data MCP 服务器？">
    Bright Data MCP（Model Context Protocol）是一种服务器，使 LLM、AI 代理和应用能够实时访问、发现和提取网页数据。\
    它允许 MCP 客户端，如 Claude Desktop、Cursor 和 Windsurf，搜索网页、浏览网站、执行操作并检索数据而不被封锁，非常适合网页抓取任务。\\

    * 对于新的 MCP 用户，我们提供免费层级

    MCP 服务器提供高级功能，包括：

    * 绕过地理限制，无论位置如何都可访问内容
    * 使用解锁技术导航带有机器人检测的网站
    * 从 Amazon、LinkedIn、Instagram 及其他数据源提取结构化数据
    * 远程浏览器自动化以处理复杂网页交互
    * 访问全球 IP 网络以避免封锁或速率限制
      **开始使用 Bright Data MCP：**

    1. [**浏览 MCP GitHub 仓库**](https://github.com/brightdata/brightdata-mcp) 查看源代码、贡献或部署您自己的实例。
    2. [**阅读 MCP 文档**](/cn/ai/mcp-server/overview) 了解 API、请求结构及支持的功能。
    3. [获取您的 API 密钥](https://www.bright.cn/cp/setting/users)
    4. [**尝试 MCP Smithery Playground**](https://smithery.ai/server/@luminati-io/brightdata-mcp/tools) 在无代码环境中测试和实验实时请求。
  </Accordion>

  <Accordion title="Bright Data 免费层有限制吗？">
    是的，每月限制为 5000 次请求。
  </Accordion>

  <Accordion title="我在哪里可以获取 API 密钥？">
    您可以在 Bright Data 账户的 [用户设置页面](https://www.bright.cn/cp/setting/users) 获取 API 令牌。
    确保您在 [brightdata.com](https://brightdata.com) 上有账户——新用户可获得免费测试额度，之后可选择按需付费。
  </Accordion>

  <Accordion title="使用 MCP 服务器需要用户名吗？">
    不需要。Bright Data MCP 服务器仅需要 API 令牌，远程（托管）和本地（自托管）两种方式均是如此。用户名（格式：`brd-customer-{customer_id}-zone-{zone_name}`）仅用于原生代理访问，MCP、SDK 或 API 集成均不需要用户名。

    如果第三方工具或集成要求填写用户名，您可以将其留空，或检查该工具是否实际上是在配置代理访问。
  </Accordion>

  <Accordion title="我如何使用 Bright Data MCP 服务器？">
    Bright Data MCP（Model Context Protocol）是本地服务器，允许 AI 代理、LLM 和开发工具使用 Bright Data 基础设施访问和提取实时网页数据。

    开始使用：[**BrightData-MCP**](/cn/ai/mcp-server/overview)

    **有用链接：**

    * [ MCP GitHub 仓库](https://github.com/brightdata/brightdata-mcp)
    * [ MCP API 文档](/cn/ai/mcp-server/overview)
    * [ 在 Smithery Playground 试用 MCP](https://smithery.ai/server/@luminati-io/brightdata-mcp/tools)
  </Accordion>

  <Accordion title="我可以使用 Bright Data MCP 服务器做什么？">
    Bright Data MCP 允许将实时网页访问集成到 AI 代理或开发工具中。它支持：

    **搜索与抓取**

    * `search_engine`: 搜索 Google、Bing、Yandex
    * `scrape_as_markdown`, `scrape_as_html`: 获取干净格式的内容
    * `session_stats`: 监控工具使用情况

    **结构化数据提取**

    * Amazon: `web_data_amazon_product`, `web_data_amazon_product_reviews`
    * LinkedIn: `web_data_linkedin_person_profile`, `web_data_linkedin_company_profile`
    * Instagram: `web_data_instagram_profiles`, `web_data_instagram_posts`, `web_data_instagram_reels`
    * Facebook: `web_data_facebook_posts`, `web_data_facebook_marketplace_listings`
    * 其他: `web_data_x_posts`, `web_data_youtube_videos`, `web_data_zillow_properties_listing`

    **浏览器自动化**

    * `scraping_browser_navigate`, `scraping_browser_click`, `scraping_browser_type`
    * `scraping_browser_get_html`, `scraping_browser_screenshot`, `scraping_browser_wait_for`

    **🔗 工具完整列表:** [GitHub 上的 MCP 工具](https://github.com/brightdata-com/brightdata-mcp/blob/main/assets/Tools.md)
  </Accordion>

  <Accordion title="哪些 AI 代理和工具可以集成 Bright Data MCP 服务器？">
    Bright Data MCP 旨在与多种 AI 工具和代理协作，包括：

    * **Claude Desktop** (Anthropic)
    * **Cursor IDE**
    * **Windsurf**
    * **LangChain**
    * **AutoGPT / AgentGPT**
    * **Smithery**
    * **支持 HTTP 请求的自定义 LLM 或 AI 代理**

    这些工具可以使用 MCP：

    * 执行实时网页搜索
    * 抓取结构化数据
    * 自动化浏览器操作
    * 访问地理限制或受保护内容

    现场试用：[Smithery Playground](https://smithery.ai/server/@luminati-io/brightdata-mcp/tools)
  </Accordion>

  <Accordion title="如何启用浏览器控制工具？">
    启用浏览器控制工具：

    1. 访问您的 Bright Data 控制面板：[brightdata.com/cp/zones](https://www.bright.cn/cp/zones)
    2. 创建一个新的“Browser API”区域
    3. 创建完成后，从 Browser API 概览标签复制认证字符串
    4. 认证字符串格式如下：`brd-customer-[您的客户ID]-zone-[您的区域ID]:[您的密码]`
    5. 将该认证字符串添加到 MCP 配置中作为 `BROWSER_AUTH` 环境变量
  </Accordion>

  <Accordion title="Bright Data MCP 服务器有哪些工具可用？">
    完整工具列表请参考我们的 GitHub 仓库：[MCP 工具](https://github.com/brightdata-com/brightdata-mcp/blob/main/assets/Tools.md)
    Bright Data MCP 提供全面的工具集，包括：
    **搜索与基础抓取：**

    * `search_engine`: 抓取 Google、Bing 或 Yandex 的搜索结果
    * `scrape_as_markdown`: 抓取网页并以 Markdown 格式获取结果
    * `scrape_as_html`: 抓取网页并以 HTML 格式获取结果
    * `session_stats`: 查看当前会话中的工具使用情况
      **结构化数据提取：**
    * Amazon: `web_data_amazon_product`, `web_data_amazon_product_reviews`
    * LinkedIn: `web_data_linkedin_person_profile`, `web_data_linkedin_company_profile`
    * ZoomInfo: `web_data_zoominfo_company_profile`
    * Instagram: `web_data_instagram_profiles`, `web_data_instagram_posts`, `web_data_instagram_reels`, `web_data_instagram_comments`
    * Facebook: `web_data_facebook_posts`, `web_data_facebook_marketplace_listings`, `web_data_facebook_company_reviews`
    * 其他: `web_data_x_posts`, `web_data_zillow_properties_listing`, `web_data_booking_hotel_listings`, `web_data_youtube_videos`
      **浏览器自动化：**
    * `scraping_browser_navigate`: 导航到 URL
    * `scraping_browser_go_back`/`scraping_browser_go_forward`: 浏览器历史导航
    * `scraping_browser_click`: 点击元素
    * `scraping_browser_links`: 获取当前页面的所有链接
    * `scraping_browser_type`: 向元素输入文本
    * `scraping_browser_wait_for`: 等待元素出现
    * `scraping_browser_screenshot`: 截屏
    * `scraping_browser_get_html`/`scraping_browser_get_text`: 获取页面内容
  </Accordion>

  <Accordion title="使用 Bright Data MCP 服务器时如何处理超时问题？">
    某些网页数据工具可能需要更长时间执行，尤其是处理复杂网站时。为确保您的代理能够获取数据：

    1. 在代理设置中设置足够高的超时时间（建议 180 秒，适用于 99% 的请求）
    2. 对于特别慢的网站，可能需要进一步增加该值
    3. 尽可能使用专门的 `web_data_*` 工具，它们通常比通用抓取更快
    4. 对于浏览器自动化操作序列，将操作尽量时间接近
  </Accordion>

  <Accordion title="我应该注意哪些安全事项？">
    始终将抓取的网页内容视为不可信数据。不要将原始抓取内容直接用于 LLM 提示，以避免潜在提示注入风险。
    应该：

    * 过滤并验证所有网页数据后再传给 LLM
    * 尽量使用结构化数据提取而非原始文本
    * 对执行抓取内容中的 JavaScript 保持谨慎
  </Accordion>

  <Accordion title="为什么会出现 'spawn npx ENOENT' 错误？">
    当系统找不到 `npx` 命令时，会出现此错误。解决方法：

    1. 找到 Node.js 路径：
       * macOS: 在终端运行 `which node`
       * Windows: 在命令提示符运行 `where node`
    2. 在 MCP 配置中使用完整路径替换 `npx`：

    ```json theme={null}
    {
      "mcpServers": {
        "Bright Data": {
          "command": "/usr/local/bin/node", // 替换为实际 Node.js 路径
          "args": ["node_modules/@brightdata/mcp/index.js"],
          "env": {
            "API_TOKEN": "<your-api-token>"
          }
        }
      }
    }
    ```
  </Accordion>

  <Accordion title="如何监控使用情况和费用？">
    您可以使用 `session_stats` 工具查看当前会话的使用情况。要获得完整的使用跟踪和账单信息，请登录 Bright Data 账户仪表板。
    `session_stats` 工具会显示：

    * 当前会话的请求次数
    * 使用的工具及使用频率
  </Accordion>

  <Accordion title="是否有试用 MCP 的 playground？">
    是的，您可以在 [Smithery](https://smithery.ai/server/@luminati-io/brightdata-mcp/tools) playground 上无需任何设置试用 Bright Data MCP。
    该平台提供了无需本地设置即可探索 Bright Data MCP 功能的简便方式。只需登录即可开始实验网页数据采集！
  </Accordion>

  <Accordion title="如何将我的 AI 代理连接到 Bright Data MCP？" iconType="solid">
    您可以通过以下方式将 AI 代理连接到 Bright Data：

    * 安装 [Node.js 包](https://nodejs.org/en/download)
    * 创建 [Bright Data 账户](https://www.bright.cn/?hs_signup=1\&utm_source=docs)（新用户获得免费测试额度）
    * 从 [用户设置页面](https://www.bright.cn/cp/setting/users) 复制 API 密钥（新用户将在欢迎邮件中收到 **API key**）
    * 使用 API 密钥配置代理。更多示例，请访问 [GitHub](https://github.com/brightdata/brightdata-mcp?tab=readme-ov-file#-usage-examples) 或查阅 [MCP 文档](/cn/ai/mcp-server/overview#configuration)
  </Accordion>

  <Accordion title="使用 MCP 时，我需要创建或配置 zones 吗？">
    不需要，我们会为您创建 :) 您只需要 NodeJS 和 BrightData API 密钥。如果您想将 zone 名称改为特定名称，也可以随时更改。
  </Accordion>

  <Accordion title="Bright Data MCP 有免费访问层吗？">
    * 有！Bright Data 为新的 MCP 用户提供每月 **5000 次请求** 的免费层。
  </Accordion>

  <Accordion title="如何为浏览器 API MCP 设置国家？">
    当前 MCP（Model Context Protocol）集成不支持在 MCP 配置中通过专用国家参数直接设置国家。但您可以通过在 MCP 设置中指定自定义 zone，并在 Bright Data 控制面板中配置该 zone 的国家，实现国家控制。

    实现方法如下：

    1. **为目标国家创建 Zone：**
       * 在 Bright Data 控制面板中创建新 zone（如 Residential、Mobile 或 Browser API），并在 zone 配置中将地理定位设置为所需国家。
    2. **在 MCP 配置中指定 Zone：**
       * 在 MCP 客户端配置中，使用相关 zone 的环境变量：
         * 网页抓取: `WEB_UNLOCKER_ZONE`
         * 浏览器自动化: `BROWSER_ZONE`
       * 示例（自定义浏览器 zone）：

         ```json theme={null}
         {
           "mcpServers": {
             "Bright Data": {
               "command": "npx",
               "args": ["@brightdata/mcp"],
               "env": {
                 "API_TOKEN": "<your_api_key>",
                 "BROWSER_ZONE": "<your_zone_name>"
               }
             }
           }
         }
         ```
       * 确保 `<your_zone_name>` 是为特定国家配置的 zone。
    3. **通过 MCP 的请求现在将使用该 zone 设置的国家目标。**

    更多详情，请参见 [MCP 服务器文档](/cn/ai/mcp-server/overview) 和 [Browser API 位置定位](/cn/scraping-automation/scraping-browser/features/proxy-location?_gl=1*g3vjv6*_gcl_au*OTk4MjcxMzc1LjE3NTQyOTAyMDQ.*_ga*NjYwNjM1MTUwLjE3NTQyOTAyMDQ.*_ga_KQX3XWKR2T*czE3NTQyOTAyMDQkbzEkZzEkdDE3NTQyOTA0MzMkajUxJGwwJGgw)。
  </Accordion>

  <Accordion title="什么是 MCP 免费层？">
    MCP 免费层允许您通过 MCP（Model Context Protocol）免费连接 AI 代理到 Bright Data 服务。\
    每月可免费进行最多 5000 次请求，抓取搜索结果并解锁任意公共网页，非常适合测试、开发或轻量使用。免费层可访问静态和动态网页内容，包括网页解锁、浏览器自动化和结构化数据提取等功能。\
    \
    更多信息，请参见：[https://docs.brightdata.com/cn/ai/mcp-server/remote/quickstart](https://docs.brightdata.com/cn/ai/mcp-server/remote/quickstart)
  </Accordion>
</AccordionGroup>
