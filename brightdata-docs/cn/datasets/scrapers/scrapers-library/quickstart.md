> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Scrapers - 快速上手

<Steps>
  <Step title="前置条件" stepNumber="0">
    * 一个 Bright Data 账户（注册 → 2 分钟）
    * 一个有效的 API Key（[如何获取 API Key](/cn/api-reference/authentication)）
  </Step>

  <Step title="选择目标网站" stepNumber="1">
    1. 访问 [Scraper Library](https://www.bright.cn/cp/scrapers/browse)
    2. 浏览列表并点击所需网站。
    3. 找不到？查看 [Custom Scrapers](/cn/datasets/scrapers/custom-scrapers/scrape-any-web) 或 [Web Scraper IDE](/cn/datasets/scraper-studio/introduction) 产品，获取定制化解决方案！
  </Step>

  <Step title="选择 Scraper 端点" stepNumber="2">
    在网站页面中，您会看到多个 Scraper 端点，例如：

    * LinkedIn
      * Profile by URL – 提供个人资料 URL，获取公开数据字段。
      * Profiles by Keyword – 提供搜索词，获取匹配的个人资料 URL（可选完整数据）。
      * Company Jobs – 收集公司页面的职位发布信息。
    * Amazon
      * 按 ASIN 获取产品、搜索结果、评论、“常一起购买”等。

    选择返回所需信息的端点，然后点击打开 API 请求生成器。

    <Frame>
      <img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/datasets/scrapers/scraping-library/quickstart/collect-by-url.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=2d4cd92cc6ade8b76a6265f20990dc37" alt="collect-by-url" width="1507" height="1229" data-path="images/datasets/scrapers/scraping-library/quickstart/collect-by-url.png" />
    </Frame>
  </Step>

  <Step title="构建请求" stepNumber="3">
    中央面板现在显示表单，从上到下依次填写：

    **A. 输入**

    * "单个输入": 直接在文本框粘贴 URL/关键字。
    * “批量 CSV”: 上传符合 Scraper 输入参数的 CSV 文件。

    **B. Scraper 设置（可选）**

    1. 输出模式 – 勾选仅需要的数据字段（节省带宽和存储）。
    2. 外部存储 – 填写 S3 / GCS / Azure 等凭据，结果文件将自动存储到指定位置。
    3. Webhook URL – 作业完成后，我们会 POST JSON 到您的端点，非常适合实时数据管道。
  </Step>

  <Step title="选择运行模式: /scrape vs /trigger" stepNumber="4">
    代码片段面板（右侧）会根据配置实时更新。运行请求时可选择以下两个端点：

    | 模式 | 路径                                                                | 行为                                                                      | 适用场景           |
    | :- | :---------------------------------------------------------------- | :---------------------------------------------------------------------- | :------------- |
    | 同步 | [/scrape](/cn/api-reference/scrapers/synchronous-requests)        | 实时返回 API 调用结果。该端点有 1 分钟超时，如果超时会自动切换为异步。                                 | 快速、小型作业，实时获取结果 |
    | 异步 | [/trigger](/cn/api-reference/rest-api/scraper/trigger-collection) | 立即返回 snapshot\_id；可轮询 `/snapshots/{id}` 或在 `logs/webhook/storage` 等待结果。 | 生产环境和大型作业      |
  </Step>

  <Step title="复制代码" stepNumber="5">
    * 语言选择器 – 使用代码块下拉选择偏好的编程语言。
    * 代码片段已包含：端点 URL、API key 头、payload JSON（输入 + 选项）。
    * 将其粘贴到终端 / IDE / serverless 函数中运行。
  </Step>

  <Step title="监控与获取结果" stepNumber="6">
    1. Scraper 页面 → Logs 标签页

    <Frame>
      <img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/datasets/scrapers/scraping-library/quickstart/logs-tab.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=3f687a1bcb539d254bdc0339aaab581c" alt="logs-tab" width="624" height="191" data-path="images/datasets/scrapers/scraping-library/quickstart/logs-tab.png" />
    </Frame>

    * 实时状态（运行中、准备好、失败）。
    * 一键下载 JSON/CSV 等文件。

    2. Webhook（如已设置）
       * 您的服务器会接收到 `{snapshot_id, status, result_url}` payload。
    3. 外部存储
       * 结果文件会出现在您配置的存储桶路径中。
    4. [快照管理 API](/cn/api-reference/scrapers/management-apis/monitor-progress)
       * 使用这些端点监控快照进度。
  </Step>
</Steps>

🎉 现在您已经可以大规模抓取数据了 — 祝收集愉快！
