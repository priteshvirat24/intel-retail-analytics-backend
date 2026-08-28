> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 住宅产品常见问题解答

> 查找有关集成、配置和使用 Bright Data 住宅代理产品的常见问题解答，包括 IP 类型、地理定位和错误代码。

<AccordionGroup>
  <Accordion title="为什么住宅代理需要 KYC？">
    Bright Data 住宅代理仅向通过 Bright Data 合规团队人工审核 KYC（了解您的客户）的已验证企业开放。住宅 IP 来自 100% 主动选择加入网络的真实用户，因此合规团队会在您通过这些真实节点转发流量之前验证您的业务和使用案例。批准绝不会自动或即时完成。完整流程请参见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
  </Accordion>

  <Accordion title="我用个人邮箱注册，能使用住宅代理吗？">
    不能。住宅访问仅向已验证企业开放。KYC 申请仅接受来自拥有公司邮箱域名的已注册企业，因此个人邮箱账户（例如 Gmail 或 Outlook）无法获批。请添加一个使用公司邮箱域名的用户，然后提交 [KYC](https://www.bright.cn/cp/kyc)。在没有 KYC 的情况下，您可使用 [ISP 代理](/cn/proxy-networks/isp/introduction)、[数据中心代理](/cn/proxy-networks/data-center/introduction) 和 [Web Unlocker API](/cn/scraping-automation/web-unlocker/introduction)。
  </Accordion>

  <Accordion title="可以把现有的 ISP 或数据中心区域切换为住宅吗？">
    仅在 KYC 批准之后。在 Bright Data 合规团队批准您的 KYC 提交之前，创建或将区域转换为住宅将被阻止。在 KYC 审核期间，您现有的 ISP 和数据中心区域照常工作。请从 [KYC 验证](https://www.bright.cn/cp/kyc) 开始。
  </Accordion>

  <Accordion title="无需 KYC 可以使用什么？">
    使用以下住宅代理的替代方案，它们均无需 KYC：

    * **[ISP 代理](/cn/proxy-networks/isp/introduction)**：静态、以住宅名义注册的 IP，具备数据中心速度，适用于广告验证、质量保证和长时间稳定会话。
    * **[数据中心代理](/cn/proxy-networks/data-center/introduction)**：快速、低成本的共享或专用 IP，适用于高并发请求。
    * **[Web Unlocker API](/cn/scraping-automation/web-unlocker/introduction)**：托管解锁，自动处理请求头、Cookie、验证码和重试，按成功请求计费。

    这些是替代方案，并非受限或试用版的住宅模式。
  </Accordion>

  <Accordion title="如何将新的代理集成到您的代码中？">
    要将代理集成到您的代码中，请访问 [API 示例页面](https://www.bright.cn/cp/zones/proxy_examples)，可通过您的 Zone 设置中的 “access parameters” 进入：

    <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/proxy-networks/faqs/integrate-new-proxy.gif?s=d6ff106d13eeb94ec0ef2d76bddc9103" alt="integrate-new-proxy.gif" width="1828" height="978" data-path="images/proxy-networks/faqs/integrate-new-proxy.gif" />

    在此页面，您可以选择大多数现代编程语言的集成示例，只需选择集成类型、代理 Zone、编程语言等，页面就会自动生成可直接使用的代码片段。
  </Accordion>

  <Accordion title="如何将代理集成到第三方软件？">
    查看上面提到的 [API 示例](https://www.bright.cn/cp/zones/proxy_examples) 页面中的一些示例（在 “language” 下拉菜单中选择 “other software”），或访问我们的 [集成页面](/cn/integrations)，其中包含最流行工具的代理集成指南。

    **重要说明**：如果您使用 Bright Data 的 Web Unlocker API、住宅代理或 SERP API，则可能需要使用我们的 SSL 证书以启用端到端加密连接。请参阅[此处的说明](/cn/general/account/ssl-certificate)。

    我们为最常用的工具准备了详细指南。以下是链接列表：

    BrowserScan     [http://docs.brightdata.com/cn/integrations/browserscan](http://docs.brightdata.com/cn/integrations/browserscan)\
    XLogin          [http://docs.brightdata.com/cn/integrations/xlogin](http://docs.brightdata.com/cn/integrations/xlogin)\
    GeeLark         [http://docs.brightdata.com/cn/integrations/geelark](http://docs.brightdata.com/cn/integrations/geelark)\
    Puppeteer       [http://docs.brightdata.com/cn/integrations/puppeteer](http://docs.brightdata.com/cn/integrations/puppeteer)\
    Playwright      [http://docs.brightdata.com/cn/integrations/playwright](http://docs.brightdata.com/cn/integrations/playwright)\
    Selenium        [http://docs.brightdata.com/cn/integrations/selenium](http://docs.brightdata.com/cn/integrations/selenium)\
    AdsPower        [http://docs.brightdata.com/cn/integrations/adspower](http://docs.brightdata.com/cn/integrations/adspower)\
    Dolphin Anty    [http://docs.brightdata.com/cn/integrations/dolphin-anty](http://docs.brightdata.com/cn/integrations/dolphin-anty)\
    Incogniton      [http://docs.brightdata.com/cn/integrations/incogniton](http://docs.brightdata.com/cn/integrations/incogniton)\
    Marketerbrowser [http://docs.brightdata.com/cn/integrations/marketerbrowser](http://docs.brightdata.com/cn/integrations/marketerbrowser)\
    SMLOGIN         [http://docs.brightdata.com/cn/integrations/smlogin](http://docs.brightdata.com/cn/integrations/smlogin)\
    Hidemyacc       [http://docs.brightdata.com/cn/integrations/hidemyacc](http://docs.brightdata.com/cn/integrations/hidemyacc)\
    OpenBullet      [http://docs.brightdata.com/cn/integrations/openbullet](http://docs.brightdata.com/cn/integrations/openbullet)\
    Switchyomega    [http://docs.brightdata.com/cn/integrations/switchyomega](http://docs.brightdata.com/cn/integrations/switchyomega)\
    PhantomBuster   [http://docs.brightdata.com/cn/integrations/phantombuster](http://docs.brightdata.com/cn/integrations/phantombuster)\
    BitBrowser      [http://docs.brightdata.com/cn/integrations/bitbrowser](http://docs.brightdata.com/cn/integrations/bitbrowser)\
    Maskfog         [http://docs.brightdata.com/cn/integrations/maskfog](http://docs.brightdata.com/cn/integrations/maskfog)\
    Ghost Browser   [http://docs.brightdata.com/cn/integrations/ghost-browser](http://docs.brightdata.com/cn/integrations/ghost-browser)\
    Postman         [http://docs.brightdata.com/cn/integrations/postman](http://docs.brightdata.com/cn/integrations/postman)\
    NGINX           [http://docs.brightdata.com/cn/integrations/nginx](http://docs.brightdata.com/cn/integrations/nginx)\
    StablerSOLO     [http://docs.brightdata.com/cn/integrations/stablersolo](http://docs.brightdata.com/cn/integrations/stablersolo)\
    VMLogin         [http://docs.brightdata.com/cn/integrations/vmlogin](http://docs.brightdata.com/cn/integrations/vmlogin)\
    GoLogin         [http://docs.brightdata.com/cn/integrations/gologin](http://docs.brightdata.com/cn/integrations/gologin)\
    Windows         [http://docs.brightdata.com/cn/integrations/windows](http://docs.brightdata.com/cn/integrations/windows)\
    Scrapy          [http://docs.brightdata.com/cn/integrations/scrapy](http://docs.brightdata.com/cn/integrations/scrapy)\
    AEZAKMI         [http://docs.brightdata.com/cn/integrations/aezakmi](http://docs.brightdata.com/cn/integrations/aezakmi)\
    Beautifulsoup   [http://docs.brightdata.com/cn/integrations/beautifulsoup](http://docs.brightdata.com/cn/integrations/beautifulsoup)\
    WebHarvy        [http://docs.brightdata.com/cn/integrations/webharvy](http://docs.brightdata.com/cn/integrations/webharvy)\
    Ubuntu          [http://docs.brightdata.com/cn/integrations/ubuntu](http://docs.brightdata.com/cn/integrations/ubuntu)\
    Lalicat         [http://docs.brightdata.com/cn/integrations/lalicat](http://docs.brightdata.com/cn/integrations/lalicat)\
    Multilogin      [http://docs.brightdata.com/cn/integrations/multilogin](http://docs.brightdata.com/cn/integrations/multilogin)\
    Undetectable    [http://docs.brightdata.com/cn/integrations/undetectable](http://docs.brightdata.com/cn/integrations/undetectable)\
    Apify           [http://docs.brightdata.com/cn/integrations/apify](http://docs.brightdata.com/cn/integrations/apify)\
    iPhone          [http://docs.brightdata.com/cn/integrations/ios](http://docs.brightdata.com/cn/integrations/ios)\
    MuLogin         [http://docs.brightdata.com/cn/integrations/mulogin](http://docs.brightdata.com/cn/integrations/mulogin)\
    Changedetection [http://docs.brightdata.com/cn/integrations/changedetection](http://docs.brightdata.com/cn/integrations/changedetection)\
    Morelogin       [http://docs.brightdata.com/cn/integrations/morelogin](http://docs.brightdata.com/cn/integrations/morelogin)\
    Proxifier       [http://docs.brightdata.com/cn/integrations/proxifier](http://docs.brightdata.com/cn/integrations/proxifier)\
    Texau           [http://docs.brightdata.com/cn/integrations/texau](http://docs.brightdata.com/cn/integrations/texau)\
    Android         [http://docs.brightdata.com/cn/integrations/android](http://docs.brightdata.com/cn/integrations/android)\
    Kameleo         [http://docs.brightdata.com/cn/integrations/kameleo](http://docs.brightdata.com/cn/integrations/kameleo)\
    Screaming Frog  [http://docs.brightdata.com/cn/integrations/screaming-frog](http://docs.brightdata.com/cn/integrations/screaming-frog)\
    Foxy            [http://docs.brightdata.com/cn/integrations/foxyproxy](http://docs.brightdata.com/cn/integrations/foxyproxy)\
    SessionBox      [http://docs.brightdata.com/cn/integrations/sessionbox](http://docs.brightdata.com/cn/integrations/sessionbox)\
    Insomniac       [http://docs.brightdata.com/cn/integrations/insomniac](http://docs.brightdata.com/cn/integrations/insomniac)\
    Helium Scraper  [http://docs.brightdata.com/cn/integrations/helium-scraper](http://docs.brightdata.com/cn/integrations/helium-scraper)\
    SaleFreaks      [http://docs.brightdata.com/cn/integrations/salefreaks](http://docs.brightdata.com/cn/integrations/salefreaks)\
    Postern         [http://docs.brightdata.com/cn/integrations/postern](http://docs.brightdata.com/cn/integrations/postern)\
    Antik           [http://docs.brightdata.com/cn/integrations/antik](http://docs.brightdata.com/cn/integrations/antik)\
    Easync          [http://docs.brightdata.com/cn/integrations/easync](http://docs.brightdata.com/cn/integrations/easync)\
    ParseHub        [http://docs.brightdata.com/cn/integrations/parsehub](http://docs.brightdata.com/cn/integrations/parsehub)\
    Sphere Browser  [http://docs.brightdata.com/cn/integrations/sphere-browser](http://docs.brightdata.com/cn/integrations/sphere-browser)\
    Octoparse       [http://docs.brightdata.com/cn/integrations/octoparse](http://docs.brightdata.com/cn/integrations/octoparse)\
    ixBrowser       [http://docs.brightdata.com/cn/integrations/ixbrowser](http://docs.brightdata.com/cn/integrations/ixbrowser)\
    Shadowrocket    [http://docs.brightdata.com/cn/integrations/shadowrocket](http://docs.brightdata.com/cn/integrations/shadowrocket)\
    Firefox         [http://docs.brightdata.com/cn/integrations/firefox](http://docs.brightdata.com/cn/integrations/firefox)\
    Chrome          [http://docs.brightdata.com/cn/integrations/chrome](http://docs.brightdata.com/cn/integrations/chrome)\
    MacOS           [http://docs.brightdata.com/cn/integrations/macos](http://docs.brightdata.com/cn/integrations/macos)\
    ClonBrowser     [http://docs.brightdata.com/cn/integrations/clonbrowser](http://docs.brightdata.com/cn/integrations/clonbrowser)\
    Octo Browser    [http://docs.brightdata.com/cn/integrations/octobrowser](http://docs.brightdata.com/cn/integrations/octobrowser)\
    Genlogin        [http://docs.brightdata.com/cn/integrations/genlogin](http://docs.brightdata.com/cn/integrations/genlogin)\
    Web Scraper     [http://docs.brightdata.com/cn/integrations/webscraper](http://docs.brightdata.com/cn/integrations/webscraper)

    如果您使用的工具未出现在列表中，并需要相关指南，请联系我们！
  </Accordion>

  <Accordion title="如何定位特定国家？">
    在发送请求时，在请求中您的 Zone 名称**之后**添加 `-country` 标志，并跟上该国家的两个字母的 [ISO 代码](https://www.nationsonline.org/oneworld/country_code_list.htm)。

    在下面的示例中：我们添加了 `-country-us`，因此请求将从美国（"us"）发出。

    ```sh theme={null}
    curl "http://target.site" --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-country-us:<zone_password>
    ```
  </Accordion>

  <Accordion title="如何定位欧盟地区">
    <Note>
      欧盟国家的分配是随机的。
    </Note>

    <Info>
      适用于 DC、ISP 和 Unlocker/SERP API
    </Info>

    您可以像“国家”一样，在请求中添加 `-country-eu` 来定位整个欧盟地区。

    使用 -country-eu 的请求将使用以下任一国家的 IP（这些国家自动包含在 “eu” 中）：

    ```
    AL, AZ, KG, BA, UZ, BI, XK, SM, DE, AT, CH, UK, GB, IE, IM, FR, ES, NL, IT, PT, BE, AD, MT, MC, MA, LU, TN, DZ, GI, LI, SE, DK, FI, NO, AX, IS, GG, JE, EU, GL, VA, FX, FO
    ```
  </Accordion>

  <Accordion title="如何定位特定城市？">
    若要定位特定城市，您需要使用 [共享（按 IP 计费）](/cn/proxy-networks/data-center/configure-your-proxy#ip-type) 或 [专用](/cn/proxy-networks/data-center/configure-your-proxy#ip-type) 代理网络。

    在配置代理 Zone 时，选择国家后可以添加城市，以进一步细化地理位置定位。

    <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/proxy-networks/faqs/add-city.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=3737416f78148a39f484861f92c78727" alt="add-city.png" width="664" height="376" data-path="images/proxy-networks/faqs/add-city.png" />

    点击 **“Add city”** 后，您将看到可定位的城市列表。若要查看特定位置的 [可用 IP 数量](https://www.bright.cn/cp/ips_availability)。

    配置完成后，您可以使用以下语法从指定城市发送请求：

    ```sh theme={null}
    curl "http://target.site" --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-country-<country>-city-<city>:<zone_password>
    ```

    <Note>
      当选择双词城市时，其名称将在语法中写作一个单词。

      例如：定位 Buenos Aires 时，应写为：

      `-country-ar-city-buenosaires`
    </Note>

    若需查看更多地理定位示例，您可查看我们的 [代理集成示例页面](https://www.bright.cn/cp/zones/proxy_examples)。
  </Accordion>

  <Accordion title="Bright Data 在哪些国家提供代理？">
    Bright Data 在全球所有国家提供代理，但以下国家除外：

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

    如果您需要这些国家的代理，我们无法提供帮助。
  </Accordion>

  <Accordion title="如何查看代理事件日志？">
    事件日志将显示您账户中任意 Zone 的最近最多 200 条请求。

    在 Bright Data 控制面板的代理页面：[https://www.bright.cn/cp/zones](https://www.bright.cn/cp/zones)

    转到 “Event Log” 标签：

    <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/proxy-networks/faqs/event-log.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=5f3ac5d7e5959497491844ba43f10e7c" alt="event-log.png" width="1833" height="977" data-path="images/proxy-networks/faqs/event-log.png" />

    显示的数据包括：

    * **Date：** 请求的时间
    * **Zone：** 使用的 Zone
    * **Source IP：** 请求发出的源 IP
    * **URL：** 请求访问的网站
    * **Result：** 请求成功或失败

          <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/proxy-networks/faqs/event-log-headers.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=4b8fc284481b3f221198c898418167be" alt="event-log-headers.png" width="1833" height="977" data-path="images/proxy-networks/faqs/event-log-headers.png" />
  </Accordion>

  <Accordion title="如何在多个请求中保持相同 IP？">
    * 您可以在代理用户名中添加 `session` 参数来实现此功能：

      ```sh theme={null}
      brd.superproxy.io:44445 br-customer-<customer_id>-zone-<zone_name>-session-rand39484
      ```

      在线程启动时生成一个随机数，并在需要更换该线程连接所分配的 Proxy Peer（代理节点）时更改它。

    * Session ID 可以是任意随机字符串或计数器：
      使用相同 Session 字符串的请求将尽可能使用同一个 Proxy Peer；
      使用不同 Session 字符串的请求将分配不同的 Proxy Peers。

          <Warning>
            * 若 Session ID 中包含以下字符将会导致报错：`-` `"` `` ` ``
            * 此功能仅适用于代理产品，对 Web Unlocker API 等抓取自动化产品 **不适用**
          </Warning>

    * 若要强制更换 IP，只需修改 Session ID 即可。

    * 如果当前分配的 Proxy Peer（出口节点 IP）不可用，Super Proxy 会在第一次请求时返回错误 **“502 - No peers available”**；第二次请求时，即使您没有更改 Session ID，它也会为您分配一个新的 peer。

    * Session IP 在空闲状态下可保持最长 5 分钟。若超过 5 分钟无请求，该 IP 将被释放回资源池。
      若您希望保持更长时间，请每 30 秒发送一个小型的 keep-alive 请求，以防该 Session 的空闲时间超过 1 分钟。
      此请求可以非常小，例如 `/favicon.ico`，甚至是返回 404 的请求（只要该 Web 服务器不会因为此请求而断开连接）。
  </Accordion>

  <Accordion title="如何定位特定操作系统？">
    Bright Data 允许定位以下 **操作系统**：

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

  <Accordion title="如何使用特定 IP？">
    当使用 Bright Data 住宅代理网络时，有时您可能需要使用分配给您 Zone 的特定 IP。

    1. **发送测试请求**，加入 `--verbose` 或 `-v` 选项以查看详细日志：

    ```sh theme={null}
    curl "https://brdtest.com/myip.json" --verbose --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>:<zone_password>
    ```

    2. **找到** x-brd-ip 响应头，并复制其值

           <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/proxy-networks/faqs/x-brd-ip.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=4a8f34a47da1aac1576d8ecc9aafed16" alt="x-brd-ip.png" width="423" height="23" data-path="images/proxy-networks/faqs/x-brd-ip.png" />

    3. **添加** -ip- 标志，并使用复制的 **hashed IP 值**

    4. 发送测试请求并 **检查响应**

    ```sh theme={null}
    curl "https://brdtest.com/myip.json" --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-ip-<hashed-ip>:<zone_password>
    ```

    我们建议使用 [https://brdtest.com/myip.json](https://brdtest.com/myip.json) 作为测试域，以检查您的 IP 凭证。
  </Accordion>

  <Accordion title="如何定位特定 ASN 的 IP？">
    可在 Zone 配置中的 **Geolocation Targeting** 添加 ASN 参数来启用此功能。

    <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/proxy-networks/faqs/asn-targeting.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=78916db58402711b9ad0b8b9ee29747f" alt="asn-targeting.png" width="583" height="931" data-path="images/proxy-networks/faqs/asn-targeting.png" />

    配置保存后，可在 Zone 凭证中加入 ASN 标志，例如：

    ```sh theme={null}
    curl --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-asn-<asn-number>:<zone_password> "<target_site>"
    ```

    **注意：** ASN 号可从 [这里](https://bgp.potaroo.net/cidr/autnums.html) 获取。
  </Accordion>

  <Accordion title="如何使用组 IP（gIPs）定位住宅代理？">
    专用住宅 IP 可以 [gIPs](/cn/proxy-networks/residential/configure-your-proxy#ip-groups-gips) 的形式使用。它们可在 Zone 配置页面中通过选择 "Dedicated" IP 类型并配置数量进行分配，同时需要绑定特定域名。

    <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/proxy-networks/faqs/number-of-dedicated-gIPs.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=5066fce4640fbb09ea33700160207c24" alt="number-of-dedicated-gIPs.png" width="839" height="1238" data-path="images/proxy-networks/faqs/number-of-dedicated-gIPs.png" />

    保存配置后，选择 “Show allocated Dedicated residential IPs” 即可看到 gIP 的哈希值列表。

    <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/proxy-networks/faqs/show-allocated-dedicated-ips.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=9228edecff61a348346d2456541bb9cd" alt="show-allocated-dedicated-ips.png" width="583" height="393" data-path="images/proxy-networks/faqs/show-allocated-dedicated-ips.png" />

    这些值可用于定位特定 gIP，例如：

    ```sh theme={null}
    curl --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-gip-<gip_hash_value>:<zone_password> "<target_site>"
    ```
  </Accordion>

  <Accordion title="如何使用中国住宅 IP 浏览中国网站">
    **当您在中国境外时**\
    只需定位中国住宅代理即可：

    ```sh theme={null}
    curl --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-country-cn:<zone_password> "<target_site>"
    ```
  </Accordion>

  <Accordion title="运营商专用代理节点 IP（Carrier-specific Proxy peer IP）">
    * 您可以从以下列表中选择特定的运营商：

    ```
    a1, aircel, airtel, att, celcom, chinamobile, claro, comcast, cox, digi, 
    dt, docomo, dtac, etisalat, idea,  meo, mtn, mtnza, 
    optus, orange, qwest, reliance_jio, robi, sprint, telefonica, telstra, 
    tmobile, tigo, tim, verizon,  vodacomza, vodafone, vivo, zain,
    vivabo, telenormyanmar, kcelljsc, swisscom, singtel, asiacell, windit, 
    cellc, ooredoo, drei, umobile, cableone, proximus, mobitel, o2, 
    bouygues, free, sfr, digicel
    ```

    * 示例：

    <CodeGroup>
      ```sh Deutsche Telekom theme={null}
      brd-customer-<customer_id>-zone-<zone_name>-carrier-dt
      ```

      ```sh Sprint theme={null}
      brd-customer-<customer_id>-zone-<zone_name>-carrier-sprint
      ```
    </CodeGroup>
  </Accordion>

  <Accordion title="哪些 Bright Data 产品最适合抓取搜索引擎（SERPs）？">
    #### 对于单步骤抓取：

    [SERP API](/cn/scraping-automation/serp-api/introduction) 是专为抓取 SERPs 而设计的理想产品，具有保证成功率（仅为成功付费）、主动解封、自动选择最佳代理、自定义请求头、指纹、CAPTCHA 解决等功能。

    #### 对于多步骤抓取（playwright/puppeteer/selenium）：

    [Browser API](/cn/scraping-automation/scraping-browser/introduction) 是最佳选择，它是完全云托管的浏览器，可让您专注于多步骤数据采集，而我们负责完整的代理与解封基础设施，包括 CAPTCHA 解决等。
  </Accordion>

  <Accordion title="我可以使用 Residential、Datacenter 或 ISP Proxy 网络来抓取 Google SERPs 吗？">
    **Residential Proxy** —— 不能。[SERP API](/cn/scraping-automation/serp-api/introduction) 是抓取 SERPs 的理想产品，具有保证成功率（仅为成功付费）、主动解封、自动选择最佳代理、自定义请求头、指纹、CAPTCHA 解决等功能。\
    从 Residential 网络抓取 Google SERPs 会触发 Super-proxy bypass，这会导致请求通过 Bright Data 服务器发送，而不是通过 peer 节点。

    **Datacenter & ISP Proxies** —— 不能。
    当尝试通过这些代理网络抓取 Google 时，请求会被拒绝，并收到以下响应头中的错误信息：

    ```
    HTTP/1.1 403 Search engine host is not allowed
    X-Luminati-Error: Forbidden: This target URL isn't supported on proxy networks, use the SERP API product for targeting this URL. You may contact your account manager or open a support ticket for assistance
    ```
  </Accordion>

  <Accordion title="通过 Bright Data Residential 与 Mobile 网络抓取搜索引擎">
    当通过 Residential 或 Mobile 网络抓取搜索引擎时，请求不会通过 Residential 或 Mobile peer，而是直接通过 super proxy。\
    这样做的原因是为了支持浏览器环境中的 Residential 和 Mobile 网络集成，因为浏览器可能需要加载来自目标站点的搜索引擎资源端点。

    **如果您在 Residential 或 Mobile 网络中访问搜索引擎域名，请求将直接通过 super proxy，并会出现以下响应头作为指示：**

    ```sh theme={null}
    x-luminati-ip: superproxy bypass
    ```
  </Accordion>

  <Accordion title="我如何查看我的 Residential 代理的 IP 地址？">
    Bright Data 不允许以明文形式查看 Residential 和 Mobile 的 IP 地址。Datacenter 和 ISP Proxy 的 IP 则可以以明文形式查看。

    当您发送请求时，在响应头中会看到 `x-brd-ip`。该响应头包含一个唯一的哈希值，用于表示您在此次请求中实际使用的 IP 地址。
  </Accordion>
</AccordionGroup>
