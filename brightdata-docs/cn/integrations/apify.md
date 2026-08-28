> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 Apify 中使用 Bright Data

> 让网络爬取更加顺畅！将 Oculus 代理集成到 Apify，可实现更流畅、匿名且高效的爬取工作流程，帮助您绕过 IP 封锁、地理限制和验证码等挑战。请按照本指南，在 Apify 中设置 Oculus 代理，以提高性能和可靠性。

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

## 什么是 Apify？

Apify 是一个功能强大的网络爬取和自动化平台。它允许开发者创建和运行自定义网络爬取工具，称为 **Actors**（执行器），以自动化数据收集和处理任务。通过集成 Bright Data 代理，您可以增强 Apify 工作流的匿名性、稳定性和效率，确保任务顺利运行。

## 如何将 Bright Data 集成到 Apify

在本指南中，我们将使用 [**Web Scraper**](https://apify.com/apify/web-scraper) 执行器作为示例。

**步骤 1. 访问您的 Apify 仪表板和工具**

1\. 使用您的凭据登录 [Apify 账户](https://apify.com/)。

2\. 在仪表板中，转到 **Apify Store** 以浏览可用工具。使用搜索栏或按类别浏览，找到 Web Scraper 执行器。

**步骤 2. 启动 Web Scraper 执行器**

1\. 在左侧菜单的 **Actors** 部分找到 **Web Scraper 执行器**。

2\. 点击它，打开配置页面。

<Frame as="div">
  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/apify2.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=3cf2447670127cca9c51b2f9ab271890" alt="" width="1485" height="365" data-path="images/integrations/apify2.png" />
</Frame>

**步骤 3. 定义爬取的目标 URL**

1\. 在 **输入（Input）** 选项卡中，找到 **基本配置（Basic Configuration）** 部分。

2\. 输入您想要爬取的网页目标 URL。

3\. 根据您的爬取需求添加一个或多个 URL。

<Frame as="div">
  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/apify3.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=b3923e861028b1f7980b82712a812cf1" alt="" width="858" height="519" data-path="images/integrations/apify3.png" />
</Frame>

<Note>
  Bright Data 合规性规定，搜索引擎（如 `google`）只能通过 SERP 代理区域访问。测试时，请使用非搜索引擎目标。
</Note>

**步骤 4. 设置自定义代理选项**

1\. 向下滚动至 **代理和浏览器配置（Proxy and Browser Configuration）** 部分。

2\. 选择 **自定义代理（Own proxies）** 以启用代理设置。

3\. 按以下格式输入您的 [Bright Data 代理详情](https://www.bright.cn/cp/zones)：

```basic theme={null}
http://[USERNAME]:[PASSWORD]@[HOST]:[PORT]
```

4\. 使用您的 Bright Data 凭据，并在需要时修改用户名以访问特定国家/地区（例如：`your-username-country-US`）。

<Frame as="div">
  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/apify4.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=ebcec1a7b26d19504803d38fbca1d950" alt="" width="833" height="401" data-path="images/integrations/apify4.png" />
</Frame>

**步骤 5. 启动并验证执行器任务**

1\. 代理配置完成后，点击 **保存 & 启动（Save & Start）** 以启动执行器。

2\. 检查日志，确保任务运行顺利，并且 Bright Data 代理已激活。

<Frame as="div">
  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/apify5.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=f6a4ff756434c146abe05e4d9346de77" alt="" width="828" height="283" data-path="images/integrations/apify5.png" />
</Frame>

通过将 Bright Data 代理集成到 Apify，您可以运行强大、匿名和地理定位的自动化工作流。无论是爬取数据、处理信息，还是管理大规模项目，Bright Data 都能确保 Apify 任务的顺畅和可靠性。立即开始构建更智能的自动化流程吧！
