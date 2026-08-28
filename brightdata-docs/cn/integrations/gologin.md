> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 GoLogin 中设置 Bright Data

> 通过 GoLogin 和 Bright Data 增强您的网络爬取与多账户管理，实现强大的反检测功能和灵活的代理控制。

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

## 什么是 GoLogin？

<Tip>
  通过在用户名中使用 `-session` 参数，可以在整个浏览器会话期间保持一致的 IP。这一点至关重要，因为 Bright Data 代理默认在每次请求时轮换 IP。[了解更多](/cn/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

GoLogin 是一款强大的工具，专为轻松安全地管理多个账户而设计。它允许您创建独立的浏览器配置文件，每个配置文件都具有唯一的指纹、IP 和 Cookie，使其看起来像不同的独立用户。这对于营销人员、电商企业以及任何需要管理多个账户的用户而言，都是理想的解决方案。

使用 GoLogin，您可以集成代理、自动化任务，并无缝切换不同的配置文件，同时保持每个账户的匿名性。它不仅能够确保账户安全，还支持团队协作，使团队成员能够安全地共享配置文件。无论您是专注于数字营销、数据爬取，还是账户安全管理，GoLogin 都是一个出色的选择。

## GoLogin 代理集成

按照以下步骤将 Bright Data 代理集成到 GoLogin：

<Steps>
  <Step title="安装 GoLogin">
    从 [GoLogin 官网](https://gologin.com/) 下载并安装 GoLogin。
  </Step>

  <Step title="创建账户">
    登录 GoLogin，开始设置您的浏览器配置文件。
  </Step>

  <Step title="创建新配置文件">
    点击 **+添加配置文件**，输入您的新浏览器配置文件的基本信息。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/gologin1.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=55c444e98d731a7ae0963f86406d2da7" alt="" width="1164" height="126" data-path="images/integrations/gologin1.png" />
    </Frame>
  </Step>

  <Step title="配置代理设置">
    输入您的 Bright Data 代理信息：

    * **代理类型**：选择 `HTTP`、`HTTPS` 或 `SOCKS5`（根据您的代理类型）。
    * **主机**：输入 `http://brd.superproxy.io/`。
    * **端口**：使用 [Bright Data 仪表盘](https://www.bright.cn/cp/zones) 提供的端口号。
    * **用户名**：输入您的 Bright Data 代理 `用户名`。
    * **密码**：输入您的 Bright Data 代理 `密码`。

    <Info>
      **您还可以指定代理的国家/地区。例如，输入 `your-username-country-US` 可获取美国出口节点。**
    </Info>

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/gologin2.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=479293b8cef9372fe5398b2b9e56bb55" alt="" width="687" height="633" data-path="images/integrations/gologin2.png" />
    </Frame>
  </Step>

  <Step title="测试代理">
    点击 **检查代理** 以确保一切正常运行。
  </Step>

  <Step title="保存并启动">
    点击 **创建配置文件** 以保存您的设置，然后点击 **运行** 以打开您的新配置文件，享受安全浏览体验。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/gologin3.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=2e97778a303f6f15fa530470c58c8cfd" alt="" width="640" height="109" data-path="images/integrations/gologin3.png" />
    </Frame>
  </Step>
</Steps>

**就是这样！** 您现已成功将 Bright Data 代理集成到 GoLogin 中。
