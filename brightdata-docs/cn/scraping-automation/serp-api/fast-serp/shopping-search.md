> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 快速购物搜索

> 使用 Bright Data 快速 SERP 服务通过本机代理接口实时获取 Google 购物搜索结果和商品详情页数据，返回紧凑的 JSON 格式。

## 快速 SERP：Google 购物端点

Google 购物提供两类页面，快速 SERP 均支持：

* **购物搜索结果**：给定搜索词的商品列表，通过 `https://www.google.com/search?q=[searchTerm]&udm=28` 获取
* **商品详情页（PDP）**：包含报价、规格和评论的完整商品页面，通过 Google 购物商品 URL 获取

两个端点都需要 `x-unblock-data-format: parsed_light` 请求头和 `brd_json=1` URL 参数。省略其中任何一个都会导致意外的响应格式。

## 快速购物搜索请求

快速 SERP for Google 购物最适合使用本机代理接口。如果您的架构需要 REST API 接口，我们可以提供。

### 购物搜索结果

使用 `udm=28` 参数获取 Google 购物搜索结果列表页。

```bash theme={null}
curl -v --proxy fserp.brd.superproxy.io:44445 \
  --proxy-user username:password \
  -k \
  -H 'x-unblock-data-format: parsed_light' \
  "https://www.google.com/search?q=iphone&udm=28&brd_json=1"
```

### 响应格式

成功的购物搜索响应包含一个 `shopping` 数组。

#### `shopping` 数组

| 字段              | 类型               | 必需 | 说明                                     |
| --------------- | ---------------- | -- | -------------------------------------- |
| `price`         | string           | 是  | 商品的显示价格                                |
| `link`          | string           | 是  | 指向商品列表页或商家页面的 URL                      |
| `global_rank`   | integer          | 是  | 该结果在页面上的排名位置                           |
| `title`         | string           | 否  | 商品名称                                   |
| `shop`          | string           | 否  | 商家或卖家名称                                |
| `image`         | string           | 否  | 商品缩略图 URL                              |
| `rating`        | number           | 否  | 平均客户评分                                 |
| `reviews_cnt`   | integer          | 否  | 客户评论数量                                 |
| `old_price`     | string           | 否  | 折扣前的原价（如适用）                            |
| `foreign_price` | string           | 否  | 当商家自有币种与搜索币种不同时，以商家币种显示的价格             |
| `price_details` | array of objects | 否  | 价格的分项明细。每个对象包含 `type` 和 `price`，两者始终存在 |
| `tag`           | string           | 否  | Google 为该列表附加的促销标签，例如 `"Sale"`         |

#### 示例响应：购物搜索结果

```json theme={null}
{
  "shopping": [
    {
      "title": "Apple iPhone 16 128GB Black",
      "link": "https://www.example-store.com/iphone-16-black",
      "price": "$799.00",
      "old_price": "$899.00",
      "foreign_price": "€739.00",
      "price_details": [
        { "type": "item", "price": "$799.00" },
        { "type": "shipping", "price": "$0.00" },
        { "type": "tax", "price": "$65.92" }
      ],
      "tag": "Sale",
      "shop": "Example Store",
      "rating": 4.8,
      "reviews_cnt": 3240,
      "image": "https://www.example-store.com/images/iphone-16.jpg",
      "global_rank": 1
    },
    {
      "title": "Apple iPhone 16 256GB White",
      "link": "https://www.another-store.com/iphone-16-white",
      "price": "$899.00",
      "shop": "Another Store",
      "rating": 4.7,
      "reviews_cnt": 1850,
      "image": "https://www.another-store.com/images/iphone-16-white.jpg",
      "global_rank": 2
    }
  ]
}
```

响应 schema：[https://api.brightdata.com/data\_schemas/fast\_serp/google\_shopping.schema.json](https://api.brightdata.com/data_schemas/fast_serp/google_shopping.schema.json)

## 快速购物商品请求

快速 SERP for Google 购物商品页最适合使用本机代理接口。如果您的架构需要 REST API 接口，我们可以提供。

对于快速 SERP，`x-unblock-data-format: parsed_light` 请求头和 `brd_json=1` URL 参数两者都是必需的。省略其中任何一个都会导致意外的响应格式。

<Note>
  Google 购物商品（PDP）URL 存活时间很短。它们带有经过编码的 `prds=` 参数，Google 会频繁轮换该参数，因此复制的 URL 在短时间后就会失效。请勿硬编码商品 URL。正确做法是：从购物搜索结果卡片打开商品，使用 Google 跳转到的那个 URL，然后附加 `&brd_json=1`。
</Note>

### 本机代理请求

```shell theme={null}
curl -v --proxy fserp.brd.superproxy.io:44445 \
  --proxy-user username:password \
  -k \
  "<GOOGLE_SHOPPING_PRODUCT_URL>&brd_json=1" \
  -H 'x-unblock-data-format: parsed_light'
```

## 响应格式

成功的响应由三个顶层字段构成：`product`、`product_offers` 和 `product_spec`。

### `product` 对象

顶层商品信息。

| 字段            | 类型               | 说明          |
| :------------ | :--------------- | :---------- |
| `title`       | string           | 商品名称        |
| `description` | string           | 完整商品描述      |
| `images`      | array of strings | 商品图片 URL 列表 |
| `rating`      | number \| null   | 平均客户评分      |
| `reviews_cnt` | integer          | 客户评论总数      |
| `ai_images`   | array of strings | AI 板块中的图片链接 |

### `product_offers` 数组

该商品各个卖家报价的列表。

| 字段                   | 类型               | 说明             |
| :------------------- | :--------------- | :------------- |
| `seller`             | string           | 卖家或商家名称        |
| `link`               | string           | 指向卖家商品页的 URL   |
| `logo`               | string           | 卖家 logo 图片 URL |
| `item_price`         | array of strings | 该报价显示的当前价格     |
| `item_old_price`     | array of strings | 之前的划线价格（如适用）   |
| `total_price`        | array of strings | 卖家显示的含运费和税费的总价 |
| `shipping`           | string           | 运费或配送信息        |
| `rating`             | number           | 卖家或报价评分        |
| `reviews_cnt`        | integer          | 该报价的评论数量       |
| `details`            | array of strings | 报价要点列表         |
| `details_and_offers` | string           | 详情与促销信息的合并文本   |
| `payment_methods`    | string           | 接受的支付方式        |

### `product_spec` 对象

按板块分组的技术规格。

| 字段                     | 类型     | 说明                       |
| :--------------------- | :----- | :----------------------- |
| `specs`                | array  | 规格板块列表                   |
| `specs[].data`         | array  | 板块内的规格条目列表               |
| `specs[].data[].name`  | string | 规格名称，例如 `"Display size"` |
| `specs[].data[].value` | string | 规格值，例如 `"6.1 inches"`    |

## 示例响应

```json theme={null}
{
  "product": {
    "title": "Apple iPhone 17 Pro Max",
    "description": "The Apple iPhone 17 Pro Max features the latest A-series chip, a pro camera system, and all-day battery life in a titanium design.",
    "images": [
      "https://www.example-store.com/images/iphone-17-pro-max-front.jpg",
      "https://www.example-store.com/images/iphone-17-pro-max-back.jpg"
    ],
    "ai_images": [
      "https://www.example-store.com/images/iphone-17-pro-max-ai-1.jpg",
      "https://www.example-store.com/images/iphone-17-pro-max-ai-2.jpg"
    ],
    "rating": 4.9,
    "reviews_cnt": 5120
  },
  "product_offers": [
    {
      "seller": "Example Store",
      "link": "https://www.example-store.com/iphone-17-pro-max",
      "logo": "https://www.example-store.com/logo.png",
      "item_price": ["$1,199.00"],
      "item_old_price": ["$1,299.00"],
      "total_price": ["$1,298.92"],
      "shipping": "Free shipping",
      "rating": 4.9,
      "reviews_cnt": 2100,
      "details": ["In stock", "Ships within 24 hours"],
      "details_and_offers": "In stock. Ships within 24 hours. 10% off with code SAVE10.",
      "payment_methods": "Visa, Mastercard, PayPal"
    },
    {
      "seller": "Another Store",
      "link": "https://www.another-store.com/iphone-17-pro-max",
      "logo": "https://www.another-store.com/logo.png",
      "item_price": ["$1,209.00"],
      "item_old_price": [],
      "total_price": ["$1,314.75"],
      "shipping": "$5.99 shipping",
      "rating": 4.7,
      "reviews_cnt": 980,
      "details": ["In stock"],
      "details_and_offers": "In stock. Standard delivery 3-5 days.",
      "payment_methods": "Visa, Mastercard"
    }
  ],
  "product_spec": {
    "specs": [
      {
        "data": [
          { "name": "Display size", "value": "6.9 inches" },
          { "name": "Display type", "value": "Super Retina XDR OLED" }
        ]
      },
      {
        "data": [
          { "name": "Storage", "value": "256GB" },
          { "name": "RAM", "value": "12GB" },
          { "name": "Processor", "value": "Apple A19 Pro" }
        ]
      },
      {
        "data": [
          { "name": "Main camera", "value": "48MP" },
          { "name": "Battery capacity", "value": "4685 mAh" }
        ]
      }
    ]
  }
}
```

响应 schema：[https://api.brightdata.com/data\_schemas/fast\_serp/google\_shopping\_product.schema.json](https://api.brightdata.com/data_schemas/fast_serp/google_shopping_product.schema.json)

## 支持的参数

| 参数         | 说明                     | 示例           | 备注                                   |
| ---------- | ---------------------- | ------------ | ------------------------------------ |
| `q`        | 搜索查询（**必须位于 URL 首位**）  | `q=iphone`   | 查询长度必须少于 8,000 个字符。<br />更长的查询会返回错误。 |
| `gl`       | 搜索国家/地区的两字母代码          | `gl=us`      |                                      |
| `hl`       | 页面语言的两字母代码             | `hl=en`      |                                      |
| `brd_json` | **必需。**`1` = 解析后的 JSON | `brd_json=1` |                                      |
