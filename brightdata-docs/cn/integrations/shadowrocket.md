> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 Shadowrocket 中设置 Bright Data

> 学习如何在 iOS 设备上将 Bright Data 集成到 Shadowrocket，实现安全、无缝的浏览体验。按照此分步指南配置代理，提升您的在线隐私。

<Warning>
  **账户管理不是 Bright Data 平台支持的使用场景**（自 2026 年 4 月 1 日起生效）。这包括在 TikTok、Instagram 等类似平台上进行账户管理。Bright Data 代理不得用于此类用途。详情请参阅[可接受使用政策](https://brightdata.com/acceptable-use-policy)。
</Warning>

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

## 什么是 Shadowrocket?

**Shadowrocket** 是一款功能强大的 iOS 应用程序，用于通过代理路由网络流量。它支持多种代理类型，包括 HTTP、HTTPS 和 SOCKS5，以其灵活性和易用性而闻名，是安全浏览和数据管理的首选应用。

<Tip>
  在整个浏览器会话中保持一致的 IP，请在用户名中使用 `-session` 参数。这一点非常重要，因为 BrightData 代理默认每次请求都会轮换 IP。[了解更多](/cn/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

## 如何将 Bright Data 集成到 Shadowrocket

### 步骤 1：安装 Shadowrocket

1. 打开 iOS 设备上的 **App Store**。
2. 搜索 **Shadowrocket** 并下载应用。
3. 安装应用并在安装完成后打开。

### 步骤 2：添加新的代理配置

1. 打开 **Shadowrocket** 应用。
2. 点击右上角的 **+** 按钮添加新的代理。

### 步骤 3：配置代理设置

1. 在配置窗口中：
   * **Type**：根据您的代理类型选择 HTTP、HTTPS 或 SOCKS5。
   * **Server**：输入 `http://brd.superproxy.io/`。
   * **Port**：使用 [Bright Data 仪表板](https://www.bright.cn/cp/zones/page/plans) 提供的端口号。
   * **Username**：输入您的 Bright Data 用户名。
   * **Password**：输入您的 Bright Data 密码。

2. 点击右上角的 **Done** 或 **Save** 保存配置。

### 步骤 4：测试代理

1. 返回主屏幕。
2. 启用新创建的代理配置旁的开关。
3. 打开浏览器或应用，访问 [httpbin.org/ip](http://httpbin.org/ip) 验证代理是否正常工作。

<Note>
  如果需要特定地区的代理，请将用户名格式化为 `your-username-country-XX`（例如 `your-username-country-US`）以通过该地区的代理连接。
</Note>

### 完成设置！

您的 Shadowrocket 应用现已集成 Bright Data。享受安全、私密、匿名的浏览体验，同时获得灵活的地理定位选项和无缝的性能。
