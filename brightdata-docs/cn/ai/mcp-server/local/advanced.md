> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 高级配置

> 完成基础设置后，您可以使用高级选项来自定义 MCP 服务器。

## MCP 服务器模式

Bright Data 的 MCP 服务器提供两种模式，以满足不同需求：

* **Rapid（免费）** - 快速抓取搜索结果，并将任何公共网页解锁为干净的 Markdown。
* **Pro** - 访问高级抓取、来自主流平台（Amazon、LinkedIn、X、Instagram 等）的结构化数据，以及完整的浏览器自动化功能。专为动态和大规模用例打造。

<Tip>
  **Rapid（免费）** 模式为默认启用，且**推荐**用于日常浏览和数据任务。
</Tip>

***

## 本地配置

在本地使用 MCP 服务器时，您可以通过环境变量进行更精细的控制：

* `RATE_LIMIT` - 设置请求的速率限制（*默认：* `100/1h`）。
* `WEB_UNLOCKER_ZONE` - 覆盖默认的网页解锁 zone（*默认：* `mcp_unlocker`）。
* `BROWSER_ZONE` - 覆盖默认的浏览器 zone（*默认：* `mcp_browser`）。
* `PRO_MODE` - 设置为 true/false 以启用或禁用 Pro 工具（*默认：* `false`）。

<Tip>
  使用 `PRO_MODE=true` 来启用 **Pro 模式**。
</Tip>

### 使用示例：

```json theme={null}
{
  "mcpServers":{
    "Bright Data":{
      "command":"npx",
      "args":["@brightdata/mcp"],
      "env":{
        "API_TOKEN":"<insert-your-api-token-here>",
        "WEB_UNLOCKER_ZONE": "my_zone_name",
        "BROWSER_ZONE": "my_browser_zone",
        "PRO_MODE": "true"
      }
    }
  }
}
```
