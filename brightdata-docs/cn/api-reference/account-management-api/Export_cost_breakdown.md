> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 费用明细导出

> 按维度（products、zones、datasets、Web Scraper API 等）导出账户费用数据，与 Cost Explorer 同源。支持 JSON 或 CSV，按天按资源粒度返回。

此端点用于按您选定的维度（products、zones、datasets、Web Scraper API、collectors、domains、dataset snapshots 或 WSA snapshots），以 JSON 或 CSV 格式导出每天每资源的费用明细，数据与控制面板 Cost Explorer 完全一致。

<Warning id="to-is-exclusive">
  **`to` 参数不包含结束日期。** 指定的日期**不会**包含在结果中。要匹配控制面板或发票中显示的某个完整自然月，请将 `to` 设置为**下一个月**的第一天。例如，`from=2026-04-01&to=2026-05-01` 将返回 2026 年 4 月的全部数据。
</Warning>

<Tip>
  将您的 API key 粘贴到授权字段中。要获取 API key，请[创建账号](https://www.bright.cn/?hs_signup=1\&utm_source=docs\&utm_campaign=playground)，并查看[如何生成新的 API key？](/cn/api-reference/authentication#如何生成新的-api-key？)
</Tip>

## 何时使用此端点

当 `GET /zone/cost` 无法满足需要时，请使用此端点。`/zone/cost` 端点仅作用于单个 zone，因此无法拆分 Web Scraper API 的费用（这些费用以 `dataset_id` 为键，而非 zone 名称），也无法回答诸如"我上月在数据中心代理和 Unlocker 上一共花了多少？"这类跨产品问题。

此端点通过 `dimension` 参数按 Cost Explorer 中相同的分组进行费用聚合。

| 维度             | 费用分组方式                                                                  |
| -------------- | ----------------------------------------------------------------------- |
| `products`     | 产品家族（datacenter、residential、ISP、mobile、unlocker、SERP API、Browser API 等） |
| `types`        | 网络或计费类型                                                                 |
| `zones`        | 账户中的各个 zone                                                             |
| `datasets`     | Dataset Marketplace 数据集购买                                               |
| `web_apis`     | Web Scraper API 的 `dataset_id`                                          |
| `collectors`   | Scraper Studio collectors                                               |
| `domains`      | 目标域名                                                                    |
| `ws_api_snaps` | Web Scraper API 快照                                                      |
| `snapshots`    | Dataset 快照                                                              |

各维度与控制面板 Cost Explorer 中看到的分组一致；了解每个维度返回什么的最简单方式，就是在控制面板中打开 Cost Explorer 并切换分组。

## 按某个维度复现您的月度发票

要获取 2026 年 4 月按 Web Scraper API dataset 拆分的完整月度费用：

```bash theme={null}
curl -X POST -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "dimension": "web_apis",
    "filters": {},
    "from": "2026-04-01",
    "to": "2026-05-01"
  }' \
  "https://api.brightdata.com/costs/export/json"
```

响应结构（按天一条记录，每天再按资源 ID 对应计费美元金额）：

```json theme={null}
{
  "2026-04-01": {
    "gd_l1viktl72bvl7bjuj0": 45.20,
    "gd_l1vikfnt1wgvvqz95w": 12.80
  },
  "2026-04-02": {
    "gd_l1viktl72bvl7bjuj0": 38.10
  }
}
```

如需以 CSV 获取相同数据，请以相同的请求体调用 `POST /costs/export/csv`。CSV 会将响应转置为每天一行，每个出现在该日期范围内的资源 ID 对应一列，因此列数会随数据而变化：

```csv theme={null}
Day,gd_l1viktl72bvl7bjuj0,gd_l1vikfnt1wgvvqz95w
2026-04-01,45.20,12.80
2026-04-02,38.10,0
```

## 使用 `filters` 字段

`filters` 对象使用 Bright Data 内部的计费结构语法，与 Cost Explorer 所用语法相同。从零构造过滤条件需要了解该结构。大多数调用方将 `filters` 留空（`{}`），仅依靠 `dimension` 参数对响应进行约束。

下面是一个可用示例，将结果限制为 datacenter 与 Web Unlocker 产品：

```json theme={null}
{
  "props": {
    "product": {
      "whitelist": ["dc", "unblocker"]
    }
  }
}
```

如果需要的过滤条件无法仅靠维度表达，请联系 Bright Data 技术支持，说明您要解答的问题。我们目前未公开完整的过滤语法；技术支持可帮您构建所需过滤条件，或确认无需过滤。

## 速率限制

* 每分钟 1,000 个请求
* 每小时 5,000 个请求

此端点接受任何具有费用数据访问权限的 API key，不需要单独的计费管理员权限。

## 与原始请求日志对账

此端点返回的值是计费的真实数据来源，与控制面板的 Cost Explorer 与"使用情况概览"匹配，并汇总进入您的发票。如果将这些值与您自行采集的原始请求日志（例如转发到 Logz 或 CloudWatch 的访问日志）进行比较，预计会有几个百分点的差异。原始日志可能记录到一些请求，但这些请求由于异步聚合时延或临时网络问题未被提交到计费数据库。您的发票始终反映此端点返回的值。

## 相关端点

* [区域总费用与带宽](/cn/api-reference/account-management-api/Get_the_total_cost_and_bandwidth_stats_for_a_Zone)。单个 zone 在指定日期范围内的费用与带宽。无法返回 Web Scraper API 或 Scraper Studio 的费用。
* [区域带宽统计](/cn/api-reference/account-management-api/Get_the_bandwidth_stats_for_a_Zone)。仅带宽，不含费用。
* [所有区域带宽统计](/cn/api-reference/account-management-api/Get_the_bandwidth_stats_for_all_your_Zones)。跨区域汇总带宽。


## OpenAPI

````yaml cn-openapi POST /costs/export/json
openapi: 3.0.1
info:
  title: Bright Data API
  description: >-
    Integrate Bright Data APIs to your pipeline and secure high-end scraping
    precision
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security:
  - bearerAuth: []
paths:
  /costs/export/json:
    post:
      description: >-
        Export account cost data broken down by dimension (products, zones,
        datasets, Web Scraper APIs, and more) as JSON. This is the same data
        source the Control Panel's Cost Explorer uses. 

         **Note:** the `to` parameter is **exclusive**. The day specified is not included in the result. To match a calendar month shown in the Control Panel or on your invoice, set `to` to the first day of the **following** month (e.g., `from=2026-04-01` and `to=2026-05-01` returns all of April 2026).
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - dimension
                - from
                - to
              properties:
                dimension:
                  type: string
                  description: >-
                    The dimension to group costs by. Same dimension semantics as
                    the Control Panel Cost Explorer.
                  enum:
                    - products
                    - types
                    - zones
                    - datasets
                    - web_apis
                    - collectors
                    - domains
                    - ws_api_snaps
                    - snapshots
                filters:
                  type: object
                  description: >-
                    Optional filter object. Uses Bright Data's internal
                    charges-structure notation and requires knowledge of that
                    structure to construct. Contact Bright Data support if you
                    need help building a filter. 

                     Example: `{ "props": { "product": { "whitelist": ["dc", "unblocker"] } } }`
                from:
                  type: string
                  format: date
                  description: Inclusive start date in `YYYY-MM-DD` format. UTC.
                to:
                  type: string
                  format: date
                  description: >-
                    **Exclusive** end date in `YYYY-MM-DD` format. UTC. The day
                    specified is NOT included in the result. To match a calendar
                    month, set `to` to the first day of the **following** month
                    (e.g., `from=2026-04-01&to=2026-05-01` returns all of April
                    2026).
            example:
              dimension: web_apis
              filters: {}
              from: '2026-04-01'
              to: '2026-05-01'
      responses:
        '200':
          description: >-
            Cost breakdown grouped by day, then by resource ID. The resource ID
            format depends on the requested dimension (e.g., for
            `dimension=web_apis`, resource IDs are dataset IDs like
            `gd_l1viktl72bvl7bjuj0`). Amounts are billed USD for the day.
          content:
            application/json:
              schema:
                type: object
                additionalProperties:
                  type: object
                  additionalProperties:
                    type: number
                example:
                  '2026-04-01':
                    gd_l1viktl72bvl7bjuj0: 45.2
                    gd_l1vikfnt1wgvvqz95w: 12.8
                  '2026-04-02':
                    gd_l1viktl72bvl7bjuj0: 38.1
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        Use your Bright Data API Key as a Bearer token in the Authorization
        header.


        **How to authenticate:**

        1. Obtain your API Key from the Bright Data account settings at
        https://brightdata.com/cp/setting/users

        2. Include the API Key in the Authorization header of your requests

        3. Format: `Authorization: Bearer YOUR_API_KEY`


        **Example:**

        ```

        Authorization: Bearer
        b5648e1096c6442f60a6c4bbbe73f8d2234d3d8324554bd6a7ec8f3f251f07df

        ```


        Learn how to get your Bright Data API key:
        https://docs.brightdata.com/api-reference/authentication
      bearerFormat: API Key

````