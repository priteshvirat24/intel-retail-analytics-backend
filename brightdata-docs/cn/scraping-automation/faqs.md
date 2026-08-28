> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 常见问题：自动化抓取产品

> 了解有关集成、配置和使用 Bright Data 自动化抓取产品的常见问题，包括 IP 类型、地理定位和错误代码。

<AccordionGroup>
  <Accordion title="如何避免被 Cloudflare 或 Cloudflare Turnstile 阻挡？">
    若要抓取使用 Cloudflare 或 Cloudflare Turnstile 的网站，我们建议使用 [Web Unlocker API](/cn/scraping-automation/web-unlocker/introduction) 或 [Browser API](/cn/scraping-automation/scraping-browser/introduction)。

    这两种方案会使用不同的方式，例如 CAPTCHA 解决、自定义指纹及请求头等，可以轻松绕过 Cloudflare。

    若你只需要从网站 `GET` HTML，而不需要在页面中执行任何互动操作，建议使用 [Web Unlocker API](/cn/scraping-automation/web-unlocker/introduction)。

    若你需要在页面执行互动（例如填写表单、点击按钮等），建议使用 [Browser API](/cn/scraping-automation/scraping-browser/introduction)。

    无论选择哪种方案，即使页面使用 Cloudflare 或 Cloudflare Turnstile，你仍然可以成功获取所需信息。
  </Accordion>

  <Accordion title="如何避免被 Datadome 阻挡？">
    若要抓取使用 Datadome 的网站，我们建议使用 [Web Unlocker API](/cn/scraping-automation/web-unlocker/introduction) 或 [Browser API](/cn/scraping-automation/scraping-browser/introduction)。

    这两种方案会使用不同的方式，例如 CAPTCHA 解决、自定义指纹及请求头等，可以轻松绕过 Datadome。

    若你只需要从网站 `GET` HTML，而不需要在页面执行互动操作，建议使用 [Web Unlocker API](/cn/scraping-automation/web-unlocker/introduction)。

    若你需要互动（例如点击、滚动、悬停等），则建议使用 [Browser API](/cn/scraping-automation/scraping-browser/introduction)。

    无论使用哪种方案，即使目标网站使用 Datadome，你仍能获取所需内容。
  </Accordion>

  <Accordion title="哪些网站被归类为高级域名（Premium Domains）？">
    高级域名是指由于解封难度较高、需要额外 Web Unlocker API 资源的网站。查看关于[高级域名及价格](/cn/scraping-automation/web-unlocker/features#web-unlocker-api-premium-domains)的更多信息。

    ### 高级域名列表

    <Note> 高级域名列表按季度更新，我们会在更新前 30 天通过邮件通知你。你随时可以在你的 Web Unlocker API Zone 中查看最新列表。</Note>

    |                        |                      |                           |
    | ---------------------- | -------------------- | ------------------------- |
    | advanceautoparts.com   | giantfoodstores.com  | realcanadiansuperstore.ca |
    | affitto.it             | gopuff.com           | realestate.com.au         |
    | agoda.cn               | gplay.bg             | restaurantguru.com        |
    | albertsons.com         | hermes.com           | searchpeoplefree.com      |
    | allpeople.com          | hyatt.com            | shopee.cl                 |
    | autozone.com           | idealo.de            | shopee.co.id              |
    | bestbuy.com            | immobilienscout24.de | shopee.co.th              |
    | bestwestern.com        | ingatlan.com         | shopee.com.br             |
    | billiger.de            | instacart.com        | shopee.com.co             |
    | bottlerover.com        | intersport.fr        | shopee.com.mx             |
    | carousell.com          | joann.com            | shopee.com.my             |
    | carousell.com.hk       | kroger.com           | shopee.ph                 |
    | carousell.com.my       | lazada.co.id         | shopee.sg                 |
    | carousell.ph           | lazada.co.th         | shopee.tw                 |
    | carousell.sg           | lazada.com.my        | shopee.vn                 |
    | carsales.com.au        | lazada.com.ph        | similarweb.com            |
    | cdiscount.com          | lazada.sg            | skyscanner.co.kr          |
    | chewy.com              | lazada.vn            | skyscanner.net            |
    | costco.com             | lowes.ca             | stopandshop.com           |
    | cvs.com                | lowes.com            | target.com                |
    | despegar.com.mx        | mcmaster.com         | temu.com                  |
    | dickssportinggoods.com | mediamarkt.de        | ticketmaster.com          |
    | dynos.es               | mediamarkt.es        | totalwine.com             |
    | emaxme.com             | medline.com          | tractorsupply.com         |
    | familytreenow\.com     | mscdirect.com        | walmart.com.mx            |
    | feuvert.fr             | napaonline.com       | wayfair.com               |
    | flooranddecor.com      | nofrills.ca          | weismarkets.com           |
    | foodlion.com           | peoplefinders.com    | wizzair.com               |
    | footlocker.co.uk       | platt.com            | worten.pt                 |
    | footlocker.com         | publicdatausa.com    |                           |
  </Accordion>

  <Accordion title="如何在 Web Unlocker API 中启用 JavaScript 渲染？" defaultOpen={false}>
    如果你需要 Web Unlocker API 通过 JavaScript 渲染网页，应使用以下功能：\
    [Manual Expect Elements](/cn/scraping-automation/web-unlocker/features#manual-'expect'-elements)

    此功能可确保 Web Unlocker API 返回的内容包含你需要渲染的页面部分。

    若你的使用场景需要在页面执行互动（点击、滚动、悬停等），则应改用\
    [Browser API](/cn/scraping-automation/scraping-browser/introduction)。
  </Accordion>

  <Accordion title="使用 Web Unlocker API、SERP API 或 Browser API 时，在哪里可以查看我的公共 IP？">
    这些产品所使用的公共 IP 对用户不可见。Web Unlocker API、SERP API 和 Browser API 使用动态 IP 池，其中包含真实的住宅 IP。为确保合规与隐私，这些 IP 会隐藏并不断轮换，以保持匿名性并优化解封效果。

    你可以通过以下测试 URL 查看有关 IP 的其他元数据，例如国家、ASN 和城市：\
    `http://brdtest.com/myip.json`

    **注意：** 返回内容中不会包含 IP 字段。
  </Accordion>

  <Accordion title="Web Unlocker API 或 SERP API 有速率限制吗？" defaultOpen={false}>
    未充值账户的默认速率限制为每分钟 1,000 次请求。你可以在控制面板中查看应用于你区域的具体速率限制，路径为该区域的“概览 (Overview)”选项卡 > 访问详情 (Access details)。向账户充值后，此默认限制将被移除。
  </Accordion>

  <Accordion title="我该如何抓取特定网站？" defaultOpen={false}>
    若要抓取特定网站，请按以下步骤操作：

    1. **选择适合你的产品：** Bright Data 提供 **Web Scraper IDE**、**Scrapers** 和 **Custom Scrapers** 等工具，可根据你的目标网站及需求进行选择。

    2. **搜索目标站点模板：** 使用 Scrapers 时，可以搜索流行网站的预构建模板，从而快速开始抓取。

    3. **自定义或构建你的 Scraper：**
       * 若目标网站没有现成模板，可使用 **Web Scraper IDE** 创建自定义 Scraper，或使用 **Custom Scrapers** 让我们为你构建。
       * 使用编辑器编写脚本或基于现有模板修改以满足需求。

    4. **测试并执行 Scraper：** s在 Bright Data 平台内运行 Scraper 获取数据，并使用 IDE 调试功能进行优化。

    5. **导出数据：** 完成抓取后，你可以以 JSON、CSV 或 Excel 格式导出数据，用于分析或集成。

    若你偏好无代码方案或需要协助，Bright Data 支持团队可为你提供帮助，也可直接请求定制数据集。
  </Accordion>
</AccordionGroup>
