> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何将 Bright Data 与 Maskfog 集成

> 了解如何将 Bright Data 与 Maskfog 集成，以增强隐私保护并简化账户管理。按照本指南轻松完成设置。

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

## 什么是 Maskfog？

**Maskfog** 是一款反检测浏览器，专为安全匿名地管理多个账户而设计。它提供工具来防止检测、保护数字足迹，并为每个配置文件模拟独特的浏览器环境。将 Bright Data 与 Maskfog 集成，可为地理定位活动增加额外的安全性和灵活性。

<Tip>
  在您的浏览会话期间，使用 `-session` 参数在用户名中保持 IP 地址一致。这一点很重要，因为 Bright Data 代理默认在每次请求时轮换 IP。[了解更多](/cn/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

## 如何将 Bright Data 与 Maskfog 集成

<Step title="下载并安装 Maskfog">
  1. 访问 [Maskfog 官网](https://www.maskfog.com/)，下载适用于您的操作系统的应用程序。
  2. 安装软件并使用您的凭据登录。
</Step>

<Step title="创建新配置文件">
  1. 打开 Maskfog，导航到 **代理服务** 部分。
  2. 点击 **配置设备** 以开始设置新的代理。

  <Frame as="div">
    <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/maskfog1.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=66098359f4a870aa4bbad388c0b0d054" alt="" width="1598" height="385" data-path="images/integrations/maskfog1.png" />
  </Frame>
</Step>

<Step title="输入代理详情">
  1. 在 **代理名称** 字段中输入一个易于识别的名称，以便后续查找该配置。

  2. 输入从您的 [Bright Data 仪表盘](https://www.bright.cn/cp/zones/page/plans) 获取的以下信息：
     * **代理类型**：选择 HTTP、HTTPS 或 SOCKS5。
     * **代理主机**：输入 `http://brd.superproxy.io/`。
     * **代理端口**：使用您的 Bright Data 仪表盘提供的端口号。
     * **代理用户名**：输入您的 Bright Data `username`。
     * **代理密码**：输入您的 Bright Data `password`。

  3. 点击 **检查代理** 以测试代理连接。在继续之前，请确保连接成功。

  4. 验证后，点击 **确定** 以保存配置。

  <Note>
    如果您需要特定国家/地区的代理，请在用户名中包含国家代码。格式如下：
    `your-username-country-XX`（例如，`your-username-country-US`），以选择来自所需国家的代理。
  </Note>
</Step>

完成设置！代理成功配置后，Maskfog 现在已集成 Bright Data，支持安全匿名的连接。尽享增强的隐私保护和无缝浏览体验！
