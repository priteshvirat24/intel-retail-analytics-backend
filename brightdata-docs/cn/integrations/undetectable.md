> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何使用 Undetectable 设置 Bright Data

> 学习如何在 Undetectable 中配置 Bright Data，实现安全匿名浏览。本逐步指南将帮助您提升在线隐私和操作效率。

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

## 什么是 Undetectable?

Undetectable 是一款防检测浏览器，通过创建具有独特数字指纹的多个浏览器配置文件，实现安全和匿名浏览。非常适合管理多个账户、网页抓取及其他需要隐私和安全的操作。

<Tip>
  使用用户名中的 `-session` 参数可在整个浏览器会话中保持一致的 IP。这一点非常重要，因为 BrightData 代理默认每次请求都会更换 IP。[了解更多](/cn/proxy-networks/faqs#如何长时间使用相同-ip) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

## 如何将 Bright Data 与 Undetectable 集成

**步骤 1. 下载并登录 Undetectable**

1. 访问 [Undetectable 网站](https://undetectable.io/) 并下载应用程序。
2. 在系统上安装软件，并使用您的凭据登录。

**步骤 2. 访问代理配置**

1. 打开 Undetectable 并进入 **Proxy** 标签页。

<Frame as="div">
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/undetectable1.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=6d1b626060b47e0a5e85fb3d55272cc1" alt="" width="370" height="261" data-path="images/integrations/undetectable1.png" />
</Frame>

2. 点击 **加号** 按钮添加新代理。

<Frame as="div">
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/undetectable2.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=cfb08d13aa815eb470116c16a0d76728" alt="" width="690" height="187" data-path="images/integrations/undetectable2.png" />
</Frame>

**步骤 3. 配置 Bright Data 代理详细信息**

1. 在代理设置窗口：

* 在 **Proxy Name** 字段中提供描述性名称以便识别。
* **Type**：选择 HTTP 或 SOCKS5。
* **Host**：`http://brd.superproxy.io/`。
* **Port**：从您的 [Bright Data 仪表板](https://www.bright.cn/cp/zones/page/plans) 获取端口号。
* **Login**：您的 Bright Data 用户名。
* **Password**：您的 Bright Data 密码。

2. 点击 **Check** 验证连接。
3. 验证成功后，点击 **Save Proxy** 保存代理设置。

<Note>
  对于地理定位代理，将用户名格式化为 `your-username-country-XX`（例如 `your-username-country-US`）以选择特定位置。
</Note>

成功将 Bright Data 集成到 Undetectable 后，您现在可以安全且匿名地浏览。享受增强的隐私保护和无缝操作吧！
