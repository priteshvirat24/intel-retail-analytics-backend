> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何将 Bright Data 与 Sphere 浏览器集成

> 将 Bright Data 与 Sphere 浏览器集成，以安全且匿名地管理多个账户。按照此逐步指南进行无缝配置。

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

## 什么是 Sphere 浏览器?

**Sphere 浏览器** 是一款防检测浏览器，旨在管理多个账户而不被检测。它允许用户创建具有独立指纹的唯一浏览器配置文件，是营销专业人士、电商运营和隐私爱好者的理想工具。将 Bright Data 与 Sphere 浏览器集成可增强匿名性，并解锁地理定位功能。

<Tip>
  使用用户名中的 `-session` 参数可在整个浏览器会话中保持一致的 IP。这一点非常重要，因为 BrightData 代理默认每次请求都会更换 IP。[了解更多](/cn/proxy-networks/faqs#如何长时间使用相同-ip) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

<Warning>
  不支持通过数据中心和 ISP 代理网络连接社交网络，包括：Facebook、TikTok、Instagram、X（Twitter）、LinkedIn、YouTube、Reddit、Pinterest、Snapchat 和 Discord。
</Warning>

## 如何将 Bright Data 与 Sphere 浏览器集成

**步骤 1. 下载并安装 Sphere 浏览器**

1. 访问 [Sphere 浏览器官网](https://linkensphere.info/en/#) 并下载应用程序。
2. 在设备上安装软件，并使用账户凭据登录。
3. 打开 Sphere 浏览器并点击 **Proxy** 开始配置设置。

<Frame as="div">
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/sphere-browser1.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=d385277e6efd50fb662c50a8c45b01de" alt="" width="1595" height="164" data-path="images/integrations/sphere-browser1.png" />
</Frame>

**步骤 2. 配置代理设置**

1. 在创建配置文件窗口中，在 **Profile Name** 字段中提供唯一且描述性的名称，以便轻松识别浏览器实例。
2. 前往您的 [Bright Data 仪表板](https://www.bright.cn/cp/zones)
3. 在 **Overview** 标签的 **Access Details** 部分，使用文本编辑器生成连接字符串，格式如下：`` host:port:username:password` ``
4. 返回 Sphere 浏览器，将凭据粘贴到相应字段中。
5. 点击 **Create** 按钮（带勾选图标）保存代理设置。

<Note>
  对于地理定位代理，将用户名格式化为 `your-username-country-XX`（例如 `your-username-country-US`）以选择特定位置。
</Note>

**步骤 3. 启动并验证**

1. 找到刚配置的配置文件。
2. 点击 **Check Proxy** 确保连接成功。

<Frame as="div">
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/sphere-browser2.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=1ef7c8e98995b3a126dc1ef0c39282e8" alt="" width="1278" height="209" data-path="images/integrations/sphere-browser2.png" />
</Frame>

将 Bright Data 与 Sphere 浏览器集成，可确保安全且匿名的浏览体验，满足您的需求。无论是管理多个账户还是访问地理限制内容，此配置都能提供所需的隐私性和灵活性。立即开始利用 Bright Data 和 Sphere 浏览器的强大功能吧！
