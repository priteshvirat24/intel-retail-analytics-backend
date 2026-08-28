> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 数据中心代理常见问题解答

> 查找有关集成、配置和使用 Bright Data 数据中心代理产品的常见问题解答，包括 IP 类型、地理定位目标和错误代码。

<AccordionGroup>
  <Accordion title="数据中心有哪些 IP 类型？">
    我们的 [数据中心代理网络](https://www.bright.cn/proxy-types/datacenter-proxies) 提供四种 IP 类型：

    1. 共享代理池（按使用量付费）- 40,000 个轮换代理的池
    2. 共享无限代理（按代理付费）- 您与他人共享的一组代理。
    3. 独享无限代理（按代理付费）- 供您独享的一组代理。
  </Accordion>

  <Accordion title="ISP 有哪些 IP 类型？">
    我们的 [ISP 代理网络](https://www.bright.cn/proxy-types/isp-proxies) 提供三种 IP 类型：

    1. 共享代理池（按使用量付费）- 10,000 个轮换代理的池
    2. 共享无限代理（按代理付费）- 您与他人共享的一组代理。
    3. 独享无限代理（按代理付费）- 供您独享的一组代理。
  </Accordion>

  <Accordion title="如何将新代理集成到您的代码中？">
    要将代理集成到您的代码中，请访问 [API 示例页面](https://www.bright.cn/cp/zones/proxy_examples)，该页面可通过您的区域设置中的“访问参数”访问：

    <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/proxy-networks/faqs/integrate-new-proxy.gif?s=d6ff106d13eeb94ec0ef2d76bddc9103" alt="integrate-new-proxy.gif" width="1828" height="978" data-path="images/proxy-networks/faqs/integrate-new-proxy.gif" />

    在此页面上，您可以选择大多数现代编程语言的集成示例，只需选择集成类型、您的代理区域、编程语言等，页面将生成一个您可以立即使用的代码片段。
  </Accordion>

  <Accordion title="如何将代理集成到第三方软件中？">
    请查看上面提到的 [API 示例](https://www.bright.cn/cp/zones/proxy_examples) 页面中的一些示例（只需在“语言”下拉菜单中选择“其他软件”），或查看我们的 [集成页面](/cn/integrations)，我们在其中提供了将我们的代理集成到当今行业中最流行的工具中的具体指南。

    **重要提示**：如果您正在使用 Bright Data 的 Web Unlocker API、住宅代理或 SERP API，您可能需要使用我们的 SSL 证书来启用端到端安全连接。请参阅[此处的说明](/cn/general/account/ssl-certificate)。
  </Accordion>

  <Accordion title="如何定位特定国家/地区？">
    发送请求时，在请求中的区域名称 **之后** 添加 `-country` 标记，后跟该国家/地区的 2 个字母的 [ISO 代码](https://www.nationsonline.org/oneworld/country_code_list.htm)。

    在以下示例中：我们在请求中添加了 `-country-us`，因此我们将发送一个源自美国（"us"）的请求。

    ```sh theme={null}
    curl "[http://target.site](http://target.site)" --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-country-us: <zone_password>
    ```
  </Accordion>

  <Accordion title="如何在数据中心和 ISP 代理网络中定位特定城市？">
    对于数据中心和 ISP 网络，城市定位已被弃用，不再可用。
  </Accordion>

  <Accordion title="Bright Data 在哪里拥有代理？">
    Bright Data 在世界上除以下国家/地区外的所有国家/地区提供代理：

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

    如果您需要来自这些国家/地区的代理，很遗憾 Bright Data 将无法为您提供帮助。
  </Accordion>

  <Accordion title="如何查看代理事件日志？">
    事件日志将显示您账户中任何区域发出的（最多）最后 200 个请求。

    在您的 Bright Data 控制面板的代理页面：[https://www.bright.cn/cp/zones](https://www.bright.cn/cp/zones)

    转到“事件日志”选项卡：

    <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/proxy-networks/faqs/event-log.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=5f3ac5d7e5959497491844ba43f10e7c" alt="event-log.png" width="1833" height="977" data-path="images/proxy-networks/faqs/event-log.png" />

    显示的数据是：

    * **Date**：请求的时间和日期
    * **Zone**：用于请求的区域
    * **Source IP**：发出请求的 IP
    * **URL**：请求的目标站点
    * **Result**：请求成功或失败

          <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/proxy-networks/faqs/event-log-headers.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=4b8fc284481b3f221198c898418167be" alt="event-log-headers.png" width="1833" height="977" data-path="images/proxy-networks/faqs/event-log-headers.png" />
  </Accordion>

  <Accordion title="如何启用自动 IP 故障转移？（以前称为 100% 正常运行时间）">
    <Info>
      适用于数据中心和 ISP
    </Info>

    **自动故障转移** 旨在防止任何“外部”事件影响用户。这个想法很简单，对于上面描述的两个问题都以相同的方式工作 – 如果我们的系统检测到问题，例如连接问题，或 IP 的地理位置与您购买该 IP 时要求的地理位置不完全相同，我们将自动通过与原始 IP 完全相同的其他 IP 路由您的请求。

    同时，我们希望确保必须使用特定 IP 的客户不会受到影响 – 因此我们做了一些例外：

    * 如果您的请求定位了特定的 IP，我们将不会为其分配故障转移 IP
    * 自动故障转移不会中断实时连接。如果需要故障转移，它将在建立下一个连接时生效

    **自动故障转移** 通过提供 100% 的连接性和持续的高性能水平带来即时价值，**免费且无需在您的代码或工作方式中进行任何更改。**

    <Note>
      自动故障转移功能可以通过 [API](/cn/api-reference/account-management-api/Switch_100_uptime_ON_OFF_in_a_Static_zone) 开启或关闭。
    </Note>
  </Accordion>

  <Accordion title="如何为代理启用自动故障转移？">
    导航到您的代理配置设置，并在 **“高级设置”** 下启用 **“自动故障转移”**
  </Accordion>

  <Accordion title="如何在多个请求中保持使用相同的 IP？">
    * 这可以通过在代理用户名中添加会话标记来实现：

    ```sh theme={null}
    brd.superproxy.io:44445 br-customer-<customer_id>-zone-<zone_name>-session-rand39484
    ```

    在线程启动时生成随机数，并在您想要更改分配给该线程连接的代理节点时更改它。

    * 会话 ID 可以是任何随机字符串/计数器：具有相同会话字符串的请求将使用相同的代理节点（尽可能长）；具有不同会话字符串的请求将被分配不同的代理节点。
    * 要强制更改 IP，只需修改会话 ID
    * 如果分配的代理节点（出口节点 IP）变得不可用，超级代理将为第一个请求返回错误“502 - 无可用节点”，然后在第二个请求中，即使您不更改会话 ID，超级代理也会分配一个新的节点。
    * 会话 IP 最多可保持 1 分钟的空闲时间。在一分钟没有请求后，IP 将被释放回池中。\
      为了保持此会话/IP 更长时间，每 30 秒发送一个微小的保持连接请求，以防止此会话空闲超过一分钟。\
      此请求可以是任何小的东西，例如 `/favicon.ico`，甚至是返回 404 的请求（只要 Web 服务器不会因此请求而断开套接字）。
    * 如果您有多个客户端，并且想要忽略您的客户端源 IP（该 IP 与您的会话 ID 一起用于创建会话），那么您想要使用全局会话，然后将 `glob\_` 作为前缀添加到您的会话中：

    ```sh theme={null}
    brd-customer-<customer_id>-zone-<zone_name>-session-glob_rand39484
    ```

    完整请求示例：

    ```sh theme={null}
    brd-customer-CXXXXX-zone-ZONE_X-session-glob_rand39484
    ```

    在线程启动时生成随机数，并在您想要更改分配给该线程连接的代理节点时更改它。
  </Accordion>

  <Accordion title="如何查看支持的端口和协议？">
    端口 80 和 443 默认在所有区域中可用，支持 HTTP 和 HTTPS 协议。

    在数据中心或 ISP 类型的代理区域中，默认支持所有高于 1024 的端口。

    在住宅或移动类型的代理区域中，默认情况下将提供以下端口：8080、8443、5678、1962、2000、4443、4433、4430、4444 和 1969。

    Bright Data 可以根据请求支持其他端口。支持新端口的每个请求都将进行与 Bright Data 合规团队的专门和额外的合规流程。\
    激活前需要 Bright Data 合规性审核的端口示例：

    | 端口   | 协议    |
    | ---- | ----- |
    | 8443 | HTTP  |
    | 8243 | HTTPS |

    要请求为您的区域添加端口权限：

    * 转到您的区域设置（如果不是，默认情况下它将打开“配置”选项卡，请单击它）
    * 向下滚动到“高级选项”并单击它
    * 启用“端口”
    * 输入您想要获得批准的端口号
    * 填写表格并等待我们的合规团队联系您并批准请求

          <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/proxy-networks/faqs/add-ports.gif?s=f9a6ec418a18d21e107a604507aaf4c3" alt="add-ports.gif" width="1828" height="978" data-path="images/proxy-networks/faqs/add-ports.gif" />
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

  <Accordion title="如何刷新分配给您的区域的 IP？">
    如果您在区域配置中选择了“按 IP 付费”共享或独享 IP 类型，您将获得一个固定的 IP 地址。有时，根据您的用例，您可能需要刷新这些 IP 地址。

    为了刷新分配给您的区域的 IP，导航到您选择的区域，在 **“分配的 IP”** 下单击 **“显示分配的 IP”**，**选中** 您希望刷新的 IP 或 gIP 的框，然后单击 **“刷新”**

    <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/proxy-networks/faqs/refresh-ips.gif?s=fef981f0b4c45b5e28e0f0f66794da23" alt="refresh-ips.gif" width="1892" height="868" data-path="images/proxy-networks/faqs/refresh-ips.gif" />

    <Note>
      刷新 IP 或 gIP 将导致额外收费。
    </Note>

    或者，您可以使用 API 刷新您的 [独享住宅 IP](/cn/api-reference/account-management-api/Refresh_dedicated_residential_IPs) 或您的 [数据中心/ISP IP](/cn/api-reference/account-management-api/Refresh_Static_Datacenter_ISP_IPs)
  </Accordion>

  <Accordion title="如何使用特定的 IP？">
    使用 Bright Data 的住宅代理网络时，您可能会发现需要使用分配给您区域的特定 IP。

    1. **发送测试请求** 并添加 `--verbose` 或 `-v` 选项（这将打开详细日志记录）

    ```sh theme={null}
    curl "[https://brdtest.com/myip.json](https://brdtest.com/myip.json)" --verbose --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>:<zone_password>
    ```

    1. **定位** `x-brd-ip` 响应标头并复制其值

           <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/proxy-networks/faqs/x-brd-ip.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=4a8f34a47da1aac1576d8ecc9aafed16" alt="x-brd-ip.png" width="423" height="23" data-path="images/proxy-networks/faqs/x-brd-ip.png" />

    2. **在** 您的区域名称之后，向您的请求添加 `-ip-` 标记，并使用上一步中复制的 **哈希 IP 值**

    3. 发送测试请求，并 **查看响应**

    ```sh theme={null}
    curl "[https://brdtest.com/myip.json](https://brdtest.com/myip.json)" --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-ip-<hashed-ip>:<zone_password>
    ```

    我们建议使用 `https://brdtest.com/myip.json` 作为测试的目标域，并查看您的 IP 凭证。
  </Accordion>

  <Accordion title="如何定位特定 ASN 的 IP？">
    可以在您的区域配置中的 **“地理定位目标”** 下添加 ASN 参数来启用此功能。

    <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/proxy-networks/faqs/asn-targeting.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=78916db58402711b9ad0b8b9ee29747f" alt="asn-targeting.png" width="583" height="931" data-path="images/proxy-networks/faqs/asn-targeting.png" />

    配置保存后，可以将 ASN 标记添加到区域的凭证中\
    并在使用住宅代理时进行集成。例如：

    ```sh theme={null}
    curl --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-asn-<asn-number>:<zone_password> "<target_site>"
    ```

    **注意：** ASN 号码的值可以在 [此处](https://bgp.potaroo.net/cidr/autnums.html) 找到。
  </Accordion>

  <Accordion title="如何定位住宅 IP 组 (gIPs)？">
    专用住宅 IP 可以 [gIP](/cn/proxy-networks/residential/configure-your-proxy#ip-groups-gips) 的形式选择。可以通过在区域的配置页面中选择“专用”IP 类型并选择 gIP 数量来分配它们。还需要定位特定的域。

    <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/proxy-networks/faqs/number-of-dedicated-gIPs.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=5066fce4640fbb09ea33700160207c24" alt="number-of-dedicated-gIPs.png" width="839" height="1238" data-path="images/proxy-networks/faqs/number-of-dedicated-gIPs.png" />

    配置保存后，选择“显示分配的专用住宅 IP”将提供\
    表示组 IP 的哈希值列表。

    <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/proxy-networks/faqs/show-allocated-dedicated-ips.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=9228edecff61a348346d2456541bb9cd" alt="show-allocated-dedicated-ips.png" width="583" height="393" data-path="images/proxy-networks/faqs/show-allocated-dedicated-ips.png" />

    这些值可用于定位特定的 gIP。例如：

    ```sh theme={null}
    curl --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-gip-<gip_hash_value>:<zone_password> "<target_site>"
    ```
  </Accordion>

  <Accordion title="如何使用中国住宅 IP 浏览中国网站">
    **在中国境外时**\
    定位中国住宅 IP 节点就足够了：

    ```sh theme={null}
    curl --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-country-cn:<zone_password> "<target_site>"
    ```
  </Accordion>

  <Accordion title="特定运营商代理节点 IP">
    * 您可以从以下列表中选择使用特定的运营商：

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
    地理定位数据库 (GeoDB) 被互联网网站用于查询用户使用的 IP 地址信息。Bright Data 监控并维护当今使用的 4 个主要 GeoDB 的正确记录：Maxmind、ip2location、db-ip 和 Google。

    还有许多其他较小的 GeoDB，其中大多数使用过时的记录或有缺陷的测试方法，因此它们提供的信息不准确，或者旨在引诱其查看者从他们那里购买 VPN 或代理产品。因此，我们强烈建议在测试 IP 时使用上面提到的 GeoDB。

    为了查看我们关于您正在使用的代理 IP 的信息，请浏览以下其中之一：

    * [https://brdtest.com/echo.json](https://brdtest.com/echo.json)
    * [https://www.iplocation.net](https://www.iplocation.net)
    * [https://www.maxmind.com/en/geoip-demo](https://www.maxmind.com/en/geoip-demo)
  </Accordion>

  <Accordion title="哪些 Bright Data 产品最适合抓取搜索引擎 (SERPs)？">
    #### 对于单步抓取：

    [SERP API](/cn/scraping-automation/serp-api/introduction) 是定位 SERP 的理想产品，因为它具有保证的成功率（仅对成功付费），具有主动解锁、自动选择最佳代理、自定义标头、指纹识别、解决 CAPTCHA 等功能。

    #### 对于多步抓取 (playwright/puppeteer/selenium)：

    [浏览器 API](/cn/scraping-automation/scraping-browser/introduction) 是理想的产品，因为它是我们完全托管在云端的浏览器，旨在帮助您轻松专注于多步数据收集，同时我们为您处理完整的代理和解锁基础设施，包括 CAPTCHA 解决。
  </Accordion>

  <Accordion title="我可以使用住宅、数据中心或 ISP 代理网络定位 Google SERP 吗？">
    **住宅代理** - 否，[SERP API](/cn/scraping-automation/serp-api/introduction) 是定位 SERP 的理想产品，因为它具有保证的成功率（仅对成功付费），具有主动解锁、自动选择最佳代理、自定义标头、指纹识别、解决 CAPTCHA 等功能。从住宅网络定位 Google SERP 将导致超级代理绕过，这将导致请求从我们的服务器而不是节点发送。

    **数据中心和 ISP 代理** - 否。尝试通过这两个代理网络中的任一定位 Google 时，您的请求将被拒绝，您将在响应标头中收到以下错误消息：

    ```
    HTTP/1.1 403 Search engine host is not allowed
    X-Luminati-Error: Forbidden: This target URL isn't supported on proxy networks, use the SERP API product for targeting this URL. You may contact your account manager or open a support ticket for assistance
    ```
  </Accordion>

  <Accordion title="我可以向 IP 而不是域名发送请求吗？">
    否 - 使用 Bright Data 时，禁止直接向主机服务器而不是向域名发送请求。\
    使用 `1.1.1.1:443` 等 URL 格式的请求将使用超级代理服务器执行，而不是代理节点 IP。

    使用超级代理的请求示例：

    <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/proxy-networks/faqs/x-luminati-ip.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=5023c43edf48fe823839513027a59769" alt="x-luminati-ip.png" width="1431" height="891" data-path="images/proxy-networks/faqs/x-luminati-ip.png" />
  </Accordion>

  <Accordion title="我可以使用端口 25 或任何其他 SMTP 端口，或使用代理 IP 发送电子邮件吗？">
    由于 BrightData 关心我们的社区和节点质量，因此会阻止可用于发送垃圾邮件的 SMTP 请求。请注意，邮件域也被禁止访问，对邮件域的请求将从超级代理服务器而不是节点 IP 发送。
  </Accordion>

  <Accordion title="刷新数据中心 IP 的费用是多少？">
    刷新数据中心 IP 的费用将根据 IP 类型而有所不同。

    * 刷新专用数据中心 IP：\$0.5/次刷新/IP
    * 刷新专用域名数据中心 IP：\$0.04/次刷新/IP
    * 刷新共享数据中心 IP：\$0.02/次刷新/IP
  </Accordion>

  <Accordion title="Bright Data 是否支持 Socks5 协议？">
    是的。Bright Data 支持 `SOCKS5` 协议，默认端口 22228 用于 SOCKS5 通信。

    有关 [完整的 SOCKS5 配置说明](/cn/proxy-networks/socks5)，请参见此处。
  </Accordion>

  <Accordion title="我如何控制请求从哪里执行？">
    * 您可以选择直接从超级代理执行请求，而不是从节点的 IP 执行请求。在这种情况下，请求的 IP 将是超级代理的 IP。您需要在请求授权字符串中添加 **“-direct”**。`brd-customer-<customer_id>-zone-<zone_name>-direct`
  </Accordion>

  <Accordion title="如何刷新会话 (IP)？">
    长时间使用相同的 IP 会使目标网站更容易将该 IP 标记为代理，并可能使您的请求被目标网站检测到。刷新您的 IP 将导致 Bright Data 分配新 IP 来替换您池中现有的 IP，从而使您能够控制您的代理池并获得更高的成功率。
  </Accordion>

  <Accordion title="我可以向 Bright Data 请求专用于无限数据中心和 ISP 的缺失代理吗？" defaultOpen="false">
    请求缺失的代理 (IP)，或为未来项目安排 IP 交付是一项处于 BETA 模式的功能，仅适用于少数选定的企业客户。

    Bright Data 允许根据以下条件提交代理请求（“代理未来订单”）：

    1. 客户已获得提交 IP 请求/订单的资格。此权限仅授予现有的企业级客户。
    2. IP 专用于客户（我们不允许订购共享 IP）。
    3. IP 仅适用于数据中心或 ISP。
    4. 必须提供单个特定国家/地区。
    5. 最小订单量为 100 个代理

    要查看您的账户是否有资格提交 IP 请求（订单），请浏览此处：[https://www.bright.cn/cp/zones/order\_ips](https://www.bright.cn/cp/zones/order_ips)

    大多数客户会发现 Bright Data 的库存足以满足他们的需求，并且不需要下任何订单。

    #### 我应该何时请求未来的代理？

    如果您的账户有资格提交请求，您可以请求未来交付代理 IP。

    #### 我尝试定义一个区域，但 Bright Data 无法分配我想要的所有代理，该怎么办？

    如果在保存区域时收到一条消息，指出特定国家/地区没有代理可用，或者只有您请求的部分数量可用，请尝试选择更多国家/地区或更改您的国家/地区设置，以便我们为您找到代理。

    一旦您提交了缺失代理的请求，我们的团队将尝试调配代理。获取和调配过程通常需要长达 14 天。一旦代理准备就绪，我们将通知您。我们鼓励您每 2-3 天再次检查一次，看看库存是否已刷新以及是否有更多代理可用。
  </Accordion>

  <Accordion title="如何将代理 (IP) 从一个区域移动到另一个区域？">
    我们的控制面板尚不支持将预付费数据中心或 ISP 无限代理（共享和专用）从一个区域移动到另一个区域。我们计划通过自助服务支持将代理从一个区域移动到另一个区域。如果您需要移动代理，请联系我们的支持团队。
  </Accordion>

  <Accordion title="我的部分 IP 被替换了，为什么会发生这种情况？">
    Bright Data 可能会识别出某些问题，这些问题使我们无法通过它们提供优质服务。它们要么变得不可用，要么出现延迟，因此为了保持我们的服务水平，我们不得不替换它们。我们会努力尽量减少这些替换，并且在可能的情况下提供初步通知。

    您可以使用此 API 来监控您的区域是否有待替换的 IP，并相应地调整您的操作（例如，刷新这些 IP）：[https://docs.brightdata.com/cn/api-reference/account-management-api/get-proxies-pending-replacement](https://docs.brightdata.com/cn/api-reference/account-management-api/get-proxies-pending-replacement)
  </Accordion>
</AccordionGroup>
