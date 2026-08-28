> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 Octoparse 中设置 Bright Data

> 通过将 Bright Data 集成到 Octoparse，提高您的网页抓取效率，确保数据提取的安全性和匿名性，同时降低 IP 封锁风险。

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

## 什么是 Octoparse？

Octoparse 是一款用户友好的网页抓取工具，无需任何编程知识即可从网站收集数据。它提供简单的点选界面，使您能够从复杂的网站提取信息。Octoparse 允许自定义、自动化和定时执行抓取任务，并支持将提取的数据保存为 CSV 或 Excel 等格式。无论是市场调研、价格监测，还是潜在客户获取，Octoparse 都能让数据收集变得快速、简单、高效！

## Octoparse 代理集成

按照以下步骤，将 Bright Data 代理集成到 Octoparse：

<Steps>
  <Step title="安装 Octoparse">
    访问 [Octoparse 官网](https://www.octoparse.com/download) 下载并安装该工具。
  </Step>

  <Step title="创建新任务">
    点击左上角的 **+New** 按钮，然后选择 **Custom Task**（自定义任务）。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/octoparse1.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=43b9c31bb400f0658336d40237f8aae9" alt="" width="226" height="175" data-path="images/integrations/octoparse1.png" />
    </Frame>
  </Step>

  <Step title="输入目标 URL">
    在 **URL Input**（URL 输入）字段中输入要抓取的网站地址，然后点击 **Save**（保存）。
  </Step>

  <Step title="进入代理设置">
    网页加载完成后，进入 **Task Settings > Anti-blocking**（任务设置 > 反封锁）。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/octoparse2.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=d4c19030c29adf2ec740314cb2b78f5e" alt="" width="468" height="67" data-path="images/integrations/octoparse2.png" />
    </Frame>
  </Step>

  <Step title="启用代理">
    勾选 **Access websites via proxies**（通过代理访问网站），然后选择 **Use my own proxies**（使用自定义代理）。点击 **Configure**（配置）。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/octoparse3.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=619b07770a23c81e8cd7867d8430f5f4" alt="" width="796" height="544" data-path="images/integrations/octoparse3.png" />
    </Frame>
  </Step>

  <Step title="配置 Bright Data 代理">
    在弹出的窗口中，按以下格式输入您的 Bright Data 代理信息：

    ```sh theme={null}
    IP/host:port:username:password
    ```

    * **IP/host**: 输入 `http://brd.superproxy.io/`。
    * **Port**: 使用您在 [Bright Data 控制面板](https://www.bright.cn/cp/zones/page/plans) 中提供的端口号。
    * **Username**: 输入您的 Bright Data 代理 `username`。
    * **Password**: 输入您的 Bright Data 代理 `password`。

    <Info>
      如果需要使用特定国家的代理，可以使用格式 `your-username-country-US` 以获取美国出口节点。
    </Info>

    如果您使用的是轮换代理，可以在 **Switch interval**（切换间隔）中设置 IP 轮换的频率。对于保持会话的代理，请根据需要调整会话时长。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/octoparse4.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=b337c93a79f9dc876dd1620c5933e104" alt="" width="793" height="543" data-path="images/integrations/octoparse4.png" />
    </Frame>
  </Step>

  <Step title="保存设置">
    点击 **Confirm**（确认）以应用更改，然后点击 **Save**（保存）。
  </Step>
</Steps>

就这样！您已成功将 Bright Data 代理集成到 Octoparse。
