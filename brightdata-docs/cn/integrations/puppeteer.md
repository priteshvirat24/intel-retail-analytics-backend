> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 Puppeteer 中设置 Bright Data

> 了解如何使用 Bright Data 增强 Puppeteer 的浏览器自动化功能。本指南将引导您设置安全、匿名的代理，以实现更顺畅的网页抓取和数据获取。

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

## 什么是 Puppeteer？

可以将 Puppeteer 看作是无头浏览器的遥控器。只需几行 Node.js 代码，您就可以让浏览器收集信息、运行测试并自动化日常操作。它的核心目标是将复杂、耗时的工作流程变成简单、易管理的步骤。

<Tip>
  通过在用户名中使用 `-session` 参数，您可以在整个浏览器会话中保持一致的 IP。这很重要，因为 Bright Data 代理默认在每个请求中轮换 IP。[了解更多](/cn/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session)

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

## 如何将 Bright Data 集成到 Puppeteer 中

### 开始之前

在集成 Bright Data 之前，请准备好以下内容：

1. **Node.js**：从 [nodejs.org](https://nodejs.org/) 安装最新版本。

2. **项目设置**：使用您喜欢的代码编辑器（如 VS Code），初始化一个 Node.js 项目。

3. **Puppeteer**：在项目中安装 Puppeteer：

```bash theme={null}
npm install puppeteer
```

### 获取您的 Bright Data 凭证

登录到您的 [Bright Data 控制面板](https://www.bright.cn/cp/zones/page/plans)，并记录以下代理信息：

* **Host**
* **Port**
* **Username**
* **Password**

这些凭证将允许 Puppeteer 通过 Bright Data 的安全匿名代理网络传输流量。

### 为 Bright Data 配置 Puppeteer

<Note>
  如果您希望在 Puppeteer 中使用 Bright Data 的 Browser API，请参阅 [Browser API 文档](/cn/scraping-automation/scraping-browser/introduction) 获取正确的设置和代码示例。以下指南适用于直接代理集成，不适用于 Browser API。
</Note>

要将 Puppeteer 与 Bright Data 连接：

1. **设置代理服务器**：将 `--proxy-server=[HOST]:[PORT]` 添加到 Puppeteer 的启动参数中。

2. **身份验证**：使用 Puppeteer 的 `page.authenticate()` 提供 Bright Data 的 **username** 和 **password**。

### 示例代码

以下是示例脚本，可供参考：

```javascript theme={null}
const puppeteer = require('puppeteer');

(async () => {
  // 使用 Bright Data 代理配置启动 Chromium
  const browser = await puppeteer.launch({
    headless: false,  // 如果您想使用无头模式，将其改为 true
    args: ['--proxy-server=[HOST]:[PORT]'] // 将此处替换为 Bright Data 的 host 和 port
  });

  const page = await browser.newPage();

  // 使用 Bright Data 凭证登录
  await page.authenticate({
    username: '[USERNAME]',   // 替换为您的 Bright Data 用户名
    password: '[PASSWORD]'    // 替换为您的 Bright Data 密码
  });

  // 通过访问 IP 检查网站测试代理设置
  await page.goto('http://httpbin.org/ip');
  // 截图以确认设置生效
  await page.screenshot({path: 'example.png'});

  await browser.close();
})();
```

将 Bright Data 代理集成到 Puppeteer 后，您可以在所有自动化任务中获得安全和私密的浏览体验。享受更平滑的数据采集、更低的被检测风险，以及更可靠的工作流程——让您专注于洞察和结果，而不是技术障碍。
