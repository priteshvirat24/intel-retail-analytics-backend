> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Dataset API 筛选语法

> Bright Data Dataset API filter 对象参考：运算符、筛选组、最多 3 层嵌套以及 CSV/JSON 文件引用。

`filter` 对象由 Bright Data 市场数据集 API 的 Search 和 Filter 两个端点共享：相同的 schema、相同的运算符、相同的嵌套规则。

<Tip>
  在构建筛选之前，使用[获取数据集元数据](/cn/api-reference/marketplace-dataset-api/get-dataset-metadata)确认字段名称和类型。
</Tip>

## 筛选有哪三种形态？

一个筛选是以下三种形态之一：单字段筛选、组合多个筛选的筛选组，或空值检查。

### 单字段筛选

用一个运算符将一个字段与一个值进行匹配：

```json theme={null}
{ "name": "name", "operator": "=", "value": "John" }
```

### 筛选组

使用 `and` 或 `or` 组合多个筛选。筛选组的最大嵌套深度为 3 层：

```json theme={null}
{
  "operator": "and",
  "filters": [
    { "name": "reviews_count", "operator": ">", "value": 200 },
    { "name": "rating", "operator": ">", "value": 4.5 }
  ]
}
```

### 空值检查

使用 `is_null` 或 `is_not_null` 匹配值是否存在。这些运算符不接受 `value`：

```json theme={null}
{ "name": "reviews_count", "operator": "is_not_null" }
```

## 有哪些可用的运算符？

下列运算符可用于字段筛选。

| 运算符                  | 字段类型        | 作用                                     |
| -------------------- | ----------- | -------------------------------------- |
| `=`                  | Any         | 等于。                                    |
| `!=`                 | Any         | 不等于。                                   |
| `\<`                 | Number、Date | 小于。                                    |
| `\<=`                | Number、Date | 小于或等于。                                 |
| `>`                  | Number、Date | 大于。                                    |
| `>=`                 | Number、Date | 大于或等于。                                 |
| `in`                 | Any         | 字段值等于所提供列表中的任意值。                       |
| `not_in`             | Any         | 字段值不等于列表中的任意值。                         |
| `includes`           | Array、Text  | 字段值包含筛选值。如果筛选值是数组，则匹配字段中包含数组里至少一个值的记录。 |
| `not_includes`       | Array、Text  | 字段值不包含该筛选值。                            |
| `array_includes`     | Array       | 数组中存在完全匹配项。                            |
| `not_array_includes` | Array       | 数组中不存在完全匹配项。                           |
| `is_null`            | Any         | 字段值为 null。无需提供值。                       |
| `is_not_null`        | Any         | 字段值不为 null。无需提供值。                      |

## 哪些运算符可读取 CSV 或 JSON 文件？

这些文件引用运算符仅在 [Filter 端点](/cn/api-reference/marketplace-dataset-api/filter-dataset)的 multipart 模式下有效。将文件名作为 value 传入，即可按存储在 CSV 或 JSON 文件中的成千上万个值进行筛选。

| 运算符                  | 字段类型       | 说明              |
| -------------------- | ---------- | --------------- |
| `in`                 | Any        | 字段值等于文件中的任意值。   |
| `not_in`             | Any        | 字段值不等于文件中的任意值。  |
| `includes`           | Array、Text | 字段值包含文件中的任意值。   |
| `not_includes`       | Array、Text | 字段值不包含文件中的任意值。  |
| `array_includes`     | Array      | 文件中的任意值存在于字段值中。 |
| `not_array_includes` | Array      | 文件中的值都不存在于字段值中。 |

Search 端点不支持文件引用。Elasticsearch 无法在查询时读取外部文件。

## 如何在单个嵌套对象内进行匹配？

对于字段是对象数组的数据集，在筛选组上设置 `combine_nested_fields: true`，使该组内的所有筛选必须在同一个对象内匹配，而不是跨数组中的不同对象：

```json theme={null}
{
  "operator": "and",
  "combine_nested_fields": true,
  "filters": [
    { "name": "experience.title", "operator": "includes", "value": "engineer" },
    { "name": "experience.company", "operator": "=", "value": "Bright Data" }
  ]
}
```

如果不设置 `combine_nested_fields`，这两个条件可能在 `experience` 数组中的不同对象上分别匹配。

## 提示

* 在构建筛选之前，使用[获取数据集元数据](/cn/api-reference/marketplace-dataset-api/get-dataset-metadata)确认字段名称和类型。
* 尽量保持嵌套层级浅。最大深度为 3 层。
* 在 Search 端点上，对自由文本字段优先使用 `includes` 而非 `=`，因为 Elasticsearch 会对其分词。
* 在 Filter 端点上，文件引用仅可与上述列出的运算符配合使用。

## 相关文档

* [Dataset API 概述](/cn/api-reference/marketplace-dataset-api/overview)
* [Search 数据集（同步）](/cn/api-reference/marketplace-dataset-api/search-dataset)
* [Filter 数据集（异步，文件上传）](/cn/api-reference/marketplace-dataset-api/filter-dataset)
* [获取数据集元数据](/cn/api-reference/marketplace-dataset-api/get-dataset-metadata)
