> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SOCKS 和 SOCKS5 代理

> 了解如何使用 SOCKS 和 SOCKS5 协议与 Bright Data 代理网络

## 支持的 SOCKS 协议

Bright Data 支持 SOCKS 协议版本 5：`SOCKS5`。

## 将 SOCKS5 用于您的抓取任务

互联网数据收集最常见的协议是 `HTTP` 和 `HTTPS`，某些工具或实用程序需要 `SOCKS5` 来进行操作。

在 Bright Data 中，我们不区分 `HTTP`、`HTTPS` 和 [`SOCKS5 代理`](https://www.bright.cn/solutions/socks5-proxies)：我们的所有代理都支持这三种协议。您可以在使用同一代理时在协议之间切换。

## 您真的需要 SOCKS5 吗？

我们的 `HTTP` 和 `HTTPS` 代理解决方案通常最适合抓取网站，提供最低成本和最高性能。但是，如果任务仍然需要 `SOCKS5`，Bright Data 可以在全球范围内提供质量代理。

## 支持的代理类型和 HTTP 协议

`SOCKS5` 代理连接在所有 Bright Data 代理网络上都支持：数据中心、ISP、住宅和移动代理。

Bright Data 仅通过 SOCKS 支持 HTTP/S 版本 2.0。

我们不支持通过 SOCKS 隧道传输 HTTP/2 版本 3.0。

<Info>
  使用 Bright Data **住宅代理**上的 `SOCKS5` 仅支持 `HTTPS` 目标，`HTTP` 目标将很快支持。
</Info>

## SOCKS5 主代理端口配置

<Note>
  **`Bright Data 使用端口 22228 进行 SOCKS5`**
</Note>

使用 `SOCKS5` 时，请确保使用 `brd.superproxy.io:22228`，而不是用于 `HTTP` 和 `HTTPS` 协议的标准端口 <Tooltip tip="端口 44445 是推荐使用的代理端口，点击了解更多">[`44445`](/general/faqs#which-port-shall-i-use-22225-or-33335)</Tooltip>。

## Bright Data 的 SOCKS5 目标定位

<Warning>
  **Bright Data 仅支持 SOCKS5 代理的主机名（域名）**
</Warning>

根据我们的合规规定，我们仅允许 `SOCKS5` 请求使用作为目标中继的主机名/域名。使用显式 IP 或本地 IP 解析发送的请求被**阻止**。

因此，请配置您的代码、客户端或调用应用程序以：

1. 使用域名作为目标
2. 远程解析 DNS，而不是本地解析

遵守这些规则将确保请求通过我们的代理对等方到达目标域 IP。

### 目标端口

#### 数据中心和 ISP

Bright Data 支持数据中心和 ISP 代理的所有高于 `1024` 的端口。

#### 住宅和移动

Bright Data 支持住宅和移动代理的端口：`8080`、`8443`、`5678`、`1962`、`2000`、`4443`、`4433`、`4430`、`4444` 和 `1969`。

## 使用 SOCKS5 与 `curl`、`Javascript` 和 `Python`

<Tabs>
  <Tab title="curl">
    <Warning>
      **`发出 curl 请求时使用 socks5h://brd.superproxy.io:22228`**
    </Warning>

    要将 `curl` 与 Bright Data SOCKS5 代理一起使用，您必须明确地：

    1. 在命令行参数中添加 `-x`
    2. 使用 SOCKS5h 协议进行远程 DNS 查询
    3. 使用代理地址 `brd.superproxy.io:22228`
    4. 提供 Bright Data 代理区域凭据
    5. **住宅和移动代理**：添加 curl `-k` 选项以忽略 SSL 错误代理或 [设置 SSL 证书](/general/account/ssl-certificate#using-the-ssl-certificate-in-your-code)

    不符合上述所有要求的请求将被阻止。

    示例 `curl` 命令：

    ```
    curl -i -k -x socks5h://brd.superproxy.io:22228 --proxy-user [USERNAME]:[PASSWORD] "https://geo.brdtest.com/welcome.txt"
    ```
  </Tab>

  <Tab title="Javascript">
    `SOCKS5` 请求的示例代码：

    ```javascript theme={null}
    // install https://www.npmjs.com/package/socks-proxy-agent
    const https = require('https');
    const { SocksProxyAgent } = require('socks-proxy-agent');
    const user_pass = 'brd-customer-[ACCOUNT ID]-zone-[ZONE NAME]:[ZONE PASSWORD]';
    const socks_proxy_url = `socks5h://${user_pass}@brd.superproxy.io:22228`;
    const agent = new SocksProxyAgent(socks_proxy_url);
    https.get('https://geo.brdtest.com/welcome.txt', {agent},
      res=>res.pipe(process.stdout));
    ```
  </Tab>

  <Tab title="Python">
    `SOCKS5` 请求的示例代码：

    ```python theme={null}
    # https://docs.python-requests.org/en/latest/user/advanced/#socks
    import requests
    user_pass = 'brd-customer-[ACCOUNT ID]-zone-[ZONE NAME]:[ZONE PASSWORD]'
    socks_proxy_url = f'socks5h://{user_pass}@brd.superproxy.io:22228'
    resp = requests.get('https://geo.brdtest.com/welcome.txt',
      proxies=dict(http=socks_proxy_url, https=socks_proxy_url))

    print(resp.text)
    ```
  </Tab>
</Tabs>

#### 使用 `curl` 进行故障排除

我们建议使用 `curl` 对您的 `SOCKS5` 请求进行故障排除，并添加 `curl` 选项 `-i` 或 `-v` 以打印标头字段。查找 `x-brd-error`、`x-brd-err-code` 和 `x-brd-err-msg` 以获取 Bright Data 代理网络发送的详细错误消息。
要查看我们的完整错误目录（对于 `HTTP` 和 `HTTPS` 以及其他），请访问此页面：[代理错误故障排除](/proxy-networks/errorCatalog)

## SOCKS5 身份验证配置

<Note>
  **Bright Data 必须接收代理区域凭据以访问 SOCKS5 代理**
</Note>

身份验证的方式与 `HTTP` 和 `HTTPS` 类似，通过中继代理访问的用户名和密码。

某些工具或实用程序会为您提供单独作为参数输入凭据和端口的位置，如控制面板中所示，有些则要求您以单个参数分隔符提供 URL：`userName:password@brd.superproxy.io:22228`。

## SOCKS5 地理位置和国家/地区选择

位置设置与 [HTTP/HTTPS 代理地理位置定位](/proxy-networks/config-options)相同，通过将 `-country-[country code]` 添加到您的 SOCKS5 用户名来设置。

用于获取意大利（国家代码：`it`）中的 SOCKS5 代理的 `curl` 命令示例：

```
curl -i -k -x socks5h://brd.superproxy.io:22228 --proxy-user [proxy zone user]-country-it:[zone password] "https://geo.brdtest.com/welcome.txt" -v
```

## SOCKS5 和 SOCKS5h 之间的差异

**SOCKS5** 和 **SOCKS5h** 之间的差异在于它们如何处理 DNS（域名系统）解析：

1. **SOCKS5**：在标准 SOCKS5 代理中，**客户端**解析 DNS。这意味着域名（例如 `example.com`）在通过代理之前被解析为 IP 地址\*\*。然后代理将流量路由到已解析的 IP 地址。
2. **SOCKS5h**："h" 代表"主机名"。在这种情况下，**代理**服务器解析 DNS。客户端将域名（而不是 IP 地址）发送到代理服务器，代理服务器解析它并转发请求。如果您想隐藏客户端网络中的目标域名，这会很有用。

总结一下：

* **SOCKS5**：DNS 解析在**客户端**进行。
* **SOCKS5h**：DNS 解析在**代理端**进行。

Bright Data 仅支持**代理端** SOCKS5h。
