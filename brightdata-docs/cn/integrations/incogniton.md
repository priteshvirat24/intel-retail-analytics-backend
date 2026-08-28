> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何将 Bright Data 与 Incogniton 集成

> 将 Bright Data 集成到 Incogniton，实现无缝的多账户管理，提供安全、匿名的浏览体验，并增强防检测和防封禁能力。

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
  通过在用户名中使用 `-session` 参数，可以在整个浏览会话期间保持一致的 IP 地址。这一点至关重要，因为 Bright Data 代理默认会在每次请求时轮换 IP。[了解更多](/cn/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

## 什么是 Incogniton？

**Incogniton** 是一款专注于隐私保护的浏览器，旨在确保用户在浏览网络时保持匿名。它允许创建和管理多个配置文件，每个配置文件都有独立的 Cookie、本地存储、IP 地址（通过代理）以及其他浏览数据。这意味着您可以放心地上网，而无需担心活动被追踪或个人信息泄露。

Incogniton 适用于隐私保护用户、营销人员以及需要管理多个社交媒体或电商账户的企业。此外，它也适用于网络爬取和测试，能够模拟真实用户的浏览行为，同时确保活动安全且私密。

## Incogniton 代理集成

在 Incogniton 中设置 Bright Data 代理的过程快速且简单。请按照以下步骤进行操作：

<Steps>
  <Step title="下载 Incogniton">
    访问 [**Incogniton 官网**](https://incogniton.com/) 下载并安装该浏览器。
  </Step>

  <Step title="创建新配置文件">
    1. 安装完成后，打开 Incogniton 并进入 **Profile Management**（配置文件管理）部分。
    2. 点击 **New Profile**（新建配置文件）以创建您的第一个配置文件。
  </Step>

  <Step title="配置代理设置">
    在配置文件设置菜单中，点击左侧的 **Proxy**（代理），然后输入您的 Bright Data 代理信息：

    * **代理类型（Proxy Type）**: 选择 `HTTP`、`HTTPS` 或 `SOCKS5`（根据您的代理类型）。
    * **代理主机（Proxy Host）**: 输入 `http://brd.superproxy.io/`。
    * **代理端口（Proxy Port）**: 使用您在 [Bright Data 控制台](https://www.bright.cn/cp/zones) 中提供的端口号。
    * **代理用户名（Proxy Username）**: 输入您的 Bright Data 代理 `用户名`。
    * **代理密码（Proxy Password）**: 输入您的 Bright Data 代理 `密码`。

    点击 **Check Proxy**（检查代理）确认代理是否正常工作。

    <Info>
      **如果需要使用特定国家的代理，可以使用 `username-country-US` 格式（例如 `username-country-US` 以获取美国 IP）。**
    </Info>
  </Step>

  <Step title="保存配置文件">
    1. 输入所有必要信息后，点击 **Create Profile**（创建配置文件）以保存设置。
    2. 您现在可以安全浏览了！
  </Step>

  <Step title="开始浏览">
    点击 **Start**（开始）以在安全的无痕浏览窗口中启动您的配置文件，并开始匿名浏览。
  </Step>
</Steps>

就是这样！您已成功将 Bright Data 代理集成到 Incogniton 中。
