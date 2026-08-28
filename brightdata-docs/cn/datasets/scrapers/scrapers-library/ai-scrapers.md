> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# AI 网络爬虫文档

> 本文档提供了系统中集成的 AI 驱动网络爬虫概览。这些爬虫通过先进的 AI 模型响应用户提示，获取结构化回答，并附带相关元数据，如来源、引用和上下文信息。

# 概览

我们的平台支持以下 AI 爬虫：

* [ChatGPT](https://www.bright.cn/cp/scrapers/browse?domain=chatgpt.com)
* [Perplexity](https://www.bright.cn/cp/scrapers/browse?domain=perplexity.ai)
* [Gemini](https://www.bright.cn/cp/scrapers/browse?domain=gemini.google.com)
* [Grok](https://www.bright.cn/cp/scrapers/browse?domain=grok.com) <Badge color="red">暂不可用</Badge>
* [Google - AI 模式](https://www.bright.cn/cp/scrapers/browse?domain=google.com)
* [Copilot](https://www.bright.cn/cp/scrapers/browse?domain=copilot.microsoft.com)

每个爬虫都设计用于处理用户提示并返回丰富的回答，提供不同程度的详细信息和支持数据。

<div>
  ## AI 爬虫与传统 SERP 爬虫的区别
</div>

AI 机器人爬虫相比传统的 SERP（搜索引擎结果页）爬虫，更智能、高效。传统 SERP 爬虫通常需要从搜索结果页面提取原始 HTML，经常需要复杂的解析和维护；而 AI 机器人爬虫利用自然语言模型理解查询意图，并返回结构化、上下文丰富的答案。\
AI 机器人爬虫相比 SERP 爬虫的主要优势：

* ✅ 理解查询上下文并提供直接答案
* ✅ 包含引用、来源及丰富内容（如地图、产品链接）
* ✅ 对界面变化和搜索引擎更新更具适应性
* ✅ 通过官方 API 更容易集成
* ✅ 提供更佳用户体验，更干净且相关性高的结果

相比之下，SERP 爬虫仅限于表层数据，往往缺乏上下文，且可能违反搜索引擎服务条款。AI 机器人爬虫是现代可扩展的智能数据提取解决方案。

***

| 爬虫                                          | 简短描述                                  | 包含内容                                                                                                                                                                         |
| :------------------------------------------ | :------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ChatGPT 爬虫**                              | 使用 OpenAI ChatGPT 生成详细、对话式回答。         | <ul><li>超链接</li><li>引用（如可用）</li><li>产品推荐</li><li>嵌入地图数据</li><li>[可用国家](https://github.com/brightdata/answer-engines-country-codes/blob/main/chatgpt_countries.csv)</li></ul> |
| **Perplexity 爬虫**                           | 通过 Perplexity AI 提供简洁、来源明确的回答，适合研究用途。 | <ul><li>可验证的超链接引用</li><li>[可用国家](https://github.com/brightdata/answer-engines-country-codes/blob/main/perplexity_countries.csv)</li></ul>                                    |
| **Copilot 爬虫**                              | 使用微软 Copilot 提供带来源的上下文答案              | <ul><li>超链接引用</li><li>上下文解释</li><li>[可用国家](https://github.com/brightdata/answer-engines-country-codes/blob/main/copilot_countries.csv)</li></ul>                             |
| **Gemini 爬虫**                               | 通过 Google Gemini 提供信息丰富的回答，并可进行网页搜索   | <ul><li>基于网页的引用和来源</li><li>超链接引用（如可用）</li><li>[国家定位](https://github.com/brightdata/answer-engines-country-codes/blob/main/gemini_countries.csv)（欧洲国家不可用）</li></ul>           |
| **Google AI 爬虫**                            | 通过提示收集 Google AI 模式的搜索结果              | <ul><li>[可用国家](https://github.com/brightdata/answer-engines-country-codes/blob/main/google_aimode_countries.csv)</li></ul>                                                   |
| **Grok 爬虫** <Badge color="red">暂不可用</Badge> | 通过提示收集 Grok 搜索结果                      | <ul><li>超链接引用</li><li>[可用国家](https://github.com/brightdata/answer-engines-country-codes/blob/main/grok_countries.csv)</li></ul>                                              |

<Note>
  是否触发网络搜索由 Gemini 内部控制，当前无法通过爬虫强制启用或禁用。提示语的表述可能影响是否触发网页搜索。
</Note>
