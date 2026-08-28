> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 Proxifier 中配置 Bright Data

> 使用 Proxifier 简化网络管理！通过集成 Bright Data，您可以安全地为缺少原生代理支持的应用程序路由流量。借助 Proxifier 灵活的规则系统，您可以自定义流量路由，享受无缝、匿名的浏览体验。

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

## 什么是 Proxifier?

**Proxifier** 是一款功能强大的桌面应用程序，允许不支持代理的程序通过 HTTPS、HTTP 或 SOCKS5 代理连接。它非常适合安全路由流量、管理特定应用程序的连接，并为 VPN 提供替代方案。基于规则的设置让您可以为特定应用分配代理，从而精确控制互联网使用。

## 如何在 Proxifier 中集成 Bright Data

**步骤 1. 下载并安装 Proxifier**

1. 访问 [Proxifier 官网](https://www.proxifier.com/download/) 下载应用程序。
2. 按照安装说明操作，并在系统中启动 Proxifier。

**步骤 2. 访问代理设置**

1. 打开 Proxifier，导航到 **Profile** 菜单。
2. 选择 **Proxy Servers** 管理代理配置。

<Frame>
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/proxifier1.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=78faf92ef402b9cb91e9d559446eeea3" alt="" width="1270" height="530" data-path="images/integrations/proxifier1.png" />
</Frame>

**步骤 3. 添加 Bright Data 代理**

1. 点击 **Add** 按钮配置新代理。

<Frame>
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/proxifier2.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=88d9f77328d89fdeefadff1983291749" alt="" width="445" height="289" data-path="images/integrations/proxifier2.png" />
</Frame>

2. 在 **Proxy Server** 对话框中输入以下信息：

* **Type**：选择 HTTP、HTTPS 或 SOCKS5。
* **Address**：`http://brd.superproxy.io/`。
* **Port**：输入来自 [Bright Data 仪表板](https://www.bright.cn/cp/zones/page/plans) 的端口号。
* 启用 **Authentication** 并提供：
  * **Username**：您的 Bright Data 用户名。
  * **Password**：您的 Bright Data 密码。

3. 点击 **OK** 保存设置。代理现在将显示在列表中。

<Note>
  **`对于地理定位代理，请在用户名中包含国家代码（例如 your-username-country-US 表示美国节点）。`**
</Note>

**步骤 4. 测试代理连接**

1. 在 **Proxy Servers** 部分，选择已配置的代理。
2. 点击 **Check**，然后 **Start Testing**。确保测试成功后再继续。

<Frame>
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/proxifier3.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=cb0e9040f34b2f440dc43614bfac402a" alt="" width="446" height="288" data-path="images/integrations/proxifier3.png" />
</Frame>

**步骤 5. 为应用创建代理规则**

1. 转到 **Profile** > **Proxification Rules**。

<Frame>
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/proxifier4.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=6c5f67c7c655c980087624b9df6227ee" alt="" width="1270" height="529" data-path="images/integrations/proxifier4.png" />
</Frame>

2. 点击 **Add** 设置新规则。

<Frame>
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/proxifier5.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=be294bfe9e40ffee28963125ba60f137" alt="" width="716" height="428" data-path="images/integrations/proxifier5.png" />
</Frame>

3. 给规则命名以便清晰识别。

<Frame>
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/proxifier6.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=6cc0536340c17eb7e53ab5fad6cf7ca0" alt="" width="479" height="534" data-path="images/integrations/proxifier6.png" />
</Frame>

4. 使用 **Browse** 按钮指定应用程序（如 Chrome、Firefox）。

<Frame>
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/proxifier7.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=6eb19d80d5af07dd923fa7db193d361d" alt="" width="844" height="305" data-path="images/integrations/proxifier7.png" />
</Frame>

5. 选择流量路由方式：

* 通过代理。
* 直接连接互联网。
* 完全阻止。

<Frame>
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/proxifier8.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=fd350c55ddbf40e7686a8868fd76042a" alt="" width="480" height="534" data-path="images/integrations/proxifier8.png" />
</Frame>

6. 保存规则并将其移至列表顶部以优先执行。

<Frame>
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/proxifier9.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=0e2e01509225accaa589903f98b0b09c" alt="" width="718" height="429" data-path="images/integrations/proxifier9.png" />
</Frame>

**步骤 6. 验证并开始浏览**

1. 启动与规则关联的应用程序。
2. 访问 IP 检查网站（如 [httpbin.org/ip](http://httpbin.org/ip)）确认代理已激活。

使用 **Bright Data** 配置 Proxifier 后，您可以精确管理网络流量，通过安全代理路由应用程序，并确保复杂工作流程的隐私。无论是追求匿名、快速连接还是应用程序特定路由，这套配置都能让您轻松掌控互联网体验。

## 为什么使用 Proxifier 和 Bright Data 时会出现错误的地理位置或被阻止？

Proxifier 允许您控制运行中的应用程序，并选择性地通过 Bright Data 代理路由流量。如果应用尝试访问的是 IP 地址而非域名，Bright Data 可能会阻止请求或通过我们的 Superproxy 服务器路由，而非通过代理节点。\
这意味着目标域将看到请求来自 Bright Data 服务器，而非您分配的代理，从而可能被阻止。

由于合规性规定，Bright Data 不允许针对 IP 地址进行访问。
