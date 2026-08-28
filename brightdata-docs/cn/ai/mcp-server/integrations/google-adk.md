> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Google ADK 集成

> 如何将 Google ADK 与 Bright Data 的 The Bright Data MCP 服务器集成，以增强 AI 代理功能。

## 远程 MCP

<Steps>
  <Step title="获取 API 密钥">
    1. 前往 [Bright Data 用户设置](https://www.bright.cn/cp/setting/users)
    2. 复制您的 API 密钥（格式类似：`2dceb1aa0***************************`）
  </Step>

  <Step title="安装所需软件包">
    ```shell theme={null}
    pip install google-adk
    ```
  </Step>

  <Step title="配置 MCP 服务器">
    ```python expandable theme={null}
    from google.adk.agents import Agent
    from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
    from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset

    BRIGHTDATA_API_TOKEN = "YOUR_BRIGHTDATA_API_TOKEN"

    root_agent = Agent(
        model="gemini-2.5-pro",
        name="brightdata_agent",
        instruction="""帮助用户使用 Bright Data 访问网页数据""",
        tools=[
            MCPToolset(
                connection_params=StreamableHTTPServerParams(
                    url=f"https://mcp.brightdata.com/mcp?token={BRIGHTDATA_API_TOKEN}",
                ),
            )
        ],
    )
    ```
  </Step>

  <Step title="设置环境变量（可选）">
    为了更安全，您可以将 API 密钥存储为环境变量：

    ```python theme={null}
    import os
    BRIGHTDATA_API_TOKEN = os.getenv("BRIGHTDATA_API_TOKEN")
    ```

    然后在项目目录下创建 `.env` 文件：

    ```env theme={null}
    BRIGHTDATA_API_TOKEN=your_brightdata_api_token_here
    ```
  </Step>

  <Step title="测试功能">
    1. 用实际的 Bright Data API 密钥替换 `YOUR_BRIGHTDATA_API_TOKEN`
    2. 运行 Google ADK 脚本
    3. 您将看到代理执行网页搜索并提供完整响应
  </Step>

  <Step title="监控使用情况">
    1. 在 Bright Data 控制台的 [我的区域](https://www.bright.cn/cp/zones) 查看 API 使用情况
    2. 免费层包含每月 5,000 个请求
  </Step>
</Steps>

## 本地 MCP 服务器

<Steps>
  <Step title="获取 API 密钥">
    1. 前往 [Bright Data 用户设置](https://www.bright.cn/cp/setting/users)
    2. 复制您的 API 密钥（格式类似：`2dceb1aa0***************************`）
  </Step>

  <Step title="安装所需软件包">
    ```shell theme={null}
    pip install google-genai
    npm install -g @brightdata/mcp
    ```
  </Step>

  <Step title="配置本地 MCP 服务器">
    ```python expandable theme={null}
    from google.adk.agents import Agent
    from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
    from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
    from mcp import StdioServerParameters

    BRIGHTDATA_API_TOKEN = "YOUR_BRIGHTDATA_API_TOKEN"

    root_agent = Agent(
        model="gemini-2.5-pro",
        name="brightdata_agent",
        instruction="帮助用户使用 Bright Data 访问网页数据",
        tools=[
            MCPToolset(
                connection_params=StdioConnectionParams(
                    server_params = StdioServerParameters(
                        command="npx",
                        args=["@brightdata/mcp"],
                        env={
                            "API_TOKEN": BRIGHTDATA_API_TOKEN,
                            "PRO_MODE": "true",  # 可选：启用全部 60+ 工具
                        }
                    ),
                    timeout=300,
                ),
            )
        ],
    )
    ```
  </Step>

  <Step title="测试功能">
    1. 用实际的 Bright Data API 密钥替换 `YOUR_BRIGHTDATA_API_TOKEN`
    2. 使用本地 MCP 服务器运行 Google ADK 脚本
    3. 代理将使用本地安装的 MCP 服务器访问所有可用工具
  </Step>

  <Step title="监控使用情况">
    1. 在 Bright Data 控制台的 [我的区域](https://www.bright.cn/cp/zones) 查看 API 使用情况
    2. 免费层包含每月 5,000 个请求
  </Step>
</Steps>

## 可用工具

Bright Data MCP 服务器提供强大的网页抓取功能：

* **快速模式（免费层）**：包含搜索、抓取和数据提取的 4 个核心工具
* **专业模式**：额外 60+ 工具，包括批量操作、浏览器自动化，以及主要平台的结构化数据 API

[查看完整工具文档](../tools)

[访问 Google ADK 文档](https://google.github.io/adk-docs/)
