> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 PhantomBuster 中设置 Bright Data

> 准备好提升您的自动化工作流程了吗？将 Bright Data 连接到 PhantomBuster，以实现更流畅、更安全、更高效的数据采集体验。在隐藏在线足迹并提升性能的同时，您可以专注于获取有价值的见解，而无需处理技术难题。

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

## 什么是 PhantomBuster？

PhantomBuster 是一个基于云的平台，可将繁琐的在线任务转化为高效的自动化流程。无需手动处理重复任务或费力获取所需数据，它会在后台完成繁重的工作，让您专注于探索机会、触达新受众并推动可衡量的成果。

<Tip>
  在浏览器会话期间保持一致的 IP，方法是在用户名中使用 `-session` 参数。这一点很重要，因为 Bright Data 代理默认情况下会在每次请求时更换 IP。[了解更多](/cn/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session) <br />

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

## 如何将 Bright Data 与 PhantomBuster 集成

将 Bright Data 代理集成到 PhantomBuster 中有助于保持匿名性、降低封锁风险并优化整个操作流程。只需按照以下步骤操作：

<Steps>
  <Step title="打开代理设置">
    登录您的 [PhantomBuster 账户](https://phantombuster.com/) 后，进入 **Proxies**（代理）设置页面。在这里，您可以配置连接，以确保自动化任务的安全性和隐私性。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/phantombuster1.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=1ceec79a02eb4fffc56d1e1410080ce7" alt="" width="187" height="381" data-path="images/integrations/phantombuster1.png" />
    </Frame>
  </Step>

  <Step title="创建新的代理池">
    点击 **"New proxy pool"**（新建代理池），创建一个专门存储 Bright Data 代理的集合。将其视为管理代理资源的安全存储库。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/phantombuster2.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=3dbca0e18a468449d724eae38700975d" alt="" width="926" height="569" data-path="images/integrations/phantombuster2.png" />
    </Frame>
  </Step>

  <Step title="命名您的代理池">
    为您的代理池设置一个清晰且易记的名称。当您处理多个项目或任务时，可以迅速识别适用于特定情况的代理池。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/phantombuster3.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=74140475b7c7e5f6d527377814ee6c58" alt="" width="532" height="246" data-path="images/integrations/phantombuster3.png" />
    </Frame>
  </Step>

  <Step title="添加 Bright Data 代理详情">
    按照以下格式输入您的 Bright Data 代理凭据：
    `host:port:username:password`

    您可以在 [Bright Data 仪表板](https://www.bright.cn/cp/zones/page/plans) 中找到这些详细信息。
    输入后，点击 **"Add proxy"**（添加代理）完成操作。您的新代理池现在已准备好作为您的数字防护盾。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/phantombuster4.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=310583a2ec6bb52d92129f6720a52d5a" alt="" width="1583" height="373" data-path="images/integrations/phantombuster4.png" />
    </Frame>
  </Step>

  <Step title="在 Phantom 的高级设置中调整配置">
    在设置 Phantom（PhantomBuster 工作流）时，打开 **Advanced settings**（高级设置），选择您创建的代理池。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/phantombuster5.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=1d7b676e2da9b0e80ea5a3165754a9a2" alt="" width="442" height="303" data-path="images/integrations/phantombuster5.png" />
    </Frame>
  </Step>

  <Step title="应用代理池">
    在 **Advanced settings**（高级设置）中，选择您刚刚配置的代理池。
    点击 **"Save settings"**（保存设置）以确认更改。
    从现在开始，您的 Phantom 任务将在 Bright Data 代理的保护下安全运行。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/pq7wn7mJJj8UJsym/images/integrations/phantombuster6.png?fit=max&auto=format&n=pq7wn7mJJj8UJsym&q=85&s=26cbcf6ebfe93a170ffb369abf5b04b5" alt="" width="742" height="530" data-path="images/integrations/phantombuster6.png" />
    </Frame>
  </Step>
</Steps>

**恭喜！您的 Bright Data 代理已成功集成到 PhantomBuster！**\
这意味着您可以更安心地运行自动化任务：您的身份保持隐藏，封锁风险降低，数据采集更加高效。尽情探索、创新，并取得成果，而无需纠结于技术难题。
