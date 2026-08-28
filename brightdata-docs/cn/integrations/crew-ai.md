> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何将 Bright Data 集成到 CrewAI 中

> 将 Bright Data 集成到 CrewAI 中，实现强大的网页抓取、数据提取和搜索功能。

一套全面的 CrewAI 工具集，利用 Bright Data 强大的基础设施来执行网页抓取、数据提取和搜索操作。这些工具提供三种不同的能力：

### BrightDataDatasetTool

使用预构建的数据集，从热门数据源（Amazon、LinkedIn、Instagram 等）中提取结构化数据。

### BrightDataSearchTool

通过多种搜索引擎执行网页搜索，并支持地理定位和设备模拟。

### BrightDataUnlockerAPITool

在绕过机器人防护机制的情况下抓取任意网站内容。

## 开始使用的步骤

要有效使用 Bright Data 工具，请按照以下步骤操作：

<Steps>
  <Step title="获取 Bright Data API 密钥">
    * 登录你的 [Bright Data 仪表盘](https://www.bright.cn/cp)。
    * 前往 [账户设置](https://www.bright.cn/cp/setting/users)。
    * 如果你还没有 API 密钥，请 [生成一个 API 密钥](/cn/api-reference/authentication#how-do-i-authenticate-with-api-key%3F)。
  </Step>

  <Step title="安装 Bright Data 集成">
    通过以下命令安装 CrewAI 的 Bright Data 集成包，以及 `aiohttp` 和 `requests`：

    ```shell theme={null}
    pip install crewai[tools] aiohttp requests
    ```
  </Step>

  <Step title="设置环境变量">
    将你的 Bright Data API 密钥设置为环境变量：

    ```bash theme={null}
    export BRIGHT_DATA_API_KEY="your_api_key_here"
    export BRIGHT_DATA_ZONE="your_zone_here"
    ```
  </Step>

  <Step title="选择你需要的 Bright Data 工具">
    Bright Data + CrewAI 集成目前支持以下工具：

    <CodeGroup>
      ```python DatasetTool theme={null}
      # Dataset Tool - 提取 Amazon 商品数据
      from crewai_tools import BrightDataDatasetTool

      # 使用特定 dataset 和 URL 初始化
      tool = BrightDataDatasetTool(
          dataset_type="amazon_product",
          url="https://www.amazon.com/dp/B08QB1QMJ5/"
      )
      result = tool.run()
      ```

      ```python SearchTool theme={null}
      # Search Tool - 执行网页搜索
      from crewai_tools import BrightDataSearchTool

      # 使用搜索查询初始化
      tool = BrightDataSearchTool(
          query="latest AI trends 2025",
          search_engine="google",
          country="us"
      )
      result = tool.run()
      ```

      ```python UnlockerAPITool theme={null}
      # Web Unlocker API Tool - 抓取网站内容
      from crewai_tools import BrightDataWebUnlockerTool

      # 使用目标 URL 初始化
      tool = BrightDataWebUnlockerTool(
          url="https://example.com",
          data_format="markdown"
      )
      result = tool.run()
      ```
    </CodeGroup>
  </Step>
</Steps>

## 结论

通过将 Bright Data 工具集成到你的 CrewAI 代理中，你可以获得企业级的网页抓取和数据提取能力。这些工具能够处理复杂的挑战，如机器人防护、地理限制和数据解析，让你专注于构建自己的应用程序，而无需管理抓取基础设施。
