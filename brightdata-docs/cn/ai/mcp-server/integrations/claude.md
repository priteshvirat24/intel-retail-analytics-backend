> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Claude Desktop 集成

> 如何将 Claude Desktop 与 Bright Data MCP 服务器集成，以增强 AI 功能。

**入门视频**：

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/2lspK4o2tTo" title="Easiest way to start with Claude" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## 托管 MCP

<Steps>
  <Step title="获取 API 令牌">
    1. 前往 [Bright Data 用户设置](https://www.bright.cn/cp/setting/users)
    2. 复制您的 API 令牌（看起来像：`2dceb1aa0***************************`）
  </Step>

  <Step title="配置 MCP 服务器">
    1. 打开 Claude Desktop
    2. 进入：Settings → Developer → Edit Config
    3. 在 `claude_desktop_config.json` 中添加以下内容：

    ```json theme={null}
    {
      "mcpServers": {
        "Bright Data": {
          "command": "npx",
          "args": [
            "mcp-remote",
            "https://mcp.brightdata.com/mcp?token=YOUR_API_TOKEN_HERE"
          ]
        }
      }
    }
    ```

    4. **将 `YOUR_API_TOKEN_HERE` 替换为第 1 步中获取的实际 API 令牌**
    5. 保存并重启 Claude Desktop
  </Step>

  <Step title="测试是否生效">
    1. 向 AI 询问：“你能搜索 Google 的 ‘今日天气’ 吗？”
    2. Claude 会请求权限 — 点击 “Allow”
    3. 您应看到搜索结果！
  </Step>

  <Step title="监控使用情况">
    1. 在 Bright Data 仪表盘的 [My Zones](https://www.bright.cn/cp/zones) 查看 API 使用情况
    2. 免费套餐每月包含 5,000 次请求
  </Step>
</Steps>

## 自托管 MCP

<Steps>
  <Step title="前置条件">
    开始前，请确保具备以下条件：

    * 已安装并更新到最新版本的 [Node.js](https://nodejs.org/en/download)
    * [Bright Data 账户](https://www.bright.cn/?hs_signup=1\&utm_source=docs) （新用户可获取免费测试额度，之后可按需付费）
    * **API 密钥**，可在 [用户设置页面](https://www.bright.cn/cp/setting/users) 获取（新用户在欢迎邮件中收到 API 密钥）

    <Tip>
      如果希望使用不同的区域名称，可在配置中通过 `WEB_UNLOCKER_ZONE` 环境变量指定
    </Tip>
  </Step>

  <Step title="基础配置">
    进入 Claude → Settings → Developer → Edit Config → `claude_desktop_config.json`，包含以下内容：

    ```json expandable theme={null}
    {
      "mcpServers": {
        "Bright Data": {
          "command": "npx",
          "args": ["@brightdata/mcp"],
          "env": {
            "API_TOKEN": "<在 https://www.bright.cn/cp/setting/users 获取您的 API 密钥>"     
          }
        }
      }
    }
    ```
  </Step>

  <Step title="高级配置">
    如果希望使用高级功能，如速率限制或自定义区域，可添加更多环境变量：

    ```json expandable theme={null}
    {
      "mcpServers": {
        "Bright Data": {
          "command": "npx",
          "args": ["@brightdata/mcp"],
          "env": {
            "API_TOKEN": "<在 https://www.bright.cn/cp/setting/users 获取您的 API 密钥>",
            "WEB_UNLOCKER_ZONE": "<可选 - 如果想为 web_unlocker 使用特定名称，在此填写；不使用则删除>",
            "BROWSER_ZONE": "<可选 - 如果想为 browser_api 使用特定名称，在此填写；不使用则删除>",
            "RATE_LIMIT": "<可选 - 速率限制格式，可选值：limit/time+unit，例如 100/1h, 50/30m, 10/5s；不使用则删除>",
            "ADVANCED_MODE":"<可选 - 默认 false，设置为 true 可开放所有 60+ 工具>"     
          }
        }
      }
    }
    ```
  </Step>
</Steps>
