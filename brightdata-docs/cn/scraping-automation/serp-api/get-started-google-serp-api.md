> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 使用 Google SERP API 入门

> 通过 Bright Data 的 Google SERP API 快速开始：登录、创建 SERP zone、获取 API key，并开始收集 Google 搜索数据。

## 几分钟内发送您的第一个请求

使用此现成代码示例，可在几分钟内测试 Google SERP API。

<CardGroup cols={3}>
  <Card title="Postman 示例" icon="user-astronaut" iconType="regular" href="https://www.postman.com/bright-data-api/bright-data-api/request/kpq952m/google-search" cta="在 1 分钟内尝试 Google SERP API" />

  <Card title="Node.js 示例" icon="code" iconType="regular" href="https://github.com/luminati-io/bright-data-serp-api-nodejs-project" cta="在 2 分钟内尝试 Google SERP API" />

  <Card title="Python 示例" icon="code" iconType="regular" href="https://github.com/brightdata/bright-data-serp-api-python-project" cta="在 5 分钟内尝试 Google SERP API" />
</CardGroup>

## Google SERP API 快速入门示例

运行以下基础示例以检查您的 Google SERP API 是否工作正常（记得更新 API key 和查询内容）：

<CodeGroup>
  ```shell cURL theme={null}
  curl -X POST https://api.brightdata.com/request \
    --header "Content-Type: application/json" \
    --header "Authorization: Bearer API_KEY" \
    --data '{
      "zone": "serp_api1",
      "url": "https://www.google.com/search?q=pizza",
      "format": "raw"
    }'
  ```

  ```javascript google-serp.js theme={null}
  (async () => {
    const response = await fetch('https://api.brightdata.com/request', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer API_KEY'
      },
      body: JSON.stringify({
        zone: 'serp_api1',
        url: 'https://www.google.com/search?q=pizza',
        format: 'raw'
      })
    });
    
    const data = await response.text();
    console.log(data);
  })();
  ```

  ```python google_serp.py theme={null}
  import requests

  # API 配置
  headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer API_KEY',
  }

  payload = {
      'zone': 'serp_api1',
      'url': 'https://www.google.com/search?q=pizza',
      'format': 'raw'
  }

  # 发送请求
  response = requests.post(
      'https://api.brightdata.com/request', 
      json=payload, 
      headers=headers
  )

  print(response.text)
  ```
</CodeGroup>

## Google SERP API 入门链接

* [SERP API 介绍](/cn/scraping-automation/serp-api/introduction)
* [获取 API key](/cn/api-reference/authentication)
* [Google 查询参数](/cn/scraping-automation/serp-api/query-parameters/google)
