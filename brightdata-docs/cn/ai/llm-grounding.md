> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# LLM 基础化与评估

> 构建 AI 系统来事实核查模型输出、验证训练数据并将语言模型基础化在真实世界信息中。创建评估工作流，针对实时网络数据测试模型准确性。

<Card title="正在构建 AI 初创公司？" cta="了解更多" href="https://brightdata.com/ai/ai-startups-program" icon="rocket-launch" iconType="duotone" arrow="true">
  您可能符合我们的初创计划资格。获得本文所介绍基础设施的全额资助访问权限（最高价值 \$20,000）。
</Card>

# LLM 基础化与评估

构建 AI 系统来事实核查模型输出、验证训练数据并将语言模型基础化在真实世界信息中。

创建评估工作流，针对实时网络数据测试模型准确性、通过多源验证来验证声明，并通过持续的真实世界基础化来维持模型可靠性。

<CardGroup cols={2}>
  <Card title="学习事实核查" icon="lightbulb" href="#fact-checking-workflows">
    了解事实核查工作流
  </Card>

  <Card title="开始使用" icon="rocket" href="#model-output-validation">
    开始验证模型输出
  </Card>
</CardGroup>

***

## 解决的挑战

处理规模化 AI 评估的独特挑战：

* **实时事实验证** - 需要快速网络访问进行即时验证
* **综合测试** - 需要广泛的来源覆盖进行彻底的评估
* **历史验证** - 需要存档访问权限来事实核查历史声明
* **持续评估** - 需要永不宕机的可靠基础设施

从简单的事实核查到综合的模型评估框架，基础化系统需要既能提供速度又能提供可靠性的基础设施。

<CardGroup cols={2}>
  <Card title="快速网络访问" icon="bolt" href="/cn/scraping-automation/serp-api/introduction">
    实时事实验证，响应时间不足一秒
  </Card>

  <Card title="广泛源覆盖" icon="globe" href="/cn/datasets/deep-lookup/overview">
    跨多个来源的综合测试
  </Card>

  <Card title="历史验证" icon="archive" href="/cn/datasets/archive/overview">
    访问历史数据来事实核查过去的声明
  </Card>

  <Card title="可靠基础设施" icon="shield-check">
    99.99% 正常运行时间确保持续评估永不停止
  </Card>
</CardGroup>

***

## 目标

为评估模式而构建，通过严格的真实世界验证来维持模型准确性和用户信任。

***

## 事实核查工作流

针对真实世界数据验证声明：

<Steps>
  <Step title="从模型输出中提取声明">
    从需要验证的模型输出中提取事实声明。

    ```json theme={null}
    {
      "claims": [
        {
          "text": "该公司成立于 2020 年",
          "entity": "company_name",
          "type": "factual"
        }
      ]
    }
    ```
  </Step>

  <Step title="搜索验证">
    跨多个来源搜索验证：

    * 实时搜索结果 (SERP API)
    * 历史数据 (网络存档)
    * 结构化数据 (Deep Lookup)

    <CodeGroup>
      ```javascript Node.js theme={null}
      async function verifyClaim(claim) {
        const searches = await Promise.all([
          searchSERP(claim.text),
          searchArchive(claim.entity, '2020-01-01'),
          searchDeepLookup(claim.entity)
        ]);
        
        return searches;
      }
      ```

      ```python Python theme={null}
      import asyncio

      async def verify_claim(claim):
          searches = await asyncio.gather(
              search_serp(claim['text']),
              search_archive(claim['entity'], '2020-01-01'),
              search_deep_lookup(claim['entity'])
          )
          
          return searches
      ```
    </CodeGroup>
  </Step>

  <Step title="针对来源验证">
    针对多个来源验证声明并确定置信度。

    <Tip>
      使用跨源验证来提高事实核查结果的置信度。
    </Tip>
  </Step>

  <Step title="报告验证结果">
    报告带有来源归属和置信度分数的验证结果。

    <Check>
      已验证的声明用置信度分数和来源参考进行标记。
    </Check>
  </Step>
</Steps>

***

## 模型输出验证

实时验证模型输出：

<CodeGroup>
  ```javascript Node.js theme={null}
  async function validateModelOutput(output, claims) {
    const validationPromises = claims.map(claim => 
      verifyClaim(claim)
    );
    
    const validationResults = await Promise.all(validationPromises);
    
    const validatedOutput = {
      original: output,
      claims: validationResults.map((result, index) => ({
        claim: claims[index],
        verified: result.confidence > 0.8,
        confidence: result.confidence,
        sources: result.sources
      }))
    };
    
    return validatedOutput;
  }
  ```

  ```python Python theme={null}
  import asyncio

  async def validate_model_output(output, claims):
      validation_tasks = [verify_claim(claim) for claim in claims]
      validation_results = await asyncio.gather(*validation_tasks)
      
      validated_output = {
          'original': output,
          'claims': [
              {
                  'claim': claim,
                  'verified': result['confidence'] > 0.8,
                  'confidence': result['confidence'],
                  'sources': result['sources']
              }
              for claim, result in zip(claims, validation_results)
          ]
      }
      
      return validated_output
  ```
</CodeGroup>

***

## 训练数据验证

针对真实世界来源验证训练数据：

<CodeGroup>
  ```javascript Node.js theme={null}
  async function verifyTrainingData(dataset) {
    const verificationResults = await Promise.all(
      dataset.map(item => verifyDataItem(item))
    );
    
    const verified = verificationResults.filter(r => r.verified);
    const unverified = verificationResults.filter(r => !r.verified);
    
    return {
      total: dataset.length,
      verified: verified.length,
      unverified: unverified.length,
      accuracy: verified.length / dataset.length,
      issues: unverified
    };
  }
  ```

  ```python Python theme={null}
  import asyncio

  async def verify_training_data(dataset):
      verification_tasks = [verify_data_item(item) for item in dataset]
      verification_results = await asyncio.gather(*verification_tasks)
      
      verified = [r for r in verification_results if r['verified']]
      unverified = [r for r in verification_results if not r['verified']]
      
      return {
          'total': len(dataset),
          'verified': len(verified),
          'unverified': len(unverified),
          'accuracy': len(verified) / len(dataset),
          'issues': unverified
      }
  ```
</CodeGroup>

***

## 使用存档进行历史事实验证

使用网络存档验证历史声明：

<CodeGroup>
  ```javascript Node.js theme={null}
  async function validateHistoricalFact(claim, date) {
    // 搜索存档中的历史数据
    const archiveResults = await searchArchive(claim.entity, date);
    
    // 与声明进行比较
    const matches = archiveResults.filter(result => 
      result.text.includes(claim.text)
    );
    
    return {
      claim,
      date,
      verified: matches.length > 0,
      confidence: matches.length / archiveResults.length,
      sources: matches
    };
  }
  ```

  ```python Python theme={null}
  import asyncio

  async def validate_historical_fact(claim, date):
      # 搜索存档中的历史数据
      archive_results = await search_archive(claim['entity'], date)
      
      # 与声明进行比较
      matches = [
          result for result in archive_results
          if claim['text'] in result['text']
      ]
      
      return {
          'claim': claim,
          'date': date,
          'verified': len(matches) > 0,
          'confidence': len(matches) / len(archive_results) if archive_results else 0,
          'sources': matches
      }
  ```
</CodeGroup>

***

## 多源交叉引用

跨多个来源交叉引用事实：

<CodeGroup>
  ```javascript Node.js theme={null}
  async function crossReferenceFact(fact) {
    const sources = await Promise.all([
      searchSERP(fact.query),
      searchDeepLookup(fact.entity),
      searchArchive(fact.entity, fact.date),
      searchSite(fact.url)
    ]);
    
    // 查找来源间的共同发现
    const commonFindings = findCommonFindings(sources);
    
    return {
      fact,
      sources: sources.length,
      commonFindings,
      confidence: commonFindings.length / sources.length,
      validated: commonFindings.length >= sources.length * 0.7
    };
  }
  ```

  ```python Python theme={null}
  import asyncio

  async def cross_reference_fact(fact):
      sources = await asyncio.gather(
          search_serp(fact['query']),
          search_deep_lookup(fact['entity']),
          search_archive(fact['entity'], fact['date']),
          search_site(fact['url'])
      )
      
      # 查找来源间的共同发现
      common_findings = find_common_findings(sources)
      
      return {
          'fact': fact,
          'sources': len(sources),
          'common_findings': common_findings,
          'confidence': len(common_findings) / len(sources) if sources else 0,
          'validated': len(common_findings) >= len(sources) * 0.7
      }
  ```
</CodeGroup>

***

## 持续评估系统

构建用于持续模型验证的持续评估系统：

<CardGroup cols={2}>
  <Card title="实时监控" icon="chart-line" href="/general/usage-monitoring/Usage">
    实时监控模型输出进行持续验证
  </Card>

  <Card title="自动化测试" icon="robot" href="/cn/scraping-automation/serp-api/introduction">
    自动化事实核查工作流进行持续评估
  </Card>

  <Card title="警报系统" icon="bell" href="/general/webhook_notifications">
    为未验证的声明或低置信度分数设置警报
  </Card>

  <Card title="性能跟踪" icon="chart-bar" href="/general/usage-monitoring/fair_use_allowance">
    跟踪评估性能和模型准确性随时间的变化
  </Card>
</CardGroup>

***

## 模板

使用预构建的通用基础化工作流模板：

<CardGroup cols={2}>
  <Card title="事实核查模板" icon="check-circle" href="/cn/scraping-automation/serp-api/introduction">
    实时事实核查工作流模板
  </Card>

  <Card title="模型评估模板" icon="clipboard-check" href="/cn/datasets/deep-lookup/overview">
    综合模型评估模板
  </Card>

  <Card title="训练数据验证" icon="database" href="/cn/datasets/data-validation/data-validation-for-customers">
    验证训练数据集的模板
  </Card>

  <Card title="历史验证" icon="archive" href="/cn/datasets/archive/overview">
    历史事实验证模板
  </Card>
</CardGroup>

***

## 后续步骤

<CardGroup cols={2}>
  <Card title="SERP API 快速开始" icon="rocket" href="/search-api-quickstart">
    开始使用实时搜索结果进行事实核查
  </Card>

  <Card title="Deep Lookup 快速开始" icon="rocket" href="/deep-lookup-quickstart">
    使用 Deep Lookup 进行综合事实验证
  </Card>

  <Card title="网络存档" icon="rocket" href="/cn/datasets/archive/overview">
    访问历史数据进行事实核查
  </Card>

  <Card title="浏览示例" icon="code" href="/cn/datasets/deep-lookup/code-examples">
    探索基础化和评估示例
  </Card>
</CardGroup>

<Info>
  **需要帮助？** 查看我们的 [评估示例](/cn/datasets/deep-lookup/code-examples) 或 [��系支持](https://www.bright.cn/contact)。
</Info>
