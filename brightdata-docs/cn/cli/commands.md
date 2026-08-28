> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 命令参考

> Bright Data CLI 每个命令的完整参考 - 标志、选项和示例。

## 全局选项

这些标志适用于任何命令：

| 标志                    | 说明            |
| --------------------- | ------------- |
| `-k, --api-key <key>` | 覆盖此请求的 API 密钥 |
| `--timing`            | 显示请求计时信息      |
| `-v, --version`       | 显示 CLI 版本     |

***

## `brightdata login`

使用 Bright Data 进行身份验证。默认在浏览器中打开 OAuth。

| 标志                       | 说明                    |
| ------------------------ | --------------------- |
| `-k, --api-key <key>`    | 直接使用 API 密钥（跳过浏览器）    |
| `-c, --customer-id <id>` | Bright Data 账户 ID（可选） |
| `-d, --device`           | 为 SSH/无头环境使用设备流       |

```bash theme={null}
brightdata login                        # Browser OAuth (recommended)
brightdata login --device               # Headless/SSH environments
brightdata login --api-key <key>        # Direct API key
```

<Tip>
  首次登录时，CLI 会自动创建 `cli_unlocker` 和 `cli_browser` 代理区域并设置合理的默认值。
</Tip>

***

## `brightdata logout`

清除存储的凭证。

```bash theme={null}
brightdata logout
```

***

## `brightdata scrape <url>`

使用 Bright Data 的 Web Unlocker 抓取任何 URL。自动处理验证码、JavaScript 渲染和反爬虫保护。

| 标志                    | 说明                                        |
| --------------------- | ----------------------------------------- |
| `-f, --format <fmt>`  | `markdown`（默认）、`html`、`screenshot`、`json` |
| `--country <code>`    | ISO 国家代码用于地理定位（例如 `us`、`de`、`jp`）         |
| `--zone <name>`       | Web Unlocker 区域名称                         |
| `--mobile`            | 使用移动用户代理                                  |
| `--async`             | 异步提交，返回快照 ID                              |
| `-o, --output <path>` | 将输出写入文件                                   |
| `--json`              | 强制 JSON 输出                                |
| `--pretty`            | 格式化打印 JSON 输出                             |

<CodeGroup>
  ```bash Markdown (default) theme={null}
  brightdata scrape https://news.ycombinator.com
  ```

  ```bash HTML theme={null}
  brightdata scrape https://example.com -f html
  ```

  ```bash JSON with geo-targeting theme={null}
  brightdata scrape https://amazon.com -f json --country us -o product.json
  ```

  ```bash Screenshot theme={null}
  brightdata scrape https://example.com -f screenshot -o page.png
  ```

  ```bash Async mode theme={null}
  brightdata scrape https://example.com --async
  ```

  ```bash Pipe to markdown reader theme={null}
  brightdata scrape https://docs.github.com | glow -
  ```
</CodeGroup>

***

## `brightdata search <query>`

通过 Bright Data 的 SERP API 搜索 Google、Bing 或 Yandex。Google 返回带有有机结果、广��、相关问题和相关搜索的结构化 JSON。Bing 和 Yandex 默认返回 markdown。

| 标志                    | 说明                                   |
| --------------------- | ------------------------------------ |
| `--engine <name>`     | `google`（默认）、`bing`、`yandex`         |
| `--country <code>`    | 本地化结果（例如 `us`、`de`）                  |
| `--language <code>`   | 语言代码（例如 `en`、`fr`）                   |
| `--page <n>`          | 页码，从 0 开始（默认：`0`）                    |
| `--type <type>`       | `web`（默认）、`news`、`images`、`shopping` |
| `--device <type>`     | `desktop`、`mobile`                   |
| `--zone <name>`       | SERP 区域名称                            |
| `-o, --output <path>` | 将输出写入文件                              |
| `--json`              | 强制 JSON 输出                           |
| `--pretty`            | 格式化打印 JSON 输出                        |

<CodeGroup>
  ```bash Basic search theme={null}
  brightdata search "typescript best practices"
  ```

  ```bash Localized search theme={null}
  brightdata search "restaurants berlin" --country de --language de
  ```

  ```bash News search theme={null}
  brightdata search "AI regulation" --type news
  ```

  ```bash Pagination theme={null}
  brightdata search "web scraping" --page 1
  ```

  ```bash Extract URLs with jq theme={null}
  brightdata search "open source scraping" --json | jq -r '.organic[].link'
  ```

  ```bash Bing search theme={null}
  brightdata search "bright data pricing" --engine bing
  ```
</CodeGroup>

***

## `brightdata pipelines <type> [params...] [options]`

从 40 多个平台提取结构化数据。触发异步收集作业，轮询直到结果准备就绪，然后返回数据。

| 标志                    | 说明                                |
| --------------------- | --------------------------------- |
| `--format <fmt>`      | `json`（默认）、`csv`、`ndjson`、`jsonl` |
| `--timeout <seconds>` | 轮询超时（默认：`600`）                    |
| `-o, --output <path>` | 将输出写入文件                           |
| `--json`              | 强制 JSON 输出                        |
| `--pretty`            | 格式化打印 JSON 输出                     |

```bash theme={null}
# List all available pipeline types
brightdata pipelines list
```

<CodeGroup>
  ```bash LinkedIn profile theme={null}
  brightdata pipelines linkedin_person_profile "https://linkedin.com/in/username"
  ```

  ```bash Amazon product theme={null}
  brightdata pipelines amazon_product "https://amazon.com/dp/B09V3KXJPB"
  ```

  ```bash Amazon search theme={null}
  brightdata pipelines amazon_product_search "laptop" "https://amazon.com"
  ```

  ```bash Instagram profile theme={null}
  brightdata pipelines instagram_profiles "https://instagram.com/username"
  ```

  ```bash YouTube comments theme={null}
  brightdata pipelines youtube_comments "https://youtube.com/watch?v=..." 50
  ```

  ```bash CSV export theme={null}
  brightdata pipelines amazon_product "https://amazon.com/dp/..." --format csv -o product.csv
  ```
</CodeGroup>

### 支持的平台

<AccordionGroup>
  <Accordion title="电子商务" icon="cart-shopping">
    | 类型                       | 平台              | 参数                       |
    | ------------------------ | --------------- | ------------------------ |
    | `amazon_product`         | Amazon 产品页面     | `<url>`                  |
    | `amazon_product_reviews` | Amazon 评论       | `<url>`                  |
    | `amazon_product_search`  | Amazon 搜索结果     | `<keyword> <domain_url>` |
    | `walmart_product`        | Walmart 产品页面    | `<url>`                  |
    | `walmart_seller`         | Walmart 卖家资料    | `<url>`                  |
    | `ebay_product`           | eBay 产品列表       | `<url>`                  |
    | `bestbuy_products`       | Best Buy        | `<url>`                  |
    | `etsy_products`          | Etsy            | `<url>`                  |
    | `homedepot_products`     | Home Depot      | `<url>`                  |
    | `zara_products`          | Zara            | `<url>`                  |
    | `google_shopping`        | Google Shopping | `<url>`                  |
  </Accordion>

  <Accordion title="专业网络" icon="briefcase">
    | 类型                         | 平台            | 参数                               |
    | -------------------------- | ------------- | -------------------------------- |
    | `linkedin_person_profile`  | LinkedIn 个人资料 | `<url>`                          |
    | `linkedin_company_profile` | LinkedIn 公司资料 | `<url>`                          |
    | `linkedin_job_listings`    | LinkedIn 职位列表 | `<url>`                          |
    | `linkedin_posts`           | LinkedIn 帖子   | `<url>`                          |
    | `linkedin_people_search`   | LinkedIn 人员搜索 | `<url> <first_name> <last_name>` |
    | `crunchbase_company`       | Crunchbase    | `<url>`                          |
    | `zoominfo_company_profile` | ZoomInfo      | `<url>`                          |
  </Accordion>

  <Accordion title="社交媒体" icon="hashtag">
    | 类型                              | 平台                   | 参数                     |
    | ------------------------------- | -------------------- | ---------------------- |
    | `instagram_profiles`            | Instagram 资料         | `<url>`                |
    | `instagram_posts`               | Instagram 帖子         | `<url>`                |
    | `instagram_reels`               | Instagram 短视频        | `<url>`                |
    | `instagram_comments`            | Instagram 评论         | `<url>`                |
    | `facebook_posts`                | Facebook 帖子          | `<url>`                |
    | `facebook_marketplace_listings` | Facebook Marketplace | `<url>`                |
    | `facebook_company_reviews`      | Facebook 评论          | `<url> [num_reviews]`  |
    | `facebook_events`               | Facebook 活动          | `<url>`                |
    | `tiktok_profiles`               | TikTok 资料            | `<url>`                |
    | `tiktok_posts`                  | TikTok 帖子            | `<url>`                |
    | `tiktok_shop`                   | TikTok 店铺            | `<url>`                |
    | `tiktok_comments`               | TikTok 评论            | `<url>`                |
    | `x_posts`                       | X（Twitter）帖子         | `<url>`                |
    | `youtube_profiles`              | YouTube 频道           | `<url>`                |
    | `youtube_videos`                | YouTube 视频           | `<url>`                |
    | `youtube_comments`              | YouTube 评论           | `<url> [num_comments]` |
    | `reddit_posts`                  | Reddit 帖子            | `<url>`                |
  </Accordion>

  <Accordion title="地图、评论及其他" icon="map-location-dot">
    | 类型                          | 平台              | 参数                   |
    | --------------------------- | --------------- | -------------------- |
    | `google_maps_reviews`       | Google Maps 评论  | `<url> [days_limit]` |
    | `google_play_store`         | Google Play     | `<url>`              |
    | `apple_app_store`           | Apple App Store | `<url>`              |
    | `github_repository_file`    | GitHub 仓库文件     | `<url>`              |
    | `yahoo_finance_business`    | Yahoo Finance   | `<url>`              |
    | `zillow_properties_listing` | Zillow          | `<url>`              |
    | `booking_hotel_listings`    | Booking.com     | `<url>`              |
  </Accordion>
</AccordionGroup>

<Tip>
  随时在终端中运行 `brightdata pipelines list` 查看所有可用类型。
</Tip>

***

## `brightdata scraper`

从终端构建、运行和维护自定义 [Bright Data Scraper Studio](/cn/datasets/scraper-studio/build-with-the-cli) 爬虫。每个爬虫由一个 Collector ID（`c_*` 字符串）标识，该 ID 在多次运行和自我修复之间保持稳定。

### `brightdata scraper create <url> <description>`

使用 Bright Data 的 AI Agent 根据自然语言描述构建爬虫。返回一个 Collector ID。

```bash theme={null}
brightdata scraper create https://news.ycombinator.com \
  "Extract top stories: title, url, points, author, comment count"
```

AI 生成通常耗时 5 到 15 分钟，复杂目标可能长达 25 分钟。

### `brightdata scraper run <collector_id> [url]`

在一个或多个 URL 上运行爬虫并返回数据。CLI 会先尝试实时模式，当某次运行超过实时模式的页面加载上限时，自动回退到批处理模式。

| 标志                    | 说明         |
| --------------------- | ---------- |
| `-o, --output <path>` | 将输出写入文件    |
| `--json`              | 强制 JSON 输出 |
| `--pretty`            | 美化 JSON 输出 |

```bash theme={null}
brightdata scraper run c_mpohus372o5tmid1jk https://news.ycombinator.com --pretty
```

### `brightdata scraper heal <collector_id> <prompt>`

通过 AI 自我修复就地修复现有爬虫。Collector ID 不变。默认情况下，`heal` 会停在批准关口，返回 `status: "awaiting_approval"` 和 `preview_result`。

| 标志                    | 说明                                  |
| --------------------- | ----------------------------------- |
| `--url <url>`         | 编入下一步提示的验证目标。不会发送到 heal 调用          |
| `--auto-approve`      | 在关口自动批准并一路轮询到 `done`                |
| `--timeout <seconds>` | 轮询超时（默认：`600`）                      |
| `--max-retries <n>`   | AI-Flow 并发作业 429 上限时的最大重试次数（默认：`4`） |
| `--no-retry`          | 遇到 429 立即失败，而不等待上限解除                |
| `-o, --output <path>` | 将输出写入文件                             |
| `--json` / `--pretty` | JSON 输出（原始 / 缩进）                    |

```bash theme={null}
brightdata scraper heal c_mpohus372o5tmid1jk \
  "The price field returns null since the redesign. Re-capture price and currency." \
  --url https://example.com/product/1
```

### `brightdata scraper approve <collector_id>`

提交等待批准的修复，或使用 `--reject` 拒绝它。

| 标志                    | 说明              |
| --------------------- | --------------- |
| `--reject`            | 拒绝所提议的修复，而不是批准它 |
| `--url <url>`         | 成功后编入下一步提示的验证目标 |
| `--timeout <seconds>` | 轮询超时（默认：`600`）  |
| `-o, --output <path>` | 将输出写入文件         |
| `--json` / `--pretty` | JSON 输出         |

```bash theme={null}
brightdata scraper approve c_mpohus372o5tmid1jk --url https://example.com/product/1
brightdata scraper approve c_mpohus372o5tmid1jk --reject
```

<Tip>
  自我修复的流程是：运行、检查、`heal`、`approve`、重新运行。完整演练参见 [Scraper Studio CLI 快速开始](/cn/datasets/scraper-studio/build-with-the-cli)。`scraper heal` 和 `scraper approve` 在 CLI v0.3.1 中加入。
</Tip>

***

## `brightdata status <job-id>`

检查异步快照作业的状态（来自 `--async` 抓取或管道收集）。

| 标志                    | 说明             |
| --------------------- | -------------- |
| `--wait`              | 轮询直到作业完成       |
| `--timeout <seconds>` | 轮询超时（默认：`600`） |
| `-o, --output <path>` | 将输出写入文件        |
| `--json` / `--pretty` | JSON 输出        |

```bash theme={null}
brightdata status s_abc123xyz
brightdata status s_abc123xyz --wait --pretty
brightdata status s_abc123xyz --wait --timeout 300
```

***

## `brightdata zones`

列出并检查 Bright Data 代理区域。

```bash theme={null}
brightdata zones                        # List all active zones
brightdata zones info <name>            # Full details for a zone
brightdata zones --json -o zones.json   # Export as JSON
brightdata zones info my_zone --pretty  # Pretty-print zone info
```

***

## `brightdata budget`

查看账户余额和按区域的成本/带宽。只读。

| 子命令           | 说明           |
| ------------- | ------------ |
| *（无）*         | 快速账户余额       |
| `balance`     | 余额 + 待定费用    |
| `zones`       | 所有区域的成本和带宽表  |
| `zone <name>` | 一个区域的详细成本和带宽 |

| 标志                    | 说明                                |
| --------------------- | --------------------------------- |
| `--from <datetime>`   | 日期范围的开始（例如 `2024-01-01T00:00:00`） |
| `--to <datetime>`     | 日期范围的结束                           |
| `--json` / `--pretty` | JSON 输出                           |

```bash theme={null}
brightdata budget
brightdata budget balance
brightdata budget zones
brightdata budget zone my_zone
brightdata budget zones --from 2024-01-01T00:00:00 --to 2024-02-01T00:00:00
```

***

## `brightdata config`

查看和管理 CLI 配置。

| 子命令                 | 说明     |
| ------------------- | ------ |
| *（无）*               | 显示所有配置 |
| `get <key>`         | 获取单个值  |
| `set <key> <value>` | 设置一个值  |

| 配置键                     | 说明                         |
| ----------------------- | -------------------------- |
| `default_zone_unlocker` | `scrape` 和 `search` 的默认区域  |
| `default_zone_serp`     | 仅 `search` 的覆盖区域           |
| `default_format`        | 默认输出格式：`markdown` 或 `json` |
| `api_url`               | 覆盖 API 基础 URL              |

```bash theme={null}
brightdata config
brightdata config set default_zone_unlocker my_zone
brightdata config set default_format json
brightdata config get default_zone_unlocker
```

***

## `brightdata init`

交互式设置向导。引导完成身份验证、区域选择和默认配置。

| 标志                    | 说明          |
| --------------------- | ----------- |
| `--skip-auth`         | 跳过身份验证步骤    |
| `-k, --api-key <key>` | 直接提供 API 密钥 |

```bash theme={null}
brightdata init
```

***

## `brightdata skill`

将 Bright Data AI 代理技能安装到编码代理中（Claude Code、Cursor、Copilot 等）。

| 子命令          | 说明                   |
| ------------ | -------------------- |
| `add`        | 交互式选择器 - 选择技能 + 目标代理 |
| `add <name>` | 直接安装特定技能             |
| `list`       | 列出所有可用技能             |

可用技能：`search`、`scrape`、`data-feeds`、`bright-data-mcp`、`bright-data-best-practices`

```bash theme={null}
brightdata skill add              # Interactive picker
brightdata skill add scrape       # Direct install
brightdata skill list             # See what's available
```
