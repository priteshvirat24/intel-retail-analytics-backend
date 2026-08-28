> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 SwitchyOmega 中设置 Bright Data

> 轻松管理您的代理！学习如何将 Bright Data 集成到 SwitchyOmega 浏览器扩展中，以增强隐私、简化账户管理，并优化网页抓取工作流。

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

## 什么是 SwitchyOmega?

**SwitchyOmega** 是适用于 Chrome 和 Firefox 的浏览器扩展，旨在让代理管理变得简单高效。它支持 HTTP、HTTPS、SOCKS4 和 SOCKS5，允许您创建自定义规则，轻松切换代理，并增强您的在线活动。无论是绕过地理限制、管理多个账户，还是保护隐私，SwitchyOmega 都是灵活代理配置的必备工具。

<Tip>
  在整个浏览器会话中保持一致的 IP，请在用户名中使用 `-session` 参数。这一点非常重要，因为 BrightData 代理默认每次请求都会轮换 IP。[了解更多](/cn/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

## 如何在 SwitchyOmega 中设置 Bright Data

### 步骤 1：安装 SwitchyOmega

1. 访问适用于您的浏览器的扩展页面：
   * [Chrome 扩展](https://chrome.google.com/webstore/detail/proxy-switchyomega/padekgcemlokbadohgkifijomclgjgif?hl=en)
   * [Firefox 插件](https://addons.mozilla.org/en-US/firefox/addon/switchyomega)

2. 将 SwitchyOmega 添加到浏览器。安装完成后，工具栏中将显示 SwitchyOmega 图标。

### 步骤 2：创建新的代理配置文件

1. 点击浏览器工具栏的 **SwitchyOmega 图标** 并选择 **Options** 打开设置页面。

<Frame as="div">
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/switchyomega1.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=f1a3e55c0fc6cfbe7c43bbc65898a79c" alt="" width="184" height="225" data-path="images/integrations/switchyomega1.png" />
</Frame>

2. 在设置页面，点击 **New Profile**。

<Frame as="div">
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/switchyomega2.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=075fc3cad4bcb69a554dbb8b7cb81f92" alt="" width="285" height="155" data-path="images/integrations/switchyomega2.png" />
</Frame>

3. 为配置文件提供一个描述性名称（例如 “Bright Data Proxy”），选择 **Proxy Profile**，然后点击 **Create** 保存。

<Frame as="div" style={{width:"70%", height:"auto"}}>
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/switchyomega3.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=79d21cc4be4f5096b737154cbabc862c" alt="" width="592" height="610" data-path="images/integrations/switchyomega3.png" />
</Frame>

### 步骤 3：配置 Bright Data 代理详情

1. 在配置文件中输入以下 Bright Data 代理信息：

   * **Protocol**：根据代理类型选择 HTTP、HTTPS 或 SOCKS5。
   * **Server**：输入 `http://brd.superproxy.io/`。
   * **Port**：输入 [Bright Data 仪表板](https://www.bright.cn/cp/zones/page/plans) 提供的端口号。

2. 点击 **Lock** 图标添加认证信息：

   * **Username**：您的 Bright Data 用户名
   * **Password**：您的 Bright Data 密码

3. 点击 **Save Changes** 保存代理配置。

<Frame as="div">
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/switchyomega4.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=054caff2869a5f5d387dd9624c183733" alt="" width="291" height="228" data-path="images/integrations/switchyomega4.png" />
</Frame>

<Note>
  如果需要特定国家的代理，请在用户名后添加国家代码，例如 `your-username-country-US`。
</Note>

### 步骤 4：应用并激活代理

1. 点击 **Apply Changes** 完成设置。

<Frame as="div">
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/switchyomega5.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=8c364de19bb44c9b3559e4ca62e96b12" alt="" width="317" height="128" data-path="images/integrations/switchyomega5.png" />
</Frame>

2. 要启用代理，从浏览器工具栏的 SwitchyOmega 下拉菜单中选择已配置的配置文件。

<Frame as="div">
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/switchyomega6.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=b178ba252ae15c28311068cde6b33260" alt="" width="181" height="252" data-path="images/integrations/switchyomega6.png" />
</Frame>

现在，您的 Bright Data 代理已与 SwitchyOmega 完全集成。无论是管理多个账户、安全浏览，还是高效抓取数据，这个设置都能为您提供灵活且可控的代理体验。
