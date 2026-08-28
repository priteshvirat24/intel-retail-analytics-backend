> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 BitBrowser 中使用 Bright Data

> 使用 Bright Data 和 BitBrowser 简化您的多账号浏览。本指南将指导您如何将 Bright Data 代理集成到 BitBrowser，以确保所有账号的安全、私密和高效浏览。

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

## 什么是 BitBrowser？

BitBrowser 是一个多账号浏览解决方案，旨在安全高效地管理多个在线身份。每个账号都在独立的环境中运行，使您能够操作多个账户，同时降低被检测的风险。集成 Bright Data 代理可增加额外的匿名性，并确保您的工作流保持顺畅连接。

<Tip>
  通过在用户名中使用 `-session` 参数，在整个浏览会话中保持一致的 IP。这一点至关重要，因为 Bright Data 代理默认会在每次请求时更换 IP。 [了解更多](/cn/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

<Warning>
  不支持通过数据中心和 ISP 代理网络连接社交网络，包括：Facebook、TikTok、Instagram、X（Twitter）、LinkedIn、YouTube、Reddit、Pinterest、Snapchat 和 Discord。
</Warning>

## 为什么在 BitBrowser 中使用 Bright Data？

* **增强隐私**：隐藏您的 IP 地址，确保您的在线活动匿名。
* **地理定位浏览**：使用 Bright Data 的国家/地区代理访问特定区域的内容。
* **稳定连接**：确保管理多个账号时的连接稳定性和可靠性。

## 如何在 BitBrowser 中使用 Bright Data

### **步骤 1：下载并安装 BitBrowser**

1. 访问官方 [BitBrowser 网站](https://www.bitbrowser.net/) 并下载适用于您的设备的应用程序。
2. 按照安装指南完成安装，并在安装完成后启动应用程序。
3. 使用您的凭据登录 BitBrowser 账号。

### **步骤 2：进入浏览器账号管理页面**

1. 登录后，您将进入 BitBrowser 的主界面。
2. 在菜单或仪表板中找到 **"浏览器账号"** 选项。

<Frame as="div" style={{width:"50%", height:"auto"}}>
  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/bitbrowser1.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=8fb6d555996ba73da9f2a5af9822ae94" alt="" width="202" height="324" data-path="images/integrations/bitbrowser1.png" />
</Frame>

### **步骤 3：创建新的浏览器账号**

1. 点击 **“+ 添加”** 按钮以创建新的浏览器账号。
2. 在账号设置窗口中，为该账号命名，以便后续识别。

<Frame as="div">
  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/bitbrowser2.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=c7f6dcfce42f7bf63295c99e814291be" alt="" width="1263" height="324" data-path="images/integrations/bitbrowser2.png" />
</Frame>

### **步骤 4：输入 Bright Data 代理信息**

登录您的 Bright Data 账号，并选择您要使用的代理区域。在 **概览** 页面下的 **访问详情** 中，您可以找到所需的代理信息。

1. 在账号配置页面向下滚动至 **"代理"** 部分。

2. 按以下方式输入您的 Bright Data 代理信息：

   * **类型**：根据 Bright Data 代理类型选择协议（`HTTP`、`HTTPS` 或 `SOCKS5`）。
   * **主机**：输入 [`http://brd.superproxy.io/`](http://brd.superproxy.io/) 作为服务器地址。
   * **端口**：44445
   * **用户名**：输入您的 Bright Data 代理用户名。对于特定区域的代理，请调整用户名格式（例如 `your-username-country-US`）。
   * **密码**：输入您的 Bright Data 代理密码。

3. 仔细检查所有输入信息，确保准确无误。

### **步骤 5：测试并保存代理设置**

1. 点击 **"检查代理"** 按钮以验证连接是否成功。
2. 如果测试成功，点击 **"确认"** 以保存账号设置。

### **步骤 6：启动账号并验证设置**

1. 在 **浏览器账号** 仪表板中，找到您刚刚创建的账号并点击 **"打开"**。
2. 浏览器启动后，访问 [httpbin.org/ip](http://httpbin.org/ip) 以确认显示的 IP 是否与您的 Bright Data 代理 IP 匹配。
3. 如果 IP 匹配，说明代理已成功集成，您的账号可以进行安全私密的浏览。

<Frame as="div">
  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/bitbrowser3.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=54d2aeb264ee2ce6730b4a2c868ffd10" alt="" width="1259" height="324" data-path="images/integrations/bitbrowser3.png" />
</Frame>

通过将 **Bright Data** 代理集成到 **BitBrowser**，您可以安全高效地管理多个在线身份。无论是管理社交媒体账号、电商运营还是研究任务，Bright Data 都能确保稳定、私密且具备地理灵活性的浏览体验。在 BitBrowser 上享受流畅的工作流和更高的匿名性吧！
