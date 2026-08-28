> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何设置 Bright Data 与 AdsPower

> 使用 Bright Data 和 AdsPower 提升您的网络爬取和多账户管理能力。在管理多个账户时保持安全且不被检测到。

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

## 什么是 AdsPower？

使用 AdsPower 掌控您的多账户管理！这款多功能浏览器非常适合市场营销人员、电商企业和社交媒体管理者，它提供了一种安全高效的方式来同时管理多个账户。每个浏览器配置文件都在其独立的环境中运行，确保您的活动不会被检测到或标记为异常。

AdsPower 为每个配置文件提供独特的数字指纹，包括 IP 地址、设备类型和用户代理等信息，使您的操作始终保持低调。不论是扩展电商业务、运行社交媒体广告活动，还是从事联盟营销，AdsPower 都能让您的多账户管理变得流畅且安全。

<Tip>
  通过在用户名中使用 `-session` 参数，在浏览会话期间保持一致的 IP。这一点很重要，因为 Bright Data 代理默认会在每次请求时轮换 IP。[了解更多](/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

## AdsPower 代理集成

将 Bright Data 代理与 AdsPower 集成简单快捷，按照以下步骤进行设置：

### 步骤 1. **下载 AdsPower**

前往 [AdsPower 官网](https://www.adspower.com/download) 下载并安装该应用程序。

### 步骤 2. **创建新配置文件**

安装完成后，打开应用程序，点击 **新建配置文件** 来创建您的第一个浏览器配置文件。

<Frame as="div">
  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/adspower1.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=bd012b7b56effe44847cf6b32cadefda" alt="" width="1016" height="508" data-path="images/integrations/adspower1.png" />
</Frame>

### 步骤 3. **配置您的代理**

接下来，我们来设置 Bright Data 代理，按照以下步骤操作：

* **代理类型**: 选择 `HTTP`、`HTTPS` 或 `SOCKS5`（根据您的代理类型）。
* **代理主机**: 输入 [`http://brd.superproxy.io/`](http://brd.superproxy.io/)。
* **代理端口**: `44445`
* **代理用户名**: 输入您的 Bright Data 代理区域 `username`。
* **代理密码**: 输入您的 Bright Data 代理区域 `password`。

### 步骤 4. **测试代理连接**

点击 **检查代理** 以确保代理配置正确。

<Note>
  某些版本的 AdsPower 使用 `google.com` 作为默认的测试网站。Bright Data 代理会阻止对 `google.com` 的访问，因此请确保测试网站不是搜索引擎网站。
</Note>

<Note>
  如果您选择了住宅代理或移动代理，必须安装 Bright Data SSL 证书，以确保端到端通信的安全性。**否则，您将遇到连接错误**。
  SSL 安装指南可在 [此处](/general/account/ssl-certificate#ssl-certificate) 找到。
  另外，您可以在 AdsPower 中忽略 SSL 验证：在设置配置文件时，进入高级设置，在启动参数中粘贴 `--ignore-certificate-errors`。
</Note>

<Info>
  **如果需要特定国家的代理，可以输入格式 `your-username-country-us` 来获得美国出口节点。**
</Info>

所有设置完成后，点击 **确定** 保存配置。

### 步骤 5. **启动浏览器**

在 **标签** 下点击 **打开** 以启动已配置代理的浏览器。

<Frame as="div">
  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/adspower4.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=1e68f7a77c870a64f065f59430e4f0ac" alt="" width="1310" height="273" data-path="images/integrations/adspower4.png" />
</Frame>

就这样！您已成功将 Bright Data 代理集成到 AdsPower 中，现在可以开始使用了！
