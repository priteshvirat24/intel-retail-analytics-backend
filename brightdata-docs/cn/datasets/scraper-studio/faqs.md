> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Scraper Studio 常见问题

> Bright Data Scraper Studio 常见问题解答：爬虫类型、输入与输出、计费、限制、快照与问题反馈。

本页回答 Bright Data 支持团队最常被问到的 Scraper Studio 问题。如果您想看演练而不是快速答案，请先阅读[了解 Scraper Studio](/cn/datasets/scraper-studio/introduction)。

## 通用问题

<AccordionGroup>
  <Accordion title="什么是 Bright Data 网页爬虫？">
    Bright Data 网页爬虫是一段自动化脚本，通过 Bright Data 的代理与解封基础设施大规模采集公开网页数据。它以结构化格式（JSON、NDJSON、CSV、XLSX）返回采集到的数据，并可交付到 API 端点、webhook、云存储或 SFTP。Bright Data 在 [Scrapers Library](https://www.bright.cn/products/web-scraper) 中维护数百个面向主流站点的预构建爬虫。
  </Accordion>

  <Accordion title="什么是 Bright Data Scraper Studio？">
    Bright Data Scraper Studio 是用于构建自定义爬虫的云端环境。它提供两种模式：从自然语言描述生成爬虫的 AI Agent，以及可直接编写 JavaScript 的 IDE。两种模式都运行在同一套 Bright Data 代理与解封基础设施之上。详见[了解 Scraper Studio](/cn/datasets/scraper-studio/introduction)。
  </Accordion>

  <Accordion title="Scraper Studio 与 Scrapers Library 有什么区别？">
    [Scrapers Library](https://www.bright.cn/products/web-scraper) 提供 Bright Data 为 Amazon、LinkedIn、Instagram 等主流站点维护的预构建爬虫。Bright Data Scraper Studio 则是您在所需站点不在库内时用来构建自定义爬虫的环境。
  </Accordion>

  <Accordion title="一个爬虫可以从多个网站采集数据吗？">
    可以。单个爬虫可以导航到您作为输入传入的任意 URL。如果不同站点需要不同的提取逻辑，可以使用多阶段（`next_stage()`），或为每个站点构建独立的爬虫。
  </Accordion>
</AccordionGroup>

## 输入、输出与 schema

<AccordionGroup>
  <Accordion title="什么是爬虫输入？">
    输入是 Bright Data Scraper Studio 在单次运行时传给爬虫的参数集合。典型输入包括 URL、搜索关键词、产品 ID 或 ASIN、用户名或日期范围。可以通过 CSV 上传或 API 在一次任务中传入多条输入。
  </Accordion>

  <Accordion title="什么是爬虫输出？">
    输出是爬虫针对一条输入返回的结构化数据。Bright Data Scraper Studio 会根据爬虫的交付偏好以 JSON、NDJSON、CSV、XLSX 或 Parquet 格式交付输出。
  </Accordion>

  <Accordion title="为什么我收到的记录数比输入数多？">
    一条输入可能产生多条记录。例如，您提交 5 个产品列表页 URL，每个列表页包含 20 个产品，那么 5 条输入会得到 100 条记录。统计页面统计的是记录数，而不是输入数。
  </Accordion>

  <Accordion title="什么是搜索爬虫？">
    搜索爬虫接收关键词作为输入，而不是 URL。Bright Data Scraper Studio 会在目标站点上执行搜索，并从结果页中提取数据。当您没有具体 URL 时可使用搜索爬虫。
  </Accordion>

  <Accordion title="什么是 discovery 爬虫？">
    Discovery 爬虫从列表页（如搜索结果、分类页或目录页）采集数据。它会提取列表上直接可见的字段（标题、价格、评分），也可以收集产品 URL 或 ID 以供后续的产品页爬取。
  </Accordion>

  <Accordion title="如果我在 Bright Data 处理托管爬虫期间更新了它的 schema，怎么办？">
    当输入或输出 schema 发生变化时，爬虫必须更新以匹配新 schema。如果在 Bright Data 完成更新之前触发爬虫，您会看到 `input(output)_schema_incompatible` 错误。

    若想忽略 schema 不匹配并继续触发，可在 UI 中点击 **Trigger anyway**（仍然触发），或在 API 请求中添加参数：

    * 输出 schema 不兼容：`override_incompatible_schema=1`
    * 输入 schema 不兼容：`override_incompatible_input_schema=1`

    ```bash theme={null}
    curl "https://api.brightdata.com/dca/trigger?scraper=ID_COLLECTOR&queue_next=1&override_incompatible_schema=1" \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer API_KEY" \
      -d '[{"url":"https://targetwebsite.com/product_id/"}]'
    ```
  </Accordion>
</AccordionGroup>

## 构建与编辑爬虫

<AccordionGroup>
  <Accordion title="如何开始构建爬虫？">
    Bright Data Scraper Studio 中有三种方式：

    * **使用 AI Agent 构建**：用自然语言描述您想要的数据。详见 [Scraper Studio AI Agent](/cn/datasets/scraper-studio/ai-agent)。
    * **在 IDE 中构建**：直接编写 JavaScript。详见[使用 IDE 开发爬虫](/cn/datasets/scraper-studio/develop-a-scraper)。
    * **申请托管爬虫**：由 Bright Data 数据团队为您构建并维护爬虫。
  </Accordion>

  <Accordion title="AI Agent 构建好爬虫后，我还能在 IDE 中修改代码吗？">
    可以。每个爬虫 —— 包括 AI Agent 生成的 —— 都可以在 Bright Data Scraper Studio IDE 中打开并编辑。您可以修改提取逻辑、调整选择器、增删输出字段，以及优化性能。如果不想写代码，可以使用[自我修复工具](/cn/datasets/scraper-studio/self-healing-tool)用自然语言提交修改请求。
  </Accordion>

  <Accordion title="AI Agent 是如何构建爬虫的？">
    向 AI Agent 传入一个目标 URL 和（可选的）想要数据的描述。AI Agent 会提出澄清问题、生成输出 schema 供您审查，并在您批准 schema 后写出完整的爬虫代码。之后您可以立刻运行爬虫，或安排周期性运行。完整演练参见 [Scraper Studio AI Agent](/cn/datasets/scraper-studio/ai-agent)。
  </Accordion>
</AccordionGroup>

## 运行与触发爬虫

<AccordionGroup>
  <Accordion title="有哪些触发爬虫的方式？">
    Bright Data Scraper Studio 支持三种触发方式：

    * **通过 API**：普通请求、排队请求或替换请求
    * **手动**：从控制面板触发
    * **按计划**：每小时、每日、每周或自定义

    详见[启动数据收集与交付](/cn/datasets/scraper-studio/initiate-collection-and-delivery-options)。
  </Accordion>

  <Accordion title="什么是排队 API 请求？">
    排队请求告诉 Bright Data Scraper Studio 在同一爬虫的上一个请求完成后再启动下一个。当您希望串行执行而非并行运行多个任务时使用它。
  </Accordion>

  <Accordion title="并发任务限制是多少？">
    Bright Data Scraper Studio 每个爬虫最多并行运行 **1,000 个批量任务**。超出部分会自动排队，等容量释放后启动。完整限制参见 [Scraper Studio 规格说明](/cn/datasets/scraper-studio/specifications)。
  </Accordion>

  <Accordion title="如何调试实时爬虫？">
    在 Bright Data Scraper Studio 仪表盘上点击 **Failed crawls**（失败抓取）下的 **Bug** 图标可在 IDE 中打开该爬虫。失败的输入会显示在 **Last errors**（最近错误）选项卡，附带精确的错误信息和错误码。Bright Data 会为每个虚拟任务保留最近 1,000 次错误，方便您重新运行失败的输入并诊断问题。
  </Accordion>
</AccordionGroup>

## 计费与限制

<AccordionGroup>
  <Accordion title="Scraper Studio 计费中的 CPM 是什么？">
    CPM 是 "cost per mille"（每千次成本）的缩写，即 1,000 次页面加载。Bright Data Scraper Studio 按 CPM 单位对页面加载计费。当前费率请参见[定价页面](https://www.bright.cn/pricing/web-scraper/studio)。
  </Accordion>

  <Accordion title="哪些操作属于计费事件？">
    计费事件指任何让 Bright Data Scraper Studio 加载页面或发起网络请求的函数：

    * `navigate()`
    * `request()`
    * `load_more()`
    * 媒体文件下载（按 GB 计费，与 CPM 分开）
  </Accordion>

  <Accordion title="Scraper Studio 有自己的免费试用额度吗？">
    Scraper Studio 没有单独的页面加载或记录额度，但它包含在账户级免费套餐内。每个新账户每月可获得 5,000 个免费信用额度，这是一个可用于 Web Unlocker API、SERP API、Web Scraper API 和 Scraper Studio 的单一共享池。在免费套餐中，Scraper Studio 每次页面加载消耗一个信用额度，从该池中扣除；记录默认不计费。新账户还会获得一笔可用于任意 Bright Data 产品的一次性新手赠送额度。参见[免费套餐](/cn/general/account/billing-and-pricing/free-tier)和[计费](/cn/general/account/billing-and-pricing/billing)页面。
  </Accordion>
</AccordionGroup>

## 快照与数据保留

<AccordionGroup>
  <Accordion title="采集完成后快照可保留多久？">
    快照保留期取决于采集类型：

    * **批量采集**：16 天
    * **实时采集**：7 天

    超期后快照会被永久删除。Bright Data 不会恢复已过期的数据。请在保留窗口关闭前下载或导出数据，或配置爬虫通过 webhook、API 下载或云存储自动交付结果。
  </Accordion>
</AccordionGroup>

## 反馈问题

<AccordionGroup>
  <Accordion title="如何反馈爬虫问题？">
    在 Bright Data Scraper Studio 控制面板中打开爬虫，从三点菜单选择 **Report an issue**（反馈问题）。Bright Data 会根据问题类型将工单路由到不同团队：

    * **Data**（缺失字段、缺失记录、解析错误）：路由给爬虫工程师。仅适用于托管爬虫。
    * **Collection and delivery**（交付不完整、爬虫运行慢）：路由给支持团队。
    * **Other**（UI 问题、产品咨询）：路由给客户经理。

    请附上受影响的 job ID、问题描述，以及能说明问题的截图或文件。
  </Accordion>

  <Accordion title="提交 bug 报告时应包含哪些信息？">
    包含以下内容：

    * 问题分类（数据错误、缺失记录、交付问题、IDE 问题、其他）
    * 问题的精确描述
    * 受影响的 job ID
    * 能展示问题的截图或文件（如有）

    Bright Data 会自动创建工单，由研发团队处理。
  </Accordion>

  <Accordion title="如何确认 Bright Data 正在处理我的托管爬虫请求？">
    当 Bright Data 工程师开始构建爬虫时您会收到一封邮件，爬虫准备就绪时会再收到一封邮件。您也可以在 Scrapers 仪表盘上跟踪状态。
  </Accordion>
</AccordionGroup>

## 相关内容

<CardGroup cols={2}>
  <Card title="了解 Scraper Studio" icon="book-open" href="/cn/datasets/scraper-studio/introduction">
    Bright Data Scraper Studio 如何工作以及何时使用
  </Card>

  <Card title="规格说明" icon="file-lines" href="/cn/datasets/scraper-studio/specifications">
    基础设施限制、计费与数据保留
  </Card>
</CardGroup>
