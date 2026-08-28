> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Bright Data CLI

> 从终端抓取网站、搜索网络、从40多个平台提取结构化数据，以及管理你的 Bright Data 账户。

<Card title="60秒快速开始" icon="rocket" href="/cn/cli/installation" cta="立即安装">
  安装 CLI，登录一次，然后开始抓取 - CAPTCHA、反爬虫保护和 JavaScript 渲染会自动处理。
</Card>

## 使用 CLI 可以做什么?

<CardGroup cols={3}>
  <Card title="抓取任何网站" icon="globe">
    从任何 URL 获取干净的 Markdown、HTML、JSON 或截图 - 包括反爬虫绕过和 JS 渲染。
  </Card>

  <Card title="搜索网络" icon="magnifying-glass">
    查询 Google、Bing 或 Yandex 并获取结构化结果，包括有机列表、广告和人们也在搜索的内容。
  </Card>

  <Card title="提取结构化数据" icon="table">
    从 Amazon、LinkedIn、Instagram 和 TikTok 等 40+ 个平台提取产品详情、资料、评论等信息。
  </Card>

  <Card title="管理区域和预算" icon="gauge">
    列出代理区域、检查配置，以及监控账户余额和各区域成本。
  </Card>

  <Card title="使用管道自动化" icon="pipe-section">
    JSON 输出、文件导出和对管道友好的设计使链接命令和构建工作流变得容易。
  </Card>

  <Card title="为 AI 代理赋能" icon="robot">
    将预构建的技能安装到 Claude Code、Cursor、Copilot 和其他 AI 编码代理中。
  </Card>
</CardGroup>

## 快速浏览

```bash theme={null}
# 将页面抓取为清晰的 Markdown
brightdata scrape https://news.ycombinator.com

# 搜索 Google 并获取结构化结果
brightdata search "best web scraping tools 2025"

# 将 Amazon 产品提取为 JSON
brightdata pipelines amazon_product "https://amazon.com/dp/B09V3KXJPB" --format json

# 获取 LinkedIn 资料
brightdata pipelines linkedin_person_profile "https://linkedin.com/in/username"

# 检查你的账户余额
brightdata budget
```

<Tip>
  CLI 别名 `bdata` 可用作快捷方式 - 例如，`bdata scrape https://example.com`。
</Tip>

## 工作原理

Bright Data CLI 将完整的 Bright Data 网络数据平台包装成简单的终端命令。在幕后，它：

1. **一次性认证** 通过 OAuth、设备流或 API 密钥 - 凭证存储在本地，永远无需再次输入
2. **自动配置代理区域**（`cli_unlocker`、`cli_browser`）在首次登录时，以便你可以立即开始
3. **路由请求** 通过 Bright Data 的基础设施，处理 CAPTCHA、爬虫检测、IP 轮换和 JavaScript 渲染
4. **返回干净的输出** - 在终端中格式化表格，或用于自动化的结构化 JSON/CSV/markdown

## 探索 CLI 资源

<CardGroup>
  <Card title="安装" icon="download" horizontal href="/cn/cli/installation">
    安装 CLI 并使用 Bright Data 进行身份验证。
  </Card>

  <Card title="命令" icon="code" horizontal href="/cn/cli/commands">
    每个命令、标志和选项的完整参考。
  </Card>

  <Card title="使用示例" icon="book-open" horizontal href="/cn/cli/examples">
    常见任务的真实工作流和配方。
  </Card>

  <Card title="常见问题" icon="question" horizontal href="/cn/scraping-automation/cli/faqs">
    常见问题的答案和故障排除提示。
  </Card>
</CardGroup>

<Check>
  **无需配置。** 在一次性 `brightdata login` 之后，每个命令都可以开箱即用 - 无需管理令牌、创建区域或配置代理。
</Check>

```
```
