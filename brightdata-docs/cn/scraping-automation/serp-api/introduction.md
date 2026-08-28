> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SERP API 入门

> 无需管理代理、CAPTCHA 或解析即可收集搜索结果。通过单个端点几分钟内即可开始。

<Note>
  [立即开始](https://www.bright.cn/?hs_signup=1\&utm_source=docs)，每月赠送 **5,000 个免费信用额度**，无需信用卡。参见[免费套餐](/cn/general/account/billing-and-pricing/free-tier)。

  我们还将匹配您的**首次账户充值金额，最高可达 \$500**。
</Note>

无需管理代理、CAPTCHA 或解析，即可大规模收集搜索引擎结果。在 1 秒内从 Google、Bing 等搜索引擎获取结构化数据。

**适用场景：**

* SEO 排名跟踪和关键词监控
* 执行网页搜索和数据丰富的 AI 代理
* 品牌保护和广告情报
* 竞争市场调研和价格比较

<Tip>
  仅为成功交付付费。
</Tip>

## 开始前

1. 登录: [https://www.bright.cn/cp/start](https://www.bright.cn/cp/start)
2. 创建 SERP API: [https://www.bright.cn/cp/learn\_more/serp-api](https://www.bright.cn/cp/learn_more/serp-api)
3. 获取您的 API 密钥: [/cn/api-reference/authentication](/cn/api-reference/authentication#如何生成新的-api-key？)

<Tip>
  新手指南：查看逐步指南: [/cn/scraping-automation/serp-api/quickstart](/cn/scraping-automation/serp-api/quickstart)
</Tip>

## 快速开始

使用 cURL 的最小请求示例。将 `<BRIGHT_DATA_API_KEY>` 和 `zone` 替换为您的值：

<CodeGroup>
  ```shell cURL theme={null}
  curl -X POST https://api.brightdata.com/request \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer <BRIGHT_DATA_API_KEY>" \
    -d '{
      "zone": "YOUR_SERP_API_ZONE",
      "url": "https://www.google.com/search?q=pizza&hl=en&gl=us",
      "format": "raw"
    }'
  ```

  ```javascript Node.js theme={null}
  // Node 18+ (global fetch)
  const resp = await fetch('https://api.brightdata.com/request', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer <BRIGHT_DATA_API_KEY>',
    },
    body: JSON.stringify({
      zone: 'YOUR_SERP_API_ZONE',
      url: 'https://www.google.com/search?q=pizza&hl=en&gl=us',
      format: 'raw' // 设置为 "json" 获取解析后的输出
    }),
  });

  console.log(await resp.text());
  ```

  ```python Python theme={null}
  import requests

  headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer <BRIGHT_DATA_API_KEY>',
  }

  payload = {
      'zone': 'YOUR_SERP_API_ZONE',
      'url': 'https://www.google.com/search?q=pizza&hl=en&gl=us',
      'format': 'raw'  # 设置为 "json" 获取解析后的输出
  }

  r = requests.post('https://api.brightdata.com/request',
                    headers=headers, json=payload)

  print(r.text)
  ```
</CodeGroup>

<Tip>
  喜欢 Markdown 输出？设置 <code>"data\_format": "markdown"</code> 接收 Markdown SERP 结构。
</Tip>

<Tip>
  喜欢 JSON 输出？设置查询参数 <code>"brd\_json=1"</code> 接收 JSON SERP 结构。
</Tip>

<CardGroup cols={3}>
  <Card title="在 Postman 中运行" icon="rocket" href="https://www.postman.com/bright-data-api/bright-data-api/request/kpq952m/google-search" cta="打开 Postman" />

  <Card title="Node.js 示例" icon="code" href="https://github.com/luminati-io/bright-data-serp-api-nodejs-project" cta="打开仓库" />

  <Card title="Python 示例" icon="code" href="https://github.com/brightdata/bright-data-serp-api-python-project" cta="打开仓库" />
</CardGroup>

## 获取的结果（解析后的 JSON 预览）

解析结构的简要示例：

```json theme={null}
{
  "engine": "google",
  "query": "pizza",
  "results": [
    { 
      "type": "organic", 
      "position": 1, 
      "title": "Best Pizza Near Me", 
      "url": "https://example.com" 
    }
  ]
}
```

查看完整的模式和示例：[/cn/scraping-automation/serp-api/parsed-json-results/parsing-search-results](/cn/scraping-automation/serp-api/parsed-json-results/parsing-search-results#expected-parsed-output-when-using-brd-json%3D1)

## 支持的搜索引擎和参数

* Google、Bing、DuckDuckGo、Yandex、Baidu、Yahoo、Naver
* 特定引擎查询参数：

  * Google: [/cn/scraping-automation/serp-api/query-parameters/google](/cn/scraping-automation/serp-api/query-parameters/google)
  * Bing: [/cn/scraping-automation/serp-api/query-parameters/bing](/cn/scraping-automation/serp-api/query-parameters/bing)

## 性能优化

### 仅获取前 10 条结果（响应更快）

如果只需要前 10 条自然结果（无广告或知识面板），添加 `"data_format": "parsed_light"` 可加快响应速度：

<CodeGroup>
  ```bash cURL highlight={8} theme={null}
  curl -X POST 'https://api.brightdata.com/request' \
    -H 'Authorization: Bearer <API_KEY>' \
    -H 'Content-Type: application/json' \
    -d '{
      "zone": "<ZONE_NAME>",
      "url": "https://www.google.com/search?q=pizza&hl=en&gl=us",
      "format": "raw",
      "data_format": "parsed_light"
    }'
  ```

  ```javascript scrape.js highlight={11} theme={null}
  const response = await fetch('https://api.brightdata.com/request', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer <API_KEY>',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      zone: '<ZONE_NAME>',
      url: 'https://www.google.com/search?q=pizza&hl=en&gl=us',
      format: 'raw',
      data_format: 'parsed_light'
    })
  });

  const data = await response.json();
  console.log(data.organic);  // 前 10 条结果数组
  ```

  ```python scrape.py highlight={8} theme={null}
  response = requests.post(
      'https://api.brightdata.com/request',
      headers={'Authorization': 'Bearer <API_KEY>'},
      json={
          'zone': '<ZONE_NAME>',
          'url': 'https://www.google.com/search?q=pizza&hl=en&gl=us',
          'format': 'raw',
          'data_format': 'parsed_light'
      }
  )

  data = response.json()
  print(data['organic'])  # 前 10 条结果数组
  ```
</CodeGroup>

响应示例：

```json successful JSON response theme={null}
{
  "organic": [
    {
      "link": "https://example.com/pizza",
      "title": "Best Pizza in NYC - Joe's Pizza",
      "description": "Family-owned pizzeria serving authentic New York slices since 1975...",
      "global_rank": 1
    },
    {
      "link": "https://example.com/pizza-guide",
      "title": "Top 10 Pizza Places in NYC",
      "description": "Discover the highest-rated pizza restaurants across all five boroughs...",
      "global_rank": 2,
      "extensions": [
        {
          "type": "site_link",
          "link": "https://example.com/pizza-guide/brooklyn",
          "text": "Brooklyn"
        }
      ]
    }
    // ... 其他 8 条结果
  ]
}
```

### 低于 1 秒的响应时间

使用专为关键 AI 应用设计的高级路由基础设施，可在 **1 秒内** 获取完整 SERP 结果（自然结果、广告、知识面板及所有元素）。

**理想用途：**

* AI 代理执行实时数据丰富
* 多步骤研究流程和事实验证
* 模型评估和响应基础
* 面向用户的搜索应用需即时结果

<Note>联系您的客户经理或 [sales@brightdata.com](mailto:sales@brightdata.com) 申请访问权限。</Note>

## 何时使用异步请求

对于大批量、页面加载慢或查询耗时长的请求，使用异步可提高可靠性和吞吐量。

* 指南：[/cn/scraping-automation/serp-api/asynchronous-requests](/cn/scraping-automation/serp-api/asynchronous-requests)

<Tip>
  针对非 SERP 页面？使用 Web Unlocker API: [/cn/scraping-automation/web-unlocker](/cn/scraping-automation/web-unlocker)
</Tip>

## 快速排查问题

* **401/403**: 检查 API 密钥和 zone 权限。参考: [/cn/api-reference/authentication](/cn/api-reference/authentication)
* **429**: 减少并发或切换至异步。参考: [/cn/scraping-automation/serp-api/asynchronous-requests](/cn/scraping-automation/serp-api/asynchronous-requests)
* **结果为空或部分结果**: 验证引擎特定参数（如 `hl`, `gl`, `uule`, `location`）
* **结果异常**: 使用非拉丁字符时可能出现。Google 搜索请求需对查询进行编码。
* **仍有问题？** 查看常见问题: [/cn/scraping-automation/serp-api/faqs](/cn/scraping-automation/serp-api/faqs)

## 下一步

<CardGroup cols={3}>
  <Card title="发送第一个请求" icon="bolt" href="/cn/scraping-automation/serp-api/send-your-first-request" cta="打开指南" />

  <Card title="SERP 定价与计费" icon="dollar-sign" href="/cn/scraping-automation/serp-api/pricing-and-billing" cta="打开定价" />

  <Card title="查询参数（Google）" icon="sliders" href="/cn/scraping-automation/serp-api/query-parameters/google" cta="打开文档" />

  <Card title="解析后的 JSON 结果" icon="list" href="/cn/scraping-automation/serp-api/parsed-json-results/parsing-search-results" cta="打开模式" />

  <Card title="异步请求" icon="clock" href="/cn/scraping-automation/serp-api/asynchronous-requests" cta="打开指南" />

  <Card title="快速开始" icon="road" href="/cn/scraping-automation/serp-api/quickstart" cta="打开步骤" />

  <Card title="常见问题" icon="circle-question" href="/cn/scraping-automation/serp-api/faqs" cta="打开 FAQs" />
</CardGroup>
