> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 文档 MCP - 从您的 Agent 查询 Bright Data 文档

> 通过模型上下文协议将您的 AI 编码 agent 连接到 Bright Data 文档。搜索和检索文档作为原生 MCP 资源 - 无需爬虫。

## 什么是文档 MCP？

文档 MCP 服务器位于 `https://docs.brightdata.com/mcp`，将所有 Bright Data 文档作为可搜索的 MCP 资源公开。任何兼容 MCP 的编码 agent 都可以连接并实时查询文档，直接在其推理循环内进行。

<Info>
  **两个 Bright MCP 服务器 - 两个不同的工作：**

  | MCP 服务器             | URL                                            | 目的                   |
  | ------------------- | ---------------------------------------------- | -------------------- |
  | **文档 MCP**          | `https://docs.brightdata.com/mcp`              | 搜索和检索 Bright Data 文档 |
  | **Bright Data MCP** | `https://mcp.brightdata.com/mcp?token=<token>` | 访问实时网络数据 - 爬虫、搜索、解锁器 |

  本页面涵盖 **文档 MCP**。要从您的 agent 访问实时网络数据，请参阅 [MCP 服务器文档 →](/cn/ai/mcp-server/overview)
</Info>

***

## 连接您的 agent

<Tabs>
  <Tab title="Claude Code">
    ```bash theme={null}
    claude mcp add --transport http brightdata-docs https://docs.brightdata.com/mcp
    ```

    验证连接：

    ```bash theme={null}
    claude mcp list
    # brightdata-docs: https://docs.brightdata.com/mcp (HTTP) - ✓ Connected
    ```
  </Tab>

  <Tab title="Cursor">
    打开 **设置 → 工具与集成 → 添加自定义 MCP** 并粘贴：

    ```json theme={null}
    {
      "mcpServers": {
        "brightdata-docs": {
          "url": "https://docs.brightdata.com/mcp",
          "transport": "http"
        }
      }
    }
    ```
  </Tab>

  <Tab title="VS Code (Copilot)">
    添加到您的 `.vscode/mcp.json` 或用户 MCP 设置：

    ```json theme={null}
    {
      "servers": {
        "brightdata-docs": {
          "url": "https://docs.brightdata.com/mcp",
          "type": "http"
        }
      }
    }
    ```
  </Tab>

  <Tab title="Claude Desktop">
    添加到 `claude_desktop_config.json`（通常位于 `~/.config/claude/`）：

    ```json theme={null}
    {
      "mcpServers": {
        "brightdata-docs": {
          "url": "https://docs.brightdata.com/mcp",
          "transport": "http"
        }
      }
    }
    ```
  </Tab>

  <Tab title="Windsurf / 任何 MCP 客户端">
    文档 MCP 使用标准 HTTP 传输 - 将任何兼容 MCP 的客户端连接到：

    ```
    https://docs.brightdata.com/mcp
    ```

    无需身份验证。无需 API 令牌。
  </Tab>
</Tabs>

***

## 您的 agent 可以用它做什么？

连接后，您的 agent 将获得对完整 Bright Data 文档索引的**搜索工具**。它可以：

* **找到正确的 API** - "在 SERP API 中设置自定义地理位置的参数是什么？"
* **检索产品页面** - 获取 Web Unlocker、Scraping Browser 或任何产品的完整参考资料
* **查找代码示例** - "显示一个用于分页 SERP 结果的 Python 示例"
* **探索集成** - "我如何将 LangChain 连接到 Bright Data？"
* **检查定价和限制** - "Bright Data MCP 免费层的速率限制是什么？"

Agent 在其推理循环中查询文档 - 因此它始终具有准确、最新的信息，而不是依赖过时的训练数据。

***

## 同时使用两个 MCP 服务器

为了获得最大的能力，在单个会话中连接**两个** MCP 服务器：

```bash theme={null}
# 文档：了解如何使用 Bright Data
claude mcp add --transport http brightdata-docs https://docs.brightdata.com/mcp

# 数据：实际使用 Bright Data
claude mcp add --transport sse brightdata https://mcp.brightdata.com/sse?token=<your-api-token>
```

现在您的 agent 可以查找文档**并**在同一会话中执行真实网络数据请求 - 无需上下文切换。

<Tip>
  编码 agent 的最佳设置是所有三个层协同工作：

  1. 用于嵌入式基线知识的\*\*[技能](/cn/ai/for-agents/skills)\*\*
  2. 用于按需文档查找的**文档 MCP**
  3. 用于实时网络访问的\*\*[Bright Data MCP](/cn/ai/mcp-server/overview)\*\*

  安装技能一次，连接两个 MCP 服务器，您的 agent 就完全装备好了。
</Tip>

***

## 速率限制

| 限制        | 值     |
| --------- | ----- |
| 每用户每小时请求数 | 200   |
| 每域名每小时请求数 | 1,000 |

这些限制适用于 Mintlify 托管的文档 MCP。对于更高的吞吐量，使用 [llms-full.txt](/cn/ai/for-agents/llm-references) 在本地加载完整文档。

***

## 后续步骤

<CardGroup cols={2}>
  <Card title="Bright Data MCP 服务器" icon="microchip-ai" href="/cn/ai/mcp-server/overview">
    添加实时网络数据访问 - 搜索、爬虫和从网络提取
  </Card>

  <Card title="LLM 参考资料" icon="file-lines" href="/cn/ai/for-agents/llm-references">
    加载 llms.txt 或 llms-full.txt 以实现离线或基于 RAG 的所有文档访问
  </Card>
</CardGroup>
