> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何将 Bright Data 与 MoreLogin 配置

> 使用 Bright Data 在 MoreLogin 上增强您的多账户管理，实现安全、匿名浏览，并更好地防止检测。

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

## 什么是 MoreLogin？

MoreLogin 是一款强大的工具，可帮助您在单个设备上管理多个在线身份。非常适合隐私保护用户、营销人员和社交媒体管理者，MoreLogin 允许您操作多个独立的浏览器配置文件，每个配置文件都有唯一的 IP、Cookie 和设备指纹，从而降低检测和账号封禁的风险。

MoreLogin 具有无缝的代理集成功能，可进一步提升您的匿名性。此外，它支持配置文件共享，非常适用于社交媒体管理、电商和联盟营销。无论是管理多个账户，还是扩大运营规模，MoreLogin 都能助您安全高效地进行操作。

<Tip>
  通过在用户名中使用 `-session` 参数，保持整个浏览会话期间的 IP 地址一致。这很重要，因为 Bright Data 代理默认会在每次请求时轮换 IP。[了解更多](/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

## MoreLogin 代理集成

以下是如何轻松将 Bright Data 代理与 MoreLogin 集成的方法：

<Steps>
  <Step title="安装 MoreLogin">
    访问 [MoreLogin 官网](https://www.morelogin.com/)，下载并安装应用程序。
  </Step>

  <Step title="创建账户">
    登录并开始进行设置。
  </Step>

  <Step title="创建新配置文件">
    点击 **+New profile** 按钮，填写您的配置文件信息。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/morelogin1.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=49efd4ff85818aa0fc7f286f4869ac92" alt="" width="1440" height="698" data-path="images/integrations/morelogin1.png" />
    </Frame>
  </Step>

  <Step title="设置初始配置文件">
    输入配置文件名称，选择您需要的浏览器指纹，并点击 **Advanced Create** 进入高级设置。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/morelogin2.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=70669aeeca09fd5dcabf2bfeda6851fe" alt="" width="560" height="383" data-path="images/integrations/morelogin2.png" />
    </Frame>
  </Step>

  <Step title="配置代理设置">
    滚动到 **Proxies** 部分，输入您的 Bright Data 代理信息：

    * **代理类型**：选择 `HTTP`、`HTTPS` 或 `SOCKS5`（根据您的代理类型）。
    * **代理服务器**：输入 `http://brd.superproxy.io/`。
    * **代理端口**：使用您在 [Bright Data 控制面板](https://www.bright.cn/cp/zones) 中提供的端口号。
    * **代理账号**：输入您的 Bright Data 代理 `用户名`。
    * **代理密码**：输入您的 Bright Data 代理 `密码`。

    <Info>
      **您还可以为代理指定国家/地区。例如，输入 `your-username-country-US` 将为您提供美国的出口节点。**
    </Info>

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/morelogin3.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=3c5d6a14398da2456cfa97994453d2a2" alt="" width="876" height="815" data-path="images/integrations/morelogin3.png" />
    </Frame>
  </Step>

  <Step title="测试代理">
    点击 **Check Proxy** 确保代理连接正常。
  </Step>

  <Step title="保存并启动">
    点击 **Confirm** 保存设置，然后点击 **Start**，在安全的浏览环境中启动您的配置文件。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/morelogin4.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=8cdcc32f348186127acd7a25685fa318" alt="" width="771" height="131" data-path="images/integrations/morelogin4.png" />
    </Frame>
  </Step>
</Steps>

完成！您已成功将 Bright Data 代理集成到 MoreLogin 中。
