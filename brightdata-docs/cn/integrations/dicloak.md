> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何将 Bright Data 与 DICloak 集成

<Warning>
  **账户管理不是 Bright Data 平台支持的使用场景**（自 2026 年 4 月 1 日起生效）。这包括在 TikTok、Instagram 等类似平台上进行账户管理。Bright Data 代理不得用于此类用途。详情请参阅[可接受使用政策](https://brightdata.com/acceptable-use-policy)。
</Warning>

# DICloak 代理集成

DICloak 是一款强大的反指纹浏览器，旨在提供安全匿名的上网体验。它具备动态指纹、配置文件管理和强大的代理支持，是寻求隐私保护和数据采集能力的专业人士的必备工具。

## DICloak 与 Bright Data：安全浏览的强大组合

将 DICloak 与 Bright Data 的代理方案结合，可为注重隐私的专业人士提供卓越体验。Bright Data 在 DICloak 中的优势包括：

* **全球代理覆盖**：访问每月 4 亿+ 住宅 IP，覆盖 195+ 国家，实现区域浏览，是全球最大的代理网络。
* **增强隐私**：通过可靠代理保障安全匿名浏览。
* **绕过地理限制**：轻松访问国际项目中的受限内容。
* **优化速度**：高性能代理确保快速连接。
* **多用途应用**：适用于网页爬取、账户管理等多种场景。

将 DICloak 与 Bright Data 代理服务集成，可确保网页爬取和浏览任务的最佳性能和安全性。本指南将提供逐步操作教程，帮助你无缝集成 Bright Data 与 DICloak。

## 如何将 Bright Data 集成到 DICloak

<Steps>
  <Step title="下载并安装 DICloak">
    1. [下载](https://dicloak.com/download) 适用于你的操作系统的 DICloak 浏览器。

    <Frame>
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/dicloak/download-dicloak.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=baf6e727718f805300324a359daea103" alt="download-dicloak" width="1880" height="863" data-path="images/integrations/dicloak/download-dicloak.png" />
    </Frame>

    2. 安装 DICloak 并启动应用。

    <Frame>
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/dicloak/launch-dicloak.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=e0abebf8db26a6d0a8316912e6ba28ea" alt="launch-dicloak" width="1999" height="1250" data-path="images/integrations/dicloak/launch-dicloak.png" />
    </Frame>
  </Step>

  <Step title="创建新配置文件">
    1. 点击 **+ 创建配置文件** 按钮。

    <Frame>
      <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/dicloak/create-profile.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=ae7dc5314f8acad0aae5ac418655128b" alt="create-profile" width="1785" height="903" data-path="images/integrations/dicloak/create-profile.png" />
    </Frame>

    2. 设置基础配置文件：

    * 输入 **配置文件名称**
    * 选择浏览器和操作系统

    <Frame>
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/dicloak/setup-basic-profile.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=b55efb8f4e07aa9797a97d6ed6c561d6" alt="setup-basic-profile" width="1999" height="1250" data-path="images/integrations/dicloak/setup-basic-profile.png" />
    </Frame>
  </Step>

  <Step title="在 DICloak 中配置代理">
    1. 向下滚动到 **代理** 部分并设置代理详情：

    * 在 **代理类型** 下拉菜单中选择 `HTTP`。

    <Frame>
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/dicloak/proxy-config.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=90d8b5ec4b7150a1c7d9837d0f043d62" alt="proxy-config" width="1999" height="1250" data-path="images/integrations/dicloak/proxy-config.png" />
    </Frame>

    2. 输入以下信息：

       * **Host:** `brd.superproxy.io`
       * **Port:** `44445`
       * **账户名:** 输入你的 Bright Data 用户名
       * **密码:** 输入你的 Bright Data 密码

           <Tip>
             在 [此指南](/cn/integrations/bright-data) 中了解如何找到 Bright Data 用户名和密码。
           </Tip>

    <Frame>
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/dicloak/proxy-connection.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=5ae68ffa62fc767ba546f0cb74011cd0" alt="proxy-connection" width="1999" height="1250" data-path="images/integrations/dicloak/proxy-connection.png" />
    </Frame>
  </Step>

  <Step title="测试代理">
    1. 点击 **检查代理** 按钮测试连接。

    <Frame>
      <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/dicloak/check-proxy.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=b68cc53091b50de0fafde36fc03667f2" alt="check-proxy" width="1999" height="1250" data-path="images/integrations/dicloak/check-proxy.png" />
    </Frame>

    2. 确认连接测试成功，并保存设置。

    <Frame>
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/dicloak/proxy-test-success.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=8523da5097a09339ebe614a47c89090c" alt="proxy-test-success" width="1999" height="1250" data-path="images/integrations/dicloak/proxy-test-success.png" />
    </Frame>
  </Step>

  <Step title="开始浏览">
    1. 点击 **打开** 按钮使用代理。

    <Frame>
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/dicloak/open-browser.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=68502c89c8c3107f5527f0151c913eb0" alt="open-browser" width="1999" height="1250" data-path="images/integrations/dicloak/open-browser.png" />
    </Frame>

    2. 浏览器将以你的首选配置和设置好的代理启动。

    <Frame>
      <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/dicloak/browser-open.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=b4c844ccf0802123c437d654e529964f" alt="browser-open" width="1999" height="1250" data-path="images/integrations/dicloak/browser-open.png" />
    </Frame>
  </Step>
</Steps>

***

## 额外提示

* **会话控制**：Bright Data 支持会话自定义。根据需要保持相同 IP 或轮换 IP。
* **代理池**：在大型数据采集项目中使用 Bright Data 的代理池。
* **DICloak 增强功能**：利用 DICloak 的反指纹特性模拟人类浏览行为。

通过本指南，你可以高效地将 Bright Data 与 DICloak 集成，实现安全、高效且匿名的浏览和数据采集。
