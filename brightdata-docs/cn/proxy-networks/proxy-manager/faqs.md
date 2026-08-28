> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 代理管理器常见问题

> 查找常见代理管理器问题的详细答案，包括访问限制、端口倍增、IP 目标定位等。

<AccordionGroup>
  <Accordion title="我可以限制对本地远程代理管理器的访问吗？">
    为了保护您的账户并防止对代理管理器进行未经授权的访问，有 3 种主要可用的工作流程：

    1. IP 白名单
    2. 使用 API 密钥的基于令牌的身份验证
    3. 使用 Bright Data 扩展程序的邮箱权限
  </Accordion>

  <Accordion title="如何通过 HTTPS 连接到超级代理？">
    代理管理器可以使用 HTTP 或 HTTPS 连接与 Bright Data 主基础设施连接。

    <Note>
      **为避免混淆：** 这**不是**连接到目标 URL 的连接类型。确保连接安全，只需保持 **“连接到超级代理”** 处于默认值 (HTTP) 即可，因为 HTTPS 请求无论如何都会与目标网站创建端到端加密连接。
    </Note>

    在大多数情况下，您甚至不需要更改此配置。但是，在从某些禁止访问某些域的地区连接时，它可能会很有用。在这些情况下，您需要将其设置为 **HTTPS**，以防止全局防火墙查看您的代理流量内容并根据目标域进行过滤
  </Accordion>

  <Accordion title="如何进行端口倍增？">
    转到“通用”选项卡，在“倍增代理端口”下拉菜单中选择您想要倍增的端口数量

    一旦您设置了所需的倍增端口数量，代理管理器将生成与您配置的端口相同的顺序端口。

    当您需要创建许多具有相同设置但只需设置一次的端口时，这是一个非常强大的功能。
  </Accordion>

  <Accordion title="如何获取来自特定位置的 IP？">
    使用 Bright Data，您可以指定用于发送流量的 IP 的地理位置和其他参数。在代理管理器中这尤其容易，因为它只需点击几下。

    根据您使用的区域，您可以请求仅来自特定国家/地区的 IP（如果您使用住宅或数据中心网络），或附加特定运营商（如果您使用移动网络）。

    **如何在代理管理器中设置目标定位？**

    要获取来自特定位置的 IP，请按照以下步骤操作：

    * 点击您想要使用特定位置 IP 的代理端口
    * 转到 **“目标定位”** 选项卡
    * 选择国家/地区、州/省、城市以选择特定地理位置的对等点
    * 选择 ASN 或运营商名称（仅适用于移动对等点）

    <Note>
      每个目标定位选项都需要您的区域具有适当的权限。
    </Note>

    <Accordion title="如何在不创建多个端口的情况下使用来自多个国家/地区的 IP？">
      如果您想使用多个国家/地区，并且不想为每个国家/地区创建单独的代理端口，也可以动态控制目标定位。
    </Accordion>
  </Accordion>

  <Accordion title="如何动态控制目标定位？">
    您不必使用用户界面中的“目标定位”选项卡预先指定国家/地区、州/省或城市目标定位。可以随请求动态地（“即时”）传递额外的目标定位选项。

    ```sh theme={null}
    curl -x lum-country-br@127.0.0.1:24001 [http://brdtest.com/myip.json](http://brdtest.com/myip.json)
    ```

    请求的结构是：

    ```sh theme={null}
    curl -x lum-country-<country_iso_code>@<ip>:<port> <destination_url>
    ```

    动态控制目标定位的另一个选项是包含一个特殊标头。

    ```sh theme={null}
    "x-lpm-country: <country_code>"
    ```

    示例请求可能如下所示：

    ```sh theme={null}
    curl --proxy [http://127.0.0.1:24000](http://127.0.0.1:24000) -H "x-lpm-country: us" [http://brdtest.com/myip.json](http://brdtest.com/myip.json)
    ```

    您还可以使用标头来控制州/省和城市：

    * 州/省：`x-lpm-state: <state>`
    * 城市：`x-lpm-city: <city_name>`
  </Accordion>

  <Accordion title="如何覆盖端口的国家/地区设置？">
    要覆盖端口中选择的国家/地区，您可以使用所选国家/地区代码发送 'x-lpm-country' 标头。

    ```sh theme={null}
    curl --proxy [LPM_DOMAIN]:[PORT] -H "x-lpm-country: il" "[http://brdtest.com/myip.json](http://brdtest.com/myip.json)"
    ```
  </Accordion>

  <Accordion title="如何设置自动跟随重定向？">
    自动跟随重定向是代理管理器中一项有价值的功能，可增强您对 30X（重定向）错误处理的控制。此功能位于端口设置中的“通用”选项卡下。它为您提供了一个选项，即在遇到 30X 错误时自动发送新请求，新请求的目标 URL 源自 Location 响应标头。本文档将指导您启用和使用此功能。

    **访问自动跟随重定向：**

    1. 打开要激活自动跟随重定向的所需端口
    2. 转到“通用”选项卡：在端口设置中，点击“通用”选项卡。您将在此处找到与代理处理请求和响应方式相关的各种设置。
    3. 切换自动跟随重定向功能：在“通用”选项卡中，您将看到“自动跟随重定向”功能。它以切换按钮的形式呈现，允许您根据需要启用或禁用它。

    **自动跟随重定向的工作原理：**

    * 启用自动跟随重定向功能后，它会指示代理管理器响应 30X 错误自动发送新请求。
    * 新请求的 URL 是根据 30X 错误响应中收到的 Location 响应标头确定的。
    * 这允许您的代理无缝地跟随重定向，并确保请求被发送到 Location 标头指定的正确目标。

    **自动跟随重定向的益处：**

    在不支持或不希望自动重定向的环境中，自动跟随重定向功能为您提供了完全控制。
  </Accordion>

  <Accordion title="如何使用会话标头控制会话一致性？">
    您可以通过发送 x-lpm-session 标头来使用代理管理器控制您的会话。

    * 添加带有任何随机会话 ID 的标头："x-lpm-session: random\_session"
    * 当使用相同的会话时，代理管理器将尝试连接到相同的出口节点（对等点/IP）
    * 当您更改会话值时，代理管理器将连接到不同的出口节点（新的对等点/IP）
    * 为了保持给定会话的活动状态，您必须每隔 7 分钟发送一次请求
    * 请注意，为了在 HTTPS 请求中使用它，您需要启用 SSL 分析并安装证书

    这是一个示例：

    ```sh theme={null}
    curl --proxy [http://127.0.0.1:24000](http://127.0.0.1:24000) -H "x-lpm-session: rand123" [http://brdtest.com/myip](http://brdtest.com/myip)
    ```
  </Accordion>

  <Accordion title="如何在云代理管理器上刷新会话？">
    您可以使用以下 curl 请求在云代理管理器上刷新会话：

    ```sh theme={null}
    curl -X POST "https://pmgr-customer-<customer_id>.brd.superproxy.io:22999/api/refresh_sessions/<port>"
    ```
  </Accordion>

  <Accordion title="如何从代理管理器导出日志？">
    在代理管理器中，我们为用户提供了一系列选项，可将日志导出到外部存储和日志监控系统。这些导出选项允许您高效地集中和分析您的日志。在本说明文档中，我们将概述可用的日志导出选项，并指导您如何通过代理管理器设置配置它们。

    **日志导出选项：**

    代理管理器提供以下日志导出选项：

    **Logz.io**

    通过指定您的 Logz.io 令牌、主机和其他所需参数，在代理管理器设置中配置 Logz.io 集成。

    **AWS S3：**

    要将日志导出到 AWS S3，请在代理管理器设置中设置 S3 集成。您需要指定您的 AWS 访问密钥、秘密密钥、S3 存储桶名称和其他相关详细信息。

    **Webhook：**

    在代理管理器设置中配置 Webhook 端点以及任何必需的身份验证详细信息和 URL，以开始通过 Webhook 导出日志。

    **Datadog：**

    要将日志导出到 Datadog，请通过提供您的 Datadog API 密钥和其他相关信息，在代理管理器设置中设置 Datadog 集成。

    **配置日志导出：**

    要配置代理管理器中的日志导出，请遵循以下一般步骤：

    1. 访问代理管理器设置：
    2. 导航到设置或配置部分。
    3. 在“启用请求日志”中选择“日志设置”选项
    4. 切换打开“使用远程日志聚合器”
    5. 选择所需的日志导出选项 (Webhook, Datadog, Logz.io, or AWS S3)。
    6. 提供配置详细信息：对于所选的导出选项，您通常需要提供特定的配置详细信息。这可能包括端点 URL、API 密钥、身份验证凭据和存储设置。
    7. 点击“测试”以检查配置
    8. 点击“确定”并“保存更改”

           <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/proxy-networks/proxy-manager/faqs/logs-settings.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=2d60acc48716f611189e757e25a5566a" alt="logs-settings.png" width="1029" height="644" data-path="images/proxy-networks/proxy-manager/faqs/logs-settings.png" />

    通过遵循这些步骤，您可以有效地配置代理管理器将日志导出到您选择的外部存储或监控系统，从而增强您有效监控和管理网络和应用程序的能力。
  </Accordion>

  <Accordion title="如何取消阻止错误代码？">
    错误代码响应可以通过以下步骤触发 IP 刷新或使用新的 IP 进行重试：

    * 在代理管理器的“规则”选项卡中添加新规则
    * 选择“状态码”作为规则类型
    * 通过选择相关的状态码来触发规则（例如 501, 402, 301 等）
    * 选择所需的结果，例如“刷新 IP”或“使用新的 IP 重试”

    观看视频：[取消阻止错误代码](https://www.bright.cn/video/unblock_error_codes)
  </Accordion>

  <Accordion title="如何通过 HTTPS 运行用户界面（仪表板）">
    **需要什么？**

    为了能够使用 HTTPS 协议访问用户界面（仪表板），您需要为代理管理器提供您域名的 SSL 证书和私钥。

    证书和私钥应专门为您的域名生成并安装在服务器上。这通常是通过服务器和域名提供商完成的

    **如何操作？**

    运行代理管理器时，同时使用指向相应证书文件的环境变量 `SSL_CERT` 和 `SSL_KEY`。在终端中运行的示例命令：

    ```sh theme={null}
    SSL_CERT=/path/to/ca.crt SSL_KEY=/path/to/ca.key pmgr
    ```

    启动后，您可以使用 [https://your-domain.com:22999/](https://your-domain.com:22999/) 访问用户界面
  </Accordion>

  <Accordion title="如何保存请求/响应历史记录？">
    通过启用 `--history` 标志。启用历史记录模式后，请求和响应标头都将保存到本地数据库。可以在“代理”部分下访问它们。通过启用 '--ssl' 标志，历史记录选项还可以跟踪 HTTPS。有关其他详细信息，请参阅 Bright Data 代理管理器 [GitHub 页面](https://github.com/luminati-io/luminati-proxy#installation)。

    这也可以通过代理管理器仪表板，在“通用设置”部分下启用“记录请求历史记录”和“启用 SSL 嗅探”来完成。
  </Accordion>

  <Accordion title="如何在 Bright Data 的代理管理器中使用 SOCKS5？">
    SOCKS 服务器是一种代理服务器，适用于任何端口上的任何类型的网络协议，它代表用户建立到服务器的连接，然后在用户和服务器之间路由流量。

    为什么在 Bright Data 中使用 [SOCKS5 代理](https://www.bright.cn/solutions/socks5-proxies)？

    当您在 Bright Data 中使用 SOCKS5 时，代理管理器会将任何对端口 80 或端口 443 的请求转换为 http 和 https 请求，因此您无需担心目标网站接受哪种格式。对于任何其他端口，流量都会在用户和主机之间按原样发送。

    使用 SOCKS5 的指南：

    * 打开代理管理器
    * 点击一个端口，然后点击“编辑代理”
    * 在“通用”下添加 SOCKS 端口号
    * 转到“性能” - 将“反向解析”设置为：DNS
    * 添加解析文件

      * 将 '--resolve PATH' 添加到程序代码
      * 遵循 hosts [文件格式](https://en.wikipedia.org/wiki/Hosts_\(file\))
      * 列出您将使用的域及其 IP
      * 在代理管理器“工具”页面中的解析文件编辑器中添加域和 IP

          <Note>
            为了允许 SOCKS5 连接，您需要完成此处所示的 KYC 流程：[https://www.bright.cn/cp/kyc，并请求我们合规部门的批准。如果您在此过程中需要帮助，请联系您的客户经理。](https://www.bright.cn/cp/kyc，并请求我们合规部门的批准。如果您在此过程中需要帮助，请联系您的客户经理。)
          </Note>
  </Accordion>

  <Accordion title="在使用 SOCKS5 协议和代理管理器时如何定义代理 IP 国家/地区？">
    <Warning>
      此选项仅适用于启用了直接接入端口的客户
    </Warning>

    `SOCKS5` 协议使用加密的 base64 字符串进行身份验证。

    因此，当使用 `SOCKS5` 时，如果您需要定义代理 IP 国家/地区 (`-country-<COUNTRY_CODE>`)，则必须将您的基本身份验证信息转换为 base64 令牌：

    * 浏览 [https://www.base64encode.org](https://www.base64encode.org/)
    * 将 `brd-customer-<customer_id>-zone-<zone_name>-country-<COUNTRY>:<zone_password>` 编码为 Base64 格式的令牌
    * 在您发送到代理管理器端口的 `SOCKS5` 请求中使用您生成的“基本授权令牌”标头：

    ```sh theme={null}
    curl -v "[http://brdtest.com/myip.json](http://brdtest.com/myip.json)" --socks5 127.0.0.1:24000 -H "Proxy-Authorization: Basic <Basic authorization token>"
    ```
  </Accordion>

  <Accordion title="如何从 API 切换到代理管理器">
    使用代理管理器提供了 API 中不具备的高级功能。您无需手动编写机制来处理诸如尽可能长时间保持 IP 或在每个请求后轮换 IP 之类的任务，而只需在代理管理器中点击一个按钮即可。

    从 API 切换到代理管理器的指南：

    1. [在此处](https://github.com/luminati-io/luminati-proxy#installation/)安装代理管理器
    2. 更改代码以将 HTTP 请求直接发送到指定端口（例如 127.0.0.1:24000），而不是发送到 brd.superproxy.io：
    3. 通过代理管理器仪表板配置您的自定义代理和区域的设置。您无需随请求发送用户参数（brd-customer-customer\_name-zone-zone\_name…），因为所有所需数据都包含在手动代理配置中。
  </Accordion>

  <Accordion title="如何模仿人类用户？">
    包括所有标头和 Cookie 行为。请参阅使用 Bright Data **代理管理器**的 Bash 示例：

    ```sh theme={null}
    curl -v "[http://brdtest.com/myip.json](http://brdtest.com/myip.json)" -H 'pragma: no-cache' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: en-US,en;q=0.8' -H 'upgrade-insecure-requests: 1' -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36' -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp, image/apng,\*/\*;q=0.8' -H 'cache-control: no-cache' -H 'cookie: bcookie="v=somekindofcookiexxx";' --proxy [http://127.0.0.1](http://127.0.0.1):PORT_NUM
    ```

    <Note>
      使用 Web Unlocker API 时，默认禁用附加标头，请联系支持以批准标头附加。
    </Note>
  </Accordion>

  <Accordion title="如何将代理管理器设置为系统服务？">
    <Steps>
      <Step title="以 'root' 身份登录到远程服务器（运行 Ubuntu）" />

      <Step title="创建服务">
        在以下位置创建新的服务文件：

        ```sh theme={null}
        /etc/systemd/system/pmgr.service
        ```

        ```sh theme={null}
        [Unit]
        Description=Proxy Manager
        Wants=network-online.target
        After=network-online.target

        [Service]
        Type=simple
        Restart=always
        RestartSec=5
        Environment=NODE_ENV=production
        ExecStart=/usr/bin/pmgr
        User=root
        StandardOutput=null
        StandardError=null

        [Install]
        WantedBy=multi-user.target
        ```
      </Step>

      <Step title="重新加载服务文件">
        ```sh theme={null}
        systemctl daemon-reload
        ```
      </Step>

      <Step title="启动代理管理器服务">
        ```sh theme={null}
        systemctl start pmgr
        ```
      </Step>

      <Step title="检查状态：">
        ```sh theme={null}
        systemctl status pmgr.service
        ```
      </Step>

      <Step title="完成！">
        您已完成将代理管理器设置为服务。您现在可以控制您的新服务：

        ```sh theme={null}
        service pmgr [stop|start|restart]
        ```
      </Step>
    </Steps>
  </Accordion>

  <Accordion title="如何查看我的请求详情？">
    在“通用设置”下启用“请求详情”将添加以下响应标头，并允许您更广泛、更具体地查看请求。此功能与使用 `-debug` 标志具有相同的功能。

    * `x-luminati-ip-destination` - 目标主机的 IP
    * `x-luminati-ip` - 分配给请求的 IP。
    * `x-luminati-timeline` - 完成所需的时间

    <Note>
      - 此功能默认在云代理管理器上关闭，如果需要，请确保启用它。
      - 启用“请求详情”对于在规则中实施操作“封禁 IP”是必需的。
    </Note>

    可以通过以下一种（或多种）方式查看这些标头

    <Tabs>
      <Tab title="通过详细标志 (-v)">
        通过使用 `-v` 标志以详细模式发送您的请求
      </Tab>

      <Tab title="查看您的代理管理器日志">
        1. 点击您要检查的特定请求
        2. 点击“标头”
      </Tab>

      <Tab title="在您的浏览器“网络”选项卡中查看">
        1. 通过点击 F12 打开“开发者工具”
        2. 转到“网络”选项卡
        3. 导航到目标 URL
        4. 点击相关的请求
        5. 相关标头将在“响应标头”下
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="如何减少响应中的数据量？">
    * 转到“通用”选项卡
    * 从“SSL 分析”中选择“开启”
    * 转到“规则”选项卡
    * 从“规则类型”下拉列表中选择“URL”
    * 选择任何文件类型以应用正则表达式
    * 从“操作类型”下拉列表中选择“空响应”

    在下面的示例中，对于以任何文件类型结尾（.jpg|.png|.gif 等）的所有请求，代理管理器将返回一个空响应（0kb 且状态码仍为 200）。

    当您希望减少响应中所需获取的数据量时，请使用此选项。
  </Accordion>

  <Accordion title="如何提高我的网络抓取速度？">
    如果通过单个 IP 轮换的请求数量高于目标网站允许的数量，则您目标定位的网站将识别您的 IP 并阻止您或用虚假信息误导您。这意味着您的信息收集可能会比您习惯的慢得多。

    **我能做些什么？**

    假设您运行 1000 万个请求，1000 个数据中心 IP 每秒 1 个请求，您的例程可能需要大约 3 小时。如果使用 10,000,000 个住宅 IP，您的例程可能只需要 1 秒。

    通过 Bright Data 住宅网络轮换多个并行会话的指南：

    1. 打开代理管理器
    2. 转到“概览”菜单
    3. 点击您的住宅区域端口
    4. 将端口设置中的“预设”编辑为“轮换 (IP)”
    5. 将您的请求路由到 `127.0.0.1:<portnum>`，其中 `portnum` 是住宅区域的端口号
  </Accordion>

  <Accordion title="如何知道我是否被伪装（cloaked）了？">
    被伪装意味着您正在从您抓取的网站获得误导性的信息。

    示例：如果您正在收集比较竞争信息以馈送您的自动定价算法，则目标网站可能会向您的请求返回人为降低的价格，以歪曲您的定价和利润。

    **我能做些什么？**

    使用传统代理网络（基于数据中心的 IP）时，您的目标网站可能会很容易识别您的活动，并可能伪装您的请求。因此，确保您不被伪装的唯一方法是通过住宅 IP 轮换您的请求。

    通过数百万住宅 IP 轮换请求的指南：

    1. 打开代理管理器
    2. 转到“概览”选项卡
    3. 点击您的住宅区域端口
    4. 将端口设置中的“预设”编辑为“轮换 (IP)”
    5. 将您的请求路由到 `127.0.0.1:<portnum>`，其中 `portnum` 是住宅区域的端口号
  </Accordion>

  <Accordion title="如何在使用代理管理器时设置长期单会话">
    在端口设置下拉菜单上选择“长期单会话”，它将自动 ping IP 以保持会话活动状态：

    <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/proxy-networks/proxy-manager/faqs/long-single-session.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=5a150a81373aa8dfe3b5d3a91e4bc4a7" alt="long-single-session.png" width="913" height="321" data-path="images/proxy-networks/proxy-manager/faqs/long-single-session.png" />
  </Accordion>

  <Accordion title="如何使用远程 DNS？">
    使用远程 DNS 为您提供一个类似于代理对等点（代理 IP 的来源）的 DNS 解析服务器。这使得您的请求看起来更可信，因为解析服务器通常在地理位置上靠近 IP，而如果不使用远程 DNS，解析服务器是 Bright Data 的超级代理之一，可能位于另一个国家/地区。要使用远程 DNS：

    <Tabs>
      <Tab title="通过代理管理器">
        转到“编辑端口”>“IP 控制”> 将“DNS 查找”设置为“远程 - 由对等点解析”
      </Tab>

      <Tab title="通过 API">
        只需将其添加到您的用户名字符串中。

        例如：

        ```sh Shell theme={null}
        brd-customer-<customer_id>-zone-<zone_name>-dns-remote
        ```
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="如何使用并行代理管理器实例以实现高性能？">
    当您不想用太多请求使一个代理管理器超载时，您可以在不同的服务器上创建代理管理器的多个实例。

    最好的方法是遵循以下步骤：

    * 在本地安装代理管理器并根据需要设置所有端口
    * 保存配置文件
    * 打开同步配置，以便所有更改都将自动在所有机器上保持同步
    * 在您想要使用的服务器上安装代理管理器
    * 将配置文件 **导入** 到服务器中的 `proxy_manager` 目录

    在服务器之间拆分您的流量

    ```js theme={null}
    request 1 -> {FIRST SERVER IP}:24000
    request 2 -> {SECOND SERVER IP}:24000
    ```

    使用此方法使用代理管理器将确保您不会使一个代理管理器实例超载，并且将帮助您在所有实例中保持相同的配置。

    这意味着您可以在每个实例上同时从同一个端口发送具有相同国家/地区的请求。

    如果您在自行设置此负载均衡时遇到问题，您可以使用我们已实现负载均衡功能的 [云服务](https://www.bright.cn/cp/lpm)。您只需使用 1 个用户界面并控制具有共享配置的所有实例，然后定位相同的 URL，我们将自行处理整个负载均衡过程。
  </Accordion>

  <Accordion title="我无法登录本地代理管理器">
    如果您无法登录 [代理管理器](/cn/proxy-networks/proxy-manager/introduction) (PM)，请执行以下操作：

    * 确保运行 PM 的计算机没有使用 VPN。

          <Note>
            请注意，运行 PM 时使用 VPN 可能会导致登录问题，还会减慢连接到代理的速度
          </Note>
    * 关闭 PM（运行 PM 的终端黑屏）
    * 删除浏览器上的 Cookie
    * 再次打开 PM（PM 需要大约 1-2 分钟才能加载）
    * 尝试使用您之前使用相同方法（通过使用 Google，或使用您注册的邮箱和密码）登录

    或者，您可以将代理管理器的托管切换到我们的 [云服务](https://www.bright.cn/cp/lpm)。我们将负责托管，甚至负责多个代理管理器实例之间的负载均衡。

    附注：PM 加载后，默认浏览器应自动打开 PM 的登录页面。如果未打开，请打开您的浏览器，浏览 127.0.0.1:22999，然后尝试登录。
  </Accordion>

  <Accordion title="代理管理器连接错误（端口状态不是 &#x22;ok&#x22;）">
    如果您无法登录代理管理器，或如果代理管理器无法连接到超级代理（即端口状态不是 OK），请检查以下内容：

    * 确保 VPN 未打开
    * 确保没有杀毒软件或任何其他安全软件（例如 360、Norton 等）阻止从代理管理器发送的流量
    * 确保防火墙（操作系统 / 服务器 / 任何其他安全软件的防火墙）允许 TCP 流量通过端口 22000-25000
    * 如果代理管理器软件安装在 macOS/Linux 服务器上 - 验证：
      * Node.js 版本在 12.18.3 和 14.18.1 之间
      * NPM 版本在 6.14.6 和 8.1.3 之间
      * 如果 NPM 和 Nodejs 版本不是我们支持的版本 - 请移除它们并安装我们指定的版本。有关 Linux/Mac 安装的更多信息，请参阅我们的 [GitHub 页面](https://github.com/luminati-io/luminati-proxy/#linuxmacos---manual-install)
  </Accordion>

  <Accordion title="为什么我会收到 '400 Proxy Error: ip_requested_not_allocated_by_customer' 错误？">
    在使用数据中心/ISP 或 gIPs 产品时，如果您的区域下的 IP 已刷新、移除或因系统更新而简单地更改，则可能会出现错误代码 `400`

    <Note>
      * 此错误通常在您的 BrightData 账户最近被暂停后出现。如果您的账户余额变为负数，则会自动暂停。如果暂停时间超过 24 小时，静态分配的 IP 将从您的账户中释放。重新激活后，重新分配的 IP 可能与原始 IP 不同，因此如果仍然定位以前分配的 IP - 则会抛出此错误。
    </Note>

    每当出现此错误时，您应该转到您的 Bright Data 区域页面，下载与此区域相关的新 IP 列表。

    如果您使用带有 IP 端口设置前缀的代理管理器工具，请确保也更新 IP 列表

    示例：

    ```sh Shell theme={null}
    curl --v "[http://brdtest.com/myip.json](http://brdtest.com/myip.json)" --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-ip-1.1.1.1:<zone_password>
    ```

    <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/proxy-networks/proxy-manager/faqs/shell-example.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=35a652a041cf58c6d4f285080d17ebe2" alt="shell-example.png" width="1600" height="630" data-path="images/proxy-networks/proxy-manager/faqs/shell-example.png" />
  </Accordion>

  <Accordion title="如何获取来自特定位置的 IP？">
    使用 Bright Data，您可以指定用于发送流量的 IP 的地理位置和其他参数。在代理管理器中这尤其容易，因为它只需点击几下。

    根据您使用的区域，您可以请求仅来自特定国家/地区的 IP（如果您使用住宅或数据中心网络），或附加特定运营商（如果您使用移动网络）。

    **如何在代理管理器中设置目标定位？**

    要获取来自特定位置的 IP，请按照以下步骤操作：

    * 点击您想要使用特定位置 IP 的代理端口
    * 转到 **“目标定位”** 选项卡
    * 选择国家/地区、州/省、城市以选择特定地理位置的对等点
    * 选择 ASN 或运营商名称（仅适用于移动对等点）
  </Accordion>

  <Accordion title="代理管理器适用于哪些 Bright Data 产品？">
    代理管理器支持以下 Bright Data 产品：数据中心代理、ISP 代理、住宅代理、移动代理、解锁器 API、SERP API \
    代理管理器不支持浏览器 API。
  </Accordion>

  <Accordion title="如何下载代理管理器？">
    我们建议您在我们的云服务器上将代理管理器作为服务运行，以获得更好的体验。如果您需要在本地机器上安装它，请使用以下链接。

    ### Windows

    [下载适用于 Windows 的代理管理器安装程序](https://github.com/luminati-io/luminati-proxy/releases/download/v1.519.10/luminati-proxy-manager-v1.519.10-setup.exe)

    ### Linux & MacOS

    `bash `安装程序：

    ```sh theme={null}
    curl -L [https://www.bright.cn/static/lpm/luminati-proxy-latest-setup.sh](https://www.bright.cn/static/lpm/luminati-proxy-latest-setup.sh) | bash
    ```

    `NPM `软件包安装程序：

    ```sh theme={null}
    sudo npm install -g @luminati-io/luminati-proxy
    ```

    `Docker`镜像：

    ```sh theme={null}
    docker pull luminati/luminati-proxy
    ```

    ### 源代码

    [https://github.com/luminati-io/luminati-proxy](https://github.com/luminati-io/luminati-proxy)
  </Accordion>
</AccordionGroup>
