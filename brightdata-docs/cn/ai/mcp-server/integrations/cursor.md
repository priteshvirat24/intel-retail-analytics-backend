> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cursor MCP 服务器集成

> 如何将 Cursor 与 Bright Data 的 MCP 服务器集成，以增强 AI 功能。

## 自托管 MCP

<Steps>
  <Step title="先决条件">
    开始之前，请确保您具备以下条件：

    * 已安装并更新到最新版本的 [Node.js](https://nodejs.org/en/download)
    * [Bright Data 账户](https://www.bright.cn/?hs_signup=1\&utm_source=docs)（新用户可获得测试用免费额度，然后可以按需付费）
    * 来自 [用户设置页面](https://www.bright.cn/cp/setting/users) 的 **API 密钥**（新用户会在欢迎邮件中收到 **API 密钥**）

    <Tip>
      如果您希望使用不同的区域名称，可以在配置中通过 `WEB_UNLOCKER_ZONE` 环境变量指定
    </Tip>
  </Step>

  <Step title="基础配置">
    前往 Cursor -> 点击齿轮图标 -> 工具与集成 -> 添加自定义 MCP -> 包含以下内容：

    ```json expandable theme={null}
    {
        "mcpServers": {
        "brightdata-mcp": {
            "command": "npx",
            "args": ["-y", "@brightdata/mcp"],
            "env": {
            "API_TOKEN": "<你的 API 密钥>"
            }
        }
        }
    }
    ```

    <Frame>
      <img src="https://mintcdn.com/brightdata/5sJgYq9iW-Vo_7rr/images/Screenshot2025-07-14at13.50.57.png?fit=max&auto=format&n=5sJgYq9iW-Vo_7rr&q=85&s=b45b0fd381570a6ec4619de710a18914" alt="Screenshot 2025-07-14 at 13.50.57.png" title="Screenshot 2025-07-14 at 13.50.57.png" width="1453" height="602" data-path="images/Screenshot2025-07-14at13.50.57.png" />
    </Frame>

    然后您应看到：

    <Frame>
      <img src="https://mintcdn.com/brightdata/5sJgYq9iW-Vo_7rr/images/Screenshot2025-07-14at14.18.16.png?fit=max&auto=format&n=5sJgYq9iW-Vo_7rr&q=85&s=8181d25cf09203efb21645492de98628" alt="Screenshot 2025-07-14 at 14.18.16.png" title="Screenshot 2025-07-14 at 14.18.16.png" width="386" height="153" data-path="images/Screenshot2025-07-14at14.18.16.png" />
    </Frame>
  </Step>
</Steps>
