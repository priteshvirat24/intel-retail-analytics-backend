> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 Playwright 中设置 Bright Data

> 使用 Bright Data 和 Playwright 简化您的网页自动化流程。本指南将向您展示如何配置安全、匿名的代理，以降低检测风险并确保任务顺利运行。

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

## 什么是 Playwright？

Playwright 是一个强大的 Node.js 工具包，可用于一次性自动化多个主流浏览器。无论您是在抓取数据、测试应用程序，还是构建无缝的自动化流程，Playwright 的统一接口和强大功能都能帮助您在不影响质量的情况下更快完成任务。

<Tip>
  通过在用户名中使用 `-session` 参数，确保整个浏览器会话保持相同的 IP 地址。这一点很重要，因为 Bright Data 代理默认会在每个请求之间更换 IP。[了解更多](/cn/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session)

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

## 如何集成 Bright Data 与 Playwright

### 前提条件

1. **Node.js**：从 [nodejs.org](https://nodejs.org/) 下载并安装最新版本。

2. **Playwright 包**：在您的项目中添加 Playwright：

```bash theme={null}
npm install playwright
```

### 获取您的 Bright Data 凭据

登录您的 [Bright Data 控制面板](https://www.bright.cn/cp/zones/page/plans)，并获取以下信息：

* **主机 (Host)**：`http://brd.superproxy.io/`
* **端口 (Port)**：`44445`
* **用户名 (Username)**：输入您的 Bright Data `username`。
* **密码 (Password)**：输入您的 Bright Data `password`。

您需要这些信息进行代理身份验证。

### 配置 Playwright 以使用 Bright Data

<Note>
  如果您希望在 Bright Data 的浏览器 API 中使用 Playwright，请参阅 [浏览器 API 文档](/cn/scraping-automation/scraping-browser/introduction)，以获取正确的设置方法和代码示例。以下的代理集成指南适用于直接代理集成，而非浏览器 API。
</Note>

1. **设置代理服务器**：在浏览器启动选项中包含您的 Bright Data 主机和端口。格式为 `host:port`。
2. **添加身份验证**：提供您的 Bright Data **`username`** 和 **`password`** 以确保安全访问。

### 忽略 SSL 错误

如果您在使用我们的住宅代理或 Web Unlocker API 时遇到 SSL 错误，请在您的 JS 代码中设置：`ignoreHTTPSErrors: True`。或者，您也可以在系统上安装我们的证书，或将其导入到代码中。有关更多访问信息，请参阅 [此处](/cn/integrations/playwright#展开以获取您的-bright-data-代理访问信息)。

### 示例代码

使用以下示例代码开始：

```javascript theme={null}
const { chromium } = require('playwright');

(async () => {
  // 使用代理设置启动浏览器
  const browser = await chromium.launch({
    headless: false,  // 设置为 true 以启用无头模式
    proxy: {
      server: 'http://[HOST]:[PORT]',  // 替换为您的代理主机和端口
      username: '[USERNAME]',        // 替换为您的代理 `username`
      password: '[PASSWORD]'         // 替换为您的代理 `password`
    }
  });

  const context = await browser.newContext();
  const page = await context.newPage();

  // 访问 IP 验证网站以测试代理
  await page.goto('http://httpbin.org/ip');
  // 截取屏幕截图以验证设置
  await page.screenshot({ path: 'example.png' });

  await browser.close();
})();
```

通过将 **Bright Data** 集成到 **Playwright**，您的自动化流程将更加安全且隐蔽。享受更快的工作流、降低检测风险，并在抓取、测试和自动化任务时更加安心。
