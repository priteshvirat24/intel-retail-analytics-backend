> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 深度研究

> 构建AI代理，在规模上进行全面的多源研究操作。结合实时搜索、历史分析和复杂网站导航，用于竞争情报和市场研究。

<Card title="正在构建 AI 初创公司？" cta="了解更多" href="https://brightdata.com/ai/ai-startups-program" icon="rocket-launch" iconType="duotone" arrow="true">
  您可能符合我们的初创计划资格。获得本文所介绍基础设施的全额资助访问权限（最高价值 \$20,000）。
</Card>

# 深度研究代理

构建AI代理，在规模上进行全面的多源研究操作。

超越简单的数据提取，创建结合实时搜索、历史分析和复杂网站导航的研究工作流。这些能力为竞争情报、市场研究和调查分析系统奠定了基础。

<CardGroup cols={2}>
  <Card title="学习研究模式" icon="lightbulb" href="#multi-source-research-patterns">
    了解多源研究工作流
  </Card>

  <Card title="快速开始" icon="rocket" href="#examples">
    探索研究示例
  </Card>
</CardGroup>

***

## 处理的研究挑战

处理通常会阻止基本抓取的研究挑战：

* **多步工作流** - 需要在多个请求中保持会话持久性
* **复杂网站交互** - 需要浏览器自动化来处理JavaScript繁重网站
* **历史背景** - 需要存档访问以进行全面研究
* **研究深度** - 需要跨源验证以确保准确性

该基础设施为全面的研究操作提供了完整的工具包。

<CardGroup cols={2}>
  <Card title="会话管理" icon="key" href="/cn/proxy-networks/residential/configure-your-proxy">
    在多步工作流中维持会话持久性
  </Card>

  <Card title="浏览器自动化" icon="browser" href="/cn/scraping-automation/scraping-browser/introduction">
    使用浏览器自动化处理复杂网站交互
  </Card>

  <Card title="历史数据" icon="archive" href="/cn/datasets/archive/overview">
    通过网络存档访问历史背景
  </Card>

  <Card title="跨源验证" icon="check-circle" href="/cn/datasets/deep-lookup/overview">
    验证多个来源的研究
  </Card>
</CardGroup>

***

## 应用和目的

从初创企业竞争分析到企业市场情报，研究代理需要能够：

* 导航复杂工作流
* 在多个来源中保持背景
* 提供当前和历史视角

为需要广度和深度的研究模式而构建。

***

## 多源研究模式

结合多个数据源进行全面研究：

<CardGroup cols={2}>
  <Card title="实时搜索" icon="magnifying-glass" href="/cn/scraping-automation/serp-api/introduction">
    使用SERP API获取多个搜索引擎的实时搜索结果
  </Card>

  <Card title="历史分析" icon="archive" href="/cn/datasets/archive/overview">
    通过网络存档访问历史数据以进行趋势分析
  </Card>

  <Card title="网站特定数据" icon="globe" href="/cn/scraping-automation/scraping-browser/introduction">
    使用浏览器自动化从特定网站提取数据
  </Card>

  <Card title="交叉参考验证" icon="check-circle" href="/cn/datasets/deep-lookup/overview">
    在多个来源中验证发现以确保准确性
  </Card>
</CardGroup>

***

## 网络存档的历史背景

访问历史数据进行全面研究：

<CodeGroup>
  ```javascript Node.js theme={null}
  // 搜索历史数据
  const response = await fetch('https://api.brightdata.com/datasets/v3/trigger?dataset_id=YOUR_ARCHIVE_DATASET_ID', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${apiKey}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify([{
      url: 'https://example.com',
      date: '2023-01-01',
      archive_type: 'web_archive'
    }])
  });
  ```

  ```python Python theme={null}
  import requests

  # 搜索历史数据
  response = requests.post(
    'https://api.brightdata.com/datasets/v3/trigger?dataset_id=YOUR_ARCHIVE_DATASET_ID',
    headers={
      'Authorization': f'Bearer {api_key}',
      'Content-Type': 'application/json'
    },
    json=[{
      'url': 'https://example.com',
      'date': '2023-01-01',
      'archive_type': 'web_archive'
    }]
  )
  ```
</CodeGroup>

***

## 复杂网站导航

使用浏览器自动化导航复杂网站：

<CodeGroup>
  ```javascript Node.js theme={null}
  // 多步研究工作流
  const response = await fetch('https://api.brightdata.com/browser_api/v1/run', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${apiKey}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      url: 'https://example.com/research',
      browser: {
        headless: true,
        viewport: { width: 1920, height: 1080 }
      },
      actions: [
        { type: 'navigate', url: 'https://example.com/search' },
        { type: 'fill', selector: '#search', value: 'research topic' },
        { type: 'click', selector: '#submit' },
        { type: 'wait', timeout: 3000 },
        { type: 'extract', selector: '.results' },
        { type: 'navigate', url: 'https://example.com/details' },
        { type: 'extract', selector: '.content' }
      ]
    })
  });
  ```

  ```python Python theme={null}
  import requests

  # 多步研究工作流
  response = requests.post(
    'https://api.brightdata.com/browser_api/v1/run',
    headers={
      'Authorization': f'Bearer {api_key}',
      'Content-Type': 'application/json'
    },
    json={
      'url': 'https://example.com/research',
      'browser': {
        'headless': True,
        'viewport': {'width': 1920, 'height': 1080}
      },
      'actions': [
        {'type': 'navigate', 'url': 'https://example.com/search'},
        {'type': 'fill', 'selector': '#search', 'value': 'research topic'},
        {'type': 'click', 'selector': '#submit'},
        {'type': 'wait', 'timeout': 3000},
        {'type': 'extract', 'selector': '.results'},
        {'type': 'navigate', 'url': 'https://example.com/details'},
        {'type': 'extract', 'selector': '.content'}
      ]
    }
  )
  ```
</CodeGroup>

***

## 研究工作流编排

编排复杂的研究工作流：

<Steps>
  <Step title="定义研究查询">
    定义您的研究查询和目标。识别您需要回答的问题。

    ```json theme={null}
    {
      "query": "AI工具市场分析",
      "objectives": [
        "识别关键竞争对手",
        "分析定价策略",
        "审查客户反馈"
      ]
    }
    ```
  </Step>

  <Step title="搜索多个来源">
    同时在多个来源中搜索：

    * 实时搜索结果（SERP API）
    * 历史数据（网络存档）
    * 网站特定数据（浏览器API）

    <CodeGroup>
      ```javascript Node.js theme={null}
      const searchPromises = [
        searchSERP(query),
        searchArchive(query),
        searchSite(query)
      ];
      const results = await Promise.all(searchPromises);
      ```

      ```python Python theme={null}
      import asyncio

      search_tasks = [
        search_serp(query),
        search_archive(query),
        search_site(query)
      ]
      results = await asyncio.gather(*search_tasks)
      ```
    </CodeGroup>
  </Step>

  <Step title="提取和结构化">
    从每个来源提取相关数据并将其结构化以供分析。

    <Tip>
      使用数据验证以确保跨来源的数据质量和一致性。
    </Tip>
  </Step>

  <Step title="交叉参考和验证">
    在多个来源间交叉参考发现并验证准确性。

    <Check>
      经验证的研究发现已准备好进行分析和报告。
    </Check>
  </Step>

  <Step title="生成研究报告">
    将发现编汇成全面的研究报告。

    <Info>
      包含来源归属和验证状态以确保透明度。
    </Info>
  </Step>
</Steps>

***

## 跨源数据验证

在多个来源中验证研究发现：

<CodeGroup>
  ```javascript Node.js theme={null}
  async function validateResearch(findings, sources) {
    const validationResults = await Promise.all(
      findings.map(finding => 
        validateAgainstSources(finding, sources)
      )
    );
    
    return validationResults.filter(result => result.confidence > 0.8);
  }

  async function validateAgainstSources(finding, sources) {
    // 在来源间交叉参考发现
    const matches = await Promise.all(
      sources.map(source => checkMatch(finding, source))
    );
    
    const confidence = matches.filter(m => m).length / sources.length;
    return { finding, confidence, sources: matches };
  }
  ```

  ```python Python theme={null}
  import asyncio

  async def validate_research(findings, sources):
      validation_results = await asyncio.gather(*[
          validate_against_sources(finding, sources)
          for finding in findings
      ])
      
      return [r for r in validation_results if r['confidence'] > 0.8]

  async def validate_against_sources(finding, sources):
      # 在来源间交叉参考发现
      matches = await asyncio.gather(*[
          check_match(finding, source)
          for source in sources
      ])
      
      confidence = sum(matches) / len(sources)
      return {'finding': finding, 'confidence': confidence, 'sources': matches}
  ```
</CodeGroup>

***

## 企业研究模板

使用预构建的模板用于常见研究工作流：

<CardGroup cols={2}>
  <Card title="竞争情报" icon="chart-line" href="/cn/datasets/scrapers/scrapers-library">
    用于竞争分析和市场研究的模板
  </Card>

  <Card title="市场分析" icon="building" href="/cn/datasets/deep-lookup/overview">
    用于全面市场研究的模板
  </Card>

  <Card title="调查研究" icon="search" href="/cn/scraping-automation/serp-api/introduction">
    用于调查研究工作流的模板
  </Card>

  <Card title="趋势分析" icon="trending-up" href="/cn/datasets/archive/overview">
    用于历史趋势分析的模板
  </Card>
</CardGroup>

***

## 示例

### 竞争情报研究

在多个来源中研究竞争对手：

<CodeGroup>
  ```javascript Node.js theme={null}
  async function researchCompetitor(competitorName) {
    // 搜索实时数据
    const serpResults = await searchSERP(`${competitorName} pricing features`);
    
    // 搜索历史数据
    const archiveResults = await searchArchive(competitorName, '2023-01-01');
    
    // 提取网站特定数据
    const siteData = await extractFromSite(`https://${competitorName}.com`);
    
    // 交叉参考发现
    const validated = await validateResearch([
      ...serpResults,
      ...archiveResults,
      siteData
    ]);
    
    return {
      competitor: competitorName,
      findings: validated,
      sources: ['serp', 'archive', 'site']
    };
  }
  ```

  ```python Python theme={null}
  import asyncio

  async def research_competitor(competitor_name):
      # 搜索实时数据
      serp_results = await search_serp(f'{competitor_name} pricing features')
      
      # 搜索历史数据
      archive_results = await search_archive(competitor_name, '2023-01-01')
      
      # 提取网站特定数据
      site_data = await extract_from_site(f'https://{competitor_name}.com')
      
      # 交叉参考发现
      validated = await validate_research([
          *serp_results,
          *archive_results,
          site_data
      ])
      
      return {
          'competitor': competitor_name,
          'findings': validated,
          'sources': ['serp', 'archive', 'site']
      }
  ```
</CodeGroup>

### 市场研究工作流

进行全面的市场研究：

<CodeGroup>
  ```javascript Node.js theme={null}
  async function conductMarketResearch(topic) {
    // 第1步：搜索当前趋势
    const currentTrends = await searchSERP(`${topic} trends 2024`);
    
    // 第2步：分析历史趋势
    const historicalTrends = await searchArchive(topic, '2020-01-01');
    
    // 第3步：提取竞争对手数据
    const competitors = await findCompetitors(topic);
    const competitorData = await Promise.all(
      competitors.map(c => researchCompetitor(c))
    );
    
    // 第4步：验证和编汇
    const researchReport = {
      topic,
      currentTrends,
      historicalTrends,
      competitors: competitorData,
      validated: true
    };
    
    return researchReport;
  }
  ```

  ```python Python theme={null}
  import asyncio

  async def conduct_market_research(topic):
      # 第1步：搜索当前趋势
      current_trends = await search_serp(f'{topic} trends 2024')
      
      # 第2步：分析历史趋势
      historical_trends = await search_archive(topic, '2020-01-01')
      
      # 第3步：提取竞争对手数据
      competitors = await find_competitors(topic)
      competitor_data = await asyncio.gather(*[
          research_competitor(c)
          for c in competitors
      ])
      
      # 第4步：验证和编汇
      research_report = {
          'topic': topic,
          'current_trends': current_trends,
          'historical_trends': historical_trends,
          'competitors': competitor_data,
          'validated': True
      }
      
      return research_report
  ```
</CodeGroup>

***

## 后续步骤

<CardGroup cols={2}>
  <Card title="SERP API 快速开始" icon="rocket" href="/cn/search-api-quickstart">
    开始收集用于研究的搜索结果
  </Card>

  <Card title="浏览器 API 快速开始" icon="rocket" href="/cn/browser-api-quickstart">
    自动化复杂网站导航以进行研究
  </Card>

  <Card title="网络存档" icon="rocket" href="/cn/datasets/archive/overview">
    访问历史数据以进行趋势分析
  </Card>

  <Card title="深度查询" icon="rocket" href="/cn/datasets/deep-lookup/overview">
    使用深度查询进行全面研究
  </Card>
</CardGroup>

<Info>
  **需要帮助？** 查看我们的[研究示例](/cn/scraping-automation/serp-api/get-top-100-google-results)或[联系支持](https://www.bright.cn/contact)。
</Info>
