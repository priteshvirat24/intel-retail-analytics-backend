> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SERP API 配置

> 配置 Bright Data SERP API（支持 31 种语言）：选择 JSON 或原始 HTML 格式，切换同步与异步模式，并通过关键请求参数丰富广告数据。

## 默认响应格式

配置 SERP API 时，您可以在多种默认响应格式之间进行选择：

1. 原始 HTML（Raw HTML）：完全不解析，按原样获取 HTML 响应。
2. 完整 JSON（Full JSON）：我们对 Google SERP HTML 的完整解读，转换为 JSON。
3. 精简 JSON（Light JSON）：完整 JSON 的子集。
4. 解析后的 Bing（Parsed Bing）：我们对 Bing SERP HTML 的完整解读，转换为 JSON。
5. Markdown：我们对 Google 和 Bing SERP HTML 的完整解读，转换为 Markdown `*.md` 文件。
6. 截图（Screenshot）：由浏览器解读的 SERP HTML 页面的图像捕获。

要详细了解响应选项和高级响应格式，请参阅[解析搜索结果](/cn/scraping-automation/serp-api/parsed-json-results/parsing-search-results)。

## 增强型广告（仅限谷歌）

Bright Data 提供了一项特殊设置，可带来更多 Google 广告数据。开启该设置后，API 将返回范围更大、更多样化的搜索结果和广告，模拟没有 cookie 的隐身浏览场景。

默认设置（关闭）会同时抓取自然搜索结果和广告，涵盖广泛的地理范围。

## 如何配置高级设置

### 自定义请求头和 Cookie

Bright Data 允许您发送自定义的请求头和 cookie。一旦您这样做，我们将不会覆盖您的设置，并会将您的请求转发给搜索引擎。

您可以从预先批准的请求头和 cookie 列表中选择，或申请新的并经过审批流程。

选择自定义请求头和 cookie 后，Bright Data 将对**所有**请求计费。使用默认设置且不自定义 cookie 时，Bright Data 仅对成功的请求计费。

### 如何发送异步请求

您可以使用异步模式调用 Bright Data API：请求会立即发送，响应就绪后您将收到通知。响应通常需要几分钟时间返回。

对于非实时应用，我们建议使用异步模式以确保更高的成功率。

提交异步请求时，Bright Data 会在后台无缝处理。您可以轮询响应，或配置 webhook，让我们在请求完成时通知您。这样您就可以在稍后更方便的时间通过指定端点收集响应，从而提高稳定性、灵活性和效率。[了解更多](/cn/scraping-automation/serp-api/asynchronous-requests)

#### Webhook 配置

Webhook 有两个可配置选项：

1. Webhook 地址 URL
2. Webhook 方法（GET/POST）

您应在网络中添加我们的 Webhook 代理来源 IP。

<Tip>
  ### 将我们的 webhook IP 列入白名单

  我们的异步 webhook 交付会从一对稳定的 IP 地址发送通知：

  1. `100.27.150.189`
  2. `18.214.10.85`

  客户可能需要在其一侧将这些 IP 列入白名单。
</Tip>
