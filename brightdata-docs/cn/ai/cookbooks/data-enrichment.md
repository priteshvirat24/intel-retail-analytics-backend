> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 数据充实代理快速入门

> 在10分钟内使用 LangGraph + Bright Data 构建一个 AI 驱动的数据充实代理

<Card title="正在构建 AI 初创公司？" cta="了解更多" href="https://brightdata.com/ai/ai-startups-program" icon="rocket-launch" iconType="duotone" arrow="true">
  您可能符合我们的初创计划资格。获得本文所介绍基础设施的全额资助访问权限（最高价值 \$20,000）。
</Card>

构建一个 AI 代理，使用 [LangGraph](https://langchain-ai.github.io/langgraph/) 和 [Bright Data](https://www.bright.cn/) 自动研究和提取结构化数据。

<Info>
  本教程让你在不到 10 分钟内从零开始拥有一个工作的 AI 充实代理。
</Info>

## 你将构建什么

一个 AI 代理，它：

1. 接收研究主题和 JSON 模式作为输入（例如："来自纽约的 B2B 企业 CTO"、"Stripe 支付公司"、"可再生能源技术的历史"）
2. 使用 **Bright Data SERP API** 搜索网络（真实搜索结果、地理定位）
3. 使用 **Bright Data Web Unlocker** 爬取网站（绕过反爬虫措施）
4. 使用 LLM 提取和结构化数据
5. 验证并返回与你的模式匹配的结构化 JSON

## 前提条件

* 一个 [Bright Data 账户](https://www.bright.cn/?hs_signup=1\&utm_source=docs)，具有来自 [仪表板](https://www.bright.cn/cp/api_tokens) 的 API 密钥
* 一个 [Anthropic](https://console.anthropic.com/) 或 [OpenAI](https://platform.openai.com/signup) API 密钥
* Python 3.10+

***

## 第 1 步：安装依赖

```bash theme={null}
pip install langgraph langchain-brightdata langchain-anthropic
```

***

## 第 2 步：设置环境变量

获取你的 API 密钥：

* [Bright Data API 密钥](/api-reference/authentication#how-do-i-generate-a-new-api-key) - 从你的仪表板生成
* [Anthropic API 密钥](https://console.anthropic.com/settings/keys) - 从控制台获取

```bash theme={null}
export BRIGHT_DATA_API_KEY="your-bright-data-api-key"
export ANTHROPIC_API_KEY="your-anthropic-api-key"
```

***

## 第 3 步：创建充实代理

创建一个名为 `enrichment_agent.py` 的文件，并分三部分构建它：

### 3.1：导入和状态定义

定义代理的状态，以跟踪研究主题、模式、消息和提取的信息。

```python theme={null}
"""Simple data enrichment agent using LangGraph + Bright Data."""

import json
from dataclasses import dataclass, field
from typing import Any, Annotated, List, Optional

from langchain_anthropic import ChatAnthropic
from langchain_brightdata import BrightDataSERP, BrightDataUnlocker
from langchain_core.messages import AIMessage, HumanMessage, BaseMessage
from langchain_core.tools import tool
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode


# Agent state tracks topic, schema, conversation history, and final output
@dataclass
class AgentState:
    """State for the enrichment agent."""
    topic: str                                                              # Research topic
    extraction_schema: dict[str, Any]                                       # JSON schema for output
    messages: Annotated[List[BaseMessage], add_messages] = field(default_factory=list)  # Chat history
    info: Optional[dict[str, Any]] = None                                   # Extracted result
```

### 3.2：工具定义

配置 Bright Data 工具用于网络搜索和内容爬取。

```python theme={null}
# --- Tools ---

# SERP tool: Searches Google and returns structured results
serp_tool = BrightDataSERP(
    search_engine="google",
    country="us",
    language="en",
    results_count=5,
    parse_results=True,
)

# Unlocker tool: Scrapes any URL, bypassing anti-bot protection
unlocker_tool = BrightDataUnlocker(
    data_format="markdown",
)


@tool
async def search(query: str) -> str:
    """Search the web for information about a topic."""
    results = await serp_tool.ainvoke(query)
    return json.dumps(results, indent=2)


@tool
async def scrape_website(url: str) -> str:
    """Scrape and extract content from a specific URL."""
    content = await unlocker_tool.ainvoke(url)
    return str(content)[:20000]  # Limit content to avoid token overflow


tools = [search, scrape_website]
```

### 3.3：代理图和执行

构建编排搜索 → 爬取 → 提取的 LangGraph 工作流。

```python theme={null}
# --- Agent ---

# System prompt instructs the LLM on its research task
SYSTEM_PROMPT = """You are a research agent. Your task is to gather information about a topic and extract structured data.

You have access to these tools:
- search: Search the web for information
- scrape_website: Get content from a specific URL
- submit_info: Call this when you have gathered all the required information

Research topic: {topic}

Required information schema:
{schema}

Search for relevant information, scrape important pages, then call submit_info with the extracted data."""


def create_agent():
    """Create the enrichment agent graph."""
    llm = ChatAnthropic(model="claude-sonnet-4-20250514")

    async def call_model(state: AgentState) -> dict:
        """Call the LLM to decide next action or submit results."""
        prompt = SYSTEM_PROMPT.format(
            topic=state.topic,
            schema=json.dumps(state.extraction_schema, indent=2)
        )
        messages = [HumanMessage(content=prompt)] + list(state.messages)

        # Dynamic tool for structured output submission
        info_tool = {
            "name": "submit_info",
            "description": "Submit the extracted information when done researching.",
            "parameters": state.extraction_schema,
        }

        model = llm.bind_tools(tools + [info_tool])
        response = await model.ainvoke(messages)

        # Check if agent is submitting final info
        info = None
        if hasattr(response, 'tool_calls') and response.tool_calls:
            for tc in response.tool_calls:
                if tc["name"] == "submit_info":
                    info = tc["args"]
                    break

        return {"messages": [response], "info": info}

    def route(state: AgentState) -> str:
        """Route: end if info submitted, else continue tool loop."""
        if state.info:
            return "__end__"
        if not state.messages:
            return "agent"

        last_msg = state.messages[-1]
        if isinstance(last_msg, AIMessage) and hasattr(last_msg, 'tool_calls') and last_msg.tool_calls:
            for tc in last_msg.tool_calls:
                if tc["name"] == "submit_info":
                    return "__end__"
            return "tools"
        return "agent"

    # Build the graph: agent ↔ tools loop until info is extracted
    graph = StateGraph(AgentState)
    graph.add_node("agent", call_model)
    graph.add_node("tools", ToolNode(tools))
    graph.add_edge("__start__", "agent")
    graph.add_conditional_edges("agent", route)
    graph.add_edge("tools", "agent")

    return graph.compile()


async def enrich(topic: str, schema: dict) -> dict:
    """Run the enrichment agent and return structured data."""
    agent = create_agent()
    result = await agent.ainvoke({
        "topic": topic,
        "extraction_schema": schema,
    })
    return result.get("info", {})


# --- Example Usage ---
if __name__ == "__main__":
    import asyncio

    schema = {
        "type": "object",
        "properties": {
            "company_name": {"type": "string"},
            "industry": {"type": "string"},
            "headquarters": {"type": "string"},
            "founded": {"type": "string"},
            "key_products": {"type": "array", "items": {"type": "string"}},
        },
        "required": ["company_name", "industry"]
    }

    result = asyncio.run(enrich("Stripe payments company", schema))
    print(json.dumps(result, indent=2))
```

***

## 第 4 步：运行代理

```bash theme={null}
python enrichment_agent.py
```

**预期输出：**

```json theme={null}
{
  "company_name": "Stripe",
  "industry": "Financial Technology / Payments",
  "headquarters": "San Francisco, California",
  "founded": "2010",
  "key_products": [
    "Stripe Payments",
    "Stripe Billing",
    "Stripe Connect",
    "Stripe Atlas"
  ]
}
```

***

## 工作原理

1. **代理**接收主题和模式，决定搜索内容
2. **搜索**使用 Bright Data SERP API 获取真实搜索结果
3. **爬取**使用 Bright Data Web Unlocker 获取页面内容
4. **代理**分析内容，继续研究或提交信息
5. **输出**是与你的模式匹配的结构化 JSON

***

## 自定义示例

### 不同的提取模式

```python theme={null}
# Extract competitor information
competitor_schema = {
    "type": "object",
    "properties": {
        "competitors": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "market_position": {"type": "string"},
                    "key_differentiator": {"type": "string"}
                }
            }
        }
    }
}

result = await enrich("Stripe competitors in payment processing", competitor_schema)
```

### 地理定位搜索

```python theme={null}
serp_tool = BrightDataSERP(
    search_engine="google",
    country="de",      # Germany
    language="de",     # German
    results_count=10,
)
```

### 使用 OpenAI 代替 Anthropic

```python theme={null}
from langchain_openai import ChatOpenAI

# Replace the LLM initialization
llm = ChatOpenAI(model="gpt-4o")
```

***

## 后续步骤

<CardGroup cols={2}>
  <Card title="LinkedIn 爬取" icon="linkedin" href="/cn/api-reference/scrapers/social-media-apis/linkedin">
    添加 LinkedIn 档案充实
  </Card>

  <Card title="LangChain 集成" icon="link" href="/integrations/langchain">
    完整的 langchain-brightdata 文档
  </Card>
</CardGroup>

## 源代码

<Card title="GitHub 仓库" icon="github" href="https://github.com/brightdata/ai-data-enrichment-agent">
  完整源代码和其他示例
</Card>

<Check>
  你现在拥有一个 AI 驱动的数据充实代理！自定义模式以提取你需要的任何结构化数据。
</Check>
