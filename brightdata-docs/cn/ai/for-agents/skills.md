> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Bright Data 编码代理技能

> 将 Bright Data 技能安装到您的 AI 编码代理中，以获得最佳实践 API 用法、可用脚本和嵌入式产品知识 - 立即可用。

## 什么是技能？

技能是**可重用的指令集** - 定义在 `SKILL.md` 文件中 - 使用 Bright Data API 扩展您的编码代理的功能。每项技能为您的代理提供嵌入式最佳实践、参数知识和可直接执行的可运行 shell 脚本。

安装 Bright Data 技能后，您的代理立即了解：

* 为搜索、抓取或结构化数据提取调用哪个 API
* 如何正确进行身份验证和构建请求
* 如何处理分页、错误和边界情况
* 可以调用以采取行动的真实脚本

技能是[开放代理技能生态系统](https://github.com/vercel-labs/skills)的一部分，可跨 40+ 编码代理工作。Bright Data 的技能托管在 [github.com/brightdata/skills](https://github.com/brightdata/skills)。

***

## 可用技能

<CardGroup cols={2}>
  <Card title="搜索" icon="magnifying-glass" href="https://github.com/brightdata/skills" cta="在 GitHub 上查看">
    搜索 Google 并获取带有标题、链接和描述的结构化 JSON 结果。支持分页。由 Bright Data SERP API 提供支持。
  </Card>

  <Card title="抓取" icon="unlock" href="https://github.com/brightdata/skills" cta="在 GitHub 上查看">
    将任何网页抓取为清洁的 markdown，具有自动机器人检测绕过、验证码解决和 JavaScript 呈现。由 Web Unlocker API 提供支持。
  </Card>

  <Card title="数据源" icon="database" href="https://github.com/brightdata/skills" cta="在 GitHub 上查看">
    从 40+ 个网站提取结构化数据 - Amazon、LinkedIn、Instagram、TikTok、YouTube、eBay、Walmart 等 - 具有自动轮询。
  </Card>

  <Card title="Bright Data MCP" icon="server" href="https://github.com/brightdata/skills" cta="在 GitHub 上查看">
    在单个集成中协调 60+ MCP 工具，用于搜索、抓取、结构化提取和浏览器自动化。
  </Card>

  <Card title="最佳实践" icon="star" href="https://github.com/brightdata/skills/tree/main/skills/bright-data-best-practices" cta="在 GitHub 上查看">
    编码代理的生产就绪 API 参考。涵盖 Web Unlocker、SERP API、Scrapers 和 Browser API - 包含 API 选择指南、身份验证模式和 Python 和 JavaScript 代码示例。
  </Card>
</CardGroup>

***

## 快速开始

<Steps>
  <Step title="先决条件">
    安装必需的 CLI 工具并设置您的 Bright Data 凭证：

    ```bash theme={null}
    # macOS
    brew install curl jq

    # Ubuntu / Debian
    sudo apt-get install curl jq
    ```

    ```bash theme={null}
    export BRIGHTDATA_API_KEY="your-api-key"
    export BRIGHTDATA_UNLOCKER_ZONE="your-zone-name"
    ```

    从 [Bright Data 用户设置页面](https://www.bright.cn/cp/setting/users)获取您的 API 密钥。要创建 Web Unlocker 区域，请参阅 [Web Unlocker 快速开始](/cn/scraping-automation/web-unlocker/quickstart)。
  </Step>

  <Step title="使用 npx skills 安装">
    使用 `npx skills` CLI 将 Bright Data 技能安装到您的代理中：

    ```bash theme={null}
    # 安装所有技能（自动检测您安装的代理）
    npx skills add brightdata/skills

    # 仅安装到特定代理
    npx skills add brightdata/skills -a claude-code
    npx skills add brightdata/skills -a cursor

    # 仅安装特定技能
    npx skills add brightdata/skills --skill search
    npx skills add brightdata/skills --skill scrape
    npx skills add brightdata/skills --skill data-feeds
    npx skills add brightdata/skills --skill bright-data-best-practices

    # 全局安装（在您的所有项目中可用）
    npx skills add brightdata/skills -g
    ```

    CLI 检测您安装的代理并自动将技能文件放在正确的目录中。
  </Step>

  <Step title="在您的代理中使用技能">
    安装后，您的代理可以直接运行这些技能：

    ```bash theme={null}
    # 搜索 Google
    bash skills/search/scripts/search.sh "your query" [page]

    # 将 URL 抓取为清洁的 markdown
    bash skills/scrape/scripts/scrape.sh "https://example.com"

    # 提取结构化数据（运行时不带参数以查看所有 40+ 数据集类型）
    bash skills/data-feeds/scripts/datasets.sh

    # 使用特定数据集类型和 URL
    bash skills/data-feeds/scripts/datasets.sh amazon_product "https://amazon.com/dp/ASIN"
    bash skills/data-feeds/scripts/datasets.sh linkedin_person_profile "https://linkedin.com/in/username"
    ```
  </Step>
</Steps>

***

## 每个代理的安装

<Tabs>
  <Tab title="Claude Code">
    ```bash theme={null}
    npx skills add brightdata/skills -a claude-code
    ```

    技能安装到项目中的 `.claude/skills/` 中（或使用 `-g` 全局的 `~/.claude/skills/`）。Claude Code 在下一个会话中自动发现它们。

    要验证安装：

    ```bash theme={null}
    npx skills list -a claude-code
    ```
  </Tab>

  <Tab title="Cursor">
    ```bash theme={null}
    npx skills add brightdata/skills -a cursor
    ```

    技能位于项目中的 `.cursor/skills/`。Cursor Composer 会自动获取它们。在聊天中引用它们：

    ```
    使用抓取技能从 https://example.com 提取内容
    ```
  </Tab>

  <Tab title="Windsurf">
    ```bash theme={null}
    npx skills add brightdata/skills -a windsurf
    ```

    Windsurf 的 Cascade 从 `.windsurf/skills/` 读取技能并自动将其加载到其上下文中。
  </Tab>

  <Tab title="一次安装所有代理">
    ```bash theme={null}
    # 安装到您安装的每个代理
    npx skills add brightdata/skills --all

    # 非交互式（CI/CD 友好）
    npx skills add brightdata/skills --all -y
    ```

    CLI 自动检测所有已安装的代理并将技能文件分发给每一个。
  </Tab>

  <Tab title="手动 / 任何代理">
    克隆存储库并直接引用 `SKILL.md` 文件：

    ```bash theme={null}
    git clone https://github.com/brightdata/skills.git
    ```

    每项技能的 `SKILL.md` 是纯 markdown - 将其注入任何代理的系统提示、RAG 索引或上下文窗口中：

    ```bash theme={null}
    cat skills/search/SKILL.md                      # 粘贴到系统提示中
    cat skills/scrape/SKILL.md
    cat skills/data-feeds/SKILL.md
    cat skills/bright-data-best-practices/SKILL.md  # API 选择 + 最佳实践
    ```
  </Tab>
</Tabs>

***

## 技能结构

每项 Bright Data 技能遵循标准技能格式：

```
skills/
├── search/
│   ├── SKILL.md              # 说明 + 元数据 - 由代理加载
│   └── scripts/
│       └── search.sh         # 代理可以运行的��执行脚本
├── scrape/
│   ├── SKILL.md
│   └── scripts/
│       └── scrape.sh
├── data-feeds/
│   ├── SKILL.md
│   └── scripts/
│       ├── datasets.sh       # 数据集包装器（40+ 类型）
│       └── fetch.sh          # 核心轮询 + 响应处理
├── bright-data-mcp/
│   ├── SKILL.md
│   └── references/           # MCP 工具参考文档
└── bright-data-best-practices/
    ├── SKILL.md              # API 选择指南 + 身份验证模式 + 代码示例
    └── references/
        ├── web-unlocker.md   # 完整 Web Unlocker 参考
        ├── serp-api.md       # 完整 SERP API 参考（Google、Bing、Maps、Trends...）
        ├── scrapers.md       # Scrapers 参考（100+ 平台）
        └── browser-api.md    # Browser API 参考（CDP 函数、地理位置、验证码）
```

`SKILL.md` 包含带有 `name` 和 `description` 的 YAML 前置内容，后跟结构化说明，告诉代理何时以及如何使用该技能。

***

## 数据源覆盖范围

数据源技能支持来自四个类别中 40+ 个平台的结构化提取：

<CardGroup cols={2}>
  <Card title="电子商务" icon="cart-shopping">
    Amazon（产品、评论、搜索）、Walmart、eBay、Best Buy、Etsy、Home Depot、Zara、Google Shopping
  </Card>

  <Card title="专业网络" icon="briefcase">
    LinkedIn（个人资料、公司、职位、帖子）、Crunchbase、ZoomInfo
  </Card>

  <Card title="社交媒体" icon="share-nodes">
    Instagram、TikTok、Facebook、X/Twitter、YouTube、Reddit
  </Card>

  <Card title="其他" icon="globe">
    Google Maps 评论、Yahoo Finance、Zillow、Booking.com、GitHub、App Stores
  </Card>
</CardGroup>

***

## 管理您的技能

```bash theme={null}
# 列出所有已安装的技能
npx skills list

# 检查更新
npx skills check

# 将所有技能更新到最新版本
npx skills update

# 删除一项技能
npx skills remove brightdata/skills
```

***

<Tip>
  为了获得最丰富的代理设置，将技能与 [Bright Data MCP 服务器](/ai/mcp-server/overview)结合使用。技能为您的代理提供嵌入式知识和可运行脚本；MCP 服务器为其提供实时网络访问，包含 60+ 工具 - 所有这些都无需离开您的编码环境。
</Tip>

<Info>
  新技能定期添加。Star [GitHub 存储库](https://github.com/brightdata/skills)以保持更新。
</Info>
