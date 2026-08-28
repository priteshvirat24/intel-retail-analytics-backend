> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 n8n 中设置 Bright Data MCP

> 学习如何将 Bright Data 的 MCP 与 n8n 集成，以构建自动化、无代码的数据工作流。

### 基于 SSE 的 MCP 集成

您也可以通过 SSE（服务器发送事件）集成我们的 MCP。

**要求：**

* [Bright Data 账户](https://www.bright.cn/?hs_signup=1\&utm_source=docs)
* 从 [用户设置](https://www.bright.cn/cp/setting/users) 获取 API 密钥

**配置：**

1. 在您喜欢的平台上创建一个 AI 代理。
2. 附加：
   * 一个聊天模型（例如 `gpt-4` 或 `gpt-4o`）
   * MCP 客户端节点
3. 配置远程 MCP URL：
   ```
   https://mcp.brightdata.com/sse?token=YOUR_API_TOKEN_HERE
   ```
4. 选择要暴露的特定工具，或让 AI 自行选择

AI 代理将使用 MCP 客户端执行任务，并实时返回结果。

### 自托管 MCP 集成（MCP 客户端 - 社区节点）

**要求：**

* 已安装 [Node.js](https://nodejs.org/en/download)
* [Bright Data 账户](https://www.bright.cn/?hs_signup=1\&utm_source=docs)
* 从 [用户设置](https://www.bright.cn/cp/setting/users) 获取 API 密钥

**配置：**

1. 在您喜欢的平台上创建一个 AI 代理。
2. 附加：
   * 一个聊天模型（例如 `gpt-4` 或 `gpt-4o`）
   * Bright Data MCP 客户端（通过 HTTP 或 WebSocket）
3. 配置：

| **变量**       | **值**                                                                                                                                                                                  |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Command      | `npx`                                                                                                                                                                                  |
| Arguments    | `@brightdata/mcp`                                                                                                                                                                      |
| Environments | **API\_KEY** = "\<api-key>"<br />**WEB\_UNLOCKER\_ZONE** = "\<unlocker\_api\_zone name>"<br />**BROWSER\_ZONE** = "\<browser zone name>"<br />**RATE\_LIMIT** = "\<rate limit format>" |

*`RATE_LIMIT 示例：可能的值：100/1h、50/30m、10/5s`*

***
