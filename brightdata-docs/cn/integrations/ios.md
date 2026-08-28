> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 iOS 上使用 Bright Data

> 了解如何在您的 iOS 设备上设置 Bright Data 代理，以享受安全、私密且无限制的浏览体验。本指南将引导您完成整个配置过程，确保连接顺畅可靠。

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

## 为什么在 iOS 上使用 Bright Data？

在 iOS 上设置 Bright Data 代理可以帮助您：

* **保护您的隐私**：隐藏您的真实 IP 地址，更安全地浏览网络。

* **访问受地理限制的内容**：通过不同地区的连接访问各个国家的内容。

* **提高稳定性**：降低被检测的风险，在手机上浏览、购物或管理账户时享受稳定的匿名连接。

## 前置要求

在开始之前，请确保您已经准备好：

1. **Bright Data 代理凭据**：
   * 登录您的 [Bright Data 仪表板](https://www.bright.cn/cp/zones) 并找到您的 Host、Port、Username 和 Password。

2. **运行 iOS 10 或更高版本的 iPhone**：
   * 以下步骤适用于大多数较新的 iOS 版本。

## 为 Wi-Fi 网络配置代理

<Steps>
  <Step title="打开 Wi-Fi 设置">
    1. 在 iPhone 主屏幕上打开 **设置**。
    2. 轻点 **Wi-Fi**，然后选择您连接的网络旁的 **i**（信息）图标。

    <Frame as="div" style={{width:"50%", height:"auto"}}>
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/iphone1.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=6513a41e615963d671f44a3a11aa9a9e" alt="" width="1170" height="1049" data-path="images/integrations/iphone1.png" />

      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/iphone2.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=abd7068fc6d328e3aeebaad536b3c466" alt="" width="1170" height="569" data-path="images/integrations/iphone2.png" />
    </Frame>
  </Step>

  <Step title="将代理设置更改为手动">
    1. 向下滚动，找到 **HTTP 代理**。
    2. 从 **关闭** 或 **自动** 切换到 **手动**。
    3. 切换 **身份验证** 为 *开启*。

    <Frame as="div" style={{width:"50%", height:"auto"}}>
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/iphone3.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=4b83d228831b93fec0fd5afa26026747" alt="" width="1170" height="1043" data-path="images/integrations/iphone3.png" />

      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/iphone4.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=b5a01029deb4913cd6d2f99b817b1e64" alt="" width="1170" height="1168" data-path="images/integrations/iphone4.png" />
    </Frame>
  </Step>

  <Step title="输入 Bright Data 代理凭据">
    1. **服务器**：输入 `http://brd.superproxy.io/`（或您的指定 Host）。
    2. **端口**：使用您的 [Bright Data 仪表板](https://www.bright.cn/cp/zones) 上提供的端口号。
    3. **用户名** 和 **密码**：填写您的 Bright Data 登录凭据。
    4. 确保所有信息正确无误。
    5. 轻点 **保存** 以确认设置。
  </Step>

  <Step title="测试">
    1. 打开 **Safari**，访问 [httpbin.org/ip](http://httpbin.org/ip)。
    2. 检查显示的 IP 是否与 Bright Data 代理 IP 匹配。如果匹配，则说明您的 Wi-Fi 流量现在是安全且私密的。
  </Step>
</Steps>

在 **iOS 设备** 上集成 **Bright Data** 后，您将能够更轻松地访问受地理限制的内容、保护您的身份，并确保更安全、私密的连接。无论您身在何处，都可以享受 Bright Data 提供的自由和安心体验！
