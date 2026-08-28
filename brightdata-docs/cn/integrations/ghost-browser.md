> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 Ghost Browser 中设置 Bright Data

> 使用 Bright Data 和 Ghost Browser 简化多账户管理，确保安全匿名浏览，同时提升您的工作效率。

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

## 什么是 Ghost Browser？

<Tip>
  通过在用户名中使用 `-session` 参数，可以在整个浏览器会话期间保持一致的 IP。这一点至关重要，因为 Bright Data 代理默认在每次请求时轮换 IP。[了解更多](/cn/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

<Warning>
  不支持通过数据中心和 ISP 代理网络连接社交网络，包括：Facebook、TikTok、Instagram、X（Twitter）、LinkedIn、YouTube、Reddit、Pinterest、Snapchat 和 Discord。
</Warning>

Ghost Browser 是一款专为需要轻松管理多个在线账户的用户设计的高效网页浏览器。它具有独特的多会话功能，允许您在不同的标签页中运行独立的浏览器会话。这意味着您可以同时登录同一平台的多个账户，而不会发生跨会话干扰。

虽然它并未专注于高级反检测功能，但 Ghost Browser 非常适合希望拥有简洁有序工作流程的用户。对于需要同时管理多个账户或项目的专业人士而言，它是一个理想的工具。

## Ghost Browser 代理集成

以下是将 Bright Data 代理集成到 Ghost Browser 的方法：

<Steps>
  <Step title="安装 Ghost Browser">
    1. 下载并安装 [**Ghost Browser**](https://ghostbrowser.com/download/)。
    2. 安装完成后，登录您的账户以访问主界面。
  </Step>

  <Step title="访问 Ghost Proxy Control">
    1. 点击浏览器右上角的 **Ghost Proxy Control** 图标。
    2. 选择 **添加/编辑代理**。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/ghostbrowser1.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=e0ccf5a905b9a6c4c28c4cb9709aebfb" alt="" width="525" height="246" data-path="images/integrations/ghostbrowser1.png" />
    </Frame>
  </Step>

  <Step title="添加新代理">
    在 **代理管理器** 中，选择 **添加单个代理** 选项。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/ghostbrowser2.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=1a23e079ca12b83fa7bd1d3f47c5a7fd" alt="" width="970" height="413" data-path="images/integrations/ghostbrowser2.png" />
    </Frame>
  </Step>

  <Step title="配置您的 Bright Data 代理">
    在代理设置窗口中，填写您的 Bright Data 代理信息：

    * **名称**：可选 – 为您的代理指定一个描述性名称（例如 "Bright Data"）。
    * **主机**：输入 `http://brd.superproxy.io/`。
    * **端口**：使用 [Bright Data 仪表盘](https://www.bright.cn/cp/zones) 提供的端口号。
    * **用户名**：输入您的 Bright Data 代理 `用户名`。
    * **密码**：输入您的 Bright Data 代理 `密码`。

    点击 **添加代理** 以保存您的设置。

    <Info>
      如果需要特定国家的代理，可以输入格式如 `your-username-country-US` 以获取美国出口节点。
    </Info>
  </Step>

  <Step title="在 Ghost Browser 中启用代理">
    1. 返回 **Ghost Proxy Control** 菜单。
    2. 在 **Active Identity** 和 **Active Workspace** 设置下选择您新添加的 Bright Data 代理。
    3. 重新加载您的标签页，以应用选定的代理到您的浏览会话。
  </Step>
</Steps>

**就是这样！** 您的 Bright Data 代理现已集成到 Ghost Browser 中。
