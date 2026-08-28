> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何将 Bright Data 与 SessionBox 集成

> 使用 Bright Data 与 SessionBox 可实现安全高效的多会话浏览，提供灵活的代理解决方案，帮助实现无痕、顺畅的账户管理。

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

## 什么是 SessionBox？

SessionBox 是一个浏览器扩展，可让你同时管理多个浏览会话。使用 SessionBox，你可以在同一网站登录多个账户而不会冲突——每个标签页作为独立隔离的会话运行。它将 Cookie、缓存和登录凭据限制在各自标签页内，为多账户管理提供了简单而有效的解决方案。

SessionBox 注重简洁和浏览器原生功能，适合轻量任务，如社交媒体管理、基础账户切换及其他简单在线操作。

<Tip>
  使用用户名中的 `-session` 参数，可在整个浏览会话中保持 IP 一致。这很重要，因为 Bright Data 代理默认每次请求都会轮换 IP。[了解更多](/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

## SessionBox 代理集成

按照以下步骤将 Bright Data 代理与 SessionBox 集成：

**步骤 1. 安装 SessionBox**\
下载并安装 [SessionBox 扩展](https://chrome.google.com/webstore/detail/sessionbox-multi-login-to/megbklhjamjbcafknkgmokldgolkdfig)（Chrome）。

**步骤 2. 打开设置**\
点击浏览器工具栏中的 **SessionBox 图标**，再点击 **三条横线** 打开菜单，选择 **Settings**。

**步骤 3. 添加代理**\
在设置中进入 **Proxy** 标签页，点击 **Add New** 创建新代理配置。

<Frame as="div">
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/sessionbox2.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=07c7dc8354eec2e2a072b74660664502" alt="" width="345" height="547" data-path="images/integrations/sessionbox2.png" />
</Frame>

**步骤 4. 配置 Bright Data 代理**\
在字段中输入你的 Bright Data 代理信息：

* **地址 (Address)**: 输入 `http://brd.superproxy.io/`
* **端口 (Port)**: 使用 [Bright Data 控制面板](https://www.bright.cn/cp/zones/page/plans) 提供的端口
* **用户名 (Username)**: 输入 Bright Data 代理用户名
* **密码 (Password)**: 输入 Bright Data 代理密码

点击 **Save** 保存代理设置。

<Info>
  对于特定国家代理，可使用格式 `your-username-country-US` 来获取美国出口节点。
</Info>

**步骤 5. 创建新会话**\
添加代理后，将其分配到新会话：

1. 打开任意网站并启动 SessionBox 插件
2. 点击 **New Stored Session** 创建会话

**步骤 6. 为会话配置代理**\
新标签页打开后，操作如下：

1. 再次打开插件
2. 点击会话旁的 **三点**，选择 **Settings**

**步骤 7. 启用代理**\
在 **Settings** 菜单中进入 **Other** 标签页，找到 **Proxy** 部分，选择你之前创建的代理配置。

**完成！**\
你的 Bright Data 代理现在已成功集成到 SessionBox，可安全、高效地进行多会话浏览和账户管理。
