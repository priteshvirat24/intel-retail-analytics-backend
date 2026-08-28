> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Web Unlocker API 概述

> Bright Data Web Unlocker API（98% 成功率）在一次调用中处理代理轮换、反机器人挑战和 CAPTCHA 破解，返回干净的 HTML 或 JSON。

**Web Unlocker API** 通过一次 API 调用即可解封任何公开网页，成功率高达 98%，并返回干净的 HTML 或 JSON。您只需发送一个包含目标 URL 的请求，Bright Data 便会在其侧处理代理轮换、浏览器指纹、CAPTCHA 破解和重试。您只需为成功的请求付费。

Web Unlocker API 是 Bright Data [Unlocker 采集套件](/cn/scraping-automation/introduction) 的一部分。您无需自行管理代理、请求头、指纹和反机器人逻辑，只需调用一个端点，即可获得已经解封、可直接解析的响应。

```sh Direct API access theme={null}
curl -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{"zone":"YOUR_ZONE_NAME","url":"https://example.com","format":"raw"}' \
  https://api.brightdata.com/request
```

响应内容即为目标页面的原始 HTML 或 JSON。无需任何代理编排、浏览器自动化或自定义重试逻辑。完整的演示以及 Python、Node.js 和 cURL 示例，请参见[发送您的第一个请求](/cn/scraping-automation/web-unlocker/send-your-first-request)。

## Web Unlocker API 是如何工作的？

每个请求在到达目标网站之前，都会在 Bright Data 侧进行优化。一次对 `https://api.brightdata.com/request` 的调用会：

* 为目标网站选择最有效的代理网络
* 设置请求头和指纹，以匹配真实用户的浏览器流量
* 自动破解 CAPTCHA 和反机器人挑战
* 使用其他配置重试失败的尝试，直到请求成功
* 仅对返回成功响应的请求收费

Bright Data 提供两种返回结果相同的访问方式：**直接 API 访问**，即对单个端点发起的 REST 调用（推荐），以及**原生代理访问**，即通过 Bright Data 超级代理路由请求。设置任意一种方式，请参见[发送您的第一个请求](/cn/scraping-automation/web-unlocker/send-your-first-request)。

## 何时应该使用 Web Unlocker API？

当您需要可靠、大规模地访问公开网页数据，又不想自行构建和维护代理与反机器人基础设施时，请使用 Web Unlocker API。它适用于：

* 抓取任何网站，包括具有高级反机器人防护的网站
* 模拟真实用户行为，以访问受保护或有地域限制的内容
* 没有可扩展代理与解封技术栈的工程团队
* 需要高成功率和可预测的按成功付费成本的生产工作负载

<Warning>
  Web Unlocker API 不支持社交网络账号管理这一使用场景。这包括管理 Facebook、TikTok、Instagram、X (Twitter)、LinkedIn、YouTube、Reddit、Pinterest、Snapchat 和 Discord 上的账号。
</Warning>

<Note>
  Web Unlocker API 不适用于基于浏览器的自动化或第三方浏览器工具，例如
  [Adspower](/cn/integrations/adspower)、
  [Puppeteer](/cn/integrations/puppeteer)、
  [Playwright](/cn/integrations/playwright)
  或 [Multilogin (MLA)](/cn/integrations/multilogin)。
  如果您的工作流需要直接与浏览器交互或执行脚本化的用户操作，请改用
  [Browser API](https://www.bright.cn/products/scraping-browser)。
</Note>

## FAQ

### Web Unlocker API 返回什么格式？

默认情况下，Web Unlocker API 返回目标页面的原始 HTML。设置 `"format":"raw"` 可获取未经修改的响应。返回的响应体可直接解析，无需任何后处理。

### 失败的请求需要付费吗？

不需要。在 Web Unlocker API 和 [SERP API](/cn/scraping-automation/serp-api) 上，您只需为成功发送到目标域的请求付费。

### Web Unlocker API 能控制浏览器吗？

不能。Web Unlocker API 通过一次请求返回页面内容。若需要点击、滚动或填写表单等脚本化的浏览器操作，请使用 [Browser API](https://www.bright.cn/products/scraping-browser)。

### Web Unlocker API 适用于搜索引擎吗？

对于 Google、Bing 和其他搜索引擎，请使用 [SERP API](/cn/scraping-automation/serp-api)。它专为搜索结果页面而设计，并返回已解析的结果。

## 相关内容

<CardGroup cols={2}>
  <Card title="发送您的第一个请求" icon="paper-plane" href="/cn/scraping-automation/web-unlocker/send-your-first-request">
    使用 Python、Node.js 或 cURL 发起您的第一个 Web Unlocker API 调用。
  </Card>

  <Card title="快速开始" icon="rocket" href="/cn/scraping-automation/web-unlocker/quickstart">
    创建 Web Unlocker API zone 并获取您的 API key。
  </Card>

  <Card title="配置" icon="sliders" href="/cn/scraping-automation/web-unlocker/configuration">
    调整国家/地区定向、响应格式和请求选项。
  </Card>

  <Card title="最佳实践" icon="list-check" href="/cn/scraping-automation/web-unlocker/bestpractices">
    获得最高的成功率和最低的每请求成本。
  </Card>
</CardGroup>
