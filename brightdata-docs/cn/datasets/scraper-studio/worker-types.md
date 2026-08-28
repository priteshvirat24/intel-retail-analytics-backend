> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Scraper Studio worker 类型

> 在 Bright Data Scraper Studio 中根据目标站点是否需要 UI 交互或纯 HTTP 请求，选择 Browser worker 或 Code worker。

Bright Data Scraper Studio 在两种 worker 类型上运行爬虫：Browser worker（真实的无头浏览器）或 Code worker（原始 HTTP 请求）。请根据目标站点所需的最低交互级别进行选择 — Code worker 更快、更便宜，建议先从它开始，仅在 Code worker 无法获取数据时再切换。

## Browser worker 与 Code worker

|               | Browser worker                | Code worker                              |
| ------------- | ----------------------------- | ---------------------------------------- |
| 执行模型          | 无头浏览器会话                       | 直接发送 HTTP 请求（类似 `curl` 或 `requests.get`） |
| 运行 JavaScript | 是                             | 否                                        |
| 点击、滚动、表单输入    | 是                             | 否                                        |
| 最适合           | 动态页面、SPA、登录流程、无限滚动、GraphQL 捕获 | 静态 HTML、站点地图爬取、公开 JSON API               |
| 速度            | 较慢（浏览器启动、完整页面加载）              | 较快（单次 HTTP 往返）                           |
| 每次页面加载成本      | 较高                            | 较低                                       |

## 应该按爬虫还是按阶段分配 worker？

默认情况下，Bright Data Scraper Studio 爬虫以 Worker per scraper（按爬虫分配 worker）模式运行，所有阶段共用同一种 worker 类型。Worker per stage（按阶段分配 worker）现已向所有用户开放，可为每个阶段单独分配不同的 worker 类型。

### 何时使用 Worker per scraper？

当所有阶段需要相同的 worker 类型时，使用 Worker per scraper：

* **所有阶段都需要 Browser worker。** 例如，阶段 1 浏览需要点击或输入才能触发结果的搜索页，阶段 2 滚动浏览动态产品列表。
* **所有阶段都需要 Code worker。** 例如，阶段 1 获取所有可用 URL，阶段 2 直接通过 HTTP 加载每个产品页。

### 何时使用 Worker per stage？

当不同阶段有不同的交互需求时，使用 Worker per stage：

* **阶段 1 需要 Code worker。** 例如，从分类页获取产品 URL 列表。
* **阶段 2 需要 Browser worker。** 例如，加载通过 JavaScript 在客户端渲染价格和评论的产品页。

为每个阶段分配合适的 worker，可避免在不需要时启动完整的浏览器会话，从而缩短运行时间。

### 如何配置 Worker per stage？

1. 在 Bright Data Scraper Studio IDE 中打开您的爬虫。
2. 在 **Settings**（设置）下拉菜单中，开启 **Worker per stage**。
3. 为每个阶段将 **Worker** 设置为 **Browser worker** 或 **Code worker**。
4. 保存爬虫。

如果您为调用仅限浏览器函数（例如 `wait`、`click`、`scroll_to`）的阶段分配了 Code worker，Bright Data Scraper Studio 会抛出 `Incompatible worker` 错误：

```text theme={null}
Click function is not supported for worker type = Code. To use it you should change the code settings to worker type = Browser.
```

完整的仅限浏览器函数列表，请参见 [哪些函数仅 Browser worker 可用？](/cn/datasets/scraper-studio/worker-types#哪些函数仅-browser-worker-可用)

## 何时使用 Browser worker？

当以下任意一项成立时，使用 Browser worker：

* 目标数据由 JavaScript 在客户端渲染，原始 HTML 响应中不存在
* 需要通过点击、滚动、悬停或输入才能访问或显示数据
* 在内容渲染前需要处理 cookie 横幅或关闭弹窗
* 需要使用 `tag_response`、`tag_script` 或 `capture_graphql` 捕获网络流量
* 需要登录、保持会话或与表单交互

## 何时使用 Code worker？

当以下条件全部满足时，使用 Code worker：

* 完整的目标数据存在于原始 HTML 响应或公开 JSON 端点中
* 无需执行 JavaScript 即可渲染数据
* 无需点击、滚动或输入等交互
* 您正在爬取站点地图、RSS 源或 API 端点

<Tip>
  先从 Code worker 开始。如果原始响应中没有您需要的数据，再切换为 Browser worker。可随时在同一爬虫上更换 worker 类型。
</Tip>

## 哪些函数仅 Browser worker 可用？

依赖实时浏览器会话的 Bright Data Scraper Studio 函数，从 Code worker 中调用时会抛出错误。如果您的爬虫需要以下任何函数，请选择 Browser worker：

| 类别      | 函数                                                                                                                                                      |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 等待 DOM  | `wait`、`wait_any`、`wait_for_text`、`wait_hidden`、`wait_visible`、`wait_network_idle`、`wait_page_idle`                                                     |
| 滚动      | `scroll_to`、`scroll_to_all`、`load_more`                                                                                                                 |
| 流量标记    | `tag_response`、`tag_all_responses`、`tag_script`、`tag_image`、`tag_video`、`tag_screenshot`、`tag_download`、`tag_window_field`、`tag_serp`、`capture_graphql` |
| 键盘与鼠标输入 | `click`、`right_click`、`hover`、`mouse_to`、`press_key`、`type`                                                                                             |
| 浏览器配置   | `browser_size`、`emulate_device`、`freeze_page`、`emulate_geolocation`                                                                                     |
| 反机器人    | `solve_captcha`、`close_popup`                                                                                                                           |

## 常见问题

<AccordionGroup>
  <Accordion title="构建爬虫后还能切换 worker 类型吗？">
    可以。在 Bright Data Scraper Studio IDE 中打开爬虫，在 **Settings**（设置）面板中更改 worker 类型。如果您从 Browser worker 切换到 Code worker，请删除上述所有仅限浏览器的函数调用，否则爬虫在下次运行时会抛出错误。
  </Accordion>

  <Accordion title="Code worker 真的比 Browser worker 更快吗？">
    是的。Code worker 仅发送一次 HTTP 请求，无需浏览器启动也无需页面渲染，因此整次往返耗时仅为 Browser worker 运行的极小一部分。具体加速比取决于目标站点，但 Code worker 任务通常在数秒内完成。
  </Accordion>

  <Accordion title="Browser worker 支持捕获后台 API 调用吗？">
    支持。使用 `tag_response` 或 `tag_all_responses` 捕获页面发起的任意 XHR 或 fetch；使用 `capture_graphql` 捕获并重放 GraphQL 查询。完整参考请参见 [Scraper Studio 函数参考](/cn/datasets/scraper-studio/functions)。
  </Accordion>
</AccordionGroup>

## 相关内容

<CardGroup cols={2}>
  <Card title="Scraper Studio 函数参考" icon="code" href="/cn/datasets/scraper-studio/functions">
    交互命令与解析器命令的完整参考
  </Card>

  <Card title="最佳实践" icon="list-check" href="/cn/datasets/scraper-studio/best-practices">
    构建高效爬虫的推荐模式
  </Card>
</CardGroup>
