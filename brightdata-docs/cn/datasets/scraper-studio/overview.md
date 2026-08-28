> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Scraper Studio

> 使用 Bright Data Scraper Studio 构建自定义网页爬虫：AI Agent、JavaScript IDE 或 CLI，运行在 Bright Data 的代理与解封基础设施之上。

<Note>
  [立即开始](https://www.bright.cn/?hs_signup=1\&utm_source=docs)，每月赠送 **5,000 个免费信用额度**，无需信用卡。参见[免费套餐](/cn/general/account/billing-and-pricing/free-tier)。

  我们还将匹配您的**首次账户充值金额，最高可达 \$500**。
</Note>

<div className="bd-landing">
  <div className="bd-page">
    <div className="bd-hero">
      <div className="bd-hero-copy">
        <span className="bd-eyebrow">Scraper Studio</span>

        <h1 className="bd-headline">为任意网站构建自定义爬虫</h1>

        <p className="bd-subhead">
          目标网站没有现成的爬虫？描述您想要的数据，即可在 Bright Data 的代理与解封基础设施上构建一个。无需管理服务器、代理轮换或重试逻辑。
        </p>

        <div className="bd-cta-row">
          <a className="bd-cta-primary" href="/cn/datasets/scraper-studio/quickstart">开始构建</a>
        </div>
      </div>

      <div className="bd-hero-image">
        <img src="https://media.brightdata.com/2025/02/scraper_studio_hero_animated.svg" alt="Bright Data Scraper Studio 主视觉插图" />
      </div>
    </div>

    <div className="bd-callout">
      <span className="bd-callout-icon">💡</span>
      <span>不想写代码？用自然语言描述您的目标，让 <a href="/cn/datasets/scraper-studio/ai-agent">AI Agent</a> 直接从您的控制台生成爬虫。</span>
    </div>

    ## 在终端中创建爬虫

    安装 Bright Data CLI，登录后传入一个目标 URL 和一句描述所需数据的话。Bright Data 的 AI Agent 会生成输出 schema、编写爬虫代码并返回一个 Collector ID。

    ```bash theme={null}
    npm install -g @brightdata/cli
    bdata login
    bdata scraper create https://news.ycombinator.com \
      "Extract top stories: title, url, points, author, comment count"
    ```

    同一个爬虫可以在 AI Agent 或 IDE 中打开编辑，并能在 Claude Code、Cursor 或 Codex 等任意编码代理的内置终端中原样运行。完整演练参见 [使用 Bright Data CLI 构建爬虫](/cn/datasets/scraper-studio/build-with-the-cli)。

    ## 选择哪种构建方式

    <CardGroup cols={3}>
      <Card title="AI Agent" icon="robot" href="/cn/datasets/scraper-studio/ai-agent">
        用自然语言描述数据。Bright Data AI 会生成 schema 并编写爬虫代码。无需写代码，最快得到可用爬虫。
      </Card>

      <Card title="IDE" icon="code" href="/cn/datasets/scraper-studio/scraper-studio-ide-interface">
        在基于浏览器的编辑器中编写和调试 JavaScript。对交互与解析逻辑拥有完全控制权。
      </Card>

      <Card title="Bright Data CLI" icon="terminal" href="/cn/datasets/scraper-studio/build-with-the-cli">
        从终端或任意编码代理创建、运行和自愈爬虫。**新功能。**
      </Card>
    </CardGroup>

    无论以何种方式构建，每个爬虫都产生相同的输出。在 AI Agent 中创建的爬虫随时可以在 IDE 中打开和编辑，因此您不会被锁定在某一种方式上。

    ## 工作原理

    每个 Bright Data Scraper Studio 爬虫都执行两项核心操作，并在目标网站发生变化时保持自身持续运行。

    <CardGroup cols={3}>
      <Card title="交互" icon="arrow-pointer">
        导航到目标 URL，处理分页，点击元素或发送 HTTP 请求。
      </Card>

      <Card title="解析" icon="brackets-curly">
        读取页面 HTML，并将结构化字段提取到预定义的 schema 中：JSON、CSV、NDJSON 或 XLSX。
      </Card>

      <Card title="自愈" icon="wand-magic-sparkles" href="/cn/datasets/scraper-studio/self-healing-tool">
        当网站布局变化导致爬虫失效时，用一段自然语言提示词更新它，而无需重写选择器。
      </Card>
    </CardGroup>

    <iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/YJFytWtplv0" title="Scrape ANY website - Scraper Studio by Bright Data" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

    ## 何时使用 Scraper Studio

    当您需要的数据不在 [爬虫库](https://brightdata.com/cp/scrapers/browse) 中、希望拥有爬虫逻辑的所有权，并且不想自行管理代理或基础设施时，就使用 Bright Data Scraper Studio。完整对比以及 AI Agent 与 IDE 的取舍，参见 [了解 Scraper Studio](/cn/datasets/scraper-studio/introduction)。

    <CardGroup cols={3}>
      <Card title="现成爬虫" icon="layer-group" href="/cn/datasets/scrapers/overview">
        需要零配置的热门网站？请改用 Web Scraper API 库中的 1000+ 现成爬虫。
      </Card>

      <Card title="托管服务" icon="screwdriver-wrench" href="/cn/datasets/scrapers/managed-services">
        希望由我们为您构建并运营爬虫？Bright Data 团队为您的目标构建自定义爬虫。**无需写代码。**
      </Card>

      <Card title="数据集市场" icon="store" href="/cn/datasets/marketplace">
        完全跳过抓取。购买按计划刷新的现成数据集。**无需写代码。**
      </Card>
    </CardGroup>

    ## 您可以构建什么

    <CardGroup cols={3}>
      <Card title="小众网站抓取" icon="globe" href="/cn/datasets/scraper-studio/quickstart">
        从任意没有现成爬虫的网站提取结构化数据，从区域性市场到行业目录皆可。
      </Card>

      <Card title="价格监控" icon="tag" href="/cn/datasets/scraper-studio/ai-agent">
        在标准爬虫库未覆盖的网站上跟踪价格、库存和商品列表。
      </Card>

      <Card title="AI 与 RAG 数据摄取" icon="robot" href="/cn/datasets/scraper-studio/build-with-the-cli">
        将目标页面转换为干净的 JSON 或 NDJSON，供模型训练和检索管道使用。
      </Card>

      <Card title="销售线索生成" icon="user-magnifying-glass" href="/cn/datasets/scraper-studio/ai-agent">
        从目录和列表中提取联系人与公司数据，导入您的销售管道。
      </Card>

      <Card title="内容聚合" icon="newspaper" href="/cn/datasets/scraper-studio/develop-a-scraper">
        从多个来源收集文章、列表或评论，汇聚成一个结构化数据源。
      </Card>

      <Card title="市场研究" icon="chart-line" href="/cn/datasets/scraper-studio/complete-examples">
        从频繁变化的网站聚合竞品动态、目录数据和趋势。
      </Card>
    </CardGroup>

    ## 进一步了解

    <CardGroup cols={4}>
      <Card title="开始使用" icon="rocket">
        [快速开始](/cn/datasets/scraper-studio/quickstart)

        [使用 AI Agent 构建](/cn/datasets/scraper-studio/ai-agent)

        [使用 CLI 构建](/cn/datasets/scraper-studio/build-with-the-cli)
      </Card>

      <Card title="IDE" icon="code">
        [IDE 界面](/cn/datasets/scraper-studio/scraper-studio-ide-interface)

        [开发爬虫](/cn/datasets/scraper-studio/develop-a-scraper)

        [Functions 参考](/cn/datasets/scraper-studio/functions)
      </Card>

      <Card title="运维" icon="gauge-high">
        [规格说明](/cn/datasets/scraper-studio/specifications)

        [交付选项](/cn/datasets/scraper-studio/initiate-collection-and-delivery-options)

        [最佳实践](/cn/datasets/scraper-studio/best-practices)
      </Card>

      <Card title="API 基础" icon="code-branch">
        [Scraper Studio API](/cn/api-reference/scraper-studio-api/Trigger_a_scraper_for_batch_collection_method)

        [Worker 类型](/cn/datasets/scraper-studio/worker-types)

        [常见问题](/cn/datasets/scraper-studio/faqs)
      </Card>
    </CardGroup>
  </div>
</div>
