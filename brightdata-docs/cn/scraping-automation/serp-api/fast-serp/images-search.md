> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 快速图片搜索

Bright Data 提供快速的 Google 图片 SERP 服务。此服务使用紧凑的 JSON 响应，为需要图片搜索结果的实时应用程序提供支持。如需获取访问权限，请联系您的 Bright Data 账户经理。

## 快速图片搜索请求

Google 图片快速 SERP 最适合与原生代理接口配合使用。如果您的架构需要 REST API 接口，我们可以提供。

`x-unblock-data-format: parsed_light` 请求头和 `brd_json=1` URL 参数都是必需的。省略其中任何一个都会导致意外的响应格式。

### 原生代理请求

```text theme={null}
curl -i --proxy fserp.brd.superproxy.io:44445 \
  --proxy-user brd-customer-<CUSTOMER>-zone-<ZONE>:<PASSWORD> \
  -k \
  -H 'x-unblock-data-format: parsed_light' \
  "https://www.google.com/search?q=pizza&tbm=isch&brd_json=1"
```

## 响应格式

成功的响应包含一个必需的 `images` 数组。

### `images` 数组

| 字段                | 类型      | 必需 | 描述             |
| ----------------- | ------- | -- | -------------- |
| `global_rank`     | integer | 是  | 结果在页面上的排名位置    |
| `title`           | string  | 否  | 图片的标题或替代文本     |
| `link`            | string  | 否  | 找到图片的来源页面的 URL |
| `image`           | string  | 否  | 缩略图图片 URL      |
| `original_image`  | string  | 否  | 完整分辨率图片 URL    |
| `image_width`     | integer | 否  | 显示的图片宽度（像素）    |
| `image_height`    | integer | 否  | 显示的图片高度（像素）    |
| `original_width`  | integer | 否  | 原始图片宽度（像素）     |
| `original_height` | integer | 否  | 原始图片高度（像素）     |
| `blurred`         | boolean | 否  | 图片是否模糊         |

## 示例响应

```text theme={null}
{
  "images": [
    {
      "global_rank": 1,
      "title": "Classic Margherita Pizza",
      "link": "https://www.example-recipe.com/margherita",
      "image": "https://www.example-recipe.com/images/margherita-thumb.jpg",
      "original_image": "https://www.example-recipe.com/images/margherita-full.jpg",
      "image_width": 400,
      "image_height": 300,
      "original_width": 1200,
      "original_height": 900,
      "blurred": false
    },
    {
      "global_rank": 2,
      "title": "Neapolitan Pizza with Fresh Basil",
      "link": "https://www.example-food.com/neapolitan",
      "image": "https://www.example-food.com/images/neapolitan-thumb.jpg",
      "original_image": "https://www.example-food.com/images/neapolitan-full.jpg",
      "image_width": 400,
      "image_height": 300,
      "original_width": 1600,
      "original_height": 1200,
      "blurred": false
    },
    {
      "global_rank": 3,
      "title": "New York Style Pizza Slice",
      "link": "https://www.example-pizza.com/ny-style",
      "image": "https://www.example-pizza.com/images/ny-slice-thumb.jpg",
      "original_image": "https://www.example-pizza.com/images/ny-slice-full.jpg",
      "image_width": 400,
      "image_height": 267,
      "original_width": 2000,
      "original_height": 1333,
      "blurred": false
    },
    {
      "global_rank": 4,
      "title": "Homemade Deep Dish Chicago Pizza",
      "link": "https://www.example-recipe.com/deep-dish",
      "image": "https://www.example-recipe.com/images/deep-dish-thumb.jpg",
      "original_image": "https://www.example-recipe.com/images/deep-dish-full.jpg",
      "image_width": 400,
      "image_height": 400,
      "original_width": 1500,
      "original_height": 1500,
      "blurred": false
    },
    {
      "global_rank": 5,
      "title": "Wood-Fired Pizza from Naples",
      "link": "https://www.example-travel.com/naples-pizza",
      "image": "https://www.example-travel.com/images/naples-pizza-thumb.jpg",
      "original_image": "https://www.example-travel.com/images/naples-pizza-full.jpg",
      "image_width": 400,
      "image_height": 267,
      "original_width": 3000,
      "original_height": 2000,
      "blurred": false
    }
  ]
}
```

响应架构：[https://api.brightdata.com/data\_schemas/fast\_serp/google\_search\_images.schema.json](https://api.brightdata.com/data_schemas/fast_serp/google_search_images.schema.json)

## 支持的参数

| 参数         | 描述                        | 示例           |
| ---------- | ------------------------- | ------------ |
| `q`        | 搜索查询（**必须位于 URL 的第一个参数**） | `q=pizza`    |
| `gl`       | 用于定义搜索国家/地区的两字母国家代码       | `gl=us`      |
| `hl`       | 用于定义页面语言的两字母语言代码          | `hl=en`      |
| `brd_json` | **必填。** `1` = 解析后的 JSON   | `brd_json=1` |
