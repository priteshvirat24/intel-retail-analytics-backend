> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# LlamaIndex 集成

> 如何将 LlamaIndex 与 Bright Data 的 The Bright Data MCP 服务器集成，以增强 AI 代理功能。

## 托管 MCP

<Steps>
  <Step title="获取 API 密钥">
    1. 前往 [Bright Data 用户设置](https://www.bright.cn/cp/setting/users)
    2. 复制您的 API 密钥（格式类似：`2dceb1aa0***************************`）
  </Step>

  <Step title="安装 LlamaIndex MCP 工具包">
    ```shell theme={null}
    pip install llama-index-tools-mcp
    ```
  </Step>

  <Step title="配置 MCP 服务器">
    ```python expandable theme={null}
    import asyncio
    from llama_index.tools.mcp import BasicMCPClient

    async def main():
        http_client = BasicMCPClient("https://mcp.brightdata.com/mcp?token=<API_TOKEN>")

        # 列出工具
        tools = await http_client.list_tools()
        print("工具列表:", tools)

        # 调用工具
        result = await http_client.call_tool("scrape_as_markdown", {"url":"https://docs.llamaindex.ai/en/stable/examples/tools/mcp/"})
        print("结果:", result)

    asyncio.run(main())
    ```
  </Step>

  <Step title="测试功能">
    1. 运行 LlamaIndex 脚本并手动调用工具
    2. 您应能看到以 Markdown 格式返回的指定 URL 内容
  </Step>

  <Step title="监控使用情况">
    1. 在 Bright Data 控制台的 [我的区域](https://www.bright.cn/cp/zones) 查看 API 使用情况
    2. 免费层包含每月 5,000 个请求
  </Step>
</Steps>
