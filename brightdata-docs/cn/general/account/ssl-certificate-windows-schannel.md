> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Windows curl 端口 44445 SSL 错误

> 修复 Windows Schannel curl 在 Bright Data 代理端口 44445 上出现的 CRYPT_E_REVOCATION_OFFLINE 和 CERT_TRUST_REVOCATION_STATUS_UNKNOWN 错误。

本指南说明如何修复使用 Schannel TLS 后端的 Windows curl 在连接 Bright Data 代理端口 `44445` 时出现的 SSL 吊销检查错误。在 curl 命令中添加 `--ssl-revoke-best-effort` 参数即可解决：

```sh theme={null}
curl -i -v \
  --ssl-revoke-best-effort \
  --proxy brd.superproxy.io:44445 \
  --proxy-user brd-customer-<customer_id>-zone-<zone_name>:<zone_password> \
  --cacert brightdata_root_ca_44445.crt \
  "https://geo.brdtest.com/mygeo.json"
```

请求应返回您的地理位置 JSON，HTTP 状态码为 200。该参数保持正常的 SSL 验证，仅在 Schannel 无法确认证书吊销状态时阻止请求失败。

## Schannel 会显示哪些错误？

受影响的 Windows curl 在 TLS 握手期间会因 `CRYPT_E_REVOCATION_OFFLINE` 或 `CERT_TRUST_REVOCATION_STATUS_UNKNOWN` 而失败。在详细模式（`-v`）输出中，错误如下所示：

```text theme={null}
schannel: next InitializeSecurityContext failed:
CRYPT_E_REVOCATION_OFFLINE (0x80092013)
The revocation function was unable to check revocation because the
revocation server was offline.
```

使用 `--cacert` 传入证书时，CA 文件可以正常加载，但握手仍在吊销检查阶段失败：

```text theme={null}
schannel: added 1 certificate(s) from CA file
schannel: CertGetCertificateChain trust error
CERT_TRUST_REVOCATION_STATUS_UNKNOWN
```

这两个错误的含义相同：Bright Data 根证书有效且已正确安装，但 Schannel 无法确认其吊销状态，并将此视为致命错误。

## 为什么 Schannel 在端口 44445 上失败？

Schannel 执行严格的证书吊销检查，并将根证书缺少吊销信息视为致命错误。在 2026 年 7 月推出的端口 `44445` 证书链中，Bright Data 将 CRL 分发点（CRL Distribution Point）从根 CA 移到了中间证书和叶证书。

旧版根 CA 包含以下扩展：

```text theme={null}
X509v3 CRL Distribution Points:
  Full Name:
    URI:http://crl.brightdata.com/proxy_ca.crl
```

新版 `brightdata_root_ca_44445.crt` 根 CA 不再包含该扩展。这是正确的证书链设计：根 CA 是自签名的信任锚，吊销信息应当由中间证书和叶证书承载。基于 OpenSSL 或 LibreSSL 的 curl（包括所有 Linux 和 macOS 版本）可以正常接受新证书链，只有基于 Schannel 的 Windows curl 可能失败。

## 如何检查 curl 的 TLS 后端

运行 `curl -V` 并查看输出的第一行。Windows 10 和 Windows 11 自带的 curl 使用 Schannel：

```text theme={null}
curl 8.x.x ... Schannel ...
```

不受影响的版本会显示 `OpenSSL` 或 `LibreSSL` 而不是 `Schannel`。如果您的 curl 显示 Schannel，请使用下面两种修复方法之一。

## 添加 --ssl-revoke-best-effort 参数

对于基于 Schannel 的 curl，推荐的修复方法是添加 `--ssl-revoke-best-effort`。根据 curl 官方手册，该参数使 curl 在"因吊销列表分发点缺失或离线导致吊销检查失败"时忽略该检查。此参数仅适用于 Schannel，自 curl 7.70.0 起可用。

添加该参数后，curl 仍会执行以下验证：

* 受信任 CA 验证
* 主机名验证
* 有效期验证
* 证书链验证

<Warning>
  请勿改用 `-k` 或 `--insecure`。这两个参数会完全禁用 SSL 验证，而 `--ssl-revoke-best-effort` 仅放宽 Schannel 无法完成的吊销检查。
</Warning>

## 改用基于 OpenSSL 或 LibreSSL 的 curl

另一种方法是安装基于 OpenSSL 或 LibreSSL 编译的 Windows curl，并通过 `curl -V` 确认后端。这类 curl 对端口 `44445` 证书链的验证方式与 Linux curl 相同，无需额外参数：

```sh theme={null}
curl -i -v \
  --proxy brd.superproxy.io:44445 \
  --proxy-user brd-customer-<customer_id>-zone-<zone_name>:<zone_password> \
  --cacert brightdata_root_ca_44445.crt \
  "https://geo.brdtest.com/mygeo.json"
```

请求成功时会返回您的地理位置 JSON，且没有 SSL 错误。

## 常见问题

### --ssl-revoke-best-effort 会禁用 SSL 验证吗？

不会。`--ssl-revoke-best-effort` 参数保留受信任 CA、主机名、有效期和证书链验证，仅在无法确认证书吊销状态时阻止 Schannel 使请求失败。它不等同于 `-k` 或 `--insecure`，后两者会完全禁用验证。

### 新版 Bright Data 证书是不是不受信任或安装有误？

不是。`CRYPT_E_REVOCATION_OFFLINE` 和 `CERT_TRUST_REVOCATION_STATUS_UNKNOWN` 错误源于 Schannel 对根证书缺少吊销信息的处理方式，而不是证书本身的问题。同一证书在 Linux、macOS 以及基于 OpenSSL 或 LibreSSL 的 Windows curl 上均可正常使用。

### 此问题会影响 Linux 或 macOS 吗？

不会。Linux 和 macOS 的 curl 使用 OpenSSL 或 LibreSSL，不执行 Schannel 的根证书级吊销检查。只有使用 Schannel TLS 后端的 Windows curl 受影响。

## 相关文档

* [根证书迁移](/cn/general/account/ssl-certificate-migration)
* [SSL 证书](/cn/general/account/ssl-certificate)
