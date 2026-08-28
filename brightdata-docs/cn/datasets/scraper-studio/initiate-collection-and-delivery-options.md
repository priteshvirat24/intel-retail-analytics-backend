> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 启动数据收集与交付

> 通过 API、手动或按计划触发 Bright Data Scraper Studio 采集，并交付到 webhook、S3、GCS、Azure、SFTP、电子邮件或 API 下载。

在 Bright Data Scraper Studio 中把爬虫保存到生产环境后，您可以通过三种方式触发采集运行（API、手动、按计划），并以五种格式（JSON、NDJSON、CSV、XLSX、Parquet）将结果交付到八种目的地（API 下载、webhook、Amazon S3、Google Cloud Storage、Azure Blob Storage、Alibaba Cloud OSS、SFTP 或电子邮件）。本页涵盖所有选项。

## 前提条件

* 一个已在 [Bright Data Scraper Studio IDE](https://www.bright.cn/cp/scrapers) 中保存到生产环境的爬虫
* 通过 API 触发或 API 交付时所需的 API key（[创建一个](https://www.bright.cn/cp/setting)）

## 如何把爬虫保存到生产环境？

在 Bright Data Scraper Studio IDE 中编辑代码时，系统会自动将您的工作保存为开发草稿。要让爬虫能在 IDE 之外运行，请点击 IDE 右上角的 **Save to Production**（保存到生产环境）。所有生产爬虫会出现在控制面板的 **My Scrapers**（我的爬虫）下，非活动爬虫以淡化状态显示。

<Frame>
  <img src="https://mintcdn.com/brightdata/S8tFtc_KJjCQxqv1/images/scraping-automation/web-scraping-ide/initiate-collection-and-delivery-options/my-scrapers.png?fit=max&auto=format&n=S8tFtc_KJjCQxqv1&q=85&s=28548dc0a6188b85153537e7292a3920" alt="My Scrapers 仪表盘，显示已保存的爬虫" width="1317" height="831" data-path="images/scraping-automation/web-scraping-ide/initiate-collection-and-delivery-options/my-scrapers.png" />
</Frame>

## 如何触发爬虫运行？

Bright Data Scraper Studio 支持三种启动采集的方式。

<Tabs>
  <Tab title="通过 API 启动">
    无需打开控制面板，通过 REST API 启动采集。认证、请求格式与响应 schema 请参见 [API 入门指南](/cn/datasets/scraper-studio/quickstart)。

    在发送请求前，请先创建 API key。前往 [仪表盘 > 账户设置 > API key](https://www.bright.cn/cp/setting)。

    <Frame>
      <img src="https://mintcdn.com/brightdata/S8tFtc_KJjCQxqv1/images/scraping-automation/web-scraping-ide/initiate-collection-and-delivery-options/initiate-by-api.png?fit=max&auto=format&n=S8tFtc_KJjCQxqv1&q=85&s=321de2e5a0c32b4955cb0eaf297e405a" alt="通过 API 启动爬虫" width="1712" height="453" data-path="images/scraping-automation/web-scraping-ide/initiate-collection-and-delivery-options/initiate-by-api.png" />
    </Frame>

    API 触发面板提供三项内容：

    1. **Inputs（输入）：** 手动或通过 API 请求体提供输入值
    2. **Trigger behavior（触发行为）：** 将多个请求加入队列以并行或顺序运行；排队任务按提交顺序执行
    3. **API 请求预览：** Bright Data 会为您生成一条可直接运行的 `curl` 命令。请为 `curl` 选择 **Linux Bash** 视图。响应中包含一个 `collection_id`，稍后可用它拉取数据。

    <Note>
      当交付方式设置为 **API download**（API 下载）时，必须调用 "Receive data" API 端点才能获取结果。Webhook 与云存储目的地会自动推送数据。
    </Note>
  </Tab>

  <Tab title="手动启动">
    无需写代码，直接从 Bright Data 控制面板启动采集。

    <Frame>
      <img src="https://mintcdn.com/brightdata/S8tFtc_KJjCQxqv1/images/scraping-automation/web-scraping-ide/initiate-collection-and-delivery-options/initiate-manually.png?fit=max&auto=format&n=S8tFtc_KJjCQxqv1&q=85&s=aa8ca692b4ad631beb71991933ddd926" alt="手动启动爬虫" width="1718" height="515" data-path="images/scraping-automation/web-scraping-ide/initiate-collection-and-delivery-options/initiate-manually.png" />
    </Frame>

    1. **Trigger behavior（触发行为）：** 并行添加多个请求，或在已有任务完成后排队添加新任务
    2. **Set up inputs manually（手动设置输入）：** 在表单中逐项输入参数
    3. **Upload CSV file（上传 CSV 文件）：** 对于大批量输入集，可上传 CSV（例如 URL 列表）。Bright Data 提供可下载的模板。
  </Tab>

  <Tab title="按计划运行">
    按周期性计划运行爬虫。

    **步骤 1：配置计划**

    1. 选择开始日期与时间
    2. 选择频率（每小时、每日、每周或自定义）
    3. 设置爬虫必须完成的截止时间
    4. 检查配置

    <Frame>
      <img src="https://mintcdn.com/brightdata/S8tFtc_KJjCQxqv1/images/scraping-automation/web-scraping-ide/initiate-collection-and-delivery-options/schedule-configuration.png?fit=max&auto=format&n=S8tFtc_KJjCQxqv1&q=85&s=796dfce40a21e6115fdda7e466f5552e" alt="计划配置界面" width="1738" height="908" data-path="images/scraping-automation/web-scraping-ide/initiate-collection-and-delivery-options/schedule-configuration.png" />
    </Frame>

    **步骤 2：设置输入**

    1. 上传含有大批量输入集的 CSV 文件（例如 URL 列表）。下载 CSV 模板以匹配预期格式
    2. 或在表单中手动输入

    <Frame>
      <img src="https://mintcdn.com/brightdata/S8tFtc_KJjCQxqv1/images/scraping-automation/web-scraping-ide/initiate-collection-and-delivery-options/enter-input.png?fit=max&auto=format&n=S8tFtc_KJjCQxqv1&q=85&s=28f558fd234ef4255abe7a8a397497af" alt="为计划运行输入参数" width="1735" height="912" data-path="images/scraping-automation/web-scraping-ide/initiate-collection-and-delivery-options/enter-input.png" />
    </Frame>
  </Tab>
</Tabs>

## 速率限制与并发限制是多少？

Bright Data Scraper Studio 按爬虫强制执行并发限制，依据请求是批量还是实时。

| 采集类型          | 并发限制               |
| ------------- | ------------------ |
| Batch（批量）     | 每个爬虫最多 1,000 个并发请求 |
| Real-time（实时） | 无限制                |

当超出批量限制时，Bright Data 会返回错误：`Maximum limit of 1000 jobs per scraper has been exceeded. Please reduce the number of parallel jobs.`

## 批量 vs 实时采集

Bright Data Scraper Studio 提供两种采集方法，分别针对不同使用场景做了优化。

|      | Batch 批量采集           | Real-time 实时采集 |
| ---- | -------------------- | -------------- |
| 输入规模 | 每个任务多条输入（URL 或关键词列表） | 每个请求一条输入       |
| 响应时机 | 任务全部完成后返回结果          | 实时返回响应         |
| 保留期  | 16 天                 | 7 天            |
| 并发限制 | 1,000 个并发任务          | 无              |
| 适用场景 | 构建数据集且可等待            | 在一次实时请求内得到结果   |

两种方法都可靠，选择与您应用形态匹配的那一种即可。

## 如何配置交付？

打开 **My Scrapers**，点击爬虫所在行，选择 **Delivery preferences**（交付偏好）以设置 Bright Data Scraper Studio 投递结果的目的地与方式。

<AccordionGroup>
  <Accordion title="什么时候接收数据？">
    * **Batch（批量）：** 整个任务完成后获取结果；适合大数据集
      * **Split batch（分批）：** 准备就绪的部分结果以小批次先行交付
    * **Real-time（实时）：** 获取单次请求的快速响应
      * **Skip retries（跳过重试）：** 出错时不重试（以完整性换取速度）
  </Accordion>

  <Accordion title="支持哪些文件格式？">
    * JSON
    * NDJSON
    * CSV
    * XLSX
    * Parquet
  </Accordion>

  <Accordion title="支持哪些交付目的地？">
    * 电子邮件
    * API 下载（通过 REST API 拉取）
    * Webhook（通过 HTTPS POST 推送）
    * 云存储：Amazon S3、Google Cloud Storage、Azure Blob Storage、Alibaba Cloud OSS
    * SFTP / FTP

    <Note>
      媒体文件无法通过电子邮件或 API 下载交付。采集图片、视频或其他二进制内容时请使用云存储、SFTP 或 webhook。
    </Note>
  </Accordion>

  <Accordion title="如何控制批量输出的内容？">
    * 结果与错误分别输出到两个文件
    * 结果与错误合并到一个文件
    * 仅成功的结果
    * 仅错误
  </Accordion>

  <Accordion title="可启用哪些通知？">
    * 采集完成时通知
    * 触达成功率阈值时通知
    * 出现错误时通知
  </Accordion>
</AccordionGroup>

## 如何配置输出 schema？

输出 schema 定义您所采集数据的结构：字段名、数据类型、默认值，以及您希望 Bright Data Scraper Studio 附加的任何额外元数据（时间戳、截图、WARC 快照）。

<img src="https://mintcdn.com/brightdata/S8tFtc_KJjCQxqv1/images/scraping-automation/web-scraping-ide/initiate-collection-and-delivery-options/output-schema.png?fit=max&auto=format&n=S8tFtc_KJjCQxqv1&q=85&s=b1de278398b8a42767334caa19c81d2a" alt="输出 schema 配置" width="1600" height="853" data-path="images/scraping-automation/web-scraping-ide/initiate-collection-and-delivery-options/output-schema.png" />

| 控件                        | 说明                     |
| ------------------------- | ---------------------- |
| **Input / Output schema** | 在输入与输出两种 schema 视图之间切换 |
| **Custom validation**     | 定义对每条采集记录运行的校验规则       |
| **Parsed data**           | 爬虫解析器代码输出的原始字段         |
| **Add new field**         | 按名称与类型新增字段             |
| **Additional data**       | 可选元数据：时间戳、截图、WARC 快照等  |

## 相关内容

<CardGroup cols={2}>
  <Card title="Scraper Studio 规格说明" icon="file-lines" href="/cn/datasets/scraper-studio/specifications">
    基础设施限制、计费与数据保留
  </Card>

  <Card title="WARC 快照" icon="file-zipper" href="/cn/datasets/scraper-studio/warc-ide">
    在采集数据的同时归档原始 HTTP 响应
  </Card>
</CardGroup>
