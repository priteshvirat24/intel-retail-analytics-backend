> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何将 Bright Data 与 Smolagents 集成

> 此工具连接到 Bright Data，使您的代理能够爬取网站、搜索网络以及访问来自 LinkedIn、Amazon 和社交媒体等平台的结构化数据。

<Card title="正在构建 AI 初创公司？" cta="了解更多" href="https://brightdata.com/ai/ai-startups-program" icon="rocket-launch" iconType="duotone" arrow="true">
  您可能符合我们的初创计划资格。获得本文所介绍基础设施的全额资助访问权限（最高价值 \$20,000）。
</Card>

## 为什么在 Smolagents 中使用 Bright Data？

Bright Data for Smolagents 工具提供以下功能：

<AccordionGroup>
  <Accordion title="网络搜索">
    * **`search_tool`**\
      搜索 Google 并获取结构化搜索结果。此工具可以搜索网络并为您的查询返回相关结果。

    ```python theme={null}
    from smolagents import Tool

    web_search = Tool.from_space(
        "BrightData/brightdata-search-tool",
        name="search_tool",
        description="search the web"
    )
    ```
  </Accordion>

  <Accordion title="提取">
    * **`extract_tool`**\
      抓取网页并以 Markdown 格式提取内容。此工具可以绕过验证码和机器人检测，可靠地从任何网站提取数据。

    ```python theme={null}
    from smolagents import Tool

    extract = Tool.from_space(
        "BrightData/brightdata-scraper-tool",
        name="extract_tool",
        description="extract data from the web as markdown without getting blocked"
    )
    ```
  </Accordion>

  <Accordion title="结构化数据源">
    * **`data_feeds_tool`**\
      从各种平台检索结构化数据，包括 LinkedIn、Amazon、Instagram、Facebook、X (Twitter)、Zillow 等。

    ```python theme={null}
    from smolagents import Tool

    data_feeds = Tool.from_space(
        "BrightData/brightdata-dataset-tool",
        name="data_feeds_tool",
        description="extract structured data from the web"
    )
    ```

    支持的平台包括：

    * LinkedIn（个人资料和公司）
    * Amazon（产品和评论）
    * Instagram（个人资料、帖子、短视频、评论）
    * Facebook（帖子、市场列表、公司评论）
    * X/Twitter（帖子）
    * Zillow（房产列表）
    * Booking.com（酒店列表）
    * YouTube（视频）
    * 以及更多

    有关更多信息，请访问 [Bright Data 文档](/)。
  </Accordion>
</AccordionGroup>

## 如何将 Bright Data 与 Smolagents 集成？

<Steps>
  <Step title="获取您的 Bright Data API 密钥">
    * 登录您的 [Bright Data 仪表板](https://www.bright.cn/cp)���
    * 转到 [账户设置](https://www.bright.cn/cp/setting/users)。
    * [生成 API 密钥](/api-reference/authentication#how-do-i-authenticate-with-api-key%3F)（如果您还没有生成）。
  </Step>

  <Step title="安装">
    安装所需的包。**重要：** 从 2025 年 12 月 9 日起，这些特定版本必须强制安装以与 Smolagents 对齐：

    ```bash theme={null}
    pip install smolagents
    pip install --upgrade --force-reinstall "gradio_client<2.0.0" "gradio<6.0.0"
    ```
  </Step>

  <Step title="配置 API 密钥">
    将您的 Bright Data API 密钥设置为环境变量：

    ```bash theme={null}
    export BRIGHTDATA_API_KEY="your-api-key"
    ```

    或在您的 Python 代码中设置：

    ```python theme={null}
    import os
    os.environ["BRIGHTDATA_API_KEY"] = "your-api-key"
    ```
  </Step>

  <Step title="获取您的 Hugging Face API 令牌">
    使用 `InferenceClientModel` 时，您需要一个 Hugging Face 令牌进行身份验证：

    * 访问 [Hugging Face 设置 - 令牌](https://hf.co/settings/tokens)
    * 创建一个具有"调用无服务器推理 API"权限的新令牌
    * 将其设置为环境变量：

    ```bash theme={null}
        export HF_TOKEN="your-hf-token"
    ```

    或在初始化模型时直接传递它：

    ```python theme={null}
        model = InferenceClientModel(
            model_id="Qwen/Qwen3-Next-80B-A3B-Thinking",
            token="your-hf-token"
        )
    ```

    **注意：** 免费 Hugging Face 账户包括推理额度。升级到 PRO 以获得更高的速率限制。
  </Step>

  <Step title="使用">
    以下是如何将 Bright Data 工具与 Smolagents 一起使用的完整示例：

    ```python theme={null}
    from smolagents import CodeAgent, InferenceClientModel, Tool

    # Load Bright Data tools from Hugging Face Spaces
    web_search = Tool.from_space(
        "BrightData/brightdata-search-tool",
        name="search_tool",
        description="search the web"
    )

    extract = Tool.from_space(
        "BrightData/brightdata-scraper-tool",
        name="extract_tool",
        description="extract data from the web as markdown without getting blocked"
    )

    data_feeds = Tool.from_space(
        "BrightData/brightdata-dataset-tool",
        name="data_feeds_tool",
        description="extract structured data from the web"
    )

    # Initialize the model
    model = InferenceClientModel(model_id="Qwen/Qwen3-Next-80B-A3B-Thinking")

    # Create the agent with Bright Data tools
    agent = CodeAgent(tools=[web_search, extract, data_feeds], model=model)

    # Run the agent
    response = agent.run(
        "Improve this prompt, then search the web for it.",
        additional_args={'user_prompt': 'who is elon musk'}
    )

    print(response)
    ```
  </Step>
</Steps>

## 示例用例

<AccordionGroup>
  <Accordion title="网络研究">
    使用搜索工具在网络上查找信息：

    ```python theme={null}
    agent.run("Search for the latest developments in quantum computing")
    ```
  </Accordion>

  <Accordion title="数据提取">
    从网站抓取和提取内容：

    ```python theme={null}
    agent.run("Extract the main content from https://example.com/article")
    ```
  </Accordion>

  <Accordion title="竞争对手分析">
    从电商平台提取结构化数据：

    ```python theme={null}
    agent.run("Get product details and reviews for the top-rated laptops on Amazon")
    ```
  </Accordion>

  <Accordion title="社交媒体情报">
    从社交媒体平台检索数据：

    ```python theme={null}
    agent.run("Get the latest posts and engagement metrics from a LinkedIn company page")
    ```
  </Accordion>
</AccordionGroup>

## 获得最佳效果的提示

* **具体指定**您的提示以帮助代理理解您确切需要的数据
* **组合工具**执行复杂任务 - 代理可以一起使用搜索、提取和数据源工具

有关更高级的配置和详细的 API 文档，请访问 [Bright Data 的文档](/)。
