> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Bing 到 Bright Data SERP 迁移指南

> 逐步指南，教你如何将 Bing Search API 迁移到 Bright Data Bing SERP API。

<Warning>
  [Microsoft Bing Search API 将于 2025 年 8 月 11 日退休](https://learn.microsoft.com/en-us/lifecycle/announcements/bing-search-api-retirement)。Bright Data 的 Bing SERP API 仍将继续支持。
</Warning>

<Info>
  **迁移优势**

  * 最小代码更改即可替换
  * 1:1 兼容 JSON 响应结构
  * 增强的请求灵活性，支持基于查询和基于 URL 的请求
</Info>

## 快速开始迁移（5 分钟）

<Steps>
  <Step title="获取 API Key">
    [注册 Bright Data](https://www.bright.cn/?hs_signup=1\&utm_source=docs) 并在仪表板获取 API key。
  </Step>

  <Step title="更新端点">
    将 `api.bing.microsoft.com` 替换为 `api.brightdata.com/request`
  </Step>

  <Step title="在请求体中添加参数并测试首个请求">
    ```bash theme={null}
    curl -X POST 'https://api.brightdata.com/request' \
      -H "Authorization: Bearer YOUR_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "search_engine": "bing",
        "query": "test search",
        "data_format": "parsed_bing_api",
        "format": "json",
        "zone": "your_zone_name_"
      }'
    ```
  </Step>
</Steps>

## 逐步迁移指南

### 步骤 1：账户设置

<AccordionGroup>
  <Accordion title="1.1 创建 Bright Data 账户">
    1. 访问 [brightdata.com/signup](https://www.bright.cn/?hs_signup=1\&utm_source=docs)
    2. 导航至 **Zones** → **Create Zone** → **SERP API**
    3. 复制你的 API key 凭据
  </Accordion>

  <Accordion title="1.2 配置认证">
    用 Bright Data 凭据替换你的 Bing API key：

    **之前（Bing）:**

    ```http theme={null}
    Ocp-Apim-Subscription-Key: YOUR_BING_KEY
    ```

    **之后（Bright Data）:**

    ```http theme={null}
    Authorization: Bearer YOUR_BRIGHTDATA_API_KEY
    ```
  </Accordion>
</AccordionGroup>

### 步骤 2：更新请求格式

<Tabs>
  <Tab title="cURL">
    **之前（Bing API）:**

    ```bash theme={null}
    curl -X GET "https://api.bing.microsoft.com/v7.0/search?q=openai" \
      -H "Ocp-Apim-Subscription-Key: YOUR_BING_KEY"
    ```

    **之后（Bright Data）:**

    ```sh theme={null}
    curl -X POST "https://api.brightdata.com/request" \
      -H "Authorization: Bearer YOUR_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "search_engine": "bing",
        "query": "openai",
        "data_format": "parsed_bing_api",
        "format": "json",
        "zone": "your_zone_name"
      }'
    ```
  </Tab>

  <Tab title="Python">
    **之前（Bing API）:**

    ```python theme={null}
    import requests

    headers = {
        'Ocp-Apim-Subscription-Key': 'YOUR_BING_KEY'
    }

    response = requests.get(
        'https://api.bing.microsoft.com/v7.0/search',
        headers=headers,
        params={'q': 'openai'}
    )
    ```

    **之后（Bright Data）:**

    ```python theme={null}
    import requests

    headers = {
        'Authorization': 'Bearer YOUR_API_KEY',
        'Content-Type': 'application/json'
    }

    payload = {
        'search_engine': 'bing',
        'query': 'openai',
        'data_format': 'parsed_bing_api',
        'format': 'json',
        'zone': 'your_zone_name'
    }

    response = requests.post(
        'https://api.brightdata.com/request',
        headers=headers,
        json=payload
    )
    ```
  </Tab>

  <Tab title="Node.js">
    **之前（Bing API）:**

    ```javascript theme={null}
    const axios = require('axios');

    const response = await axios.get(
        'https://api.bing.microsoft.com/v7.0/search',
        {
            headers: {
                'Ocp-Apim-Subscription-Key': 'YOUR_BING_KEY'
            },
            params: { q: 'openai' }
        }
    );
    ```

    **之后（Bright Data）:**

    ```javascript theme={null}
    const axios = require('axios');

    const response = await axios.post(
        'https://api.brightdata.com/request',
        {
            search_engine: 'bing',
            query: 'openai',
            data_format: 'parsed_bing_api',
            format: 'json',
            zone: 'your_zone_name'
        },
        {
            headers: {
                'Authorization': 'Bearer YOUR_API_KEY',
                'Content-Type': 'application/json'
            }
        }
    );
    ```
  </Tab>
</Tabs>

### 步骤 3：处理响应格式

使用 `data_format: "parsed_bing_api"` 时，响应格式与 Bing API 保持一致：

<CodeGroup>
  ```json Response Structure theme={null}
  {
    "_type": "SearchResponse",
    "queryContext": {
      "originalQuery": "openai"
    },
    "webPages": {
      "totalEstimatedMatches": 12300000,
      "value": [
        {
          "name": "OpenAI",
          "url": "https://openai.com/",
          "displayUrl": "openai.com",
          "snippet": "OpenAI is an AI research and deployment company..."
        }
      ]
    },
    "images": { "value": [...] },
    "videos": { "value": [...] },
    "relatedSearches": { "value": [...] }
  }
  ```

  ```python Parse Results theme={null}
  # 你现有的 Bing API 解析代码无需更改
  data = response.json()

  # 提取网页结果
  web_results = data.get('webPages', {}).get('value', [])
  for result in web_results:
      print(f"Title: {result['name']}")
      print(f"URL: {result['url']}")
      print(f"Snippet: {result['snippet']}")

  # 提取图片
  images = data.get('images', {}).get('value', [])
  for image in images:
      print(f"Image: {image['thumbnailUrl']}")
  ```
</CodeGroup>
