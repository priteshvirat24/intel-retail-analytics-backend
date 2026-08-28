> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何设置 Bright Data 与 ChangeDetection

> 使用 ChangeDetection 和 Bright Data 安全、匿名地监控网站。通过集成 Bright Data，您可以跟踪网站更新，同时确保您的活动保持私密且不可检测。

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

## 什么是 ChangeDetection？

**ChangeDetection** 是一款强大的网站更新监测工具，允许您跟踪内容变化、接收通知，并实时分析更新情况。无论是监控竞争对手、价格变动，还是产品可用性，ChangeDetection 都能确保您时刻掌握最新信息。通过集成 **Bright Data**，您可以增强隐私保护，绕过访问限制，并高效管理多个监测任务。

<Tip>
  在浏览会话期间保持一致的 IP，请在用户名中使用 `-session` 参数。这一点非常重要，因为 Bright Data 代理默认会在每个请求后轮换 IP。[了解更多](/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

### 如何将 Bright Data 与 ChangeDetection 集成

**步骤 1. 安装并启动 ChangeDetection**

1\. 访问 [ChangeDetection 官网](https://changedetection.io/)，下载适用于您的操作系统的应用程序。

2\. 安装 ChangeDetection 并启动应用程序。

3\. 登录您的账户，进入仪表板。

**步骤 2. 配置代理设置**

1\. 在 ChangeDetection 仪表板中，打开 **设置** 菜单。

2\. 进入 **网络设置** 或 **代理设置** 部分。

**步骤 3. 输入您的 Bright Data 代理信息**

1. 在代理配置字段中输入您的 Bright Data 代理信息：

   * **协议**：根据您的代理类型选择 HTTP、HTTPS 或 SOCKS5。

   * **主机**：输入 [`http://brd.superproxy.io/`](http://brd.superproxy.io/)

   * **端口**：使用您的 [Bright Data 控制面板](https://www.bright.cn/cp/zones) 提供的端口号。

   * **用户名**：输入您的 Bright Data 用户名。

   * **密码**：输入您的 Bright Data 密码。

<Note>
  **如果需要地理定位代理，请在用户名中包含国家代码（例如 `your-username-country-US` 代表美国代理）。**
</Note>

**步骤 4. 验证代理连接**

1. 测试代理连接以确保其正常工作：

   * 在相同的设置菜单中，查找 **测试代理** 或 **验证代理** 按钮。

   * 运行测试，确认代理配置是否正确。

2. 保存设置以应用代理配置。

**步骤 5. 使用 Bright Data 监控网站**

1. 返回 ChangeDetection 仪表板，开始添加要监控的网站。

2. 根据需求配置个性化任务，并确保它们使用代理设置以提高隐私性和效率。

通过在 **ChangeDetection** 中集成 **Bright Data**，您可以安全监控网站、绕过地理访问限制，并轻松管理多个监测任务。立即设置，享受无缝追踪和隐私保护的优势！
