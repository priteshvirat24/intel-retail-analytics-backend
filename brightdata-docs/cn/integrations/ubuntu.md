> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 Ubuntu 上设置 Bright Data

> 在 Ubuntu 上优化你的终端工作流！通过 Bright Data 安全地路由命令和应用程序，确保隐私并顺利访问受地理限制的资源。本指南将教你如何在 Ubuntu 系统上配置 Bright Data。

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

## 为什么在 Ubuntu 上使用 Bright Data？

在 Ubuntu 上通过 Bright Data 代理路由流量可以增强隐私，同时访问特定地区的内容。无论是运行脚本、管理远程服务器，还是使用命令行工具，Bright Data 都能确保连接安全高效。

<Tip>
  在整个会话期间保持一致的 IP 地址，请在用户名中使用 `-session` 参数。由于 BrightData 代理默认每次请求都会旋转 IP，这一点至关重要。[了解更多](/cn/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

## 如何在 Ubuntu 上设置 Bright Data

**步骤 1. 打开终端**

1. 按 **Ctrl+Alt+T** 打开终端。

**步骤 2. 设置代理环境变量**

1. 将 `[HOST]`、`[PORT]`、`[USERNAME]` 和 `[PASSWORD]` 替换为你的 Bright Data 信息。
2. 运行以下命令：

```bash theme={null}
export http_proxy="http://[USERNAME]:[PASSWORD]@[HOST]:[PORT]"
export https_proxy="http://[USERNAME]:[PASSWORD]@[HOST]:[PORT]"
```

使用以下命令进行 SOCKS5 配置：

```bash theme={null}
export socks_proxy="socks5://[USERNAME]:[PASSWORD]@[HOST]:[PORT]"
```

如果需要使用特定国家/地区的出口节点，请相应修改 `[USERNAME]`（例如 `your-username-country-US`）。

**步骤 3. 验证代理配置**

1. 运行以下命令测试代理设置：

```bash theme={null}
curl http://httpbin.org/ip
```

2. 输出应显示 Bright Data 分配的 IP 地址。

**步骤 4. 使代理设置永久生效（可选）**

1. 打开主目录下的 `.bashrc` 文件：

```bash theme={null}
nano ~/.bashrc
```

2. 在文件末尾添加以下行：

```bash theme={null}
export http_proxy="http://[USERNAME]:[PASSWORD]@[HOST]:[PORT]"
export https_proxy="http://[USERNAME]:[PASSWORD]@[HOST]:[PORT]"
export socks_proxy="socks5://[USERNAME]:[PASSWORD]@[HOST]:[PORT]"
```

3. 保存并退出 (`Ctrl+O`, `Enter`, `Ctrl+X`)。
4. 重新加载文件以应用更改：

```bash theme={null}
source ~/.bashrc
```

通过在 Ubuntu 上集成 Bright Data，你可以轻松管理连接，同时获得增强的隐私和安全性。无论是执行日常任务还是访问特定地区内容，Bright Data 都能确保平稳可靠的体验。快来尝试吧，享受无忧的终端访问！
