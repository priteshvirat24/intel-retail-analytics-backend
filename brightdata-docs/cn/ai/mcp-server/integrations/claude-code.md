> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Claude Code MCP 服务器集成

> 如何将 Claude Code 与 Bright Data MCP 服务器集成，以增强 AI 功能。

## 快速安装

要将 Bright Data 集成到 Claude Code，只需将以下命令复制到终端：

```bash theme={null}
claude mcp add --transport sse brightdata "https://mcp.brightdata.com/sse?token=<your-api-token>"
```

## 自托管 MCP

<Steps>
  <Step title="先决条件">
    开始之前，请确保您具备以下条件：

    * 已安装并配置 [Claude Code](https://docs.anthropic.com/en/docs/claude-code)
    * 拥有 [Bright Data 账户](https://www.bright.cn/?hs_signup=1\&utm_source=docs)（新用户可获得免费测试额度，之后可按需付费）
    * 从 [用户设置页面](https://www.bright.cn/cp/setting/users) 获取 **API 密钥**（新用户将在欢迎邮件中收到 **API key**）

    <Tip>
      如果您希望使用不同的 zone 名称，可以在配置中通过 `unlocker` URL 参数指定
    </Tip>
  </Step>

  <Step title="基本配置">
    将 Bright Data MCP 服务器添加到 Claude Code 配置中：

    ```bash theme={null}
    claude mcp add --transport sse brightdata https://mcp.brightdata.com/sse?token=<your-api-token>
    ```

    将 `<your-api-token>` 替换为您从 Bright Data 获取的实际 API 令牌。
  </Step>

  <Step title="验证">
    通过运行以下命令验证集成：

    ```bash theme={null}
    claude mcp list
    ```

    您应看到如下输出，确认连接成功：

    ```
    brightdata: https://mcp.brightdata.com/sse?token=<yourapikey>(SSE) - ✓ Connected
    ```
  </Step>
</Steps>
