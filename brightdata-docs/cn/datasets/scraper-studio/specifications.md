> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Scraper Studio 规格说明

> Bright Data Scraper Studio 基础设施限制、计费模式（CPM + 按 GB 下载）以及批量和实时快照的数据保留规则。

本参考文档涵盖 Bright Data Scraper Studio 的基础设施限制、计费模式和数据保留规则。

## 计费

Bright Data Scraper Studio 的计费基于页面加载和文件下载。

| 项目   | 单位                 | 费率                                                         |
| ---- | ------------------ | ---------------------------------------------------------- |
| 页面加载 | CPM（每 1,000 次页面加载） | 见 [定价页面](https://www.bright.cn/pricing/web-scraper/studio) |
| 文件下载 | 每 GB               | 单独计费，不包含在页面加载费用中                                           |

**页面加载的定义：** Bright Data Scraper Studio 基础设施处理的一次 URL 请求，无论响应大小如何。

<Note>
  文件下载按单独的每 GB 费率计费，不计入 CPM。查看您的 [计费仪表板](https://www.bright.cn/cp/billing/overview) 了解当前费率。
</Note>

## 基础设施限制

| 项目      | 限制          | 超出限制时的行为   |
| ------- | ----------- | ---------- |
| 并行批处理作业 | 1,000 个同时作业 | 其他作业自动排队   |
| 作业队列大小  | 无限制         | 当容量可用时作业运行 |

## 数据保留

| 数据类型   | 保留期  | 过期后的行为 |
| ------ | ---- | ------ |
| 批量收集结果 | 16 天 | 永久删除   |
| 实时结果   | 7 天  | 永久删除   |

<Warning>
  请在保留期到期前导出您的数据。Bright Data 不会恢复已过期的数据。
</Warning>

## 常见问题

<AccordionGroup>
  <Accordion title="当我超过 1,000 个并行作业时会发生什么？">
    其他作业会自动排队。不会有任何作业被丢弃或取消。作业按提交顺序在容量可用时运行。
  </Accordion>

  <Accordion title="保留期过后我的数据会怎样？">
    数据会在 16 天（批量）或 7 天（实时）后被永久删除。Bright Data 不会恢复已过期的数据。请在过期前导出您的结果。
  </Accordion>

  <Accordion title="文件下载是否包含在我的 CPM 计费中？">
    不包括。文件下载按单独的每 GB 费率计费。CPM 仅涵盖页面加载。两项费用都会显示在您的 [计费仪表板](https://www.bright.cn/cp/billing/overview) 中。
  </Accordion>

  <Accordion title="什么被定义为页面加载？">
    一次页面加载等于 Bright Data Scraper Studio 基础设施处理的一次 URL 请求，无论页面大小或响应内容如何。
  </Accordion>
</AccordionGroup>

## 相关内容

<CardGroup cols={2}>
  <Card title="了解 Scraper Studio" icon="book-open" href="/cn/datasets/scraper-studio/introduction">
    了解 Scraper Studio 的工作原理以及何时使用它
  </Card>

  <Card title="定价与计费" icon="credit-card" href="https://www.bright.cn/cp/billing/overview">
    所有 Bright Data 产品的完整计费详情
  </Card>
</CardGroup>
