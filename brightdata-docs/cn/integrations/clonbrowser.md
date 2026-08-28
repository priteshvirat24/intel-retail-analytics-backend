> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何将 Bright Data 集成到 ClonBrowser

> 使用 Bright Data 在 ClonBrowser 上保护您的浏览和自动化工作流。本指南将引导您完成设置过程，确保您的浏览既私密又流畅。

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

## 什么是 ClonBrowser？

**ClonBrowser** 是一款专为隐私保护用户、营销人员和自动化专家设计的多账户浏览器。它允许您管理多个浏览器配置文件，同时保持匿名，非常适合用于广告投放、数据抓取等在线任务。

<Tip>
  在浏览会话期间保持一致的 IP，请在用户名中使用 `-session` 参数。这一点非常重要，因为 Bright Data 代理默认会在每个请求后轮换 IP。[了解更多](/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

<Warning>
  不支持通过数据中心和 ISP 代理网络连接社交网络，包括：Facebook、TikTok、Instagram、X（Twitter）、LinkedIn、YouTube、Reddit、Pinterest、Snapchat 和 Discord。
</Warning>

## 如何将 Bright Data 集成到 ClonBrowser

### **步骤 1. 下载并安装 ClonBrowser**

1. 访问 [ClonBrowser 官网](https://www.clonbrowser.com/)，根据您的操作系统下载应用程序。
2. 安装应用程序，并使用您的账户凭据登录。

### **步骤 2. 设置新的浏览器配置文件**

1. 进入 **代理** 选项卡，找到配置文件管理部分。
2. 点击 **新建** 来创建新的浏览器配置文件。

<Frame as="div">
  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/clonbrowser1.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=ed40825101578866106191ee5d3dbf9e" alt="" width="913" height="276" data-path="images/integrations/clonbrowser1.png" />
</Frame>

### **步骤 3. 配置代理详情**

1. 访问您的 [Bright Data 控制面板](https://www.bright.cn/cp/zones)
2. 创建一个 `:` 分隔的代理字符串，格式如下：`Proxy Host:Proxy Port:Proxy Zone username:Proxy Zone password`
3. 将该代理字符串粘贴到 ClonBrowser 指定的代理字段中。
4. 点击 **解析**（Parse），自动填充必填字段（主机、端口、用户名、密码）。
5. 点击 **连接测试**（Connect Test）以确保代理连接正常。
6. 连接成功后，点击 **保存**（Save）以应用代理设置。

<Note>
  如果使用地理定向代理，请在用户名中包含国家代码（例如：`your-username-country-US`），以便访问指定地区的代理。
</Note>

### **步骤 4. 完成设置并开始浏览**

1. 返回 **代理** 选项卡，找到您刚刚配置的代理配置文件。
2. 点击 **Ping** 以确保代理正常运行。

<Frame as="div">
  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/clonbrowser2.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=ab484587de6b8ec6b1d9e8397544631b" alt="" width="1892" height="222" data-path="images/integrations/clonbrowser2.png" />
</Frame>

按照上述步骤，您可以轻松地将 Bright Data 与 ClonBrowser 集成，确保安全、高效的浏览体验，满足您的各种需求。
