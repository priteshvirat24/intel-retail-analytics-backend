> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 Kameleo 中设置 Bright Data

> 将 Bright Data 与 Kameleo 集成，实现安全浏览和高效管理多个配置文件，提供增强的隐私保护和强大的反检测能力。

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

## 什么是 Kameleo？

Kameleo 是一款先进的反检测浏览器，专为需要管理多个在线配置文件而又不希望被检测到的用户设计。无论您是社交媒体经理、联盟营销人员、电商运营者，还是网页爬取者，Kameleo 都能为您提供绕过 IP 封禁、防止设备追踪、避免账户关联的工具。

借助 Kameleo，您可以自定义浏览器指纹（如用户代理、屏幕分辨率和字体），确保每个配置文件看起来都是独立的，从而避免被检测。Kameleo 支持多种代理，包括住宅代理、数据中心代理和 ISP 代理，让您可以为每个配置文件分配不同的 IP 地址和数字身份。这使其非常适合在社交媒体、电商网站等多个平台上管理多个账户，并且可以在单个会话中完成所有操作。

除了强大的反检测功能外，Kameleo 还支持自动化工具，非常适用于批量任务，如自动发帖或数据爬取。无论您是管理少量账户，还是需要扩展规模，Kameleo 都能在优化在线活动的同时，确保您的隐私和安全。

<Tip>
  在浏览器会话期间保持 IP 地址一致，请在用户名中使用 `-session` 参数。这很重要，因为 Bright Data 代理默认会在每次请求时更换 IP 地址。[了解更多](/cn/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

## Kameleo 代理集成

按照以下步骤，将 Bright Data 代理集成到 Kameleo：

<Steps>
  <Step title="打开 Kameleo">
    启动 [**Kameleo 应用**](https://kameleo.io/downloads/)，并登录您的账户。
  </Step>

  <Step title="创建新配置文件">
    点击左侧导航面板中的 **New Profile**（新建配置文件）选项，开始设置新的浏览器配置文件。
  </Step>

  <Step title="配置您的配置文件偏好">
    选择与您的设备类型、操作系统、浏览器和语言设置匹配的配置文件选项。
  </Step>

  <Step title="配置 Bright Data 代理">
    进入配置文件设置中的 **Connection**（连接）部分，并输入以下信息来配置 Bright Data 代理：

    * **代理类型**：根据您的代理类型，选择 `HTTP`、`HTTPS` 或 `SOCKS5`。
    * **主机地址**：输入 `http://brd.superproxy.io/`。
    * **端口**：使用您在 [Bright Data 控制面板](https://www.bright.cn/cp/zones) 中提供的端口号。
  </Step>

  <Step title="启用身份验证">
    点击 **Authentication**（身份验证）按钮，显示 `用户名` 和 `密码` 字段。\
    在此处输入您的 Bright Data 代理凭据。

    为了确保设置正确，点击 **Test Proxy**（测试代理）按钮，运行多个测试来检查代理连接。

    <Info>
      **如果需要特定国家的代理，您可以使用 `your-username-country-US` 这样的格式，以获取美国出口节点。**
    </Info>
  </Step>

  <Step title="保存设置">
    配置完成后，点击 **OK**（确定）保存您的设置。

    或者，点击 **START**（启动），立即使用您的配置文件打开浏览器。
  </Step>
</Steps>

就这样！您已成功将 Bright Data 代理集成到 Kameleo 中。
