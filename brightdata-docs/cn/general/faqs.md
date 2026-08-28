> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 常见问题 (FAQs)

> 关于 Bright Data 账户的常见问题：代理凭据、端口 44445、SSL 证书以及所有代理和 API 产品的 IP 管理。

<AccordionGroup>
  <Accordion title="我的代理用户名和密码在哪里？">
    您可以在您创建的 Bright Data 产品（例如代理、Web Unlocker API、Browser API 等）的“**概览**”选项卡中找到您的用户名和密码。如果需要，您可以创建多个密码。

    **注意**：您为 Bright Data 网站创建的用户名和密码**不能**用于访问实际产品。它仅用于**仪表板访问**。
  </Accordion>

  <Accordion title="我应该使用哪个代理服务端口：22225 还是 33335？">
    在 Bright Data 中，我们区分代理服务端口（您向其发送请求的端口）和目标端口（指您尝试访问的目标网站或主机）。

    此条目指的是我们的主机的代理服务端口：[brd.superproxy.io](http://brd.superproxy.io)

    #### 代理端口

    在以 **原生模式 (Native mode)** 使用 Bright Data 代理时，您需要提供一个代理端口。在使用代理 API 时，此设置是多余的 — 有关 [API 与原生访问 (API vs. native Access)](/api-reference/authentication) 差异的更多信息，请参阅此处。

    #### 代理端口迁移

    Bright Data 现在通过原生代理端口 `44445` 提供服务，该端口随 2026 年 7 月推出的新版根证书启用。端口 `22225` 和 `33335` 上的旧证书将于 2026 年 9 月 25 日 00:00 UTC 到期，该日期之后仍依赖旧证书的流量将失败。如需分步迁移说明，请参阅[根证书迁移指南](/cn/general/account/ssl-certificate-migration)。

    对于需要 [KYC 验证](/proxy-networks/residential/network-access#kyc-verification) 或 [SSL 证书](/general/account/ssl-certificate) 的 **住宅、移动、Web Unlocker API 和 SERP API** 类型的代理区域，**必须**安装与所用端口兼容的正确证书。

    如果您仍在使用端口 `22225` 或 `33335`，请在 2026 年 9 月 25 日之前完成向端口 `44445` 的过渡。

    #### 支持的设置

    | 端口      | 证书        | 到期时间            |
    | ------- | --------- | --------------- |
    | `44445` | 新证书（必须使用） | 自 2026 年 7 月生效  |
    | `33335` | 旧证书（已弃用）  | 2026 年 9 月 25 日 |
    | `22225` | 旧证书（已弃用）  | 2026 年 9 月 25 日 |

    #### 协同工作

    证书协同运行且仅端口不同，因此您可以平稳迁移。请对所连接的端口使用相应的证书。端口 `44445` 使用 `brightdata_root_ca_44445.crt`。

    ### 迁移步骤

    要迁移到端口 `44445`，您应该：

    1. 通知您的网络管理员或安全管理员，允许您的对外通信开放域名 `brd.superproxy.io` 的端口 `44445`。
    2. 如果您正在使用证书：安装新证书。请参阅此处的证书安装说明：[SSL 证书](/general/account/ssl-certificate)
  </Accordion>

  <Accordion title="如何为我的账户设置密码？">
    即使您最初是通过“**魔法链接 (magic link)**”或六位数字代码登录的，您也随时可以为您的账户创建一个密码。然后您可以将密码保存在浏览器中，以便更快地访问控制面板。

    要为您的 Bright Data 账户设置密码，请遵循以下步骤：

    1. **访问身份验证设置**：点击“**设置**”并转到 ['密码与身份验证' 选项卡](https://www.bright.cn/cp/setting/auth)。
    2. **创建您的密码**：按照说明为您的账户创建密码。我们建议密码至少 10 位，包含数字和符号。

    请记住，每个用户必须设置自己的密码。如果您的账户中有其他用户，他们可以根据需要单独配置他们的密码。

    注意：如果您是通过 Google 或 GitHub 等第三方服务进行身份验证的，请添加一个单独的用户并通过 Bright Data 的标准注册流程登录，而不是使用第三方服务。
  </Accordion>

  <Accordion title="为什么我收不到密码重置邮件？">
    <Note>
      如果您的组织已配置**强制启用 SSO**（通过 Microsoft Entra ID、Okta 或 Google Workspace），则**不会**发送密码重置邮件。在强制启用 SSO 的账户上，基于密码的身份验证已被禁用。

      请改为通过您组织的身份提供商登录：

      * **Microsoft Entra ID**：在 Bright Data 登录页面输入您的邮箱；系统会自动将您重定向到 Entra。
      * **Okta**：通过您的 Okta 仪表板或 Bright Data Okta 磁贴登录。
      * **Google Workspace**：在 Bright Data 登录页面使用“使用 Google 账号登录”选项。

      如果您需要恢复访问权限，请联系您的账户管理员。另请参阅：

      * [通过 Bright Data 设置 Azure SSO (Entra ID)](/cn/general/authentication/How_to_set_up_Azure_SSO_Entra_ID_with_Bright_Data)
      * [通过 Bright Data 设置 Okta SSO](/cn/general/authentication/How_to_set_up_SSO_with_Okta_in_Bright_Data)
      * [通过 Bright Data 设置 Google Workspace SSO](/cn/general/authentication/How_to_set_up_SSO_with_Google_Workspace_in_Bright_Data)
    </Note>

    如果您的账户**未**强制启用 SSO，但仍然收不到重置邮件：

    * 检查您的垃圾邮件文件夹。
    * 在 [账户设置 → 个人资料](https://www.bright.cn/cp/setting/customer_details) 中核实登记的邮箱地址。
    * 确保您的邮件服务商没有对来自 `sendgrid.net` / Bright Data 域名的邮件进行限流或拦截。
    * 如果问题仍然存在，请联系 [Bright Data 支持团队](https://www.bright.cn/contact)。
  </Accordion>

  <Accordion title="如何查看分配给您的区域的 IP？">
    要查看分配给您区域的 IP 列表，只需导航到 [**‘我的代理页面’**](https://www.bright.cn/cp/zones)，**点击**您的代理区域，向下滚动到 **‘已分配 IP’ (Allocated IPs)** 部分，然后点击 **‘显示已分配 IP’ (Show allocated IPs)** 或 **‘下载 IP 列表’ (Download IPs list)**。

    <Note>
      出于隐私和安全考虑，此选项不适用于住宅共享按 GB 付费配置。请改用 `-session` 标志。
    </Note>

    <img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/faqs/review-allocated-ips.gif?s=b6913172ce8a9cb9a4d3ec92992901f2" alt="review-allocated-ips.gif" width="1600" height="734" data-path="images/general/faqs/review-allocated-ips.gif" />
  </Accordion>

  <Accordion title="如何查看您区域的统计信息？">
    有两种方法可以查看您区域的统计信息：

    <Tabs>
      <Tab title="通过控制面板">
        * 要查看所有区域的统计信息，请转到您的 [仪表板](https://www.bright.cn/cp/zones/dashboard)：

                  <img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/faqs/statistics-via-control-panel.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=51f20710c1dd6c8f8d3b82048b0e6aa5" alt="statistics-via-control-panel.png" width="1827" height="977" data-path="images/general/faqs/statistics-via-control-panel.png" />
        * 要查看特定区域的统计信息，请点击左侧导航栏上的“代理和爬取 (Proxies and Scraping)”，然后进入该区域的设置并点击“**统计信息 (statistics)**”选项卡：

                  <img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/faqs/specific-zone-statics.gif?s=1be027b9cfc6c1c4e61839f4034215d1" alt="specific-zone-statics.gif" width="1828" height="978" data-path="images/general/faqs/specific-zone-statics.gif" />
      </Tab>

      <Tab title="通过 API">
        * 请访问 [此页面](/api-reference/) 查看所有可用的 API 端点（支持多种语言）以及与查看统计信息相关的示例响应。
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="如何设置带宽使用限制？">
    默认情况下，所有代理区域的使用都是**无限制**的，您可以通过以下 4 个参数之一设置限制：

    * \$ /天
    * \$ /月
    * 字节/天
    * 字节/月

    要在您的某个区域上设置此限制，请从 Bright Data 的 ['我的代理页面'](https://www.bright.cn/cp/zones) 执行以下步骤：

    <Steps>
      <Step title="点击您的任何一个区域，进入该区域的设置。" />

      <Step title="转到“访问参数 (Access parameters)”选项卡。">
        <img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/faqs/access-parameters.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=76be7260cd910fb1fd0ba8a217c06e32" alt="access-parameters.png" width="677" height="159" data-path="images/general/faqs/access-parameters.png" />
      </Step>

      <Step title="向下滚动到“限制 (Limit)”，默认值为“无限制 (unlimited)”" />

      <Step title="点击“编辑”按钮">
        <img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/faqs/edit-limit.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=cfd7dcad99841c7b5f8f27fcd5353213" alt="edit-limit.png" width="760" height="914" data-path="images/general/faqs/edit-limit.png" />
      </Step>

      <Step title="启用“支出限制 (spend limit)”选项。">
        <img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/faqs/spend-limit-toggle.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=5d30ea5ee8b33b4719d291e4079612ba" alt="spend-limit-toggle.png" width="647" height="353" data-path="images/general/faqs/spend-limit-toggle.png" />
      </Step>

      <Step title="设置您希望使用的参数并点击“更新”" />

      <Step title="您将在“限制”部分以及“使用/支出限制 (Usage/Spend Limit)”列中的代理页面上看到更改。" />
    </Steps>
  </Accordion>

  <Accordion title="如何计算住宅 IP 的成本效益？">
    <img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/faqs/cost-limits-table.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=36ac2f0f007d771badb7ddb8335ca77e" alt="cost-limits-table.png" width="680" height="369" data-path="images/general/faqs/cost-limits-table.png" />

    **我们是如何计算这张表的？**

    您的公司需要通过每小时向特定网站发送 1,000 个 http 请求来收集网络信息。您编写了爬虫代码并在服务器上运行它。目标网站在阻止您的爬虫之前，允许来自同一 IP 的每分钟 50 个请求。现在，您必须购买更多代理。

    **假设您选择数据中心代理：**
    您不想共享 IP，因此购买了 **200 个专用数据中心 IP**。您将爬虫与新的数据中心代理进行集成，耗时 2 小时，然后运行新程序。这一次，您的目标网站需要 **3 天**才能检测到您的爬虫。一旦您的代理被检测到，您将不得不购买新的代理并再次重复此过程，每天检查以确保代理未被检测到。每月成本（所有数字均来自真实客户）：

    * 200 个专用 IP：**\$500**
    * 带宽：（1000 个请求 X 每个请求 20KB X 24 小时 X 30 天 = 14.5GB）：每月 **\$3**
    * 开发人员（2 小时集成 X 10 + 每 3 天 1 小时管理代理）：每月约 **3 天工作量**或约 **\$900**

    仅这些项目的每月总成本将**至少为 \$1400**，而且开发人员每小时 **\$30** 的薪水是非常保守的。此外，这还没有考虑到如果您的目标网站在阻止您之前发送错误信息，或者如果您的信息流每隔几天就被切断，这将对您的品牌或收入流造成不利影响，从而导致信息可靠性缺乏。

    **假设您选择 Bright Data 住宅代理：**
    您购买了一个包含 **40GB** 访问无限量住宅 IP 的基本套餐。集成您的爬虫需要 **2 小时**。由于每天平均有 **300 万个住宅 IP** 可用，您的目标网站无法检测到您的爬虫，从而让您能够专注于其他项目。

    带宽和无限量 IP 每月只需 **\$500**。您的信息始终**可靠**，因为您的请求总是成功的，并且访问永远不会在月中被切断。当您的业务因此次爬取而增长，并且您的项目每月超过 600MB 时，成本差异可能远高于**约 \$1000**。

    Bright Data 还允许您在不使用时**暂停**您的账户，因此您的成本可能低于每月 \$500。首先使用 **\$5 代金券**免费数据中心流量来测试 Bright Data 的优势，然后请求访问我们的住宅网络，以实现廉价且可靠的数据收集。
  </Accordion>

  <Accordion title="我区域名称旁边的黄色警告图标是什么意思？">
    > **这是设置您的允许列表访问的提醒**

    为了限制您的代理区域被未经授权的服务器访问，我们建议您设置 **IP 允许列表**。这将确保只允许您识别的 IP 访问您的代理区域，以实现更高的安全性和控制。

    请咨询您的 IT 或网络专家，以确保您的**出站 IP 是固定的且不会更改**，否则您可能会阻止您公司或您公司中的其他授权用户访问代理区域。
  </Accordion>

  <Accordion title="如何使用基于令牌的身份验证来限制访问">
    当使用多个具有轮换 IP 且目标为远程安装的代理管理器 (Proxy Manager) 的爬虫时，此工作流程是最佳的。此方法需要您的 API 密钥和身份验证令牌。

    在远程服务器内部的终端/CMD 中运行以下命令

    ```sh theme={null}
    curl -X GET "[http://127.0.0.1:22999/api/gen_token](http://127.0.0.1:22999/api/gen_token)" -H "accept: application/json"
    ```

    这将为您生成一个 API 密钥作为身份验证令牌：

    ```sh Output theme={null}
    "token":"<API_KEY>"
    ```

    现在，您可以简单地使用您刚刚创建的 API 密钥发送请求：

    ```sh theme={null}
    curl -x token:<API_KEY>@<remote-server-IP>:<Port> "target-site.com"
    ```
  </Accordion>

  <Accordion title="是否有办法知道我的公开数据是否被 Bright Data 的收集平台收集了？">
    > **是的**

    您可以在此处查看您的公开数据是否被收集：[https://www.bright.cn/check\_your\_data](https://www.bright.cn/check_your_data)
  </Accordion>

  <Accordion title="你们只采集公开数据，还是也会采集私人数据？">
    我们从不采集私人数据。我们只采集公开可获取的数据。
  </Accordion>

  <Accordion title="什么是试玩模式 (Playground mode)？">
    当您注册时，您的账户会自动进入为期 7 天的免费试用“**试玩模式**”，让您可以立即尝试不同的 Bright Data 解决方案。不需要信用卡或任何其他形式的付款方式。

    此外，每个新账户还会获得一个每月循环的[免费套餐](/cn/general/account/billing-and-pricing/free-tier)，可在 Web Unlocker API、SERP API、Web Scraper API 和 Scraper Studio 上使用 5,000 个信用额度。这些额度在每月 1 号续期，不会随试用结束而过期。

    您可以延长此免费试用期。要在没有任何限制的情况下测试或使用 Bright Data 的代理解决方案并获得 **\$5 免费额度**，请 [验证您的账户](https://www.bright.cn/cp/billing_flow) 以开始我们的**限时 30 天试用**。请注意，30 天试用不适用于某些国家/地区。

    在试玩模式期间，无法提交 KYC 验证表或端口请求表。要开始 KYC 或端口请求流程，您需要向账户存入至少 **\$10**。

    <Note>
      试玩模式是一个免费试用，旨在进行**小规模测试和探索**，不适用于大规模测试或生产用途。在您 [验证您的账户](https://www.bright.cn/cp/billing_flow) 并开始我们的 [限时试用](/general/faqs#what-is-limited-trial-mode) 之前，产品使用将受到速度、带宽和每秒请求数等限制。
    </Note>

    <Note>
      在试玩模式（或任何未充值状态）下，SERP API、Web Unlocker API 和代理产品的请求受每分钟 1,000 次请求的默认速率限制。您可以在控制面板中查看当前速率限制，路径为该区域的“概览 (Overview)”选项卡 > 访问详情 (Access details)。
    </Note>
  </Accordion>

  <Accordion title="什么是限时试用模式 (Limited Trial mode)？">
    **限时试用**模式是一个免费试用期，允许您在无需立即付款的情况下**自由探索**我们的 Bright Data 代理解决方案。您将获得 **\$5 信用额度**，可在 **30 天**内使用我们的任何代理服务，让您有整整一个月的时间来测试和体验我们的产品。

    请注意，30 天试用不适用于某些国家/地区。如果您没有看到此选项，请向您的账户添加资金以开始使用 Bright Data — 您只需添加低至 **\$10** 即可开始使用即用即付 (Pay as You Go) 计划。

    #### 我如何验证我的账户以开始“限时试用”并获得 \$5 信用额度？

    账户验证简单且免费。只需 [向您的账户添加有效的付款方式](https://www.bright.cn/cp/billing_flow) 即可开始**限时试用**模式并获得您的 **\$5 信用额度**。您将**不会**被收费。

    #### 30 天试用期结束后会发生什么？

    在 30 天试用期结束时，您的 \$5 代理试用额度将过期（如果尚未使用），您需要向账户**添加资金**才能继续使用代理产品。可在 Web Unlocker API、SERP API、Web Scraper API 和 Scraper Studio 上使用的每月 5,000 个信用额度的[免费套餐](/cn/general/account/billing-and-pricing/free-tier)不受影响，并继续按月续期。

    #### 我可以在您的任何代理产品上使用免费信用额度吗？

    是的，在试用期间，**\$5 试用信用额度**可用于我们的**任何代理产品**，让您能够测试最符合您需求的产品。
  </Accordion>

  <Accordion title="为什么我无法连接到 brightdata.com 网站或仪表板？">
    在极少数情况下，一些**广告拦截程序/扩展**可能会阻止访问 Bright Data 网站。如果您遇到任何问题，请**将 brightdata.com 加入允许列表**或禁用广告拦截程序。
  </Accordion>

  <Accordion title="在哪里可以查看国家代码列表？">
    以下是 ISO 3166 国家代码列表。**并非**列表中的所有国家都拥有 Bright Data 代理，但大多数国家都有。

    | 国家名称               | 国家代码 |
    | ------------------ | ---- |
    | 奥兰群岛               | ax   |
    | 津巴布韦               | zw   |
    | 赞比亚                | zm   |
    | 也门                 | ye   |
    | 西撒哈拉               | eh   |
    | 瓦利斯和富图纳            | wf   |
    | 美属维尔京群岛            | vi   |
    | 英属维尔京群岛            | vg   |
    | 越南                 | vn   |
    | 委内瑞拉（玻利瓦尔共和国）      | ve   |
    | 瓦努阿图               | vu   |
    | 乌兹别克斯坦             | uz   |
    | 乌拉圭                | uy   |
    | 美利坚合众国             | us   |
    | 美属离岛               | um   |
    | 大不列颠及北爱尔兰联合王国      | gb   |
    | 阿拉伯联合酋长国           | ae   |
    | 乌克兰                | ua   |
    | 乌干达                | ug   |
    | 图瓦卢                | tv   |
    | 特克斯和凯科斯群岛          | tc   |
    | 土库曼斯坦              | tm   |
    | 土耳其                | tr   |
    | 突尼斯                | tn   |
    | 特立尼达和多巴哥           | tt   |
    | 汤加                 | to   |
    | 托克劳                | tk   |
    | 多哥                 | tg   |
    | 东帝汶                | tl   |
    | 泰国                 | th   |
    | 坦桑尼亚联合共和国          | tz   |
    | 塔吉克斯坦              | tj   |
    | 中国台湾省              | tw   |
    | 叙利亚阿拉伯共和国          | sy   |
    | 瑞士                 | ch   |
    | 瑞典                 | se   |
    | 斯瓦尔巴和扬马延           | sj   |
    | 苏里南                | sr   |
    | 苏丹                 | sd   |
    | 斯里兰卡               | lk   |
    | 西班牙                | es   |
    | 南苏丹                | ss   |
    | 南乔治亚和南桑威奇群岛        | gs   |
    | 南非                 | za   |
    | 索马里                | so   |
    | 所罗门群岛              | sb   |
    | 斯洛文尼亚              | si   |
    | 斯洛伐克               | sk   |
    | 荷属圣马丁              | sx   |
    | 新加坡                | sg   |
    | 塞拉利昂               | sl   |
    | 塞舌尔                | sc   |
    | 塞尔维亚               | rs   |
    | 塞内加尔               | sn   |
    | 沙特阿拉伯              | sa   |
    | 圣多美和普林西比           | st   |
    | 圣马力诺               | sm   |
    | 萨摩亚                | ws   |
    | 圣文森特和格林纳丁斯         | vc   |
    | 圣皮埃尔和密克隆           | pm   |
    | 法属圣马丁              | mf   |
    | 圣卢西亚               | lc   |
    | 圣基茨和尼维斯            | kn   |
    | 圣赫勒拿、阿森松和特里斯坦-达库尼亚 | sh   |
    | 圣巴泰勒米              | bl   |
    | 留尼汪                | re   |
    | 卢旺达                | rw   |
    | 罗马尼亚               | ro   |
    | 北马其顿共和国            | mk   |
    | 卡塔尔                | qa   |
    | 波多黎各               | pr   |
    | 葡萄牙                | pt   |
    | 波兰                 | pl   |
    | 皮特凯恩               | pn   |
    | 菲律宾                | ph   |
    | 秘鲁                 | pe   |
    | 巴拉圭                | py   |
    | 巴布亚新几内亚            | pg   |
    | 巴拿马                | pa   |
    | 巴勒斯坦国              | ps   |
    | 帕劳                 | pw   |
    | 巴基斯坦               | pk   |
    | 阿曼                 | om   |
    | 挪威                 | no   |
    | 北马里亚纳群岛            | mp   |
    | 诺福克岛               | nf   |
    | 纽埃                 | nu   |
    | 尼日利亚               | ng   |
    | 尼日尔                | ne   |
    | 尼加拉瓜               | ni   |
    | 新西兰                | nz   |
    | 新喀里多尼亚             | nc   |
    | 荷兰                 | nl   |
    | 尼泊尔                | np   |
    | 瑙鲁                 | nr   |
    | 纳米比亚               | na   |
    | 缅甸                 | mm   |
    | 莫桑比克               | mz   |
    | 摩洛哥                | ma   |
    | 蒙特塞拉特              | ms   |
    | 黑山                 | me   |
    | 蒙古                 | mn   |
    | 摩纳哥                | mc   |
    | 摩尔多瓦共和国            | md   |
    | 密克罗尼西亚联邦           | fm   |
    | 墨西哥                | mx   |
    | 马约特                | yt   |
    | 毛里求斯               | mu   |
    | 毛里塔尼亚              | mr   |
    | 马提尼克               | mq   |
    | 马绍尔群岛              | mh   |
    | 马耳他                | mt   |
    | 马里                 | ml   |
    | 马尔代夫               | mv   |
    | 马来西亚               | my   |
    | 马拉维                | mw   |
    | 马达加斯加              | mg   |
    | 中国澳门               | mo   |
    | 卢森堡                | lu   |
    | 立陶宛                | lt   |
    | 列支敦士登              | li   |
    | 利比亚                | ly   |
    | 利比里亚               | lr   |
    | 莱索托                | ls   |
    | 黎巴嫩                | lb   |
    | 拉脱维亚               | lv   |
    | 老挝人民民主共和国          | la   |
    | 吉尔吉斯斯坦             | kg   |
    | 科威特                | kw   |
    | 大韩民国               | kr   |
    | 朝鲜民主主义人民共和国        | kp   |
    | 基里巴斯               | ki   |
    | 肯尼亚                | ke   |
    | 哈萨克斯坦              | kz   |
    | 约旦                 | jo   |
    | 泽西岛                | je   |
    | 日本                 | jp   |
    | 牙买加                | jm   |
    | 意大利                | it   |
    | 以色列                | il   |
    | 马恩岛                | im   |
    | 爱尔兰                | ie   |
    | 伊拉克                | iq   |
    | 伊朗（伊斯兰共和国）         | ir   |
    | 印度尼西亚              | id   |
    | 印度                 | in   |
    | 冰岛                 | is   |
    | 匈牙利                | hu   |
    | 中国香港               | hk   |
    | 洪都拉斯               | hn   |
    | 教廷                 | va   |
    | 赫德岛和麦克唐纳群岛         | hm   |
    | 海地                 | ht   |
    | 圭亚那                | gy   |
    | 几内亚比绍              | gw   |
    | 几内亚                | gn   |
    | 根西岛                | gg   |
    | 危地马拉               | gt   |
    | 关岛                 | gu   |
    | 瓜德罗普               | gp   |
    | 格林纳达               | gd   |
    | 格陵兰                | gl   |
    | 希腊                 | gr   |
    | 直布罗陀               | gi   |
    | 加纳                 | gh   |
    | 德国                 | de   |
    | 格鲁吉亚               | ge   |
    | 冈比亚                | gm   |
    | 加蓬                 | ga   |
    | 法属南部领地             | tf   |
    | 法属波利尼西亚            | pf   |
    | 法属圭亚那              | gf   |
    | 法国                 | fr   |
    | 芬兰                 | fi   |
    | 斐济                 | fj   |
    | 法罗群岛               | fo   |
    | 福克兰群岛（马尔维纳斯）       | fk   |
    | 埃塞俄比亚              | et   |
    | 斯威士兰               | sz   |
    | 爱沙尼亚               | ee   |
    | 厄立特里亚              | er   |
    | 赤道几内亚              | gq   |
    | 萨尔瓦多               | sv   |
    | 埃及                 | eg   |
    | 厄瓜多尔               | ec   |
    | 多米尼加共和国            | do   |
    | 多米尼克               | dm   |
    | 吉布提                | dj   |
    | 丹麦                 | dk   |
    | 科特迪瓦               | ci   |
    | 捷克                 | cz   |
    | 塞浦路斯               | cy   |
    | 库拉索                | cw   |
    | 古巴                 | cu   |
    | 克罗地亚               | hr   |
    | 哥斯达黎加              | cr   |
    | 库克群岛               | ck   |
    | 刚果共和国              | cg   |
    | 刚果民主共和国            | cd   |
    | 科摩罗                | km   |
    | 哥伦比亚               | co   |
    | 科科斯（基林）群岛          | cc   |
    | 圣诞岛                | cx   |
    | 中国                 | cn   |
    | 智利                 | cl   |
    | 乍得                 | td   |
    | 中非共和国              | cf   |
    | 开曼群岛               | ky   |
    | 加拿大                | ca   |
    | 喀麦隆                | cm   |
    | 柬埔寨                | kh   |
    | 佛得角                | cv   |
    | 布隆迪                | bi   |
    | 布基纳法索              | bf   |
    | 保加利亚               | bg   |
    | 文莱达鲁萨兰国            | bn   |
    | 英属印度洋领地            | io   |
    | 巴西                 | br   |
    | 布韦岛                | bv   |
    | 博茨瓦纳               | bw   |
    | 波斯尼亚和黑塞哥维那         | ba   |
    | 博内尔、圣尤斯特歇斯和萨巴      | bq   |
    | 玻利维亚（多民族国）         | bo   |
    | 不丹                 | bt   |
    | 百慕大                | bm   |
    | 贝宁                 | bj   |
    | 伯利兹                | bz   |
    | 比利时                | be   |
    | 白俄罗斯               | by   |
    | 巴巴多斯               | bb   |
    | 孟加拉国               | bd   |
    | 巴林                 | bh   |
    | 巴哈马                | bs   |
    | 阿塞拜疆               | az   |
    | 奥地利                | at   |
    | 澳大利亚               | au   |
    | 阿鲁巴                | aw   |
    | 亚美尼亚               | am   |
    | 阿根廷                | ar   |
    | 安提瓜和巴布达            | ag   |
    | 南极洲                | aq   |
    | 安圭拉                | ai   |
    | 安哥拉                | ao   |
    | 安道尔                | ad   |
    | 美属萨摩亚              | as   |
    | 阿尔及利亚              | dz   |
    | 阿尔巴尼亚              | al   |
    | 阿富汗                | af   |
  </Accordion>

  <Accordion title="我可以将 Bright Data 用作我的电脑 VPN 吗？">
    并非如此。Bright Data 是一项面向希望从互联网收集公共网络数据的企业客户的服务，并非为个人用户设计。

    此外，使用 Bright Data 不会加密您的互联网流量。

    如果您想要免费 VPN，我们建议您查看 [BrightVPN](https://brightvpn.com) - 它适用于 Windows 和 macOS，甚至不需要您开通账户，确保完全匿名。
  </Accordion>

  <Accordion title="我可以使用 Bright Data 直接 API 来管理我的账户吗？">
    是的，我们提供了广泛的操作，您可以使用我们的直接 API 通过代码以编程方式执行这些操作，以管理您的账户和代理/区域 - 您可以执行添加或删除区域、管理 IP 允许/拒绝列表、获取分配给您的区域的 IP 列表、获取账单余额等操作。
    有关更详细和准确的信息，请参阅我们的 API 文档部分 -
    [账户管理 API 文档](/cn/api-reference/account-management-api)
  </Accordion>

  <Accordion title="如何将我的公司详细信息添加到发票中？">
    您可以在[账户设置](https://www.bright.cn/cp/setting/customer_details)中添加您的公司详细信息，您的月度发票将自动发送给您的公司。
  </Accordion>

  <Accordion title="如何更改/更新我的账户邮箱地址？">
    您无法直接“更改”或“更新”您账户中的邮箱地址。
    但是，您可以创建一个具有新邮箱地址的新用户，然后删除“旧”用户 - 这将达到与更新/更改/替换邮箱地址相同的预期结果。
  </Accordion>

  <Accordion title="如何仅使用 IP 允许列表访问代理？(IP:PORT 方法)" defaultOpen="false">
    要仅通过 IP 允许列表身份验证 (IP:PORT) 访问您的代理，而无需使用 API 密钥身份验证方法或 USERNAME:PASSWORD 身份验证方法，您可以使用 [Proxy Manager (代理管理器)](/cn/proxy-networks/proxy-manager/introduction) 工具。
  </Accordion>

  <Accordion title="获得 KYC 决定需要多长时间以及如何查看我的账户验证状态？ ">
    审核您的 KYC 请求通常最多需要 2 个工作日。但是，如果您的提交资料不完整，或者提交的文档在视觉上不清晰、已过期或不正确，KYC 可能需要更长的时间。

    要查看您的账户验证状态，请浏览到控制面板的“账户设置 -> 个人资料”下。在那里，您可以看到您的验证状态，可能是以下之一： `not submitted` (未提交) 、 `in progress` (进行中) 、 `approved` (已批准) 或 `denied` (已拒绝)。

    点击此链接查看状态: [https://www.bright.cn/cp/setting/customer\_details](https://www.bright.cn/cp/setting/customer_details)
  </Accordion>

  <Accordion title="我可以使用个人邮箱进行 KYC 吗？" defaultOpen="false">
    不可以，只有公司邮箱地址才被接受用于 KYC 验证。
  </Accordion>

  <Accordion title="我在哪里可以查看 Bright Data 的法律限制和政策？" defaultOpen="false">
    要查看我们的法律限制和政策，请参阅以下页面：[Bright Data 主服务协议](https://www.bright.cn/license)
  </Accordion>

  <Accordion title="如何联系 Bright Data 支持/账户经理/销售/合规团队？ " defaultOpen="false">
    如果您需要联系我们的员工，可以通过控制面板中的“帮助与支持”部分（屏幕右上角问号图标 (?) 下方）进行，或发送电子邮件至 [sales@brightdata.com](mailto:sales@brightdata.com)、[support@brightdata.com](mailto:support@brightdata.com) 或 [compliance@brightdata.com](mailto:compliance@brightdata.com)。

    注意：我们的员工仅向付费客户或企业员工客户提供协助。如果通过控制面板无法使用联系支持的选项，请向您的账户充值，该选项将会解锁。
  </Accordion>

  <Accordion title="什么是 `zproxy.lum-superproxy.io`？ " defaultOpen="false">
    `zproxy.lum-superproxy.io` 是 Bright Data 过去使用的一个已弃用的代理集成端点 - 它不应再使用，因为它已被 `brd.superproxy.io` 取代。
  </Accordion>

  <Accordion title="我应该何时使用 Scrapers (爬虫) 和何时使用 Datasets (数据集)？" defaultOpen="false">
    **我应该何时使用 Scrapers (爬虫) 与 Datasets (数据集)？**

    * 使用 Scrapers (爬虫)：当您需要**新鲜或实时**数据（例如价格、新闻或实时更新），或者现有数据集中**没有**所需数据时。Scrapers (爬虫) 非常适合跟踪随时间的变化或直接从网站收集**小众、特定**的信息。
    * 使用 Datasets (数据集)：当您需要**历史**数据或**预先收集**的**结构化**信息时。Datasets (数据集) 可以节省时间和精力，特别适用于机器学习、分析或研究，但可能并非总是最新的。

    对于持续进行的项目，您可以结合使用 Datasets (数据集) 来获取历史背景，并使用 Scrapers (爬虫) 来获取实时更新。
  </Accordion>

  <Accordion title="我想删除我的账户">
    如果您希望**彻底删除**您的账户：

    * 转到 “设置 -> 账户设置 -> 个人资料”。
    * 点击 “删除账户”。

    请注意：

    * 此操作无法撤消。
    * 您的所有数据和设置都将丢失。
    * 所有用户将被注销并失去对平台的访问权限。
  </Accordion>

  <Accordion title="如何查找我的 Bright Data 账户 ID？ ">
    您的 Bright Data 账户 ID 是您的代理用户名凭证中的一个组成部分，在寻求支持时，您可能需要提供它，以便支持工程师提供正确的答复。

    您的账户 ID 和 Bright Data 控制面板登录信息**不是**您的代理登录信息。每个区域都有自己的用户名和密码进行访问。

    如果您点击控制面板右上角的用户图标，或者通过左侧菜单中的 “账户设置” 并选择 “个人资料” 标签，您就可以看到您的 Bright Data 账户 ID。您可以通过此链接直接访问个人资料标签：[https://www.bright.cn/cp/setting/customer\_details](https://www.bright.cn/cp/setting/customer_details)
  </Accordion>

  <Accordion title="我需要做什么才能提交 KYC？">
    为了提交 KYC，您必须使用**公司邮箱**注册 [BrightData.com](http://BrightData.com) 。像 `***@google.com` 或 `***@yahoo.com` 这样的免费邮箱**没有资格**提交 KYC。来自免费邮箱提供商的请求是不允许的，并将立即被拒绝。

    在此过程中，您将被要求提供身份证明、企业身份证明和所有权/角色证明以及您的业务用例。
  </Accordion>
</AccordionGroup>
