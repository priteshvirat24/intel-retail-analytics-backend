> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Search 数据集（同步，Elasticsearch）

> 对 Bright Data 市场数据集运行实时、基于 Elasticsearch 的查询。亚秒级响应，每次调用最多 1,000 条记录。

Bright Data 市场数据集 API 的 Search 端点对市场数据集运行实时、基于 Elasticsearch 的查询：发送一个 filter，即可在响应中以亚秒级延迟取回记录。

<Tip>
  将您的 API Key 粘贴到授权字段。要获取 API Key，请[创建账户](https://www.bright.cn/?hs_signup=1\&utm_source=docs\&utm_campaign=playground)并了解[如何生成 API Key](/cn/api-reference/authentication#如何生成新的-api-key？)。
</Tip>

## 何时使用 Search？

当您需要在单次低延迟调用中取回少量记录时，使用 Search：

* 实时查询，例如线索一进入 CRM 就立即增强。
* 将实时记录输入 AI agent 或 LLM 应用。
* 按姓名、职位、公司或地区进行销售勘探。
* 购买前抽样数据集，搭配 `"sort": "random"`。
* 任何需要在一次调用中取回最多 1,000 条记录的工作负载。

如果您需要文件上传、批量导出，或某个不在支持列表中的数据集，请改用 [Filter](/cn/api-reference/marketplace-dataset-api/filter-dataset)。

## 运行您的第一个 Search 查询

向 `/datasets/search/:dataset_id` 发送 `POST` 请求，并带上一个 `filter` 对象。下面的示例在 LinkedIn 人物档案数据集中查询 `name` 包含 `Egor` 的记录：

```bash theme={null}
curl -X POST "https://api.brightdata.com/datasets/search/gd_l1viktl72bvl7bjuj0" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "size": 10,
    "filter": {
      "name": "name",
      "operator": "includes",
      "value": "Egor"
    }
  }'
```

Search 内联返回记录。无需轮询，也没有快照 ID：

```json theme={null}
{
  "hits": [ /* records */ ],
  "total_hits": 579859,
  "took": 142
}
```

## Search 支持哪些数据集？

Search 处于 alpha 阶段，目前支持三个 LinkedIn 数据集。其他任何数据集请使用 [Filter](/cn/api-reference/marketplace-dataset-api/filter-dataset)。

| 数据集                    | `dataset_id`            |
| ---------------------- | ----------------------- |
| LinkedIn 人物档案          | `gd_l1viktl72bvl7bjuj0` |
| LinkedIn 人物档案（含联系方式增强） | `gd_me5ppxjr2ge6icjuh0` |
| LinkedIn 公司信息          | `gd_l1vikfnt1wgvvqz95w` |

<Note>
  Amazon 数据集即将推出。更多数据集将在 2026 年第三季度逐步走向正式发布（GA）。向 Search 传入不受支持的 `dataset_id` 会返回 `404`。
</Note>

## 如何进行身份验证？

Search 使用 Bearer token 身份验证。在 `Authorization` 请求头中传入您的 API Key：

```bash theme={null}
Authorization: Bearer YOUR_API_KEY
```

从[账户设置](/cn/api-reference/authentication#如何生成新的-api-key？)获取您的 Key。

## Search 接受哪些参数？

| 名称             | 类型             | 默认值 | 必填 | 说明                                                                              |
| -------------- | -------------- | --- | -- | ------------------------------------------------------------------------------- |
| `filter`       | object         | -   | 是  | 筛选表达式。不能为空。参见[筛选语法参考](/cn/api-reference/marketplace-dataset-api/filter-syntax)。 |
| `size`         | number         | 100 | 否  | 返回的记录数量。Search 最适合每次调用最多 1,000 条记录。                                             |
| `sort`         | string 或 array | -   | 否  | `default`、`random`，或自定义排序，如 `[{"timestamp":"asc"}]`。                            |
| `search_after` | array          | -   | 否  | 分页游标。传入上一次响应中的 `search_after` 值。                                                |

## Search 返回什么？

| 名称             | 类型     | 说明                       |
| -------------- | ------ | ------------------------ |
| `hits`         | array  | 匹配的记录。                   |
| `total_hits`   | number | 与筛选匹配的记录总数。              |
| `took`         | number | 服务器耗时（毫秒）。               |
| `search_after` | array  | 下一页的游标。仅在设置了 `sort` 时返回。 |

## 如何排序和分页？

设置 `sort` 控制排序，并使用返回的 `search_after` 游标翻页。

### 使用随机排序抽样数据集

使用 `"sort": "random"` 提取有代表性的样本，例如在购买数据集之前：

```bash theme={null}
curl -X POST "https://api.brightdata.com/datasets/search/gd_l1viktl72bvl7bjuj0" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "size": 10,
    "sort": "random",
    "filter": { "name": "name", "operator": "includes", "value": "Egor" }
  }'
```

### 使用 search\_after 翻页

设置 `"sort": "default"` 以在响应中获得 `search_after` 游标。请求第一页：

```json theme={null}
{
  "size": 10,
  "sort": "default",
  "filter": { "name": "name", "operator": "includes", "value": "Egor" }
}
```

将返回的 `search_after` 数组传回以获取下一页：

```json theme={null}
{
  "size": 10,
  "sort": "default",
  "search_after": [ /* value from previous response */ ],
  "filter": { "name": "name", "operator": "includes", "value": "Egor" }
}
```

### 按自定义字段排序

传入由"字段到方向"对象组成的数组，按指定字段排序：

```json theme={null}
{ "sort": [{ "timestamp": "asc" }] }
```

## Search 的费用是多少？

Search 的费用为 \$2.5 CPM（每返回 1,000 条记录），与市场价格相同。筛选返回 0 条记录时不收费。

## Search 可能返回哪些错误？

| 状态码   | 含义               | 处理方式                                                                               |
| ----- | ---------------- | ---------------------------------------------------------------------------------- |
| `400` | 筛选或参数有误          | 使用[获取数据集元数据](/cn/api-reference/marketplace-dataset-api/get-dataset-metadata)核对字段名。 |
| `401` | API Key 错误或缺失    | 检查您的 Bearer token。                                                                 |
| `402` | 余额不足             | 充值或减小 `size`。                                                                      |
| `404` | 未知的 `dataset_id` | 确认数据集在上方的支持列表中。                                                                    |
| `422` | 筛选未匹配任何记录        | 放宽筛选条件或检查字段值。                                                                      |
| `429` | 触发速率限制           | 退避后重试。                                                                             |

## 常见问题

### Search 支持 CSV 或 JSON 文件上传吗？

不支持。Elasticsearch 无法在查询时读取外部文件。要按 CSV 或 JSON 文件中的成千上万个值进行筛选，请使用 [Filter 端点](/cn/api-reference/marketplace-dataset-api/filter-dataset)。

### Search 一次调用能返回多少条记录？

Search 最适合每次调用最多 1,000 条记录。如需更大规模的提取，请使用 [Filter](/cn/api-reference/marketplace-dataset-api/filter-dataset)，它基于快照并支持批量导出。

### 为什么 Search 和 Filter 返回的结果略有不同？

两个端点使用不同的引擎。Elasticsearch 对文本的分词方式与快照引擎不同，因此自由文本匹配可能存在差异。在自由文本字段上，建议优先使用 `includes` 运算符而非 `=`。

## 相关文档

* [Dataset API 概述](/cn/api-reference/marketplace-dataset-api/overview)
* [筛选语法参考](/cn/api-reference/marketplace-dataset-api/filter-syntax)
* [Filter 数据集（异步，文件上传）](/cn/api-reference/marketplace-dataset-api/filter-dataset)
* [获取数据集元数据](/cn/api-reference/marketplace-dataset-api/get-dataset-metadata)
