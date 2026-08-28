> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 Multilogin 中设置 Bright Data

> 将 Bright Data 集成到 Multilogin 可增强您的多账户管理，提供安全、不可检测的浏览体验，提高隐私性并降低账户被封的风险。

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

## 什么是 Multilogin？

Multilogin 是一款强大的浏览器工具，可用于管理多个在线账户，而不会被检测或封禁。它是市场营销人员、电商专业人士、联盟营销人员和增长黑客的热门选择，能够绕过检测相同 IP 地址或设备的限制。

Multilogin 通过创建隔离的、独特的浏览配置文件来模拟不同的设备。每个配置文件看起来都像是从不同的位置或设备访问的，使平台无法关联账户。这确保了更安全、更隐蔽的浏览体验，让您可以放心管理多个账户。

<Tip>
  通过在用户名中使用 `-session` 参数，在整个浏览会话中保持一致的 IP。这一点很重要，因为 Bright Data 代理默认会在每次请求时轮换 IP。[了解更多](/cn/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

<Warning>
  不支持通过数据中心和 ISP 代理网络连接社交网络，包括：Facebook、TikTok、Instagram、X（Twitter）、LinkedIn、YouTube、Reddit、Pinterest、Snapchat 和 Discord。
</Warning>

## Multilogin 代理集成

按照以下简单步骤在 Multilogin 中设置 Bright Data 代理：

<Steps>
  <Step title="打开 Multilogin">
    启动 [**Multilogin 应用**](https://multilogin.com/) 并登录您的账户。
  </Step>

  <Step title="创建新配置文件">
    点击 **“新建配置文件”** 并输入以下信息：

    * **配置文件名称**：选择一个易识别的名称（如 *Bright Data*）。
    * **操作系统**：选择与您的原始设置匹配的操作系统（macOS、Windows 或 Linux），以避免指纹不匹配。
    * **存储类型**：如果需要在团队中协作或在多个设备上使用该配置文件，请选择 **云存储**。
    * **浏览器类型**：选择 **Mimic**（基于 Chrome）或 **Stealthfox**（基于 Firefox），它们都具有强大的防检测功能。
  </Step>

  <Step title="添加代理">
    在配置文件设置中，找到 **代理** 选项并选择 **自定义**。
  </Step>

  <Step title="配置 Bright Data 代理">
    按照以下步骤输入您的 Bright Data 代理信息：

    * **代理类型**：选择 `HTTP`、`HTTPS` 或 `SOCKS5`（根据您的 Bright Data 代理类型）。
    * **地址**：输入 `http://brd.superproxy.io/`。
    * **端口**：使用您的 [Bright Data 仪表盘](https://www.bright.cn/cp/zones) 提供的端口号。
    * **登录名**：输入您的 Bright Data 代理 `用户名`。
    * **密码**：输入您的 Bright Data 代理 `密码`。

    点击 **检查代理** 以验证连接。

    <Info>
      **如需特定国家/地区的代理，可使用 `your-username-country-US` 格式，以获得美国出口节点。**
    </Info>
  </Step>

  <Step title="保存设置">
    输入完所有代理信息后，点击 **创建配置文件** 以保存设置。
  </Step>
</Steps>

就是这样！您已成功将 Bright Data 代理集成到 Multilogin。
