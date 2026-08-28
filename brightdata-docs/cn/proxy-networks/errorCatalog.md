> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 代理错误排查

> 查看 Bright Data HTTP 错误目录，包括错误代码、描述以及解决常见代理问题的操作指南。

本文介绍如何区分代理错误与其他错误，如何分析错误，以及如何排查并解决使用 Bright Data 代理服务时遇到的问题。

## 我如何查看 Bright Data 代理服务的健康状态？

Bright Data 会在此页面发布其产品与服务状态： [https://www.bright.cn/network-status](https://www.bright.cn/network-status) 。在此页面，你可以查看你所使用的产品或全球可用性是否存在问题或事件。你还可以注册电子邮件提醒，当可用性变化或出现大范围事件时将收到通知。

## 如果我发现正在使用的代理网络存在当前事件，该怎么办？

首先，你需要检查你的业务是否受到影响。两个主要指标是响应时间下降（变慢）或错误率上升。如果出现其中任何一种情况，请降低处理速率，并继续下一步排查问题。

## 如何判断我遇到的错误是否来自 Bright Data 代理？

在使用代理时，你可能会遇到并非由 Bright Data 引起的错误。要识别错误来源，请检查响应头中是否包含 Bright Data 的错误字段，我们在这些字段中按代理层级覆盖了大多数错误。

如果你仍无法访问目标网站，或收到 `HTTP` 状态 `200` 但没有预期数据，则很可能已被目标网站屏蔽。在本文： [突破网站封锁](/cn/proxy-networks/website-blocking) 中，我们提供了一些最佳实践。

## 在其他软件中测试 Bright Data 代理时出现 “Proxy Error” 如何解决？

许多软件工具与实用程序使用 Bright Data 代理，并提供 “Test proxy” 功能。当你点击 “Test proxy” 并看到通用的 “Proxy Error” 错误时，该问题可能来自多种原因。

### 常见问题与解决方案

* 目标为搜索引擎如 [google.com](http://google.com) 或 [bing.com](http://bing.com)：Bright Data 限制通过代理网络访问搜索引擎。要解决此问题，请进入软件设置并将测试网址更改为： [https://geo.brdtest.com/welcome.txt](https://geo.brdtest.com/welcome.txt)
* 使用住宅代理网络但未安装证书：Bright Data 不允许在未通过 KYC 或未安装证书的情况下使用住宅代理网络。请阅读不同的访问模式： [Residential Network Access Policy.](/cn/proxy-networks/residential/network-access)

# Bright Data 代理错误排查

## Bright Data 的代理错误格式与标准现支持 RFC9209

自 2025 年 10 月起，Bright Data 在响应负载中支持两组用于传递代理错误的头字段：

1. 私有的 `x-brd-*` 字段：`x-brd-err-code` 与 `x-brd-err-msg`
2. 标准 RFC9209 的 `Proxy-Status` 响应头格式。

`Proxy-Status` 标准字段将在 2026 年逐步替代所有 `x-brd-*` 字段。

## 什么是 RFC9209？

RFC9209 是关于如何在代理响应头中传递代理错误的标准。Bright Data 正在采用该标准并将其应用于所有错误目录。这将帮助客户代码与使用代理作为基础设施的第三方工具更快识别和解决代理交互问题。

你可以在此处了解更多内容： [The Proxy-Status HTTP Response Header](https://www.rfc-editor.org/rfc/rfc9209.html)

## 如何实现 RFC9209？

### Proxy-Status HTTP 头示例

```

Proxy-Status: brd.brighdata.io;
received-status=400;
error=destination_ip_unroutable;
details="client-10060: Requested IP ##.##.##.## is not allocated to this zone. Select an IP that is allocated to this zone or skip the -ip parameter in proxy username."

```

### 实现说明

1. 解析响应头：确保你的系统能够解析 HTTP 响应中的 Proxy-Status 头。

2. 提取相关字段：

   * `received-status`：提供收到的 HTTP 状态码
   * `error`：描述遇到的核心错误
   * `details`：包含具体错误代码及进一步信息
   * 中第一个字段为 Bright Data 错误代码（如 client\_10060）并以冒号分隔
   * 你可以直接使用此前缀浏览错误文档：\
     `https://docs.brightdata.com/cn/proxy-networks/errorCatalog#[Bright data error code]`\
     示例 client\_10060：\
     [https://docs.brightdata.com/cn/proxy-networks/errorCatalog#client\_10060](https://docs.brightdata.com/cn/proxy-networks/errorCatalog#client_10060)

3. 根据这些结构化代码调整错误处理流程，以改进调试效率并确保代理正常运行。

## Bright Data HTTP 代理头字段

以下字段在发送 `HTTP` 或 `HTTPS` 请求时返回：

| Field            | Description                                             | Examples                                                                                                                                                                                                                                  | REST API Field Name |
| :--------------- | :------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| `HTTP Error`     | 协议错误码                                                   | `404` 或 `502`                                                                                                                                                                                                                             | `status_code`       |
| `x-brd-err-code` | Bright Data 模块与错误代码                                     | `client_10001`                                                                                                                                                                                                                            | `error_code`        |
| `x-brd-error`    | Bright Data 主错误信息                                       | Authentication failed                                                                                                                                                                                                                     | `error`             |
| `x-brd-err-msg`  | Bright Data 详细错误与操作建议                                   | Authentication failed. Please check your credentials or review your [account status and billing settings](https://www.bright.cn/cp/settings/billing).                                                                                     | `error_message`     |
| `Proxy-Status`   | RFC9209 兼容响应头，包括代理服务器、HTTP 状态和指向 Bright Data 错误代码的详情字符串 | `Proxy-Status: brd.superproxy.io; received-status=407; error="http_request_denied"; details="client_10000: Invalid authentication: check credentials and retry. Bright Data credentials include your account ID, zone name and password"` | Not supported       |

### 获取 HTTP 头字段

#### 从命令行测试

你可以在 shell 终端使用 `curl` 命令并加上 `-v` 或 `-i` 查看设置或复现问题。这些选项会打印所有头字段，包括自定义错误代码与消息。

```sh theme={null}
curl -v [rest of curl command options]
```

若想仅查看响应头，可使用：

```sh theme={null}
curl -i [rest of curl command options]
```

你也可以使用 `nc` 命令打印字段：

```sh theme={null}
echo "[tcp nc inputs]" | nc -C -v brd.superproxy.io 44445
```

<Note>
  `nc` 输入中可能包含 “空行”，这些对于正确测试是必需的。
</Note>

#### `curl` 命令片段

你所使用 zone 的 **Overview** 标签中提供包含全部参数的 `curl` 命令片段。

#### 通过编程语言访问

Bright Data HTTP 头字段可如同其他 HTTP 头一样在你的程序中读取。

#### 通过 Bright Data 的 Proxy REST API 访问

Bright Data 提供 REST API 以访问代理网络、Web Unlocker API 和 SERP。字段名称略有不同，但内容完全一致。

示例响应：

```JSON theme={null}
"status_code": 407,
"status_message": "Proxy Authentication Required",
"error": "Proxy Authentication Required",
"error_message": "No proxy credentials provided. Please add credentials and try again.",
"error_code": "client_10010"
```

## 错误目录

### HTTP 错误 400

当你在使用 Data Center / ISP 或 gIPs 产品并使用 `-ip-x.x.x.x` 定向标记时，如果你所在 Zone 下的 IP 因系统更新被刷新、移除或变更，就可能出现 `400` 错误码。

<Note>
  这个错误通常会在你的 Bright Data 账户**最近被暂停**后出现。如果账户余额变为负数，系统会自动暂停账户。如果暂停超过 24 小时，你的静态分配 IP 将会被释放。账户恢复后，重新分配的 IP 可能与之前不同，因此如果你的请求仍然指定旧的 IP，就会触发此错误。
</Note>

当出现此错误时，请前往 Bright Data 的 Zones 页面，查看该 Zone 最新的可用 IP 列表。

| 错误代码                                     | `x-brd-error`                            | `x-brd-err-msg`                                                                                                                                            |
| :--------------------------------------- | :--------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span id="client_10060" />`client_10060` | `ip_requested_not_allocated_by_customer` | 请求的 IP `##.##.##.##` 未分配给该 Zone。请选择分配给该 Zone 的 IP，或在代理用户名中移除 `-ip` 参数。                                                                                     |
| <span id="client_10061" />`client_10061` | Peer not found                           | 在默认国家 `%Countries_list%` 中未找到代理。请检查你的默认国家设置，或通过 `-country` 参数指定其他国家以覆盖默认设置。[更多信息](/cn/api-reference/proxy/geolocation-targeting)                           |
| <span id="client_10062" />`client_10062` | Peer not found                           | 你的 `[proxy type] [DC\|ISP]` Zone 在所选国家没有可用 IP。可能是 IP 位置变更，或该 Zone 未配置这些国家的代理。请检查 Zone 配置，并使用相关国家代码重试。[更多信息](/cn/api-reference/proxy/geolocation-targeting) |

### HTTP 错误 401

以下是 HTTP 401 错误对应的 `x-brd-err-code` 值：

| 错误代码                                     | `x-brd-error`                     | `x-brd-err-msg`                                                                                                 |
| :--------------------------------------- | :-------------------------------- | :-------------------------------------------------------------------------------------------------------------- |
| <span id="client_10050" />`client_10050` | Auth failed: IP denylisted `[IP]` | 认证失败，IP 被加入拒绝列表：`[IP]`。参考：[FAQ：如何设置允许/拒绝名单？](/cn/proxy-networks/faqs#how-to-allowlist-denylist-ips-and-domains) |

<span id="http-error-402" />

### HTTP 错误 402

以下为 HTTP 402 错误对应的 `x-brd-err-code`：

<Note>
  以下 402 错误适用于 2026 年 7 月 7 日（含）之前创建的住宅区域，并对这些现有区域持续有效。它们不适用于 2026 年 7 月 7 日之后创建的住宅区域（这些区域需要 KYC）。参见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Note>

| 错误代码                                     | `x-brd-error`                     | `x-brd-err-msg`                                                                                                                                                                               |
| :--------------------------------------- | :-------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span id="policy_20130" />`policy_20130` | Residential Failed `bad_endpoint` | Residential 失败 (`bad_endpoint`) - 请求的网站在即时 Residential（无 KYC）访问模式下不可用，因为 `%HTTP_METHOD%` 请求不被允许。如需完全 Residential 访问权限，请填写 KYC 表单：[https://www.bright.cn/cp/kyc](https://www.bright.cn/cp/kyc) |
| <span id="policy_20140" />`policy_20140` | Residential Failed `bad_endpoint` | 请求的网站在 Bright Data Residential 网络的即时访问模式下不可用，因为目标网站违反 robots.txt。如需访问权限，请参考：[Residential Network Access](/cn/proxy-networks/residential/network-access)                                       |

<span id="http-error-403" />

### HTTP 错误 403

HTTP 403 表示你正在访问一个**有效 URL**，但访问被禁止。服务器处理了请求，但无法返回结果，可能是请求格式错误或者被 Bright Data 策略所限制。

#### `kyc_required`

通过 2026 年 7 月 7 日之后创建的住宅区域发出的请求，若来自使用公司邮箱但尚未完成 KYC 的账户，将返回 HTTP 403。住宅访问仅向经过 KYC 验证的企业开放。2026 年 7 月 7 日（含）之前创建的住宅区域不受影响。

**如何解决：** 完成 [KYC 验证](https://www.bright.cn/cp/kyc)，以便 Bright Data 合规团队批准住宅访问。在此之前，请使用无需 KYC 的 [ISP 代理](/cn/proxy-networks/isp/introduction) 或[数据中心代理](/cn/proxy-networks/data-center/introduction)。参见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。

响应体携带稳定的 `code` 值以及可改为创建的替代方案：

```json theme={null}
{
  "error": {
    "code": "kyc_required",
    "message": "Residential proxies are available to verified companies only, after KYC review, in accordance with Bright Data's compliance policy.",
    "action": "Start verification at brightdata.com/cp/kyc. Applications are reviewed by our compliance team.",
    "alternatives": [
      { "product": "ISP proxy", "plan": { "type": "static", "pool_ip_type": "static_res", "ips_type": "shared" } },
      { "product": "Web Unlocker API", "plan": { "type": "unblocker" } }
    ],
    "docs": "https://docs.brightdata.com/compliance/kyc"
  }
}
```

#### `business_account_required`

通过 2026 年 7 月 7 日之后创建的住宅区域发出的请求，若来自使用个人邮箱的账户（非已验证公司），将返回 HTTP 403。住宅访问仅向已验证企业开放。2026 年 7 月 7 日（含）之前创建的住宅区域不受影响。

**如何解决：** 个人邮箱账户不具备住宅资格，也不会获得 KYC 流程。请使用公司邮箱并联系 Bright Data 团队以确认企业资格。在此之前，请使用无需 KYC 的 [ISP 代理](/cn/proxy-networks/isp/introduction) 或[数据中心代理](/cn/proxy-networks/data-center/introduction)。参见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。

```json theme={null}
{
  "error": {
    "code": "business_account_required",
    "message": "Residential proxies are available to verified companies only. Eligibility requires a corporate email and full verification with the Bright Data team.",
    "action": "Contact the Bright Data team with a corporate email to determine business eligibility for Residential access.",
    "alternatives": [
      { "product": "ISP proxy", "plan": { "type": "static", "pool_ip_type": "static_res", "ips_type": "shared" } },
      { "product": "Web Unlocker API", "plan": { "type": "unblocker" } }
    ],
    "docs": "https://docs.brightdata.com/compliance/kyc"
  }
}
```

以下是 HTTP 403 对应的 `x-brd-err-code`：

| 错误代码                                     | `x-brd-error`                        | `x-brd-err-msg`                                                                                                                                      |
| :--------------------------------------- | :----------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span id="client_10070" />`client_10070` | No Protocol                          | 请求未包含协议。请添加 HTTP 或 HTTPS 后重试。                                                                                                                        |
| <span id="client_10080" />`client_10080` | No Destination Host                  | 未指定目标主机或填写错误。请检查请求参数。                                                                                                                                |
| <span id="client_10090" />`client_10090` | 你正在尝试将 Browser API Zone 当成普通代理使用     | Browser API Zone 必须通过浏览器访问。参考：[Browser API](/cn/scraping-automation/scraping-browser/introduction)                                                   |
| <span id="client_10130" />`client_10130` | 此 super proxy 仅适用于中国域名与中国代理          | 否则请使用 `brd.superproxy.io`。                                                                                                                           |
| <span id="client_10250" />`client_10250` | 目标 `%HOST%` 被禁止                      | 该域名未包含在你的 allowlist 里。请将目标加入 allowlist 或清空 allowlist 以允许全部域名。                                                                                        |
| <span id="client_10260" />`client_10260` | 目标 `%HOST%` 被禁止                      | 该域名被你的 denylist 拒绝。请从 denylist 中移除该域名或清空 denylist。                                                                                                   |
| <span id="policy_20010" />`policy_20010` | Bad protocol                         | 不支持该协议。Bright Data 支持 HTTP、HTTPS、SOCKS5（须特殊申请）。                                                                                                      |
| <span id="policy_20020" />`policy_20020` | Bad port                             | 端口错误。可用端口请参考：[支持的端口](/cn/proxy-networks/faqs#how-to-see-supported-ports-and-protocols)                                                               |
| <span id="policy_20050" />`policy_20050` | 禁止访问：目标站点需要特殊权限                      | 你正在尝试访问根据合规政策不被允许的目标站点。你可能需要完成 KYC 流程：[https://www.bright.cn/cp/kyc](https://www.bright.cn/cp/kyc)。如果你已经通过 KYC，请联系你的客户经理。                            |
| <span id="policy_20051" />`policy_20051` | 禁止访问：目标站点需要特殊权限                      | 该目标站点为政府网站，需要特殊权限才能访问。你可能需要完成 KYC 流程：[https://www.bright.cn/cp/kyc](https://www.bright.cn/cp/kyc)。如果你已经完成 KYC 审批，请联系你的客户经理。                          |
| <span id="policy_20052" />`policy_20052` | 禁止访问：目标站点无法通过所选网络访问                  | 由于合规政策，所选网络类型限制访问此站点。请尝试切换到其他网络类型。如需在同一网络获得访问权限，你可能需要完成 KYC 流程：[https://www.bright.cn/cp/kyc](https://www.bright.cn/cp/kyc)。                         |
| <span id="policy_20080" />`policy_20080` | 禁止访问：该请求必须使用住宅代理网络                   | 你正在访问一个不允许通过 Bright Data 数据中心或 ISP 网络访问的域名。请使用 Residential（住宅）网络 zone 重试请求。                                                                          |
| <span id="policy_20090" />`policy_20090` | 禁止访问：该域名在代理网络中被阻止                    | 该域名在数据中心、ISP 和 Residential 住宅代理网络中均被阻止。请通过 Web Unlocker API zone 或 IDE 工具访问，或联系你的客户经理。                                                               |
| <span id="policy_20091" />`policy_20091` | 禁止访问：目标 `$host` 在 IPv6 协议下被阻止        | 目标 `$host` 在 IPv6 协议下被 Bright Data 阻止。请尝试使用 IPv4 代理或使用 Web Unlocker API 访问该目标。                                                                       |
| <span id="policy_20030" />`policy_20030` | 禁止访问：目标被阻止                           | 你尝试访问 `www.somehost.com` 但被阻止。这可能与你的 denylist 或 allowlist 设置相关，或该站点不允许根据 Bright Data 的政策访问。[了解更多](/cn/proxy-networks/faqs#what-is-error-code-403)    |
| <span id="policy_20000" />`policy_20000` | 访问被拒绝：`<URL>` 被分类为 `<category>` 并被阻止 | `%URL%` 被分类为 `%CATEGORY%`，并因可能违反 Bright Data 使用政策而被阻止。[详情请查看](/cn/proxy-networks/residential/network-access#residential-proxy-network-policy)        |
| <span id="policy_20230" />`policy_20230` | `%COUNTRY%` 不允许作为目标国家                | `%COUNTRY%` 不允许作为目标国家，请修改为其他国家。                                                                                                                      |
| <span id="policy_20250" />`policy_20250` | 禁止访问：你尝试访问 `%HOST%` 但被阻止             | 你尝试访问 `%HOST%` 但被 Bright Data 政策设置阻止。该站点可能违背 Bright Data 政策，或你的账号没有访问该站点的权限。                                                                         |
| <span id="policy_20251" />`policy_20251` | 禁止访问：你尝试访问 `%HOST%` 但被阻止             | 你尝试访问 `%HOST%` 但被 Bright Data 政策设置阻止。该站点可能违背 Bright Data 政策，或你的账号没有访问权限。                                                                             |
| <span id="policy_20260" />`policy_20260` | 禁止访问：你尝试访问 `%HOST%` 但被阻止             | 你尝试访问 `%HOST%` 但被 Bright Data 政策设置阻止。该站点可能违背政策，或你的账号没有相应权限。                                                                                          |
| <span id="policy_20261" />`policy_20261` | 禁止访问：你尝试访问 `%HOST%` 但被阻止             | 你尝试访问 `%HOST%` 但被 Bright Data 政策设置阻止。该站点可能违背政策，或你的账号无访问权限。                                                                                           |
| <span id="policy_20031" />`policy_20031` | 禁止访问：目标 `%HOST%` 被阻止                 | 目标 `%HOST%` 被 Bright Data 阻止。该目标提供与 Bright Data 相关的服务或信息，因此无法通过 Bright Data 代理访问。如需进一步协助，请联系 [support@brightdata.com](mailto:support@brightdata.com) |
| <span id="policy_20040" />`policy_20040` | 禁止的主机                                | 目标主机根据 Bright Data 合规政策或你的账号规则配置被阻止。请在 zone 设置中检查该域名是否允许作为目标：[https://www.bright.cn/cp/zones/](https://www.bright.cn/cp/zones/)                      |
| <span id="policy_20240" />`policy_20240` | 代理端口 `%PORT%` 已被限制                   | 代理端口 `%PORT%` 已被限制。请联系 [Bright Data 支持](mailto:support@brightdata.com)。                                                                              |
| <span id="policy_20110" />`policy_20110` | 禁止的 SERP 域名                          | 目标主机根据 Bright Data 合规政策或你的账号规则配置被阻止。请在 zone 设置中检查该域名是否允许作为目标：[https://www.bright.cn/cp/zones/](https://www.bright.cn/cp/zones/)                      |

### HTTP 错误 407

HTTP 407 表示认证失败，可能是凭据错误，或账户被暂停。

| 错误代码                                     | `x-brd-error`                 | `x-brd-err-msg`                                                                                                                   |
| :--------------------------------------- | :---------------------------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| <span id="client_10000" />`client_10000` | Authentication failed         | 认证失败，请检查凭据（账户 ID、Zone 名、密码）。                                                                                                      |
| <span id="client_10001" />`client_10001` | Invalid Auth                  | 认证无效，请检查凭据。                                                                                                                       |
| <span id="client_10002" />`client_10002` | Zone not found                | Zone 名错误、已禁用或已删除。请确认 Zone 在控制面板中为 Active，或使用 API 查询：[Get Active Zones](/cn/api-reference/account-management-api/Get_active_Zones) |
| <span id="client_10010" />`client_10010` | Proxy Authentication Required | 未提供代理凭据，请补充后重试。                                                                                                                   |
| <span id="client_10020" />`client_10020` | Account is suspended          | 账户已暂停，请[登录激活](https://www.bright.cn/cp/setting/billing)。                                                                          |
| <span id="client_10030" />`client_10030` | Authentication failed         | 该 IP 不允许访问 API，请检查 IP allowlist。                                                                                                  |
| <span id="client_10040" />`client_10040` | KYC Required                  | 请前往 [http://www.bright.cn/cp/kyc](http://www.bright.cn/cp/kyc) 完成验证。                                                              |
| <span id="policy_20120" />`policy_20120` | IP 参数格式错误                     | IP 参数格式错误，请使用 `x-brd-ip` header 格式。                                                                                               |

### HTTP 错误 429

<Note>
  如果你使用的是未充值账户，可能会触及每分钟 1,000 次请求的默认速率限制。你可以在控制面板中查看当前应用的限制，路径为该区域的“概览 (Overview)”选项卡 > 访问详情 (Access details)。向账户充值后，此默认限制将被移除。
</Note>

| 错误代码                                     | `x-brd-error`         | `x-brd-err-msg`                                                                           |
| :--------------------------------------- | :-------------------- | :---------------------------------------------------------------------------------------- |
| <span id="client_10110" />`client_10110` | 请求速率过高                | 你的试用账户超过速率限制。请降低请求量或完成验证流程。                                                               |
| <span id="policy_20220" />`policy_20220` | 对 `%URL%` 请求速率过高      | 目标域名 `%DOMAIN%` 达到速率上限，健康监控正在限流。更多支持请联系 [brightdata.com](http://www.bright.cn/)。          |
| <span id="policy_20221" />`policy_20221` | 对 IP 地理位置数据库的请求受速率限制  | 对 IP 地理位置数据库提供商的请求受速率限制。请改用 Bright Data 无速率限制的地理位置接口：`https://geo.brdtest.com/mygeo.json` |
| <span id="policy_20222" />`policy_20222` | 单 IP 速率过高             | IP `%IP%` 在 Zone `%ZONE%` 的速率达到上限，请增加 IP 数量或降低速率。                                         |
| <span id="policy_20223" />`policy_20223` | 对 `%DOMAIN%` 的请求受速率限制 | 对 `%DOMAIN%` 的请求受速率限制。Bright Data 检测到该域名的成功率下降，正在着手解决。建议你在我们逐步解除限制期间重试失败的请求，或降低请求速率后稍后再试。 |

当某个域名的成功率下降时，Bright Data 会对该域名应用自适应速率限制，即返回 `policy_20223`。该限制会动态调整，因此重试失败的请求属于预期行为，并有助于在成功率恢复后更快解除限制。

### HTTP 错误 502

以下是 HTTP 502 错误对应的 `x-brd-err-code`：

| 错误代码                                     | `x-brd-error`                                                 | `x-brd-err-msg`                                                                                                                     |
| :--------------------------------------- | :------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------- |
| <span id="client_10120" />`client_10120` | Block direct route                                            | 请求的直连路由被阻止。你选择了在请求失败时不通过 superproxy 重路由，因此系统阻止了重路由。更多信息请查看：[Request Error Handling](/cn/api-reference/proxy/request_error_handling) |
| <span id="peer_30030" />`peer_30030`     | Proxy Error: We do not have proxies in the city you requested | 代理错误：你请求的城市没有可用代理。请检查城市名称拼写，或稍后重试。更多信息请查看：[Target a specific city](/cn/proxy-networks/faqs#how-to-target-a-specific-city)           |
| <span id="policy_20070" />`policy_20070` | Host is blocked in requested country                          | 目标主机在所选国家被阻止。请切换国家后重试。                                                                                                              |
| <span id="client_10100" />`client_10100` | Zone has reached usage limit                                  | 该 Zone 已达到使用限制。请前往 [https://www.bright.cn/cp/zones](https://www.bright.cn/cp/zones) 修改或移除限制。                                        |
| <span id="target_40001" />`target_40001` | Could not resolve host `%HOST%`                               | 无法解析主机 `%HOST%`。请检查拼写是否正确。如果拼写无误，请联系 brightdata.com 获取 DNS 支持。                                                                      |
| <span id="target_40011" />`target_40011` | No IPv6 address (AAAA record) found for `%HOST%`              | 无法将 `%HOST%` 解析为 IPv6 地址。目标主机可能未提供 IPv6 记录。请改用 IPv4 代理重试。                                                                           |
