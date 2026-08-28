> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 Screaming Frog 中设置 Bright Data

> 通过将 Bright Data 与 Screaming Frog 集成，简化您的 SEO 任务。按照此逐步指南设置代理，实现高效且安全的网页抓取。

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

## 什么是 Screaming Frog？

**Screaming Frog SEO Spider** 是一款功能多样的 SEO 工具，适用于 SEO 专业人士和网站管理员。它可以帮助审核网站、识别技术问题，并通过生成可操作的见解来优化性能。将 Screaming Frog 与 **Bright Data** 结合使用，可以进行安全、不受限制且基于地理位置的爬取，确保 SEO 分析顺畅无阻。

## 如何在 Screaming Frog 中设置 Bright Data

**步骤 1. 下载并安装 Screaming Frog**

1. 访问官方 [Screaming Frog 网站](https://www.screamingfrog.co.uk/seo-spider/)。
2. 下载并安装适用于您操作系统的 SEO Spider 工具。
3. 安装完成后，启动应用程序。

**步骤 2. 访问代理设置**

1. 在 Screaming Frog 中，点击顶部菜单的 **File**。
2. 选择 **Settings > Proxy** 打开代理配置窗口。

<Frame as="div">
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/screamingfrog1.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=4bccd791fd603f359db168b51a52ab66" alt="" width="1016" height="713" data-path="images/integrations/screamingfrog1.png" />
</Frame>

**步骤 3. 输入 Bright Data 代理详情**

1. 在 **Proxy** 窗口中，勾选 **Use Proxy Server** 以启用代理。
2. 如有需要，勾选 **Use Proxy Credentials** 并提供您的登录信息。
3. 按以下方式填写所需的代理字段：
   * **Address**：输入 `http://brd.superproxy.io/`。
   * **Port**：输入在您的 [Bright Data 控制面板](https://www.bright.cn/cp/zones/page/plans) 中找到的端口号。
   * **Username**：提供您的 Bright Data 用户名。
   * **Password**：输入您的 Bright Data 密码。
4. 输入所有信息后，点击 **OK and Restart** 保存代理设置。

<Note>
  对于基于地理位置的代理，在用户名后附加国家代码（例如 `your-username-country-US`）即可使用特定出口位置。
</Note>

现在，您的 Bright Data 代理已与 Screaming Frog 集成，可实现更安全、更高效的网页抓取。通过此设置，您可以绕过限制、避免 IP 封锁，并进行基于地理位置的审计，从而轻松提升 SEO 任务效率。
