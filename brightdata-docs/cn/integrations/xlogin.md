> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 XLogin 中使用 Bright Data

> 使用 Bright Data 的安全匿名代理增强 XLogin 体验。本指南将引导您设置 Bright Data 代理，实现更顺畅、安全和高效的在线自动化。

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
  使用用户名中的 `-session` 参数可在整个浏览器会话中保持一致的 IP。这一点非常重要，因为 BrightData 代理默认每次请求都会更换 IP。[了解更多](/cn/proxy-networks/faqs#如何长时间使用相同-ip) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

## 什么是 XLogin?

XLogin 是一款浏览器配置文件管理工具，帮助您运行多个在线账户而不会互相干扰。每个配置文件都像一个独立的隔离浏览器环境，使处理电商运营扩展、管理社交媒体活动和进行详细研究等任务更加轻松。通过集成 Bright Data 代理，您为每个配置文件增加了一层隐私和可靠性。

## 为什么在 XLogin 中使用 Bright Data?

将 Bright Data 代理与 XLogin 结合可带来：

* **增强隐私**：使用安全匿名代理隐藏真实 IP。
* **降低检测风险**：通过不同 IP 分散活动，减少封禁或限制。
* **稳定连接**：访问特定地区内容并在多个配置文件间保持一致可靠的会话。

## 前置条件

开始之前：

* **XLogin 账户**：如果还没有，请在 [XLogin 官网](https://xlogin.us/) 注册。
* **Bright Data 代理凭据**：请参考本页顶部说明。

## 逐步集成指南

**步骤 1. 登录 XLogin**

1. 访问 [XLogin](https://xlogin.us/) 并输入您的 XLogin 凭据。
2. 进入仪表板后，如果之前创建过配置文件，将会显示列表。

**步骤 2. 创建或选择浏览器配置文件**

1. 如果您是 XLogin 新用户，点击 **"New browser profile"**（或类似按钮）创建新的浏览器配置文件。
2. 如果已有配置文件，选择要通过 Bright Data 代理运行的配置文件，然后点击 **"Edit"** 或 **"Settings"** 进行配置。

<Frame as="div">
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/xlogin1.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=e780377078d05097c518c0ba646becc3" alt="" width="239" height="265" data-path="images/integrations/xlogin1.png" />
</Frame>

**步骤 3. 个性化并配置浏览器配置文件**

首先，为浏览器配置文件输入清晰的 **“Display name”**，以便清楚区分。然后点击 **“Setting proxy server”** 按钮打开代理配置面板。如果找不到，可查看高级菜单或参考 XLogin 文档。

**步骤 4. 输入 Bright Data 代理详情**

1. 根据 Bright Data 代理类型选择正确协议 (`HTTP`、`HTTPS` 或 `SOCKS5`)。

2. 填写必填字段：
   * **Host**：您的 Bright Data host（例如 [`http://brd.superproxy.io/`](http://brd.superproxy.io/)）。
   * **Port**：由 [Bright Data 仪表板](https://www.bright.cn/cp/zones) 提供的端口号。
   * **Username**：您的 Bright Data 代理 `username`。
   * **Password**：您的 Bright Data 代理 `password`。

3. 仔细检查准确性——任何拼写错误或错误信息都可能导致连接失败。

<Note>
  想使用美国出口节点？在用户名后附加 `-country-US`（例如 `your-username-country-US`）。其他国家同理，只需替换国家代码。
</Note>

**步骤 5. 保存设置**

完成设置前，点击 **"Test Proxy"** 验证连接是否正常。如果一切正常，点击 **"Save"** 完成配置。最后确保记录的详细信息与预期代理设置一致。

**步骤 6. 测试代理连接**

1. 启动更新后的浏览器配置文件。
2. 访问网站，如 [http://httpbin.org/ip](http://httpbin.org/ip)。
3. 确认显示的 IP 与 Bright Data 代理的 IP 匹配，而不是您的真实 IP。如果匹配，则设置成功。

完成以上步骤，您已成功将 **Bright Data** 代理集成到 **XLogin**。现在，您拥有更高的隐私性、降低的检测风险和更稳定的连接，可更自信高效地管理多个配置文件。享受更顺畅、更安全的浏览体验吧！
