> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 一次 API 调用获取 Google 前 100 条结果

> 通过单次请求获取 Google 搜索结果第 1-100 位，并可完全控制语言、地理位置和分页深度，同时包括 AI Overview 提取。

<Note>
  本指南使用 Scrapers（Datasets）一次请求返回 Google SERP 第 1-100 位。您可以控制语言、地理定位、分页深度和设备类型。
</Note>

## 前置条件

开始前，请确保您拥有：

* 一个有效的 Bright Data 账户
* API key（在仪表盘 **API Tokens** 中可找到）
* Dataset ID：`gd_mfz5x93lmsjjjylob`

<Note>
  **计费说明：** 一次成功的 API 调用 = 一次计费请求，无论分页深度如何。包含重试，无额外带宽费用。详情请参见 [SERP 定价与计费](/cn/scraping-automation/serp-api/pricing-and-billing)。
</Note>

## 快速开始

尝试以下示例，一次请求获取前 100 条结果。将 `${API_KEY}` 替换为您的实际 API key。

<CardGroup cols={1}>
  <Card title="在 Postman 测试" icon="user-astronaut" iconType="regular" href="https://www.postman.com/bright-data-api/bright-data-api/request/h7ov9x5/google-serp-100-results">
    预配置的 Google SERP 前 100 条结果集合
  </Card>
</CardGroup>

### 基本示例

该示例返回大约 100 条结果（10 页 × 每页约 10 条）：

<CodeGroup>
  ```bash cURL theme={null}
  curl -X POST "https://api.brightdata.com/datasets/v3/trigger?dataset_id=gd_mfz5x93lmsjjjylob&include_errors=true" \
    -H "Authorization: Bearer ${API_KEY}" \
    -H "Content-Type: application/json" \
    -d '[{
      "url": "https://www.google.com/",
      "keyword": "pizza",
      "language": "en",
      "country": "US",
      "start_page": 1,
      "end_page": 10
    }]'
  ```

  ```js Node.js theme={null}
  import fetch from "node-fetch";

  const API_KEY = process.env.API_KEY;
  const DATASET_ID = "gd_mfz5x93lmsjjjylob";

  const payload = [
    {
      url: "https://www.google.com/",
      keyword: "pizza",
      language: "en",
      country: "US",
      start_page: 1,
      end_page: 10,
    },
  ];

  const res = await fetch(
    `https://api.brightdata.com/datasets/v3/trigger?dataset_id=${DATASET_ID}&include_errors=true`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${API_KEY}`,
      },
      body: JSON.stringify(payload),
    }
  );

  const job = await res.json();
  console.log(job); // 包含用于状态检查和下载的 snapshot_id
  ```

  ```py Python theme={null}
  import os
  import json
  import requests

  API_KEY = os.environ.get("API_KEY")
  DATASET_ID = "gd_mfz5x93lmsjjjylob"

  payload = [
      {
          "url": "https://www.google.com/",
          "keyword": "pizza",
          "language": "en",
          "country": "US",
          "start_page": 1,
          "end_page": 10
      }
  ]

  res = requests.post(
      f"https://api.brightdata.com/datasets/v3/trigger?dataset_id={DATASET_ID}&include_errors=true",
      headers={
          "Authorization": f"Bearer {API_KEY}",
          "Content-Type": "application/json",
      },
      data=json.dumps(payload),
  )

  print(res.json())  # 包含用于状态检查的 snapshot_id
  ```
</CodeGroup>

### 关键参数

| 参数           | 类型      | 描述               | 示例             |
| ------------ | ------- | ---------------- | -------------- |
| `keyword`    | string  | 搜索关键词            | `"pizza"`      |
| `language`   | string  | UI 语言（ISO 639-1） | `"en"`, `"de"` |
| `country`    | string  | 地理位置（ISO 3166-1） | `"US"`, `"DE"` |
| `start_page` | integer | 起始页              | `1`            |
| `end_page`   | integer | 结束页              | `10`（约前 100 条） |

<Tip>
  **分页范围：** 使用 `start_page` 和 `end_page` 控制深度：

  * `1..2` ≈ 前 20 条结果
  * `1..5` ≈ 前 50 条结果
  * `1..10` ≈ 前 100 条结果

  较小范围完成更快，返回的 payload 更小。
</Tip>

## AI Overview 提取

当搜索查询可用时，API 会自动捕获 **Google AI Overview**。

### 什么是 AI Overview？

AI Overview 是 Google 自动生成的摘要，显示在搜索结果顶部，提供来自多个来源的快速答案。

### 返回字段

AI Overview 文本返回在 `aio_text` 字段中：

```json theme={null}
{
  "keyword": "does honey expire?",
  "aio_text": "No, pure honey does not expire , as its high sugar content, low moisture, and acidity create an environment hostile to bacteria. While pure honey can last indefinitely, commercial honey may have a \"best by\" date for quality rather than safety...",
  "organic": [...],
  "people_also_ask": [...]
}
```

<Note>
  **AI Overview 可用性：** 如果搜索结果没有显示 AI Overview，则 `aio_text` 字段为空或 null。
</Note>

### 示例处理

```js theme={null}
const results = await response.json();

results.forEach(result => {
  if (result.aio_text) {
    console.log('AI Overview:', result.aio_text);
    
    // 拆分成多个段落
    const sections = result.aio_text.split('\n\n');
    sections.forEach(section => console.log(section));
  }
});
```

## 理解异步工作流

Scrapers 为异步工作模式，工作流程如下：

1. **触发请求** → 获取 `snapshot_id`
2. **监控进度** → 使用 `snapshot_id` 查看状态
3. **下载结果** → 完成后获取数据

### API 端点

| 操作   | 方法   | 端点                                                     |
| ---- | ---- | ------------------------------------------------------ |
| 触发请求 | POST | `/datasets/v3/trigger?dataset_id=gd_mfz5x93lmsjjjylob` |
| 检查进度 | GET  | `/datasets/v3/progress/{snapshot_id}`                  |
| 下载结果 | GET  | `/datasets/v3/snapshot/{snapshot_id}`                  |

<Info>
  了解更多异步工作流，请参见 [异步请求](/cn/scraping-automation/serp-api/asynchronous-requests)。
</Info>

### 完整工作流示例

<CodeGroup>
  ```js Node.js theme={null}
  import fetch from "node-fetch";

  const API_KEY = process.env.API_KEY;
  const DATASET_ID = "gd_mfz5x93lmsjjjylob";

  // 步骤 1：触发请求
  const triggerRes = await fetch(
    `https://api.brightdata.com/datasets/v3/trigger?dataset_id=${DATASET_ID}&include_errors=true`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${API_KEY}`,
      },
      body: JSON.stringify([
        {
          url: "https://www.google.com/",
          keyword: "pizza",
          language: "en",
          country: "US",
          start_page: 1,
          end_page: 10,
        },
      ]),
    }
  );

  const { snapshot_id } = await triggerRes.json();

  // 步骤 2：轮询完成状态
  let progress;
  do {
    await new Promise((resolve) => setTimeout(resolve, 5000)); // 等待 5 秒
    const progressRes = await fetch(
      `https://api.brightdata.com/datasets/v3/progress/${snapshot_id}`,
      {
        headers: { Authorization: `Bearer ${API_KEY}` },
      }
    );
    progress = await progressRes.json();
  } while (progress.status !== "ready");

  // 步骤 3：下载结果
  const downloadRes = await fetch(
    `https://api.brightdata.com/datasets/v3/snapshot/${snapshot_id}?format=json`,
    {
      headers: { Authorization: `Bearer ${API_KEY}` },
    }
  );

  const results = await downloadRes.json();
  console.log(results);
  ```

  ```python Python theme={null}
  import os
  import time
  import requests

  API_KEY = os.getenv("API_KEY")
  DATASET_ID = "gd_mfz5x93lmsjjjylob"

  # 步骤 1：触发请求
  trigger_url = f"https://api.brightdata.com/datasets/v3/trigger?dataset_id={DATASET_ID}&include_errors=true"
  trigger_response = requests.post(
      trigger_url,
      headers={
          "Content-Type": "application/json",
          "Authorization": f"Bearer {API_KEY}",
      },
      json=[{
          "url": "https://www.google.com/",
          "keyword": "pizza",
          "language": "en",
          "country": "US",
          "start_page": 1,
          "end_page": 10,
      }],
  )

  snapshot_id = trigger_response.json()["snapshot_id"]

  # 步骤 2：轮询完成状态
  progress = None
  while progress is None or progress["status"] != "ready":
      time.sleep(5)  # 等待 5 秒
      progress_url = f"https://api.brightdata.com/datasets/v3/progress/{snapshot_id}"
      progress_response = requests.get(
          progress_url,
          headers={"Authorization": f"Bearer {API_KEY}"},
      )
      progress = progress_response.json()

  # 步骤 3：下载结果
  download_url = f"https://api.brightdata.com/datasets/v3/snapshot/{snapshot_id}?format=json"
  download_response = requests.get(
      download_url,
      headers={"Authorization": f"Bearer {API_KEY}"},
  )

  results = download_response.json()
  print(results)
  ```
</CodeGroup>

## 高级配置

### 批量多个查询

一次请求处理多个搜索查询：

```json theme={null}
[
  {
    "url": "https://www.google.com/",
    "keyword": "pizza",
    "language": "en",
    "country": "US",
    "start_page": 1,
    "end_page": 10
  },
  {
    "url": "https://www.google.com/",
    "keyword": "coffee",
    "language": "de",
    "country": "DE",
    "start_page": 1,
    "end_page": 10
  },
  {
    "url": "https://www.google.com/",
    "keyword": "running shoes",
    "language": "en",
    "country": "GB",
    "start_page": 1,
    "end_page": 5
  }
]
```

### 移动端搜索结果

添加 `"brd_mobile": true` 获取移动端 SERP 数据：

```bash cURL theme={null}
curl -X POST "https://api.brightdata.com/datasets/v3/trigger?dataset_id=gd_mfz5x93lmsjjjylob&include_errors=true" \
  -H "Authorization: Bearer ${API_KEY}" \
  -H "Content-Type: application/json" \
  -d '[{
    "url": "https://www.google.com/",
    "keyword": "running shoes",
    "language": "en",
    "country": "US",
    "start_page": 1,
    "end_page": 10,
    "brd_mobile": true
  }]'
```

### 从 Web 标签页获取结果（udm=14）

Google 的 `udm` 参数定义了 SERP 来自哪个搜索标签页。Bright Data SERP Scraper 将原生 Google 的 `udm` 值映射到其自己的请求参数 `udm_web`。

要获取 **Web** 标签页（即 Google 上的 `udm=14`）的结果，请在请求中将 `udm_web` 设置为 `true`：

<Note>
  `udm_web` 参数无法与 `tbm` 参数同时使用。
</Note>

```bash cURL theme={null}
curl -X POST "https://api.brightdata.com/datasets/v3/trigger?dataset_id=gd_mfz5x93lmsjjjylob&include_errors=true" \
  -H "Authorization: Bearer ${API_KEY}" \
  -H "Content-Type: application/json" \
  -d '[{
    "url": "https://www.google.com/",
    "keyword": "pizza kraków",
    "language": "pl",
    "country": "PL",
    "uule": "w+CAIQICIGUG9sYW5k",
    "udm_web": true,
    "include_paginated_html": true
  }]'
```

### 包含 HTML 快照

同时捕获原始 HTML 以便审计或自定义解析：

```json theme={null}
{
  "url": "https://www.google.com/",
  "keyword": "pizza",
  "language": "en",
  "country": "US",
  "start_page": 1,
  "end_page": 10,
  "include_paginated_html": true
}
```

启用后，结果中每页将包含 `pagination[].page_html`。

### 本地化示例

通过语言和国家组合定位特定市场：

```json theme={null}
// 德语，德国
{
  "keyword": "laufschuhe",
  "language": "de",
  "country": "DE",
  "start_page": 1,
  "end_page": 5
}

// 英语，英国
{
  "keyword": "trainers",
  "language": "en",
  "country": "GB",
  "start_page": 1,
  "end_page": 10
}

// 西班牙语，墨西哥
{
  "keyword": "zapatos deportivos",
  "language": "es",
  "country": "MX",
  "start_page": 1,
  "end_page": 10
}
```

## 常见问题

<AccordionGroup>
  <Accordion title="如何选择特定的输出字段？">
    您可以选择返回所有页面的解析字段。若要同时包含每页的原始 HTML，请在请求中添加 `"include_paginated_html": true`。这样会在解析字段旁返回 `pagination[].page_html`。
  </Accordion>

  <Accordion title="我可以控制 AI Overview (AIO) 的显示吗？">
    当 Google 显示 AI Overview 且输出字段中包含该字段时，它会返回。未来将提供开关以显式包含或排除 AIO。
  </Accordion>

  <Accordion title="浏览器工作器实现有什么变化？">
    我们现在使用浏览器工作器进行 SERP 抓取。这减少了重复结果，提高了分页间的会话连续性，并支持更丰富的输出（例如 AI Overview）。所有现有请求仍向后兼容。
  </Accordion>

  <Accordion title="Top 100 结果的计费方式是什么？">
    一次成功的 API 调用 = 一次计费请求，即使它返回了 10 页共 100+ 结果。重试请求自动包含在内，无额外带宽费用。完整详情请参见 [SERP 计费](/cn/scraping-automation/serp-api/pricing-and-billing)。
  </Accordion>

  <Accordion title="language 和 country 参数有什么区别？">
    * `language`：控制 Google 使用的界面语言（例如 `"en"`、`"de"`、`"es"`）
    * `country`：控制结果的地理位置（例如 `"US"`、`"DE"`、`"MX"`）

    这两个参数可以独立组合，以针对特定市场。
  </Accordion>

  <Accordion title="获取结果需要多长时间？">
    时间取决于查询复杂度和页面深度。较小的页面范围（例如 `1..2`）完成速度快于较大范围（例如 `1..10`）。可使用 Progress API 监控请求状态。
  </Accordion>
</AccordionGroup>

## 下一步

<CardGroup cols={2}>
  <Card title="计费与费用" icon="credit-card" href="/cn/scraping-automation/serp-api/pricing-and-billing">
    了解请求的计费方式
  </Card>

  <Card title="Google 查询参数" icon="sliders" href="/cn/scraping-automation/serp-api/query-parameters/google">
    探索所有可用参数
  </Card>

  <Card title="解析后的 JSON 结果" icon="code" href="/cn/scraping-automation/serp-api/parsed-json-results/parsing-search-results">
    了解响应结构
  </Card>

  <Card title="异步请求" icon="clock" href="/cn/scraping-automation/serp-api/asynchronous-requests">
    深入异步工作流
  </Card>
</CardGroup>
