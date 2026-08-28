> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 区域总费用与带宽

> 返回某个 Zone 在指定日期范围内的计费费用、带宽和使用统计，与控制面板的“使用情况概览”及发票数据保持一致。

<Warning id="to-is-exclusive">
  **`to` 参数不包含结束日期。** 指定的日期**不会**包含在结果中。要匹配控制面板或发票中显示的某个完整自然月，请将 `to` 设置为**下一个月**的第一天。例如，`from=2026-04-01&to=2026-05-01` 将返回 2026 年 4 月的全部数据。
</Warning>

<Note>
  此端点的范围仅限单个 zone，无法返回 Web Scraper API 或 Scraper Studio 的费用数据（这些费用以 `dataset_id` / collector ID 为键，而非以 zone 名称为键）。如需跨产品或 WSA / Scraper Studio 维度的费用明细，请使用 [费用明细导出](/cn/api-reference/account-management-api/Export_cost_breakdown)。
</Note>

<Tip>
  将您的 API key 粘贴到授权字段中。要获取 API key，请[创建账号](https://www.bright.cn/?hs_signup=1\&utm_source=docs\&utm_campaign=playground)，并查看[如何生成新的 API key？](/cn/api-reference/authentication#如何生成新的-api-key？)
</Tip>

## 复现您的月度发票

要获取与控制面板和发票上完全一致的某个自然月计费用量，请将 `from` 设置为该月第一天，将 `to` 设置为**下一个月**的第一天：

```bash theme={null}
# 返回 2026 年 4 月的全部计费用量
curl -H "Authorization: Bearer YOUR_API_KEY" \
  "https://api.brightdata.com/zone/cost?zone=YOUR_ZONE&from=2026-04-01&to=2026-05-01"
```

如果使用 `to=2026-04-30`，将会漏掉当月最后一天。请始终将 `to` 设置为您希望包含的最后一天的**下一天**。

## 与原始请求日志对账

此端点返回的值是计费的真实数据来源，与控制面板的“使用情况概览”以及您的发票相匹配。如果将这些值与您自行采集的原始请求日志（例如转发到 Logz、CloudWatch 或其他系统的访问日志）进行比较，预计会有几个百分点的差异。原始日志可能记录到一些请求，但这些请求由于异步聚合时延或临时网络问题未被提交到计费数据库。您的发票始终反映此端点返回的值。

## 相关端点

* [区域带宽统计](/cn/api-reference/account-management-api/Get_the_bandwidth_stats_for_a_Zone)。仅带宽，不含费用。
* [所有区域带宽统计](/cn/api-reference/account-management-api/Get_the_bandwidth_stats_for_all_your_Zones)。跨区域汇总。


## OpenAPI

````yaml cn-openapi GET /zone/cost
openapi: 3.0.1
info:
  title: Bright Data API
  description: 将 Bright Data API 集成到您的流程中，以实现高端的爬取精度
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security:
  - bearerAuth: []
paths:
  /zone/cost:
    get:
      description: 获取区域总成本和带宽统计信息
      parameters:
        - in: query
          name: zone
          description: 区域名称
          required: true
          schema:
            type: string
        - in: query
          name: from
          description: 开始时间
          required: false
          schema:
            type: string
        - in: query
          name: to
          description: 结束时间
          required: false
          schema:
            type: string
      responses:
        '200':
          description: 成功
          content:
            application/json:
              schema:
                type: object
                example:
                  ID:
                    back_m2:
                      bw: 0
                      cost: 0
                    back_m1:
                      bw: 36557298
                      cost: 0
                    back_m0:
                      bw: 1219004
                      cost: 0
                    back_d2:
                      bw: 82190
                      cost: 0
                    back_d1:
                      bw: 0
                      cost: 0
                    back_d0:
                      bw: 0
                      cost: 0
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        在 Authorization 头中使用您的 Bright Data API Key 作为 Bearer token。


        **认证方法:**

        1. 从 Bright Data 账户设置获取您的 API Key:
        https://brightdata.com/cp/setting/users

        2. 在请求的 Authorization 头中包含 API Key

        3. 格式: `Authorization: Bearer YOUR_API_KEY`


        **示例:**

        ```

        Authorization: Bearer
        b5648e1096c6442f60a6c4bbbe73f8d2234d3d8324554bd6a7ec8f3f251f07df

        ```


        了解如何获取 Bright Data API Key:
        https://docs.brightdata.com/cn/api-reference/authentication#如何生成新的-api-key？
      bearerFormat: API Key

````