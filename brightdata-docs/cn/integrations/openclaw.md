> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何将 Bright Data 与 OpenClaw 集成

> 为您的 OpenClaw AI 代理赋予实时网络搜索、机器人绕过抓取、浏览器自动化和 50+ 结构化数据工具，由 Bright Data 提供支持。

<Warning>
  **账户管理不是 Bright Data 平台支持的使用场景**（自 2026 年 4 月 1 日起生效）。这包括在 TikTok、Instagram 等类似平台上进行账户管理。Bright Data 代理不得用于此类用途。详情请参阅[可接受使用政策](https://brightdata.com/acceptable-use-policy)。
</Warning>

<Card title="正在构建 AI 初创公司？" cta="了解更多" href="https://brightdata.com/ai/ai-startups-program" icon="rocket-launch" iconType="duotone" arrow="true">
  您可能符合我们的初创计划资格。获得本文所介绍基础设施的全额资助访问权限（最高价值 \$20,000）。
</Card>

[OpenClaw](https://openclaw.ai/) 是一个自托管的 AI 助手网关，可将 WhatsApp、Telegram、Discord 和 iMessage 等消息应用连接到 AI 编码代理。它具有插件系统，可让您使用新工具和功能扩展代理。

**Bright Data 的 OpenClaw 插件**将 Bright Data 网络数据基础设施的全部功能直接带入您的 OpenClaw 代理中。安装一次，您的代理即可获得：

* **实时网络搜索**通过 Google、Bing 和 Yandex 进行地理定位
* **机器人绕过抓取**通过 Web Unlocker，它自动处理验证码、JS 渲染和速率限制
* **完整的浏览器自动化**通过实际的 Chromium 实例，由 Bright Data 的住宅代理网络路由
* **50+ 结构化数据工具**用于 Amazon、LinkedIn、Instagram、TikTok、YouTube、Reddit 等

<Note>
  该插件注册了 **66 个工��**，分为五个类别：搜索、抓取、批量操作、浏览器自动化和结构化网络数据。
</Note>

## 入门步骤

<Steps>
  <Step title="前置条件">
    * [OpenClaw](https://openclaw.ai/) 已安装并运行
    * 具有 API 密钥的 [Bright Data 账户](https://brightdata.com)
    * Node.js 22+（由 OpenClaw 管理）
  </Step>

  <Step title="获取您的 Bright Data API 密钥">
    * 登录您的 [Bright Data 仪表板](https://www.bright.cn/cp)。
    * 转到 [账户设置](https://www.bright.cn/cp/setting/users)。
    * 如果尚未生成，请[生成 API 密钥](/api-reference/authentication#how-do-i-authenticate-with-api-key%3F)。
  </Step>

  <Step title="安装 Bright Data 插件">
    使用 OpenClaw CLI 安装插件：

    ```bash theme={null}
    openclaw plugins install @brightdata/brightdata-plugin
    ```

    验证安装：

    ```bash theme={null}
    openclaw plugins inspect brightdata
    ```

    您应该看到插件 ID `brightdata` 以及所有已注册的工具。
  </Step>

  <Step title="配置您的 API 密钥">
    选择以下方法之一来提供您的 Bright Data API 密钥：

    <Tabs>
      <Tab title="环境变量（推荐用于本地开发）">
        ```bash theme={null}
        export BRIGHTDATA_API_TOKEN=your_token_here
        ```
      </Tab>

      <Tab title="OpenClaw 配置（推荐用于持久设置）">
        ```bash theme={null}
        openclaw config set plugins.entries.brightdata.config.webSearch.apiKey your_token_here
        ```
      </Tab>
    </Tabs>

    <Tip>
      该插件在首次使用时自动创建两个代理区域：`mcp_unlocker`（Web Unlocker）和 `mcp_browser`（Browser API）。无需手动设置区域。
    </Tip>

    要使用现有的区域，请改为执行以下操作：

    ```bash theme={null}
    export BRIGHTDATA_UNLOCKER_ZONE=my_existing_zone
    export BRIGHTDATA_BROWSER_ZONE=my_existing_browser_zone
    ```
  </Step>

  <Step title="启用插件">
    启用插件并重启网关：

    ```bash theme={null}
    openclaw plugins enable brightdata
    openclaw gateway restart
    ```

    <Note>
      如果插件工具未向您的代理公开，您可能需要显式允许插件工具：

      ```bash theme={null}
      openclaw config set tools.alsoAllow '["group:plugins"]'
      ```
    </Note>
  </Step>

  <Step title="开始使用工具">
    您的 OpenClaw 代理现在可以访问所有 66 个 Bright Data 工具。尝试这些示例提示：

    ```text 搜索网络 theme={null}
    使用 brightdata_search 工具搜索"最新 AI 新闻"并返回前 5 个结果。
    ```

    ```text 抓取网页 theme={null}
    在 https://example.com 上使用 brightdata_scrape 工具，并用 3 个要点总结页面。
    ```

    ```text 自动化浏览器 theme={null}
    使用 brightdata_browser_navigate 打开 https://example.com，然后使用 brightdata_browser_get_text 返回可见的页面文本。
    ```

    ```text 获取结构化数据 theme={null}
    使用 brightdata_amazon_product 获取 https://www.amazon.com/dp/B0D2Q9397Y 的详细信息
    ```
  </Step>
</Steps>

## 可用工具

### 搜索

| 工具                        | 描述                                          |
| ------------------------- | ------------------------------------------- |
| `brightdata_search`       | 使用地理定位搜索 Google、Bing 或 Yandex。返回支持分页的结构化结果。 |
| `brightdata_search_batch` | 并行运行最多 5 个搜索查询。部分失败会内联返回。                   |

**`brightdata_search` 的参数：**

| 参数             | 类型                                   | 描述                          |
| -------------- | ------------------------------------ | --------------------------- |
| `query`        | `string`                             | **必需。** 搜索查询                |
| `engine`       | `"google"` \| `"bing"` \| `"yandex"` | 搜索引擎（默认：`google`）           |
| `count`        | `number`                             | 要返回的结果数，1-10                |
| `cursor`       | `string`                             | 下一页的分页游标                    |
| `geo_location` | `string`                             | 2 字母 ISO 国家代码（例如 `us`、`de`） |

### 抓取

| 工具                        | 描述                                                  |
| ------------------------- | --------------------------------------------------- |
| `brightdata_scrape`       | 通过 Web Unlocker 获取任何页面。适用于受机器人保护的站点、JS 渲染页面和地理限制内容。 |
| `brightdata_scrape_batch` | 使用相同的提取选项并行抓取最多 5 个 URL。                            |

**`brightdata_scrape` 的参数：**

| 参数            | 类型                                   | 描述                          |
| ------------- | ------------------------------------ | --------------------------- |
| `url`         | `string`                             | **必需。** 要抓取的 HTTP/HTTPS URL |
| `extractMode` | `"markdown"` \| `"text"` \| `"html"` | 输出格式（默认：`markdown`）         |
| `maxChars`    | `number`                             | 要返回的最大字符数（最小：100）           |

### 浏览器自动化

完整的 Chromium 浏览器控制，通过 Bright Data 的住宅代理网络路由。会话在 10 分钟后空闲超时。

| 工具                                    | 描述                        |
| ------------------------------------- | ------------------------- |
| `brightdata_browser_navigate`         | 使用可选的国家路由导航到 URL          |
| `brightdata_browser_snapshot`         | 捕获具有交互元素引用的 ARIA 快照       |
| `brightdata_browser_click`            | 通过快照引用点击元素                |
| `brightdata_browser_type`             | 通过引用在字段中输入（可选择按 Enter 提交） |
| `brightdata_browser_fill_form`        | 在单个操作中填充多个表单字段            |
| `brightdata_browser_screenshot`       | 拍摄视口或整页截图                 |
| `brightdata_browser_get_html`         | 获取当前页面 HTML               |
| `brightdata_browser_get_text`         | 获取当前页面文本内容                |
| `brightdata_browser_scroll`           | 滚动到页面底部                   |
| `brightdata_browser_scroll_to`        | 滚动到由引用指定的特定元素             |
| `brightdata_browser_wait_for`         | ���待元素变为可见                |
| `brightdata_browser_network_requests` | 列出页面加载以来的网络请求             |
| `brightdata_browser_go_back`          | 后退导航                      |
| `brightdata_browser_go_forward`       | 前进导航                      |

### 结构化网络数据（50+ 平台）

每个工具接受 `url` 或 `keyword` 并返回干净的、类型化的 JSON。无需抓取或解析。

<AccordionGroup>
  <Accordion title="电子商务（10 个工具）">
    | 工具                                  | 数据         |
    | ----------------------------------- | ---------- |
    | `brightdata_amazon_product`         | 产品详情、定价、规格 |
    | `brightdata_amazon_product_reviews` | 客户评论和评分    |
    | `brightdata_amazon_product_search`  | 搜索结果与排名    |
    | `brightdata_walmart_product`        | 产品详情和可用性   |
    | `brightdata_walmart_seller`         | 卖家资料和指标    |
    | `brightdata_ebay_product`           | 列表详情和竞价    |
    | `brightdata_homedepot_products`     | 产品目录和定价    |
    | `brightdata_zara_products`          | 时尚目录数据     |
    | `brightdata_etsy_products`          | 手工制作和古董列表  |
    | `brightdata_bestbuy_products`       | 电子产品目录和优惠  |
  </Accordion>

  <Accordion title="专业网络（7 个工具）">
    | 工具                                    | 数据         |
    | ------------------------------------- | ---------- |
    | `brightdata_linkedin_person_profile`  | 完整的个人资料    |
    | `brightdata_linkedin_company_profile` | 公司概览和统计    |
    | `brightdata_linkedin_job_listings`    | 具有详情的空缺职位  |
    | `brightdata_linkedin_posts`           | 帖子内容和参与度   |
    | `brightdata_linkedin_people_search`   | 人物搜索结果     |
    | `brightdata_crunchbase_company`       | 融资、投资者、创始人 |
    | `brightdata_zoominfo_company_profile` | 公司情报数据     |
  </Accordion>

  <Accordion title="社交媒体（17 个工具）">
    **Instagram**

    | 工具                              | 数据       |
    | ------------------------------- | -------- |
    | `brightdata_instagram_profiles` | 资料统计和简介  |
    | `brightdata_instagram_posts`    | 帖子内容和参与度 |
    | `brightdata_instagram_reels`    | 卷轴元数据和浏览 |
    | `brightdata_instagram_comments` | 评论线程     |

    **Facebook**

    | 工具                                         | 数据      |
    | ------------------------------------------ | ------- |
    | `brightdata_facebook_posts`                | 帖子内容和反应 |
    | `brightdata_facebook_marketplace_listings` | 市场列表    |
    | `brightdata_facebook_company_reviews`      | 页面评论和评分 |
    | `brightdata_facebook_events`               | 活动详情和参与 |

    **TikTok**

    | 工具                           | 数据            |
    | ---------------------------- | ------------- |
    | `brightdata_tiktok_profiles` | 创作者资料和统计      |
    | `brightdata_tiktok_posts`    | 视频内容和指标       |
    | `brightdata_tiktok_shop`     | TikTok 商城产品数据 |
    | `brightdata_tiktok_comments` | 评论线程          |

    **X（Twitter）**

    | 工具                           | 数据      |
    | ---------------------------- | ------- |
    | `brightdata_x_posts`         | 帖子内容和指标 |
    | `brightdata_x_profile_posts` | 资料帖子历史  |

    **YouTube 和 Reddit**

    | 工具                            | 数据      |
    | ----------------------------- | ------- |
    | `brightdata_youtube_profiles` | 频道统计和信息 |
    | `brightdata_youtube_videos`   | 视频详情和指标 |
    | `brightdata_youtube_comments` | 评论线程    |
    | `brightdata_reddit_posts`     | 帖子内容和得分 |
  </Accordion>

  <Accordion title="地图、购物和应用（4 个工具）">
    | 工具                               | 数据      |
    | -------------------------------- | ------- |
    | `brightdata_google_maps_reviews` | 地点评论和评分 |
    | `brightdata_google_shopping`     | 购物结果和价格 |
    | `brightdata_google_play_store`   | 应用详情和评论 |
    | `brightdata_apple_app_store`     | 应用详情和评论 |
  </Accordion>

  <Accordion title="金融、新闻和代码（3 个工具）">
    | 工具                                  | 数据      |
    | ----------------------------------- | ------- |
    | `brightdata_yahoo_finance_business` | 公司财务和新闻 |
    | `brightdata_github_repository_file` | 仓库文件内容  |
  </Accordion>

  <Accordion title="房地产和旅游（2 个工具）">
    | 工具                                     | 数据      |
    | -------------------------------------- | ------- |
    | `brightdata_zillow_properties_listing` | 房产清单和估计 |
    | `brightdata_booking_hotel_listings`    | 酒店列表和定价 |
  </Accordion>

  <Accordion title="AI 见解（3 个工具）">
    | 工具                                  | 数据            |
    | ----------------------------------- | ------------- |
    | `brightdata_chatgpt_ai_insights`    | ChatGPT 响应    |
    | `brightdata_grok_ai_insights`       | Grok 响应       |
    | `brightdata_perplexity_ai_insights` | Perplexity 响应 |
  </Accordion>
</AccordionGroup>

## 网络搜索提供商集成

该插件也注册为 OpenClaw **网络搜索提供商**。要将 Bright Data 设置为您的默认搜索提供商：

```bash theme={null}
openclaw config set tools.web.search.provider brightdata
```

设置后，您的代理执行的任何通用网络搜索都将通过 Bright Data 的搜索基础设施路由。

## 配置参考

所有设置都可以通过环境变量或 OpenClaw 配置提供。环境变量优先。

| 设置          | 环境变量                       | OpenClaw 配置路径                                                       | 默认值                          |
| ----------- | -------------------------- | ------------------------------------------------------------------- | ---------------------------- |
| API 密钥      | `BRIGHTDATA_API_TOKEN`     | `plugins.entries.brightdata.config.webSearch.apiKey`                | **必需**                       |
| 基础 URL      | `BRIGHTDATA_BASE_URL`      | `plugins.entries.brightdata.config.webSearch.baseUrl`               | `https://api.brightdata.com` |
| Unlocker 区域 | `BRIGHTDATA_UNLOCKER_ZONE` | `plugins.entries.brightdata.config.webSearch.unlockerZone`          | `mcp_unlocker`               |
| 浏览器区域       | `BRIGHTDATA_BROWSER_ZONE`  | `plugins.entries.brightdata.config.webSearch.browserZone`           | `mcp_browser`                |
| 请求超时        | -                          | `plugins.entries.brightdata.config.webSearch.timeoutSeconds`        | `30s` 搜索 / `60s` 抓取          |
| 轮询超时        | -                          | `plugins.entries.brightdata.config.webSearch.pollingTimeoutSeconds` | `600s`                       |

## 插件管理

```bash theme={null}
# 验证安装和加载的工具
openclaw plugins inspect brightdata

# 更新到最新版本
openclaw plugins update brightdata

# 临时禁用
openclaw plugins disable brightdata

# 重新启用
openclaw plugins enable brightdata

# 卸载
openclaw plugins uninstall brightdata
```

## 故障排除

**安装后找不到插件**

* 运行 `openclaw plugins list` 以验证插件已安装。
* 使用 `openclaw plugins inspect brightdata` 检查插件 ID 是否为 `brightdata`。
* 运行 `openclaw plugins doctor` 获取诊断信息。

**工具未注册**

* 确保插件已启用：`openclaw plugins enable brightdata`。
* 重启网关：`openclaw gateway restart`。

**身份验证错误**

* 验证您的 API 密钥是否通过环境变量或配置正确设置。
* 检查密钥是否未在您的 [Bright Data 仪表板](https://www.bright.cn/cp/setting/users) 中过期。

**区域创建失败**

* 该插件在首次使用时��动创建 `mcp_unlocker` 和 `mcp_browser` 区域。
* 如果自动创建失败，请在 Bright Data 仪表板中手动创建区域，并通过环境变量设置它们。

## 其他资源

* [OpenClaw 文档](https://docs.openclaw.ai)
* [OpenClaw 插件 CLI 参考](https://openclawlab.com/en/docs/cli/plugins/)
* [Bright Data API 文档](/)
* [GitHub 上的插件源代码](https://github.com/brightdata/openclaw-plugin)
