> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 Firefox 中配置代理设置

> 掌控您的在线体验！在 Firefox 中设置代理可为您的浏览提供安全防护——无论是增强隐私、绕过限制，还是轻松管理多个账户，它都能助您一臂之力。按照本指南设置代理，释放 Firefox 的全部潜力。

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
  通过在用户名中使用 `-session` 参数，确保整个浏览会话使用一致的 IP。这一点至关重要，因为 Bright Data 代理默认会在每次请求时更换 IP。[了解更多](/cn/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

## 在 Firefox 中更改代理设置

掌控您的 Firefox 浏览体验！设置代理很简单——按照以下步骤轻松完成配置：

<Steps>
  <Step title="访问 Firefox 设置">
    启动 Firefox 并点击位于右上角的 **菜单图标**（三条横线）。\
    在下拉菜单中选择 **设置**，进入浏览器的配置菜单。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/firefox1.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=32492262d4b037fd13e11c83c73bbf0f" alt="" width="414" height="954" data-path="images/integrations/firefox1.png" />
    </Frame>
  </Step>

  <Step title="进入网络设置">
    在设置菜单中向下滚动，找到 **网络设置** 部分。\
    点击 **设置**，打开代理配置窗口。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/firefox2.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=cba94c178b127480447c583e904f116e" alt="" width="1571" height="867" data-path="images/integrations/firefox2.png" />
    </Frame>
  </Step>

  <Step title="设置代理配置">
    在代理设置窗口中，按照以下步骤操作：

    1. 选择 **手动代理配置**，启用自定义代理设置。
    2. 输入必要的信息：

    * **HTTP 代理**：输入 `http://brd.superproxy.io/`。
    * **端口**：输入您的 [Bright Data 控制面板](https://www.bright.cn/cp/zones) 中显示的端口号。

    3. （可选）启用 **对所有协议使用相同的代理服务器**，以应用相同的代理设置。
    4. 如果使用 SOCKS 代理，选择 **SOCKS v5** 并填写相应的服务器信息。
  </Step>

  <Step title="进行身份验证">
    当您访问某些网站时，Firefox 可能会要求您输入身份验证信息。\
    请输入您的 Bright Data 账户 **用户名** 和 **密码** 进行验证。
  </Step>
</Steps>

### 收到“软件阻止 Firefox 安全连接到此网站”的错误提示？

您可能正在尝试访问被 Bright Data 策略阻止的网站。我们经常在通过数据中心、ISP、住宅或移动代理访问 [google.com](http://google.com) 时看到这种情况。请尝试访问其他网站；我们建议您使用我们的测试网站来验证代理连接是否正常： [https://geo.brdtest.com/welcome.txt](https://geo.brdtest.com/welcome.txt) 。

就是这么简单！您的 Firefox 浏览器现已成功配置 **Bright Data** 代理，让您的浏览体验更加安全、私密。无论是管理账户、执行重要任务，还是畅游无阻的互联网，您都已准备就绪，享受更快速、安全、可靠的在线旅程。
