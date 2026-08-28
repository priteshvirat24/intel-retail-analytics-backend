> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何使用 Postern 设置 Bright Data

> 将 Bright Data 与 Postern 集成，以轻松管理您的代理配置。按照本指南安全配置代理，实现高效、无缝的浏览体验。

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

## 什么是 Postern？

Postern 是一款 Android 代理管理工具，允许用户通过代理路由应用流量，实现安全和私密的连接。它支持 HTTP、HTTPS 和 SOCKS5 代理，是管理网络连接和优化工作流程的多功能工具。

## 如何使用 Postern 设置 Bright Data

<Steps>
  <Step title="下载并安装 Postern">
    1. 在 Google Play 商店中搜索 Postern，并在您的 Android 设备上安装该应用。
    2. 打开应用并允许所有必需的权限。
  </Step>

  <Step title="配置代理设置">
    1. 打开 Postern，点击 **Add Proxy** 以开始配置新代理。

    <Frame as="div" style={{width:"50%", height:"auto"}}>
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/postern1.jpg?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=c9d7b9e1d4f6379fcc519dc36b88e09e" alt="" width="1080" height="583" data-path="images/integrations/postern1.jpg" />
    </Frame>

    2. 填写您的 Bright Data 代理详细信息：
       * **服务器名称**：输入一个描述性名称（例如 "Bright Data Proxy"）。
       * **服务器地址**：`http://brd.superproxy.io/`。
       * **服务器端口**：使用您的 [Bright Data 控制面板](https://www.bright.cn/cn/cp/zones/page/plans) 中提供的端口号。
       * **服务器类型**：根据您的代理类型选择 HTTP、HTTPS 或 SOCKS5。
       * **用户名**：输入您的 Bright Data `username`。
       * **密码**：输入您的 Bright Data `password`。

    3. 点击 **Save** 保存代理配置。
  </Step>

  <Step title="配置规则以启用代理">
    1. 进入应用菜单，导航到 **Rules**。

    <Frame as="div" style={{width:"50%", height:"auto"}}>
      <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/postern2.jpg?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=ea7476fa06c799592830c5399ab51bd5" alt="" width="1080" height="1378" data-path="images/integrations/postern2.jpg" />
    </Frame>

    2. 点击 **Add Rule** 以创建新的代理规则。

    <Frame as="div" style={{width:"50%", height:"auto"}}>
      <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/postern3.jpg?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=c15c2c4eb371e0937242ea6ce236eb08" alt="" width="1080" height="735" data-path="images/integrations/postern3.jpg" />
    </Frame>

    3. 进行以下设置：

    * **匹配方法**：选择 **Match All** 以将所有流量路由至代理。
    * **规则类型**：选择 **Proxy/Tunnel**。
    * **代理/代理组**：确保已选择您配置的代理（例如 `http://brd.superproxy.io/:port`）。

    4. 点击 **Save** 以完成规则配置。
  </Step>

  <Step title="激活代理">
    1. 打开应用菜单，切换 **VPN Off** 以启用连接。
    2. 启用后，所有流量将通过您的 Bright Data 代理进行路由。

    <Frame as="div" style={{width:"50%", height:"auto"}}>
      <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/postern4.jpg?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=37c83f77f0c68d82e047fbc0f4d66efe" alt="" width="1080" height="1412" data-path="images/integrations/postern4.jpg" />
    </Frame>

    <Note>
      对于地理定位代理，请更新您的用户名格式以包含国家代码（例如 `your-username-country-US`），以便路由至特定位置。
    </Note>
  </Step>
</Steps>

现在，Bright Data 已成功配置到 Postern，您的应用流量将安全、匿名地传输。无论是个人使用还是业务场景，这种设置都能确保隐私和无缝连接。
