> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 常见问题解答

<AccordionGroup>
  <Accordion title="数据集市场中有哪些可用的数据集？">
    以下是数据集市场中可立即下载的数据集部分列表：

    **热门数据集**

    * 亚马逊产品
    * Crunchbase 公司信息
    * Facebook — 按群组 URL 抓取的帖子
    * Github 代码仓库
    * Glassdoor 公司概览信息
    * LinkedIn 公司信息
    * LinkedIn 个人资料
    * LinkedIn 帖子
    * 路透新闻
    * Zillow 房产列表信息

    数据集按类别划分。以下是主要类别及部分示例数据集：

    **电商数据（eCommerce Data）**

    * amazon.com、amazon.co.uk、amazon.de、amazon.es、amazon.fr、amazon.in、amazon.it
    * homedepot.com、homedepot.ca
    * lazada.com.my、lazada.sg、lazada.vn

    **房地产数据（Real Estate Data）**

    此类数据集包含住房数据、房地产价格、租金价格等信息。

    * Bayut 阿联酋房产列表
    * Booking.com 房产列表
    * Dubizzle 阿联酋房产列表
    * PropertyFinder 房产列表
    * 美国消费者房产数据
    * ZoomProperty 阿联酋房产列表
    * infocasas.com.uy
    * inmuebles24.com
    * metrocuadrado.com
    * otodom.pl
    * properati.com.co
    * realestate.com.au
    * toctoc.com
    * zillow\.com
    * zonaprop.com.ar
    * zoopla.co.uk

    **社交媒体数据（Social Media Data）**

    * facebook.com
    * instagram.com
    * linkedin.com
    * pinterest.com
    * reddit.com
    * tiktok.com
    * unashamedcataddicts.quora.com
    * vimeo.com
    * x.com
    * youtube.com

    **旅行数据（Travel Data）**

    * Booking.com 酒店房价及可用性
    * Deliveroo 餐厅列表
    * OpenTable 餐厅列表
    * 短租入住率与价格数据集
    * Talabat 餐厅列表
    * Tripadvisor 餐厅列表
    * Zomato 阿联酋餐厅列表
    * airbnb.com

    **B2B 数据**

    * 商业联系人数据集
    * 企业工商信息（Firmographics）
    * 商业情报数据集
    * 商业位置（POI）数据集
    * 公司层级结构数据集
    * 在线意图数据
    * 政治敏感人物名单（PEP）
    * 技术安装量数据源
    * 美国 B2B 员工数据
    * 美国消费者人口统计数据
    * crunchbase.com
    * g2.com
    * glassdoor.com
    * google.com
    * indeed.com
    * linkedin.com
    * manta.com
    * owler.com
    * slintel.com
    * stackoverflow\.com
    * trustpilot.com
    * ventureradar.com
    * xing.com
    * yelp.com

    数据集市场会持续更新新的数据集。要查看完整列表，请点击侧边栏中的 “Web Data”，然后在顶部菜单中选择 “Datasets Marketplace”。

    如果你需要的数据源在市场中不存在，可以通过定制数据集（Custom Dataset, CDS）进行请求。
  </Accordion>

  <Accordion title="你们是否提供免费的数据集？">
    是的！你可以下载一些免费的数据集：

    * espn.com — NBA 数据
    * goodreads.com
    * imdb.com
    * worldpopulationreview\.com

    数据集市场会持续更新新的数据集。要查看完整列表，请点击侧边栏中的 “Web Data”，然后在顶部菜单中选择 “Datasets Marketplace”。
  </Accordion>

  <Accordion title="为什么市场中的时间戳与交付日期不同？">
    计划任务的运行方式是为了确保按时交付。

    交付截止时间是根据之前的采集周期和预估的刷新时长计算得出的。

    因此，为了保证数据按时交付，采集过程可能会在交付日期之前开始。
  </Accordion>

  <Accordion title="我如何查看已准备好的数据快照？">
    你可以在 “My datasets” 标签下找到你的数据快照。在那里，你会看到一个表格，其中包含每个快照的信息，包括其状态：ready、failed 或 in building。
  </Accordion>

  <Accordion title="我应该如何使用 Snapshot ID？">
    Snapshot ID 是分配给特定数据快照的唯一标识符，格式为 “snap\_XXXXXX”。

    当某个数据快照出现问题时，你应该使用 Snapshot ID。将此 ID 包含在支持工单中，可以帮助支持团队快速定位具体的快照，从而更快解决问题。

    Snapshot ID 确保你和支持团队所指的是同一个数据集，减少沟通中的混淆并避免处理延误。
  </Accordion>
</AccordionGroup>

<AccordionGroup>
  <Accordion title="如何设置记录数量上限？">
    你可以通过两种方式设置记录上限：

    **使用控制面板：** 在购买数据集之前，点击 “Proceed to purchase”。在 “Choose delivery frequency” 页面中，选择 “Too pricey? Limit dataset records” 选项，然后指定你想要的记录上限。

    **通过 Filter API：** 添加一个参数来限制 API 返回的记录数量。参考文档见：\
    [Dataset Filter API - records\_limit](/cn/api-reference/marketplace-dataset-api/filter-dataset#body-records-limit)。
  </Accordion>

  <Accordion title="Dataset（Filter）API 是否有承诺费用？">
    目前，使用 Dataset Filter API **不需要每月承诺消费，也没有最低 \$250 的订单要求**。你只需根据实际消耗的记录数量付费。
  </Accordion>

  <Accordion title="我运行了一个过滤请求，还没购买数据就被收费了，这是为什么？">
    当你提交一个 dataset filter API 请求时，系统会使用计算资源来查找符合筛选条件的记录。\
    如果找到匹配的记录，你将根据匹配到的记录数量收费。\
    但如果没有匹配记录，则不会收费。

    如果你想在探索筛选条件时避免产生费用，可以在控制面板的数据集预览表中测试过滤器，该功能每天提供 **最多 10 次免费过滤**。
  </Accordion>

  <Accordion title="为什么有些字段无法完全填写？">
    某些字段的填充率较低，可能是因为公开可获取的数据源存在限制或缺口。\
    填充率会根据数据集类型和来源质量而有所不同，因此某些属性可能只具备部分数据。\
    我们为每个数据集提供详细的填充率和统计信息，帮助你在购买之前评估数据完整度。
  </Accordion>

  <Accordion title="我需要数据集">
    Bright Data 提供多种服务来访问和管理数据集：

    1. **Dataset Marketplace**：\
       这是一个集中平台，你可以在其中发现、定制并购买来自 250 多个领域的高质量数据集。你可以浏览预构建的数据集、查看数据样本并应用高级过滤器。\
       [点击这里浏览 Dataset Marketplace](https://www.bright.cn/datasets/marketplace/browse)。

    2. **Dataset APIs**：\
       使用这些 API，你可以请求、启动并管理数据采集任务。你可以定义新数据集采集的参数、查看请求状态，并使用快照 ID 下载数据集。\
       [在此了解 Dataset APIs](https://www.bright.cn/api-reference/marketplace-dataset-api/request-a-collection)。

    3. **Deep Lookup**：\
       该服务提供一种更细粒度、更高效的方式来请求和管理数据采集，使数据集生成更符合你的特定需求。\
       [点击查看 Deep Lookup](/cn/datasets/deep-lookup/overview)。

    你需要我为这些服务中的某一个做更详细的说明吗？
  </Accordion>
</AccordionGroup>

<AccordionGroup>
  <Accordion title="“LinkedIn People Profiles” 数据集是否包含电子邮件地址或电话号码？">
    * 默认情况下，标准的 LinkedIn 个人资料记录**不包含**电子邮件地址或电话号码，因为这些信息在 LinkedIn 上并非公开可获取。
    * 不过，Bright Data 提供与 RevenueBase 合作的**增强型商业联系人**解决方案，可为许多 LinkedIn 人物档案添加商业邮箱和电话号码——完全符合 GDPR，通过第三方验证来源。
    * 联系方式的覆盖范围可能因个人资料和使用场景而异。
  </Accordion>

  <Accordion title="如何请求带有邮箱和电话的增强记录？">
    * 在 Dataset Marketplace 中选择 “LinkedIn People Profiles” 后，点击数据样本视图右侧的 **Contact filters（联系人过滤器）** 按钮来选择你的联系人数据选项：
      * **标准 LinkedIn 资料数据：** 无联系信息。
      * **增强的商业联系信息：** 选择 “Standard Profiles + Enriched with Business Contact Info”（标准档案 + 增强商业联系方式）或 “Only Profiles with Business Contact Info”（仅限包含商业联系方式的档案）可获得可用的商业邮箱和电话号码（由 RevenueBase 提供并符合 GDPR/合规要求）。
    * 点击 “Apply filter” 来预览并购买带有增强联系信息的数据集。
  </Accordion>

  <Accordion title="增强数据是否符合 GDPR？">
    是的。所有提供的商业联系信息均通过授权合作方（如 RevenueBase）按照 GDPR 和其他合规要求进行获取与处理。
  </Accordion>

  <Accordion title="我可以使用 Deep Lookup 获取联系信息吗？">
    可以。Bright Data 的 [Deep Lookup](https://www.bright.cn/cp/deep-lookup) 能搜索人物并返回可用的商业联系数据（邮箱/电话），前提是数据来源合法且符合合规要求。\
    你可以在查询中指定实体及所需字段（例如 email、phone）。
  </Accordion>

  <Accordion title="购买前如何查看包含哪些字段？">
    * 打开控制面板 → Dataset Marketplace → LinkedIn People Profiles。
    * 点击 “Preview sample” 查看所有可用字段。
    * 对于增强型数据集，可使用上述 **Contact filters** 面板，并在下单前预览示例行。
  </Accordion>

  <Accordion title="如果我有合规或使用方面的问题怎么办？">
    如需了解合规要求、允许的使用方式以及支持的地区，请直接联系你的 Bright Data 客户经理，或通过 [Support](https://www.bright.cn/cp/support) 联系支持团队。

    **总结：**

    * **标准 LinkedIn 资料**不包含邮箱/电话。
    * **增强型商业联系方式**（邮箱/电话）可用：在 Dataset Marketplace 中使用联系人过滤器即可。
    * **Deep Lookup** 是另一种获取联系信息的途径。
    * **购买前务必预览**筛选后的样本，如有定制需求，请联系支持。

    如果你想要在线演示、价格信息或覆盖范围估算，请告诉我！
  </Accordion>
</AccordionGroup>

<AccordionGroup>
  <Accordion title="API 的速率限制是多少？">
    Filter API 的速率限制为每小时 60 次请求。此限制适用于所有 API 调用以及指定时间范围内的快照触发。\
    注意：请合理规划 API 调用，以确保不超出每小时限制。可考虑实现指数退避的重试逻辑以优化性能。
  </Accordion>

  <Accordion title="我可以向 API 过滤器发送的最大值数量是多少？">
    使用列表过滤器或包含过滤器时，单次 API 请求最多可发送 10,000 条输入行。\
    最佳实践：对于大型数据集，建议将请求分批处理，以保持在 10,000 行限制内，同时确保高效处理。
  </Accordion>

  <Accordion title="API 的最大输入文件大小是多少？">
    单次 API 请求的最大输入文件大小为 200 MiB。\
    警告：超过 200 MiB 的文件将被拒绝。请在提交前压缩数据或将大文件拆分为较小块。
  </Accordion>

  <Accordion title="单文件下载的最大快照大小是多少？">
    您可以将快照作为单个文件下载，最大为 5 GB。

    <Tip>
      对于大于 5 GB 的快照，API 将自动提供分块下载选项或流式传输功能，以高效处理数据。
    </Tip>

    ### 快速参考

    | 限制类型   | 数值      | 描述             |
    | :----- | :------ | :------------- |
    | 速率限制   | 60/小时   | 每小时最多 API 调用次数 |
    | 输入行数   | 10,000  | 列表/包含过滤器的最大值数量 |
    | 输入文件大小 | 200 MiB | 上传文件的最大大小      |
    | 快照下载   | 5 GB    | 单文件下载的最大快照大小   |

    <Note>
      **需要更高的限制？**\
      请联系企业团队获取定制的速率限制和容量扩展选项，以满足您的业务需求。
    </Note>
  </Accordion>
</AccordionGroup>

<AccordionGroup>
  <Accordion title="我在哪里获取 Snapshot ID？">
    当您[触发采集](/cn/api-reference/rest-api/scraper/asynchronous-requests)（POST `/datasets/v3/trigger`）、[筛选数据集](/cn/api-reference/marketplace-dataset-api/filter-dataset-with-csv-json-files)（POST `/datasets/filter`）或通过数据集订阅时，都会返回 Snapshot ID。您也可以[列出您的所有快照](/cn/api-reference/marketplace-dataset-api/get-dataset-list)（GET `/datasets/v3/snapshots`）。

    > 更多详情请参阅[交付快照](/cn/api-reference/marketplace-dataset-api/deliver-snapshot)页面。
  </Accordion>

  <Accordion title="响应中的交付任务 ID 该如何使用？">
    响应中的 `id` 是交付任务 ID。使用它调用 GET `/datasets/v3/delivery/{delivery_id}` 来跟踪交付进度，请轮询直到状态为 "done"。

    > 更多详情请参阅[交付快照](/cn/api-reference/marketplace-dataset-api/deliver-snapshot)页面。
  </Accordion>

  <Accordion title="快照是否需要处于特定状态？">
    是的。快照必须处于 `ready` 状态。在调用交付接口前，请使用 GET `/datasets/snapshots/{id}` 进行检查。

    > 可能的状态：`scheduled`、`building`、`ready`、`failed`。
  </Accordion>

  <Accordion title="我可以将同一个快照交付到多个目的地吗？">
    可以。使用相同的 Snapshot ID，以不同的交付配置多次调用该接口即可。
  </Accordion>

  <Accordion title="支持哪些文件格式？">
    json、jsonl 和 csv。
  </Accordion>

  <Accordion title="如何将大型快照拆分为较小的文件？">
    使用 `batch_size` 参数设置每个文件的记录数。每个文件（批次）必须低于 5GB 硬性上限。用 5GB 除以您的平均记录大小来估算 `batch_size`，然后从较低的值开始，并根据实际获得的文件大小进行调整。

    例如，如果您的平均记录约为 5KB，则 `batch_size` 为 1,000,000 时文件恰好接近 5GB 上限。建议从 500,000 条记录（约 2.5GB）开始，以确保安全低于上限，然后根据收到的文件大小调高或调低 `batch_size`。
  </Accordion>

  <Accordion title="为什么我的请求返回 400 错误？">
    最常见的原因是您的 `batch_size` 生成的文件超过 5GB。例如，如果您的平均记录大小约为 5KB，则 `batch_size` 为 1,000,000 会生成约 5GB 的文件，可能超出限制。请调低 `batch_size`（例如调至 100,000）后重试。
  </Accordion>

  <Accordion title="我可以压缩输出吗？">
    可以。设置 `compress: true` 即可接收 gzip 压缩文件。
  </Accordion>

  <Accordion title="每个批次的最大文件大小是多少？">
    5GB。这是每个交付文件的硬性上限。使用 `batch_size` 控制每个文件包含的记录数，确保每个文件都低于此阈值。
  </Accordion>
</AccordionGroup>
