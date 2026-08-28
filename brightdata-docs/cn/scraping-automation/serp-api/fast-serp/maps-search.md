> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 快速地图搜索

Bright Data 为谷歌地图提供快速 SERP 服务，仅向特定企业客户提供。该服务以紧凑的 JSON 响应，为需要本地商业列表和地点数据的实时应用提供支持。如需获取访问权限，请联系您的 Bright Data 账户经理。

## Google Maps 端点

Google Maps Fast SERP 根据您访问的 URL 支持两种响应类型：

* **地图搜索结果** — 与搜索查询匹配的地点列表，返回 `organic` 数组
* **地点详情页面** — 单个地点记录，返回 `place` 对象

两个端点都需要 `x-unblock-data-format: parsed_light` 请求头和 `brd_json=1` URL 参数。省略任何一个都会导致意外的响应格式。

## Fast Maps 搜索请求

Google Maps Fast SERP 最适合使用原生代理接口。如果您的架构需要 REST API 接口，我们可以提供一个。

### 地图搜索结果

```text theme={null}
curl -v --proxy fserp.brd.superproxy.io:44445 \
  --proxy-user username:password \
  -k \
  -H 'x-unblock-data-format: parsed_light' \
  "https://www.google.com/maps/search/coffee+shops+new+york/?hl=en&gl=us&brd_json=1"
```

### 地点详情页面

```text theme={null}
curl -v --proxy fserp.brd.superproxy.io:44445 \
  --proxy-user username:password \
  -k \
  -H 'x-unblock-data-format: parsed_light' \
  "https://www.google.com/maps/place/?q=place_id:ChIJN1t_tDeuEmsRUsoyG83frY4&hl=en&gl=us&brd_json=1"
```

## 响应格式

响应是两种形状之一，取决于目标 URL：搜索结果页面返回 `organic` 数组；地点详情页面返回 `place` 对象。两者都使用相同的 `OrganicMapsItem` 结构。

### `organic` 数组 / `place` 对象

`organic` 中的项目和 `place` 对象都共享以下字段：

| 字段               | 类型  | 必需 | 描述                                  |
| ---------------- | --- | -- | ----------------------------------- |
| `global_rank`    | 整数  | 是  | 结果在页面上的排名位置                         |
| `title`          | 字符串 | 否  | 地点名称                                |
| `address`        | 字符串 | 否  | 地点的完整地址                             |
| `phone`          | 字符串 | 否  | 地点的电话号码                             |
| `link`           | 字符串 | 否  | 地点网站的 URL                           |
| `map_link`       | 字符串 | 否  | 地点在 Google Maps 上的 URL              |
| `map_id`         | 字符串 | 否  | Google Maps 地点标识符                   |
| `map_id_encoded` | 字符串 | 否  | Google Maps 地点标识符的编码版本              |
| `description`    | 字符串 | 否  | 地点的简短描述                             |
| `price`          | 字符串 | 否  | 价格范围指标，例如 `"$$"`                    |
| `rating`         | 数字  | 否  | 平均客户评分                              |
| `reviews_cnt`    | 数字  | 否  | 客户评论总数                              |
| `latitude`       | 数字  | 否  | 地点的纬度坐标                             |
| `longitude`      | 数字  | 否  | 地点的经度坐标                             |
| `image`          | 字符串 | 否  | 主要图像 URL                            |
| `original_image` | 字符串 | 否  | 原始全分辨率图像 URL                        |
| `thumbnail`      | 字符串 | 否  | 缩略图 URL                             |
| `open_hours`     | 对象  | 否  | 按日期划分的营业时间，例如 `"Monday": "9am–5pm"` |
| `category`       | 数组  | 否  | 地点类别列表（见下文）                         |
| `images`         | 数组  | 否  | 地点图像列表（见下文）                         |
| `menu_images`    | 数组  | 否  | 菜单图像列表（见下文）                         |
| `tags`           | 数组  | 否  | 地点属性标签列表（见下文）                       |
| `reviews`        | 数组  | 否  | 客户评论列表（见下文）                         |

### `category` 项目

| 字段            | 类型  | 必需 | 描述      |
| ------------- | --- | -- | ------- |
| `id`          | 字符串 | 是  | 类别标识符   |
| `title`       | 字符串 | 是  | 完整类别名称  |
| `title_short` | 字符串 | 否  | 缩短的类别名称 |

### `images` 和 `menu_images` 项目

| 字段                | 类型  | 必需 | 描述          |
| ----------------- | --- | -- | ----------- |
| `image`           | 字符串 | 是  | 图像 URL      |
| `image_width`     | 整数  | 否  | 显示的图像宽度（像素） |
| `image_height`    | 整数  | 否  | 显示的图像高度（像素） |
| `original_width`  | 整数  | 否  | 原始图像宽度（像素）  |
| `original_height` | 整数  | 否  | 原始图像高度（像素）  |

### `tags` 项目

| 字段                  | 类型  | 必需 | 描述         |
| ------------------- | --- | -- | ---------- |
| `group_id`          | 字符串 | 是  | 标签组的标识符    |
| `group_title`       | 字符串 | 是  | 标签组的显示名称   |
| `key_id`            | 字符串 | 是  | 标签键的标识符    |
| `key_title`         | 字符串 | 是  | 标签键的显示名称   |
| `value`             | 数字  | 否  | 与标签关联的数值   |
| `value_title`       | 字符串 | 否  | 标签值的显示标签   |
| `value_title_short` | 字符串 | 否  | 标签值的缩短显示标签 |

### `reviews` 项目

| 字段                          | 类型    | 描述              |
| --------------------------- | ----- | --------------- |
| `author`                    | 字符串   | 评论者的名称          |
| `avatar`                    | 字符串   | 评论者的个人资料图像 URL  |
| `author_reviews_cnt`        | 数字    | 此作者撰写的评论总数      |
| `author_photos_cnt`         | 数字    | 此作者上传的照片总数      |
| `rating`                    | 数字    | 此评论中给出的评分       |
| `text`                      | 字符串   | 评论文本内容          |
| `timestamp_added`           | 字符串   | 评论发布的日期/时间      |
| `timestamp_edited`          | 字符串   | 评论最后编辑的日期/时间    |
| `link`                      | 字符串   | 评论的 URL         |
| `source`                    | 字符串   | 评论的平台来源         |
| `source_logo`               | 字符串   | 来源平台的徽标 URL     |
| `images`                    | 字符串数组 | 附加到评论的图像 URL 列表 |
| `response_text`             | 字符串   | 所有者对评论的回复       |
| `response_timestamp_added`  | 字符串   | 所有者回复发布的日期/时间   |
| `response_timestamp_edited` | 字符串   | 所有者回复最后编辑的日期/时间 |

## 示例响应

### 地图搜索结果

```text theme={null}
{
  "organic": [
    {
      "global_rank": 1,
      "title": "Example Coffee Co.",
      "address": "123 Main St, New York, NY 10001",
      "phone": "+1 212-555-0100",
      "link": "https://www.example-coffee.com",
      "map_link": "https://www.google.com/maps/place/example-coffee",
      "map_id": "0x6b12ae37b47f5b37:0x8eaddfcd1b32ca52",
      "map_id_encoded": "ChIJN1t_tDeuEmsRUsoyG83frY4",
      "description": "Specialty coffee shop serving single-origin espresso and pour-overs.",
      "price": "$$",
      "rating": 4.7,
      "reviews_cnt": 1280,
      "latitude": 40.7128,
      "longitude": -74.0060,
      "thumbnail": "https://www.example-coffee.com/images/thumb.jpg",
      "open_hours": {
        "Monday": "7am–7pm",
        "Tuesday": "7am–7pm",
        "Wednesday": "7am–7pm",
        "Thursday": "7am–7pm",
        "Friday": "7am–8pm",
        "Saturday": "8am–8pm",
        "Sunday": "9am–6pm"
      },
      "category": [
        { "id": "coffee_shop", "title": "Coffee Shop", "title_short": "Coffee" }
      ],
      "tags": [
        {
          "group_id": "service_options",
          "group_title": "Service options",
          "key_id": "dine_in",
          "key_title": "Dine-in",
          "value": 1,
          "value_title": "Available",
          "value_title_short": "Yes"
        }
      ],
      "reviews": [
        {
          "author": "Jane D.",
          "avatar": "https://example.com/avatars/jane.jpg",
          "author_reviews_cnt": 42,
          "author_photos_cnt": 15,
          "rating": 5,
          "text": "Best espresso in the city, hands down.",
          "timestamp_added": "2025-03-10T09:00:00Z",
          "source": "Google",
          "source_logo": "https://www.google.com/images/google-logo.png",
          "response_text": "Thank you so much, Jane! See you soon.",
          "response_timestamp_added": "2025-03-11T10:00:00Z"
        }
      ]
    }
  ]
}
```

### 地点详情页面

```text theme={null}
{
  "place": {
    "global_rank": 1,
    "title": "Example Coffee Co.",
    "address": "123 Main St, New York, NY 10001",
    "phone": "+1 212-555-0100",
    "link": "https://www.example-coffee.com",
    "map_link": "https://www.google.com/maps/place/example-coffee",
    "map_id": "0x6b12ae37b47f5b37:0x8eaddfcd1b32ca52",
    "map_id_encoded": "ChIJN1t_tDeuEmsRUsoyG83frY4",
    "description": "Specialty coffee shop serving single-origin espresso and pour-overs.",
    "price": "$$",
    "rating": 4.7,
    "reviews_cnt": 1280,
    "latitude": 40.7128,
    "longitude": -74.0060,
    "thumbnail": "https://www.example-coffee.com/images/thumb.jpg",
    "images": [
      {
        "image": "https://www.example-coffee.com/images/interior.jpg",
        "image_width": 800,
        "image_height": 600,
        "original_width": 1600,
        "original_height": 1200
      }
    ],
    "open_hours": {
      "Monday": "7am–7pm",
      "Friday": "7am–8pm",
      "Saturday": "8am–8pm",
      "Sunday": "9am–6pm"
    },
    "category": [
      { "id": "coffee_shop", "title": "Coffee Shop", "title_short": "Coffee" }
    ]
  }
}
```

响应模式（地图搜索结果）：[https://api.brightdata.com/data\_schemas/fast\_serp/google\_maps\_search.schema.json](https://api.brightdata.com/data_schemas/fast_serp/google_maps_search.schema.json)

响应模式（地点详情页）：[https://api.brightdata.com/data\_schemas/fast\_serp/google\_maps\_place.schema.json](https://api.brightdata.com/data_schemas/fast_serp/google_maps_place.schema.json)

## 支持的参数

### `gl`

两字母国家代码，用于定义搜索的国家

### `hl`

两字母语言代码，用于定义页面语言
