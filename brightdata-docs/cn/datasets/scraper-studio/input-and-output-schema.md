> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 输入与输出架构

> 定义 Bright Data Scraper Studio IDE 采集器的输入字段和结构化输出架构，涵盖 18 种输出字段类型，并支持验证和 PII 标记。

输入与输出架构定义了 Bright Data Scraper Studio IDE 采集器的数据契约：即一次采集运行接受哪些字段，以及采集器返回哪些结构化字段。

* **输入架构**定义一次采集运行接受的字段，例如 `url`、`keyword`、`country`、`date`，或你的交互代码从 `input` 读取的任何自定义字段。
* **输出架构**定义抓取器返回的结构化字段，基于 `collect()` 发出的数据。

这两种架构都在 Bright Data Scraper Studio IDE 中配置。当你点击 **Save to Production** 时，架构更改会应用到生产采集器。

## 什么是输入架构？

输入架构定义了你的抓取器在运行时可以接收的值。

抓取器通常使用 `url` 输入，但输入并不局限于 URL。根据采集器逻辑，输入可以是关键词、位置、日期、ID、国家或任何自定义参数。

你的交互代码通过 `input` 对象读取输入值：

```js theme={null}
navigate(input.url);
wait('.product-title');

const data = parse();
collect(data);
```

对于基于关键词的抓取器：

```js theme={null}
navigate(`https://example.com/search?q=${input.keyword}`);
wait('.search-results');

collect(parse());
```

如果目标 URL 或采集逻辑硬编码在抓取器代码中，抓取器也可以在没有用户提供输入的情况下运行。

## 定义输入参数

要在 Bright Data Scraper Studio IDE 中定义输入架构：

1. 在 **Scraper Studio IDE** 中打开你的采集器。
2. 前往 **Code** 选项卡。
3. 点击 **Add input parameter**。
4. 输入字段名称，例如 `url`、`keyword`、`country` 或 `date`。
5. 添加可选的说明。
6. 选择字段类型。
7. 如果采集器缺少该字段就无法运行，则将其标记为 **Required**。
8. 点击 **Save**。
9. 当采集器就绪后，点击 **Save to Production**。

在采集器已经保存后，点击 IDE 中的 **Edit schema** 即可更新其输入架构。

### 输入参数有哪些设置？

| 设置                    | 说明                                            |
| --------------------- | --------------------------------------------- |
| **Field name**        | 在代码中作为 `input.<field_name>` 使用的键。             |
| **Description**       | 可选说明，用于解释用户应提供什么值。                            |
| **Type**              | 期望的值类型，例如 text/string、boolean、date 或 country。 |
| **Required**          | 如果启用，每个采集输入都必须包含此字段。                          |
| **Predefined values** | 可选的固定选项，在所选类型支持时可用。例如 `country` 类型。           |
| **Case-insensitive**  | 在字段配置支持时，将匹配值视为不区分大小写。                        |

## 采集输入是什么样的？

基于 URL 的采集器可以接受一个或多个 URL：

```json theme={null}
[
  { "url": "https://example.com/product/1" },
  { "url": "https://example.com/product/2" }
]
```

采集器也可以接受多个输入字段：

```json theme={null}
[
  {
    "url": "https://example.com/search",
    "keyword": "standing desk",
    "country": "US"
  },
  {
    "url": "https://example.com/search",
    "keyword": "monitor arm",
    "country": "GB"
  }
]
```

只有标记为 **Required** 的字段才必须为每个输入对象提供。可选字段可以省略。

## 什么是输出架构？

输出架构定义了数据点的结构以及数据的组织方式。

在 Bright Data Scraper Studio IDE 中，输出架构通常由传递给 `collect()` 的对象生成。

```js theme={null}
collect({
  title: $('.product-title').text_sane(),
  price: new Money(+$('.price').text().replace(/\D+/g, ''), 'USD'),
  availability: $('.stock-status').text_sane(),
});
```

这会生成如下输出字段：

```json theme={null}
{
  "title": "ErgoDesk Pro",
  "price": {
    "value": 349.99,
    "currency": "USD"
  },
  "availability": "In stock"
}
```

当抓取器保存时，Scraper Studio 会检测所采集数据的结构，并创建或更新输出架构。

## 更新输出架构

有两种方式更新输出架构：从解析器代码自动更新，或在架构编辑器中手动更新。

### 自动更新架构

1. 在解析器代码中添加或更改字段。
2. 运行预览，确认必填字段按预期返回。
3. 点击 **Save to Production**。
4. 如果 Scraper Studio 检测到架构更改，点击 **Update schema**。
5. 再次点击 **Save to Production**。

### 手动更新架构

1. 点击 IDE 中的 **Edit schema**。
2. 按名称和类型添加或编辑字段。
3. 配置必填标记、默认值、格式化、验证或 PII 设置。
4. 保存架构。
5. 点击 **Save to Production**。

## 什么是输出架构编辑器（Output Schema Editor）？

输出架构编辑器精确定义了你的采集器返回哪些字段，以及每个字段如何验证、格式化和交付。

编辑器有两种视图：

| 视图             | 说明                  |
| -------------- | ------------------- |
| **Table view** | 字段的可视化列表，带有开关和字段配置。 |
| **JSON view**  | 直接对架构对象进行 JSON 编辑。  |

点击某个字段行会打开该字段的配置侧面板。

## 输出架构是如何构建的？

输出架构是一个 JSON 对象，包含顶层的 `type` 和一个 `fields` 对象：

```json theme={null}
{
  "type": "object",
  "fields": {
    "title": {
      "type": "text",
      "active": true
    },
    "price": {
      "type": "price",
      "active": true
    }
  }
}
```

## 输出字段可以有哪些属性？

这些属性适用于用户定义的输出字段。

| 属性                  | 类型      | 说明                                                  |
| ------------------- | ------- | --------------------------------------------------- |
| `type`              | string  | 字段类型，例如 `text`、`number`、`price`、`image` 或 `object`。 |
| `active`            | boolean | 该字段是否包含在输出中。默认值：`true`。                             |
| `required`          | boolean | 如果为 `true`，此字段没有有效值的行会被标记为错误。                       |
| `default_value`     | string  | 当字段无法填充时使用的值。                                       |
| `description`       | string  | 该字段的人类可读说明。                                         |
| `pii`               | boolean | 将该字段标记为包含个人身份信息。                                    |
| `custom_formatting` | object  | 用于高级输出整形的自定义 JavaScript 格式化器。                       |
| `custom_validation` | object  | 定义在每条采集记录上运行的验证规则。                                  |

## 在侧面板中配置字段

侧面板包含针对特定字段的设置。

| 设置                        | 说明                             |
| ------------------------- | ------------------------------ |
| **Field name**            | 在输出 JSON 中使用的键。适用于用户定义的字段。     |
| **Display name**          | 可选的 UI 标签，与输出键分开。              |
| **Data type**             | 字段类型。更改类型会重置特定于类型的设置。          |
| **Active**                | 将该字段包含在输出中或从输出中排除。             |
| **Required**              | 当此字段缺失或无效时，将行标记为错误。            |
| **Default value**         | 当字段无法填充时的回退值。                  |
| **Description**           | 该字段的可选人类可读说明。                  |
| **Contains PII**          | 将该字段标记为包含个人身份信息。               |
| **Format**                | 特定于类型的输出格式化。例如 price/money 类型。 |
| **Download**              | 对于媒体/文件字段，将文件下载到已配置的存储中。       |
| **Array values**          | 定义 `array` 字段的项目类型。            |
| **Subfields**             | 定义 `object` 字段的嵌套字段。           |
| **Normalize**             | 控制空数组的行为。                      |
| **Set as quick filter**   | 将该字段作为数据集查看器中的筛选器公开。           |
| **Quick filter operator** | 定义快速筛选器使用的比较运算符。               |

## 有哪些可用的默认值？

可用的默认值取决于字段类型。

| 选项          | 输出行为          | 适用于              |
| ----------- | ------------- | ---------------- |
| `undefined` | 字段从输出中省略。     | 所有类型             |
| `null`      | 字段返回为 `null`。 | 所有类型             |
| `""`        | 空字符串。         | `text`           |
| `false`     | 布尔值 false。    | `boolean`        |
| `0`         | 数字零。          | `number`、`price` |
| `[]`        | 空数组。          | `array`          |

## 有哪些可用的输出字段类型？

Scraper Studio 支持以下用户定义的输出字段类型。

### `text`

自由格式文本。

```json theme={null}
{
  "type": "text",
  "active": true,
  "required": false,
  "default_value": "null"
}
```

示例值：

```json theme={null}
"Laptop 15-inch Pro"
```

### `number`

整数或小数。数字字符串可以转换为数字。

```json theme={null}
{
  "type": "number",
  "active": true,
  "format": {
    "decimal_places": 2
  },
  "default_value": "zero"
}
```

示例值：

```json theme={null}
11.23
```

### `url`

URL 字符串。仅接受 `http://` 和 `https://` URL。

```json theme={null}
{
  "type": "url",
  "active": true,
  "required": true
}
```

示例值：

```json theme={null}
"https://example.com/product/123"
```

### `price`

以数值和货币代码表示的货币值。

```json theme={null}
{
  "type": "price",
  "active": true,
  "format": {
    "preset": "us_style"
  }
}
```

示例值：

```json theme={null}
{
  "value": 99.99,
  "currency": "USD"
}
```

价格格式预设：

| 预设         | 说明                                              | 示例                                        |
| ---------- | ----------------------------------------------- | ----------------------------------------- |
| `us_style` | 美式格式。                                           | `$1,234.56`                               |
| `locale`   | 区域感知格式。需要区域设置。                                  | `1.234,56 €`                              |
| `number`   | 仅数值。                                            | `1234.56`                                 |
| `raw`      | 原始对象。                                           | `{ "value": 1234.56, "currency": "USD" }` |
| `custom`   | 使用 `{[symbol]}`、`{[value]}`、`{[currency]}` 的模板。 | `USD 1234.56`                             |

### `boolean`

true/false 值。

```json theme={null}
{
  "type": "boolean",
  "active": true,
  "default_value": "false"
}
```

示例值：

```json theme={null}
true
```

### `date`

日期或时间戳值。

```json theme={null}
{
  "type": "date",
  "active": true,
  "format": {
    "preset": "iso"
  }
}
```

日期格式预设：

| 预设          | 说明               | 示例                                  |
| ----------- | ---------------- | ----------------------------------- |
| `iso`       | ISO 8601 字符串。    | `2024-03-15T10:30:00.000Z`          |
| `timestamp` | 以毫秒表示的 Unix 时间戳。 | `1710494400000`                     |
| `locale`    | 区域感知的可读日期。       | `March 15, 2024 at 10:30:00 AM UTC` |

区域格式化可以包括：

* 区域设置，例如 `en-US`、`fr-FR`、`ru-RU`
* 日期样式：`long`、`medium`、`short`
* 时间样式：`long`、`medium`、`short`

### `country`

两个字母的 ISO 3166-1 alpha-2 国家代码。

```json theme={null}
{
  "type": "country",
  "active": true
}
```

示例值：

```json theme={null}
"US"
```

### `phone`

解析为结构化组件的电话号码。

```json theme={null}
{
  "type": "phone",
  "active": true
}
```

示例值：

```json theme={null}
{
  "area_code": 1,
  "number": 5555555555,
  "extension": "1234"
}
```

### `image`

已下载或被引用的图片。

```json theme={null}
{
  "type": "image",
  "active": true,
  "download": true,
  "format": {
    "behavior": "object",
    "content_type": true
  }
}
```

当启用 **Download** 时，文件会存储在已配置的交付目标中。在适用情况下，文件下载与页面加载分开计费。

### `video`、`pdf` 和 `doc`

这些文件类型使用与 `image` 相同的下载和行为设置。

```json theme={null}
{
  "type": "video",
  "active": true,
  "download": true
}
```

支持的文件字段类型：

| 类型      | 说明               |
| ------- | ---------------- |
| `video` | 已下载或被引用的视频文件。    |
| `pdf`   | 已下载或被引用的 PDF 文件。 |
| `doc`   | 已下载或被引用的文档文件。    |

## **文件字段输出选项**

对于已下载的文件字段，例如 `image`、`video`、`pdf` 和 `doc`，输出架构编辑器允许你控制文件元数据的返回方式。

这些设置在字段行为设置为 **Object** 时出现。

### **Behavior**

使用 **Behavior** 选择文件字段的返回方式。

* **Simple** — 仅返回已下载的文件路径或原始远程 URL。
* **Object** — 返回一个包含文件元数据的对象，例如 `file_path`、`remote_url`、`content_type`、`file_size` 和 `response_headers`，具体取决于启用了哪些选项。

当你需要的不仅仅是文件路径时使用 **Object**，例如在验证文件类型、检查文件大小或调试下载头时。

### **Include content type**

启用 **Include content type** 以在输出中包含文件的 MIME 类型。

示例：

```json theme={null}
{
  "content_type": "image/jpeg"
}
```

用它来确认已下载的文件是图片、PDF、视频还是其他媒体类型。

### **Include file size**

启用 **Include file size** 以包含以字节为单位的已下载文件大小。

示例：

```json theme={null}
{
  "file_size": 123456
}
```

用它来验证文件大小、检测空的或意外过大的下载，或排查失败的媒体处理。

### **Include response headers**

启用 **Include response headers** 以包含 Scraper Studio 下载文件时收到的 HTTP 响应头。

示例：

```json theme={null}
{
  "response_headers": {
    "accept-ranges": "bytes",
    "age": "21753",
    "cache-control": "public, max-age=31557600",
    "content-type": "image/jpeg",
    "date": "Sun, 05 Jul 2026 12:43:07 GMT",
    "last-modified": "Sun, 05 Jul 2026 06:40:34 GMT",
    "source-length": "2088714",
    "source-type": "image/jpeg",
    "vary": "Accept"
  }
}
```

响应头可以帮助你调试文件下载、验证内容类型、检查缓存行为，以及排查意外的媒体响应。

### **示例输出**

当 **Behavior** 设置为 **Object** 且所有元数据选项都启用时，输出可能如下所示：

```json theme={null}
{
  "image": {
    "file_path": "image.jpg",
    "remote_url": "https://example.com/image",
    "content_type": "image/jpeg",
    "file_size": 123456,
    "response_headers": {
      "accept-ranges": "bytes",
      "age": "21753",
      "cache-control": "public, max-age=31557600",
      "content-type": "image/jpeg",
      "date": "Sun, 05 Jul 2026 12:43:07 GMT",
      "last-modified": "Sun, 05 Jul 2026 06:40:34 GMT",
      "source-length": "2088714",
      "source-type": "image/jpeg",
      "vary": "Accept"
    }
  }
}
```

### `array`

有序的值列表。元素类型通过 `items` 定义。

```json theme={null}
{
  "type": "array",
  "active": true,
  "normalize": {
    "empty": "keep"
  },
  "default_value": "empty_array",
  "items": {
    "type": "text"
  }
}
```

空数组行为：

| 选项     | 说明             |
| ------ | -------------- |
| `keep` | 将空数组保持为 `[]`。  |
| `drop` | 用已配置的默认值替换空数组。 |

嵌套对象的数组：

```json theme={null}
{
  "type": "array",
  "active": true,
  "items": {
    "type": "object",
    "fields": {
      "name": {
        "type": "text",
        "active": true
      },
      "price": {
        "type": "price",
        "active": true
      }
    }
  }
}
```

### `object`

带有自身子字段的嵌套对象。

```json theme={null}
{
  "type": "object",
  "active": true,
  "fields": {
    "title": {
      "type": "text",
      "active": true
    },
    "price": {
      "type": "price",
      "active": true
    },
    "in_stock": {
      "type": "boolean",
      "active": true
    }
  }
}
```

### 有哪些可用的 HTML 转换字段类型？

| 类型              | 说明                                 | 示例值                                         |
| --------------- | ---------------------------------- | ------------------------------------------- |
| `html2text`     | HTML 转换为可读文本。                      | `Product title\nDescription text`           |
| `html2markdown` | HTML 转换为 Markdown。                 | `## Product title`                          |
| `html2html`     | 原始 HTML 内容。                        | `<div class="product"><h1>Title</h1></div>` |
| `html2ldjson`   | 来自 `application/ld+json` 脚本的结构化数据。 | `{"@type":"Product","name":"Widget"}`       |

示例：

```json theme={null}
{
  "type": "html2markdown",
  "active": true
}
```

## 如何验证字段值？

自定义验证让你定义在字段的每个采集值上运行的 JavaScript 规则。

抛出错误可将该值标记为无效：

```js theme={null}
function validate(v) {
  if (!v)
    throw new Error('Value is required');

  return true;
}
```

当为必需的输出质量配置了验证时，未通过验证的行会被视为错误行。

## 如何格式化字段值？

自定义格式化让你在输出交付之前转换字段值。

```js theme={null}
function process(value) {
  return value;
}
```

当内置格式化选项不符合所需的输出形态时，使用自定义格式化。

## 我应该在什么时候使用 collect() 而不是 set\_lines()？

记录的发出方式会影响输出数据集。

| 函数                | 行为                 | 使用场景           |
| ----------------- | ------------------ | -------------- |
| `collect(data)`   | 向数据集追加一条记录。        | 大多数抓取器。        |
| `set_lines(data)` | 用最新的一组记录替换先前发出的记录。 | 应保留最新快照的渐进式采集。 |

使用 `collect()` 的示例：

```js theme={null}
collect({
  title,
  price,
  availability,
});
```

使用 `set_lines()` 的示例：

```js theme={null}
set_lines(products);
```

## 我可以添加哪些系统字段？

系统字段由 Scraper Studio 生成。它们的名称和类型是固定的。你可以在输出架构配置的 **Additional data** 下打开或关闭它们。

| 字段                    | 类型              | 默认 | 说明                                   |
| --------------------- | --------------- | -- | ------------------------------------ |
| `input`               | string / object | 开  | 触发本次爬取的输入值或对象。                       |
| `prime_input`         | string / object | 关  | 使用发现或分页时的原始根输入。                      |
| `error`               | string          | 开  | 该行采集失败原因的说明。                         |
| `error_code`          | string          | 开  | 结构化错误代码，例如 `validation` 或 `timeout`。 |
| `warning`             | string          | 开  | 该行的系统级警告。                            |
| `warning_code`        | string          | 开  | 结构化警告代码。                             |
| `status_code`         | number          | 关  | 类似 HTTP 的爬取结果代码，例如 `200` 或 `404`。    |
| `timestamp`           | date            | 关  | 页面被采集的日期和时间。                         |
| `requested_timestamp` | date            | 关  | 作业被触发的日期和时间。                         |
| `page_id`             | string          | 关  | 页面爬取的唯一标识符。                          |
| `job_id`              | string          | 关  | 产生该行的作业 ID。                          |
| `collector_id`        | string          | 关  | 采集器的 ID。                             |
| `collector_queue`     | string          | 关  | 作业提交到的队列。                            |
| `crawl_type`          | string          | 关  | 该行使用的爬取或解析器类型。                       |
| `screenshot`          | file            | 关  | 采集时浏览器页面的截图。                         |
| `html`                | file            | 关  | 页面的完整 HTML 快照。                       |
| `warc`                | file            | 关  | 页面的 WARC 存档。                         |

当 `screenshot`、`html` 或 `warc` 处于活动状态时，文件会下载到已配置的存储目标。

## 如何添加截图水印？

当启用 `screenshot` 系统字段时，可以为截图添加水印。每个水印项都有一个标签和一个数据源。

| 数据源         | 说明                                     |
| ----------- | -------------------------------------- |
| Browser URL | 截图时浏览器所在的 URL。                         |
| Timestamp   | 截图捕获的时间戳。                              |
| Input value | 来自采集器输入的值，例如 `url` 或 `config.country`。 |

## 完整的输出架构是什么样的？

```json theme={null}
{
  "type": "object",
  "fields": {
    "url": {
      "type": "url",
      "active": true,
      "required": true
    },
    "title": {
      "type": "text",
      "active": true
    },
    "price": {
      "type": "price",
      "active": true,
      "format": {
        "preset": "us_style"
      },
      "default_value": "zero"
    },
    "rating": {
      "type": "number",
      "active": true,
      "format": {
        "decimal_places": 1
      }
    },
    "in_stock": {
      "type": "boolean",
      "active": true,
      "default_value": "false"
    },
    "listed_date": {
      "type": "date",
      "active": true,
      "format": {
        "preset": "iso"
      }
    },
    "country": {
      "type": "country",
      "active": true
    },
    "images": {
      "type": "array",
      "active": true,
      "normalize": {
        "empty": "keep"
      },
      "default_value": "empty_array",
      "items": {
        "type": "image",
        "download": true
      }
    },
    "seller": {
      "type": "object",
      "active": true,
      "fields": {
        "name": {
          "type": "text",
          "active": true
        },
        "phone": {
          "type": "phone",
          "active": true
        }
      }
    }
  }
}
```

## 相关内容

<CardGroup cols={2}>
  <Card title="开发抓取器" icon="wrench" href="/cn/datasets/scraper-studio/develop-a-scraper">
    在 IDE 中构建抓取器的分步演练
  </Card>

  <Card title="函数参考" icon="code" href="/cn/datasets/scraper-studio/functions">
    带有参数和示例的交互与解析器函数
  </Card>

  <Card title="发起采集与交付" icon="paper-plane" href="/cn/datasets/scraper-studio/initiate-collection-and-delivery-options">
    触发采集并将输出交付到你的目标
  </Card>

  <Card title="触发抓取器（API）" icon="bolt" href="/cn/api-reference/scraper-studio-api/Trigger_a_scraper_for_batch_collection_method">
    通过 API 运行已发布的采集器进行批量采集
  </Card>
</CardGroup>
