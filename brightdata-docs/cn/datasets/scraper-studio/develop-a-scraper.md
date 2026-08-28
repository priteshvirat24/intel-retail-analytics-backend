> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 使用 IDE 开发爬虫

> 在 Bright Data Scraper Studio IDE 中构建自定义网页爬虫：使用 JavaScript 编写交互代码和解析器代码，预览、保存到生产环境，并配置交付方式。

本指南将带您从零开始在 Bright Data Scraper Studio IDE 中构建一个自定义网页爬虫。您将编写导航目标站点的交互代码、提取结构化字段的解析器代码，然后将爬虫保存到生产环境并配置交付方式。完成后，您将获得一个可通过 API、手动或按计划触发的可运行爬虫。

**预计用时：** 每个爬虫约 15 到 30 分钟，具体取决于目标站点的复杂程度。

## 前提条件

* 一个已激活且可访问 Scraper Studio 的 [Bright Data 账户](https://www.bright.cn/?hs_signup=1\&utm_source=docs)
* 基础的 JavaScript 知识（变量、函数、控制流）
* 一个您想抓取的目标 URL

<Tip>
  如果您更习惯用自然语言描述爬虫而不是亲自写代码，请使用 [Scraper Studio AI Agent](/cn/datasets/scraper-studio/ai-agent)。AI Agent 生成的爬虫与 IDE 编写的属于同一类。
</Tip>

## 如何在 IDE 中构建爬虫？

<Steps>
  <Step title="打开 Scraper Studio IDE">
    前往 [www.bright.cn/cp/scrapers](https://www.bright.cn/cp/scrapers)，点击 **Scraper Studio**，然后点击 **Develop a web scraper (IDE)**（使用 IDE 开发爬虫）打开一个空爬虫。
  </Step>

  <Step title="从零开始或选择模板">
    如果您的目标站点有匹配的起始模板，可以在 **Templates**（模板）面板中选择一个；否则从空白爬虫开始。模板是面向常见模式与站点的预构建爬虫，是快速熟悉 Bright Data Scraper Studio 写法约定的捷径。
  </Step>

  <Step title="编写交互代码">
    交互代码负责导航目标站点并将所需数据传递给解析器。在左侧的 **Interaction code**（交互代码）编辑器中编写。

    最简单的交互脚本：

    ```js theme={null}
    navigate(input.url);
    wait('.product-title');

    let data = parse();
    collect(data);
    ```

    对于多页抓取，使用 `next_stage()` 进行分发：

    ```js theme={null}
    navigate(input.url);
    wait('.listing');
    let listings = parse().listings;
    for (let url of listings)
      next_stage({url});
    ```

    每条交互命令的完整说明请参见 [Scraper Studio 函数参考](/cn/datasets/scraper-studio/functions)。
  </Step>

  <Step title="编写解析器代码">
    解析器代码读取已加载页面的 HTML，返回一条结构化记录。使用 Cheerio 类 jQuery 风格的 `$` 选择器。

    ```js theme={null}
    return {
      title: $('h1').text_sane(),
      price: new Money(+$('.price').text().replace(/\D+/g, ''), 'USD'),
      image: new Image($('img.product').attr('src')),
      listings: $('.listing a').toArray().map(el => $(el).attr('href')),
    };
    ```

    解析器代码会将数据返回给调用 `parse()` 的那个交互函数。Bright Data Scraper Studio 提供的解析器辅助函数请参见 [Scraper Studio 函数参考](/cn/datasets/scraper-studio/functions#parser-functions)。
  </Step>

  <Step title="选择 worker 类型">
    在 **Settings**（设置）面板中选择 worker 类型：

    * **Code worker**（更快、更便宜）：适用于静态 HTML 页面和公开 JSON 端点
    * **Browser worker**：适用于 JavaScript 渲染的页面、点击、滚动、弹窗或需要捕获后台流量的场景

    建议先用 Code worker，如果您需要使用[仅限 Browser worker 的函数](/cn/datasets/scraper-studio/worker-types#which-functions-are-browser-worker-only)，再切换为 Browser worker。
  </Step>

  <Step title="运行预览">
    点击 **Preview**（预览）按钮，对单个测试输入运行爬虫。结果会出现在 **Output**（输出）选项卡。使用 **Run log**（运行日志）和 **Browser network**（浏览器网络）选项卡可调试失败的运行。

    > **预期结果：** Output 选项卡显示一条包含解析器代码中所定义字段的结构化记录。
  </Step>

  <Step title="保存到生产环境">
    点击右上角的 **Save to Production**（保存到生产环境）。爬虫会出现在控制面板的 **My Scrapers**（我的爬虫）下，可通过 API、手动或按计划触发。
  </Step>

  <Step title="配置交付方式">
    在 **My Scrapers** 中打开爬虫，点击 **Delivery preferences**（交付偏好），选择目标位置（API 下载、webhook、S3、GCS、Azure、SFTP 或电子邮件）以及格式（JSON、NDJSON、CSV、XLSX）。完整的选项请参见 [启动数据收集与交付](/cn/datasets/scraper-studio/initiate-collection-and-delivery-options)。
  </Step>

  <Step title="启动爬虫">
    触发首次生产运行。根据您的工作流选择启动方式：

    * [通过 API 启动](/cn/datasets/scraper-studio/initiate-collection-and-delivery-options#how-do-i-trigger-a-scraper-run)
    * [手动启动](/cn/datasets/scraper-studio/initiate-collection-and-delivery-options#how-do-i-trigger-a-scraper-run)
    * [按计划调度爬虫](/cn/datasets/scraper-studio/initiate-collection-and-delivery-options#how-do-i-trigger-a-scraper-run)
  </Step>
</Steps>

## 常见问题

<AccordionGroup>
  <Accordion title="如何调试某个特定输入下失败的爬虫？">
    在 Bright Data Scraper Studio IDE 中打开爬虫，查看 **Last errors**（最近错误）选项卡。每个失败的输入都会与其精确的错误信息和错误代码一起被保存（最多保留最近 1,000 次失败）。在 IDE 中重新运行失败的输入以本地复现问题，修复交互或解析器代码后，保存一个新的生产版本。
  </Accordion>

  <Accordion title="可以编辑由 AI Agent 生成的爬虫吗？">
    可以。Bright Data Scraper Studio 中的任何爬虫，无论以何种方式创建，都可以在 IDE 中打开并编辑。您可以修改提取逻辑、调整选择器、增删输出字段，以及更换 worker 类型。
  </Accordion>

  <Accordion title="如何向输出 schema 添加字段？">
    在 IDE 的输出 schema 面板中点击 **Edit Schema**（编辑 schema）并添加新字段；或者直接在解析器代码中返回这些字段，保存到生产环境时 Bright Data Scraper Studio 会提示您更新 schema。
  </Accordion>

  <Accordion title="collect() 和 set_lines() 有什么区别？">
    使用 `collect()` 每次追加一条记录，这是发出数据的默认方式。`set_lines()` 用于逐步收集记录的场景：即使后续步骤抛出错误，也会交付最近一次的快照。每次调用 `set_lines()` 都会覆盖前一次。详见 [collect](/cn/datasets/scraper-studio/functions#collect-append-a-record-to-the-dataset) 和 [set\_lines](/cn/datasets/scraper-studio/functions#set-lines-set-output-lines-overriding-previous-calls)。
  </Accordion>
</AccordionGroup>

## 相关内容

<CardGroup cols={2}>
  <Card title="Scraper Studio 函数参考" icon="code" href="/cn/datasets/scraper-studio/functions">
    交互命令与解析器命令的完整参考
  </Card>

  <Card title="最佳实践" icon="list-check" href="/cn/datasets/scraper-studio/best-practices">
    构建快速、可靠爬虫的推荐模式
  </Card>

  <Card title="Scraper Studio IDE 界面" icon="display-code" href="/cn/datasets/scraper-studio/scraper-studio-ide-interface">
    IDE 中每个面板与控件的参考
  </Card>

  <Card title="自我修复工具" icon="wand-magic-sparkles" href="/cn/datasets/scraper-studio/self-healing-tool">
    使用自然语言提示词修复失效的爬虫并新增字段
  </Card>
</CardGroup>
