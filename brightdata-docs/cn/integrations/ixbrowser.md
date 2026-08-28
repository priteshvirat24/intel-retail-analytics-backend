> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何将 Bright Data 与 IXBrowser 集成

> 使用 Bright Data 和 IXBrowser 简化您的账户管理并保护您的浏览安全。按照本指南配置 Bright Data，以实现无缝且匿名的 IXBrowser 体验。

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

## 什么是 IXBrowser？

<Tip>
  在您的浏览会话期间保持一致的 IP，请在用户名中使用 `-session` 参数。这一点至关重要，因为 Bright Data 代理默认情况下会在每次请求时更换 IP。[了解更多](/cn/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

<Warning>
  不支持通过数据中心和 ISP 代理网络连接社交网络，包括：Facebook、TikTok、Instagram、X（Twitter）、LinkedIn、YouTube、Reddit、Pinterest、Snapchat 和 Discord。
</Warning>

**IXBrowser** 是一款专注于隐私的防检测浏览器，旨在帮助用户管理多个平台上的账户。它提供了高级匿名功能，使用户能够绕过限制并避免检测。将 Bright Data 与 IXBrowser 集成可以进一步增强隐私保护，并实现地理定位浏览。

## 如何将 Bright Data 与 IXBrowser 集成

<Steps>
  <Step title="下载并安装 IXBrowser">
    1. 访问 [IXBrowser 官网](https://ixbrowser.com/) 并下载应用程序。
    2. 安装软件并使用您的账户凭据登录。
  </Step>

  <Step title="创建新配置文件">
    1. 打开 IXBrowser，进入 **浏览器配置** 下的 **配置文件列表** 版块。
    2. 点击 **创建新配置文件** 以开始设置新的浏览器实例。
    3. 在配置文件设置中，在 **配置文件名称** 字段输入一个描述性名称，以便稍后轻松识别您的配置文件。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/ixbrowser1.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=dff907199d2e46177f8ccc24db657ea5" alt="" width="1364" height="197" data-path="images/integrations/ixbrowser1.png" />
    </Frame>
  </Step>

  <Step title="配置代理设置">
    1. 在配置文件设置页面，切换到 **代理配置** 选项卡。

    2. 选择 **自定义** 以启用代理设置选项。

    3. 填写从您的 [Bright Data 控制面板](https://www.bright.cn/cp/zones) 获取的代理信息：
       * **代理类型**：根据您的代理类型选择 HTTP、HTTPS 或 SOCKS5。
       * **代理主机**：`http://brd.superproxy.io/`
       * **代理端口**：输入 Bright Data 控制面板中的端口号。
       * **代理账号**：使用您的 Bright Data `用户名`。
       * **代理密码**：使用您的 Bright Data `密码`。

    4. 输入完毕后，点击 **创建** 以保存配置。

    <Note>
      若使用地理定位代理，请按照 `your-username-country-XX` 格式设置您的用户名（例如：`your-username-country-US`），以访问特定地区。
    </Note>
  </Step>

  <Step title="启动配置文件">
    1. 返回 **配置文件列表** 版块。
    2. 找到您新创建的配置文件，点击 **打开** 以使用配置的 Bright Data 代理设置启动浏览器。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/ixbrowser2.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=68b4a9cc70ff0c048252378a0925b663" alt="" width="1353" height="278" data-path="images/integrations/ixbrowser2.png" />
    </Frame>
  </Step>
</Steps>

将 Bright Data 与 IXBrowser 集成可确保私密且可靠的账户管理，同时提升您的在线匿名性。无论您是管理多个账户还是进行地理定位操作，此设置都能为您提供安全无缝的浏览体验。立即开始，享受更高效的操作体验！
