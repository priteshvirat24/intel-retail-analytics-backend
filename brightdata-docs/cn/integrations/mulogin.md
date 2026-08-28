> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 MuLogin 中使用 Bright Data

> 通过集成 Bright Data 代理增强您的 MuLogin 体验。本指南将向您展示如何设置安全、匿名的连接，以实现更好的自动化、数据收集和账户管理。

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

## 什么是 MuLogin？

MuLogin 是一个多账号浏览器管理工具，帮助您在多个在线账户之间进行隔离管理，避免相互干扰。它旨在保护您的隐私、防止检测，并简化您的数字运营。使用 MuLogin，您可以无缝管理多个会话，非常适合电商运营、社交媒体管理以及其他在线项目。

<Tip>
  通过在用户名中使用 `-session` 参数，确保整个浏览会话的 IP 地址保持一致。这一点非常重要，因为 Bright Data 代理默认会在每个请求时更换 IP。[了解更多](/cn/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

## 为什么要在 MuLogin 中集成 Bright Data？

通过在 MuLogin 中使用 Bright Data 代理，您可以：

* **保护您的身份**：隐藏真实 IP，在安全匿名的代理后面进行操作。
* **降低被检测的风险**：分散您的活动，使用多个 IP 地址，减少被封禁的可能性。
* **提高稳定性**：访问特定地区的内容，并在多个会话之间保持稳定连接。

## 如何在 MuLogin 中配置 Bright Data 代理

按照以下步骤在 MuLogin 中设置 Bright Data 代理：

<Steps>
  <Step title="访问 MuLogin 仪表盘">
    1. 访问 [MuLogin](https://www.mulogin.com/) 并登录您的账户。
    2. 登录后，您将看到仪表盘，其中列出了已有的浏览器配置文件（如果有的话）。
  </Step>

  <Step title="创建或编辑浏览器配置文件">
    1. 如果需要新建配置文件，点击 **“快速创建”** 按钮。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/mulogin1.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=2d7dbdc8466dbb50ed4ccc114a9cfbc9" alt="" width="1385" height="375" data-path="images/integrations/mulogin1.png" />
    </Frame>

    2. 如果想修改已有配置文件，选择对应文件，然后点击 **“编辑”**、**“设置”** 或 **齿轮图标**（不同版本 UI 可能略有不同）。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/mulogin2.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=8a5d2851e23c024845c5a1f268551e57" alt="" width="1612" height="242" data-path="images/integrations/mulogin2.png" />
    </Frame>
  </Step>

  <Step title="输入名称并进入代理设置">
    1. 在 **“基本配置”** 页面，找到 **“显示名称”** 字段。
    2. 输入一个便于识别的名称，以便日后管理。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/mulogin3.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=9a14703fb331c7800c76d4442babe4e8" alt="" width="803" height="623" data-path="images/integrations/mulogin3.png" />
    </Frame>

    3. 向下滚动，找到 **“代理设置”** 选项，并点击进入代理配置界面。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/mulogin4.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=41a5830ddfffa848de0858b263d9be27" alt="" width="807" height="621" data-path="images/integrations/mulogin4.png" />
    </Frame>
  </Step>

  <Step title="输入 Bright Data 代理信息">
    1. 进入代理设置界面后，填写以下信息：

       * **协议/类型**：选择 `HTTP`、`HTTPS` 或 `SOCKS5`（根据您在 Bright Data 购买的代理类型）。
             <Frame as="div">
               <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/mulogin5.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=76f23b3a56cae4dd64b10114def091ab" alt="" width="791" height="246" data-path="images/integrations/mulogin5.png" />
             </Frame>

       * **代理地址**：输入 `http://brd.superproxy.io/` 或 Bright Data 提供的地址。

       * **端口号**：填写您在 [Bright Data 仪表盘](https://www.bright.cn/cp/zones) 获取的端口号。

       * **用户名 & 密码**：输入您的 Bright Data 账户信息。

       <Note>如果需要使用特定国家的代理出口，请在用户名中添加 `your-username-country-US`（示例为美国）。</Note>

    2. 输入 Bright Data 代理信息后，点击 **“测试代理”** 或 **“检查网络”** 以确保代理连接正常。

    3. 如果测试通过，点击 **“保存”** 确认设置。
  </Step>

  <Step title="启动浏览器配置文件并验证">
    1. 保存设置后，在 MuLogin 仪表盘中启动该浏览器配置文件。
    2. 进入浏览器后，访问 [httpbin.org/ip](http://httpbin.org/ip) 以确认您的 IP 地址是否已变更为 Bright Data 代理的 IP。
    3. 如果 IP 地址正确匹配，则表示 MuLogin 已成功集成 Bright Data 代理。
  </Step>
</Steps>

至此，您已成功在 **MuLogin** 中配置 **Bright Data** 代理。这将大幅提升您的在线操作能力，让您能够更安全地管理多个账户，减少被检测的风险，并保持流畅、稳定的工作流。
