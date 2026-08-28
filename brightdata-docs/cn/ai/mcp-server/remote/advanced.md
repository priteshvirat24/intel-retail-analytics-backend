> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 高级配置

> 完成基础设置后，您可以使用高级选项自定义 MCP 服务器。

## MCP 服务器模式

Bright Data 的 MCP 服务器提供两种模式，以满足不同需求：

* **Rapid（免费）** - 快速抓取搜索结果，并将任何公共网页转换为干净的 Markdown。
* **Pro** - 访问高级抓取功能、来自主要平台（Amazon、LinkedIn、X、Instagram 等）的结构化数据，以及完整的浏览器自动化。适用于动态和大规模的使用场景。

<Tip>
  **Rapid（免费）** 模式默认启用，并**推荐**用于日常浏览与数据需求。
</Tip>

***

## 远程配置

在使用远程 MCP 服务器时，可以通过向端点传递查询参数来配置高级选项：

<ParamField query="unlocker" type="string" default="mcp_unlocker">
  为网页抓取使用自定义区域名称。

  > **例如：** `&unlocker=my_zone_name`
</ParamField>

<ParamField query="browser" type="string" default="mcp_browser">
  为浏览器自动化使用自定义区域名称。

  > **例如：** `&browser=my_browser_zone`
</ParamField>

<ParamField query="pro" type="number" default="0">
  启用高级（Pro）处理。

  > **例如：** `&pro=1`

  <Tip>
    使用 `&pro=1` 来启用 **Pro 模式**。
  </Tip>
</ParamField>

### 使用示例：

<CodeGroup>
  ```sh SSE (Server-Sent Events) endpoint: theme={null}
  https://mcp.brightdata.com/sse?token=YOUR_API_TOKEN&unlocker=my_zone_name&browser=my_browser_zone&pro=1
  ```

  ```sh Streamable HTTP endpoint: theme={null}
  https://mcp.brightdata.com/mcp?token=YOUR_API_TOKEN&unlocker=my_zone_name&browser=my_browser_zone&pro=1
  ```
</CodeGroup>

***
