> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 数据丰富

> 构建AI代理，自动填充CRM数据、丰富潜在客户并大规模完成客户记录。掌握丰富操作的搜索和提取模式。

<Card title="正在构建 AI 初创公司？" cta="了解更多" href="https://brightdata.com/ai/ai-startups-program" icon="rocket-launch" iconType="duotone" arrow="true">
  您可能符合我们的初创计划资格。获得本文所介绍基础设施的全额资助访问权限（最高价值 \$20,000）。
</Card>

# 数据丰富

构建AI代理，自动填充CRM数据、丰富潜在客户并大规模完成客户记录。

掌握丰富操作的搜索和提取模式，从LinkedIn公司数据收集到潜在客户评分工作流。

<CardGroup cols={2}>
  <Card title="学习模式" icon="lightbulb" href="#the-enrichment-pattern">
    了解丰富工作流程
  </Card>

  <Card title="开始使用" icon="rocket" href="#contact-enrichment---linkedin-example">
    从LinkedIn示例开始
  </Card>
</CardGroup>

***

## 复杂性处理

解决丰富系统中的常见挑战：

* **LinkedIn的激进反机器人措施** - 使用Web Unlocker自动绕过
* **CAPTCHA挑战** - 无需手动干预的自动CAPTCHA求解
* **速率限制** - 智能速率管理和代理轮换
* **数据质量问题** - 内置验证和错误处理

Bright Data的基础设施通过自动CAPTCHA求解、智能速率管理和生产就绪的可靠性解决这些问题。

<CardGroup cols={2}>
  <Card title="自动CAPTCHA求解" icon="unlock" href="/cn/scraping-automation/web-unlocker/introduction">
    永远不会被CAPTCHA或机器人检测阻止
  </Card>

  <Card title="速率管理" icon="clock" href="/proxy-networks/residential/configure-your-proxy">
    智能速率限制和代理轮换
  </Card>

  <Card title="数据验证" icon="check-circle" href="/cn/datasets/data-validation/data-validation-for-customers">
    内置验证确保数据质量
  </Card>

  <Card title="错误处理" icon="exclamation-triangle" href="/proxy-networks/errorCatalog">
    强大的错误处理以实现生产可靠性
  </Card>
</CardGroup>

***

## 可扩展性

从丰富数百个潜在客户扩展到处理数百万条记录，使用相同的基础设施。

为丰富模式而构建，例如：

* **并行处理**以提高吞吐量
* **错误处理**以提高可靠性
* **数据验证**以提高质量

<CardGroup cols={3}>
  <Card title="并行处理" icon="server">
    使用企业级基础设施同时处理数千个潜在客户
  </Card>

  <Card title="错误处理" icon="shield-check">
    强大的错误处理确保大规模可靠性
  </Card>

  <Card title="数据验证" icon="check-circle">
    内置验证确保高质量的丰富数据
  </Card>
</CardGroup>

***

## 丰富模式

丰富模式通常遵循以下步骤：

1. **输入** - 接收需要丰富的潜在客户或记录列表
2. **搜索** - 使用SERP API或网络抓取来搜索每个潜在客户
3. **提取** - 从搜索结果中提取相关数据
4. **验证** - 验证提取的数据的质量
5. **丰富** - 将丰富的数据添加到您的CRM或数据库
6. **监控** - 监控成功率和数据质量

<Steps>
  <Step title="准备输入数据">
    准备需要丰富的潜在客户或记录列表。包括公司名称、域或电子邮件地址等标识符。

    ```json theme={null}
    [
      {
        "company_name": "Example Corp",
        "domain": "example.com",
        "email": "contact@example.com"
      }
    ]
    ```
  </Step>

  <Step title="搜索数据">
    使用SERP API或网络抓取为每个潜在客户搜索并查找相关信息。

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
          keyword: 'Example Corp company information',
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
          'keyword': 'Example Corp company information',
          'country': 'US'
        }]
      )
      ```
    </CodeGroup>
  </Step>

  <Step title="提取和验证">
    从搜索结果中提取相关数据并验证质量。

    <Tip>
      使用数据验证端点确保提取的数据符合您的质量标准。
    </Tip>
  </Step>

  <Step title="丰富记录">
    将丰富的数据添加到您的CRM或数据库。

    <Check>
      成功丰富的潜在客户将以完整的联系信息保存。
    </Check>
  </Step>
</Steps>

***

## 联系人丰富 - LinkedIn示例

使用LinkedIn公司数据丰富潜在客户：

### 步骤1：搜索LinkedIn

在LinkedIn上搜索公司信息：

<CodeGroup>
  ```javascript Node.js theme={null}
  const response = await fetch('https://api.brightdata.com/datasets/v3/trigger?dataset_id=YOUR_LINKEDIN_DATASET_ID', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${apiKey}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify([{
      url: 'https://www.linkedin.com/company/example-corp',
      company_name: 'Example Corp'
    }])
  });
  ```

  ```python Python theme={null}
  import requests

  response = requests.post(
    'https://api.brightdata.com/datasets/v3/trigger?dataset_id=YOUR_LINKEDIN_DATASET_ID',
    headers={
      'Authorization': f'Bearer {api_key}',
      'Content-Type': 'application/json'
    },
    json=[{
      'url': 'https://www.linkedin.com/company/example-corp',
      'company_name': 'Example Corp'
    }]
  )
  ```
</CodeGroup>

### 步骤2：提取公司数据

提取公司信息：

```json theme={null}
{
  "company_name": "Example Corp",
  "industry": "Technology",
  "employee_count": "1000-5000",
  "location": "San Francisco, CA",
  "website": "https://example.com",
  "description": "Leading technology company..."
}
```

### 步骤3：丰富您的CRM

将丰富的数据添加到您的CRM：

<CodeGroup>
  ```javascript Node.js theme={null}
  // 将丰富的数据添加到您的CRM
  await crm.addContact({
    company_name: enrichedData.company_name,
    industry: enrichedData.industry,
    employee_count: enrichedData.employee_count,
    location: enrichedData.location,
    website: enrichedData.website
  });
  ```

  ```python Python theme={null}
  # 将丰富的数据添加到您的CRM
  crm.add_contact(
    company_name=enriched_data['company_name'],
    industry=enriched_data['industry'],
    employee_count=enriched_data['employee_count'],
    location=enriched_data['location'],
    website=enriched_data['website']
  )
  ```
</CodeGroup>

***

## 批量处理

高效地处理大���潜在客户：

### 并行处理

同时处理多个潜在客户：

<CodeGroup>
  ```javascript Node.js theme={null}
  const leads = [/* array of leads */];
  const enrichmentPromises = leads.map(lead => 
    enrichLead(lead)
  );

  const enrichedLeads = await Promise.all(enrichmentPromises);
  ```

  ```python Python theme={null}
  import asyncio

  leads = [/* list of leads */]

  async def enrich_lead(lead):
      # Enrichment logic
      pass

  async def enrich_all_leads():
      tasks = [enrich_lead(lead) for lead in leads]
      enriched_leads = await asyncio.gather(*tasks)
      return enriched_leads
  ```
</CodeGroup>

### 批量处理

分批处理潜在客户以管理速率限制：

<CodeGroup>
  ```javascript Node.js theme={null}
  async function processBatch(leads, batchSize = 10) {
    for (let i = 0; i < leads.length; i += batchSize) {
      const batch = leads.slice(i, i + batchSize);
      await Promise.all(batch.map(lead => enrichLead(lead)));
      // Wait between batches to respect rate limits
      await new Promise(resolve => setTimeout(resolve, 1000));
    }
  }
  ```

  ```python Python theme={null}
  import time

  def process_batch(leads, batch_size=10):
      for i in range(0, len(leads), batch_size):
          batch = leads[i:i + batch_size]
          for lead in batch:
              enrich_lead(lead)
          # Wait between batches to respect rate limits
          time.sleep(1)
  ```
</CodeGroup>

***

## 常见数据源

<CardGroup cols={2}>
  <Card title="LinkedIn" icon="linkedin" href="/cn/api-reference/scrapers/social-media-apis/linkedin">
    来自LinkedIn的公司和专业数据
  </Card>

  <Card title="Google搜索" icon="magnifying-glass" href="/cn/scraping-automation/serp-api/introduction">
    用于公司信息和新闻的搜索结果
  </Card>

  <Card title="公司网站" icon="globe" href="/cn/scraping-automation/scraping-browser/introduction">
    直接从网站中提取公司信息
  </Card>

  <Card title="社交媒体" icon="share" href="/api-reference/scrapers/social-media-apis/overview">
    社交媒体资料和参与度数据
  </Card>
</CardGroup>

***

## 错误处理

实施强大的错误处理以实现生产可靠性：

<CodeGroup>
  ```javascript Node.js theme={null}
  async function enrichLeadWithRetry(lead, maxRetries = 3) {
    for (let attempt = 1; attempt <= maxRetries; attempt++) {
      try {
        const result = await enrichLead(lead);
        return result;
      } catch (error) {
        if (attempt === maxRetries) {
          throw error;
        }
        // Exponential backoff
        await new Promise(resolve => setTimeout(resolve, Math.pow(2, attempt) * 1000));
      }
    }
  }
  ```

  ```python Python theme={null}
  import time

  def enrich_lead_with_retry(lead, max_retries=3):
      for attempt in range(1, max_retries + 1):
          try:
              result = enrich_lead(lead)
              return result
          except Exception as error:
              if attempt == max_retries:
                  raise error
              # Exponential backoff
              time.sleep(2 ** attempt)
  ```
</CodeGroup>

***

## 模板

使用预构建的模板进行常见丰富工作流程：

<CardGroup cols={2}>
  <Card title="LinkedIn公司丰富" icon="linkedin" href="/cn/api-reference/scrapers/social-media-apis/linkedin">
    使用LinkedIn公司数据丰富潜在客户的模板
  </Card>

  <Card title="电子邮件验证" icon="envelope" href="/cn/datasets/deep-lookup/overview">
    用于验证和丰富电子邮件地址的模板
  </Card>

  <Card title="联系信息" icon="address-book" href="/cn/datasets/deep-lookup/overview">
    用于丰富联系信息的模板
  </Card>

  <Card title="公司情报" icon="building" href="/cn/datasets/deep-lookup/overview">
    用于收集公司情报数据的模板
  </Card>
</CardGroup>

***

## 后续步骤

<CardGroup cols={2}>
  <Card title="SERP API快速入门" icon="rocket" href="/search-api-quickstart">
    开始收集用于丰富的搜索结果
  </Card>

  <Card title="LinkedIn抓取工具" icon="rocket" href="/cn/api-reference/scrapers/social-media-apis/linkedin">
    使用预构建的LinkedIn抓取工具获取公司数据
  </Card>

  <Card title="深度查找" icon="rocket" href="/cn/datasets/deep-lookup/overview">
    使用深度查找进行全面的数据丰富
  </Card>

  <Card title="浏览示例" icon="code" href="/cn/datasets/scrapers/scrapers-library">
    探索常见数据源的预构建抓取工具
  </Card>
</CardGroup>

<Info>
  **需要帮助？** 查看我们的[数据验证指南](/cn/datasets/data-validation/data-validation-for-customers)或[联系支持](https://www.bright.cn/contact)。
</Info>
