> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 根证书迁移

> 在旧证书（端口 22225 和 33335）于 2026 年 9 月 25 日到期之前，迁移到 Bright Data 位于代理端口 44445 的新版根证书。

Bright Data 正在更换其代理端点（包括 `brd.superproxy.io` 以及 `zproxy.lum-superproxy.io` 等旧版主机名）的 SSL 根证书。您必须在当前证书于 **2026 年 9 月 25 日 00:00 UTC** 到期之前，迁移到代理端口 `44445` 上的新证书，以避免服务中断。

<Warning>
  当前证书无法延期或续订。2026 年 9 月 25 日 00:00 UTC 之后，仍依赖端口 `22225` 或 `33335` 旧证书的流量将全部失败。请在此日期之前完成迁移。
</Warning>

## 哪些用户需要迁移

如果您在端口 `22225` 或 `33335` 上使用 Bright Data 代理、SERP API 或 Web Unlocker API，和/或您的代码引用了 Bright Data 的 `.crt` 证书文件，则本次迁移适用于您。

如果您的代码通过 `zproxy.lum-superproxy.io` 或其他 `luminati.io` 时期的旧版主机名连接，本次迁移同样适用。这些主机名已弃用，请在迁移时一并更新为 `brd.superproxy.io`。

如果您通过 Bright Data Proxy API（而非原生代理模式）连接，或者您的账户已通过 [KYC 验证流程](/cn/proxy-networks/residential/network-access#kyc-verification) 且未加载证书，则不受影响。请参阅 [API 与原生访问](/cn/api-reference/authentication)。

## 迁移时间线

端口 `44445` 和新版根证书已于 2026 年 7 月上线。在过渡期内，新旧证书同时有效，您可以在截止日期前按自己的节奏完成迁移。**2026 年 9 月 25 日 00:00 UTC**，端口 `22225` 和 `33335` 上的旧证书到期，仍依赖旧证书的流量将失败。

## 有哪些变化

| 设置   | 迁移前                                                                 | 迁移后                                                                  |
| ---- | ------------------------------------------------------------------- | -------------------------------------------------------------------- |
| 根证书  | `brightdata_root_ca_33335.crt` 或端口 `22225` 证书（均于 2026 年 9 月 25 日到期） | `brightdata_root_ca_44445.crt`                                       |
| 代理端口 | `22225` 或 `33335`                                                   | `44445`                                                              |
| 证书文件 | `brightdata_proxy_ca.zip`                                           | `brightdata_proxy_ca.zip`（更新后的证书包，包含 `brightdata_root_ca_44445.crt`） |

## 前提条件

* 可访问运行爬取代码或应用程序的主机（即加载或安装证书的位置）
* 来自 Bright Data 的新版证书文件
* 能够在网络或防火墙中开放对 `brd.superproxy.io` 端口 `44445` 的出站流量

## 如何迁移到新版证书

1. **开放端口 `44445`**，用于对 `brd.superproxy.io` 的出站流量。如果出站端口受限，请联系您的网络或安全管理员放行。
2. **下载证书包**：从 [www.bright.cn/static/brightdata\_proxy\_ca.zip](https://www.bright.cn/static/brightdata_proxy_ca.zip) 下载，并将 `brightdata_root_ca_44445.crt` 保存到运行代码的主机上。
3. **更新代理主机名和端口**：在所有连接 Bright Data 的代码或工具中，将当前端口（`22225` 或 `33335`）改为 `44445`，并将 `zproxy.lum-superproxy.io` 等旧版主机名替换为 `brd.superproxy.io`。新证书必须与端口 `44445` 配合使用。
4. **加载或安装新版证书**：与您当前使用证书的方式相同。对于在运行时加载证书的代码，将 `--cacert`（或对应语言的等效参数）指向新文件。对于需要安装证书的工具，请按照 [SSL 证书安装](/cn/general/account/ssl-certificate#installation-of-the-ssl-certificate) 中的步骤操作。
5. **测试一个请求**：向 `https://geo.brdtest.com/mygeo.json` 发送请求，确认迁移成功后再切换全部流量。

以下 cURL 示例展示了使用新端口和证书发送请求：

```sh theme={null}
curl --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<account-id>-zone-<zone-name>:<zone-password> --cacert <PATH TO NEW CA.CRT> "https://geo.brdtest.com/mygeo.json"
```

## 如何验证迁移是否成功

* 通过端口 `44445` 向 `https://geo.brdtest.com/mygeo.json` 发送的请求返回您的地理位置 JSON，且没有 SSL 错误。
* 切换端口和证书后，您现有的爬取流量继续正常运行。

如果迁移后请求出现 SSL 错误，请确认运行请求的主机上加载或安装的是新版证书，并且请求的目标端口为 `44445`。如果 Windows 上的 curl 因 `CRYPT_E_REVOCATION_OFFLINE` 或 `CERT_TRUST_REVOCATION_STATUS_UNKNOWN` 而失败，请参阅 [Windows curl 端口 44445 SSL 错误](/cn/general/account/ssl-certificate-windows-schannel)。

如果您在迁移过程中仍然遇到困难，请联系 [support@brightdata.com](mailto:support@brightdata.com)。

## 常见问题

### 如果我未在 2026 年 9 月 25 日前完成迁移会怎样？

2026 年 9 月 25 日 00:00 UTC 之后，仍依赖端口 `22225` 或 `33335` 旧证书的流量将全部失败。旧证书无法延期或续订。

### 过渡期间可以同时使用两个证书吗？

可以。过渡期内新旧证书同时有效，各自对应不同的端口，您可以在 2026 年 9 月 25 日之前按自己的节奏迁移。请对所连接的端口使用相应的证书。

### 如果我的代码忽略 SSL 错误会怎样？

如果您的代码禁用了 SSL 验证（例如 curl 的 `-k` 参数或所用语言的等效设置），证书到期不会导致请求失败，因为证书从未被验证。Bright Data 仍建议您迁移到端口 `44445`，以便您的配置与当前文档和示例代码保持一致。请参阅 [SSL 证书](/cn/general/account/ssl-certificate)页面中的"如何忽略 SSL 错误"部分。

### 为什么 Windows 上的 curl 在端口 44445 上出现吊销检查错误？

使用 Schannel TLS 后端的 Windows curl 可能因 `CRYPT_E_REVOCATION_OFFLINE` 或 `CERT_TRUST_REVOCATION_STATUS_UNKNOWN` 而失败，原因是新版根证书不再包含 CRL 分发点。请在 curl 命令中添加 `--ssl-revoke-best-effort` 参数。详情请参阅 [Windows curl 端口 44445 SSL 错误](/cn/general/account/ssl-certificate-windows-schannel)。

### 本次迁移适用于哪些产品？

在端口 `22225` 或 `33335` 上以原生代理模式使用 Bright Data SSL 证书的 Bright Data 代理、SERP API 和 Web Unlocker API 连接。
