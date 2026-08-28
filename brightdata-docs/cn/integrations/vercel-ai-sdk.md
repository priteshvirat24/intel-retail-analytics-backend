> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何将 Bright Data 集成到 Vercel AI SDK 中

Vercel AI SDK 是一个用于构建 AI 应用的 TypeScript 工具包，可与 React、Next.js、Vue、Svelte、Node.js 等框架搭配使用。它提供统一的 API，用于与不同的 AI 服务商交互，并包含用于流式输出、函数调用和构建对话式界面的实用工具。

## 入门步骤

<Steps>
  <Step title="先决条件">
    * Bright Data API Key
    * Node.js 20.18.1+
    * TypeScript（推荐）
  </Step>

  <Step title="安装">
    安装所需依赖：

    ```bash theme={null}
    npm install @brightdata/sdk ai zod
    ```
  </Step>

  <Step title="创建 Bright Data 工具">
    创建文件 `brightdata-tools.ts` 并写入以下内容：

    ```typescript brightdata-tools.ts expandable theme={null}
    import { tool, type Tool } from 'ai'
    import { z } from 'zod'
    import { bdclient } from '@brightdata/sdk'

    type BrightDataTools = 'scrape' | 'search' | 'amazonProduct'|'linkedinCollectProfiles'

    interface BrightDataToolsConfig {
    apiKey: string
    excludeTools?: BrightDataTools[]
    }

    export const brightDataTools = (
    config: BrightDataToolsConfig
    ): Partial<Record<BrightDataTools, Tool>> => {
    const client = new bdclient({ 
    apiKey: config.apiKey,
    autoCreateZones: true
    })

    const tools: Partial<Record<BrightDataTools, Tool>> = {
    scrape: tool({
      description:
        'Scrape website content and return it in clean markdown format. Bypasses anti-bot protection and CAPTCHAs.',
      inputSchema: z.object({
        url: z
          .string()
          .url()
          .describe('The URL of the website to scrape'),
        country: z
          .string()
          .length(2)
          .optional()
          .describe('Two-letter country code for proxy location (e.g., "us", "gb", "de")'),
      }),
      execute: async ({ url, country }) => {
        try {
          const result = await client.scrape(url, {
            dataFormat: 'markdown',
            format: 'raw',
            country: country?.toLowerCase(),
          })
          return result
        } catch (error) {
          return `Error scraping ${url}: ${String(error)}`
        }
      },
    }),

    search: tool({
      description:
        'Search the web using Google, Bing, or Yandex. Returns search results with anti-bot protection bypass.',
      inputSchema: z.object({
        query: z
          .string()
          .describe('The search query'),
        searchEngine: z
          .enum(['google', 'bing', 'yandex'])
          .optional()
          .default('google')
          .describe('Search engine to use'),
        country: z
          .string()
          .length(2)
          .optional()
          .describe('Two-letter country code for localized results'),
        dataFormat: z
          .enum(['html', 'markdown'])
          .optional()
          .default('markdown')
          .describe('Format of returned search results'),
      }),
      execute: async ({ query, searchEngine, country, dataFormat }) => {
        try {
          const result = await client.search(query, {
            searchEngine,
            dataFormat,
            format: 'raw',
            country: country?.toLowerCase(),
          })
          return result
        } catch (error) {
          return `Error searching for "${query}": ${String(error)}`
        }
      },
    }),

    amazonProduct: tool({
      description:
        'Get detailed Amazon product information including price, ratings, reviews, and specifications. Requires a valid Amazon product URL.',
      inputSchema: z.object({
        url: z
          .string()
          .url()
          .describe('Amazon product URL (must contain /dp/ or /gp/product/)'),
        zipcode: z
          .string()
          .optional()
          .describe('ZIP code for location-specific pricing and availability'),
      }),
      execute: async ({ url, zipcode }) => {
        try {
          const result = await client.datasets.amazon.collectProducts(
            [{ url, zipcode }],
            { 
              format: 'json',
              async: false 
            }
          )
          return JSON.stringify(result, null, 2)
        } catch (error) {
          return `Error fetching Amazon product data: ${String(error)}`
        }
      },
    }),

    linkedinCollectProfiles: tool({
        description:
          'Fetch LinkedIn profile data for one or more LinkedIn profile URLs. Returns detailed information including work experience, education, skills, and contact information.',
        inputSchema: z.object({
          urls: z
            .array(z.string().url())
            .min(1)
            .describe('Array of LinkedIn profile URLs to collect data from (e.g., ["https://www.linkedin.com/in/example"])'),
          format: z
            .enum(['json', 'jsonl'])
            .optional()
            .default('json')
            .describe('Output format for the results'),
        }),
        execute: async ({ urls, format }) => {
          try {
            const result = await client.datasets.linkedin.collectProfiles(
              urls,
              {
                format: format || 'json',
                async: false
              }
            )
            return JSON.stringify(result, null, 2)
          } catch (error) {
            return `Error fetching LinkedIn profiles: ${String(error)}`
          }
        },
      }),
    }

    // Remove excluded tools
    for (const toolName in tools) {
    if (config.excludeTools?.includes(toolName as BrightDataTools)) {
      delete tools[toolName as BrightDataTools]
    }
    }

    return tools
    }
    ```
  </Step>

  <Step title="使用示例">
    <Tabs>
      <Tab title="Next.js App Router">
        创建一个可用于任意 AI 提供商的 API 路由：

        ```typescript app/api/chat/route.ts theme={null}
        import { openai } from '@ai-sdk/openai'
        import { streamText, stepCountIs } from 'ai'
        import { brightDataTools } from '@/lib/brightdata-tools'

        export const maxDuration = 60

        export async function POST(req: Request) {
          const { messages } = await req.json()

          const tools = brightDataTools({
            apiKey: process.env.BRIGHTDATA_API_KEY!,
          })

          const result = streamText({
            model: openai('gpt-4o'),
            messages,
            tools,
            stopWhen: stepCountIs(10),
          })

          return result.toDataStreamResponse()
        }
        ```

        然后在你的组件中使用它：

        ```typescript app/page.tsx theme={null}
        'use client'

        import { useChat } from 'ai/react'

        export default function Chat() {
          const { messages, input, handleInputChange, handleSubmit } = useChat()

          return (
            <div className="flex flex-col h-screen">
              <div className="flex-1 overflow-y-auto p-4">
                {messages.map((m) => (
                  <div key={m.id} className="mb-4">
                    <strong>{m.role === 'user' ? 'You: ' : 'AI: '}</strong>
                    {m.content}
                  </div>
                ))}
              </div>
              <form onSubmit={handleSubmit} className="p-4 border-t">
                <input
                  value={input}
                  onChange={handleInputChange}
                  placeholder="Try: 'Scrape https://example.com' or 'Search for best laptops 2024'"
                  className="w-full p-2 border rounded"
                />
              </form>
            </div>
          )
        }
        ```
      </Tab>

      <Tab title="Node.js Script">
        ```typescript script.ts theme={null}
        import { anthropic } from '@ai-sdk/anthropic'
        import { generateText, stepCountIs } from 'ai'
        import { brightDataTools } from './brightdata-tools'

        async function main() {
          const tools = brightDataTools({
            apiKey: process.env.BRIGHTDATA_API_KEY!,
          })

          // Example 1: Scrape a website
          console.log('=== Example 1: Web Scraping ===')
          const scrapeResult = await generateText({
            model: anthropic('claude-3-5-sonnet-20241022'),
            tools,
            stopWhen: stepCountIs(10),
            prompt: 'Scrape https://news.ycombinator.com and summarize the top 5 stories',
          })
          console.log(scrapeResult.text)

          // Example 2: Web search
          console.log('\n=== Example 2: Web Search ===')
          const searchResult = await generateText({
            model: anthropic('claude-3-5-sonnet-20241022'),
            tools,
            stopWhen: stepCountIs(10),
            prompt: 'Search for the latest JavaScript frameworks and tell me about the top 3',
          })
          console.log(searchResult.text)

          // Example 3: Amazon product research
          console.log('\n=== Example 3: Amazon Product ===')
          const amazonResult = await generateText({
            model: anthropic('claude-3-5-sonnet-20241022'),
            tools,
            stopWhen: stepCountIs(10),
            prompt: 'Get details about this product: https://www.amazon.com/dp/B0D2Q9397Y and tell me if it\'s worth buying',
          })
          console.log(amazonResult.text)
        }

        main()
        ```
      </Tab>

      <Tab title="排除特定工具">
        ```typescript theme={null}
        import { openai } from '@ai-sdk/openai'
        import { streamText } from 'ai'
        import { brightDataTools } from './brightdata-tools'

        // Only include scrape and search, exclude Amazon tools
        const tools = brightDataTools({
          apiKey: process.env.BRIGHTDATA_API_KEY!,
          excludeTools: ['amazonProduct'],
        })

        const result = streamText({
          model: openai('gpt-4o'),
          messages: [
            { role: 'user', content: 'Scrape https://example.com' }
          ],
          tools,
        })
        ```
      </Tab>

      <Tab title="高级：多数据集">
        使用 LinkedIn 和 Instagram 扩展工具：

        ```typescript brightdata-tools-extended.ts theme={null}
        import { tool } from 'ai'
        import { z } from 'zod'
        import { bdclient } from '@brightdata/sdk'

        export const brightDataExtendedTools = (apiKey: string) => {
          const client = new bdclient({ apiKey, autoCreateZones: true })

          return {
            linkedinProfile: tool({
              description: 'Get detailed LinkedIn profile information',
              inputSchema: z.object({
                url: z.string().url().describe('LinkedIn profile URL'),
              }),
              execute: async ({ url }) => {
                try {
                  const result = await client.datasets.linkedin.collectProfiles(
                    [url],
                    { format: 'json', async: false }
                  )
                  return JSON.stringify(result, null, 2)
                } catch (error) {
                  return `Error: ${String(error)}`
                }
              },
            }),

            linkedinJobs: tool({
              description: 'Search for LinkedIn job postings by location and keyword',
              inputSchema: z.object({
                location: z.string().describe('Job location (e.g., "New York, NY")'),
                keyword: z.string().optional().describe('Job title or keyword'),
                country: z.string().length(2).optional().describe('Country code'),
              }),
              execute: async ({ location, keyword, country }) => {
                try {
                  const result = await client.datasets.linkedin.discoverJobs(
                    [{ location, keyword, country }],
                    { format: 'json' }
                  )
                  return JSON.stringify(result, null, 2)
                } catch (error) {
                  return `Error: ${String(error)}`
                }
              },
            }),

            instagramProfile: tool({
              description: 'Get Instagram profile information and recent posts',
              inputSchema: z.object({
                url: z.string().url().describe('Instagram profile URL'),
              }),
              execute: async ({ url }) => {
                try {
                  const result = await client.datasets.instagram.collectProfiles(
                    [url],
                    { format: 'json', async: false }
                  )
                  return JSON.stringify(result, null, 2)
                } catch (error) {
                  return `Error: ${String(error)}`
                }
              },
            }),
          }
        }
        ```
      </Tab>
    </Tabs>
  </Step>
</Steps>

## 示例输出

### 抓取示例

**用户输入：** "Scrape [https://example.com](https://example.com) and tell me what it's about"

**AI 回复：**

```
I've scraped the website. Here's what I found:

# Example Domain

This domain is for use in illustrative examples in documents. You may use this
domain in literature without prior coordination or asking for permission.

The website appears to be a placeholder domain used for documentation and
examples. It's maintained by IANA (Internet Assigned Numbers Authority) and
serves as a standard example domain that can be referenced in documentation
without needing permission.

```

### 搜索示例

**用户输入：** "Search for best mechanical keyboards 2024"

**AI 回复：**

```

I found several highly-rated mechanical keyboards for 2024:

1. **Keychron Q1 Pro** - A premium 75% layout keyboard with hot-swappable
   switches, wireless connectivity, and excellent build quality. Price around $200.

2. **Wooting 60HE** - Features analog switches that allow for adjustable
   actuation points and rapid trigger technology. Popular among gamers.

3. **GMMK Pro** - A versatile 75% gasket-mounted keyboard with extensive
   customization options and strong community support.

All three offer different features depending on whether you prioritize gaming,
typing, or customization.

```

### 亚马逊产品示例

**用户输入：** "Get information about Amazon product B0D2Q9397Y"

**AI 回复：**

```

I've retrieved the product information:

**Product:** Logitech MX Master 3S Wireless Mouse
**Price:** $99.99
**Rating:** 4.6/5 stars (8,234 reviews)
**Key Features:**

* 8K DPI sensor for precise tracking
* Quiet clicks technology
* USB-C charging
* Multi-device connectivity (up to 3 devices)
* Customizable buttons

The product has excellent reviews, with users praising its ergonomics and
productivity features. However, some note it's on the pricier side. It's
particularly popular among creative professionals and developers.

```

## 可用工具

| 工具                        | 描述                      | 使用场景           |
| ------------------------- | ----------------------- | -------------- |
| `scrape`                  | 抓取任意网站并返回 markdown 内容   | 内容提取、监控、数据采集   |
| `search`                  | 搜索 Google、Bing 或 Yandex | 研究、竞品分析、趋势监控   |
| `amazonProduct`           | 获取亚马逊产品详情               | 价格监控、产品研究、产品对比 |
| `linkedinCollectProfiles` | 获取 LinkedIn 个人资料        | 数据增强、人员研究      |

## 更多数据集工具

Bright Data SDK 支持更多可集成的数据集：

* **LinkedIn**：个人资料、公司、职位、帖子
* **Instagram**：个人资料、帖子、Reels、评论
* **Facebook**：帖子、Marketplace、活动、评论
* **Twitter/X**：帖子与个人资料
* **TikTok**：视频、个人资料、评论
* **Google Maps**：评论、商家信息
* **电商**：Walmart、eBay、Best Buy、Etsy、Zara

更多数据集请参考\
[Bright Data SDK 文档](https://github.com/brightdata/bright-data-sdk-js)。

## 最佳实践

1. **错误处理**：始终使用 try-catch 包裹工具调用
2. **速率限制**：多次请求时注意 API 限速
3. **数据格式**：抓取时使用 `markdown` 格式以获得更干净的内容
4. **异步操作**：处理大型数据集时使用 `async: true` 避免超时
5. **地域定向**：需要本地化结果时可指定国家代码

## 环境变量

```bash .env.local theme={null}
BRIGHTDATA_API_KEY=your_api_key_here
```

从 [Bright Data Dashboard](https://www.bright.cn/cp) 获取你的 API Key。
