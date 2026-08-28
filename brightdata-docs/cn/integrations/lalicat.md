> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 Lalicat 中设置 Bright Data

> 将 Bright Data 集成到 Lalicat 可确保安全、匿名的多账户管理，提供灵活的代理解决方案，实现可靠高效的浏览体验。

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

## 什么是 Lalicat？

Lalicat 是一款简单的防检测浏览器，旨在帮助您安全、匿名地管理多个账户。它创建独立的浏览器配置文件，并隔离数字指纹（如 IP 地址和设备信息），让您轻松绕过跟踪系统，避免检测。

无论是社交媒体管理、电商运营，还是 Web 数据抓取，Lalicat 都是一个可靠且经济的解决方案，适合注重隐私和效率的专业人士。对于需要同时管理多个账户而不被标记或封禁的用户来说，它是完美的选择。

<Tip>
  在整个浏览器会话期间保持 IP 一致，请在用户名中使用 `-session` 参数。这一点至关重要，因为 Bright Data 代理默认会在每次请求时更换 IP。[了解更多](/cn/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

## Lalicat 代理集成

按照以下步骤将 Bright Data 代理集成到 Lalicat：

<Steps>
  <Step title="安装 Lalicat">
    1. [**下载**](https://www.lalicat.com/download)、安装并启动 Lalicat。
    2. 创建账户并登录。
  </Step>

  <Step title="添加浏览器配置文件">
    在主界面点击 **+添加浏览器** 以创建新的浏览器实例。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/lalicat1.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=61fb5af29351a62b2c74a438dd2a0867" alt="" width="1534" height="364" data-path="images/integrations/lalicat1.png" />
    </Frame>
  </Step>

  <Step title="配置基本设置">
    在 **基本配置** 部分，输入 **配置文件名称**，选择模拟的 **操作系统**，并调整其他必要的设置。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/lalicat2.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=7c8fc63bc9dd44de0a4cbb58ad9a1e2b" alt="" width="715" height="611" data-path="images/integrations/lalicat2.png" />
    </Frame>
  </Step>

  <Step title="配置 Bright Data 代理">
    滚动至 **代理设置** 部分，并输入以下信息：

    * **代理类型**: 选择 `HTTP`、`HTTPS` 或 `SOCKS5`（根据您的代理类型）。
    * **IP 地址**: 输入 `http://brd.superproxy.io/`。
    * **端口**: 使用您的 [Bright Data 控制面板](https://www.bright.cn/cp/zones) 提供的端口号。
    * **登录名**: 输入您的 Bright Data 代理 `用户名`。
    * **密码**: 输入您的 Bright Data 代理 `密码`。

    <Info>
      **针对特定国家/地区的代理，您可以使用格式 `your-username-country-US` 以获得美国出口节点。**
    </Info>
  </Step>

  <Step title="测试代理">
    点击 **检查代理** 以验证连接是否成功。

    如果一切正常，点击 **保存** 完成配置。
  </Step>
</Steps>

**就这样！** 您已成功将 Bright Data 代理集成到 Lalicat。
