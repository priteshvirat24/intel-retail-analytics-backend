> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# CrewAI 集成

> 如何将 CrewAI 与 Bright Data 的 The Bright Data MCP 服务器集成，以增强 AI 代理功能。

## 托管 MCP

<Steps>
  <Step title="获取 API 令牌">
    1. 前往 [Bright Data 用户设置](https://www.bright.cn/cp/setting/users)
    2. 复制您的 API 令牌（看起来像：`2dceb1aa0***************************`）
  </Step>

  <Step title="配置 MCP 服务器">
    ```python expandable theme={null}
    from crewai import Agent, Task, Crew
    from crewai_tools import MCPServerAdapter
    import os

    server_params = {
        "url": "https://mcp.brightdata.com/sse?token=API_TOKEN",
        "transport": "sse"
    }

    try:
        with MCPServerAdapter(server_params) as mcp_tools:
            print(f"可用工具: {[tool.name for tool in mcp_tools]}")
            
            my_agent = Agent(
                role="网页抓取专家",
                goal="使用 Bright Data 工具从网站提取数据",
                backstory="我擅长使用 MCP 工具进行网页抓取和数据提取。",
                tools=mcp_tools,
                verbose=True,
                llm="gpt-4o-mini",
            )
            
            task = Task(
                description="搜索从纽约到旧金山的航班，并提供你找到的信息摘要。使用 search_engine 工具获取航班信息，并以清晰的格式返回结果。",
                expected_output="提供从纽约到旧金山可用航班的清晰摘要，包括主要细节，如航空公司、时间和票价（如有）。",
                agent=my_agent
            )
            
            crew = Crew(
                agents=[my_agent],
                tasks=[task],
                verbose=True
            )
            
            result = crew.kickoff()
            print("\n=== 结果 ===")
            print(result)
            
    except Exception as e:
        print(f"连接 MCP 服务器出错: {e}")
        print("请确保你已经：")
        print("1. 设置了 BRIGHT_DATA_API_KEY 环境变量")
        print("2. 安装了 Bright Data MCP 服务器: npm install -g @bright_data/mcp-server-bright-data")
        print("3. 系统中已安装 Node.js")
    ```
  </Step>

  <Step title="测试是否生效">
    1. 使用包含航班搜索任务的 CrewAI 脚本运行
    2. 代理将使用 Bright Data 工具搜索航班信息
    3. 您应看到包含航班详情的结果
  </Step>

  <Step title="监控使用情况">
    1. 在 Bright Data 仪表盘的 [My Zones](https://www.bright.cn/cp/zones) 查看 API 使用情况
    2. 免费套餐每月包含 5,000 次请求
  </Step>
</Steps>
