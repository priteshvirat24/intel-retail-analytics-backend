> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 Octo Browser 中设置 Bright Data

> 将 Bright Data 集成到 Octo Browser，以增强您的多账户管理和网页抓取能力，同时提供强大的防检测功能和安全的浏览体验。

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

## 什么是 Octo Browser？

Octo Browser 是一款智能工具，可帮助您管理多个在线账户，而不会被检测或封禁。它非常适合营销人员、电商卖家和网页抓取者，让您可以安全地操作多个账户。

Octo Browser 通过创建独立的配置文件，每个文件都有自己独特的设置，如 IP 地址和设备信息，从而确保账户之间不会关联。它支持 HTTP、HTTPS 和 SOCKS5 代理，并提供自动化和团队协作等功能，是一款强大且易于使用的安全高效在线工具。

<Tip>
  在浏览器会话期间保持一致的 IP 地址，需在用户名中使用 `-session` 参数。这很重要，因为 Bright Data 代理默认在每次请求时轮换 IP。[了解更多](/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

<Warning>
  不支持通过数据中心和 ISP 代理网络连接社交网络，包括：Facebook、TikTok、Instagram、X（Twitter）、LinkedIn、YouTube、Reddit、Pinterest、Snapchat 和 Discord。
</Warning>

## Octo Browser 代理集成

以下是将 Bright Data 代理集成到 Octo Browser 的方法：

<Steps>
  <Step title="安装 Octo Browser">
    下载并安装 [**Octo Browser**](https://octobrowser.net/download/)，然后登录您的账户。
  </Step>

  <Step title="创建配置文件">
    1. 进入 **Profiles**（配置文件）页面，点击 **Create Profile**（创建配置文件）。
    2. 为您的配置文件命名，并设置所需的参数。
  </Step>

  <Step title="添加代理">
    1. 在配置文件设置中，进入 **Connection**（连接）选项卡，并点击 **Proxy**（代理）字段。
    2. 点击 **+ Set a new proxy**（+ 设置新代理）以打开代理配置窗口。
  </Step>

  <Step title="配置 Bright Data 代理">
    在弹出窗口中，输入您的 Bright Data 代理信息：

    * **Host**: 输入 `http://brd.superproxy.io/`。
    * **Port**: 使用您在 [Bright Data 控制面板](https://www.bright.cn/cp/zones) 中提供的端口号。
    * **Login**: 输入您的 Bright Data 代理 `username`。
    * **Password**: 输入您的 Bright Data 代理 `password`。

    <Info>
      **如果需要使用特定国家的代理，可以使用格式 `your-username-country-US` 以获取美国出口节点。**
    </Info>
  </Step>

  <Step title="测试代理">
    1. 点击 **Check Proxy**（检查代理）以确保连接正常。
    2. 确认无误后，点击 **Confirm**（确认）以保存代理设置到配置文件。
  </Step>

  <Step title="保存并启动配置文件">
    1. 点击 **Create Profile**（创建配置文件）以保存您的设置。
    2. 在 **Profiles**（配置文件）页面，点击 **Start**（启动）即可运行您配置好的浏览器环境。
  </Step>
</Steps>

就这样！您已成功将 Bright Data 代理集成到 Octo Browser。
