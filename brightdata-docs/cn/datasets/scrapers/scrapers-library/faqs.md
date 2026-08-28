> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Scrapers 常见问题解答

> 查找有关 Bright Data Scrapers 的常见问题解答，包括设置、身份验证、数据格式、定价以及大规模数据提取。

<AccordionGroup>
  <Accordion title="什么是 Scrapers？">
    Scrapers 允许用户使用预构建的爬虫按需提取最新网站数据。它可用于自动化数据收集并与其他系统集成。
  </Accordion>

  <Accordion title="谁可以从使用 Scrapers 中受益？">
    数据分析师、科学家、工程师和开发人员，或寻求高效收集和分析 Web 数据的方法（用于 AI、ML、大数据应用等，无需开发爬虫）的人，将会发现 Scraper API 特别有用。
  </Accordion>

  <Accordion title="我如何开始使用 Scrapers？">
    使用 Scraper API 非常简单，一旦您开通 Bright Data 账户，您需要从账户设置中[生成 API 密钥](/cn/api-reference/authentication#how-do-i-authenticate-with-api-key%3F)。拥有密钥后，您可以参考我们的[API 文档](/cn/datasets/scrapers/scrapers-library/overview) 获取如何发起首次 API 调用的详细说明。

    <iframe width="640" height="480" src="https://app.arcade.software/share/BPGoTdRmf89Ip1EQuIOW" title="观看演示视频" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />
  </Accordion>

  <Accordion title="不同爬虫之间有什么区别？">
    每个爬虫可能需要不同的输入。爬虫主要分为两类：

    1. **PDP** \
       这些爬虫需要 URL 作为输入。PDP 爬虫可从网页提取详细的产品信息，如规格、价格和功能
    2. **Discovery/ Discovery+PDP** \
       Discovery 爬虫允许您通过搜索、分类、关键词等方式探索并发现新实体/产品。

    <Frame>
      <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/scraping-automation/scrapers/faqs/delivery-pdp.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=7fac3344d0f8ac7684e4b2e1a0a364a9" alt="delivery-pdp.png" width="1456" height="398" data-path="images/scraping-automation/scrapers/faqs/delivery-pdp.png" />
    </Frame>
  </Accordion>

  <Accordion title="为什么同一域名有不同的 Discovery API？">
    每个 Discovery API 允许您使用不同的方法查找所需数据，可能通过关键词、分类 URL，甚至地理位置。
  </Accordion>

  <Accordion title="我如何使用 Scrapers 进行认证？">
    认证通过 API 密钥完成。在请求的 `Authorization` 头中包含 API 密钥，如下所示：`Authorization: Bearer YOUR_API_KEY`。
  </Accordion>

  <Accordion title="我如何自定义请求并触发它？">
    选择要运行的 API 后，您可以使用我们的[详细 API 参数文档](/cn/api-reference/rest-api/scraper/asynchronous-requests)自定义请求，指定不同类型及预期的输入和响应。
  </Accordion>

  <Accordion title="是否提供免费试用？">
    您将获得 2\$ 额度来探索和测试我们的服务。
  </Accordion>

  <Accordion title="我如何测试 API？">
    您可以通过在控制面板上自定义代码快速测试产品（[演示视频](https://app.arcade.software/flows/BPGoTdRmf89Ip1EQuIOW/view)）

    <Steps>
      <Step title="从多种 API 中选择所需的 API" />

      <Step title="输入您的参数">
        <Frame>
          <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/scraping-automation/scrapers/faqs/trigger-a-collection.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=b8e9ff22fea2f39a9936177a8d96cc11" alt="trigger-a-collection.png" width="1122" height="804" data-path="images/scraping-automation/scrapers/faqs/trigger-a-collection.png" />
        </Frame>
      </Step>

      <Step title="输入您的 API 密钥">
        <Frame>
          <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/scraping-automation/scrapers/faqs/enter-api-token.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=e7f11d9d1c1ef44e2e30dd8314fa0e56" alt="enter-api-token.png" width="834" height="138" data-path="images/scraping-automation/scrapers/faqs/enter-api-token.png" />
        </Frame>
      </Step>

      <Step title="选择首选的交付方式">
        <Frame>
          <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/scraping-automation/scrapers/faqs/delivery-method.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=6250a3a6aee2d2328406ab309c35a520" alt="delivery-method.png" width="1306" height="582" data-path="images/scraping-automation/scrapers/faqs/delivery-method.png" />
        </Frame>

        使用 webhook - 更新 webhook URL 并复制“触发数据收集”代码，在客户端运行。

        使用 API - 根据所选特定设置（`S3`、`GCP`、`pubsub` 等）填写所需凭证和信息，收集结束后复制并运行代码
      </Step>

      <Step title="复制代码并在客户端运行">
        <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/scraping-automation/scrapers/faqs/code.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=62d7f95c64499d9fdaad46eb8b7a69f2" alt="code.png" width="1056" height="478" data-path="images/scraping-automation/scrapers/faqs/code.png" />

        上述操作也可通过免费工具完成，例如 [Webhook-site](https://webhook.site/) 和 [Postman](https://web.postman.co/)

        我们还提供额外的管理 API，可获取收集状态信息，并在 **Management APIs** 标签下获取所有快照列表
      </Step>
    </Steps>
  </Accordion>

  <Accordion title="Scrapers 支持哪些数据格式？">
    Scrapers 支持多种数据格式提取，包括 `JSON`、`NDJSON`、`JSONL` 和 `CSV`。请在请求参数中指定所需格式。
  </Accordion>

  <Accordion title="Scrapers 的收费标准是什么？">
    我们按交付的记录数量收费，您只需为实际获取的内容付费。请注意，由用户输入错误导致的失败尝试仍会计费。由于数据未成功获取是用户输入问题，而非系统性能问题，因此仍会消耗资源处理请求。每条记录的费率取决于您的订阅计划（起价 0.7\$ / 1000 条记录）。请查看我们的[定价计划](https://www.bright.cn/pricing/web-scraper)或您的账户详情了解具体费率。
  </Accordion>

  <Accordion title="如果我的 API 密钥过期，我该怎么办？">
    对于账户管理员：如果 API 密钥过期，您需要在账户设置中创建新的密钥。

    <Frame>
      <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/scraping-automation/scrapers/faqs/no-api-token.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=de1643fff3cf459461ee1fa8f4a9773e" alt="no-api-token.png" width="2048" height="184" data-path="images/scraping-automation/scrapers/faqs/no-api-token.png" />
    </Frame>

    对于账户用户：如果 API 密钥过期，请联系账户管理员签发新的 API 密钥。

    <Frame>
      <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/scraping-automation/scrapers/faqs/no-api-token-user.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=7023e6f9f3254895fc2aab4cfb1ef941" alt="no-api-token-user.png" width="2048" height="193" data-path="images/scraping-automation/scrapers/faqs/no-api-token-user.png" />
    </Frame>
  </Accordion>

  <Accordion title="Scraper API 如何管理大规模数据提取任务？">
    通过支持高并发和批处理的能力，Scraper API 在大规模数据提取场景中表现出色。这确保开发者可以高效扩展爬取操作，应对大量请求并保持高吞吐量。
  </Accordion>

  <Accordion title="我如何升级我的订阅计划？">
    要升级订阅计划，请访问仪表盘账户的计费部分并选择所需计划。如需进一步帮助，请联系支持团队。
  </Accordion>

  <Accordion title="Scraper API 针对哪些特定用例进行了优化？">
    Scrapers 支持广泛的用例，包括竞争基准分析、市场趋势分析、动态定价算法、情感提取以及将数据输入机器学习管道。对于电商、金融科技和社交媒体分析至关重要，这些 API 让开发者能够有效实施数据驱动策略。
  </Accordion>

  <Accordion title="Scrapers 的速度有多快？">
    我们为使用 URL 作为输入的爬虫提供实时支持，每次可处理最多 20 个 URL 输入，对于超过 20 个输入则支持批量处理，无论爬虫类型如何。

    Scrapers 每次调用可为最多 20 个输入提供实时数据，响应时间因域名而异，确保获取最新数据而无需依赖缓存信息。

    用于发现新记录的爬虫（例如“按关键词发现”、“按话题发现”）通常耗时更长，并使用批量支持，因为实际响应时间可能受多种因素影响，包括目标 URL 的加载时间和用户定义页面交互的执行时间。每个爬虫的平均响应时间可在对应的 Scraper 页面查看。
  </Accordion>

  <Accordion title="我如何取消 API 调用？">
    您可以使用以下端点取消运行：

    ```sh theme={null}
      curl -H "Authorization: API key" -H "Content-Type: application/json" -k "https://api.brightdata.com/datasets/v3/snapshot/SNAPSHOT_ID/cancel" -X POST
    ```

    确保使用的是您想要取消的快照 ID。

    注意：如果取消运行，将不会向您交付任何数据，并且快照在收集完成后无法取消。
  </Accordion>

  <Accordion title="notify URL 和 webhook URL 配置有什么区别？">
    API 配置中 notify URL 与 webhook URL 的主要区别在于用途和使用方式：

    Notify URL：

    * 通常用于异步通信。
    * 当任务完成或事件发生时，系统会向指定 URL 发送通知。
    * 通知通常比较轻量，不包含详细数据，但可能提供参考或状态以便进一步操作（例如：“作业完成，请检查日志详情”）。

    Webhook URL：

    * 也用于异步通信，但更以数据为中心。
    * 当特定事件发生时，系统会将详细的实时数据推送到指定 URL。
    * Webhook 提供直接可操作的信息，无需客户端轮询系统。

    示例用例：

    * notify URL 可用于通知您爬取任务已完成。
    * webhook URL 可将实际爬取的数据或完成的详细元数据直接发送给您。
  </Accordion>

  <Accordion title="触发收集后，快照可保留多久？">
    快照可保存 30 天，
    在此期间，您可以通过[交付 API](/cn/api-reference/scrapers/delivery-apis/download-snapshot)及快照 ID 获取快照。
  </Accordion>

  <Accordion title="特定爬虫或域名是否有任何限制？">
    这些平台存在一定限制：

    <AccordionGroup>
      <Accordion title="Facebook" icon="facebook">
        |               |   |
        | ------------- | - |
        | 贴文（按个人资料 URL） |   |
        | 评论            |   |
        | Reels         |   |
      </Accordion>

      <Accordion title="Instagram" icon="instagram">
        |               |   |
        | ------------- | - |
        | 贴文（按关键词）      |   |
        | 贴文（按个人资料 URL） |   |
        | 评论            |   |
        | Reels         |   |

        <Warning>
          媒体链接在 24 小时后过期。
        </Warning>
      </Accordion>

      <Accordion title="Pinterest" icon="pinterest">
        |               |   |
        | ------------- | - |
        | 个人资料          |   |
        | 贴文（按关键词）      |   |
        | 贴文（按个人资料 URL） |   |
      </Accordion>

      <Accordion title="Reddit" icon="reddit">
        |          |   |
        | -------- | - |
        | 贴文（按关键词） |   |
        | 评论       |   |
      </Accordion>

      <Accordion title="TikTok" icon="tiktok">
        |               |   |
        | ------------- | - |
        | 个人资料（按搜索 URL） |   |
        | 评论            |   |
        | 贴文（按关键词）      |   |
        | 贴文（按个人资料 URL） |   |
      </Accordion>

      <Accordion title="Quora" icon="quora">
        |    |   |
        | -- | - |
        | 贴文 |   |
      </Accordion>

      <Accordion title="Vimeo" icon="vimeo">
        |           |   |
        | --------- | - |
        | 贴文（按关键词）  |   |
        | 贴文（按 URL） |   |
      </Accordion>

      <Accordion title="X (Twitter)" icon="twitter">
        |    |   |
        | -- | - |
        | 贴文 |   |
      </Accordion>

      <Accordion title="YouTube" icon="YouTube">
        |             |   |
        | ----------- | - |
        | 个人资料        |   |
        | 贴文（按关键词）    |   |
        | 贴文（按 URL）   |   |
        | 贴文（按搜索过滤条件） |   |
      </Accordion>

      <Accordion title="TikTok" icon="TikTok">
        媒体仅在同一会话生成的密钥下可访问。
      </Accordion>

      <Accordion title="Linkedin" icon="Linkedin">
        贴文数量限制为公开显示的数量（例如 **10**）
      </Accordion>
    </AccordionGroup>
  </Accordion>

  <Accordion title="当快照被标记为空时意味着什么？">
    当快照被标记为空时，表示快照中没有有效或可用的记录。然而，这并不意味着快照完全没有内容。在大多数情况下，它包含诸如错误或无效页面的信息：

    * **错误**：在数据收集过程中遇到的问题，例如无效输入、系统错误或访问限制。
    * **无效页面**：无法访问的页面，原因可能包括 404 错误（页面未找到）、内容已移除（例如不可用的产品）或访问受限。

    要查看这些详细信息，您可以在请求中使用参数 `include_errors=true`，它将显示快照中的错误信息和无效页面信息。这有助于您诊断并理解快照中的问题。
  </Accordion>

  <Accordion title="如何停止 Web Scraper 任务？">
    您可以通过以下 API 调用停止正在运行的收集：
    [https://docs.brightdata.com/cn/api-reference/scrapers/management-apis/cancel-snapshot](https://docs.brightdata.com/cn/api-reference/scrapers/management-apis/cancel-snapshot)
  </Accordion>

  <Accordion title="您提供哪些域名的爬虫？">
    ae.com

    airbnb.com

    amazon.com

    apps.apple.com

    ashleyfurniture.com

    asos.com

    balenciaga.com

    bbc.com

    berluti.com

    bestbuy.com

    booking.com

    bottegaveneta.com

    bsky.app

    carsales.com.au

    carters.com

    celine.com

    chanel.com

    chileautos.cl

    crateandbarrel.com

    creativecommons.org

    crunchbase.com

    delvaux.com

    digikey.com

    dior.com

    ebay.com

    edition.cnn.com

    en.wikipedia.org

    enricheddata.com

    espn.com

    etsy.com

    example.com

    facebook.com

    fanatics.com

    fendi.com

    finance.yahoo.com

    g2.com

    github.com

    glassdoor.com

    global.llbean.com

    goodreads.com

    google.com

    hermes.com

    homedepot.ca

    homedepot.com

    ikea.com

    imdb.com

    indeed.com

    infocasas.com.uy

    inmuebles24.com

    instagram.com

    la-z-boy.com

    lazada.com.my

    lazada.sg

    lazada.vn

    lego.com

    linkedin.com

    loewe.com

    lowes.com

    manta.com

    martindale.com

    massimodutti.com

    mattressfirm.com

    mediamarkt.de

    metrocuadrado.com

    montblanc.com

    mouser.com

    moynat.com

    mybobs.com

    myntra.com

    news.google.com

    nordstrom.com

    olx.com

    otodom.pl

    owler.com

    ozon.ru

    pinterest.com

    pitchbook.com

    play.google.com

    prada.com

    properati.com.co

    raymourflanigan.com

    realestate.com.au

    reddit.com

    revenuebase.ai

    sephora.fr

    shop.mango.com

    shopee.co.id

    sleepnumber.com

    slintel.com

    target.com

    tiktok.com

    toctoc.com

    tokopedia.com

    toysrus.com

    trustpilot.com

    trustradius.com

    unashamedcataddicts.quora.com

    us.shein.com

    ventureradar.com

    vimeo.com

    walmart.com

    wayfair.com

    webmotors.com.br

    wildberries.ru

    worldpopulationreview\.com

    worldpostalcode.com

    www2.hm.com

    x.com

    xing.com

    yapo.cl

    yelp.com

    youtube.com

    ysl.com

    zalando.de

    zara.com

    zarahome.com

    zillow\.com

    zonaprop.com.ar

    zoominfo.com

    zoopla.co.uk

    如果您的目标域名不在此列表中，我们可以为您开发专属的定制爬虫
  </Accordion>

  <Accordion title="我如何使用 Bright Data 通过 API 访问酒店数据？">
    我们没有专门为酒店提供的爬虫，但我们提供了 Booking.com 爬虫，并可以根据您的特定需求创建定制爬虫。
  </Accordion>

  <Accordion title="我如何获取所需的数据？">
    以下是快速指南，帮助您入门并选择适合您需求的解决方案：

    * 选项 1：丰富的预收集数据 – 探索我们的数据集市场

    如果您需要可直接使用的高质量数据，我们的数据集市场是最佳起点。我们已经收集并丰富了来自各种来源的大量数据。这些数据集旨在节省您的时间和精力，让您专注于分析数据并做出更明智的决策。

    只需浏览市场，找到符合您需求的数据集，即可立即开始使用。

    * 选项 2：用于实时数据的新鲜爬虫

    如果您的项目需要新鲜数据或数据集市场中不可用的高度特定信息，我们提供强大的工具，帮助您直接从网络收集实时数据。开始方法如下：

    **预建网页爬虫**\
    我们提供广泛的[热门网站预建爬虫](/cn/datasets/scrapers/scrapers-library/overview)，让您快速高效地收集数据。这些爬虫可直接使用，设置简单，非常适合希望快速上手的用户。

    **定制爬虫**\
    如果在预建爬虫列表中找不到目标网站，也没问题\\! 我们可以为您创建[专属定制爬虫](/cn/datasets/scrapers/custom-scrapers/scrape-any-web)。我们的专家团队将与您合作，设计能够收集精确所需数据的解决方案。

    **自行构建爬虫**\
    对于具备 JavaScript 知识或开发资源的用户，我们还提供使用[集成开发环境（IDE）](/cn/datasets/scraper-studio/introduction)构建爬虫的选项。这让您可以完全控制并灵活地创建符合您独特需求的爬虫。

    如有疑问或需要帮助，我们的专家团队随时为您提供支持。让我们开始吧\\!
  </Accordion>

  <Accordion title="我如何从 Google Maps 抓取数据？">
    1. 在控制面板找到“Google Maps 评论”爬虫，选择以 API 请求运行或使用“无代码”选项启动。
    2. 输入参数（地点页面 URL 以及要检索评论的天数）。
    3. 配置所需请求参数（如果使用 API）。
    4. 启动运行并收集数据。
  </Accordion>

  <Accordion title="我如何取消正在运行的快照？">
    要取消正在运行的快照，可使用以下方法之一：

    1. **API 请求：**

    * 发送 `POST` 请求至端点：

      POST /datasets/v3/snapshot/cencel ([playground](/cn/api-reference/scrapers/management-apis/cancel-snapshot))
    * 将 `{snapshot_id}` 替换为要取消的快照 ID。

    2. **控制面板：**

    * 转到爬虫的 **日志** 标签。
    * 找到正在运行的快照。
    * 将鼠标悬停在特定运行上，点击 **"X"** 进行取消。

    如果快照正在运行，这两种方法都会停止快照进程。
  </Accordion>

  <Accordion title="当“SearchGPT”处于激活状态时，ChatGPT 爬虫能工作吗？">
    可以，Bright Data GPT 爬虫在“搜索”功能激活时始终可工作。
  </Accordion>

  <Accordion title="我可以查看爬虫的代码吗？">
    Web Scrapers Library 中的爬虫是预建解决方案，其底层代码无法访问或修改。\
    对于希望了解爬虫工作原理的用户，Web Scraper IDE 在创建新爬虫时提供多个示例模板。这些示例可作为实用参考，帮助您理解爬虫技术并构建自己的定制解决方案。
  </Accordion>

  <Accordion title="我可以在使用 Scrapers 时直接将结果获取到我的本地或软件中吗？">
    是的，使用 Scrapers 您可以将抓取的数据返回到请求端点。\
    使用以下端点 - `POST api.brightdata.com/datasets/v3/scrape`\
    该端点允许高效获取数据，并确保与您的应用或工作流程无缝集成。\
    \
    **它是如何工作的？**\
    API 使您可以发送抓取请求，并直接在请求端点接收结果。这消除了数据检索或发送至外部存储的需求，简化了数据收集流程。\
    \
    **限制**

    * 对于长时间的收集操作，最佳做法是使用我们的[tigger/](/cn/api-reference/rest-api/scraper/asynchronous-requests)端点（如果在使用 /scrape 端点时收集请求耗时过长，您将获得快照 ID，收集完成后可使用该 ID[下载](/cn/api-reference/scrapers/delivery-apis/download-snapshot)数据）。
  </Accordion>

  <Accordion title="什么是 Dataset ID，我在哪里可以找到？">
    Dataset ID 是 Scrapers 请求中使用的唯一标识符。它包含在请求 URL 中，用于指定您要访问的特定爬虫。该 ID 确保您的 API 调用从系统中正确爬虫获取数据。用法如下：\
    `https://api.brightdata.com/datasets/v3/trigger?dataset_id=DATASET_ID_HERE`

    Dataset ID 示例：`gd_XXXXXXXXXXXXXXXXX`\
    例如：`gd_l1viktl72bvl7bjuj0`

    您可以在感兴趣爬虫的 Scrapers 页面中，在 **API 请求生成器** 标签下找到精确的 Dataset ID，已自动填入 API 请求，方便复制使用。

    注意：类似 `s_XXXXXXXXXXXXXXXXXX` 的 ID，例如 `s_m7hm4et0141r2rhojq` 不是 Dataset ID，而是快照 ID——快照是从单次 Scrapers 请求收集的数据集合。
  </Accordion>

  <Accordion title="什么是“仅发现”模式？">
    在仅发现模式下，发现阶段获得的结果会作为最终输出返回，不会进入 PDP（产品详情页）阶段。

    例如，如果启动亚马逊产品发现爬虫时使用仅发现模式，它只会返回发现阶段找到的产品 URL。当关闭此模式时，爬虫会继续访问并提取在发现阶段识别的每个产品页面的数据。
  </Accordion>

  <Accordion title="是否可以重新运行失败的快照？">
    可以。您可以使用 rerun API 重新运行快照。

    示例：

    ```bash theme={null}
    curl --request POST --url https://api.brightdata.com/datasets/v3/snapshot/{snapshot_id}/rerun --header 'Authorization: Bearer {token}'
    ```
  </Accordion>

  <Accordion title="如何取回您的原始输入？">
    您可以使用以下 API 调用取回输入数据：

    ```bash theme={null}
    curl -H "Authorization: Bearer TOKEN API" -H "Content-Type: application/json" "https://api.brightdata.com/datasets/v3/snapshot/sd_XXXX/input" -k
    ```

    只需替换：

    * `YOUR_API_KEY` 替换为您的实际 API key
    * `sd_XXXX` 替换为您的快照 ID
  </Accordion>

  <Accordion title="UI 中的“同步（实时）”和“异步”有什么区别？">
    控制面板使用两个直接映射到 API 端点的 UI 标签：

    | UI 标签                               | API 端点                      | 适用场景                  |
    | ----------------------------------- | --------------------------- | --------------------- |
    | **同步（实时）（Synchronous (Real-time)）** | `POST /datasets/v3/scrape`  | 需要对 1–20 个 URL 获取即时结果 |
    | **异步（Asynchronous）**                | `POST /datasets/v3/trigger` | 处理批量 URL、发现任务或大型数据集   |
  </Accordion>

  <Accordion title="我在哪里获取快照 ID？">
    触发收集（POST `/datasets/v3/trigger`）、过滤数据集（POST `/datasets/filter`）或通过数据集订阅时，都会返回快照 ID。您也可以使用 GET `/datasets/v3/snapshots` 列出您的所有快照。
  </Accordion>

  <Accordion title="响应中的交付任务 ID 用来做什么？">
    响应中的 `id` 是交付任务 ID。使用它调用 GET `/datasets/v3/delivery/{delivery_id}` 来跟踪交付进度。轮询直到状态为 "done"。
  </Accordion>

  <Accordion title="快照需要处于特定状态吗？">
    是的。快照必须处于 `ready` 状态。在调用 deliver 之前，使用 GET `/datasets/snapshots/{id}` 进行检查。可能的状态：`scheduled`、`building`、`ready`、`failed`。
  </Accordion>

  <Accordion title="我可以将同一个快照交付到多个目的地吗？">
    可以。对同一个快照 ID，使用不同的交付配置多次调用此端点即可。
  </Accordion>

  <Accordion title="支持哪些文件格式？">
    `json`、`jsonl` 和 `csv`。
  </Accordion>

  <Accordion title="如何将大型快照拆分为较小的文件？">
    使用 `batch_size` 参数设置每个文件的记录数。每个文件（批次）必须低于 5GB 硬性上限。用 5GB 除以您的平均记录大小来估算 `batch_size`，然后从较低的值开始，并根据实际获得的文件大小进行调整。

    例如，如果您的平均记录约为 5KB，则 `batch_size` 为 1,000,000 时文件恰好接近 5GB 上限。建议从 500,000 条记录（约 2.5GB）开始，以确保安全低于上限，然后根据收到的文件大小调高或调低 `batch_size`。
  </Accordion>

  <Accordion title="为什么我的请求返回 400 错误？">
    最常见的原因是您的 `batch_size` 生成的文件超过 5GB。例如，如果您的平均记录大小约为 5KB，则 `batch_size` 为 1,000,000 会生成约 5GB 的文件，可能超出限制。请调低 `batch_size`（例如调至 100,000）后重试。
  </Accordion>

  <Accordion title="我可以压缩输出吗？">
    可以。设置 `compress: true` 即可接收 gzip 压缩的文件。
  </Accordion>

  <Accordion title="每个批次的最大文件大小是多少？">
    5GB。这是每个交付文件的硬性上限。使用 `batch_size` 控制每个文件包含的记录数，确保每个文件都低于此阈值。
  </Accordion>
</AccordionGroup>
