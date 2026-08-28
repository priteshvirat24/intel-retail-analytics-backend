> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何将 Bright Data 与 HideMyAcc 集成

> 使用 Bright Data 和 HideMyAcc 保护并优化您的浏览体验。本指南将指导您如何在 HideMyAcc 中配置 Bright Data，以实现私密、可靠和高效的账户管理。

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

<Tip>
  通过在用户名中使用 `-session` 参数，可以在整个浏览会话期间保持一致的 IP 地址。这一点至关重要，因为 Bright Data 代理默认情况下会在每次请求时轮换 IP。[了解更多](/cn/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

## 什么是 HideMyAcc？

**HideMyAcc** 是一款高级防检测浏览器，专为安全管理多个账户而设计。它可帮助用户绕过限制、保持匿名，并通过提供私密的浏览环境避免被检测。集成 Bright Data 可以增强 HideMyAcc 的功能，实现安全的地理定向连接。

## 如何在 HideMyAcc 中集成 Bright Data

<Steps>
  <Step title="下载并安装 HideMyAcc">
    1. 访问 [HideMyAcc 官网](https://hidemyacc.com/)，下载适用于您的操作系统的软件。
    2. 安装应用程序并使用您的账户凭据登录。
  </Step>

  <Step title="创建新配置文件">
    1. 打开 HideMyAcc，导航到 **Profiles**（配置文件）选项卡。
    2. 点击 **Create a new profile**（创建新配置文件）以设置新的浏览实例。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/hidemyacc1.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=9de473f20401802c05b4b25d896f73e5" alt="" width="1349" height="535" data-path="images/integrations/hidemyacc1.png" />
    </Frame>
  </Step>

  <Step title="启用代理配置">
    1. 在配置文件创建页面，找到 **Proxy**（代理）部分。
    2. 在配置文件设置中输入 **Profile Name**（配置文件名称），以便后续识别。
    3. 切换 **Your Proxy**（您的代理）选项以激活配置。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/hidemyacc2.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=41336440b71ba65e51564fe740acaab6" alt="" width="1331" height="254" data-path="images/integrations/hidemyacc2.png" />
    </Frame>
  </Step>

  <Step title="添加 Bright Data 代理详情">
    1. 前往 [Bright Data 控制台](https://www.bright.cn/cp/zones)，点击要使用的代理区域。
    2. 在 **Overview**（概览）选项卡下，复制 Bright Data 提供的代理访问详细信息，格式为：`host:port:username:password`。
    3. 将此代码粘贴到 HideMyAcc 的 **Quick add**（快速添加）字段中。
    4. 使用 **Check Proxy**（检查代理）选项验证连接是否正常。
    5. 代理配置验证成功后，点击 **Create**（创建）以保存代理设置。

    <Note>
      如果需要使用特定国家的代理，可以使用 `your-username-country-XX`（例如 `your-username-country-US`）格式的用户名，以指定目标地区。
    </Note>
  </Step>

  <Step title="启动配置文件">
    导航到 **Profiles** 选项卡，选择刚创建的配置文件，然后点击 **Run**（运行）以使用 Bright Data 进行安全浏览。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/hidemyacc3.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=9a045acbf9b4d27f00aa357537d71974" alt="" width="1331" height="135" data-path="images/integrations/hidemyacc3.png" />
    </Frame>
  </Step>
</Steps>

通过将 **Bright Data** 与 **HideMyAcc** 集成，您可以享受更高的隐私保护和无缝的账户管理体验。无论是管理多个账户，还是执行地理定向任务，此设置都能确保您的浏览体验既安全又高效。立即开始，享受私密、可靠的浏览环境！
