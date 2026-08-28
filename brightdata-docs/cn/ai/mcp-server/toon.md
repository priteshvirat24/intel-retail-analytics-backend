> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# TOON 格式

> 了解如何使用面向令牌的对象记号法 (TOON) 来减少使用 MCP 数据时的令牌消耗

<Card title="正在构建 AI 初创公司？" cta="了解更多" href="https://brightdata.com/ai/ai-startups-program" icon="rocket-launch" iconType="duotone" arrow="true">
  您可能符合我们的初创计划资格。获得本文所介绍基础设施的全额资助访问权限（最高价值 \$20,000）。
</Card>

## 什么是 TOON？

**面向令牌的对象记号法 (TOON)** 是为 LLM 输入而设计的 JSON 数据模型的紧凑、人类可读的编码方式。它最小化令牌使用，同时保持完整的数据保真度，是处理大量结构化数据时降低成本的绝佳选择。

TOON 将 YAML 的基于缩进的结构与 CSV 样式的表格布局相结合，适用于统一数组，实现了与标准 JSON 相比 **30-60% 的令牌减少**。

<Info>
  TOON 是一个**转译层** - 在代码中以编程方式使用 JSON，将数据传递给 LLM 时将其编码为 TOON。
</Info>

***

## TOON 如何工作

### JSON 的问题

标准 JSON 为每条记录重复字段名称，这在令牌方面很昂贵：

```json theme={null}
{
  "products": [
    { "id": 1, "name": "Laptop", "price": 999 },
    { "id": 2, "name": "Mouse", "price": 29 },
    { "id": 3, "name": "Keyboard", "price": 79 }
  ]
}
```

### TOON 解决方案

TOON 声明字段一次，然后以紧凑行的形式流式传输数据：

```yaml theme={null}
products[3]{id,name,price}:
  1,Laptop,999
  2,Mouse,29
  3,Keyboard,79
```

* `[3]` 声明数组长度（有助于检测截断）
* `{id,name,price}` 声明字段名称一次
* 每行包含逗号分隔的值

***

## 令牌节省示例

<CardGroup cols={2}>
  <Card title="JSON" icon="file-code">
    **235 个令牌**

    冗长且包含重复的键
  </Card>

  <Card title="TOON" icon="compress">
    **106 个令牌**

    \~55% 的减少
  </Card>
</CardGroup>

```json JSON (235 个令牌) theme={null}
{
  "context": {
    "task": "Product catalog",
    "category": "Electronics"
  },
  "items": [
    { "id": 1, "name": "Laptop", "price": 999, "stock": 50, "active": true },
    { "id": 2, "name": "Mouse", "price": 29, "stock": 200, "active": true },
    { "id": 3, "name": "Keyboard", "price": 79, "stock": 150, "active": false }
  ]
}
```

```yaml TOON (106 个令牌) theme={null}
context:
  task: Product catalog
  category: Electronics
items[3]{id,name,price,stock,active}:
  1,Laptop,999,50,true
  2,Mouse,29,200,true
  3,Keyboard,79,150,false
```

***

## 何时使用 TOON

<Check>
  **TOON 在扁平、统一的对象数组中表现出色** - 数据中的项目在所有记录中共享相同的结构。
</Check>

### 理想使用案例

| 数据类型 | 示例          | 令牌节省   |
| ---- | ----------- | ------ |
| 产品列表 | 电商目录        | 40-60% |
| 用户记录 | 扁平配置文件数据    | 35-55% |
| 日志条目 | 结构化日志       | 45-60% |
| 搜索结果 | SERP 数据（扁平） | 40-55% |
| 简单表格 | 类似电子表格的数据   | 50-65% |

***

## 何时不使用 TOON

<Warning>
  **TOON 在深层嵌套或非统一数据结构上表现不佳。** 这对 Bright Data MCP 响应特别相关。
</Warning>

### 避免在以下情况使用 TOON：

<AccordionGroup>
  <Accordion title="数据深度嵌套" icon="sitemap">
    具有多个嵌套级别的复杂对象无法从 TOON 的表格格式中受益。JSON-compact 通常对此类结构使用更少的令牌。

    **示例：** 包含嵌套经历、教育和技能对象的 LinkedIn 配置文件。
  </Accordion>

  <Accordion title="数据不统一" icon="shuffle">
    当数组项具有不同的字段或可选属性时，TOON 的基于标头的方法会崩溃。

    **示例：** 具有不同属性的混合产品类型。
  </Accordion>

  <Accordion title="使用 Bright Data MCP 结构化端点" icon="database">
    大多数 Bright Data Web 数据端点返回**富嵌套的 JSON**，具有分层关系。TOON 在这里不会提供有意义的节省。

    **示例：** `web_data_amazon_product`、`web_data_linkedin_person_profile` 等。
  </Accordion>
</AccordionGroup>

***

## Bright Data MCP 中的 TOON

### 理解限制

Bright Data 的 MCP 服务器从 Amazon、LinkedIn、Instagram 等平台返回结构化数据。这些数据通常是**嵌套且分层的**，不适合 TOON 优化。

<Tabs>
  <Tab title="远程 MCP (SSE)">
    通过服务器发送事件连接：

    ```
    https://mcp.brightdata.com/mcp?token=YOUR_API_TOKEN
    ```
  </Tab>

  <Tab title="本地 MCP (STDIO)">
    在 MCP 客户端中配置：

    ```json theme={null}
    {
      "mcpServers": {
        "Bright Data": {
          "command": "npx",
          "args": ["@brightdata/mcp"],
          "env": {
            "API_TOKEN": "<insert-your-api-token-here>",
            "WEB_UNLOCKER_ZONE": "my_zone_name",
            "BROWSER_ZONE": "my_browser_zone",
            "PRO_MODE": "true",
            "GROUPS": "browser,advanced_scraping",
            "TOOLS": "web_data_linkedin_person_profile,web_data_amazon_product"
          }
        }
      }
    }
    ```
  </Tab>
</Tabs>

### TOON 何时有帮助

虽然大多数 Bright Data 端点返回嵌套数据，但在某些情况下 TOON 可能会有益：

<Steps>
  <Step title="首先展平数据">
    对 MCP 响应进行后处理，在编码为 TOON 之前提取扁平数组。
  </Step>

  <Step title="用于批处理结果">
    使用 `scrape_batch` 或 `search_engine_batch` 时，URL/内容对可以展平。
  </Step>

  <Step title="自定义提取">
    使用 `extract` 工具，使用请求扁平、表格数据的提示。
  </Step>
</Steps>

***

## TOON 快速入门

### 安装

<CodeGroup>
  ```bash npm theme={null}
  npm install @toon-format/toon
  ```

  ```bash pnpm theme={null}
  pnpm add @toon-format/toon
  ```

  ```bash yarn theme={null}
  yarn add @toon-format/toon
  ```
</CodeGroup>

### 基本使用

```typescript theme={null}
import { encode, decode } from '@toon-format/toon'

// 您的扁平数据（TOON 理想选择）
const data = {
  products: [
    { id: 1, name: 'Laptop', price: 999 },
    { id: 2, name: 'Mouse', price: 29 },
    { id: 3, name: 'Keyboard', price: 79 }
  ]
}

// 编码为 TOON 用于 LLM 输入
const toonData = encode(data)
console.log(toonData)
// 输出：
// products[3]{id,name,price}:
//   1,Laptop,999
//   2,Mouse,29
//   3,Keyboard,79

// 解码回 JSON（无损往返）
const jsonData = decode(toonData)
```

### CLI 使用

```bash theme={null}
# 将 JSON 转换为 TOON
npx @toon-format/cli input.json -o output.toon

# 将 TOON 转换回 JSON
npx @toon-format/cli input.toon -o output.json
```

***

## 实际示例：在 MCP 客户端中使用 TOON

此示例演示了一个完整的工作流程：连接到 Bright Data 的 MCP 服务器、获取数据、展平嵌套响应，以及将其转换为 TOON 格式以实现令牌高效的 LLM 处理。

### 完整 MCP 客户端示例

```typescript theme={null}
import { Client } from '@modelcontextprotocol/sdk/client/index.js'
import { SSEClientTransport } from '@modelcontextprotocol/sdk/client/sse.js'
import { encode } from '@toon-format/toon'

// 使用 Bright Data 初始化 MCP 客户端（电商组用于 Amazon 工具）
const transport = new SSEClientTransport(
  new URL('https://mcp.brightdata.com/sse?token=YOUR_API_TOKEN&groups=ecommerce')
)

const client = new Client({
  name: 'toon-example-client',
  version: '1.0.0'
})

await client.connect(transport)

// 使用 MCP 获取 Amazon 产品数据（超时用于缓慢响应）
const result = await client.callTool(
  {
    name: 'web_data_amazon_product',
    arguments: {
      url: 'https://www.amazon.com/dp/B0EXAMPLE123'
    }
  },
  undefined,
  { timeout: 120000 } // 2 分钟超时
)

// MCP 响应是包含嵌套产品数据的数组
const mcpResponse = JSON.parse(result.content[0].text)
console.log('Raw MCP Response:', JSON.stringify(mcpResponse, null, 2))
// [
//   {
//     "title": "Ceramic Vase Set of 3...",
//     "final_price": 29.99,
//     "initial_price": 29.99,
//     "currency": "USD",
//     "rating": 4.5,
//     "reviews_count": 1250,
//     "seller_name": "HomeDecorStore",
//     "brand": "Lyeec",
//     "is_available": true,
//     "asin": "B0G13HFJNB",
//     ...
//   }
// ]

// 展平嵌套数据以进行 TOON 优化
// 将实际的 MCP 字段名称映射到扁平结构
function flattenProduct(product: any) {
  return {
    title: product.title,
    price: product.final_price,
    original_price: product.initial_price,
    currency: product.currency,
    rating: product.rating,
    reviews: product.reviews_count,
    seller: product.seller_name,
    brand: product.brand,
    in_stock: product.is_available
  }
}

// 响应是一个数组 - 展平所有产品
const flatProducts = mcpResponse.map(flattenProduct)

// 编码为 TOON - 现在它很高效！
const toonOutput = encode({ products: flatProducts })
console.log('TOON Output:', toonOutput)
// products[1]{title,price,original_price,currency,rating,reviews,seller,brand,in_stock}:
//   Ceramic Vase Set of 3...,29.99,29.99,USD,4.5,1250,HomeDecorStore,Lyeec,true

// 在您的 LLM 提示中使用 TOON 编码的数据
const prompt = `Analyze this product data and suggest pricing strategy:\n\n${toonOutput}`
```

### 批处理多个产品

对于较大的数据集，令牌节省变得更加显著：

```typescript theme={null}
import { Client } from '@modelcontextprotocol/sdk/client/index.js'
import { SSEClientTransport } from '@modelcontextprotocol/sdk/client/sse.js'
import { encode } from '@toon-format/toon'

const transport = new SSEClientTransport(
  new URL('https://mcp.brightdata.com/sse?token=YOUR_API_TOKEN&groups=ecommerce')
)

const client = new Client({ name: 'batch-example', version: '1.0.0' })
await client.connect(transport)

// 获取多个产品
const productUrls = [
  'https://www.amazon.com/dp/B0EXAMPLE1',
  'https://www.amazon.com/dp/B0EXAMPLE2',
  'https://www.amazon.com/dp/B0EXAMPLE3'
]

const results = await Promise.all(
  productUrls.map(async (url) => {
    const result = await client.callTool(
      { name: 'web_data_amazon_product', arguments: { url } },
      undefined,
      { timeout: 120000 }
    )
    // MCP 返回一个数组，获取第一个项目
    return JSON.parse(result.content[0].text)[0]
  })
)

// 使用实际的 MCP 字段名称展平所有产品用于 TOON
const flattenedProducts = results.map(p => ({
  title: p.title,
  price: p.final_price,
  currency: p.currency,
  rating: p.rating,
  reviews: p.reviews_count,
  seller: p.seller_name,
  brand: p.brand,
  in_stock: p.is_available
}))

// 转换为 TOON - 具有多个项目的大规模令牌节省！
const toonData = encode({ products: flattenedProducts })
console.log(toonData)
// products[3]{title,price,currency,rating,reviews,seller,brand,in_stock}:
//   Wireless Mouse,29.99,USD,4.5,1250,TechGear,Logitech,true
//   Gaming Keyboard,89.99,USD,4.7,890,KeyMaster,Razer,true
//   USB Hub,19.99,USD,4.2,2100,PortPlus,Anker,false

// 3 个产品的令牌比较：
// - JSON：~180 个令牌
// - TOON：~65 个令牌（64% 节省！）
```

### 创建可重复使用的展平器

对于生产使用，创建一个具有正确 MCP 字段映射的可重复使用的实用程序：

```typescript theme={null}
import { encode } from '@toon-format/toon'

// 用于常见 MCP 数据结构的通用展平器
// 这些映射 Bright Data MCP 返回的实际字段名称
const flatteners = {
  amazon_product: (p: any) => ({
    title: p.title,
    price: p.final_price,
    original_price: p.initial_price,
    currency: p.currency,
    rating: p.rating,
    reviews: p.reviews_count,
    seller: p.seller_name,
    brand: p.brand,
    in_stock: p.is_available
  }),

  linkedin_profile: (p: any) => ({
    name: p.full_name,
    headline: p.headline,
    location: p.city,
    country: p.country,
    connections: p.connections_count,
    followers: p.followers_count,
    company: p.current_company_name,
    position: p.position
  }),

  instagram_post: (p: any) => ({
    caption: p.description?.substring(0, 100),
    likes: p.likes,
    comments: p.comments,
    posted: p.upload_date,
    author: p.channel
  })
}

// 辅助函数处理 MCP 响应并转换为 TOON
function mcpToToon<T>(
  data: T | T[],
  flattener: (item: T) => Record<string, any>,
  key: string = 'items'
): string {
  const items = Array.isArray(data) ? data : [data]
  const flattened = items.map(flattener)
  return encode({ [key]: flattened })
}

// 使用示例
const result = await client.callTool(
  { name: 'web_data_amazon_product', arguments: { url: '...' } },
  undefined,
  { timeout: 120000 }
)
const mcpData = JSON.parse(result.content[0].text)
const toonOutput = mcpToToon(mcpData, flatteners.amazon_product, 'products')
```

***

## 总结

<CardGroup cols={2}>
  <Card title="在以下情况使用 TOON" icon="check" color="#22c55e">
    * 扁平、统一的数组
    * 表格数据结构
    * 具有重复模式的大型数据集
    * 后处理、展平的 MCP 数据
  </Card>

  <Card title="在以下情况避免 TOON" icon="xmark" color="#ef4444">
    * 深度嵌套的对象
    * 非统一数据结构
    * 直接 MCP 端点响应
    * 复杂的分层数据
  </Card>
</CardGroup>

<Info>
  **总之：** TOON 是令牌优化的强大工具，但它专为扁平、统一的数据设计。Bright Data MCP 响应通常是嵌套的，因此仅在将数据展平为表格结构后再应用 TOON。
</Info>

***

## 资源

<CardGroup cols={3}>
  <Card title="TOON 规范" icon="book" href="https://github.com/toon-format/spec">
    官方格式规范
  </Card>

  <Card title="TypeScript SDK" icon="npm" href="https://www.npmjs.com/package/@toon-format/toon">
    NPM 包文档
  </Card>

  <Card title="TOON 网站" icon="globe" href="https://toonformat.dev">
    交互式游乐场和文档
  </Card>
</CardGroup>
