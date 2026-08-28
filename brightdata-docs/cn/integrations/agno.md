> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 Agno 中设置 Bright Data

Bright Data MCP 工具包现已在 Agno 中提供，为 AI 智能体带来真实的网页访问能力。此集成使智能体能够从超过 40 个平台（包括 Amazon、LinkedIn、TikTok、Instagram 和 Facebook）进行结构化数据提取和网页抓取。

智能体可以执行诸如抓取产品列表、截图采集、运行搜索查询、访问实时结构化数据流等任务，且仅需最少的设置。这使您能够轻松构建具备推理、行动和实时数据获取能力的智能体，用于研究、自动化和监控。

## 如何将 Bright Data 集成到 LangChain 中

<Steps>
  <Step title="前置条件">
    * Bright Data API 密钥
    * 用于搜索引擎功能的有效 SERP Zone
    * 用于抓取的有效 Web Unlocker API Zone
  </Step>

  <Step title="获取 Bright Data API 密钥">
    * 登录您的 [Bright Data 仪表盘](https://www.bright.cn/cp)。
    * 前往 [Account Settings](https://www.bright.cn/cp/setting/users)。
    * 如果尚未生成，请[生成 API 密钥](/cn/api-reference/authentication#how-do-i-authenticate-with-api-key%3F)。
  </Step>

  <Step title="安装 Bright Data 集成">
    您可以从 GitHub 直接安装 Bright Data 集成，工具代码可在[此处](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/brightdata.py)获取。

    <Note>
      该集成将于本周末发布到 **PyPI**。发布后，您可以使用以下命令进行安装：

      ```sh theme={null}
      pip install agno
      ```
    </Note>
  </Step>

  <Step title="设置环境变量">
    将您的 Bright Data API 密钥设置为环境变量：

    ```python theme={null}
    import os


    os.environ["BRIGHT_DATA_API_KEY"] = "your-api-key"
    ```
  </Step>

  <Step title="使用示例">
    ```python theme={null}
    from agno.agent import Agent
    from agno.tools.brightdata import BrightDataTools 
    from agno.models.openai import OpenAIChat 
    from dotenv import load_dotenv 

    load_dotenv() 

    agent = Agent(
      tools=[
          BrightDataTools(
            serp_zone="serp",
            web_unlocker_zone="unlocker"
          )
        ],
      show_tool_calls=True,
      model=OpenAIChat(id="gpt-4o-mini"),
    ) 

    agent.print_response("Search for AAPL news", markdown=True)
    ```
  </Step>
</Steps>
