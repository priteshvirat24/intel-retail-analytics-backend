> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何使用 Haystack 集成 Bright Data

<Card title="正在构建 AI 初创公司？" cta="了解更多" href="https://brightdata.com/ai/ai-startups-program" icon="rocket-launch" iconType="duotone" arrow="true">
  您可能符合我们的初创计划资格。获得本文所介绍基础设施的全额资助访问权限（最高价值 \$20,000）。
</Card>

将 Bright Data 与 Haystack 集成可以为您的 RAG 管道和 AI 应用程序增强可靠、可扩展的网页数据提取功能，适用于真实场景。

`haystack-brightdata` Python 包是 Bright Data 的官方 Haystack 集成，包括对以下功能的支持：

* **Bright Data 网页爬虫** - 从 45+ 个支持的网站提取结构化数据，包括 Amazon、LinkedIn、Instagram、Facebook、TikTok、YouTube 等，使用 Bright Data 的数据集 API。
* **Bright Data SERP** - 查询搜索引擎（Google、Bing、Yahoo），支持地理定位和语言自定义，获取实时搜索结果。
* **Bright Data Unlocker** - 访问地理限制和机器人保护的网站，绕过验证码和反机器人措施，以多种格式提取内容。

## 如何使用 Haystack 集成 Bright Data

<Steps>
  <Step title="获取您的 Bright Data API 密钥">
    * 登录您的 [Bright Data 仪表板](https://www.bright.cn/cp)。
    * 进入 [账户设置](https://www.bright.cn/cp/setting/users)。
    * [生成 API 密钥](/api-reference/authentication#how-do-i-authenticate-with-api-key%3F)（如果您还没有的话）。
  </Step>

  <Step title="安装 Bright Data 集成">
    运行以下命令安装 Bright Data 的 Haystack 集成包：

    ```bash theme={null}
    pip install haystack-brightdata
    ```
  </Step>

  <Step title="设置环境变量">
    将您的 Bright Data API 密钥设置为环境变量：

    ```python theme={null}
    import os
    os.environ["BRIGHT_DATA_API_KEY"] = "your-api-key"
    ```
  </Step>

  <Step title="选择您首选的 Bright Data 组件">
    Bright Data + Haystack 集成目前支持：

    <Tabs>
      <Tab title="BrightDataWebScraper">
        <Tip>
          **API 参考**: [爬虫文档](/datasets/scrapers/scrapers-library/overview)
        </Tip>

        从 45+ 个支持的网站（包括电子商务、社交媒体和商业智能平台）提取结构化数据。

        <CodeGroup>
          ```python 基本用法 theme={null}
          from haystack_brightdata import BrightDataWebScraper
          import os

          # 设置您的 API 密钥
          os.environ["BRIGHT_DATA_API_KEY"] = "your-api-key"

          # 初始化爬虫
          scraper = BrightDataWebScraper()

          # 提取 Amazon 产品数��
          result = scraper.run(
              dataset="amazon_product",
              url="https://www.amazon.com/dp/B08N5WRWNW"
          )
          print(result["data"])
          ```

          ```python 高级用法 - LinkedIn 个人资料 theme={null}
          from haystack_brightdata import BrightDataWebScraper
          import os

          os.environ["BRIGHT_DATA_API_KEY"] = "your-api-key"

          scraper = BrightDataWebScraper()

          # 提取 LinkedIn 个人资料数据
          result = scraper.run(
              dataset="linkedin_person_profile",
              url="https://www.linkedin.com/in/example-profile/"
          )
          print(result["data"])

          # 提取 Instagram 个人资料数据
          result = scraper.run(
              dataset="instagram_profiles",
              url="https://www.instagram.com/username/"
          )
          print(result["data"])
          ```

          ```python 列出支持的数据集 theme={null}
          from haystack_brightdata import BrightDataWebScraper

          # 获取所有支持的数据集
          datasets = BrightDataWebScraper.get_supported_datasets()
          for dataset in datasets:
              print(f"{dataset['id']}: {dataset['description']}")

          # 获取特定数据集的信息
          info = BrightDataWebScraper.get_dataset_info("amazon_product")
          print(f"描述: {info['description']}")
          print(f"必需输入: {info['inputs']}")
          ```
        </CodeGroup>
      </Tab>

      <Tab title="BrightDataSERP">
        <Tip>
          **API 参考**: [SERP API 文档](/cn/scraping-automation/serp-api/introduction)
        </Tip>

        收集搜索引擎结果，支持地理定位和语言自定义。

        <CodeGroup>
          ```python 基本用法 theme={null}
          from haystack_brightdata import BrightDataSERP
          import os

          # 设置您的 API 密钥
          os.environ["BRIGHT_DATA_API_KEY"] = "your-api-key"

          # 初始化 SERP 组件
          serp = BrightDataSERP(
              default_search_engine="google",
              default_country="us",
              default_language="en"
          )

          # 执行搜索查询
          result = serp.run(
              query="machine learning tutorials",
              num_results=20,
              search_type="web"
          )
          print(result)
          ```

          ```python 带地理定位的高级用法 theme={null}
          from haystack_brightdata import BrightDataSERP
          import os

          os.environ["BRIGHT_DATA_API_KEY"] = "your-api-key"

          serp = BrightDataSERP()

          # 从不同国家以不同语言搜索
          result = serp.run(
              query="inteligencia artificial",
              country="es",
              language="es",
              num_results=10
          )
          print(result)
          ```
        </CodeGroup>
      </Tab>

      <Tab title="BrightDataUnlocker">
        <Tip>
          **API 参考**: [Web Unlocker 文档](/cn/scraping-automation/web-unlocker/introduction)
        </Tip>

        访问任何公共网站，即使它受到机器人保护或地理限制。

        <CodeGroup>
          ```python 基本用法 theme={null}
          from haystack_brightdata import BrightDataUnlocker
          import os

          # 设置您的 API 密钥
          os.environ["BRIGHT_DATA_API_KEY"] = "your-api-key"

          # 初始化 Web Unlocker
          unlocker = BrightDataUnlocker(default_output_format="markdown")

          # 访问网站并获取 markdown 格式的内容
          result = unlocker.run(
              url="https://example.com/restricted-content",
              output_format="markdown"
          )
          print(result["content"])
          ```

          ```python 带地理定位的高级用法 theme={null}
          from haystack_brightdata import BrightDataUnlocker
          import os

          os.environ["BRIGHT_DATA_API_KEY"] = "your-api-key"

          unlocker = BrightDataUnlocker()

          # 从特定国家访问
          result = unlocker.run(
              url="https://example.com",
              country="gb",
              output_format="html"
          )
          print(result)

          # 获取截图
          result = unlocker.run(
              url="https://example.com",
              output_format="screenshot"
          )
          # result 包含 base64 编码的截图
          ```
        </CodeGroup>
      </Tab>
    </Tabs>
  </Step>
</Steps>

## RAG 管道示例

### 产品数据 RAG 管道

构建一个检索增强生成 (RAG) 管道，使用 Bright Data 从 Amazon 提取产品数据并回答有关产品的问题：

```python theme={null}
import os
from haystack import Pipeline, Document
from haystack.components.builders import ChatPromptBuilder
from haystack.components.generators.chat import OpenAIChatGenerator
from haystack.components.embedders import OpenAIDocumentEmbedder, OpenAITextEmbedder
from haystack.components.retrievers.in_memory import InMemoryEmbeddingRetriever
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.dataclasses import ChatMessage
from haystack_brightdata import BrightDataWebScraper
import json

# 设置 API 密钥
os.environ["BRIGHT_DATA_API_KEY"] = "your-brightdata-api-key"
os.environ["OPENAI_API_KEY"] = "your-openai-api-key"

# 初始化组件
scraper = BrightDataWebScraper()
document_store = InMemoryDocumentStore()
docs_embedder = OpenAIDocumentEmbedder()
text_embedder = OpenAITextEmbedder()
retriever = InMemoryEmbeddingRetriever(document_store)
generator = OpenAIChatGenerator()

# 从多个 Amazon 产品爬取产品数据
product_urls = [
    "https://www.amazon.com/dp/B0DRWBJDLJ",
    "https://www.amazon.com/dp/B08B8M5JGN",
    "https://www.amazon.com/dp/B09WTTWH1R",
]

documents = []
for url in product_urls:
    result = scraper.run(dataset="amazon_product", url=url)

    # 解析响应
    if isinstance(result["data"], str):
        product_data = json.loads(result["data"])
    else:
        product_data = result["data"]

    if not isinstance(product_data, list):
        product_data = [product_data]

    for product in product_data:
        content_parts = [
            f"产品: {product.get('title', 'N/A')}",
            f"品牌: {product.get('brand', 'N/A')}",
            f"价格: ${product.get('final_price', 'N/A')} {product.get('currency', '')}",
            f"评级: {product.get('rating', 0)}/5",
            f"评论数: {product.get('reviews_count', 0)}",
        ]

        if product.get('description'):
            content_parts.append(f"描述: {product.get('description')}")

        if product.get('features'):
            features_text = '\n  - '.join(product.get('features', []))
            content_parts.append(f"特性:\n  - {features_text}")

        content = '\n'.join(content_parts)

        documents.append(Document(
            content=content,
            meta={
                "url": product.get('url', url),
                "title": product.get('title', ''),
                "price": product.get('final_price', 0),
                "rating": product.get('rating', 0),
            }
        ))

# 嵌入并存储文档
embeddings = docs_embedder.run(documents)
document_store.write_documents(embeddings["documents"])

# 使用 ChatPromptBuilder 创建 RAG 管道
messages = [
    ChatMessage.from_system("您是一位有帮助的购物助手。"),
    ChatMessage.from_user("""
背景:
{% for document in documents %}
    {{ document.content }}
{% endfor %}

问题: {{question}}
""")
]

prompt_builder = ChatPromptBuilder(template=messages)

# 构建并连接管道
pipe = Pipeline()
pipe.add_component("embedder", text_embedder)
pipe.add_component("retriever", retriever)
pipe.add_component("prompt_builder", prompt_builder)
pipe.add_component("llm", generator)

pipe.connect("embedder.embedding", "retriever.query_embedding")
pipe.connect("retriever", "prompt_builder.documents")
pipe.connect("prompt_builder", "llm")

# 询问关于产品的问题
question = "哪个产品的评级最高？"
response = pipe.run({
    "embedder": {"text": question},
    "prompt_builder": {"question": question}
})

print(f"答案: {response['llm']['replies'][0].text}")
```

### SERP + 网页内容 RAG 管道

使用 SERP API 查找相关网页，然后使用 Web Unlocker 提取内容用于 RAG 管道：

```python theme={null}
import os
from haystack import Pipeline, Document
from haystack.components.builders import ChatPromptBuilder
from haystack.components.generators.chat import OpenAIChatGenerator
from haystack.components.embedders import OpenAIDocumentEmbedder, OpenAITextEmbedder
from haystack.components.retrievers.in_memory import InMemoryEmbeddingRetriever
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.dataclasses import ChatMessage
from haystack_brightdata import BrightDataSERP, BrightDataUnlocker
import json

# 设置 API 密钥
os.environ["BRIGHT_DATA_API_KEY"] = "your-brightdata-api-key"
os.environ["OPENAI_API_KEY"] = "your-openai-api-key"

# 初始化组件
serp = BrightDataSERP()
unlocker = BrightDataUnlocker(default_output_format="markdown", zone="unblocker")
document_store = InMemoryDocumentStore()
docs_embedder = OpenAIDocumentEmbedder()
text_embedder = OpenAITextEmbedder()
retriever = InMemoryEmbeddingRetriever(document_store)
generator = OpenAIChatGenerator(model="gpt-4")

# 搜索信息
search_query = "生产中机器学习的最佳实践"
search_result = serp.run(query=search_query, num_results=5)
search_data = json.loads(search_result["results"])

# 从搜索结果中提取 URL
urls = []
for result in search_data.get("organic", [])[:5]:
    url = result.get("url") or result.get("link")
    if url:
        urls.append(url)

# 从每个 URL 获取内容
documents = []
for url in urls:
    try:
        result = unlocker.run(url=url, output_format="markdown")
        content = result["content"]
        documents.append(Document(
            content=content,
            meta={"url": url}
        ))
    except Exception as e:
        print(f"无法获取 {url}: {e}")

# 嵌入并存储文档
embeddings = docs_embedder.run(documents)
document_store.write_documents(embeddings["documents"])

# 创建 RAG 管道
messages = [
    ChatMessage.from_system("您是一位知识丰富的 AI 助手。"),
    ChatMessage.from_user("""
来自网��资源的背景:
{% for document in documents %}
    来源: {{ document.meta.url }}
    {{ document.content }}
{% endfor %}

问题: {{question}}
""")
]

prompt_builder = ChatPromptBuilder(template=messages)

pipe = Pipeline()
pipe.add_component("embedder", text_embedder)
pipe.add_component("retriever", retriever)
pipe.add_component("prompt_builder", prompt_builder)
pipe.add_component("llm", generator)

pipe.connect("embedder.embedding", "retriever.query_embedding")
pipe.connect("retriever", "prompt_builder.documents")
pipe.connect("prompt_builder", "llm")

# 提出问题
question = "在生产中部署 ML 模型的主要挑战是什么？"
response = pipe.run({
    "embedder": {"text": question},
    "prompt_builder": {"question": question}
})

print(f"答案: {response['llm']['replies'][0].text}")
```

## 支持的数据集

`BrightDataWebScraper` 组件支持 45+ 个数据集，涵盖多个类别：

| 类别            | 数据集                                                                                                                                                                                          |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **电子商务**      | amazon\_product, amazon\_product\_reviews, amazon\_product\_search, walmart\_product, walmart\_seller, ebay\_product, homedepot\_products, zara\_products, etsy\_products, bestbuy\_products |
| **LinkedIn**  | linkedin\_person\_profile, linkedin\_company\_profile, linkedin\_job\_listings, linkedin\_posts, linkedin\_people\_search                                                                    |
| **Instagram** | instagram\_profiles, instagram\_posts, instagram\_reels, instagram\_comments                                                                                                                 |
| **Facebook**  | facebook\_posts, facebook\_marketplace\_listings, facebook\_company\_reviews, facebook\_events                                                                                               |
| **TikTok**    | tiktok\_profiles, tiktok\_posts, tiktok\_shop, tiktok\_comments                                                                                                                              |
| **YouTube**   | youtube\_profiles, youtube\_videos, youtube\_comments                                                                                                                                        |
| **搜索与商务**     | google\_maps\_reviews, google\_shopping, google\_play\_store, apple\_app\_store, zillow\_properties\_listing, booking\_hotel\_listings                                                       |
| **商业智能**      | crunchbase\_company, zoominfo\_company\_profile                                                                                                                                              |
| **其他**        | github\_repository\_file, yahoo\_finance\_business, x\_posts, reddit\_posts                                                                                                                  |

<Tip>
  有关每个数据集及其所需参数的详细信息：

  ```python theme={null}
  from haystack_brightdata import BrightDataWebScraper

  # 列出所有数据集
  datasets = BrightDataWebScraper.get_supported_datasets()
  for dataset in datasets:
      print(f"{dataset['id']}: {dataset['description']}")
  ```
</Tip>

## 用例

Bright Data 的 Haystack 集成支持强大的用例：

* **电子商务智能**: 价格监测、产品数据提取和竞争分析
* **社交媒体分析**: 跨平台的内容监测和参与度分析
* **商业智能**: 公司研究和竞争格局分析
* **搜索分析**: 具有地理定位搜索结果的 SEO/SEM 研究
* **内容聚合**: 使用实时网页数据构建 RAG 管道
* **市场研究**: 访问地理限制内容��行全球研究
