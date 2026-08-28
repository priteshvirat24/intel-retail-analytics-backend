> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 Pica 中设置 Bright Data

[Pica](https://www.picaos.com/) 是一个平台，旨在增强 AI 代理的工作流，通过提供可靠、匿名且可扩展的网络访问，实现真实数据的自动化。将 Pica 与 Bright Data 集成，可以让 AI 代理利用 Bright Data 的高级网页抓取和代理网络能力，高效地收集和处理网络数据。

## 可用的 Bright Data 工具

Bright Data 为与 Pica 的集成提供以下工具：

* **Scrapers**：使用 Bright Data 强大的 Scrapers 自动化网页数据提取。
* **Web Unlocker API**：访问并获取采用高级反爬虫措施的网站数据。

## 如何将 Bright Data 与 Pica 集成

<Steps>
  <Step title="获取 Bright Data API Key">
    * 登录 [Bright Data 控制面板](https://www.bright.cn/cp)。
    * 进入 [账户设置](https://www.bright.cn/cp/setting/users)。
    * 如果尚未生成，请 [生成 API Key](/cn/api-reference/authentication#how-do-i-authenticate-with-api-key%3F)。
  </Step>

  <Step title="安装 Bright Data 集成">
    通过以下命令安装 Pica 的 Bright Data 集成包：

    ```sh theme={null}
    pip install pica-langchain
    ```

    <Note>
      其他可用集成包括：

      * [Vercel AI SDK](https://docs.picaos.com/cn/sdk/vercel-ai)
      * [MCP](https://docs.picaos.com/cn/sdk/mcp)
    </Note>
  </Step>

  <Step title="选择您偏好的 Bright Data 工具">
    [Pica 连接器](https://www.picaos.com/community/connectors) 提供两种主要的 Bright Data 集成工具：

    <CodeGroup>
      ```python Scrapers 在 Pica + LangChain 中使用示例 theme={null}
      import os
      from langchain_openai import ChatOpenAI
      from langchain.agents import AgentType
      from pica_langchain import PicaClient, create_pica_agent
      from pica_langchain.models import PicaClientOptions

      def main():
        try:
            pica_client = PicaClient(
                secret=os.environ["PICA_SECRET"],
                options=PicaClientOptions(
                    connectors=["test::bright-data::default::fd583f2344fa414293bdda4f240258c1"] # Initialize all available connections or pass specific connector keys
                )
            )

            pica_client.initialize()
            
            llm = ChatOpenAI(
                temperature=0,
                model="gpt-4o",
            )

            # Create an agent with Pica tools
            agent = create_pica_agent(
                client=pica_client,
                llm=llm,
                agent_type=AgentType.OPENAI_FUNCTIONS,
            )

            # Execute a multi-step workflow using the GitHub Connector
            result = agent.invoke({
                "input": (
                    "Trigger Synchronous Web Scraping and Retrieve Results, use this dataset ID : gd_l7q7dkf244hwjntr0 and search for this URL : https://www.amazon.com/dp/B0D2Q9397Y?th=1&psc=1"
                )
            })
            
            print(f"\nWorkflow Result:\n {result}")
        
        except Exception as e:
            print(f"ERROR: An unexpected error occurred: {e}")


      if __name__ == "__main__":
        main()

      ```

      ```python Web Unlocker API 在 Pica + LangChain 中使用示例 theme={null}
      import os
      from langchain_openai import ChatOpenAI
      from langchain.agents import AgentType
      from pica_langchain import PicaClient, create_pica_agent
      from pica_langchain.models import PicaClientOptions

      def main():
        try:
            pica_client = PicaClient(
                secret=os.environ["PICA_SECRET"],
                options=PicaClientOptions(
                    connectors=["test::bright-data::default::fd583f2344fa414293bdda4f240258c1"] # Initialize all available connections or pass specific connector keys
                )
            )

            pica_client.initialize()
            
            llm = ChatOpenAI(
                temperature=0,
                model="gpt-4o",
            )

            # Create an agent with Pica tools
            agent = create_pica_agent(
                client=pica_client,
                llm=llm,
                agent_type=AgentType.OPENAI_FUNCTIONS,
            )

            # Execute a multi-step workflow using the GitHub Connector
            result = agent.invoke({
                "input": (
                    "Unlock this site and provide me with the data : https://www.amazon.com/dp/B0D2Q9397Y?th=1&psc=1"
                )
            })
            
            print(f"\nWorkflow Result:\n {result}")
        
        except Exception as e:
            print(f"ERROR: An unexpected error occurred: {e}")


      if __name__ == "__main__":
        main()
      ```
    </CodeGroup>
  </Step>
</Steps>
