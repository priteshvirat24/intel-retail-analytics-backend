> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 快速网络搜索

Bright Data 为精选企业客户提供快速 SERP 服务。该 SERP 服务返回紧凑的 JSON 格式，为需要实时搜索结果的应用程序提供支持。要获取此服务的访问权限，请联系您的 Bright Data 账户经理。

## 开始前

<AccordionGroup>
  <Accordion title="我需要哪种 Google 搜索类型？">
    Fast SERP 支持多个 Google 垂直领域——网络搜索、新闻、购物、图片等。本页面涵盖标准网络搜索 (`google.com/search`)。如果您需要其他垂直领域，请查看该搜索类型的相关页面。
  </Accordion>

  <Accordion title="我需要多少 QPS（每秒查询数）？">
    在开始之前，请同时考虑您的 POC/测试量和预期的生产量。这有助于确保您的区域针对您的工作负载进行了正确配置。如果您不确定，请从估计开始——您的账户经理可以随着您的使用增长而调整您的速率分配。
  </Accordion>

  <Accordion title="我需要在我这边控制或限制流量吗？">
    如果您的系统具有内部速率限制或负载控制机制，请与您的账户经理共享这些��细信息。这有助于将您的区域容量与您的基础设施行为相匹配，并避免不必要的错误。
  </Accordion>

  <Accordion title="我应该使用本机代理接口还是 REST API？">
    Fast SERP 最适合使用**本机代理接口**——它比 REST API 略快。如果您的架构需要，可以提供 REST API 接口。
  </Accordion>

  <Accordion title="我的爬虫将从哪个地理区域运行？">
    Fast SERP 支持多个部署区域：**美国东部**、**美国西部**、**欧盟**和 **APAC**。提前了解您的爬虫区域有助于优化路由和延迟。如果您的生产流量分布在多个区域，请告知您的账户经理。
  </Accordion>
</AccordionGroup>

## Fast SERP 请求

Fast SERP 最适合与本机代理接口配合使用。如果您的架构需要 REST API 接口，可以提供。

<Note>
  对于 Fast SERP，**两者都需要**：`x-unblock-data-format: parsed_light` 请求头**和** `brd_json=1` URL 参数。省略其中任何一个都会导致意外的响应格式。
</Note>

### 本机代理请求

#### 有机结果

使用请求头值 `x-unblock-data-format: parsed_fast`——此请求头将返回有机结果。

```shell theme={null}
curl -i --proxy fserp.brd.superproxy.io:44445 \
  --proxy-user brd-customer-<CUSTOMER>-zone-<ZONE>:<PASSWORD> \
  -k \
  -H 'x-unblock-data-format: parsed_fast' \
  "https://www.google.com/search?q=pizza&brd_json=1" \
  > output.json
```

#### 有机结果及 Google 的"头条新闻"

使用请求头值 `x-unblock-data-format: parsed_light`——此请求头将在响应中返回 Google 的"头条新闻"以及有机结果。

```shell theme={null}
curl -i --proxy fserp.brd.superproxy.io:44445 \
  --proxy-user brd-customer-<CUSTOMER>-zone-<ZONE>:<PASSWORD> \
  -k \
  -H 'x-unblock-data-format: parsed_light' \
  "https://www.google.com/search?q=pizza&brd_json=1" \
  > output.json
```

## 响应格式

### `organic` 数组

主要的网络搜索结果数组，存在于 `parsed_light` 和 `parsed_fast` 响应中。

| 字段            | 类型  | 描述                   |
| ------------- | --- | -------------------- |
| `link`        | 字符串 | 结果页面的 URL            |
| `title`       | 字符串 | 结果的标题                |
| `description` | 字符串 | 搜索结果中显示的片段/摘要        |
| `global_rank` | 整数  | 结果在页面上的排名位置          |
| `extensions`  | 数组  | 与结果关联的网站链接的可选列表（见下文） |

#### `extensions` 项目

| 字段     | 类型  | 描述                  |
| ------ | --- | ------------------- |
| `type` | 字符串 | 扩展类型，例如 `site_link` |
| `link` | 字符串 | 网站链接的 URL           |
| `text` | 字符串 | 网站链接的锚文本            |

### `general` 对象

在每个 `parsed_light` 响应中返回。报告你提交的查询以及 Google 实际执行的查询，用于检测 Google 何时截断了搜索。

| 字段               | 类型  | 描述                                                |
| ---------------- | --- | ------------------------------------------------- |
| `query`          | 字符串 | 你提交的搜索查询                                          |
| `detected_query` | 字符串 | Google 实际返回结果的查询。当 Google 更正拼写或截断搜索时，与 `query` 不同 |

<Note>
  如果 `detected_query` 与 `query` 不同，请检查响应中是否存在 `spelling` 部分。如果存在 `spelling`，则差异是由自动拼写更正引起的，响应有效。如果 `spelling` 不存在，则查询被截断（cloaked），返回的是原始查询被截断版本的结果。
</Note>

### `spelling` 对象

仅当 Google 应用或建议拼写更正时，才在 `parsed_light` 响应中返回。所有字段均可为空，仅在 Google 提供相应变体时出现。

| 字段                    | 类型          | 描述                             |
| --------------------- | ----------- | ------------------------------ |
| `original_text`       | 字符串 \| null | 更正前的原始查询关键词                    |
| `original_link`       | 字符串 \| null | 原始查询的 Google 搜索 URL            |
| `auto_corrected_text` | 字符串 \| null | Google 改用的更正后关键词               |
| `auto_corrected_link` | 字符串 \| null | 更正后查询的 Google 搜索 URL           |
| `auto_included_text`  | 字符串 \| null | Google 自动包含在搜索中的词条             |
| `auto_included_link`  | 字符串 \| null | 自动包含词条的 Google 搜索 URL          |
| `suggested_text`      | 字符串 \| null | Google 建议的关键词（"您是不是要找"），但不改变结果 |
| `suggested_link`      | 字符串 \| null | 建议查询的 Google 搜索 URL            |
| `original_empty`      | 布尔值         | 当 Google 对原始查询未返回结果时为 `true`   |

### `top_stories` 数组

仅在使用 `x-unblock-data-format: parsed_light` 时返回。包含 Google 的"头条新闻"新闻轮播结果。

| 字段       | 类型  | 描述         |
| -------- | --- | ---------- |
| `link`   | 字符串 | 新闻文章的 URL  |
| `title`  | 字符串 | 文章的标题      |
| `source` | 字符串 | 新闻发布商的名称   |
| `date`   | 字符串 | 文章的发布日期/时间 |
| `image`  | 字符串 | 文章缩略图的 URL |

### 响应示例 — `parsed_fast`（有机结果）

```text theme={null}
{
  "organic": [
    {
      "link": "https://en.wikipedia.org/wiki/Pizza",
      "title": "Pizza - Wikipedia",
      "description": "Pizza is an Italian dish consisting of a flat base of leavened wheat-based dough topped with tomato, cheese, and other ingredients.",
      "global_rank": 1,
      "extensions": [
        {
          "type": "site_link",
          "link": "https://en.wikipedia.org/wiki/Neapolitan_pizza",
          "text": "Neapolitan pizza"
        }
      ]
    },
    {
      "link": "https://www.example-pizza.com/best-pizza-nyc",
      "title": "Best Pizza in NYC - Joe's Pizza",
      "description": "Family-owned pizzeria serving authentic New York slices since 1975.",
      "global_rank": 2
    },
    {
      "link": "https://www.pizza-guide.com/top-10",
      "title": "Top 10 Pizza Places in NYC",
      "description": "Discover the highest-rated pizza restaurants across all five boroughs.",
      "global_rank": 3
    }
  ]
}
```

### 响应示例 — `parsed_light`（包含头条新闻）

```text theme={null}
{
  "general": {
    "query": "pizza",
    "detected_query": "pizza"
  },
  "organic": [
    {
      "link": "https://en.wikipedia.org/wiki/Pizza",
      "title": "Pizza - Wikipedia",
      "description": "Pizza is an Italian dish consisting of a flat base of leavened wheat-based dough topped with tomato, cheese, and other ingredients.",
      "global_rank": 1,
      "extensions": [
        {
          "type": "site_link",
          "link": "https://en.wikipedia.org/wiki/Neapolitan_pizza",
          "text": "Neapolitan pizza"
        },
        {
          "type": "site_link",
          "link": "https://en.wikipedia.org/wiki/Pizzeria",
          "text": "Pizzeria"
        }
      ]
    },
    {
      "link": "https://www.example-pizza.com/best-pizza-nyc",
      "title": "Best Pizza in NYC - Joe's Pizza",
      "description": "Family-owned pizzeria serving authentic New York slices since 1975.",
      "global_rank": 2
    }
  ],
  "top_stories": [
    {
      "link": "https://www.example-news.com/pizza-festival",
      "title": "NYC Pizza Festival Returns This Summer",
      "source": "Example News",
      "date": "3 hours ago",
      "image": "https://www.example-news.com/images/pizza-fest.jpg"
    },
    {
      "link": "https://www.another-outlet.com/pizza-record",
      "title": "World Record Pizza Baked in Naples",
      "source": "Another Outlet",
      "date": "5 hours ago",
      "image": "https://www.another-outlet.com/images/pizza-record.jpg"
    }
  ]
}
```

<Note>
  查询截断检测和 `query_rejected` 查询拦截行为适用于整个 SERP API，而不仅仅是 Fast SERP。参见 SERP API 调试页面上的 [如何检测查询截断](/cn/scraping-automation/serp-api/debugging#如何检测查询截断) 和 [查询被拦截时会发生什么](/cn/scraping-automation/serp-api/debugging#查询被拦截时会发生什么)。
</Note>

响应架构——包含头条新闻：[https://api.brightdata.com/data\_schemas/fast\_serp/google\_search.schema.json](https://api.brightdata.com/data_schemas/fast_serp/google_search.schema.json)

响应架构——不包含头条新闻：[https://api.brightdata.com/data\_schemas/fast\_serp/google\_search\_web.schema.json](https://api.brightdata.com/data_schemas/fast_serp/google_search_web.schema.json)
