> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 代理产品常见问题

> 了解在集成、配置和使用 Bright Data 代理产品时的常见问题，包括 IP 类型、地理定位和错误代码。

<AccordionGroup>
  <Accordion title="什么是 zone（区域），zone 名称有多重要？">
    在 Bright Data 中，“zone（区域）”代表一个特定的产品及其配置设置。你可以将它理解为云计算中的一个实例。

    例如，你可以创建一个用于德国数据中心代理的 zone，也可以为法国数据中心代理创建一个单独的 zone。

    每个 zone 都有一个名称和一个或多个密码，用于与其交互。

    zone 名称一旦配置后就无法更改，因此你可能希望使用一个容易记住、能代表你目标的名称。请记住，你可以为 zone 添加描述，而且随时可以修改。你可以在页面顶部的 zone 名称下方找到这个描述。

    zone 名称会用于生成你的代理用户名，你也可以[根据需要自定义代理控制方式](/cn/proxy-networks/config-options)。下面是一个用于美国代理的示例用户名——你可以看到其中包含了 zone 名称：

    `brd-customer-<customer_id>-zone-<zone_name>-country-us`

    如前所述，zone 名称在保存后不能再修改——如果你想更换名称，只需创建一个新的 zone。
  </Accordion>

  <Accordion title="与第三方工具的集成">
    Bright Data 可以轻松集成到许多第三方工具中。一般来说，你只需要使用 Bright Data 产品的凭据配置一个 HTTP/HTTPS 代理即可。如果你使用的是住宅代理（Residential Proxies）、Web Unlocker API 或 SERP API，请不要忘记[使用 SSL 证书](/cn/general/account/ssl-certificate)，以确保完整的端到端加密连接。

    <Warning>
      住宅代理需要[经过 KYC 验证的企业账户](/cn/proxy-networks/residential/network-access)。部分第三方工具也无法安装 Bright Data SSL 证书，因此在这些工具中可能无法集成住宅代理。尚未完成 KYC 时，请使用 [ISP 或数据中心代理](/cn/proxy-networks/residential/network-access)。
    </Warning>

    我们已经为最常用的工具准备了详细指南，你可以在下面的列表中找到对应的链接：

    * [BrowserScan](/cn/integrations/browserscan)
    * [XLogin](/cn/integrations/xlogin)
    * [GeeLark](/cn/integrations/geelark)
    * [Puppeteer](/cn/integrations/puppeteer)
    * [Playwright](/cn/integrations/playwright)
    * [Selenium](/cn/integrations/selenium)
    * [AdsPower](/cn/integrations/adspower)
    * [Dolphin Anty](/cn/integrations/dolphin-anty)
    * [Incogniton](/cn/integrations/incogniton)
    * [Marketerbrowser](/cn/integrations/marketerbrowser)
    * [SMLOGIN](/cn/integrations/smlogin)
    * [Hidemyacc](/cn/integrations/hidemyacc)
    * [OpenBullet](/cn/integrations/openbullet)
    * [Switchyomega](/cn/integrations/switchyomega)
    * [PhantomBuster](/cn/integrations/phantombuster)
    * [BitBrowser](/cn/integrations/bitbrowser)
    * [Maskfog](/cn/integrations/maskfog)
    * [Ghost Browser](/cn/integrations/ghost-browser)
    * [Postman](/cn/integrations/postman)
    * [NGINX](/cn/integrations/nginx)
    * [StablerSOLO](/cn/integrations/stablersolo)
    * [VMLogin](/cn/integrations/vmlogin)
    * [GoLogin](/cn/integrations/gologin)
    * [Windows](/cn/integrations/windows)
    * [Scrapy](/cn/integrations/scrapy)
    * [AEZAKMI](/cn/integrations/aezakmi)
    * [Beautifulsoup](/cn/integrations/beautifulsoup)
    * [WebHarvy](/cn/integrations/webharvy)
    * [Ubuntu](/cn/integrations/ubuntu)
    * [Lalicat](/cn/integrations/lalicat)
    * [Multilogin](/cn/integrations/multilogin)
    * [Undetectable](/cn/integrations/undetectable)
    * [Apify](/cn/integrations/apify)
    * [iPhone](/cn/integrations/ios)
    * [MuLogin](/cn/integrations/mulogin)
    * [Changedetection](/cn/integrations/changedetection)
    * [Morelogin](/cn/integrations/morelogin)
    * [Proxifier](/cn/integrations/proxifier)
    * [Texau](/cn/integrations/texau)
    * [Android](/cn/integrations/android)
    * [Kameleo](/cn/integrations/kameleo)
    * [Screaming Frog](/cn/integrations/screaming-frog)
    * [Foxy](/cn/integrations/foxyproxy)
    * [SessionBox](/cn/integrations/sessionbox)
    * [Insomniac](/cn/integrations/insomniac)
    * [Helium Scraper](/cn/integrations/helium-scraper)
    * [SaleFreaks](/cn/integrations/salefreaks)
    * [Postern](/cn/integrations/postern)
    * [Antik](/cn/integrations/antik)
    * [Easync](/cn/integrations/easync)
    * [ParseHub](/cn/integrations/parsehub)
    * [Sphere Browser](/cn/integrations/sphere-browser)
    * [Octoparse](/cn/integrations/octoparse)
    * [ixBrowser](/cn/integrations/ixbrowser)
    * [Shadowrocket](/cn/integrations/shadowrocket)
    * [Firefox](/cn/integrations/firefox)
    * [Chrome](/cn/integrations/chrome)
    * [MacOS](/cn/integrations/macos)
    * [ClonBrowser](/cn/integrations/clonbrowser)
    * [Octo Browser](/cn/integrations/octobrowser)
    * [Genlogin](/cn/integrations/genlogin)
    * [Web Scraper](/cn/integrations/webscraper)

    如果你使用的工具不在列表中并且希望获得对应的指南，请联系我们！
  </Accordion>

  <Accordion title="住宅代理与移动代理的 IP 类型有哪些？">
    在住宅代理（Residential）和移动代理（Mobile）中，我们提供两种类型的 IP：

    <Tabs>
      <Tab title="Shared（共享）">
        这些 IP 会在**多个用户之间共享**。你可以连接到我们超过 [每月 4 亿+ 住宅 IP](https://www.bright.cn/proxy-types/residential-proxies) 的完整网络，并通过 Proxy Manager、浏览器扩展或原始 API 命令来在不同国家、城市或 ASN 间轮换。

        费用根据使用的流量（GB）按你的[月度套餐](/cn/general/account/billing-and-pricing/billing)计费。

        ## 地理定位（Geolocation targeting）

        分配给你的 zone 的 IP 将来自你所选择的国家、城市、ASN 或邮编。只需在下拉菜单中选择所需参数。

        <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/proxy-networks/faqs/geolocation-targeting-dropdown.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=66aec06829d865c646f89b5a3fbac791" alt="geolocation-targeting-dropdown.png" width="536" height="178" data-path="images/proxy-networks/faqs/geolocation-targeting-dropdown.png" />

        ## 使用地理定位发送请求

        * 使用共享 IP 时，你可以在发送请求时控制地理位置。
        * 若要指定特定国家，可在请求中添加 `-country` 参数。

        例如，如果你希望从美国（"us"）发出请求，请求示例如下：

        ```sh theme={null}
        curl "http://target.site" --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-country-us:<zone_password>
        ```
      </Tab>

      <Tab title="Dedicated（独享）">
        这些 IP **仅由你使用**。由于 Bright Data 的住宅网络是一个基于用户自愿加入的全球网络，Bright Data 采用 gIP（组 IP）方法来增强独享 IP 的能力。

        ## Dedicated IP groups（gIPs）

        一个 gIP 组包含 6–90 个 IP，同时共享相同属性，并针对你在 zone“配置”部分中设置的独享域名。

        <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/proxy-networks/faqs/dedicated-ip-groups.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=69fe693ea76efdfa14b83441e808df7c" alt="dedicated-ip-groups.png" width="526" height="124" data-path="images/proxy-networks/faqs/dedicated-ip-groups.png" />

        ## 地理定位

        分配给你的 zone 的 IP 将来自你所选择的国家。

        <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/proxy-networks/faqs/add-country.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=82cd90e0d741bde37507e80147c0910a" alt="add-country.png" width="514" height="112" data-path="images/proxy-networks/faqs/add-country.png" />

        ## 域名（Domains）

        定义希望独享 IP 仅用于访问的域名。对**其他任何域名**的请求将被绕过，并从我们的服务器发送。

        <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/proxy-networks/faqs/add-domains.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=34f814a87723444adfc75931067e7104" alt="add-domains.png" width="528" height="134" data-path="images/proxy-networks/faqs/add-domains.png" />

        <Note>
          不支持添加“所有域名”。未包含在列表中的域名请求将绕过超级代理（super-proxy），可能导致被封锁或通过其他代理发送。
        </Note>

        ## 使用地理定位发送请求

        你发送的请求将自动从你在 zone 配置中设定的国家发出，**无需额外添加国家参数**。例如，如果你设定的国家为美国（"us"），你可以直接使用以下语法：

        ```sh theme={null}
        curl "http://target.site" --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>:<zone_password>
        ```
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="什么是 super-proxy（超级代理）？">
    Super-proxy 是 Bright Data 的网关服务器。所有通过 Bright Data 代理平台发送的请求都会经过它们，由它们根据请求详情选择最佳 peer，并在 peer 之间平衡负载。

    在某些情况下，Bright Data 无法通过 peer 处理你的请求，此时会发生 super-proxy bypass（绕过），即请求将直接从网关服务器发送。

    当发生 super-proxy bypass 时，响应头中会包含原因说明信息。

    如果你希望阻止来自 super-proxy 的请求，可在代理用户名中添加 `-route_err-block` 参数：

    ```sh theme={null}
    curl "http://target.site" --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-route_err-block:<zone_password>
    ```
  </Accordion>

  <Accordion title="数据中心（Datacenter）的代理（IP）类型有哪些？">
    我们在[数据中心代理网络](https://www.bright.cn/proxy-types/datacenter-proxies)中提供三种类型的 IP：

    1. 共享（按使用量付费）：访问一个包含约 40,000 个轮换代理的共享池
    2. 共享无限：访问一组特定的代理，与其他用户共享，使用量无限。
    3. 专用无限：访问一组特定的代理，为您独享，使用量无限
  </Accordion>

  <Accordion title="ISP 的 IP 类型有哪些？">
    我们在[ISP 代理网络](https://www.bright.cn/proxy-types/isp-proxies)中提供三种类型的 IP：

    1. 共享（按使用量付费）
    2. 共享无限（按代理付费）
    3. 专用无限（按代理付费）

    在所有代理类型中，您可以通过区域配置或在代码/代理用户名中使用 `-country` 参数来选择代理的地理位置。

    ### 共享按使用量付费

    来自一个包含 10,000 个代理（IP 地址）池的轮换代理。代理与其他用户共享，并根据您的使用量计费：即您通过它们传输的 GB 数量。

    ### 共享无限

    一组代理，与其他用户共享，按代理付费。您购买得越多，每个代理的费用就越低。请参阅我们针对无限区域的[公平使用](/cn/general/usage-monitoring/fair_use_allowance)政策。

    ### 专用无限

    一组代理，为您独享，按代理付费。您购买得越多，每个代理的费用就越低。请参阅我们针对无限区域的[公平使用](/cn/general/usage-monitoring/fair_use_allowance)政策。
  </Accordion>

  <Accordion title="如何查找并轮换我的已分配 IP？">
    您可以在以下页面中找到您的 IP 列表：

    1. 区域概览页面：在代码示例下方有“下载”和“查看”按钮。
    2. 主区域表格：在“已分配 IP”列下方有“下载”和“查看”图标。

    在这两种情况下，按钮功能相同：

    1. “查看”按钮将允许您查看、刷新和从池中移除 IP。
    2. “下载”按钮将下载一个 CSV 文件，其中包含 `host:port:username:password` 格式的完整列表。

    我们的代理将自动轮换分配给该区域的代理，并遵守您指定的地理位置。如果您想更好地控制通过特定代理（IP）发送请求，您可以使用 `-ip` 或 `-gip` 选项。在此处阅读更多相关信息：[控制您的代理](/cn/proxy-networks/config-options#controlling-your-proxies)。对于高级代理轮换控制，您需要安装并使用 Bright Data [代理管理器](/cn/proxy-networks/proxy-manager/introduction)来路由您的请求。
  </Accordion>

  <Accordion title="如何将新代理集成到您的代码中？">
    要将代理集成到您的代码中，请访问[API 示例页面](https://www.bright.cn/cp/zones/proxy_examples)，您可以通过您的区域设置进行访问：

    <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/proxy-networks/faqs/integrate-new-proxy.gif?s=d6ff106d13eeb94ec0ef2d76bddc9103" alt="integrate-new-proxy.gif" width="1828" height="978" data-path="images/proxy-networks/faqs/integrate-new-proxy.gif" />

    在此页面上，您可以选择适用于大多数现代编码语言的集成示例，只需选择集成类型、您的代理区域、编码语言等，页面将生成一个您可以立即使用的代码片段。
  </Accordion>

  <Accordion title="如何测试我的代理是否工作？">
    要测试您的代理，请使用代理**概览**选项卡中提供的终端命令。

    复制并粘贴到您的终端。在 Windows 中，单击“开始”按钮并输入“cmd”。在 Mac 或 Linux 中，运行“终端”应用程序。然后，将代码粘贴到新窗口中。

    如果您的代理运行良好，您将在控制台上看到有关您的代理详细信息的文本。

    如果失败，您将看到一个错误代码。您可以随时将错误代码粘贴到仪表板中集成的 AI 代理中，以获取更多详细信息。
  </Accordion>

  <Accordion title="如何将代理集成到第三方软件中？">
    请查看上面提到的[API 示例](https://www.bright.cn/cp/zones/proxy_examples)页面中的一些示例（只需在“语言”下拉菜单中选择“其他软件”），或查看我们的[集成页面](/cn/integrations)，我们在其中提供了将我们的代理集成到当今业界最流行工具中的具体指南。

    **重要提示**：如果您正在使用 Bright Data 的 Web Unlocker API、住宅代理或 SERP API，您可能需要使用我们的 SSL 证书来启用端到端安全连接。请参阅[此处的说明](/cn/general/account/ssl-certificate)。
  </Accordion>

  <Accordion title="如何配置特定国家或地区的代理？">
    您可以轻松控制您发送的每个请求的地理位置。您可以按国家、州、城市、邮政编码和 ASN 选择代理。在本回答中，我们将重点介绍如何选择特定国家。

    发送请求时，您可以通过在请求中**紧跟**您的区域名称之后添加 `-country` 标志，然后加上该国家/地区的 2 个字母的 [ISO 代码](https://www.nationsonline.org/oneworld/country_code_list.htm)，使您的代理看起来位于特定国家/地区。

    如果您使用第三方工具或应用程序，只需使用配置中包含 `country-xx` 的用户名。换句话说，在需要输入代理用户名的框中，输入完整的字符串，包括国家/地区参数，例如：`brd-customer-<customer_id>-zone-<zone_name>-country-us` - 不要忘记使用您可以在“概览”选项卡中找到的自己的凭据。

    如果您使用自己的代码，请参阅以下示例：我们在请求中添加了 `-country-us`，因此我们将发送一个源自美国（“us”）的请求。

    ```sh theme={null}
    curl "[http://target.site](http://target.site)" --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-country-us: <zone_password>
    ```

    如果您将第三方应用程序与代理结合使用，您可以在软件的配置中输入包含国家/地区的用户名。

    当然，如果您使用自己编写的代码向代理发送请求，您可以轻松调整用户名以根据需要定位特定的国家/地区。

    请记住，您还可以按国家、州、城市、邮政编码和 ASN 选择代理。请参阅[此指南](/cn/proxy-networks/config-options)了解更多信息。
  </Accordion>

  <Accordion title="如何为具有固定 IP 池的区域设置默认国家/地区？">
    某些区域将为您提供访问全球大型固定 IP 池的权限。在这些区域中，您可以选择默认目标国家/地区，而无需在请求中指定国家/地区。

    选择默认国家/地区后，该区域将在每个请求中定位其中一个国家/地区。您仍然可以通过在请求中添加 `-country-xx` 标志来定位其他国家/地区，并覆盖默认的国家/地区选择。
  </Accordion>

  <Accordion title="为什么我在列表中找不到某个国家/地区？">
    Bright Data 在世界大多数国家/地区都拥有数据中心和 ISP 代理，但并非全部。我们正在不断增加新的国家/地区的数据中心。

    如果您在数据中心或 ISP 代理中找不到您要查找的国家/地区，我们建议您查看住宅代理。由于住宅代理基于拥有真实设备的真实用户，我们能够提供全球每个国家/地区的住宅代理！
  </Accordion>

  <Accordion title="如何定位欧盟地区">
    <Note>
      欧盟内部的国家/地区分配是随机的。
    </Note>

    <Info>
      适用于所有代理网络：数据中心、ISP、住宅和移动，以及我们的 Unlocker 和 SERP API
    </Info>

    您可以通过在请求中的 "country" 后面添加 "eu" 来定位整个欧盟地区（成员国），与上述“国家/地区”的方式相同：`-country-eu`

    使用 `-country-eu` 发送的请求将使用来自以下国家/地区中**随机选择的单个**国家/地区的 IP，这些国家/地区自动包含在“eu”中：

    成员国包括：奥地利、比利时、保加利亚、克罗地亚、塞浦路斯共和国、捷克共和国、丹麦、爱沙尼亚、芬兰、法国、德国、希腊、匈牙利、爱尔兰、意大利、拉脱维亚、立陶宛、卢森堡、马耳他、荷兰、波兰、葡萄牙、罗马尼亚、斯洛伐克、斯洛文尼亚、西班牙、瑞典
  </Accordion>

  <Accordion title="如何定位除中国以外的所有国家/地区？">
    在为区域分配 IP 时，在配置 UI 中的国家/地区选择部分，您可以选择“除中国外全部”选项（`All except CN`），这允许您分配来自世界各地但排除中国 IP 的代理。

    请注意，此选项仅适用于以下区域类型：

    * 数据中心/ISP - 共享 - 按代理付费
    * 数据中心/ISP - 专用
  </Accordion>

  <Accordion title="如何定位特定城市？">
    数据中心和 ISP 代理的城市定位功能已被弃用，不再可用。住宅和移动网络支持城市定位。[在此处阅读更多内容 >>](/cn/proxy-networks/faqs#where-does-bright-data-have-proxies)
  </Accordion>

  <Accordion title="Bright Data 在哪些地方提供代理？">
    Bright Data 在全球每个国家/地区提供代理，但以下国家/地区除外：

    * 伊朗
    * 伊拉克
    * 叙利亚
    * 黎巴嫩
    * 巴勒斯坦
    * 朝鲜
    * 古巴
    * 苏丹
    * 白俄罗斯
    * 俄罗斯

    如果您需要来自这些国家/地区的代理，很抱歉 Bright Data 将无法为您提供帮助。
  </Accordion>

  <Accordion title="如何查看代理事件日志？">
    事件日志将向您显示（最多）您账户中使用任何区域进行的最后 200 个请求。

    在您的 Bright Data 控制面板的代理页面中：[https://www.bright.cn/cp/zones](https://www.bright.cn/cp/zones)

    转到“事件日志”选项卡：

    <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/proxy-networks/faqs/event-log.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=5f3ac5d7e5959497491844ba43f10e7c" alt="event-log.png" width="1833" height="977" data-path="images/proxy-networks/faqs/event-log.png" />

    显示的数据包括：

    * **Date:** 请求的时间和日期
    * **Zone:** 用于请求的区域
    * **Source IP:** 发出请求的 IP
    * **URL:** 请求的目标网站
    * **Result:** 请求的成功或失败

          <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/proxy-networks/faqs/event-log-headers.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=4b8fc284481b3f221198c898418167be" alt="event-log-headers.png" width="1833" height="977" data-path="images/proxy-networks/faqs/event-log-headers.png" />
  </Accordion>

  <Accordion title="如何启用自动 IP 故障转移？（以前称为 100% 正常运行时间）">
    <Info>
      适用于数据中心和 ISP
    </Info>

    **自动故障转移(Automatic Failover)** 旨在防止任何“外部”事件影响用户。这个想法很简单，对上述两个问题的工作方式相同——如果我们的系统检测到问题，例如连接问题，或者您购买 IP 时地理位置与您要求的地理位置不完全一致的 IP，我们将自动通过与原始 IP 完全相同的其他 IP 路由您的请求。

    同时，我们希望确保必须使用特定 IP 的客户不会受到影响——因此我们做出了一些例外：

    * 如果您的请求中定位了特定的 IP，我们将不会为其分配故障转移 IP
    * 自动故障转移不会中断实时连接。如果需要故障转移，它将在下一次连接建立时生效

    **自动故障转移**通过提供 100% 连接性和持续的高性能水平带来即时价值，**免费且无需更改您的代码或工作方式。**

    <Note>
      自动故障转移功能可以通过 [API 开启或关闭](/cn/api-reference/account-management-api/Switch_100_uptime_ON_OFF_in_a_Static_zone)。
    </Note>
  </Accordion>

  <Accordion title="如何为代理启用自动故障转移？">
    导航到您的代理配置设置，并在**高级设置（Advanced settings）**下启用**“自动故障转移（Automatic failover）”**
  </Accordion>

  <Accordion title="如何在多个请求中保持使用相同的 IP？">
    * 这可以通过向代理用户名添加会话标志来实现：

    ```sh theme={null}
    brd.superproxy.io:44445 br-customer-<customer_id>-zone-<zone_name>-session-rand39484
    ```

    在线程启动时生成随机数，并在您想要更改分配给该线程连接的代理节点时更改它。

    * 会话 ID 可以是任何随机字符串/计数器：具有相同会话字符串的请求将使用相同的代理节点（尽可能长）；具有不同会话字符串的请求将被分配不同的代理节点。
    * 要强制更改 IP，只需修改会话 ID
    * 如果分配的代理节点（出口节点 IP）变得不可用，超级代理将在第一个请求返回错误“502 - 无可用节点（No peers available）”，然后在第二个请求中，即使您不更改会话 ID，超级代理也会分配一个新的节点。
    * 会话 IP 最多可保持 7 分钟的空闲时间。7 分钟内没有请求后，IP 将被释放回池中。
      为了更长时间地保持此会话/IP，请发送一个不超过 7 分钟的微小保持活动请求，以防止此会话空闲超过 7 分钟。
      此请求可以是任何小的东西，例如 `/favicon.ico`，甚至是返回 404 的请求（只要网络服务器不因该请求而断开套接字）。
    * 如果您有多个客户端并希望忽略您的客户端源 IP（与您的会话 ID 一起用于创建会话），那么您想使用全局会话，然后将 `glob_` 作为前缀添加到您的会话中：

    ```sh theme={null}
    brd-customer-<customer_id>-zone-<zone_name>-session-glob_rand39484
    ```

    完整请求示例：

    ```sh theme={null}
    brd-customer-CXXXXX-zone-ZONE_X-session-glob_rand39484
    ```

    在线程启动时生成随机数，并在您想要更改分配给该线程连接的代理节点时更改它。
  </Accordion>

  <Accordion title="我在哪里可以找到我的代理地址和端口？">
    您可以在您配置的代理内的“概览（Overview）”选项卡中找到您的代理地址和端口。

    为此，请单击“我的区域（my zones）”，然后单击您需要的代理所在行。

    在“概览”选项卡中，您还可以复制您的代理列表、下载它、刷新您的代理等。
  </Accordion>

  <Accordion title="如何设置 IP 和域名的允许列表/拒绝列表？">
    将您的 IP 列入 **允许列表(allowlist)** 是保持账户安全的好方法，因为即使其他人拥有您的用户名和密码，这也阻止了他们访问您的代理。

    当您将某个 IP 列入允许列表时，只有该 IP 才能向您的代理发送请求。一旦此列表中存在单个 IP，所有其他 IP 将无法再访问该区域的代理并将被阻止。

    从允许列表中的 IP 进行访问仍然需要您提供区域的用户名和密码才能访问该区域的代理。

    允许列表不会影响对 Bright Data 控制面板的访问：它仅限制对代理的访问。

    将 IP 添加到区域的拒绝列表/允许列表有 2 种方式：

    * 通过控制面板：

          <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/proxy-networks/faqs/whitelist-blacklist.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=71d845b5fdcf78f37e13767cea788313" alt="whitelist-blacklist.png" width="557" height="490" data-path="images/proxy-networks/faqs/whitelist-blacklist.png" />

      添加所有相关的 IP 和域名，您将允许它们使用您的代理区域进行访问。

      * 转到您的任何区域设置，然后单击“配置（Configuration）”选项卡。
      * 向下滚动到“安全设置（Security settings）”部分，它们分别负责 IP 和域名的允许/拒绝列表：
    * **通过 API 端点：**
      * [将 IP 添加到区域允许列表](/cn/api-reference/account-management-api/allowlist-ip)
      * [将 IP 从区域允许列表中移除](/cn/api-reference/account-management-api/remove-ip-from-zone-allowlist)
      * [将 IP 添加到区域拒绝列表](/cn/api-reference/account-management-api/denylist-ip)
      * [将 IP 从区域拒绝列表中移除](/cn/api-reference/account-management-api/remove-ip-from-zone-denylist)
      * [将域名从区域允许列表/拒绝列表中移除](/cn/api-reference/account-management-api/remove-domain-from-zone-allowlist-or-denylist)
      * [将域名添加到区域允许列表/拒绝列表](/cn/api-reference/account-management-api/allowlist-or-denylist-domains)

    #### 关于允许列表的重要提示：

    * 添加域名的示例：

          <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/proxy-networks/faqs/domain-add-example.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=85101978c1c88aa75143d767ca4096ac" alt="domain-add-example.png" width="376" height="112" data-path="images/proxy-networks/faqs/domain-add-example.png" />
    * 添加 IP 的示例：

          <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/proxy-networks/faqs/ip-add-example.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=6c561db8d8b1bf536ea69f8f11c15a10" alt="ip-add-example.png" width="222" height="82" data-path="images/proxy-networks/faqs/ip-add-example.png" />
    * 应该列入允许列表的 IP 是**您**将用于发送请求的机器的 IP，**而不是**您区域中的代理 IP。
    * 我们**强烈建议**在可能的情况下将您的 IP 列入允许列表，因为当允许列表为空时，如果我们的自动安全阻止系统检测到任何异常活动，您的未列入允许列表的 IP 可能会被暂时阻止，从而带来风险。请参阅[此视频](https://www.bright.cn/static/video/howto/blacklist_system_explanation.mp4?md5=153602994-22bce32a\&hver=2)了解更多信息。
    * 您可以添加到允许列表的 IP/域名数量**没有限制**，我们也支持 IP 范围。
  </Accordion>

  <Accordion title="如何查看支持的端口和协议？">
    #### HTTP 和 HTTPS 协议

    协议 `HTTP` 和 `HTTPS` 默认支持。

    #### SOCKS5 协议

    Bright Data 支持 `SOCKS5` 协议，默认分配端口 22228 用于 SOCKS5 通信。

    SOCKS5 支持所有 Bright Data 的代理网络：数据中心、ISP、住宅和移动。

    有关 [完整的 SOCKS5 配置说明](/cn/proxy-networks/socks5)，请参阅此处。

    #### 目标端口

    我们区分两种端口：Bright Data 代理和抓取服务端口，以及在定位主机（网站）时使用的特定端口。此常见问题解答指的是**目标端口**；即代理节点应与目标网站通信所使用的端口。

    在所有区域中，端口 80 和 443 默认可用，用于 HTTP 和 HTTPS 协议。

    在数据中心或 ISP 类型的代理区域中，所有高于 1024 的端口默认支持。

    在住宅或移动类型的代理区域中，以下端口将默认可用：8080、8443、5678、1962、2000、4443、4433、4430、4444 和 1969。

    Bright Data 可以应请求支持额外的端口。每个要求支持新端口的请求都将伴随与 Bright Data 合规团队的专门额外合规流程。
    需要 Bright Data 合规审核才能激活的端口示例：

    要发起将端口权限添加到您的区域的请求：

    * 转到您的区域设置（默认情况下将打开“配置”选项卡，如果不是，请单击它）
    * 向下滚动到“高级选项（advanced options）”并单击它
    * 启用“端口（ports）”
    * 输入您希望获得批准的端口号
    * 填写表格并等待我们的合规团队与您联系并批准请求

          <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/proxy-networks/faqs/add-ports.gif?s=f9a6ec418a18d21e107a604507aaf4c3" alt="add-ports.gif" width="1828" height="978" data-path="images/proxy-networks/faqs/add-ports.gif" />
  </Accordion>

  <Accordion title="如何定位特定操作系统？">
    Bright Data 允许定位以下**操作系统（Operating Systems）**：

    <CodeGroup>
      ```sh Windows theme={null}
        curl --proxy-user brd-customer-<customer_id>-zone-<zone_name>-os-windows:<zone_password> --proxy brd.superproxy.io:44445 "<target_site>"
      ```

      ```sh macOS theme={null}
        curl --proxy-user brd-customer-<customer_id>-zone-<zone_name>-os-osx:<zone_password> --proxy brd.superproxy.io:44445 "<target_site>"
      ```

      ```sh Android theme={null}
        curl --proxy-user brd-customer-<customer_id>-zone-<zone_name>-os-android:<zone_password> --proxy brd.superproxy.io:44445 "<target_site>"
      ```
    </CodeGroup>
  </Accordion>

  <Accordion title="如何刷新分配给您的区域的 IP？">
    如果您在区域配置中选择了“按 IP 付费”共享或专用 IP 类型，您将被分配一个固定的 IP 地址。有时，根据您的用例，您可能需要刷新这些 IP 地址。

    要刷新分配给您区域的 IP，请导航到您选择的区域，在 **“已分配 IP（Allocated IPs）”**下单击 **“显示已分配 IP（Show allocated IPs）”**，**选中**您希望刷新的 IP 或 gIP 旁边的**复选框**，然后单击 **“刷新（Refresh）”**

    <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/proxy-networks/faqs/refresh-ips.gif?s=fef981f0b4c45b5e28e0f0f66794da23" alt="refresh-ips.gif" width="1892" height="868" data-path="images/proxy-networks/faqs/refresh-ips.gif" />

    <Note>
      刷新 IP 或 gIP 将产生额外费用。
    </Note>

    或者，您可以使用 API 刷新您的[专用住宅 IP](/cn/api-reference/account-management-api/Refresh_dedicated_residential_IPs) 或您的[数据中心/ISP IP](/cn/api-reference/account-management-api/Refresh_Static_Datacenter_ISP_IPs)
  </Accordion>

  <Accordion title="如何使用特定的 IP？">
    使用 Bright Data 的住宅代理网络时，您可能需要使用分配给您区域的特定 IP。

    1. **发送一个测试请求**，并添加 `--verbose` 或 `-v` 选项（这将开启详细日志记录）

    ```sh theme={null}
    curl "[https://brdtest.com/myip.json](https://brdtest.com/myip.json)" --verbose --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>:<zone_password>
    ```

    1. **找到** `x-brd-ip` 响应标头并复制其值

           <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/proxy-networks/faqs/x-brd-ip.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=4a8f34a47da1aac1576d8ecc9aafed16" alt="x-brd-ip.png" width="423" height="23" data-path="images/proxy-networks/faqs/x-brd-ip.png" />

    2. **在**您的区域名称之后，在请求中**添加** `-ip-` 标志，并使用上一步中复制的**哈希 IP 值**

    3. 发送一个测试请求，并**查看响应**

    ```sh theme={null}
    curl "[https://brdtest.com/myip.json](https://brdtest.com/myip.json)" --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-ip-<hashed-ip>:<zone_password>
    ```

    我们建议使用 `https://brdtest.com/myip.json` 作为测试的目标域名，并查看您的 IP 凭据。
  </Accordion>

  <Accordion title="如何定位特定 ASN 的 IP？">
    此功能可以通过在**地理定位 (Geolocation Targeting)** 下，向您的区域配置添加 ASN 参数来启用。

    <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/proxy-networks/faqs/asn-targeting.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=78916db58402711b9ad0b8b9ee29747f" alt="asn-targeting.png" width="583" height="931" data-path="images/proxy-networks/faqs/asn-targeting.png" />

    配置保存后，ASN 标志可以添加到区域的凭据中，并在使用住宅代理时进行集成。例如：

    ```sh theme={null}
    curl --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-asn-<asn-number>:<zone_password> "<target_site>"
    ```

    **注意：** ASN 号码的值可以在[这里](https://bgp.potaroo.net/cidr/autnums.html)找到。
  </Accordion>

  <Accordion title="如何定位住宅 IP 组 (gIP)？">
    专用住宅 IP 可以以 [gIP](cn/proxy-networks/residential/configure-your-proxy#ip-groups-gips) 的形式选择。可以通过在区域配置页面中选择“专用（Dedicated）”IP 类型并选择 gIP 的数量来分配它们。同时需要定位特定的域名。

    <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/proxy-networks/faqs/number-of-dedicated-gIPs.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=5066fce4640fbb09ea33700160207c24" alt="number-of-dedicated-gIPs.png" width="839" height="1238" data-path="images/proxy-networks/faqs/number-of-dedicated-gIPs.png" />

    配置保存后，选择“显示已分配专用住宅 IP（Show allocated Dedicated residential IPs）”将提供代表组 IP 的哈希值列表。

    <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/proxy-networks/faqs/show-allocated-dedicated-ips.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=9228edecff61a348346d2456541bb9cd" alt="show-allocated-dedicated-ips.png" width="583" height="393" data-path="images/proxy-networks/faqs/show-allocated-dedicated-ips.png" />

    这些值可用于定位特定的 gIP。例如：

    ```sh theme={null}
    curl --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-gip-<gip_hash_value>:<zone_password> "<target_site>"
    ```
  </Accordion>

  <Accordion title="如何在控制面板中查看代理产品的使用统计信息">
    有两种方式可以跟踪使用情况：

    #### 代理仪表板

    在此处访问主代理仪表板：[https://www.bright.cn/cp/zones/dashboard](https://www.bright.cn/cp/zones/dashboard)

    * 按网络划分的数据使用量：显示所选时间范围内每个代理产品的总带宽和请求数量。
    * 使用概览：显示一个图表，您可以在其中选择时间范围、数据点（带宽、请求、每个请求的平均带宽），并按区域、产品或目标域进行筛选。您还可以使用“比较到（Compare to）”选项比较不同时间范围内的使用情况。

    #### 区域概览页面

    * 在区域“概览（Overview）”部分，您可以查看特定区域的统计信息，并可选择比较时间范围、选择数据点（带宽、请求、每个请求的带宽），并在图表下方的表格中查看其他指标。
  </Accordion>

  <Accordion title="如何使用中国住宅 IP 浏览中文网站">
    **在中国境外时**
    定位中国住宅 IP 节点就足够了：

    ```sh theme={null}
    curl --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-country-cn:<zone_password> "<target_site>"
    ```
  </Accordion>

  <Accordion title="特定运营商的代理节点 IP">
    * 您可以选择使用此列表中的特定运营商：

    ```
    a1, aircel, airtel, att, celcom, chinamobile, claro, comcast, cox, digi, 
    dt, docomo, dtac, etisalat, idea,  meo, mtn, mtnza, 
    optus, orange, qwest, reliance_jio, robi, sprint, telefonica, telstra, 
    tmobile, tigo, tim, verizon,  vodacomza, vodafone, vivo, zain,
    vivabo, telenormyanmar, kcelljsc, swisscom, singtel, asiacell, windit, 
    cellc, ooredoo, drei, umobile, cableone, proximus, mobitel, o2, 
    bouygues, free, sfr, digicel
    ```

    * 例如

    <CodeGroup>
      ```sh Deutsche Telekom theme={null}
      brd-customer-<customer_id>-zone-<zone_name>-carrier-dt
      ```

      ```sh Sprint theme={null}
      brd-customer-<customer_id>-zone-<zone_name>-carrier-sprint
      ```
    </CodeGroup>
  </Accordion>

  <Accordion title="关于地理定位数据库，以及如何检查代理 IP 信息？">
    地理定位数据库（GeoDB）被互联网网站用于查询用户使用的 IP 地址信息。Bright Data 监控和维护 MaxMind GeoDB 的正确记录。

    还有许多其他较小的 GeoDB，其中大多数使用过时记录或有缺陷的测试方法，因此它们提供的信息不准确，或者旨在引诱其观看者购买他们的 VPN 或代理产品。

    为了查看我们关于您正在使用的代理 IP 的信息，请使用以下链接：[https://geo.brdtest.com/mygeo.json](https://geo.brdtest.com/mygeo.json)
  </Accordion>

  <Accordion title="哪种 Bright Data 产品最适合抓取搜索引擎（SERP）？">
    #### 对于单步抓取：

    [SERP API](/cn/scraping-automation/serp-api/introduction) 是针对 SERP 的理想产品，因为它具有保证的成功率（仅按成功付费），并具有主动解锁、自动选择最佳代理、自定义标头、指纹识别、解决 CAPTCHA 等功能。

    #### 对于多步抓取 (playwright/puppeteer/selenium)：

    [浏览器 API](/cn/scraping-automation/scraping-browser/introduction) 是理想的产品，因为它是我们完全云托管的浏览器，旨在帮助您轻松专注于多步数据收集，同时我们为您处理完整的代理和解锁基础设施，包括 CAPTCHA 解决。
  </Accordion>

  <Accordion title="我可以通过住宅、数据中心或 ISP 代理网络定位 Google SERP 吗？">
    **住宅代理** - 否，[SERP API](/cn/scraping-automation/serp-api/introduction) 是针对 SERP 的理想产品，因为它具有保证的成功率（仅按成功付费），并具有主动解锁、自动选择最佳代理、自定义标头、指纹识别、解决 CAPTCHA 等功能。通过住宅网络定位 Google SERP 将导致超级代理绕过，这将导致请求从我们的服务器而不是节点发送。

    **数据中心和 ISP 代理** - 否。当试图通过这些代理网络中的任何一个专门定位 Google 时，您的请求将被拒绝，并且您将在响应标头中收到以下错误消息：

    ```
    HTTP/1.1 403 Search engine host is not allowed
    X-Luminati-Error: Forbidden: This target URL isn't supported on proxy networks, use the SERP API product for targeting this URL. You may contact your account manager or open a support ticket for assistance
    ```
  </Accordion>

  <Accordion title="住宅和移动网络">
    通过住宅或移动网络定位搜索引擎时，请求不会通过住宅或移动节点，而是直接通过我们的一个超级代理发送。这种行为的原因是为了支持住宅和移动网络与浏览器的集成，浏览器可能需要从目标网站加载搜索引擎资源端点。

    **如果您使用住宅或移动网络定位搜索引擎域，请求将直接通过超级代理传递，以下响应标头将作为指示：**

    ```sh theme={null}
    x-luminati-ip: superproxy bypass
    ```
  </Accordion>

  <Accordion title="我可以向 IP 而非域名发送请求吗？">
    否 - 在使用 Bright Data 时，禁止直接向主机服务器而非域名发送请求。
    使用 `1.1.1.1:443` 等 URL 格式的请求将使用超级代理服务器执行，而不是代理节点 IP。

    使用超级代理的请求示例：

    <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/proxy-networks/faqs/x-luminati-ip.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=5023c43edf48fe823839513027a59769" alt="x-luminati-ip.png" width="1431" height="891" data-path="images/proxy-networks/faqs/x-luminati-ip.png" />
  </Accordion>

  <Accordion title="我可以使用端口 25 或任何其他 SMTP 端口，或使用代理 IP 发送电子邮件吗？">
    由于 Bright Data 关注我们的社区和节点质量，可能用于发送垃圾邮件的 SMTP 请求被阻止。请注意，邮件域的访问也被阻止，对邮件域的请求将从超级代理服务器发送，而不是节点 IP。
  </Accordion>

  <Accordion title="Bright Data 是否支持 Socks5 协议">
    是的。Bright Data 支持 `SOCKS5` 协议，默认分配端口 22228 用于 SOCKS5 通信。

    有关 [完整的 SOCKS5 配置说明](/cn/proxy-networks/socks5)，请参阅此处或访问 [SOCKS5 代理页面](https://www.bright.cn/solutions/socks5-proxies)。
  </Accordion>

  <Accordion title="我如何控制请求从哪里执行？">
    * 您可以选择直接从超级代理执行请求而不是从节点 IP 执行。在这种情况下，请求的 IP 将是超级代理的 IP。您需要在请求授权字符串中添加 **'-direct'**。`brd-customer-<customer_id>-zone-<zone_name>-direct`
  </Accordion>

  <Accordion title="如何刷新会话（IP）？">
    长时间使用相同的 IP 会使目标网站更容易将该 IP 标记为代理，并可能使您的请求更容易被目标网站检测到。刷新您的 IP 将导致从 Bright Data 分配新的 IP 来替换您池中现有的 IP，从而使您能够控制您的 IP 池并获得更高的成功率。
  </Accordion>

  <Accordion title="如何使用中国住宅 IP 浏览中文网站？">
    无需特殊设置，只需在您的凭据中使用 `country-cn` 标志
  </Accordion>

  <Accordion title="如何长时间使用相同的 IP 以及我可以保持多久？ (长会话)">
    如果您希望长时间保持相同的 IP 以用于基于会话的用途，您有以下选项：

    * 使用 `-ip` 标志定位特定的 IP：在您的区域 IP 池中查看您的代理列表（可以在控制面板的区域“概览”选项卡中找到），选择一个 IP 并使用 `-ip` 标志定位它。这将把您的所有请求路由到同一个 IP。只要该 IP 分配给您的区域，您就可以一直使用它。
    * 保持相同的会话 IP：通过使用 `-session-<SESSION_ID>` 标志，您的请求将被路由到相同的 IP。为了确保相同的 IP 保持绑定到您的会话 ID，您需要确保会话空闲时间不超过 7 分钟。您可以同时拥有多个并行会话 - 每个会话分配一个不同的 IP。

    可选：通过使用[代理管理器](/cn/proxy-networks/proxy-manager/introduction)，您可以使用[长单会话（long single session）](/cn/proxy-networks/proxy-manager/configuration#presets)预设，它将自动定期发送虚拟请求，以确保 IP 保持分配。

    <Note>
      对于住宅/移动区域，IP 是真实用户设备的 IP，因此只能在用户设备处于空闲状态时使用（即设备已连接到互联网、有足够的电池电量且用户当前未在使用它）。如果 IP 变得不可用，我们的系统将自动为您分配另一个可用的住宅 IP，其类型和地理位置与您使用的 IP 相同。
    </Note>

    有关更多说明和示例，请参阅以下文章：[https://docs.brightdata.com/cn/proxy-networks/config-options#controlling-your-proxies-rotation](https://docs.brightdata.com/cn/proxy-networks/config-options#controlling-your-proxies-rotation)
  </Accordion>

  <Accordion title="错误代码 502 是什么？">
    HTTP 错误代码 502 表示“错误网关（Bad Gateway）”。当您向 URL 发送请求时，如果该 URL 的服务器从其依赖的另一个服务器接收到无效响应以完成请求，则会发生此错误。

    Bright Data 使用 HTTP 标头来显示有关 HTTP 错误的其他信息，这有助于识别根本原因并解决问题。

    查看我们的[错误目录](/cn/proxy-networks/errorCatalog#http-error-502)以了解 HTTP 错误 502 的原因。
  </Accordion>

  <Accordion title="错误代码 403 是什么？">
    HTTP 403 响应代码表示您被禁止访问**有效**的 URL。服务器理解请求，但由于客户端问题无法完成请求。

    Bright Data 使用 HTTP 标头来显示有关 HTTP 错误的其他信息，这有助于识别根本原因并解决问题。

    查看我们的[错误目录](/cn/proxy-networks/errorCatalog#http-error-403)以了解 HTTP 错误 403 的原因。
  </Accordion>

  <Accordion title="为什么我会收到 SSL 错误？ (ERR_CERT_AUTHORITY_INVALID)">
    如果您尝试使用住宅或移动代理网络，并遇到以下错误之一或与之类似的错误：

    * `net::ERR_SSL_PROTOCOL_ERROR`
    * `ERR_INVALID_CERT`
    * `Error: self-signed certificate in certificate chain`
    * `ERROR: No matching issuer found`
    * `NET::ERR_CERT_AUTHORITY_INVALID`
    * `SSL: CERTIFICATE_VERIFY_FAILED`

    这意味着您正在通过 HTTPS 使用住宅或移动网络，并且没有正确处理 SSL 验证。

    有关住宅网络访问和 KYC 的更多信息，请参见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。

    **如何解决 SSL 错误？**

    您有以下选项：

    * 使用 API 访问而不是原生代理访问：如果您是通过编程方式连接，则应考虑通过 API 方法连接 - 这会在幕后为您处理 SSL 证书：[API 访问与原生代理访问](/cn/api-reference/authentication)
    * 完成客户身份验证 (KYC) 流程，该流程需要大约 2-3 个工作日来处理 - 之后您将能够以最小的限制使用住宅/移动网络，这也解决了 SSL 错误。

      要完成 KYC 流程，请填写 [KYC 表格](https://www.bright.cn/cp/kyc)
    * 根据我们的 [SSL 证书安装指南](/cn/general/account/ssl-certificate)安装 Bright Data SSL 证书（请注意，对于某些特定的集成方法，由于不支持，可能无法安装 SSL 证书）

          <Note>
            此解决方案可能不受某些第三方代理工具（例如 GoLogin、MultiLogin）支持。
          </Note>
    * 如果您是通过代码（NodeJS、Python、C# 等）或控制台使用我们的代理，您可以完全忽略 SSL 验证，这解决了所有 SSL 验证错误。我们在 [SSL 证书文档页面](/cn/general/account/ssl-certificate)上提供了有关如何执行此操作的示例。
    * 使用不同的产品：您可以改用不同的产品，例如数据中心或 ISP 代理，而不是住宅代理，这些产品不需要“特殊权限”（KYC）。您可以将其作为临时措施，直到您的 KYC 表格获得批准。
  </Accordion>

  <Accordion title="如何将 `curl` 输出重定向到文件？">
    在抓取大文件或为了记录 `curl` 输出时，您可能希望将输出重定向到文件。为此，请在您的 `curl` 命令选项中添加 `--output [filename]`。
  </Accordion>

  <Accordion title="如何允许/阻止我的区域定位特定域名？">
    您可以通过在区域内进行简单的配置，允许或阻止特定域名来控制访问。请遵循以下步骤来管理域名访问：

    1. 访问[区域页面](https://www.bright.cn/cp/zones) 前往您仪表板中的区域页面。
    2. 选择您想要的区域 选择您希望配置域名访问的区域。
    3. 导航到“配置”选项卡 进入您选择的区域后，找到“配置（Configuration）”选项卡，然后向下滚动到“安全选项（Security Options）”。
    4. 允许或阻止域名
       * 要允许特定域名，请将它们添加到“允许的目标主机（Allowed Target Hosts）”中。
       * 要阻止特定域名，请将它们添加到“阻止的目标主机（Blocked Target Hosts）”中。
    5. 域名通配符选项
       * 根域名包含：添加根域名（例如：`example.com`）将自动包含其所有子域名（例如：`sub.example.com`）。
       * 通配符使用：利用 `*` 通配符来覆盖所有子域名和后缀变体。例如，添加 `example.*` 将包括 `sub.example.*` 和各种域名后缀，如 `example.com`、`example.co.uk` 等。

    <Tip>
      这些配置为您管理代理区域的域名级别访问提供了灵活性，确保安全和受控的连接。
    </Tip>
  </Accordion>

  <Accordion title="如何定位政府网站？">
    Bright Data 政策允许在通过 KYC 流程后定位政府网站。[阅读有关 KYC 流程的更多信息](/cn/proxy-networks/residential/network-access#kyc-verification)。
  </Accordion>

  <Accordion title="为什么我收到关于 robots.txt 的错误？">
    `robots.txt` 是网站所有者用于定义自动化系统可以访问其网站哪些区域的文件。在住宅网络上，Bright Data 遵守这些规则以确保道德合规。对被阻止区域的请求将返回 502 Residential Failed (`bad_endpoint`) 错误。

    要解决这些错误，您可以选择以下解决方案之一：

    * 与 Bright Data 合规团队及时更新您的 KYC 使用案例，使已批准的住宅访问覆盖您要定位的网站。住宅访问需要 KYC 批准。要开始或查看此流程，请参阅：[https://www.bright.cn/cp/kyc](https://www.bright.cn/cp/kyc)
    * 使用我们的其他不需要 KYC 验证的产品，例如 ISP 和数据中心代理。
    * 避免导航到网站在 `robots.txt` 文件中阻止的网络路径。

    有关更多信息，请参阅以下文章：[https://docs.brightdata.com/cn/proxy-networks/residential/network-access](https://docs.brightdata.com/cn/proxy-networks/residential/network-access)
  </Accordion>

  <Accordion title="你们提供 IPv6 代理吗？我如何获得 IPv6 代理？">
    我们将考虑向选定的客户提供 IPv6 代理。有关咨询事宜，请联系我们：[support@brightdata.com](mailto:support@brightdata.com)
  </Accordion>

  <Accordion title="如何理解我收到某个特定错误的原因？" defaultOpen="false">
    要尝试理解您在使用我们的代理网络时遇到特定错误的原因，您应该尝试重现遇到错误的相同请求，并通过 CMD/BASH 上的 cURL 或其他 HTTP 请求服务（如 Postman）发送它。

    在发送请求时，请确保在请求中附加 `-v` 或 `-verbose` 标志（对于 cURL），这将确保您收到包含有关错误来源的重要信息的响应标头，并将指导您找到解决方案。

    如果响应标头包含 `x-brd-`，则错误源于 Bright Data，您应该查看[Bright Data 错误目录](/cn/proxy-networks/errorCatalog)以获取进一步建议。

    否则，则不是我们方面的问题 - 您应该查看有关[网站阻止](/cn/proxy-networks/website-blocking)的文章。

    错误也可能源于您的集成问题，您应该检查您是否正确集成了，有关集成的帮助 - 请参阅我们的[集成部分](/cn/integrations/introduction)。
  </Accordion>

  <Accordion title="Bright Data 是否有任何请求限制？" defaultOpen="false">
    Bright Data 允许大规模的代理访问和操作，我们不强制执行全局请求限制（也称为“速率限制”），但我们会监控客户的使用情况 - 如果使用量超过正常行为，我们会发出警报。我们会保护我们的代理网络，如果请求速率过高，您将收到 HTTP 错误 429（[在此处查看错误描述和故障排除](/cn/proxy-networks/errorCatalog#http-error-429)）。

    我们监控一般请求流入以及**每个代理（IP）的请求数量**，如果发现特定代理 IP 过载，我们可能会限制它并返回带有特定错误消息的 HTTP 错误 429，指示此类情况。您将被要求添加更多 IP 或减少负载。

    我们强烈建议，在遇到速率限制错误（HTTP 错误 429）时，检查您的轮换逻辑（如果您明确指的是代理 IP）- 您可能一直使用请求定位一组特定的 IP，而让其他 IP 未被使用。
  </Accordion>

  <Accordion title="为什么我无法使用代理访问（被阻止的）google, bing.com, youtube.com？" defaultOpen="false">
    作为 Bright Data 政策的一部分 - 当用户尝试使用我们的常规代理访问 `google.com`、`youtube.com`、`bing.com` 和少数其他选定域名时，我们会执行阻止或[超级代理绕过](/cn/proxy-networks/faqs#what-is-a-super-proxy)。如果您希望抓取 Google 搜索结果数据或 `youtube.com`，请改用 [SERP API](/cn/scraping-automation/serp-api/introduction) 或 Web Unlocker API。
  </Accordion>

  <Accordion title="为什么我在检查代理 IP 时获得错误的地理定位？" defaultOpen="false">
    当您通过第三方 IP 检查网站检查您的 Bright Data 代理 IP 位置和详细信息时，您可能会在结果中收到“错误”的地理定位，这可能是由于两个主要原因：

    * 地理定位数据库：地理定位数据库（GeoDB）被互联网网站用于查询用户使用的 IP 地址信息。Bright Data 监控和维护 MaxMind GeoDB 的正确记录。还有许多其他较小的 GeoDB，其中大多数使用过时记录或有缺陷的测试方法，因此它们提供的信息不准确，或者旨在引诱其观看者购买他们的 VPN 或代理产品。
    * 超级代理绕过：对于第三方 IP 检查器，我们可能会执行超级代理绕过而不是完全阻止请求，这样做是为了保持我们 IP 的声誉。当发生这种情况时，您可能会看到我们超级代理的位置，而不是您的代理节点的位置。不用担心 - 对于其他常规网站，将使用您的真实代理节点。[什么是超级代理绕过？](/cn/proxy-networks/faqs#what-is-a-super-proxy)

    为避免此类问题，请仅使用我们的官方 IP 检查网站，它将向您显示准确的信息：[https://geo.brdtest.com/mygeo.json](https://geo.brdtest.com/mygeo.json)
  </Accordion>

  <Accordion title="如何在 IP:PORT 格式中使用 Bright Data 代理？" defaultOpen="false">
    Bright Data 代理原生支持行业标准格式：`IP/HOST:PORT:USERNAME:PASSWORD`。如果您的集成方法不支持此格式，并且只需要 `IP:PORT`，您可以使用 **Bright Data 代理管理器（Proxy Manager）**—一个免费的开源工具，允许您使用 `IP:PORT` 格式路由请求到我们的代理。

    有关配置代理管理器以进行此设置的更多详细信息，请参阅我们的指南：[端口定位配置](/cn/proxy-networks/proxy-manager/configuration#port-targeting)
  </Accordion>

  <Accordion title="为什么我的 IP 地址被添加到区域拒绝列表？" defaultOpen="false">
    #### 处理您账户上的 IP 限制

    如果我们的系统检测到源自您某个区域的特定 IP 地址的异常或可疑活动，我们的自动化安全措施将拒绝列出该 IP 以保护您的账户。虽然此系统有效地阻止了大多数恶意活动，但它偶尔可能会阻止合法的用户，导致 `ip_forbidden` 错误消息。

    #### 如何解决此问题

    如果您遇到此错误，可以通过以下方式快速解决：

    1. 转到仪表板中的“代理和抓取（Proxy & Scraping）”选项卡
    2. 导航到列表中受影响的区域
    3. 在配置面板中选择“安全设置（Security Settings）”
    4. 找到“IP 允许列表（IP allowlist）”选项
    5. 将您当前机器的 IP 地址添加到允许列表

    一旦您的 IP 被允许列入该区域，您将立即重新获得对服务的访问权限。
  </Accordion>

  <Accordion title="如何获取您的 Bright Data 连接信息？">
    ### 您的代理访问信息

    Bright Data 代理分组在“代理区域（Proxy zones）”中。每个区域都包含其所持有的代理的配置。

    要获取对代理区域的访问权限：

    1. 登录 Bright Data 控制面板
    2. 选择代理区域或设置一个新的区域
    3. 单击新区域名称，然后选择\*\*概览（Overview）\*\*选项卡。
    4. 在“概览”选项卡中，在\*\*访问详细信息（Access details）\*\*下，您可以找到代理访问详细信息，并在单击时将其复制到剪贴板。
    5. 您将需要：代理主机（Proxy Host）、代理端口（Proxy Port）、代理区域用户名（Proxy Zone username）和代理区域密码（Proxy Zone password）。
    6. 单击复制图标以将文本复制到剪贴板，并粘贴到您的工具的代理配置中。

    ### 访问详细信息部分示例

    <Frame>
      <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/proxy-networks/data-center/configure-your-proxy/your-proxy-list.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=31997c6595461a3b94ce0c4f8b873cd4" alt="your-proxy-list" width="1465" height="607" data-path="images/proxy-networks/data-center/configure-your-proxy/your-proxy-list.png" />
    </Frame>

    ### 住宅代理访问

    要访问 Bright Data 的**住宅代理（Residential Proxies）**，您需要通过我们的合规团队验证，或安装证书。[阅读更多...](/cn/proxy-networks/residential/network-access)

    ### 定位搜索引擎？

    如果您定位像 Google、Bing 或 Yandex 这样的搜索引擎，您需要一个特殊的搜索引擎结果页面（**SERP**）代理 API。使用 Bright Data SERP API 来定位搜索引擎。[点击此处阅读有关 Bright Data SERP 代理 API 的更多信息。](/cn/scraping-automation/serp-api/introduction)

    ### 避免在您的工具中出现 `PROXY ERROR`

    有些工具使用搜索引擎作为代理的测试目标：如果您的代理测试失败，这可能是原因。确保您的测试域名不是搜索引擎（这在工具配置中完成，不受 Bright Data 控制）。
  </Accordion>

  <Accordion title="Bright Data 代理是否支持 HTTP3？" defaultOpen="false">
    是的。我们向选定的客户提供使用我们支持 HTTP3 协议的高级高性能代理网络。这是对我们的企业级客户的有限优惠：要将 HTTP3 用于您的抓取操作，请联系您的 Bright Data 客户经理。
  </Accordion>

  <Accordion title="使用 Bright Data 代理网络使用 HTTP3 我需要了解什么？" defaultOpen="false">
    ### 我如何知道我的目标域是否支持 HTTP3？

    您可以通过发送 `curl` 请求并检查响应标头中是否存在 `alt-svc` 标头来判断您的目标域是否在宣传 HTTP3。如果响应中存在此标头，则表示该域提供通过 HTTP3 的访问。

    ```
    curl -k -i https://[my target website]
    ```

    或者，您可以检查 [https://http3check.net/](https://http3check.net/) 或类似的网站。

    ### 我可以使用我安装的 `curl` 通过 HTTP3 查询吗？

    是的 - 但您需要一个专门构建的、支持 `HTTP3` 的 `curl` 实用程序。大多数流行的 `curl` 版本不支持 `HTTP3`。

    ### 为什么我应该使用 HTTP3？

    一些网站期望 HTTP3 流量；因此，通过使用目标预期的协议访问，您可能会体验到更顺畅、不被阻止的访问。对于某些用例，HTTP3 访问速度比 HTTP2 快，因此您的吞吐量可能会更高。

    ### 我是否需要在我的代理上执行特殊设置？

    否。Bright Data 提供的所有代理都可以中继 HTTP3 流量，无需特殊设置或修改。

    ### 我是否需要修改我的操作或访问以使用 HTTP3？

    请咨询您的 IT、网络和安全管理员，以在您的网络上启用 HTTP3。可能需要一些网络或防火墙设置来允许此流量从/流向您的组织的网络。

    ### 我如何查看我的 Chrome 浏览器是否正在利用 HTTP3 进行流量传输？

    以开发模式打开您的 Chrome 浏览器，并打开“网络（network）”选项卡。在 `protocol` 列中，如果您看到 `h3`，则表示请求正在通过 HTTP3 发送和接收。

    ### 我如何加入 Bright Data 的 HTTP3 Beta 试用？

    要获得对我们 HTTP3 Beta 的访问权限，请联系您在 Bright Data 的客户经理。我们目前仅授权选定的企业加入我们的 HTTP3 Beta 试用。
  </Accordion>

  <Accordion title="我可以导出我的日志吗？" defaultOpen="false">
    是的 - Bright Data 支持将您的日志导出到 AWS S3 存储。在此处在您的控制面板中进行设置：[https://www.bright.cn/cp/setting/logs\_delivery](https://www.bright.cn/cp/setting/logs_delivery)

    ***注意：您的 AWS S3 存储桶必须位于 us-east-1 区域***
  </Accordion>
</AccordionGroup>
