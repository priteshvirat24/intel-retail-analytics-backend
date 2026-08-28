> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# LangChain 集成

> 如何将 LangChain 与 Bright Data 的 The Bright Data MCP 服务器集成，以增强 AI 代理功能。

## 托管 MCP

<Steps>
  <Step title="获取 API 密钥">
    1. 前往 [Bright Data 用户设置](https://www.bright.cn/cp/setting/users)
    2. 复制您的 API 密钥（格式类似：`2dceb1aa0***************************`）
  </Step>

  <Step title="安装所需软件包">
    ```shell theme={null}
    pip install langchain-mcp-adapters
    ```
  </Step>

  <Step title="配置 MCP 服务器">
    ```python expandable theme={null}
    import asyncio
    from langchain_openai import ChatOpenAI
    from langgraph.prebuilt import create_react_agent
    from langchain_mcp_adapters.client import MultiServerMCPClient
    from dotenv import load_dotenv
    import os

    load_dotenv()

    async def main():
        # 配置 MCP 客户端
        client = MultiServerMCPClient({
            "bright_data": {
                "url": "https://mcp.brightdata.com/sse?token=<API_TOKEN>",
                "transport": "sse",
            }
        })

        # 获取可用工具
        tools = await client.get_tools()
        print("可用工具:", [tool.name for tool in tools])

        # 配置 LLM
        llm = ChatOpenAI(
            openai_api_key=os.getenv("OPENROUTER_API_KEY"),
            openai_api_base="https://openrouter.ai/api/v1",
            model_name="moonshotai/kimi-k2"
        )

        # 网络搜索代理的系统提示
        system_prompt = """
        你是一个具备全面抓取能力的网页搜索代理。你的工具包括：
        - **search_engine**：从 Google/Bing/Yandex 获取搜索结果
        - **scrape_as_markdown**：从任何网页提取内容，绕过机器人检测
        - **Structured extractors**：快速可靠地从主要平台获取数据（Amazon、LinkedIn、Instagram、Facebook、X、TikTok、YouTube、Reddit、Zillow 等）
        - **浏览器自动化**：导航、点击、输入、截图以进行复杂操作

        指南：
        - 对支持的平台尽可能使用结构化 web_data_* 工具（更快、更可靠）
        - 对其他网站使用通用抓取
        - 优雅地处理错误并遵守速率限制
        - 逐步思考需要哪些信息以及使用哪些工具
        - 研究全面，提供完整答案

        回答时遵循以下模式：
        1. 思考所需信息
        2. 选择合适的工具
        3. 执行工具
        4. 分析结果
        5. 提供清晰、全面的答案
        """

        # 创建 ReAct 代理
        agent = create_react_agent(
            model=llm,
            tools=tools,
            prompt=system_prompt
        )

        # 测试代理
        print("正在使用可用工具测试 ReAct 代理...")
        print("=" * 50)

        result = await agent.ainvoke({
            "messages": [("human", "搜索关于 AI 最新发展的新闻")]
        })

        print("\n代理响应:")
        print(result["messages"][-1].content)

    if __name__ == "__main__":
        asyncio.run(main())
    ```
  </Step>

  <Step title="设置环境变量">
    在项目目录下创建 `.env` 文件：

    ```env theme={null}
    OPENROUTER_API_KEY=your_openrouter_api_key_here
    ```
  </Step>

  <Step title="测试功能">
    1. 用实际的 Bright Data API 密钥替换 `<API_TOKEN>`
    2. 运行 LangChain 脚本
    3. 您将看到代理执行网页搜索并提供完整响应
  </Step>

  <Step title="监控使用情况">
    1. 在 Bright Data 控制台的 [我的区域](https://www.bright.cn/cp/zones) 查看 API 使用情况
    2. 免费层包含每月 5,000 个请求
  </Step>
</Steps>
