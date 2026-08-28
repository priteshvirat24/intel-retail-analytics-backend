> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何将 Bright Data 与 TexAu 集成

> 通过在 TexAu 上使用 Bright Data 来最大化自动化能力。本指南将逐步引导你配置安全、匿名的代理连接，以简化自动化工作流程。

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

<Warning>
  **账户管理不是 Bright Data 平台支持的使用场景**（自 2026 年 4 月 1 日起生效）。这包括在 TikTok、Instagram 等类似平台上进行账户管理。Bright Data 代理不得用于此类用途。详情请参阅[可接受使用政策](https://brightdata.com/acceptable-use-policy)。
</Warning>

## 什么是 TexAu？

TexAu 是一个增长自动化平台，旨在帮助营销人员和企业扩展他们的潜在客户获取和线上互动能力。通过将 TexAu 的自动化功能与 Bright Data 结合，你可以保护身份、访问地理定向数据，并降低 IP 封禁的风险。

<Tip>
  在浏览器会话期间使用 `-session` 参数可保持一致的 IP。这非常重要，因为 BrightData 代理默认在每次请求时轮换 IP。 [了解更多](/cn/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

## 为什么要在 TexAu 中使用 Bright Data？

* **增强隐私保护**：在自动化任务执行期间保护你的 IP 地址。
* **地理定向数据**：使用特定国家代理访问对应地区的信息。
* **稳定连接**：确保自动化流程顺畅、不间断运行。

## 如何将 Bright Data 与 TexAu 集成

按照以下步骤将 Bright Data 连接到 TexAu：

**步骤 1：登录 TexAu**

1. 访问 [TexAu 官网](https://texau.com/) 并登录你的账号。
2. 进入 **Dashboard（仪表盘）** 查看自动化工具。

**步骤 2：打开代理配置设置**

1. 在仪表盘左侧菜单中进入 **Preferences（偏好设置）**。
2. 选择 **Proxies** 标签进入代理配置页面，并点击 **New Proxy** 开始配置。

<Frame as="div">
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/texau1.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=dfbc4d053fd6b063b4b6d28f79d6aa2e" alt="" width="1918" height="548" data-path="images/integrations/texau1.png" />
</Frame>

**步骤 3：添加 Bright Data 代理信息**

1. 按如下填写代理信息：
   * **Host**：输入 `http://brd.superproxy.io/`
   * **Port**：使用你在 [Bright Data 控制台](https://www.bright.cn/cp/zones/page/plans) 中获得的端口号
   * **Username**：输入你的 Bright Data 用户名
   * **Password**：输入你的 Bright Data 密码

2. 填写完成后，点击 **Test Proxy** 测试连接。

<Note>
  如果使用国家定向代理，请将用户名格式写为：\
  \`your-username-country-XX\`（例如：\`your-username-country-US\`）来选择具体国家。
</Note>

**步骤 4：保存并应用代理**

代理测试成功后，点击 **Save** 保存配置。

通过将 **Bright Data** 与 **TexAu** 集成，你将获得一个安全、高效的自动化体验。无论你是在生成潜在客户、抓取数据，还是管理线上互动，Bright Data 都能确保隐私、稳定性和高性能。立即开始优化你的自动化工作流程吧！
