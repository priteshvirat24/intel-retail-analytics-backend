> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 快速开始

## 我如何获得 Bright Data 的 Fast SERP 访问权限？

Fast SERP 的访问权限仅适用于企业客户：请联系您的客户经理 [sales@brightdata.com](mailto:sales@brightdata.com) 了解您的账户是否符合条件。Fast SERP 在高流量场景中提供最佳结果，低于 50 QPS 的请求批准概率较小。

## Fast SERP 有多快？

Fast SERP 的响应速度至少比我们的常规 SERP 快两倍，P(90) 约为 1 秒。

*P(90) 是第 90 百分位，意味着 90% 的请求。*

## Fast SERP 支持哪些 Google 搜索？

Fast SERP 支持多个 Google 搜索垂直领域。请查看该搜索类型的相关页面。

支持的垂直领域：

1. 网页搜索
2. 新闻
3. 购物
4. 图片
5. 地图

## 支持多少 QPS（每秒查询数）的流量？

Bright Data 可以支持从数百到数千 QPS 的高容量 SERP 流量。

在开始之前，请考虑您的 POC/测试流量和预期的生产流量。这有助于确保您的区域为您的工作负载正确配置。如果您不确定，请从估计开始——您的客户经理可以根据您的使用增长调整您的速率分配。如果您的使用在短时间内波动（如突然或计划的高峰期，或突然或计划的零流量期），请告诉我们，以便我们确保服务水平。

## 我需要在端点控制或限制流量吗？

如果您的系统具有内部速率限制或负载控制机制，请与您的客户经理分享这些详情。这有助于将您区域的容量与您基础设施的行为相协调，并避免不必要的错误。

## 我应该使用本地代理接口还是 REST API？

Fast SERP 最适合与**本地代理接口**配合使用——它比 REST API 稍快一些。如果您的架构需要，可以提供 REST API 接口。

## 我的爬虫将从哪个地理区域运行？

Fast SERP 支持多个部署区域：**美国东部**、**美国西部**、**欧盟**和 **APAC**。提前了解您的爬虫区域有助于优化路由和延迟。如果您的生产流量分布在多个区域，请告知您的客户经理。
