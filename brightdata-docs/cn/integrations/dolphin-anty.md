> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 Dolphin Anty 中设置 Bright Data

> 使用 Dolphin Anty 和 Bright Data 代理增强您的网络爬取和多账户管理。享受安全、高效的数据提取和强大的反检测功能。

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

## 什么是 Dolphin Anty？

Dolphin Anty 是一款易于使用的反检测浏览器，专为需要管理多个账户而不被标记的营销人员、社交媒体管理者和电商专业人士打造。它为每个配置文件创建独特的数字指纹（如 IP 地址和设备类型），使平台无法将多个账户关联到同一用户。借助 Dolphin Anty，您可以安全地运行社交媒体广告活动、管理联盟营销以及处理电商任务，而无需担心账户被封。

<Tip>
  通过在用户名中使用 `-session` 参数，在整个浏览器会话中保持一致的 IP。这一点至关重要，因为 Bright Data 代理默认在每次请求时轮换 IP。[了解更多](/cn/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

## Dolphin Anty 代理集成

以下是快速入门指南：

### 第 1 步. **下载 Dolphin Anty**

访问 [Dolphin Anty 官网](https://dolphin-anty.com/) 下载并安装软件。

### 第 2 步. **创建并登录您的账户**

安装完成后，打开 Dolphin Anty，创建账户并登录。

### 第 3 步. **创建新配置文件**

点击 **+ 创建配置文件** 以开始设置新的浏览环境。

### 第 4 步. **添加新代理**

向下滚动至 **新代理** 部分，开始配置 Bright Data 代理。

### 第 5 步. **配置 Bright Data 代理**

按照以下格式输入您的代理信息：`type://host:port:username:password`

* **Type（类型）**：选择 `HTTP` 或 `SOCKS5`（根据您的代理类型）。
* **Host（主机）**：输入 [`http://brd.superproxy.io/`.](http://brd.superproxy.io/.)
* **Port（端口）**：使用 [Bright Data 控制面板](https://www.bright.cn/cp/zones) 中提供的端口号。
* **Username（用户名）**：输入您的 Bright Data 代理 `用户名`。
* **Password（密码）**：输入您的 Bright Data 代理 `密码`。

点击 **⮂ 测试连接** 按钮验证连接是否成功。

<Info>
  **如果需要特定国家的代理，可以输入类似 `your-username-country-US` 的格式，以获取美国出口节点。**
</Info>

### 第 6 步. **保存设置**

一切设置完成后，点击 **+ 创建** 以保存您的配置文件。

***

完成！您已成功将 Bright Data 代理集成到 Dolphin Anty 中。
