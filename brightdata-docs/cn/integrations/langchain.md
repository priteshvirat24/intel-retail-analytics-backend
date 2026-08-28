> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 LangChain 中设置 Bright Data

将 Bright Data 与 LangChain 集成，可为基于 LLM 的代理提供可靠、匿名且可扩展的网页访问，以实现真实世界的应用。\
您可以通过使用官方 LangChain 集成的 `langchain-brightdata` Python 包来实现，其中包括对以下内容的支持：

* **BrightDataSERP** - Bright Data 提供强大的 SERP API，可让您查询搜索引擎（Google、Bing、DuckDuckGo、Yandex），支持地理定位和高级自定义选项，特别适合需要实时网页信息的 AI 代理。
* **BrightDataUnlockerAPI** - Bright Data 提供强大的 Web Unlocker API，可访问可能受到反爬虫措施、地理限制或其他访问限制的网站，对于需要可靠网页内容提取的 AI 代理非常有用。
* **BrightDataWebScraperAPI** - Bright Data 提供强大的 Scrapers，可从 100+ 个流行域中提取结构化数据，包括 Amazon 产品详情、LinkedIn 个人资料等，非常适合需要可靠结构化网页数据的 AI 代理。

或者使用 [**Bright Data 的 MCP（模型上下文协议）**](/cn/mcp-server/overview#configuration) —— 一个本地服务器，提供各种爬取和自动化工具。虽然不属于 `langchain-brightdata` 包的一部分，但可以通过 LangChain 的 `Tool` 或 `RequestsWrapper` 手动集成。

## 如何将 Bright Data 与 LangChain 集成

<Steps>
  <Step title="获取您的 Bright Data API Key">
    * 登录您的 [Bright Data 控制面板](https://www.bright.cn/cp)。
    * 转到 [账户设置](https://www.bright.cn/cp/setting/users)。
    * 如果尚未生成，请 [生成 API Key](/cn/api-reference/authentication#如何生成新的-api-key？)。
  </Step>

  <Step title="安装 Bright Data 集成">
    通过运行以下命令安装 LangChain 的 Bright Data 集成包：

    ```bash theme={null}
    pip install langchain-brightdata
    ```
  </Step>

  <Step title="设置环境变量">
    将您的 Bright Data API Key 设置为环境变量：

    ```python theme={null}
    import os
    os.environ["BRIGHT_DATA_API_KEY"] = "your-api-key"
    ```

    <Tip>
      或在初始化工具时直接传入：

      ```python theme={null}
      from langchain_bright_data import BrightDataSERP

      tool = BrightDataSERP(bright_data_api_key="your-api-key")
      ```
    </Tip>
  </Step>

  <Step title="选择您偏好的 Bright Data 工具">
    Bright Data + LangChain 集成目前支持：

    <Tabs>
      <Tab title="BrightDataSERP">
        <Tip>
          **API 文档**: [SERP API 文档](/cn/scraping-automation/serp-api/introduction)
        </Tip>

        收集支持地理定位的搜索引擎结果

        <CodeGroup>
          ```python Basic Usage theme={null}
          from langchain_brightdata import BrightDataSERP

          # Initialize the tool
          serp_tool = BrightDataSERP(
              bright_data_api_key="your-api-key"  # Optional if set in environment variables
          )

          # Run a basic search
          results = serp_tool.invoke("latest AI research papers")

          print(results)
          ```

          ```python Advanced Usage with Parameters theme={null}
          from langchain_brightdata import BrightDataSERP

          # Initialize with default parameters
          serp_tool = BrightDataSERP(
              bright_data_api_key="your-api-key",
              search_engine="google",  # Default
              country="us",  # Default
              language="en",  # Default
              results_count=10,  # Default
              parse_results=True,  # Get structured JSON results
          )

          # Use with specific parameters for this search
          results = serp_tool.invoke(
              {
                  "query": "best electric vehicles",
                  "country": "de",  # Get results as if searching from Germany
                  "language": "de",  # Get results in German
                  "search_type": "shop",  # Get shopping results
                  "device_type": "mobile",  # Simulate a mobile device
                  "results_count": 15,
              }
          )

          print(results)
          ```

          ```python Use within an agent theme={null}
          from langchain_brightdata import BrightDataSERP
          from langchain_google_genai import ChatGoogleGenerativeAI
          from langgraph.prebuilt import create_react_agent

          # Initialize the LLM
          llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key="your-api-key")

          # Initialize the Bright Data SERP tool
          serp_tool = BrightDataSERP(
              bright_data_api_key="your-api-key",
              search_engine="google",
              country="us",
              language="en",
              results_count=10,
              parse_results=True,
          )

          # Create the agent
          agent = create_react_agent(llm, [serp_tool])

          # Provide a user query
          user_input = "Search for 'best electric vehicles' shopping results in Germany in German using mobile."

          # Stream the agent's output step-by-step
          for step in agent.stream(
              {"messages": user_input},
              stream_mode="values",
          ):
              step["messages"][-1].pretty_print()
          ```
        </CodeGroup>
      </Tab>

      <Tab title="BrightDataUnblocker">
        <Tip>
          **API 文档**: [Web Unlocker API 文档](/cn/scraping-automation/web-unlocker/introduction)
        </Tip>

        访问任何公共网站，即使受机器人保护或地理限制。

        <CodeGroup>
          ```python Basic Usage theme={null}
          from langchain_brightdata import BrightDataUnlocker

          # Initialize the tool
          unlocker_tool = BrightDataUnlocker(
              bright_data_api_key="your-api-key"  # Optional if set in environment variables
          )

          # Access a webpage
          result = unlocker_tool.invoke("https://example.com")

          print(result)
          ```

          ```python Advanced Usage with Parameters theme={null}
          from langchain_brightdata import BrightDataUnlocker

          unlocker_tool = BrightDataUnlocker(
              bright_data_api_key="your-api-key",
          )

          # Access a webpage with specific parameters
          result = unlocker_tool.invoke(
              {
                  "url": "https://example.com/region-restricted-content",
                  "country": "gb",  # Access as if from Great Britain
                  "data_format": "html",  # Get content in markdown format
                  "zone": "unlocker",  # Use the unlocker zone
              }
          )

          print(result)
          ```

          ```python Use within an agent theme={null}
          from langchain_brightdata import BrightDataUnlocker
          from langchain_google_genai import ChatGoogleGenerativeAI
          from langgraph.prebuilt import create_react_agent

          # Initialize the LLM
          llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key="your-api-key")

          # Initialize the tool
          bright_data_tool = BrightDataUnlocker(bright_data_api_key="your-api-key")

          # Create the agent
          agent = create_react_agent(llm, [bright_data_tool])

          # Input URLs or prompt
          user_input = "Get the content from https://example.com/region-restricted-page - access it from GB"

          # Stream the agent's output step by step
          for step in agent.stream(
              {"messages": user_input},
              stream_mode="values",
          ):
              step["messages"][-1].pretty_print()
          ```
        </CodeGroup>
      </Tab>

      <Tab title="BrightDataWebScraperAPI">
        <Tip>
          **API 文档**: [Scrapers 文档](/cn/datasets/scrapers/scrapers-library/overview)
        </Tip>

        从 100 多个支持的域中提取结构化数据，如 Amazon、LinkedIn 等。

        <CodeGroup>
          ```python Basic Usage theme={null}
          from langchain_brightdata import BrightDataWebScraperAPI

          # Initialize the tool
          scraper_tool = BrightDataWebScraperAPI(
              bright_data_api_key="your-api-key"  # Optional if set in environment variables
          )

          # Extract Amazon product data
          results = scraper_tool.invoke(
              {"url": "https://www.amazon.com/dp/B08L5TNJHG", "dataset_type": "amazon_product"}
          )

          print(results)
          ```

          ```python Advanced Usage with Parameters theme={null}
          from langchain_brightdata import BrightDataWebScraperAPI

          # Initialize with default parameters
          scraper_tool = BrightDataWebScraperAPI(bright_data_api_key="your-api-key")

          # Extract Amazon product data with location-specific pricing
          results = scraper_tool.invoke(
              {
                  "url": "https://www.amazon.com/dp/B08L5TNJHG",
                  "dataset_type": "amazon_product",
                  "zipcode": "10001",  # Get pricing for New York City
              }
          )

          print(results)

          # Extract LinkedIn profile data
          linkedin_results = scraper_tool.invoke(
              {
                  "url": "https://www.linkedin.com/in/satyanadella/",
                  "dataset_type": "linkedin_person_profile",
              }
          )

          print(linkedin_results)
          ```

          ```python Use within an agent theme={null}
          from langchain_brightdata import BrightDataWebScraperAPI
          from langchain_google_genai import ChatGoogleGenerativeAI
          from langgraph.prebuilt import create_react_agent

          # Initialize the LLM
          llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key="your-api-key")

          # Initialize the Bright Data Scrapers tool
          scraper_tool = BrightDataWebScraperAPI(bright_data_api_key="your-api-key")

          # Create the agent with the tool
          agent = create_react_agent(llm, [scraper_tool])

          # Provide a user query
          user_input = "Scrape Amazon product data for https://www.amazon.com/dp/B0D2Q9397Y?th=1 in New York (zipcode 10001)."

          # Stream the agent's step-by-step output
          for step in agent.stream(
              {"messages": user_input},
              stream_mode="values",
          ):
              step["messages"][-1].pretty_print()
          ```
        </CodeGroup>
      </Tab>
    </Tabs>
  </Step>
</Steps>
