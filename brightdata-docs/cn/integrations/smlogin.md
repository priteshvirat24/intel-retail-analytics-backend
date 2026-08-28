> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何使用 SMLogin 设置 Bright Data

> 在 SMLogin 中配置 Bright Data 代理，实现安全的多账户管理和匿名浏览，覆盖 195 个以上国家和地区。

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

## 什么是 SMLogin?

SMLOGIN 是一款先进的反关联指纹浏览器，为需要高效管理多个账户的用户提供了强大的解决方案。通过模拟真实设备并提供多账户/多平台安全操作环境，SMLOGIN 以易用性、低资源消耗和全面的安全功能而脱颖而出。

将 SMLOGIN 与 Bright Data 的代理结合使用，可进一步增强这些优势，为用户的在线操作提供无与伦比的匿名性、安全性和灵活性。

<Tip>
  使用用户名中的 `-session` 参数可在整个浏览器会话中保持一致的 IP。这一点非常重要，因为 BrightData 代理默认每次请求都会更换 IP。[了解更多](/cn/proxy-networks/faqs#如何长时间使用相同-ip) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

## 使用 Bright Data 代理的优势

SMLOGIN 与 [Bright Data 代理服务](https://www.bright.cn/proxy-types) 的结合，为管理众多账户的数字营销人员、电商运营者和数据分析师提供了无与伦比的解决方案。原因如下：

* **全球网络无与伦比**：Bright Data 提供每月 4 亿+ 个 [真实住宅 IP](https://www.bright.cn/proxy-types/residential-proxies)，覆盖 195+ 国家，包括数据中心、住宅区域和移动网络。此广泛选择确保 SMLOGIN 用户能够从任何地理位置顺利管理账户，对于需要特定区域访问的任务至关重要。
* **卓越的匿名性和安全性**：操作多个账户需要高水平的匿名性以防止检测和潜在封禁。Bright Data 的代理提供强大的安全功能，保护用户的数字足迹，确保每次 SMLOGIN 会话都保持不可被追踪和安全。
* **高速性能**：在当今快节奏的数字环境中，速度至关重要。Bright Data 高效的代理服务器保证了最小的延迟和快速加载时间，提升 SMLOGIN 的性能，使多账户操作更高效。
* **成本效益与资源高效**：与云服务器和虚拟机相关的高成本相比，Bright Data 代理解决方案提供了更经济、更高效的多账户管理方式。这对于利用 SMLOGIN 进行大规模电商运营和社交媒体活动的用户尤为有利。
* **灵活且可扩展的解决方案**：Bright Data 的代理服务设计高度灵活，满足从网页抓取、竞争分析到社交媒体管理和电商运营的 [多种用例](https://www.bright.cn/use-cases)。无论您管理的是少量账户还是成千上万的账户，Bright Data 的基础设施都能扩展以满足需求，同时保持质量和安全。
* **易于集成和全面支持**：将 Bright Data 代理与 SMLOGIN 集成非常简单，确保用户可以快速设置并开始管理账户，同时提升匿名性和效率。此外，Bright Data 提供丰富的文档和专门支持，帮助用户最大化使用 SMLOGIN 代理以获得最佳效果。

通过将 SMLOGIN 与 Bright Data 的代理解决方案结合，用户可以获得多账户管理的强大组合，同时享受无与伦比的安全性、全球覆盖和操作效率。

## SMLOGIN 代理集成

按照此逐步指南，可在几分钟内将我们的代理服务与 SMLOGIN 集成。

<Frame caption="带有高亮下载按钮的软件下载页面">
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/smlogin19.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=60875b3f919b808984763f2c055df308" alt="smlogin19.png" width="1999" height="1250" data-path="images/integrations/smlogin19.png" />
</Frame>

### 注册并下载 SMLOGIN

首先在 [SMLOGIN 注册页面](https://sys.smlogin.cc/#/passport/register) 注册账户。

从 SMLOGIN Downloads 下载兼容 Windows 7 及以上的 SMLOGIN 应用程序。

<Frame caption="带有邮箱和密码字段的登录页面">
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/smlogin17.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=cd491633a8f1b4bf02a62d8c49fc624b" alt="smlogin17.png" width="1366" height="768" data-path="images/integrations/smlogin17.png" />
</Frame>

### 安装和账户登录

按照屏幕上的说明安装 SMLOGIN 应用程序。

启动 SMLOGIN 并使用您的凭据登录账户。

<Frame caption="显示 SMLogin 界面和选项的浏览器窗口">
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/smlogin11.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=8d018deeb867ca04e80966b256ddb5e6" alt="smlogin11.png" width="1366" height="768" data-path="images/integrations/smlogin11.png" />
</Frame>

### 创建新配置文件

在 SMLOGIN 仪表板中，点击“+ 一键新建配置文件”按钮创建新的浏览器配置文件。

<Frame caption="在应用界面创建新配置文件">
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/smlogin13.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=45b2b7ed56ac7d5c1645e6606a9a02ce" alt="smlogin13.png" width="1366" height="768" data-path="images/integrations/smlogin13.png" />
</Frame>

### 设置配置文件

根据您的偏好自定义新配置文件，包括设置浏览器指纹、屏幕分辨率及其他与浏览或操作相关的设置。

<Frame caption="浏览器配置文件管理界面">
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/smlogin22.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=9568ee5f071a2d60c1cbc0e7116002cd" alt="smlogin22.png" width="1366" height="768" data-path="images/integrations/smlogin22.png" />
</Frame>

### 为配置文件绑定 IP

配置文件设置完成后，它将显示在仪表板上。在新创建的配置文件旁找到并点击“绑定 IP”选项，以配置代理设置。

<Frame caption="显示代理 IP 配置选项的软件界面">
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/smlogin5.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=b59b4655e2b1e33722ffb5ebd4efa45e" alt="smlogin5.png" width="1366" height="768" data-path="images/integrations/smlogin5.png" />
</Frame>

### 配置代理

从“代理类型”下拉菜单中选择“HTTP”以使用默认 Bright Data 代理。如果使用 Bright Data 的住宅代理，也可以从下拉列表中选择“Luminati (Residential)”。

<Frame caption="代理设置: IP brd.superproxy.io, 端口 44445">
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/smlogin6.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=d42db116c74b0cd40e7065d71d07a911" alt="smlogin6.png" width="1366" height="768" data-path="images/integrations/smlogin6.png" />
</Frame>

### 输入代理详细信息

填写代理详细信息：Host、Port、Username 和 Password。

* **Host**: 输入代理服务器地址 brd.superproxy.io
* **Port**: 指定代理端口为 44445
* **Username**: 您的 Bright Data 用户名
* **Password**: 您的 Bright Data 密码

<Frame caption="显示代理 IP 设置和信息的软件界面">
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/smlogin2.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=3e93ff6aa65b6fe93ec80d7446f3c882" alt="smlogin2.png" width="1366" height="768" data-path="images/integrations/smlogin2.png" />
</Frame>

### 验证代理连接

点击“检查代理”按钮测试连接。如果设置成功，您将看到代理 IP 和位置信息。

<Frame caption="SMLOGIN 应用程序中的代理 IP 设置窗口">
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/smlogin16.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=109692bcd4874bdd2e8a63a04ef1ab6a" alt="smlogin16.png" width="1366" height="768" data-path="images/integrations/smlogin16.png" />
</Frame>

### 保存代理配置

确认代理信息正确并测试成功后，点击“保存代理”完成配置文件的代理设置。

<Frame>
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/smlogin8.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=5e8952ef14ae6bd46cfb441c6ecb4a36" alt="smlogin8.png" width="1366" height="768" data-path="images/integrations/smlogin8.png" />
</Frame>

### 启动配置文件

点击刚刚配置的配置文件以打开它。现在，您可以使用 Bright Data 代理安全高效地浏览互联网。

<Warning>
  **重要提示**:

  如果您使用 Bright Data 的住宅代理、Web Unlocker API 或 SERP API，则需要安装 SSL 证书，以启用到目标网站的端到端安全连接。

  这是一个简单过程，请参阅 [此指南](/cn/general/account/ssl-certificate#installation-of-the-ssl-certificate) 获取说明。
</Warning>
