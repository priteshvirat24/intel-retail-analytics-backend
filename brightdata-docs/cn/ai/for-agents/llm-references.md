> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# LLM友好的文档参考

> Bright Data 全部文档的纯文本和机器可读版本 - 为 AI 代理、RAG 管道和 LLM 上下文注入而构建。

## 概述

Bright Data 发布两个遵循 [llms.txt 标准](https://llmstxt.org) 的机器可读文档文件：

| 文件              | URL                                                   | 最适合             |
| --------------- | ----------------------------------------------------- | --------------- |
| `llms.txt`      | [`docs.brightdata.com/llms.txt`](/llms.txt)           | 代理感知、导航、检索路由    |
| `llms-full.txt` | [`docs.brightdata.com/llms-full.txt`](/llms-full.txt) | RAG 管道、上下文注入、微调 |

***

## llms.txt - 文档索引

`llms.txt` 是 Bright Data 全部文档页面的结构化、markdown 格式化索引 - 每个页面一个条目，包含简短描述和直接链接。

**格式：**

```markdown theme={null}
# Bright Data Docs

## Docs

- [Agent Web Access](/ai/agents.md): Complete web infrastructure for AI agents
- [SERP API Introduction](/scraping-automation/serp-api/introduction.md): Real-time search results
- [Web Unlocker](/scraping-automation/web-unlocker/introduction.md): Bypass bot detection
...
```

注意每个链接都指向页面的 `.md` 版本 - 纯净 markdown，无 HTML。

**何时使用：**

* 加载到代理的系统提示中以获得完整的产品认知
* 向检索系统提供用于决定获取哪些文档页面
* 为编码代理提供可用产品的地图

```bash theme={null}
# 快速预览
curl https://docs.brightdata.com/llms.txt | head -40

# 下载以供离线使用
curl -o brightdata-llms.txt https://docs.brightdata.com/llms.txt
```

***

## llms-full.txt - 完整文档

`llms-full.txt` 包含单个文件中 Bright Data 全部文档的完整文本 - 纯净 markdown，无 HTML，无导航界面。

**何时使用：**

* 在 Bright Data 文档上构建 RAG 管道
* 将完整产品知识注入到长上下文模型（Gemini 1.5 Pro、Claude 等）
* 创建微调或评估数据集
* 为代理提供完整的离线参考

```bash theme={null}
# 下载
curl -o brightdata-llms-full.txt https://docs.brightdata.com/llms-full.txt
```

<Warning>
  `llms-full.txt` 体积较大。对于实时代理会话，先加载 `llms.txt` 并按需获取特定页面的方式更节省 token。
</Warning>

***

## 加载到你的代理

<Tabs>
  <Tab title="Claude Code">
    在提示中直接引用该文件 - Claude Code 将获取并读取它：

    ```
    Please read https://docs.brightdata.com/llms.txt to understand the available
    Bright Data products, then help me choose the right API for scraping Amazon product pages.
    ```

    或将其保存为项目上下文文件：

    ```bash theme={null}
    mkdir -p .claude
    curl -o .claude/brightdata-docs.txt https://docs.brightdata.com/llms.txt
    ```

    然后在你的 CLAUDE.md 或系统提示中引用它：

    ```markdown theme={null}
    # 项目上下文
    查看 .claude/brightdata-docs.txt 获取完整的 Bright Data 产品参考。
    ```
  </Tab>

  <Tab title="Cursor / Windsurf">
    添加为项目规则文件，以便你的代理自动在上下文中具有它：

    ```bash theme={null}
    # 保存到项目规则目录
    curl -o .cursor/rules/brightdata.md https://docs.brightdata.com/llms.txt
    # 或者用于 Windsurf：
    curl -o .windsurf/rules/brightdata.md https://docs.brightdata.com/llms.txt
    ```

    现在每个 Cursor Composer 或 Windsurf Cascade 会话都内置了 Bright Data 产品认知。
  </Tab>

  <Tab title="RAG 管道">
    ```python theme={null}
    import httpx
    from langchain.text_splitter import MarkdownTextSplitter

    # 获取完整文档
    response = httpx.get("https://docs.brightdata.com/llms-full.txt")
    docs_content = response.text

    # 分割成块
    splitter = MarkdownTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.create_documents([docs_content])

    # 添加到你的向量存储
    vectorstore.add_documents(chunks)
    ```
  </Tab>

  <Tab title="OpenAI / 自定义 LLM">
    ```python theme={null}
    import httpx

    # 获取索引
    llms_txt = httpx.get("https://docs.brightdata.com/llms.txt").text

    messages = [
        {
            "role": "system",
            "content": f"""You are a helpful assistant with expertise in Bright Data's web data APIs.

    Here is the full index of available documentation:
    {llms_txt}

    Use this to understand which products and APIs are available, then fetch
    specific pages when you need full details on a product."""
        },
        {"role": "user", "content": "How do I scrape Amazon product pages?"}
    ]
    ```
  </Tab>
</Tabs>

***

## 按页面 markdown 访问

每个 Bright Data 文档页面也可作为纯净 markdown 获得。在任何页面 URL 后附加 `.md`：

| 页面                                                                  | Markdown URL                                                                           |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `docs.brightdata.com/ai/agents`                                     | [`docs.brightdata.com/ai/agents.md`](/ai/agents.md)                                    |
| `docs.brightdata.com/scraping-automation/web-unlocker/introduction` | [`...web-unlocker/introduction.md`](/scraping-automation/web-unlocker/introduction.md) |
| `docs.brightdata.com/ai/mcp-server/overview`                        | [`...mcp-server/overview.md`](/ai/mcp-server/overview.md)                              |

这让代理可以按需获取特定页面，而无需解析任何 HTML。

<Tip>
  **代理推荐模式：** 加载 `llms.txt` 以了解可用内容 → 识别相关页面 → 获取该页面的 `.md` URL 获得完整详情。这保持 token 使用效率，同时在需要时为代理提供完整信息。
</Tip>

***

## 后续步骤

<CardGroup cols={2}>
  <Card title="安装技能" icon="bolt" href="/ai/for-agents/skills">
    包含可运行脚本的预打包代理知识包
  </Card>

  <Card title="连接文档 MCP" icon="server" href="/ai/for-agents/docs-mcp">
    从代理工具内部将 Bright Data 文档查询为 MCP 资源
  </Card>
</CardGroup>
