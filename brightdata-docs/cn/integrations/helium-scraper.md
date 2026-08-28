> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 Helium Scraper 中设置 Bright Data

> 将 Bright Data 与 Helium Scraper 集成，实现安全、高效和匿名的网页抓取，并灵活管理代理。

<Accordion title="展开以获取您的 Bright Data 代理访问信息">
  ### 您的代理访问信息

  Bright Data 代理按“代理区域”（Proxy zones）进行分组。每个区域包含其对应的代理配置。&#x20;

  要获取代理区域的访问权限：&#x20;

  1. 登录 Bright Data 控制面板
  2. 选择现有代理区域或新建一个代理区域
  3. 点击新的区域名称，并选择 **概览（Overview）** 选项卡
  4. 在概览选项卡中，找到 **访问详情（Access details）**，并单击复制图标将代理访问信息复制到剪贴板&#x20;
  5. 您需要以下信息：代理主机（Proxy Host）、代理端口（Proxy Port）、代理区域用户名（Proxy Zone username）和代理区域密码（Proxy Zone password）
  6. 点击复制图标，将文本复制到剪贴板，并粘贴到您的工具的代理配置中&#x20;

  ### 访问详情示例

  <img src="https://mintcdn.com/brightdata/w0SvUEkwL-1dGVtS/snippets/accessdetails.png?fit=max&auto=format&n=w0SvUEkwL-1dGVtS&q=85&s=a3d4e920631ae105cb2f388c63bc5b5d" alt="" width="597" height="508" data-path="snippets/accessdetails.png" />

  ### 住宅代理访问

  要使用 Bright Data 的 **住宅代理（Residential Proxies）**，您必须是经过 KYC 验证的企业账户。请与 Bright Data 合规团队完成 KYC 验证；不存在自动或无需 KYC 的访问方式。尚未完成 KYC 时，请使用 ISP 或数据中心代理。[了解更多...](/proxy-networks/residential/network-access)

  ### 目标是搜索引擎？

  如果您的目标是 Google、Bing 或 Yandex 等搜索引擎，则需要使用专门的搜索引擎结果页（**SERP**）代理 API。请使用 Bright Data SERP API 来访问搜索引擎。\
  [点击此处了解 Bright Data SERP 代理 API。](/scraping-automation/serp-api/introduction)

  ### 避免工具中的 `PROXY ERROR`

  一些工具会使用搜索引擎作为代理测试目标：如果您的代理测试失败，这可能就是原因。请确保您的测试目标域名不是搜索引擎（此设置在工具配置中，而非 Bright Data 代理的控制范围内）。
</Accordion>

## 什么是 Helium Scraper？

Helium Scraper 是一款直观的桌面网页抓取工具，可帮助您无需任何编码技能即可从网站提取数据。它的可视化界面使数据选择、提取和整理变得简单，非常适合初学者和有经验的用户。

Helium Scraper 适用于中小规模的抓取项目。无论您是自由职业者、营销人员还是商业专业人士，它都能为您提供一种高效、简单的方法来收集和组织网页数据，而无需编程的复杂性。

## Helium Scraper 代理集成

按照以下简单步骤，在 Helium Scraper 中设置 Bright Data 代理：

<Steps>
  <Step title="安装 Helium Scraper">
    1. [下载 Helium Scraper](https://www.heliumscraper.com/eng/download.php) 并安装到您的计算机上。
    2. 安装完成后，启动该工具。
  </Step>

  <Step title="访问代理列表">
    在 Helium Scraper 中，点击 **File > Proxy List** 打开代理配置面板。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/helium-scraper1.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=1a4776cc1bac43a22bc25ab504f39dcf" alt="" width="200" height="248" data-path="images/integrations/helium-scraper1.png" />
    </Frame>
  </Step>

  <Step title="配置 Bright Data 代理">
    在提供的字段中输入您的 Bright Data 代理信息：

    * **主机 (Host)**：输入 `http://brd.superproxy.io/`。
    * **端口 (Port)**：使用您的 [Bright Data 控制面板](https://www.bright.cn/cp/zones) 提供的端口号。
    * **用户名 (Username)**：输入您的 Bright Data 代理用户名。
    * **密码 (Password)**：输入您的 Bright Data 代理密码。

    点击 **OK** 保存您的代理设置。

    <Info>
      **对于特定国家的代理，您可以输入类似 `your-username-country-US` 的格式，以获取美国出口节点。**
    </Info>
  </Step>

  <Step title="为您的项目启用代理">
    1. 在菜单中点击 **Project > Settings**。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/helium-scraper2.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=de0b0b37d37a7116f217647518075fe9" alt="" width="199" height="104" data-path="images/integrations/helium-scraper2.png" />
    </Frame>

    2. 在设置窗口中，将 **Enable Proxies** 选项设置为 **True**。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/helium-scraper3.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=f7d6adcabcae72fcda56e036b8be9d64" alt="" width="350" height="554" data-path="images/integrations/helium-scraper3.png" />
    </Frame>
  </Step>

  <Step title="验证代理设置">
    1. 使用 Helium Scraper 内置浏览器打开一个显示您 IP 地址的网站。
    2. 检查显示的 IP 是否与 Bright Data 代理设置匹配，以确认代理集成成功。
  </Step>
</Steps>

**就是这样！** 您已成功将 Bright Data 代理集成到 Helium Scraper 中。
