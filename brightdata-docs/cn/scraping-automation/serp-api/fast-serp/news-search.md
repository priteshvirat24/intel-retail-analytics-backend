> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 快速新闻搜索

Bright Data 为 Google 新闻提供快速 SERP 服务，仅向精选企业客户开放。此服务以紧凑的 JSON 格式响应，可为需要最新新闻结果的实时应用提供支持。如需获取访问权限，请联系您的 Bright Data 账户经理。

## 开始前

<AccordionGroup>
  <Accordion title="我需要哪种 Google 搜索类型？">
    快速 SERP 支持多个 Google 搜索垂直领域。对于新闻结果，您应该定位到 `google.com/search?tbm=nws` — **而不是** `news.google.com`。这两个端点返回不同的响应结构；本页面仅涵盖 `google.com/search?tbm=nws`。
  </Accordion>

  <Accordion title="我需要多少 QPS（每秒查询数）？">
    在开始之前，请同时考虑您的 POC/测试流量和预期的生产流量。这有助于确保您的区域配置正确。如果您不确定，可以先从估计值开始 — 您的账户经理可以根据您的使用情况增加调整速率分配。
  </Accordion>

  <Accordion title="我需要在自己的一端控制或限制流量吗？">
    如果您的系统有内部速率限制或负载控制机制，请与您的账户经理分享这些详细信��。这有助于使您的区域容量与基础架构的行为保持一致，并避免不必要的错误。
  </Accordion>

  <Accordion title="我应该使用本机代理接口还是 REST API？">
    快速 SERP 最适合使用**本机代理接口** — 它比 REST API 略快。如果您的架构需要，可以提供 REST API 接口。
  </Accordion>

  <Accordion title="我的爬虫将从哪个地理区域运行？">
    快速 SERP 支持多个部署区域：**美国东部**、**美国西部**、**欧盟** 和 **亚太地区**。提前了解您的爬虫区域有助于优化路由和延迟。如果您的生产流量分布在多个区域，请告知您的账户经理。
  </Accordion>
</AccordionGroup>

## 快速新闻搜索请求

快速 SERP for Google 新闻最适合使用本机代理接口。如果您的架构需要 REST API 接口，我们可以提供。

<Note>
  对于快速 SERP，**同时**需要 `x-unblock-data-format: parsed_light` 请求头**和** `brd_json=1` URL 参数。省略其中任何一个都会导致意外的响应格式。
</Note>

### 本机代理请求

```shell theme={null}
curl -i --proxy fserp.brd.superproxy.io:44445 \
  --proxy-user brd-customer-<CUSTOMER>-zone-<ZONE>:<PASSWORD> \
  -k \
  -H 'x-unblock-data-format: parsed_light' \
  "https://www.google.com/search?q=earthquake&tbm=nws&brd_json=1"
```

## 响应格式

成功的响应返回一个 JSON 对象，包含以下顶级字段。

### `news` 数组

单个新闻结果的主数组。

| 字段            | 类型      | 描述           |
| ------------- | ------- | ------------ |
| `link`        | string  | 新闻文章的 URL    |
| `title`       | string  | 文章标题         |
| `source`      | string  | 新闻出版商的名称     |
| `source_logo` | string  | 出版商徽标图像的 URL |
| `date`        | string  | 文章的发布日期/时间   |
| `image`       | string  | 文章缩略图的 URL   |
| `global_rank` | integer | 结果在页面上的排名位置  |

### `article_sets` 数组

按主题组织的分组文章集群，每个集群包含一个 `heading` 标签和一个 `items` 文章数组。

<Note>
  article\_sets 不保证在每个响应中都出现。您的实现应该妥善处理其缺失的情况。
</Note>

### 示例响应

```JSON theme={null}
{
  "organic": [],
  "news": [
    {
      "link": "https://www.example-news.com/world/earthquake-latest",
      "title": "Major Earthquake Strikes Pacific Region",
      "source": "Example News",
      "source_logo": "https://www.example-news.com/logo.png",
      "date": "2 hours ago",
      "image": "https://www.example-news.com/images/earthquake.jpg",
      "global_rank": 1
    },
    {
      "link": "https://www.another-outlet.com/earthquake-update",
      "title": "Rescue Operations Underway After Earthquake",
      "source": "Another Outlet",
      "source_logo": "https://www.another-outlet.com/logo.png",
      "date": "3 hours ago",
      "image": "https://www.another-outlet.com/images/rescue.jpg",
      "global_rank": 2
    }
  ],
  "article_sets": [
    {
      "heading": "Latest Updates",
      "items": [
        {
          "link": "https://www.example-news.com/world/earthquake-latest",
          "title": "Major Earthquake Strikes Pacific Region",
          "source": "Example News",
          "date": "2 hours ago"
        }
      ]
    }
  ]
}
```

响应模式：[https://api.brightdata.com/data\_schemas/fast\_serp/google\_search\_news.schema.json](https://api.brightdata.com/data_schemas/fast_serp/google_search_news.schema.json)
