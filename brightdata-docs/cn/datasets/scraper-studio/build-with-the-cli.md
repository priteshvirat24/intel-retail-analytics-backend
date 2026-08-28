> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 使用 Bright Data CLI 构建爬虫

> 使用 Bright Data CLI，在您的终端或 Claude Code、Cursor 等编码助手中创建、运行并自我修复 Scraper Studio 爬虫。

Bright Data CLI 可在您的终端中通过三条命令构建 Bright Data Scraper Studio 爬虫：使用 `bdata login` 登录，然后运行 `bdata scraper create` 和 `bdata scraper run`。通过 `npx` 按需运行，无需安装任何东西。本教程将带您端到端构建一个 Hacker News 头条新闻爬虫。该 CLI 在 Claude Code、Cursor 或 Codex 等编码助手的内嵌终端中可原样运行。

**预计用时：** 约 10 分钟（AI 生成在后台运行）

## 前提条件

* 一个 Bright Data 账户（[免费注册](https://www.bright.cn/?hs_signup=1\&utm_source=docs)，无需信用卡）
* 一个可使用 `npx` 的终端（`npx` 随 Node.js 20 或更高版本一起提供）。任何内嵌终端同样适用：Claude Code、Cursor、Codex、VS Code

## 使用 npx 运行 Bright Data CLI

无需安装任何东西。通过 `npx` 按需运行 CLI，它每次都会获取最新版本：

```bash theme={null}
npx -p @brightdata/cli bdata --version
```

为了让本教程后续的命令保持简短，请为当前 shell 会话设置 `bdata` 别名。否则，请在下面每个 `bdata` 命令前加上 `npx -p @brightdata/cli`：

```bash theme={null}
alias bdata="npx -p @brightdata/cli bdata"
```

该 CLI 在 npm 上发布为 `@brightdata/cli`。`bdata` 和 `brightdata` 命令可以互换使用。相比 npx 更想要一个持久可用的命令？使用 `npm install -g @brightdata/cli` 进行全局安装。

## 在终端构建您的第一个爬虫

<Steps>
  <Step title="登录">
    运行 `bdata login`。CLI 会打开一个浏览器标签页，让您授权访问 Bright Data 账户，然后将 API key 保存到本地。您无需粘贴或复制 key。

    ```bash theme={null}
    bdata login
    ```

    > **预期结果：**
    >
    > ```text theme={null}
    > Opening browser for Bright Data authentication...
    > Logged in successfully. Key: 2e75****12bf
    > Checking for required zones...
    > Zone "cli_unlocker" already exists.
    > Zone "cli_browser" already exists.
    > ```

    这两个 zone（`cli_unlocker` 和 `cli_browser`）是 CLI 运行爬虫时使用的 Web Unlocker API 和 Browser API 端点。Bright Data 会在首次登录时自动创建它们。
  </Step>

  <Step title="创建爬虫">
    传入一个目标 URL 和一句描述您想要的数据的话。Bright Data 的 AI Agent 会生成输出 schema、编写爬虫代码并返回一个 Collector ID。

    ```bash theme={null}
    bdata scraper create https://news.ycombinator.com \
      "Extract top stories: title, url, points, author, comment count"
    ```

    AI 流水线分七个阶段实时输出：`user_intent_analyzer`、`planner`、`collector_maintainer`、`output_schema_generator`、`code_generator`、`input_schema_generator`、`preview_runner` 和 `preview_picker`。通常耗时 5 到 15 分钟；复杂目标可能需要长达 25 分钟。

    > **预期结果：**
    >
    > ```text theme={null}
    > Template created: c_mpohus372o5tmid1jk
    > Triggering AI generation...
    > Generating scraper...
    > Step: user_intent_analyzer — polling (attempt 1/600)
    > ...
    > Done in 280 poll attempts.
    > {"status":"done","completed_steps":[...],"step":"preview_picker"}
    > ```

    保存 Collector ID（即 `c_*` 字符串）。它是后续每次运行、调度或 API 调用的稳定句柄。
  </Step>

  <Step title="运行爬虫">
    传入 Collector ID 和一个 URL。使用 `--pretty` 美化 JSON 输出。

    ```bash theme={null}
    bdata scraper run c_mpohus372o5tmid1jk https://news.ycombinator.com --pretty
    ```

    CLI 会先尝试实时模式。如果爬虫触发的页面数超过实时模式允许的上限，CLI 会静默切换到批处理模式（`POST /dca/trigger`，然后轮询 `GET /dca/dataset`）继续执行。无需任何参数。

    > **预期结果：** 一个 JSON 数组，每条结果对应一行。
    >
    > ```json theme={null}
    > [
    >   {
    >     "title": "Last.fm is now independent",
    >     "url": "https://support.last.fm/t/last-fm-is-now-independent/118591",
    >     "points": 447,
    >     "author": "twistslider",
    >     "comment_count": 131
    >   },
    >   {
    >     "title": "DuckDuckGo search saw 28% more visits after Google said people love AI mode",
    >     "url": "https://www.pcgamer.com/hardware/duckduckgos-ai-free-search-saw-nearly-28-percent-more-visits-in-the-week-following-googles-insistence-that-people-love-ai-mode/",
    >     "points": 418,
    >     "author": "HelloUsername",
    >     "comment_count": 212
    >   }
    > ]
    > ```
  </Step>
</Steps>

## 如何在 Claude Code、Cursor 或 Codex 中使用？

Bright Data CLI 可在任意内嵌终端中原样运行。编码助手本身并不构建爬虫；构建工作由 CLI 调用 Bright Data 的 AI Agent 完成，编码助手只是代您调用 CLI。

有两种集成方式让 CLI 在编码助手中更加原生：

**在助手的规则文件中固定 Collector ID**，让助手在多次会话中复用您的爬虫，而不是每次都重新构建：

```text CLAUDE.md / .cursor/rules / CODEX.md theme={null}
SCRAPER_STUDIO_COLLECTOR_ID=c_mpohus372o5tmid1jk
HACKER_NEWS_SCRAPER_USAGE="bdata scraper run $SCRAPER_STUDIO_COLLECTOR_ID <url> --pretty"
```

**通过 `brightdata add mcp` 将 Bright Data MCP 服务器接入您的助手**。MCP 服务器与 Scraper Studio CLI 相互独立，但能为助手提供可直接调用的额外抓取工具（`scrape_as_markdown`、`search_engine` 等）：

```bash theme={null}
brightdata add mcp                # 交互式：选择 Claude Code、Cursor 或 Codex
```

参阅 [Bright Data MCP 服务器快速开始](/cn/ai/mcp-server-quickstart)了解 MCP 提供的能力。

## 刚才发生了什么？

三条 CLI 命令对应四个 Bright Data Scraper Studio API 端点。当您准备不通过 CLI 直接集成时，可用下表将 CLI 流程映射到原始 HTTP 调用：

| 您执行的命令                     | 背后的 Bright Data API 端点                                                  |
| -------------------------- | ----------------------------------------------------------------------- |
| `bdata login`              | 本地凭据存储。读取来自[账户设置](https://brightdata.com/cp/setting)的 API key。          |
| `bdata scraper create`     | `POST /dca/collector`，随后 `POST /dca/collectors/{c_*}/automate_template` |
| `bdata scraper run`（输入较少时） | `POST /dca/trigger_immediate`，随后 `GET /dca/get_result`                  |
| `bdata scraper run`（输入较多时） | `POST /dca/trigger`，随后轮询 `GET /dca/dataset?id=j_*`                      |

完整的 cURL、Python 和 Node.js 调用示例参见 [Bright Data Scraper Studio API 快速开始](/cn/datasets/scraper-studio/quickstart)。完整端点参考参见 [Scraper Studio API 参考](/cn/api-reference/scraper-studio-api/Getting_started_wtih_the_API)。

## 如何在目标站点变化时修复爬虫？

当目标站点改版、爬虫开始返回 null 或缺失字段时，使用 `bdata scraper heal` 就地修复。自我修复会保留相同的 Collector ID，因此引用该爬虫的每一次触发、调度和集成都能继续工作。流程是：运行、检查、修复（heal）、批准（approve）、重新运行。

<Steps>
  <Step title="修复爬虫">
    传入 Collector ID 和一句描述问题的自然语言。提示词请保持在 1,000 字符以内。

    ```bash theme={null}
    bdata scraper heal c_mpohus372o5tmid1jk \
      "The points and comment_count fields return null since the site redesign. Re-capture them from the new markup." \
      --url https://news.ycombinator.com
    ```

    默认情况下，`heal` 会停在批准关口，让您在修复上线前先审查。

    > **预期结果：** 命令返回一个信封对象，其中 `status` 为 `"awaiting_approval"`，`preview_result` 展示所提议修复的示例输出，并附带 `next_step` 提示告诉您下一步该运行什么命令。
  </Step>

  <Step title="批准或拒绝修复">
    审查预览。如果无误，批准它。修复会提交到现有爬虫，Collector ID 不变。

    ```bash theme={null}
    bdata scraper approve c_mpohus372o5tmid1jk --url https://news.ycombinator.com
    ```

    若要放弃所提议的修复并改用更精确的提示词，拒绝它：

    ```bash theme={null}
    bdata scraper approve c_mpohus372o5tmid1jk --reject
    ```

    > **预期结果：** 批准后，`status` 推进到 `done`。拒绝后，爬虫保持不变，您可以用更清晰的提示词重新运行 `heal`。
  </Step>

  <Step title="重新运行以验证">
    在同一 URL 上运行修复后的爬虫，确认此前损坏的字段已重新填充。

    ```bash theme={null}
    bdata scraper run c_mpohus372o5tmid1jk https://news.ycombinator.com --pretty
    ```
  </Step>
</Steps>

<Tip>
  对于无人值守的工作流，在 `heal` 命令中加上 `--auto-approve`。它会自动批准修复并一路轮询到 `done`。仅在您信任该修复、无需人工审查时使用。
</Tip>

## 常见问题

<AccordionGroup>
  <Accordion title="为什么 `bdata scraper create` 用了超过 10 分钟？">
    AI 生成时间取决于目标的复杂度。简单的单页爬虫一般 5 到 10 分钟即可完成；带懒加载、分页或反机器人挑战的页面可能需要 15 到 25 分钟。CLI 每五秒轮询一次 Bright Data 的 AI Flow API 并打印当前阶段，因此您可以让它继续运行，稍后再回来查看。等待期间无需任何操作。
  </Accordion>

  <Accordion title="为什么 CLI 在运行中途从实时模式切换到批处理模式？">
    实时模式对每次请求的页面加载数有上限。当爬虫触发的页面数超过实时模式允许的上限时，CLI 会打印 `Realtime page limit exceeded, switching to batch mode...`，将相同的输入提交到 `POST /dca/trigger`，并轮询 `GET /dca/dataset?id=j_*` 直到快照就绪。此切换是自动的，最终 JSON 数据结构保持一致。页面加载上限请参阅 [Scraper Studio 规格说明](/cn/datasets/scraper-studio/specifications)。
  </Accordion>

  <Accordion title="为什么有些行缺少 `points` 或 `comment_count` 字段？">
    AI Agent 生成的 schema 是逐行尽力而为的，并非严格匹配。Hacker News 上的招聘帖、"Show HN" 帖和非常新的提交并不总是有 points 或评论数，因此爬虫会在该行省略这些字段，而不是编造数值。在您自己的代码中请将缺失字段视为 `null`。如需强制更严格的 schema，请在 [Scraper Studio](/cn/datasets/scraper-studio/ai-agent) 中打开该爬虫，或使用[自我修复工具](/cn/datasets/scraper-studio/self-healing-tool)重写 schema。
  </Accordion>

  <Accordion title="我可以不用 CLI 而从自己的代码触发这个爬虫吗？">
    可以。`bdata scraper create` 返回的 Collector ID（`c_*` 字符串）就是 Bright Data Scraper Studio API 使用的同一个句柄。从任意 HTTP 客户端将它传给 `POST /dca/trigger` 即可。cURL、Python 和 Node.js 示例参见 [Bright Data Scraper Studio API 快速开始](/cn/datasets/scraper-studio/quickstart)。
  </Accordion>

  <Accordion title="当目标站点变化时，如何修复爬虫？">
    使用 `bdata scraper heal` 就地修复，它会保留相同的 Collector ID。完整的运行、修复、批准、重新运行流程见上文[如何在目标站点变化时修复爬虫？](#如何在目标站点变化时修复爬虫)一节。两种替代方案：

    * **控制面板：** 使用[自我修复工具](/cn/datasets/scraper-studio/self-healing-tool)用自然语言描述修复要求。
    * **直接调用 API：** `heal` 和 `approve` 命令封装了一个三步循环。`POST /dca/collectors/{c_*}/refactor_template` 附上提示词，轮询 `GET .../refactor_template/progress` 直到 `status` 为 `pending_answer`，然后 `POST .../resume_automation_job` 批准或拒绝。参见 [Trigger Self-Healing](/cn/api-reference/scraper-studio-api/ai-flow/trigger-self-healing) 和 [Resume Self-Healing Job](/cn/api-reference/scraper-studio-api/ai-flow/resume-self-healing-job)。Node.js 实现参见 [Scraper Studio 自我修复演示](https://github.com/anil-bd/scraper-studio-self-healing-demo)。
  </Accordion>

  <Accordion title="`bdata login` 在没有浏览器的环境（例如 CI）中也能用吗？">
    `bdata login` 命令需要浏览器回调。对于无头环境，请将您的 API key 导出为 `BRIGHTDATA_API_KEY`，CLI 会直接使用它而无需登录步骤：

    ```bash theme={null}
    export BRIGHTDATA_API_KEY="your_api_key_here"
    bdata scraper run c_mpohus372o5tmid1jk https://news.ycombinator.com
    ```

    可从[账户设置](https://brightdata.com/cp/setting)复制 key。
  </Accordion>
</AccordionGroup>

## 相关内容

<CardGroup cols={2}>
  <Card title="使用 AI Agent 构建" icon="wand-magic-sparkles" href="/cn/datasets/scraper-studio/ai-agent">
    在 Bright Data 控制面板中构建相同的爬虫，无需打开终端
  </Card>

  <Card title="Scraper Studio API 快速开始" icon="code" href="/cn/datasets/scraper-studio/quickstart">
    构建完成后，从 cURL、Python 或 Node.js 触发现有爬虫
  </Card>

  <Card title="自我修复工具" icon="screwdriver-wrench" href="/cn/datasets/scraper-studio/self-healing-tool">
    当目标站点变化时，用自然语言提示词修复爬虫
  </Card>

  <Card title="Bright Data CLI 概览" icon="terminal" href="/cn/cli/overview">
    每条 `bdata` 命令及示例
  </Card>
</CardGroup>
