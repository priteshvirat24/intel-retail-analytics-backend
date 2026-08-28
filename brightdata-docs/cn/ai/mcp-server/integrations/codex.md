> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Codex MCP 服务器集成

> 通过 config.toml 或 codex mcp add 命令将 OpenAI Codex CLI 与 Bright Data MCP 服务器（60+ 工具）集成，实现实时网络搜索和抓取。

<Card title="正在构建 AI 初创公司？" cta="了解更多" href="https://brightdata.com/ai/ai-startups-program" icon="rocket-launch" iconType="duotone" arrow="true">
  您可能符合我们的初创计划资格。获得本文所介绍基础设施的全额资助访问权限（最高价值 \$20,000）。
</Card>

将 Bright Data MCP 服务器添加到 OpenAI Codex CLI，让您的编码代理无需担心被封锁即可搜索、抓取和浏览实时网络。Codex 从 `~/.codex/config.toml` 读取 MCP 服务器定义，您可以直接编辑该文件，或使用 `codex mcp add` 命令进行更新。

## 先决条件

* 已安装并登录 [Codex CLI](https://github.com/openai/codex)
* 已安装并更新 [Node.js](https://nodejs.org/en/download)（仅自托管服务器需要）
* 拥有 [Bright Data 账户](https://www.bright.cn/?hs_signup=1\&utm_source=docs)（新用户可获得免费测试额度，之后可按需付费）
* 从 [用户设置页面](https://www.bright.cn/cp/setting/users) 获取 API 密钥（新用户将在欢迎邮件中收到 API 密钥）

## 托管 MCP

托管服务器无需本地安装。将以下表添加到 `~/.codex/config.toml`，并将 `<your-api-token>` 替换为您的 Bright Data API 密钥：

```toml theme={null}
[mcp_servers.brightdata]
url = "https://mcp.brightdata.com/mcp?token=<your-api-token>"
```

`[mcp_servers.<id>]` 表使用 `url` 定义可流式传输的 HTTP 服务器。Bright Data 托管 MCP 通过 `token` 查询参数接受 API 密钥，因此无需单独的认证头。

<Tip>
  如果您希望使用不同的 zone 名称，可通过 `unlocker` URL 参数指定，例如 `...?token=<your-api-token>&unlocker=<your-zone>`。
</Tip>

## 自托管 MCP

自托管服务器通过 `npx` 在本地运行，并从环境变量读取您的 API 密钥。

<Steps>
  <Step title="使用 CLI 添加服务器">
    在终端中运行以下命令。`--` 分隔符告诉 Codex 环境标志在哪里结束、服务器命令从哪里开始：

    ```bash theme={null}
    codex mcp add brightdata --env API_TOKEN=<your-api-token> -- npx -y @brightdata/mcp
    ```
  </Step>

  <Step title="或直接编辑 config.toml">
    或者，将以下表添加到 `~/.codex/config.toml`：

    ```toml theme={null}
    [mcp_servers.brightdata]
    command = "npx"
    args = ["-y", "@brightdata/mcp"]

    [mcp_servers.brightdata.env]
    API_TOKEN = "<your-api-token>"
    ```
  </Step>
</Steps>

## 验证

通过列出已配置的 MCP 服务器来验证集成：

```bash theme={null}
codex mcp list
```

您应在输出中看到 `brightdata`，确认服务器已配置。启动 Codex 会话并让它抓取一个实时网页，以确认工具正常响应。
