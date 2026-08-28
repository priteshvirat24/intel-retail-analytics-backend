> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何将 Bright Data 与 GenLogin 结合使用

> 使用 Bright Data 和 GenLogin 安全管理多个浏览器配置文件。本指南将引导您完成集成 Bright Data 以实现匿名和高效浏览的步骤。

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

## 什么是 GenLogin？

<Tip>
  在浏览器会话期间保持一致的 IP 地址，请在用户名中使用 `-session` 参数。这一点至关重要，因为 Bright Data 代理默认会在每次请求时更换 IP。[了解更多](/cn/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

**GenLogin** 是一款专为需要管理多个账户或项目的专业用户设计的高级浏览器配置管理工具。它可以创建隔离的浏览器环境，确保每个配置文件独立运行并保持安全。通过集成 **Bright Data**，您可以增强 GenLogin 的功能，实现可靠的匿名代理连接。

## 如何将 Bright Data 与 GenLogin 结合使用

<Steps>
  <Step title="下载并打开 GenLogin">
    1. 访问 [GenLogin 官网](https://genlogin.com/)，下载适用于您的操作系统的应用程序。
    2. 按照屏幕提示安装 GenLogin 并启动应用程序。
    3. 登录您的 GenLogin 账户。如果没有账户，请免费注册。
  </Step>

  <Step title="创建或编辑浏览器配置文件">
    1. 在 GenLogin 仪表板中，点击 **创建配置文件** 以创建新配置文件，或选择一个已有配置文件进行编辑。
    2. 在配置文件设置中，在 **名称** 字段中为您的配置文件输入一个独特且易于识别的名称。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/genlogin1.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=245fc0ebe89bd6afa5beb7e73c5d98d7" alt="" width="1319" height="285" data-path="images/integrations/genlogin1.png" />
    </Frame>
  </Step>

  <Step title="配置代理设置">
    1. 在配置文件设置中，滚动到 **网络** 部分。

    2. 选择 **自定义代理** 并输入 Bright Data 代理信息：
       * **代理类型**: 选择 HTTP、HTTPS 或 SOCKS5。
       * **代理主机**: 输入 `http://brd.superproxy.io/`。
       * **代理端口**: 使用您的 [Bright Data 仪表板](https://www.bright.cn/cp/zones/page/plans) 提供的端口号。
       * **用户名**: 输入您的 Bright Data 用户名。
       * **密码**: 输入您的 Bright Data 密码。

    3. 点击 **检查代理** 确保连接正常。
  </Step>

  <Step title="保存并启动配置文件">
    1. 代理信息验证成功后，点击 **创建配置文件** 以保存设置。
    2. 进入 **配置文件** 部分，找到刚创建的配置文件。
    3. 点击 **启动**，使用已配置的设置打开浏览器。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/genlogin2.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=271cba0057cede9811ce012db8a7d9aa" alt="" width="1900" height="307" data-path="images/integrations/genlogin2.png" />
    </Frame>
  </Step>

  <Step title="验证代理连接">
    1. 在已启动的浏览器配置文件中，打开浏览器并访问 [httpbin.org/ip](http://httpbin.org/ip)。
    2. 确保显示的 IP 地址与您的 Bright Data 代理匹配，以验证设置是否成功。
  </Step>
</Steps>

将 Bright Data 与 GenLogin 结合使用，能让您更安全、更高效地管理多个账户。Bright Data 的可靠代理结合 GenLogin 强大的浏览器配置管理功能，可以帮助您实现卓越的隐私保护和生产力优化。立即体验 Bright Data 和 GenLogin 的强大组合吧！
