> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 macOS 上使用 Bright Data

> 将 Bright Data 代理集成到 macOS 网络设置中，实现安全、私密和灵活的地理位置浏览。本指南将引导您完成整个配置过程，帮助您高效、安全地上网。

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
  在浏览器会话期间保持 IP 地址一致，请在用户名中使用 `-session` 参数。这一点至关重要，因为 Bright Data 代理默认在每次请求时轮换 IP。[了解更多](/cn/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

## 为什么在 macOS 上使用 Bright Data？

将 Bright Data 代理添加到 Mac 的网络设置可以提供以下优势：

* **增强隐私**：隐藏真实 IP，使在线活动更安全。
* **灵活的地理访问**：通过不同地区的 IP 访问特定地区的内容。
* **稳定匿名连接**：降低被检测的风险，并在各种应用程序（不仅限于浏览器）中保持可靠的浏览体验。

## 在 macOS 上设置 Bright Data

<Steps>
  <Step title="前提条件">
    在开始之前，请确保您具备以下条件：

    1. **Bright Data 代理凭据**：
       * 登录 [Bright Data 控制面板](https://www.bright.cn/cp/zones) 获取主机、端口、用户名和密码。
       * 确认您拥有 `HTTP`、`HTTPS` 或 `SOCKS5` 代理。

    2. **运行较新 macOS 版本的 macOS 设备**（以下指南适用于 macOS 10.12 Sierra 及以上版本）。
  </Step>

  <Step title="打开网络偏好设置">
    1. 点击屏幕左上角的 **苹果菜单**。
    2. 选择 **系统设置**（较旧 macOS 版本为 **系统偏好设置**）。

    <Frame as="div" style={{width:"50%", height:"auto"}}>
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/macos1.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=f2c5b563ce602aeb7118d2295c9814cc" alt="" width="252" height="316" data-path="images/integrations/macos1.png" />
    </Frame>

    3. 进入 **网络** 选项，并选择要配置的网络连接（如 **Wi-Fi** 或 **以太网**）。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/macos2.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=e22679f9962e38421ffc7eae16fdb55a" alt="" width="719" height="309" data-path="images/integrations/macos2.png" />
    </Frame>
  </Step>

  <Step title="进入高级设置">
    1. 在网络面板右上角点击 **“详情…”** 按钮。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/macos3.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=059e51de8f14d0141e717158183e5874" alt="" width="490" height="386" data-path="images/integrations/macos3.png" />
    </Frame>

    2. 在新窗口中，选择底部的 **代理** 选项卡。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/macos4.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=c2e52cd0da04e5d8919c094c1d270242" alt="" width="659" height="420" data-path="images/integrations/macos4.png" />
    </Frame>
  </Step>

  <Step title="选择代理类型">
    勾选需要配置的代理协议类型。

    对于 Bright Data 的 `HTTP` 或 `HTTPS` 代理，选择 **Web 代理（HTTP）** 或 **安全 Web 代理（HTTPS）**。对于 `SOCKS` 代理，选择 **SOCKS 代理**。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/macos5.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=7ff0889a67e296175a4f1387d7847c5d" alt="" width="659" height="420" data-path="images/integrations/macos5.png" />
    </Frame>
  </Step>

  <Step title="输入 Bright Data 代理详情">
    * **服务器**：输入 Bright Data 主机地址（例如 `http://brd.superproxy.io/`）。
    * **端口**：输入 [Bright Data 控制面板](https://www.bright.cn/cp/zones) 提供的端口号。
    * **启用身份验证**：勾选 **“代理服务器需要密码”**（或类似选项）以启用凭据字段。
    * **用户名** 和 **密码**：填写您的 Bright Data 代理凭据。如需特定国家的出口节点，请在用户名后添加 `-country-XX`（例如 `your-username-country-US` 以使用美国代理）。
    * 点击 **确定** 以保存设置。
  </Step>

  <Step title="测试代理连接">
    1. 打开 **Safari**、**Chrome** 或其他浏览器。
    2. 访问 [httpbin.org/ip](http://httpbin.org/ip) 以检查您的 IP 地址。
    3. 确认显示的 IP 与 Bright Data 代理的 IP 相匹配。如果匹配，则您的 Mac 现在已通过 Bright Data 代理进行流量路由。
  </Step>
</Steps>

将 **Bright Data** 代理集成到 **macOS** 网络设置后，您可以在所有应用程序中享受更安全、私密和灵活的浏览体验。访问地理限制内容、保护身份并提升连接稳定性——在 Mac 上，Bright Data 让一切变得更加轻松！
