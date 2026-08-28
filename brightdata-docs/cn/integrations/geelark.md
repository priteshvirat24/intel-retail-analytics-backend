> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 Geelark 中使用 Bright Data

> 将 Bright Data 与 Geelark 集成，以最大限度地提高您的隐私和效率。本指南将指导您配置 Bright Data 代理，以便在 Geelark 中实现安全匿名浏览。

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
  通过在用户名中使用 `-session` 参数，在整个浏览会话中保持一致的 IP 地址。这很重要，因为 Bright Data 代理默认在每次请求时更换 IP。[了解更多](/cn/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

## 什么是 Geelark？

**Geelark** 是一款面向隐私保护用户和专业人士的多功能浏览器配置文件管理工具。它允许您创建独立的浏览环境、管理多个账户，并根据您的需求自定义浏览配置文件。通过 Bright Data，您可以将 Geelark 配置文件提升到新的水平，实现匿名访问、绕过限制并获取特定区域的内容。

## 如何将 Bright Data 集成到 Geelark

<Steps>
  <Step title="先决条件">
    1. **Bright Data 代理凭据**：
       * 登录您的 [Bright Data 仪表板](https://www.bright.cn/cp/zones) 获取 **Host**、**Port**、**Username** 和 **Password**。
       * 如果需要特定地区的代理，请使用地理位置特定的用户名（例如 `your-username-country-US`）。

    2. **安装 Geelark**：
       * 从 [geelark.com](https://geelark.com/) 下载并安装 Geelark。
       * 启动 Geelark 并使用您的账户凭据登录。
       * 如果没有账户，请点击 **Sign Up** 进行注册。
  </Step>

  <Step title="创建并配置新配置文件">
    1. 在 Geelark 仪表板上，点击 **New Profile**（新建配置文件）。
    2. 输入 **名称** 并选择该配置文件的目标操作系统。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/geelark1.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=158f9dc832276c407c9b8c1f6687ae45" alt="" width="761" height="239" data-path="images/integrations/geelark1.png" />
    </Frame>
  </Step>

  <Step title="配置代理设置">
    1. 在 **Proxy Settings**（代理设置）部分，选择 **Custom**（自定义）。

    2. 根据您的 Bright Data 配置选择 **代理类型**（HTTP、HTTPS 或 SOCKS5）。

    3. 输入以下 Bright Data 代理信息：
       * **代理主机**：`http://brd.superproxy.io/`。
       * **端口**：使用您的 [Bright Data 仪表板](https://www.bright.cn/cp/zones) 提供的端口号。
       * **用户名**：您的 Bright Data `用户名`。
       * **密码**：您的 Bright Data `密码`。

    4. 点击 **Check Proxy**（检查代理）以验证代理设置。在继续之前确保连接成功。
  </Step>

  <Step title="保存并启动配置文件">
    1. 配置代理设置后，点击 **OK** 保存配置文件。
    2. 在 Geelark 仪表板中，找到新创建的配置文件，然后点击 **Start**（启动）以运行它。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/geelark2.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=299a08057cb44f9a32e41d2c54e416c8" alt="" width="1198" height="241" data-path="images/integrations/geelark2.png" />
    </Frame>
  </Step>

  <Step title="测试您的设置">
    1. 在启动的配置文件中，打开 Web 浏览器。
    2. 访问 [httpbin.org/ip](http://httpbin.org/ip) 以验证您的 IP 地址是否反映为 Bright Data，确认设置成功。
  </Step>
</Steps>

将 Bright Data 集成到 Geelark 后，您将获得更强的隐私保护、控制能力和高效的浏览体验。无论您是管理多个浏览器配置文件、访问地理限制内容，还是确保安全连接，Bright Data 都能帮助您轻松实现目标。立即尝试，提升您的 Geelark 体验！
