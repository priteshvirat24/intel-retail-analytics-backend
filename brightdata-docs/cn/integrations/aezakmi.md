> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何设置 Bright Data 与 Aezakmi

> 在 Aezakmi 中使用 Bright Data 提升您的匿名性并简化在线任务。按照本指南配置安全可靠的代理连接，为您的浏览器配置文件提供保障。

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

## 什么是 Aezakmi？

Aezakmi 是一款浏览器自动化工具，适用于需要多个独立浏览器配置文件的营销人员、研究人员和开发者。结合 Bright Data，您可以确保安全、匿名，并通过定位代理访问特定地区的内容，同时避免 IP 封禁和追踪。

<Tip>
  通过在用户名中使用 `-session` 参数，在浏览会话期间保持一致的 IP。这一点很重要，因为 Bright Data 代理默认会在每次请求时轮换 IP。[了解更多](/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

## 为什么在 Aezakmi 中使用 Bright Data？

* **增强隐私**：隐藏您的真实 IP 地址，实现安全浏览。

* **地理定位**：使用特定国家的代理访问区域限制的内容。

* **稳定的性能**：确保所有浏览器配置文件都能获得可靠且不中断的连接。

## 如何在 Aezakmi 中集成 Bright Data？

按照以下步骤在 Aezakmi 中配置 Bright Data 代理：

### **步骤 1. 安装并登录 Aezakmi**

1\. 从 [官方网站](https://aezakmi.run/) 下载并安装 Aezakmi。

2\. 打开应用程序，并使用您的账户凭据登录。

### **步骤 2. 创建新的浏览器配置文件**

1\. 进入您的 [仪表板](https://account.aezakmi.run/#/dashboard) 或在 **Aezakmi 扩展** 中点击 **创建新配置文件**。

2\. 选择以下参数来配置您的浏览器配置文件：

* **操作系统**

* **浏览器**

* **屏幕分辨率**

* **显卡型号**

3\. 点击 **生成指纹**，创建一个独特的浏览器指纹配置文件。

<Frame as="div">
  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/aezakmi1.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=0dc409873f10c2c9ceb284a65b887487" alt="" width="1080" height="643" data-path="images/integrations/aezakmi1.png" />
</Frame>

### **步骤 3. 启用代理**

1\. 在配置文件设置页面的 **配置文件名称** 字段中输入一个易于识别的名称。

2\. 切换 **启用代理** 为 *开启*，以激活代理配置选项。

<Frame as="div">
  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/aezakmi2.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=a066ad016ae08424c304d0973a634ec4" alt="" width="1099" height="182" data-path="images/integrations/aezakmi2.png" />
</Frame>

### **步骤 4. 配置代理设置**

1\. 在代理设置部分，输入您的 Bright Data 代理信息：

* **协议**: 选择 `HTTP`、`HTTPS` 或 `SOCKS5`（根据您的代理类型）。

* **地址**: 输入 [`http://brd.superproxy.io/`](http://brd.superproxy.io/)。

* **端口**: `44445`

* **用户名**: 输入您的 Bright Data 代理区域 `username`。

* **密码**: 输入您的 Bright Data 代理区域 `password`。

2\. 点击 **检查代理** 以验证您的连接，并确保测试成功。

<Note>
  对于地理定位代理，在用户名中添加国家代码，格式为 `your-username-country-XX`（例如 `your-username-country-US`）。
</Note>

### **步骤 5. 保存并启动**

* 代理信息验证完成后，点击 **保存指纹** 以应用设置并保存配置文件。

通过将 Bright Data 集成到 Aezakmi，您可以解锁安全高效的浏览体验。无论是管理多个账户、抓取数据，还是访问受地理限制的内容，Bright Data 都能确保隐私、安全性和稳定性。立即开始，最大化您的工作效率！
