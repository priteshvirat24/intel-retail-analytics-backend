> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 Windows 上设置 Bright Data

> 通过代理优化你的在线体验！无论是访问地理受限内容、保护隐私还是保障设备安全，这些工具都能帮助你优化浏览体验。本指南将逐步演示如何在 Windows 10 和 11 上设置 Bright Data 代理服务器。

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

<Tip>
  在整个会话期间保持一致的 IP 地址，请在用户名中使用 `-session` 参数。由于 BrightData 代理默认每次请求都会旋转 IP，这一点至关重要。[了解更多](/cn/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

## 在 Windows 上设置代理

在 Windows 10 和 11 上，设置代理的步骤几乎相同。按照以下步骤快速配置：

**步骤 1. 打开网络与 Internet 设置**\
按 **Windows + I** 打开 **设置**，然后进入 **网络和 Internet**。

<Frame as="div">
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/windows1.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=10ee3b06b6304857e1fc7198d749fe6b" alt="" width="1920" height="1020" data-path="images/integrations/windows1.png" />
</Frame>

**步骤 2. 启用自动检测**\
从侧边栏选择 **代理**。在 **自动代理设置** 下，将 **自动检测设置** 切换为 *开启*。

<Frame as="div">
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/windows2.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=724186d91eac36e09ccc2b4c7b472eb5" alt="" width="1920" height="1020" data-path="images/integrations/windows2.png" />
</Frame>

**步骤 3. 设置手动代理**\
滚动到 **手动代理设置**，将 **使用代理服务器** 切换为 *开启*，并填写以下信息：

* **地址**：输入 `http://brd.superproxy.io/`
* **端口**：使用你的 [Bright Data 仪表板](https://www.bright.cn/cp/zones/page/plans) 中提供的端口号

完成后点击 **保存** 确认更改。

<Note>
  Windows 不允许直接在代理设置中保存用户名和密码。别担心！当应用程序或浏览器请求凭证时，直接输入你的 Bright Data **用户名** 和 **密码** 即可。例如，在浏览时弹出窗口出现时，填写信息即可安全继续。
</Note>

设置完成！你的 Windows 设备已配置 Bright Data，提供额外的隐私保护、便捷访问以及更安全的浏览体验。无论是办公、观看流媒体还是日常浏览，你都准备就绪了！
