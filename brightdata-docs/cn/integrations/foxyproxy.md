> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何使用 FoxyProxy 设置 Bright Data

> 使用 FoxyProxy 轻松提升您的浏览体验！通过集成 Bright Data，您可以安全地管理和切换代理服务器，以实现流畅高效的网页抓取、安全浏览和应用测试。请按照本指南设置 Bright Data 与 FoxyProxy，以优化您的在线操作。

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

## 什么是 FoxyProxy？

**FoxyProxy** 是一款适用于 Chrome 和 Firefox 的多功能浏览器扩展，旨在简化代理管理。只需点击几下，您就可以在多个代理服务器之间切换，并利用浏览器的内置代理 API。无论您是进行数据抓取、测试应用程序，还是增强在线隐私，FoxyProxy 都能提供直观高效的代理管理解决方案。

## 如何将 Bright Data 集成到 FoxyProxy

<Steps>
  <Step title="安装 FoxyProxy 扩展程序">
    1. **对于 Chrome**：访问 [Chrome 网上应用店](https://chromewebstore.google.com/detail/foxyproxy/gcknhkkoolaabfmlnjonogaaifnjlfnp)，然后点击 **添加至 Chrome**。
    2. **对于 Firefox**：前往 [Mozilla 附加组件页面](https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-standard/)，然后点击 **添加至 Firefox**。

    安装完成后，您将在浏览器工具栏中看到 FoxyProxy 图标。
  </Step>

  <Step title="打开 FoxyProxy 设置">
    1. 点击工具栏中的 FoxyProxy 图标，并从下拉菜单中选择 **选项**。
    2. 这将打开 FoxyProxy 设置页面，您可以在其中管理代理配置。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/foxyproxy1.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=53800ad4881823fdef26a74df18d6fba" alt="" width="317" height="402" data-path="images/integrations/foxyproxy1.png" />
    </Frame>
  </Step>

  <Step title="添加新的代理配置">
    1. 在 FoxyProxy 设置菜单中，进入 **代理** 选项卡。
    2. 点击 **添加** 按钮，打开代理配置窗口。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/foxyproxy2.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=f69966818d2f9a65143025db5c9229d5" alt="" width="1243" height="218" data-path="images/integrations/foxyproxy2.png" />
    </Frame>
  </Step>

  <Step title="输入 Bright Data 代理详细信息">
    1. 在代理设置表单中，输入您的 Bright Data 账户信息：
       * **类型**：根据您的代理类型选择 `HTTP`、`HTTPS` 或 `SOCKS5`。
       * **主机名**：输入 `http://brd.superproxy.io/`。
       * **端口**：使用您的 [Bright Data 仪表板](https://www.bright.cn/cp/zones/page/plans) 提供的端口号。
       * **用户名**：输入您的 Bright Data 用户名。
       * **密码**：输入您的 Bright Data 密码。

    2. 输入所有详细信息后，点击 **保存** 以存储代理配置。

    <Note>
      如果要使用特定国家的代理，请在用户名后添加国家代码（例如，`your-username-country-US` 表示使用美国代理）。
    </Note>
  </Step>

  <Step title="激活并测试您的代理">
    1. 要启用已配置的代理，请点击工具栏中的 FoxyProxy 图标，并选择您刚刚创建的代理。
    2. 访问 [httpbin.org/ip](http://httpbin.org/ip) 以验证连接。显示的 IP 地址应与您的 Bright Data 代理匹配。

    <Note>
      如果您使用的是 Bright Data 的数据中心或 ISP 代理，您将能够查看代理 IP 地址。住宅代理可能会被我们的策略阻止，因此您可能会收到错误提示。若要查看住宅代理的详细信息（包括位置），请访问： [https://geo.brdtest.com/welcome.txt?product=resi\&method=native](https://geo.brdtest.com/welcome.txt?product=resi\&method=native) 。
    </Note>

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/foxyproxy3.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=2384fcc04773552c550ad595e8493d6e" alt="" width="314" height="405" data-path="images/integrations/foxyproxy3.png" />
    </Frame>
  </Step>
</Steps>

现在，您已成功配置 FoxyProxy 与 Bright Data，可以享受安全、流畅的浏览体验，并高效地进行网络操作。无论是测试应用、抓取数据，还是增强隐私保护，该设置都能让您的代理管理变得更加轻松便捷。
