> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 概述

> Deep Lookup API 使您能够以编程方式访问搜索并从公开网页中提取结构化数据。通过将实时网页情报直接集成到您的工作流程中，使任何应用程序都成为数据强力引擎。

## 入门指南

**基础 URL：** `https://api.brightdata.com/datasets/deep_lookup/v1`

**身份验证：** 所有 API 请求都需要在请求头中使用您的 API key 进行身份验证。

```bash theme={null}
curl -H "Authorization: Bearer YOUR_API_KEY" \
  https://api.brightdata.com/datasets/deep_lookup/v1/preview
```

## 核心工作流程

Deep Lookup API 遵循一个简单的工作流程，旨在实现最大灵活性和成本控制：

<CardGroup cols={2}>
  <Card title="创建预览" href="/cn/api-reference/deep-lookup/create-preview" icon="square-1">
    启动预览以使用示例结果测试您的查询。
  </Card>

  <Card title="获取预览数据" href="/cn/api-reference/deep-lookup/get-preview-data" icon="square-2">
    处理完成后检索预览结果。
  </Card>

  <Card title="增强查询（可选）" href="/cn/api-reference/deep-lookup/enhance-query" icon="square-3">
    根据预览结果优化您的查询。
  </Card>

  <Card title="触发完整请求" href="/cn/api-reference/deep-lookup/trigger-full-request" icon="square-4">
    使用您期望的参数执行完整研究。
  </Card>
</CardGroup>

<Card title="获取结果" href="/cn/api-reference/deep-lookup/download-results" icon="square-5">
  以 JSON 或 CSV 格式获取结构化数据。
</Card>

## 了解列类型

在使用规格创建请求时，您需要定义列类型：

### 列类型：`enrichment`

添加数据属性而不对结果进行过滤。

> **示例：**
>
> * 公司收入
> * 联系信息
> * 社交媒体资料

### 列类型：`constraint`

根据条件过滤结果。只有满足**所有**约束条件的实体才会被包含。

> **示例：**
>
> * 必须是初创企业
> * 收入超过 \$10M
> * 2020 年之后成立

## 处理步骤

在监控请求进度时，`step` 字段表示当前处理阶段：

| 步骤                  | 描述            |
| :------------------ | :------------ |
| `identifying`       | 理解并分析您的查询     |
| `generating_schema` | 创建结果的数据结构     |
| `generating`        | 从数据源主动采集并处理数据 |
| `done`              | 研究成功完成        |

## Webhooks（即将推出）

配置 webhooks 以在研究完成时接收通知：

```json theme={null}
{
  "webhook_url": "https://your-app.com/webhook",
  "events": ["request.completed", "request.failed"]
}
```
