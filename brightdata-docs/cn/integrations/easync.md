> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 Easync 中设置 Bright Data

> 在 Easync 上使用 Bright Data 提高自动化工作流程的效率。按照本指南配置 Bright Data，实现无缝且安全的操作。

<Accordion title="展开以获取您的 Bright Data 代理访问信息">
  ### 您的代理访问信息

  Bright Data 代理按“代理区域”（Proxy zones）进行分组。每个区域包含其对应的代理配置。&#x20;

  要获取代理区域的访问权限：&#x20;

  1. 登录 Bright Data 控制面板
  2. 选择现有代理区域或新建一个代理区域
  3. 点击新的区域名称，并选择 **概览（Overview）** 选项卡
  4. 在概览选项卡中，找到 **访问详情（Access details）**，并单击复制图标将代理访问信息复制到剪贴板&#x20;
  5. 您需要以下信息：代理主机（Proxy Host）、代理端口（Proxy Port）、代理区域用户名（Proxy Zone username）和代理区域密码（Proxy Zone password）
  6. 点击复制图标，将文本复制到剪贴板，并粘贴到您的工具的代理配置中&#x20;

  ### 访问详情示例

  <img src="https://mintcdn.com/brightdata/w0SvUEkwL-1dGVtS/snippets/accessdetails.png?fit=max&auto=format&n=w0SvUEkwL-1dGVtS&q=85&s=a3d4e920631ae105cb2f388c63bc5b5d" alt="" width="597" height="508" data-path="snippets/accessdetails.png" />

  ### 住宅代理访问

  要使用 Bright Data 的 **住宅代理（Residential Proxies）**，您必须是经过 KYC 验证的企业账户。请与 Bright Data 合规团队完成 KYC 验证；不存在自动或无需 KYC 的访问方式。尚未完成 KYC 时，请使用 ISP 或数据中心代理。[了解更多...](/proxy-networks/residential/network-access)

  ### 目标是搜索引擎？

  如果您的目标是 Google、Bing 或 Yandex 等搜索引擎，则需要使用专门的搜索引擎结果页（**SERP**）代理 API。请使用 Bright Data SERP API 来访问搜索引擎。\
  [点击此处了解 Bright Data SERP 代理 API。](/scraping-automation/serp-api/introduction)

  ### 避免工具中的 `PROXY ERROR`

  一些工具会使用搜索引擎作为代理测试目标：如果您的代理测试失败，这可能就是原因。请确保您的测试目标域名不是搜索引擎（此设置在工具配置中，而非 Bright Data 代理的控制范围内）。
</Accordion>

## 什么是 Easync？

**Easync** 是一款专为电商业务设计的自动化工具。它可以帮助用户优化订单履行、库存更新和跨平台价格追踪。通过集成 **Bright Data**，您可以增强 Easync 的功能，保持匿名访问、获取特定地区的数据，并降低 IP 封禁风险。

## 如何将 Bright Data 集成到 Easync

### **步骤 1. 登录 Easync**

要在 Easync 中启用 Bright Data，首先需要在您的操作系统上进行相应配置。请根据您的操作系统选择以下指南：

* [如何在 Windows 上设置 Bright Data](/cn/integrations/windows)
* [如何在 macOS 上设置 Bright Data](/cn/integrations/macos)

完成后，您的系统将准备好通过 Bright Data 进行流量路由。

### **步骤 2. 打开代理配置**

1\. 访问 [Easync 官网](https://easync.io/) 并登录您的账户。\
2\. Easync 会自动检测并使用您在操作系统上配置的代理设置。\
3\. 通过在 Easync 中执行简单操作来测试集成，例如：

* 获取产品详情
* 进行测试订单

这可以确保您的任务通过 Bright Data 安全路由。

### **步骤 3. 验证并监控设置**

1\. 打开浏览器或使用 [httpbin.org/ip](http://httpbin.org/ip) 服务，验证您的代理 IP 是否处于活动状态。\
2\. 在 Easync 中监控性能，确保代理在任务运行时正常工作。

通过在 Easync 集成 Bright Data，您可以自信地自动化任务，确保安全高效的操作。无论是处理订单还是分析数据，您的连接都将受到保护，并针对性能进行优化。
