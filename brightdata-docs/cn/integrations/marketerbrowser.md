> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 MarketerBrowser 中使用 Bright Data

> 轻松提升您的浏览器配置文件管理能力，使用 Bright Data 与 MarketerBrowser 集成可确保您的连接安全，管理多个账户，并轻松访问特定地区的内容。按照本指南立即设置 Bright Data 与 MarketerBrowser 的集成。

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

## 什么是 MarketerBrowser？

<Tip>
  通过在用户名中使用 `-session` 参数，在整个浏览器会话期间保持一致的 IP 地址。这一点至关重要，因为 Bright Data 代理默认会在每次请求时轮换 IP。[了解更多](/cn/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

<Warning>
  不支持通过数据中心和 ISP 代理网络连接社交网络，包括：Facebook、TikTok、Instagram、X（Twitter）、LinkedIn、YouTube、Reddit、Pinterest、Snapchat 和 Discord。
</Warning>

**MarketerBrowser** 是一款专为管理多个账户或营销活动的专业人士设计的浏览器。它允许您创建隔离的浏览器配置文件，确保每个会话的安全性和隐私性。通过集成 **Bright Data**，您可以增强匿名性、访问受地理限制的内容，并降低被检测的风险。

## 如何在 MarketerBrowser 中集成 Bright Data

<Step title="安装并打开 MarketerBrowser">
  1. 从 [官方网站](https://www.marketerbrowser.com/) 下载 MarketerBrowser。
  2. 按照屏幕上的安装说明，在您的设备上完成应用程序的设置。
  3. 打开 MarketerBrowser 并使用您的凭据登录。如果您没有账户，请注册一个。
</Step>

<Step title="创建或编辑浏览器配置文件">
  1. 在 **Profiles**（配置文件）页面，点击 **Create Profile**（创建配置文件）以设置新的浏览器实例，或选择现有配置文件进行编辑。
  2. 在 **Name**（名称）字段中提供一个描述性名称，以便日后轻松识别。

  <Frame as="div">
    <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/marketerbrowser1.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=8252cdbb0021120499c04182a8900be7" alt="" width="761" height="329" data-path="images/integrations/marketerbrowser1.png" />
  </Frame>
</Step>

<Step title="配置代理设置">
  1. 在配置文件设置菜单中找到 **Proxy**（代理）部分。

  2. 输入您的 Bright Data 代理详细信息：
     * **Type**（类型）：选择 HTTP、HTTPS 或 SOCKS5。
     * **Server**（服务器）：输入 `http://brd.superproxy.io/`。
     * **Port**（端口）：输入您的 [Bright Data 控制面板](https://www.bright.cn/cp/zones) 中的端口号。
     * **Username**（用户名）：使用您的 Bright Data `username`。
     * **Password**（密码）：输入您的 Bright Data `password`。

  3. 点击 **Check**（检查）测试代理连接，以确保设置正确。

  4. 输入并测试代理详细信息后，点击 **Create**（创建）保存配置文件设置。
</Step>

<Step title="保存并激活配置文件">
  1. 转到 **Profiles**（配置文件）部分，选择您新配置的配置文件。
  2. 切换 **Launch**（启动）开关至 *On*，以使用 Bright Data 设置激活该配置文件。

  <Frame as="div">
    <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/marketerbrowser2.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=b874e81dac57c1cda72c3169cfcf33ba" alt="" width="1268" height="241" data-path="images/integrations/marketerbrowser2.png" />
  </Frame>
</Step>

<Step title="验证代理设置">
  1. 在已启动的配置文件中，打开浏览器并导航至 [httpbin.org/ip](http://httpbin.org/ip)。
  2. 确保显示的 IP 地址与您的 Bright Data 代理匹配，以验证设置是否正确。
</Step>

通过将 **Bright Data** 与 **MarketerBrowser** 集成，您可以创建一个无缝且安全的环境，用于管理多个账户、访问特定地区的内容，并保持匿名性。按照这些步骤优化您的工作流程，并使用 Bright Data 和 MarketerBrowser 提高隐私性！
