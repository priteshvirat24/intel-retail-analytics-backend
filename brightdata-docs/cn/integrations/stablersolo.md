> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何将 Bright Data 集成到 StablerSOLO

> 通过将 Bright Data 与 StablerSOLO 集成来增强你的数据提取能力。按照此分步指南无缝配置你的代理设置。

<Warning>
  **账户管理不是 Bright Data 平台支持的使用场景**（自 2026 年 4 月 1 日起生效）。这包括在 TikTok、Instagram 等类似平台上进行账户管理。Bright Data 代理不得用于此类用途。详情请参阅[可接受使用政策](https://brightdata.com/acceptable-use-policy)。
</Warning>

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

## 什么是 StablerSOLO？

**StablerSOLO** 是一个数据提取与网页抓取服务，提供低代码界面用于配置爬虫。它使开发者和数据科学家能够高效提取数据，而无需为每个任务编写自定义爬虫。

## 将 Bright Data 与 StablerSOLO 一起使用的好处

通过将 **Bright Data** 与 StablerSOLO 集成，你可以获得：

* **增强匿名性：** 在进行网页抓取活动时保护你的身份。
* **地理定向能力：** 可通过选择不同地区的代理来访问特定区域的数据。
* **更高的成功率：** 使用高质量代理 IP 绕过反爬虫机制。

## 如何将 Bright Data 集成到 StablerSOLO

按照以下步骤，将 Bright Data 集成到 StablerSOLO：

**步骤 1：访问 StablerSOLO 的代理配置**

1. 登录你的 [StablerSOLO 账号](https://stabler.tech/)。
2. 在主控制台页面向下滚动至底部的 **Recent Proxies** 部分。
3. 点击 **New Proxy** 按钮打开代理配置窗口。

<Frame as="div">
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/stabler1.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=79de6aba5243c73c596ee2636206cdab" alt="" width="606" height="191" data-path="images/integrations/stabler1.png" />
</Frame>

**步骤 2：配置并保存你的代理设置**

1. 在代理配置窗口中：

* 切换到 **Proxies List** 标签页。

* 输入你的 Bright Data 代理信息，格式如下：\
  `[USERNAME]:[PASSWORD]@[HOST]:[PORT]`。

2. 点击 **Test a Proxy Randomly** 来验证连接。
3. 测试成功后，点击 **Add New Proxy** 将代理保存到列表中。

将 **Bright Data** 与 **StablerSOLO** 集成，可通过提供匿名性、地理定向和更高成功率来增强你的数据提取流程。按照本指南设置你的代理并开始高效抓取吧。
