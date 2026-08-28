> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何配置代理管理器

> 了解更多关于代理管理器可以做什么、如何根据您的需求定制它以及如何实现流行的优化工作流程。

## 下载并安装代理管理器

***

我们的代理管理器易于在您的本地计算机或我们托管的云服务器上设置和维护。我们推荐使用云服务器设置，以获得代理管理器提供的所有功能。

### Bright Data 云托管

避免自行搭建本地代理管理器时服务器资源和网络设置的麻烦——云实例将让您专注于您的操作。

我们提供了一个多实例云，通过一个统一用户界面来控制您的代理管理器的操作。

* 要启用此选项，请在您账户中的[代理管理器页面](https://www.bright.cn/cp/lpm)上选择 **激活**，实例将自动提供。

<Note>
  要使代理管理器仪表板在您的浏览器中运行，必须在浏览器中**允许第三方 Cookie**。
</Note>

### 在您托管的环境（云/本地）上下载并安装代理管理器

Bright Data 为每个平台提供安装程序。最低主机要求至少为：

* 4GB RAM

* 2 CPU

* 3GB HDD

相应操作系统的下载和安装方法：

<Tabs>
  <Tab title="Windows">
    从我们的 [GitHub](https://github.com/luminati-io/luminati-proxy) 版本中下载 [Installer](https://github.com/luminati-io/luminati-proxy/tags) 文件。
    <Tip>请务必下载最新版本。</Tip>
  </Tab>

  <Tab title="Linux/MacOS">
    <Warning>不支持 Linux CentOS 8.x（请改用 CentOS 7.x！）</Warning>

    <Accordion title="Linux/macOS 要求">
      * 确认推荐的硬件要求：

        1. 4GB RAM
        2. 2 个 CPU
        3. 3GB SSD

      * 确认推荐的软件要求：
        * [Node.js](https://nodejs.org/en/about/) 支持的版本：`12.18.3 - 14.18.1`
        * [NPM](https://docs.npmjs.com/about-npm) 支持的版本：`6.14.6 - 8.1.3`

                <Note>
                  您可以手动安装 NPM v6.14.6：

                  ```sh theme={null}
                  sudo npm install -g npm@6.14.6
                  ```
                </Note>

      * 确认网络流量未受限制：
        * 服务器/计算机不使用任何 VPN 或代理 IP！
        * 操作系统防火墙已关闭
        * TCP 端口 20000-30000 允许出入流量
    </Accordion>

    * 通过在终端中运行以下命令之一来安装代理管理器：
      ```sh theme={null}
      curl -L [https://www.bright.cn/static/lpm/luminati-proxy-latest-setup.sh](https://www.bright.cn/static/lpm/luminati-proxy-latest-setup.sh) | bash
      wget -qO- [https://www.bright.cn/static/lpm/luminati-proxy-latest-setup.sh](https://www.bright.cn/static/lpm/luminati-proxy-latest-setup.sh) | bash
      sudo npm install -g @luminati-io/luminati-proxy
      ```

    您可以在[手动安装说明](https://github.com/luminati-io/luminati-proxy#linuxmacos---manual-install)中找到更多信息。
  </Tab>

  <Tab title="Docker">
    Docker 镜像可以在[此处](https://hub.docker.com/r/luminati/luminati-proxy/)找到

    ```sh theme={null}
    docker pull luminati/luminati-proxy
    docker run luminati/luminati-proxy proxy-manager
    docker run luminati/luminati-proxy proxy-manager --version
    ```

    * 确保转发适当的端口。代理管理器默认使用 22999 作为 Web 控制台和 API，<Tooltip tip="端口 44445 是推荐使用的代理端口，点击了解更多">[`44445`](/cn/general/faqs#我应该使用哪个端口-22225-还是-33335) </Tooltip> 用于直接接入，以及 24000-24... 用于您将创建的所有端口。
    * 要使用 cli 选项运行 docker，请参阅以下示例：
      ```sh theme={null}
      sudo docker run -v ~/proxy_manager:/lpm -p 127.0.0.1:22999:22999 -p 127.0.0.1:22998:22998 -p 127.0.0.1:24000:24000 luminati/luminati-proxy pmgr --www_whitelist_ips 172.17.0.1 --config /lpm/config.json
      ```
  </Tab>
</Tabs>

***

## 预设

***

<Tabs>
  <Tab title="长期单会话 (IP)">
    如果您需要完整页面加载，请使用此预设。从浏览器（例如 Chrome/Firefox）或以编程方式（例如 Puppeteer/Selenium）手动连接。所有请求共享相同的 IP。您可以从用户界面或 API 控制何时刷新 IP。
  </Tab>

  <Tab title="轮换">
    如果您希望在每个请求中获得全新的 IP，请使用此预设。此预设还会自动轮换 User-Agent 标头。它最适用于在您不加载完整页面时进行 API 抓取。
  </Tab>

  <Tab title="自定义">
    构建适合您需求的预设

    <Note> 使用自定义预设需要在投入生产之前在内部环境中进行测试，以验证流程是否按预期工作</Note>
  </Tab>
</Tabs>

## 规则和标头

***

导航到“规则”并开始根据触发器构建您自己的规则，例如：

* URL 后缀
* 状态码
* 响应正文中找到的字符串值
* 请求延迟

您可以选择对每个触发器分别采取的行动。

例如，实施一条规则通过取消媒体 URL 的输出来节省带宽。

此外，您可以在“规则”部分预先实施所需的标头。

例如，添加 i686 CPU 上 Linux 桌面的 user-agent 标头（有关 user-agent 的更多信息可以在[此处](https://developers.whatismybrowser.com/useragents/explore/)找到）

## 端口目标定位

***

Bright Data 代理管理器支持使用 IP:PORT 格式定位代理。例如，当代理管理器安装在本地时，定位索引为 24000 的[端口](/cn/api-reference/proxy-manager/create_a_new_proxy_port)：

```sh theme={null}
curl --proxy 127.0.0.1:24000 https://target.site
```

Here’s the translated MDX following all your rules:

<Note>
  如果远程安装，只需将 127.0.0.1 替换为远程服务器的 IP 地址即可。（而不是 IP:PORT USERNAME:PASSWORD）
</Note>

```sh theme={null}
curl --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>:<zone_password> "https://target.site"
```

这允许：

* 从请求中移除 username:password 部分。
* 与只接受 IP:Port 格式的第三方软件集成。
* 代码更整洁。端口可以预先配置所有必要的 headers 和规则，无需调整命令/请求本身。更多信息可在[此处](/cn/api-reference/proxy-manager/update_a_proxy_port)查看。

## 添加外部代理

***

Bright Data Proxy Manager 支持来自其他供应商的外部代理。连接外部代理将允许您在一个地方优化和管理所有代理。

* 登录您的 Proxy Manager
* 设置一个新端口
* 选择 'External'
* 按如下格式添加您的代理

```js theme={null}
[
  '<proxy_peer_IP>', '<username>:<password>@<proxyprovider_server>:<port>'
]
```

* 点击 'Save'，外部代理将作为 Proxy Manager 端口之一可用

<Frame>
  <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/proxy-networks/proxy-manager/configuration/external-sources.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=3e8d62df4a6def4d1aa026e0ae10ee21" alt="" width="612" height="431" data-path="images/proxy-networks/proxy-manager/configuration/external-sources.png" />
</Frame>

## 流量计算差异

***

Proxy Manager 是请求发起方与我们的 Super Proxy 服务器之间的中间人。Proxy Manager 的统计信息可在[此处](https://www.bright.cn/cp/lpm)查看，Super Proxy 的统计信息可在[此处](https://www.bright.cn/cp/zones)查看。因此，每个发送到 Proxy Manager 的请求最终都会到达 Super Proxy。但流量计算可能存在差异，原因如下：

* Proxy Manager 在发送请求时就计算流量，但在请求到达 Proxy Manager 后，它会附加额外的 headers，因此该请求的响应将包含更多关于请求流程的信息（时间线、代理 IP 等）。
* 从 Proxy Manager 到达 Super Proxy 服务器的请求带有这些附加参数；这就是 Super Proxy 计算的请求量比最初到达 Proxy Manager 时略大。
* Proxy Manager 有时会添加 headers 以呈现更好的日志视图，但这些数据不会计入账单。

总之，主要的流量统计来源应为[Zones](https://www.bright.cn/cp/zones)页面，因为它代表了 Super Proxy 形成的统计数据。

按照规则 — Bright Data 使用[Zones](https://www.bright.cn/cp/zones)页面进行计算，作为唯一可信来源

发票和计费事件将基于 Zones 的计算触发
