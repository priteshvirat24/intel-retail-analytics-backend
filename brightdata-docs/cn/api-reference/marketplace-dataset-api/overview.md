> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Dataset API：Search 与 Filter

> 通过两个端点查询 Bright Data 市场数据集：Search 用于亚秒级查询，Filter 用于批量异步任务。共享筛选语法，$2.5 CPM。

Bright Data 市场数据集 API（Marketplace Dataset API）提供两个端点，用于从 250+ 个市场数据集中提取记录：**Search** 用于实时查询，**Filter** 用于批量异步任务。两个端点共享同一套筛选 schema、同一种身份验证方式以及相同的 \$2.5 CPM 定价。

<Tip>
  将您的 API Key 粘贴到授权字段。要获取 API Key，请[创建账户](https://www.bright.cn/?hs_signup=1\&utm_source=docs\&utm_campaign=playground)并了解[如何生成 API Key](/cn/api-reference/authentication#如何生成新的-api-key？)。
</Tip>

## Dataset API 有哪两个端点？

市场数据集 API 提供两种提取记录的方式，可根据任务选择：

* **Search（同步）** 基于 Elasticsearch，以亚秒级响应内联返回记录。适用于实时查询、线索增强和抽样。
* **Filter（异步）** 基于快照，支持 CSV/JSON 文件上传和大体量负载。适用于批量导出和值列表筛选。

<CardGroup cols={2}>
  <Card title="Search 数据集（同步）" href="/cn/api-reference/marketplace-dataset-api/search-dataset" icon="bolt">
    Elasticsearch 查询，内联返回结果，亚秒级延迟。每次调用最多 1,000 条记录。
  </Card>

  <Card title="Filter 数据集（异步）" href="/cn/api-reference/marketplace-dataset-api/filter-dataset" icon="layer-group">
    基于快照的任务，支持 CSV/JSON 上传，负载最大 200 MiB。覆盖全部 250+ 个数据集。
  </Card>
</CardGroup>

## 我该使用哪个端点？

低延迟、单次调用的查询使用 Search；批量或基于文件的任务使用 Filter。

| 需求                        | 使用                           |
| ------------------------- | ---------------------------- |
| 实时查询，最多 1,000 条记录，亚秒级延迟   | Search                       |
| 对单条记录进行线索增强               | Search                       |
| 购买前快速抽样数据集                | Search，搭配 `"sort": "random"` |
| 批量导出或大规模提取                | Filter                       |
| 按 CSV/JSON 中 10 万以上的值列表筛选 | Filter                       |
| Search 尚不支持的数据集           | Filter                       |

## 两个端点有何区别？

Search 和 Filter 端点接受相同的 filter 对象，但在引擎、延迟和数据集覆盖范围上有所不同。

|                | Search                              | Filter                  |
| -------------- | ----------------------------------- | ----------------------- |
| 路径             | `POST /datasets/search/:dataset_id` | `POST /datasets/filter` |
| 引擎             | Elasticsearch                       | 基于快照                    |
| 模式             | 同步（内联返回结果）                          | 异步（返回 `snapshot_id`）    |
| 延迟             | 亚秒级                                 | 每个任务最长 5 分钟             |
| 数据集            | 3 个 LinkedIn 数据集（alpha）             | 全部 250+ 个市场数据集          |
| 最大负载           | 单个请求体                               | 最大 200 MiB（multipart）   |
| 文件上传（CSV/JSON） | 不支持                                 | 支持                      |
| 分页             | `search_after` 游标                   | 快照上的 `records_limit`    |
| 返回             | `hits`、`total_hits`、`took`          | `snapshot_id`（需单独下载）    |
| 定价             | \$2.5 CPM                           | \$2.5 CPM               |

两个引擎之间的结果可能存在差异。Elasticsearch 对文本的分词方式与快照引擎不同。

## 如何进行身份验证？

两个端点都使用 Bearer token 身份验证。在 `Authorization` 请求头中传入您的 API Key：

```bash theme={null}
Authorization: Bearer YOUR_API_KEY
```

从[账户设置](/cn/api-reference/authentication#如何生成新的-api-key？)获取您的 Key。

## Dataset API 的费用是多少？

两个端点的费用均为 \$2.5 CPM（每返回 1,000 条记录），与市场价格相同。实时 Search 不收取额外费用，筛选返回 0 条记录时也不收费。

| 项目              | 价格                       |
| --------------- | ------------------------ |
| Search 与 Filter | \$2.5 CPM（每返回 1,000 条记录） |
| 零匹配查询           | 免费（筛选返回 0 条记录时不收费）       |
| 订阅              | 按月承诺用量，超额部分享受更低的有效 CPM   |
| 企业版             | 定制 SLA，专属容量              |

## 筛选语法在哪里查看？

两个端点都接受相同的 `filter` 对象，运算符和嵌套规则一致。[筛选语法参考](/cn/api-reference/marketplace-dataset-api/filter-syntax)记录了运算符列表、筛选组、最多 3 层嵌套以及 CSV/JSON 文件引用。

## 相关文档

* [Search 数据集（同步）](/cn/api-reference/marketplace-dataset-api/search-dataset)
* [Filter 数据集（异步，文件上传）](/cn/api-reference/marketplace-dataset-api/filter-dataset)
* [筛选语法参考](/cn/api-reference/marketplace-dataset-api/filter-syntax)
* [获取数据集元数据](/cn/api-reference/marketplace-dataset-api/get-dataset-metadata)
* [获取数据集列表](/cn/api-reference/marketplace-dataset-api/get-dataset-list)
* 在查询前构建或刷新数据集，请参阅[创建数据收集请求](/cn/api-reference/marketplace-api/request-a-collection)。
