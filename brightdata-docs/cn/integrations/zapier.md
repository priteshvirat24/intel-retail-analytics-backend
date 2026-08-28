> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何将 Bright Data 与 Zapier 集成

> 了解如何将 Bright Data Actors 与 Zapier 集成。

Bright Data 的 Zapier 集成让你无需编写任何代码即可自动化网页数据采集，并将结构化数据无缝传输到 Google Sheets、Slack、Trello、Airtable、Salesforce 等应用中。

## 可用的 Zap 操作：

以下是当前通过 Bright Data Zapier 集成支持的操作：

| 操作                                   | 描述                                      |
| :----------------------------------- | :-------------------------------------- |
| Scrape Amazon                        | 创建一个新的 Amazon 数据抓取请求，并等待数据返回            |
| Scrape Crunchbase                    | 创建一个新的 Crunchbase 数据抓取请求，并等待数据返回        |
| Scrape Facebook                      | 抓取来自 Facebook 帖子、评论或 Reels 的数据          |
| Scrape Google Play Store             | 创建一个新的 Google Play Store 数据抓取请求，并等待数据返回 |
| Scrape Instagram                     | 创建一个新的 Instagram 数据抓取请求，并等待数据返回         |
| Scrape Pinterest                     | 创建一个新的 Pinterest 数据抓取请求，并等待数据返回         |
| Run an Web Unlocker API              | 创建一个 Web Unlocker API 运行任务              |
| Scrape Vimeo                         | 创建一个新的 Vimeo 数据抓取请求，并等待数据返回             |
| Scrape Yelp                          | 创建一个新的 Yelp 数据抓取请求，并等待数据返回              |
| Scrape ChatGPT                       | 创建一个新的 ChatGPT 数据抓取请求，并等待数据返回           |
| Download Snapshot Content (Scrapers) | 下载 Snapshot 内容（Scrapers）                |
| Scrape Glassdoor                     | 创建一个新的 Glassdoor 数据抓取请求，并等待数据返回         |
| Scrape Indeed                        | 创建一个新的 Indeed 数据抓取请求，并等待数据返回            |
| Scrape LinkedIn                      | 创建一个新的 LinkedIn 数据抓取请求，并等待数据返回          |
| Scrape Pitchbook                     | 创建一个新的 Pitchbook 数据抓取请求，并等待数据返回         |
| Scrape TikTok                        | 创建一个新的 TikTok 数据抓取请求，并等待数据返回            |
| Scrape X (Twitter)                   | 创建一个新的 X 数据抓取请求，并等待数据返回                 |
| Scrape YouTube                       | 创建一个新的 YouTube 数据抓取请求，并等待数据返回           |

## 如何将 Bright Data 与 Zapier 集成

<Steps>
  <Step title="前置条件">
    在开始之前，请确保你已经准备好以下内容：

    * 一个有效的 <a href="/cn/api-reference/authentication#如何生成新的-api-key？">Bright Data API Key</a>
    * 一个可用的 <a href="https://zapier.com/">Zapier 账户</a>
  </Step>

  <Step title="创建一个 Zap">
    登录你的 Zapier 账户，导航到 **Zaps** 区域，然后点击 **Create Zap** 来开始构建你的工作流。
  </Step>

  <Step title="设置触发器">
    选择与你的使用场景匹配的触发应用和事件。例如：

    * 使用 **Schedule by Zapier** 来每小时或每天运行一次抓取。
    * 使用 **New Row in Google Sheets** 在新增数据时触发抓取。
    * 使用 **Webhook** 或 **表单提交** 来基于实时输入动态触发抓取任务。
  </Step>

  <Step title="添加 Bright Data 作为 Action">
    在 **Action** 步骤中搜索并选择 **Bright Data**。接下来系统会提示你设置期望执行的 Bright Data 操作。

    <Frame>
      <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/zapier-action-setup.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=77777d21d76a8e12f57c71827ef191de" alt="zapier-action-setup" width="391" height="740" data-path="images/integrations/zapier-action-setup.png" />
    </Frame>
  </Step>

  <Step title="选择操作事件">
    选择你希望执行的具体 Bright Data 操作。例如，如需抓取 Amazon 数据，请选择 **Scrape Amazon**。\
    Zapier 还支持来自 LinkedIn、TikTok、YouTube 等多平台的数据抓取。
  </Step>

  <Step title="连接你的 Bright Data 账户">
    点击 Bright Data 连接字段旁的 **Sign In** 以授权访问你的账户。\
    系统会打开一个新窗口，你可以在其中输入你的 Bright Data API Key。

    <Frame>
      <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/zapier-api-key.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=79af8f89302f99eead2748a1ff347ed8" alt="zapier-api-key" width="950" height="695" data-path="images/integrations/zapier-api-key.png" />
    </Frame>
  </Step>

  <Step title="配置并测试 Action">
    根据所选操作自定义你的抓取参数。例如，**Scrape Amazon** 支持提取：

    * 产品详情
    * 评论
    * 卖家信息
    * 搜索结果
    * 全球商品数据库条目

    配置完成后，点击 **Test Action** 以确保设置正确。你应该会收到一个示例响应以确认输出无误。
  </Step>

  <Step title="发布你的 Zap">
    测试成功后，点击 **Publish Zap** 激活你的工作流。\
    激活后会根据触发条件自动运行。

    你还可以继续添加更多动作，例如：

    * 通过 Slack 或 email 发送通知
    * 将结构化数据写入 Google Sheets、Airtable、各种 CRM

    自动化组合无限可能！
  </Step>
</Steps>

## 总结

通过 Bright Data 的 Zapier 集成，你可以无需编写任何代码即可自动化网页数据收集。\
无论是定时抓取、事件触发抓取，还是基于实时输入的动态抓取，此集成都能让数据采集、管理以及在你的工具链中流转变得更加轻松高效，从而简化业务监控、报告和工作流程管理。
