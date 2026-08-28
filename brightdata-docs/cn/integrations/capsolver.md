> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何设置 Bright Data 与 Capsolver

> 将 Bright Data 与 Capsolver 集成，以增强您的 CAPTCHA 解决流程。按照本指南安全配置代理，实现高效且不中断的自动化。

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

## 什么是 Capsolver？

Capsolver 是一款 CAPTCHA 解决服务，旨在自动化绕过 CAPTCHA 挑战的过程。通过集成 Bright Data，您可以安全地解决 CAPTCHA，保持匿名，并轻松访问特定地区的内容。

## 为什么要将 Bright Data 与 Capsolver 结合？

* **匿名性**：在解决 CAPTCHA 任务时保护您的 IP 地址。

* **地理定位**：使用国家/地区特定代理访问本地 CAPTCHA 解决方案。

* **可靠连接**：确保不中断的服务，实现流畅的工作流程。

## 如何将 Bright Data 与 Capsolver 集成

**步骤 1. 登录 Capsolver**

* 访问 [Capsolver 官网](https://www.capsolver.com/)，并登录您的账户。

**步骤 2. 打开代理配置**

1\. 打开 **Capsolver 扩展**，进入 **设置** 页面。

2\. 找到 **代理** 选项，并将其切换为 *开启* 以启用代理设置。

<Frame as="div">
  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/capsolver1.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=317c5dca43c093a2de663051aa21ff06" alt="" width="460" height="643" data-path="images/integrations/capsolver1.png" />
</Frame>

**步骤 3. 添加您的 Bright Data 代理信息**

在代理配置页面，输入您的 Bright Data 账号信息：

* **Host**: [`http://brd.superproxy.io/`](http://brd.superproxy.io/)

* **Port**: 44445

* **用户名**：输入您的 Bright Data 用户名。

* **密码**：输入您的 Bright Data 密码。

<Note>
  若需使用特定国家/地区的代理，请将用户名格式设置为 `your-username-country-XX`（例如 `your-username-country-US`）以选择特定位置。
</Note>

将 Bright Data 与 Capsolver 集成，可实现安全高效的 CAPTCHA 解决流程。无论是批量处理 CAPTCHA，还是应对地理限制任务，Bright Data 都能确保无缝体验。立即完成设置，享受隐私保护和可靠性！
