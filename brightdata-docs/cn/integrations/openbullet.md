> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 OpenBullet 中设置 Bright Data

> 在 OpenBullet 上集成 Bright Data，增强您的自动化工作流程。本指南将帮助您配置 Bright Data，以实现安全高效的操作。

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

## 什么是 OpenBullet？

**OpenBullet** 是一款功能强大的自动化和测试工具，通常用于管理和测试 HTTP 请求、抓取数据以及执行自动化工作流程。通过集成 **Bright Data**，您可以确保安全、私密和可靠的连接，同时最大程度地降低被检测或封禁的风险。

## 如何在 OpenBullet 中设置 Bright Data

按照以下步骤，将 **Bright Data** 集成到 OpenBullet：

<Steps>
  <Step title="安装 OpenBullet">
    1. 访问 [OpenBullet GitHub 页面](https://github.com/openbullet/OpenBullet2) 并下载最新版本。
    2. 解压下载的文件，并在您的系统上运行应用程序。
  </Step>

  <Step title="创建代理组">
    1. 在 OpenBullet 仪表板中，进入 **Proxies**（代理）选项卡。
    2. 点击 **Add Group**（添加组）以创建新的代理组。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/openbullet1.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=b5bd17e20685e2fb3f19c42f770a8e24" alt="" width="800" height="178" data-path="images/integrations/openbullet1.png" />
    </Frame>

    3. 在 **Name**（名称）字段中输入一个描述性名称，以便日后管理和识别。
    4. 点击 **Accept**（接受）以确认并保存代理组。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/openbullet2.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=bee2c729b308476f812121517ae4191a" alt="" width="265" height="129" data-path="images/integrations/openbullet2.png" />
    </Frame>
  </Step>

  <Step title="添加 Bright Data 代理">
    1. 从代理组列表中选择刚刚创建的组。
    2. 点击 **Import**（导入）以打开代理配置面板。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/openbullet3.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=4579710ccd86efc37d84525a0d8a9f36" alt="" width="728" height="182" data-path="images/integrations/openbullet3.png" />
    </Frame>

    3. 在 **Import proxies**（导入代理）窗口：
       * 切换到 **Paste**（粘贴）选项卡。
       * 按以下格式粘贴您的 Bright Data 代理信息：\
         `[HOST]:[PORT]:[USERNAME]:[PASSWORD]`
       * 点击 **Accept**（接受）以保存您的代理设置。

    <Note>
      如果需要特定国家的代理，请调整用户名格式为 `your-username-country-XX`（例如 `your-username-country-US`），以使用特定的出口节点。
    </Note>
  </Step>
</Steps>

通过在 **OpenBullet** 中集成 **Bright Data**，您可以使用安全匿名的连接来增强自动化任务、测试应用程序或抓取数据。Bright Data 可确保稳定的性能和隐私保护。
