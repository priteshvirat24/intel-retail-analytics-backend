> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 爬虫

> 使用 Bright Data 爬虫从任意网站提取结构化数据。

<Note>
  [立即开始](https://www.bright.cn/?hs_signup=1\&utm_source=docs)，每月赠送 **5,000 个免费信用额度**，无需信用卡。参见[免费套餐](/cn/general/account/billing-and-pricing/free-tier)。

  我们还将匹配您的**首次账户充值金额，最高可达 \$500**。
</Note>

<div className="bd-landing">
  <div className="bd-page">
    <div className="bd-hero">
      <div className="bd-hero-copy">
        <span className="bd-eyebrow">爬虫</span>

        <h1 className="bd-headline">来自任意网站的结构化数据</h1>

        <p className="bd-subhead">
          发送一个 URL，获得结构化 JSON/CSV。无需管理代理、浏览器、反爬虫系统或数据解析。1000+ 个预构建爬虫覆盖 LinkedIn、Instagram、TikTok、Amazon、Google 地图等。
        </p>

        <div className="bd-cta-row">
          <a className="bd-cta-primary" href="/cn/datasets/scrapers/linkedin/quickstart">开始构建</a>
        </div>
      </div>

      <div className="bd-hero-image">
        <img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/datasets/scrapers/hero.svg?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=716425fd45445e4a2544f2d79225a095" alt="Bright Data Web Scraper API 概览插图" width="548" height="500" data-path="images/datasets/scrapers/hero.svg" />
      </div>
    </div>

    <div className="bd-callout">
      <span className="bd-callout-icon">💡</span>
      <span>还没准备好完整集成？直接在 <a href="https://www.bright.cn/cp/scrapers/browse">无代码控制台</a> 中运行任意爬虫。</span>
    </div>

    ## 发送你的第一个请求

    将 `API_KEY` 替换为来自 [账户设置](https://www.bright.cn/cp/setting/users) 的密钥。你将收到一条包含 200+ 字段的 JSON 记录。同样的请求模式适用于库中的每个爬虫。

    <CodeGroup>
      ```bash cURL theme={null}
      curl "https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_l1viktl72bvl7bjuj0&format=json" \
        -H "Authorization: Bearer API_KEY" \
        -H "Content-Type: application/json" \
        -d '[{"url": "https://www.linkedin.com/in/elad-moshe-05a90413/"}]'
      ```

      ```python Python theme={null}
      import requests

      url = "https://api.brightdata.com/datasets/v3/scrape"
      headers = {
          "Authorization": "Bearer API_KEY",
          "Content-Type": "application/json",
      }
      params = {"dataset_id": "gd_l1viktl72bvl7bjuj0", "format": "json"}
      payload = [{"url": "https://www.linkedin.com/in/elad-moshe-05a90413/"}]

      response = requests.post(url, headers=headers, params=params, json=payload)
      print(response.json())
      ```

      ```javascript Node.js theme={null}
      const response = await fetch(
        "https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_l1viktl72bvl7bjuj0&format=json",
        {
          method: "POST",
          headers: {
            "Authorization": "Bearer API_KEY",
            "Content-Type": "application/json",
          },
          body: JSON.stringify([
            { url: "https://www.linkedin.com/in/elad-moshe-05a90413/" },
          ]),
        }
      );

      const data = await response.json();
      console.log(data);
      ```
    </CodeGroup>

    ## 热门爬虫

    <div className="bd-group-label">
      <span className="bd-pill">最受欢迎</span>
    </div>

    <CardGroup cols={4}>
      <Card title="LinkedIn" icon="linkedin" href="/cn/datasets/scrapers/linkedin/quickstart">
        个人资料、公司、职位、帖子。
      </Card>

      <Card title="Instagram" icon="instagram" href="/cn/datasets/scrapers/instagram/quickstart">
        个人资料、帖子、Reels、评论。
      </Card>

      <Card title="TikTok" icon="tiktok" href="/cn/datasets/scrapers/tiktok/quickstart">
        个人资料、帖子、评论、店铺。
      </Card>

      <Card title="Amazon" icon="amazon" href="/cn/datasets/scrapers/amazon/quickstart">
        产品、评论、卖家、搜索。
      </Card>
    </CardGroup>

    <h3 className="bd-group-heading">社交</h3>

    <CardGroup cols={4}>
      <Card title="Facebook" icon="facebook" href="/cn/datasets/scrapers/facebook/quickstart">
        主页、帖子、活动。
      </Card>

      <Card title="X / Twitter" icon="x-twitter" href="/cn/datasets/scrapers/twitter/quickstart">
        个人资料和帖子。
      </Card>

      <Card title="YouTube" icon="youtube" href="/cn/datasets/scrapers/youtube/quickstart">
        频道、视频、评论。
      </Card>

      <Card title="Reddit" icon="reddit" href="/cn/datasets/scrapers/reddit/introduction">
        子版块、帖子、评论。
      </Card>
    </CardGroup>

    <h3 className="bd-group-heading">AI 与搜索</h3>

    <CardGroup cols={3}>
      <Card title="ChatGPT" icon="comments" href="/cn/datasets/scrapers/chatgpt/quickstart">
        对话和提示。
      </Card>

      <Card title="Google 搜索" icon="magnifying-glass" href="/cn/datasets/scrapers/scrapers-library/overview">
        SERP、摘要、精选结果。
      </Card>

      <Card title="Google 地图" icon="location-dot" href="/cn/datasets/scrapers/scrapers-library/overview">
        地点、评论、营业时间。
      </Card>
    </CardGroup>

    <a className="bd-browse-all" href="https://www.bright.cn/cp/scrapers/browse">浏览全部 1000+ 个爬虫 →</a>

    <div className="bd-callout">
      <span className="bd-callout-icon">🛠️</span>
      <span>找不到你需要的站点？使用 AI 驱动的 <a href="/cn/datasets/scraper-studio/introduction">Scraper Studio</a> 在几分钟内构建自定义爬虫。</span>
    </div>

    ## 工作方式

    先选择请求模式，再选择数据交付方式。

    ### 请求模式

    <CardGroup cols={3}>
      <Card title="同步" icon="bolt" href="/cn/datasets/scrapers/concepts/sync-vs-async">
        一次请求，一次响应。适合单 URL 和实时场景。
      </Card>

      <Card title="异步" icon="layer-group" href="/cn/datasets/scrapers/linkedin/async-requests">
        触发任务后再获取结果。单次请求可处理数千个 URL。
      </Card>

      <Card title="发现" icon="magnifying-glass" href="/cn/datasets/scrapers/scrapers-library/working-with-sources">
        在没有具体 URL 时，通过关键字或类别查找记录。
      </Card>
    </CardGroup>

    ### 交付选项

    <CardGroup cols={4}>
      <Card title="API 下载" icon="download" href="/api-reference/scrapers/delivery-apis/download-snapshot">
        任务完成后从 API 拉取结果。
      </Card>

      <Card title="Webhook" icon="webhook" href="/cn/datasets/scrapers/linkedin/data-delivery/webhooks">
        快照就绪后立即推送到你的端点。
      </Card>

      <Card title="云存储" icon="cloud" href="/cn/datasets/scrapers/linkedin/data-delivery/amazon-s3">
        直接交付到 S3、GCS、Azure 或 Snowflake。
      </Card>

      <Card title="流式传输" icon="stream" href="/cn/datasets/scrapers/scrapers-library/stream-and-file-delivery">
        抓取过程中分批接收结果。
      </Card>
    </CardGroup>

    ## 预构建爬虫之外

    <CardGroup cols={3}>
      <Card title="自定义爬虫" icon="code" href="/cn/datasets/scraper-studio/introduction">
        使用 Scraper Studio 为任意站点构建爬虫。传入 URL 并描述你需要的数据。
      </Card>

      <Card title="托管服务" icon="screwdriver-wrench" href="/cn/datasets/scrapers/managed-services">
        Bright Data 团队为你的目标站点构建并运营自定义爬虫。**无需代码。**
      </Card>

      <Card title="数据集市场" icon="store" href="/cn/datasets/marketplace">
        完全跳过抓取。购买按计划刷新的现成数据集。**无需代码。**
      </Card>
    </CardGroup>

    ## 示例工作流

    端到端教程，将爬虫与交付选项和目标系统结合起来。

    <CardGroup cols={3}>
      <Card title="LinkedIn 资料 → 你的 CRM" icon="user-magnifying-glass" href="/cn/datasets/scrapers/linkedin/quickstart">
        使用 LinkedIn 爬虫获取个人资料和公司数据，再通过 Webhook 推送到 HubSpot 或 Salesforce。
      </Card>

      <Card title="Amazon 价格监控" icon="tag" href="/cn/datasets/scrapers/amazon/quickstart">
        对 SKU 列表运行异步任务，将结果流式写入 S3，实现每日价格和库存跟踪。
      </Card>

      <Card title="社交监听" icon="bell" href="/cn/datasets/scrapers/instagram/quickstart">
        结合 Instagram、TikTok 和 X 爬虫与"发现"模式，按关键字跟踪提及。
      </Card>
    </CardGroup>

    ## 你能构建什么

    <CardGroup cols={3}>
      <Card title="销售线索富化" icon="user-magnifying-glass" href="/cn/datasets/scrapers/linkedin/quickstart">
        将 LinkedIn 个人资料和公司数据导入你的 CRM 或销售流程。
      </Card>

      <Card title="价格监控" icon="tag" href="/cn/datasets/scrapers/amazon/quickstart">
        跨电商站点跟踪产品价格、库存和评论。
      </Card>

      <Card title="市场研究" icon="chart-line" href="/cn/datasets/scrapers/instagram/quickstart">
        汇总社交信号、竞争对手活动和热门内容。
      </Card>

      <Card title="AI 训练数据" icon="robot" href="/cn/datasets/scrapers/concepts/web-scraper-api-vs-diy">
        构建大规模、结构化的数据集用于训练和微调模型。
      </Card>

      <Card title="职位聚合" icon="briefcase" href="/cn/datasets/scrapers/linkedin/quickstart">
        将 LinkedIn 等求职网站的职位列表汇总到单一信息流。
      </Card>

      <Card title="品牌监控" icon="bell" href="/cn/datasets/scrapers/twitter/quickstart">
        跨社交平台跟踪提及、话题标签和情感。
      </Card>
    </CardGroup>

    ## 更多资源

    <CardGroup cols={4}>
      <Card title="概念" icon="lightbulb">
        [同步 vs 异步](/cn/datasets/scrapers/concepts/sync-vs-async)

        [Web Scraper API vs DIY](/cn/datasets/scrapers/concepts/web-scraper-api-vs-diy)
      </Card>

      <Card title="库参考" icon="book">
        [库概览](/cn/datasets/scrapers/scrapers-library/overview)

        [自定义输入](/cn/datasets/scrapers/scrapers-library/custom-inputs)

        [使用源](/cn/datasets/scrapers/scrapers-library/working-with-sources)
      </Card>

      <Card title="API 基础" icon="code-branch">
        [API 参考](/cn/api-reference/rest-api/scraper/asynchronous-requests)

        [错误目录](/cn/datasets/scrapers/scrapers-library/error-list-by-endpoint)

        [常见问题](/cn/datasets/scrapers/scrapers-library/faqs)
      </Card>

      <Card title="运维" icon="gauge-high">
        [交付选项](/cn/datasets/scrapers/scrapers-library/delivery-options)

        [流式与文件交付](/cn/datasets/scrapers/scrapers-library/stream-and-file-delivery)

        [截止时间功能](/cn/datasets/scrapers/scrapers-library/deadline-feature)
      </Card>
    </CardGroup>
  </div>
</div>
