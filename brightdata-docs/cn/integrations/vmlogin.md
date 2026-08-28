> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何使用 VMLogin 设置 Bright Data

> 将 Bright Data 与 VMLogin 集成可确保安全匿名浏览和高效的多账户管理，降低被检测和 IP 封禁的风险。

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

## 什么是 VMLogin?

VMLogin 是一款强大的防检测浏览器，帮助您安全地管理多个在线账户而无需担心被检测。通过创建具有独特数字指纹的虚拟浏览器配置文件，VMLogin 确保每个配置文件被网站视为独立、无关联的用户。

VMLogin 非常适合需要高匿名性和灵活性的行业，如社交媒体管理、电商和网页抓取。凭借强大的防检测功能和用户友好的工具，它是团队或个人用户进行安全、高效账户管理的优秀选择。

<Tip>
  使用用户名中的 `-session` 参数可在整个浏览器会话中保持一致的 IP。这一点非常重要，因为 BrightData 代理默认每次请求都会更换 IP。[了解更多](/cn/proxy-networks/faqs#如何长时间使用相同-ip) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

## VMLogin 代理集成

按照以下步骤在 VMLogin 中设置 Bright Data 代理：

**步骤 1. 安装 VMLogin**\
下载并安装 [VMLogin](https://www.vmlogin.us/download.html)。启动应用程序并登录您的账户。

**步骤 2. 创建新浏览器配置文件**\
在主菜单中，点击 **New browser profile** 按钮以打开设置页面。

<Frame as="div">
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/vmlogin1.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=e43349f255b24958eafc4a6433ed1284" alt="" width="235" height="291" data-path="images/integrations/vmlogin1.png" />
</Frame>

**步骤 3. 设置配置文件**\
在 **Display name** 字段中输入浏览器配置文件名称。然后点击 **Setting proxy server** 按钮配置代理设置。

<Frame as="div">
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/vmlogin2.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=f6ad6138ad0e950b21d84715c588d5e3" alt="" width="992" height="647" data-path="images/integrations/vmlogin2.png" />
</Frame>

**步骤 4. 配置 Bright Data 代理**\
启用 **Proxy server** 开关，并填写 Bright Data 代理信息：

* **Proxy type**：根据代理类型选择 `HTTP`、`HTTPS` 或 `SOCKS5`。
* **IP address**：输入 `http://brd.superproxy.io/`。
* **Port**：使用您在 [Bright Data 仪表板](https://www.bright.cn/cp/zones/page/plans) 中提供的端口号。
* **Username**：输入 Bright Data 代理 `username`。
* **Password**：输入 Bright Data 代理 `password`。

<Info>
  **对于特定国家/地区的代理，可使用格式 `your-username-country-US` 以获取美国出口节点。**
</Info>

**步骤 5. 测试代理**\
点击 **Test Proxy** 测试连接。如果测试成功并显示详细的 IP 信息，点击 **Confirm**。完成代理设置后点击 **Save**。

**步骤 6. 保存配置文件**\
配置代理并设置其他偏好后，点击 **Save profile** 按钮以完成浏览器配置文件的保存。

**完成！** 您已成功将 Bright Data 代理集成到 VMLogin。
