> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# AI 代理网络访问

> 为需要可靠、可扩展网络访问的AI代理提供完整的网络基础设施。企业级网络访问的生产就绪API。

<Card title="正在构建 AI 初创公司？" cta="了解更多" href="https://brightdata.com/ai/ai-startups-program" icon="rocket-launch" iconType="duotone" arrow="true">
  您可能符合我们的初创计划资格。获得本文所介绍基础设施的全额资助访问权限（最高价值 \$20,000）。
</Card>

# Agent Web Access

为需要可靠、可扩展网络访问的AI代理提供完整的网络基础设施。

构建能自动丰富数据、进行竞争情报研究和评估模型输出的AI代理。企业级网络访问的生产就绪API。

<CardGroup cols={2}>
  <Card title="开始使用" icon="rocket" href="#architecture-patterns">
    学习如何为AI代理设计网络访问架构
  </Card>

  <Card title="产品选择" icon="list" href="#product-selection-guide">
    为您的使用场景选择合适的产品
  </Card>
</CardGroup>

***

## 可扩展性和性能

从简单的搜索和提取工作流（同时处理数千条线索）扩展到复杂的多步骤研究操作（浏览器自动化、会话管理、历史数据访问）。

凭借99.99%的正常运行时间和亚秒级响应时间，您可以专注于构建AI代理，而我们负责处理网络访问的复杂性。

<CardGroup cols={3}>
  <Card title="99.99% 正常运行时间" icon="shield-check">
    企业级可靠性确保您的AI代理永不错过关键数据
  </Card>

  <Card title="亚秒级响应时间" icon="bolt">
    闪电般快速的网络访问使您的代理始终保持响应式和高效
  </Card>

  <Card title="并发操作" icon="server">
    使用企业级基础设施处理数千个并发操作
  </Card>
</CardGroup>

***

## AI Agent 专用功能

为AI代理模式构建，包括：

* **自动CAPTCHA解决** - 永远不会被CAPTCHA或机器人检测阻止
* **企业级并发操作** - 自信地处理生产工作负载
* **集成代理管理** - 自动IP轮换和会话管理
* **浏览器自动化** - 与JavaScript重型站点复杂交互
* **历史数据访问** - 访问存档网络内容进行全面研究
* **实时搜索结果** - 为发现工作流获取最新搜索数据

***

## 架构模式

<CardGroup cols={2}>
  <Card title="搜索和提取" icon="magnifying-glass" href="/cn/scraping-automation/serp-api/introduction">
    使用SERP API从搜索结果中发现和提取数据
  </Card>

  <Card title="浏览器自动化" icon="browser" href="/cn/scraping-automation/scraping-browser/introduction">
    使用浏览器API处理复杂的JavaScript重型交互
  </Card>

  <Card title="CAPTCHA解决" icon="unlock" href="/cn/scraping-automation/web-unlocker/introduction">
    使用Web Unlocker自动绕过CAPTCHA和阻止
  </Card>

  <Card title="历史数据" icon="archive" href="/cn/datasets/archive/overview">
    访问存档网络内容进行全面研究
  </Card>
</CardGroup>

***

## 产品选择指南

为您的AI代理使用场景选择合适的产品：

### 发现和搜索

* **SERP API** - 用于代理发现的实时搜索结果
* **网络存档** - 访问历史数据进行全面研究

### 数据提取

* **爬虫工具** - 从热门域名进行结构化数据提取
* **浏览器API** - 与JavaScript重型站点进行复杂交互

### 可靠性和规模

* **Web Unlocker** - 自动CAPTCHA解决和阻止绕过
* **住宅代理** - 真实用户IP以获得最大可靠性

***

## 扩展考虑

<CardGroup cols={2}>
  <Card title="速率限制" icon="clock" href="/general/usage-monitoring/fair_use_allowance">
    了解大容量使用的速率限制和最佳实践
  </Card>

  <Card title="错误处理" icon="exclamation-triangle" href="/proxy-networks/errorCatalog">
    为生产工作负载实现健壮的错误处理
  </Card>

  <Card title="会话管理" icon="key" href="/proxy-networks/residential/configure-your-proxy">
    管��会话以维护请求间的状态
  </Card>

  <Card title="监控" icon="chart-line" href="/general/usage-monitoring/Usage">
    监控使用情况和性能以优化您的工作流
  </Card>
</CardGroup>

***

## 示例

### 简单搜索和提取

为竞争情报提取搜索结果：

<CodeGroup>
  ```javascript Node.js theme={null}
  const response = await fetch('https://api.brightdata.com/datasets/v3/trigger?dataset_id=YOUR_DATASET_ID', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${apiKey}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify([{
      url: 'https://www.google.com/search',
      keyword: 'competitor analysis',
      country: 'US'
    }])
  });
  ```

  ```python Python theme={null}
  import requests

  response = requests.post(
    'https://api.brightdata.com/datasets/v3/trigger?dataset_id=YOUR_DATASET_ID',
    headers={
      'Authorization': f'Bearer {api_key}',
      'Content-Type': 'application/json'
    },
    json=[{
      'url': 'https://www.google.com/search',
      'keyword': 'competitor analysis',
      'country': 'US'
    }]
  )
  ```
</CodeGroup>

### 浏览器自动化

自动化与JavaScript重型站点的复杂交互：

<CodeGroup>
  ```javascript Node.js theme={null}
  const response = await fetch('https://api.brightdata.com/browser_api/v1/run', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${apiKey}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      url: 'https://example.com',
      browser: {
        headless: false,
        viewport: { width: 1920, height: 1080 }
      },
      actions: [
        { type: 'click', selector: '#button' },
        { type: 'wait', timeout: 2000 },
        { type: 'extract', selector: '.content' }
      ]
    })
  });
  ```

  ```python Python theme={null}
  import requests

  response = requests.post(
    'https://api.brightdata.com/browser_api/v1/run',
    headers={
      'Authorization': f'Bearer {api_key}',
      'Content-Type': 'application/json'
    },
    json={
      'url': 'https://example.com',
      'browser': {
        'headless': False,
        'viewport': {'width': 1920, 'height': 1080}
      },
      'actions': [
        {'type': 'click', 'selector': '#button'},
        {'type': 'wait', 'timeout': 2000},
        {'type': 'extract', 'selector': '.content'}
      ]
    }
  )
  ```
</CodeGroup>

***

## 后续步骤

<CardGroup cols={2}>
  <Card title="SERP API 快速开始" icon="rocket" href="/search-api-quickstart">
    开始为AI代理收集搜索结果
  </Card>

  <Card title="浏览器 API 快速开始" icon="rocket" href="/browser-api-quickstart">
    自动化浏览器交互以进行复杂工作流
  </Card>

  <Card title="Web Unlocker 快速开始" icon="rocket" href="/unlocker-api-quickstart">
    自动绕过CAPTCHA和阻止
  </Card>

  <Card title="浏览示例" icon="code" href="/cn/scraping-automation/serp-api/get-top-100-google-results">
    探索代码示例和使用案例
  </Card>
</CardGroup>

<Info>
  **需要帮助?** 查看我们的 [API参考](/api-reference/authentication) 或 [联系支持](https://www.bright.cn/contact)。
</Info>
