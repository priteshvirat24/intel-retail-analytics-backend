> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 LlamaIndex 中设置 Bright Data

该工具连接到 [Bright Data](https://www.bright.cn/)，使您的代理能够爬取网站、搜索网页，并从 LinkedIn、Amazon 及社交媒体等平台访问结构化数据。

Bright Data 工具提供强大的网页抓取功能，内置 CAPTCHA 解决和反爬虫检测规避，允许您可靠地从网页提取数据。

## 为什么在 LlamaIndex 中使用 Bright Data？

Bright Data 工具提供以下功能：

<AccordionGroup>
  <Accordion title="网页抓取">
    * **`scrape_as_markdown`**\
      抓取网页并将内容转换为 Markdown 格式。该工具可以绕过 CAPTCHA 和反爬虫检测。

    ```python theme={null}
    result = brightdata_tool.scrape_as_markdown("https://example.com")
    print(result.text)    
    ```
  </Accordion>

  <Accordion title="网页截图">
    * **`get_screenshot`**\
      截取网页并保存到文件。

    ```python theme={null}
    screenshot_path = brightdata_tool.get_screenshot(
        "https://example.com", output_path="example_screenshot.png"
    )
    ```
  </Accordion>

  <Accordion title="搜索引擎访问">
    * **`search_engine`**\
      搜索 Google、Bing 或 Yandex，并以 JSON 或 Markdown 格式获取结构化搜索结果。支持高级参数以进行更具体的搜索。

    ```python theme={null}
    search_results = brightdata_tool.search_engine(
        query="climate change solutions",
        engine="google",
        language="en",
        country_code="us",
        num_results=20,
    )
    print(search_results.text)
    ```
  </Accordion>

  <Accordion title="结构化网页数据提取">
    * **`web_data_feed`**\
      从多个平台获取结构化数据，包括 LinkedIn、Amazon、Instagram、Facebook、X (Twitter)、Zillow 等。

    ```python theme={null}
    linkedin_profile = brightdata_tool.web_data_feed(
        source_type="linkedin_person_profile",
        url="https://www.linkedin.com/in/username/",
    )
    print(linkedin_profile)

    amazon_product = brightdata_tool.web_data_feed(
        source_type="amazon_product", url="https://www.amazon.com/dp/B08N5KWB9H"
    )
    print(amazon_product)
    ```
  </Accordion>

  <Accordion title="高级配置">
    Bright Data 工具为特殊用例提供多种配置选项：

    ### 搜索引擎参数

    `search_engine` 函数支持高级参数，例如：

    * 语言定向（`language` 参数）
    * 国家/地区搜索（`country_code` 参数）
    * 不同搜索类型（图片、购物、新闻等）
    * 分页控制
    * 移动设备模拟
    * 地理位置定向
    * 酒店搜索参数

    ```python theme={null}
    results = brightdata_tool.search_engine(
        query="best hotels in paris",
        engine="google",
        language="fr",
        country_code="fr",
        search_type="shopping",
        device="mobile",
        hotel_dates="2025-06-01,2025-06-05",
        hotel_occupancy=2,
    )
    ```

    ### 支持的网页数据源

    `web_data_feed` 函数支持从以下平台获取结构化数据：

    * LinkedIn（个人资料和公司）
    * Amazon（产品和评价）
    * Instagram（个人资料、帖子、Reels、评论）
    * Facebook（帖子、市场列表、公司评价）
    * X/Twitter（帖子）
    * Zillow（房产列表）
    * Booking.com（酒店列表）
    * YouTube（视频）
    * ZoomInfo（公司资料）

    更多信息，请访问 [Bright Data 文档](/cn/)。
  </Accordion>
</AccordionGroup>

## 如何将 Bright Data 与 LlamaIndex 集成？

<Steps>
  <Step title="获取 Bright Data API Key">
    * 登录您的 [Bright Data 控制面板](https://www.bright.cn/cp)。
    * 转到 [账户设置](https://www.bright.cn/cp/setting/users)。
    * 如果尚未生成，请 [生成 API Key](/cn/api-reference/authentication#如何生成新的-api-key？)。
  </Step>

  <Step title="安装">
    安装所需的包：

    ```bash theme={null}
    pip install llama-index llama-index-core llama-index-tools-brightdata
    ```
  </Step>

  <Step title="使用方法">
    以下示例展示如何在 LlamaIndex 中使用 BrightDataToolSpec：

    ```python theme={null}
    llm = OpenAI(model="gpt-4o", api_key="your-api-key")

    brightdata_tool = BrightDataToolSpec(api_key="your-api-key", zone="unlocker")

    tool_list = brightdata_tool.to_tool_list()

    for tool in tool_list:
        tool.original_description = tool.metadata.description
        tool.metadata.description = "Bright Data web scraping tool"

    agent = OpenAIAgent.from_tools(tools=tool_list, llm=llm)

    query = (
        "Find and summarize the latest news about AI from major tech news sites"
    )
    tool_descriptions = "\n\n".join(
        [
            f"Tool Name: {tool.metadata.name}\nTool Description: {tool.original_description}"
            for tool in tool_list
        ]
    )

    query_with_descriptions = f"{tool_descriptions}\n\nQuery: {query}"

    response = agent.chat(query_with_descriptions)
    print(response)
    ```
  </Step>
</Steps>
