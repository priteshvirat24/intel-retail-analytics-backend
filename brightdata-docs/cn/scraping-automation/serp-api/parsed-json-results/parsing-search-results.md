> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 使用 SERP API 获取解析后的 JSON 结果

> 本文将介绍使用 SERP API 进行解析的基础知识，并展示解析后的真实 JSON 数据示例。

## 什么是解析？

[解析](https://www.bright.cn/blog/web-data/what-is-data-parsing) 对于 SERP API 来说，是将原始 HTML 响应转换为 **结构化 JSON** 的过程，JSON 中包含字段和数据值。此高级解析功能专门支持 Google 和 Bing。

启用解析后，来自 SERP HTML 的数据会进一步被结构化为可用的字段和值（例如 `rank`、`link`、`title`、`description`、`rating` 等几十个字段），使你能够监控竞争对手的 SERP 排名、分析关键字趋势，并获取有价值的市场洞察。

## 发送基础解析请求

默认情况下，基础解析请求已在网页访问 SERP API 创建页面中配置。

## 覆盖默认配置

如果需要覆盖默认数据格式，请学习如何使用指定的头参数。

<Tip>
  解析支持 **Google** 和 **Bing** 搜索引擎。
</Tip>

<Info>
  上述请求为 **同步** 请求（实时接收响应）。如果你希望发送 **异步** 解析请求，请参见 [这里](/scraping-automation/serp-api/asynchronous-requests)。
</Info>

***

## 基础请求 - 拆解

|                                                                                                                  |                                  |
| ---------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| `brd.superproxy.io`                                                                                              | 我们的负载均衡器地址，会为你的请求找到最快的超级代理       |
| <Tooltip tip="端口 44445 是推荐使用的代理端口，点击了解更多">[44445](/general/faqs#which-port-shall-i-use-22225-or-33335)</Tooltip> | 超级代理使用的基础设施端口，用于接收你的请求           |
| `-user brd-customer-<customer_id> -zone-<zone_name>`                                                             | 用户名认证。最基本的形式下，定义你的用户名以及你请求将使用的区域 |
| `ZONE_PASSWORD`                                                                                                  | 区域密码。所有区域都使用密码进行认证               |

***
