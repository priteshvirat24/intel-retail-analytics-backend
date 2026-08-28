> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 开始使用 Bing SERP API

> 通过 3 个步骤开始使用 Bright Data 的 Bing SERP API：登录、创建 SERP 区域、获取 API 密钥，并开始收集 Bing 搜索数据。

## 几分钟内发出您的第一个请求

使用以下现成代码示例，几分钟内即可测试 Bing SERP API。

<CardGroup cols={3}>
  <Card title="Postman 示例" icon="user-astronaut" iconType="regular" href="https://www.postman.com/bright-data-api/bright-data-api/request/uzaea2u/bing-search" cta="在不到 1 分钟内尝试 Bing SERP API" />

  <Card title="Node.js 示例" icon="code" iconType="regular" href="https://github.com/brightdata/bright-data-bing-serp-api-nodejs-project" cta="在不到 2 分钟内尝试 Bing SERP API" />

  <Card title="Python 示例" icon="code" iconType="regular" href="https://github.com/brightdata/bright-data-bing-serp-api-python-project" cta="在不到 5 分钟内尝试 Bing SERP API" />
</CardGroup>

## Bing SERP API 快速入门示例

运行这些基础示例以检查您的 Bing SERP API 是否正常工作（记得替换 API 密钥和查询内容）：

<CodeGroup>
  ```shell cURL theme={null}
  curl -X POST https://api.brightdata.com/request \
    --header "Content-Type: application/json" \
    --header "Authorization: Bearer API_KEY" \
    --data '{
      "zone": "serp_api1",
      "url": "https://www.bing.com/search?q=pizza",
      "format": "raw"
    }'
  ```

  ```javascript bing-serp.js theme={null}
  (async () => {
    const response = await fetch('https://api.brightdata.com/request', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer API_KEY'
      },
      body: JSON.stringify({
        zone: 'serp_api1',
        url: 'https://www.bing.com/search?q=pizza',
        format: 'raw'
      })
    });
    
    const data = await response.text();
    console.log(data);
  })();
  ```

  ```python bing_serp.py theme={null}
  import requests

  # API 配置
  headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer API_KEY',
  }

  payload = {
      'zone': 'serp_api1',
      'url': 'https://www.bing.com/search?q=pizza',
      'format': 'raw'
  }

  # 发出请求
  response = requests.post(
      'https://api.brightdata.com/request', 
      json=payload, 
      headers=headers
  )

  print(response.text)
  ```
</CodeGroup>

## Bing SERP API 入门链接

* [SERP API 介绍](/cn/scraping-automation/serp-api/introduction)
* [获取 API 密钥](/cn/api-reference/authentication)
* [Bing 查询参数](/cn/scraping-automation/serp-api/query-parameters/bing)

## Microsoft Bing API 到 Bright Data SERP API 迁移指南

[Bing API 到 Bright Data SERP API 迁移指南](/cn/scraping-automation/serp-api/parsed-json-results/bing-to-bright-data-serp-migration-guide)
