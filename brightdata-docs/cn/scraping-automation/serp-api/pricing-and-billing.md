> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SERP 定价与计费

> 仅为成功请求付费。了解 Bright Data SERP API 的计费方式、包含内容以及异步计费机制。

Bright Data SERP API 使用 **每 1,000 个成功请求** 的计费模式。失败或出错的请求不计费。解析和解锁功能已包含，无需支付带宽费用。

> * 计费单位：每成功请求（每 1,000 次）
> * 包含解析/解锁（无需带宽费用）
> * 异步模式：发起请求计费；收集/检索免费

[Bright Data SERP API 价格层级及批量折扣](https://www.bright.cn/pricing/serp?utm_source=docs\&utm_medium=pricing-billing\&utm_campaign=serp_pricing)

## 按成功请求付费

在 Bright Data 中，**仅对成功响应计费**。

* 计费单位：每 1,000 个成功请求
* 包含内容：解析（JSON/Markdown/HTML）、代理管理、解锁/CAPTCHA 处理
* 无带宽费用

<Note>如果请求在后台重试，不会额外收费，仅对最终成功的响应计费。</Note>

***

## 异步计费

长时间运行任务或大批量请求可使用异步模式。

* **计费**：首次发起“发送请求”调用
* **不计费**：后续“收集/检索”调用

参见：[异步请求](/cn/scraping-automation/serp-api/asynchronous-requests)

***

## 单位价格包含内容

* 结构化输出：**JSON**、**Markdown** 或 **原始 HTML**
* 代理管理与 **解锁**（包括 CAPTCHA 处理）
* 自动重试及最佳 header/设备逻辑
* 城市/邮编地理定位；**桌面和移动**用户代理

***

## 常见问题

**重试或异步“收集”会计费吗？**\
重试包含在内。在异步模式下，“收集/检索” **不计费**——仅“发送请求”计费。

**解析是否包含在内？**\
是的——**JSON/Markdown/HTML** 均包含在单位价格内。

**会收取带宽费用吗？**\
不会，计费仅按成功请求计算。

***

## 相关链接

* [SERP 定价](https://www.bright.cn/pricing/serp?utm_source=docs\&utm_medium=pricing-billing\&utm_campaign=serp_pricing)
* [SERP API 介绍](/cn/scraping-automation/serp-api/introduction)
* [异步请求](/cn/scraping-automation/serp-api/asynchronous-requests)
* [解析的 JSON 结果](/cn/scraping-automation/serp-api/parsed-json-results/parsing-search-results)
