> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 Chrome 中配置代理设置

> 使用 Chrome 代理优化您的浏览体验！代理可以保护您的隐私、访问受限网站，并管理多个账户。在本指南中，我们将引导您完成设置，帮助您充分利用 Chrome 代理。

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

<Warning>
  **账户管理不是 Bright Data 平台支持的使用场景**（自 2026 年 4 月 1 日起生效）。这包括在 TikTok、Instagram 等类似平台上进行账户管理。Bright Data 代理不得用于此类用途。详情请参阅[可接受使用政策](https://brightdata.com/acceptable-use-policy)。
</Warning>

<Tip>
  在浏览会话期间保持一致的 IP，请在用户名中使用 `-session` 参数。这一点非常重要，因为 Bright Data 代理默认会在每个请求后轮换 IP。[了解更多](/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

## 在 Chrome 中更改代理设置

准备好在 Chrome 中使用代理了吗？只需按照以下步骤操作，轻松完成设置：

### 步骤 1. **访问 Chrome 设置**

打开 Chrome，点击右上角的 **三点菜单**，然后从下拉菜单中选择 **设置**。

<Frame as="div">
  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/chrome1.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=8b62de64984b10e89b0a8121e96680f7" alt="" width="336" height="801" data-path="images/integrations/chrome1.png" />
</Frame>

### 步骤 2. **打开系统代理设置**

进入 **系统** 部分，选择 **打开您的计算机代理设置** 以继续。

<Frame as="div">
  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/chrome2.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=29c5e9546eb415ae598db95b80a759f8" alt="" width="1276" height="724" data-path="images/integrations/chrome2.png" />
</Frame>

### 步骤 3. **在您的操作系统中配置代理**

由于 Chrome 使用操作系统的代理设置，您将被重定向到系统的代理配置界面。请根据您的操作系统进行相应设置：

* **在 Windows 上**：启用“使用代理服务器”，然后输入您在 [Bright Data 控制面板](https://www.bright.cn/cp/zones) 中获取的代理地址和端口。
* **在 macOS 上**：选择适当的协议（如 HTTP 或 SOCKS5），然后输入代理地址、端口和凭据。操作简单快捷！

设置完成！现在，您的 Chrome 浏览器已成功配置 **Bright Data** 代理。无论是管理账户、全球购物，还是匿名浏览，您都可以享受安全流畅的体验。
