> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Web Unlocker API 错误代码

> 按 HTTP 状态码整理的 Bright Data Web Unlocker API 错误目录，包含每个 x-brd-error-code 的含义及对应的解决方法。

本参考页面说明如何识别 Web Unlocker API 错误、同一错误在两种接入模式下的呈现方式，以及最常见错误代码的解决方法。

## 如何判断错误来自 Web Unlocker 还是目标网站？

每个 Web Unlocker 错误都带有描述失败原因的 `x-brd-error` 响应头。大多数错误还带有机器可读的错误代码：unlocker 层错误使用 `x-brd-error-code`，透传的代理层错误使用 `x-brd-err-code`。如果响应中没有 `x-brd-error`，则该响应来自目标网站本身，包括目标网站自己的错误页面和 4xx/5xx 状态码，这些内容会原样传递给您。

请基于错误代码（而不是错误消息文本）编写分支逻辑，因为消息中包含选择器、主机名、超时时间等与具体请求相关的细节。

## 错误在两种接入模式下分别出现在哪里？

两种接入模式返回相同的错误代码，区别在于 HTTP 状态码所在的位置：

| 接入模式       | Endpoint                     | 状态码位置                                                                                                                                     |
| ---------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Direct API | `api.brightdata.com/request` | 请求到达 unlocker 后，外层响应始终为 `200 OK`，实际结果状态码在 `x-brd-status-code` 响应头中。在解锁开始前被拒绝的请求会返回真实的外层状态码：API key 问题返回 `401`，zone 名称不存在或 URL 无效返回 `400`。 |
| 原生代理       | `brd.superproxy.io:33335`    | 响应本身的 HTTP 状态码，错误消息（或其缩写形式）位于状态原因短语中。                                                                                                     |

在原生代理模式下，国家和会话选项从 JSON body 参数改为用户名标志（例如 `-country-us`），但产生的错误代码相同。

同一失败在 Direct API 下的响应：

```http Direct API 响应 theme={null}
HTTP/1.1 200 OK
x-brd-error: Navigation failed: The SSL/TLS certificate presented by the server is not valid for the current date
x-brd-error-code: net_err_cert_date_invalid
x-brd-status-code: 502
```

在原生代理下的响应：

```http 原生代理响应 theme={null}
HTTP/1.1 502 Navigation failed
x-brd-error: Navigation failed: The SSL/TLS certificate presented by the server is not valid for the current date
x-brd-error-code: net_err_cert_date_invalid
```

## 哪些响应头携带错误代码？

按层级分为两组错误响应头：

| 层级                                               | 代码响应头              | 消息响应头           | 文档位置                                      |
| ------------------------------------------------ | ------------------ | --------------- | ----------------------------------------- |
| Unlocker 层                                       | `x-brd-error-code` | `x-brd-error`   | 本页面                                       |
| 代理层透传（`policy_*`、`client_*`、`peer_*`、`target_*`） | `x-brd-err-code`   | `x-brd-err-msg` | [代理错误目录](/cn/proxy-networks/errorCatalog) |

两组响应头在两种接入模式下都可能出现。状态码为 `400`、`403` 或 `407` 的响应还带有 RFC9209 `Proxy-Status` 响应头，其 `details` 字段会重复代理层代码（例如 `details="policy_20020: Bad Port used..."`）。下文列出的 502 解锁失败不携带该响应头。

## 哪些错误可以通过重试解决？

由 peer 或解锁尝试本身导致的错误值得重试，因为每次请求使用不同的 peer。由目标网站自身属性或您的请求参数导致的错误，每次尝试都会返回相同结果。

| 行为                     | 代码                                                                                                                                                                         |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 重试可能成功                 | `reject_block`、`resolve_failed_*`                                                                                                                                          |
| 重试返回相同错误，应先解决根本原因      | `net_err_cert_date_invalid`、`net_err_cert_common_name_invalid`、`net_err_cert_authority_invalid`、由 TLS 或加密套件不匹配导致的 `document_load_failed`、主机无法解析时的 `proxy_error`、`no_peers` |
| 配置错误，在 zone 或请求更改前保持不变 | `premium`、`feature_not_active`、`ub_bad_endpoint_robots`                                                                                                                    |

## 错误目录

### HTTP 错误 400

400 表示请求在解锁尝试开始前就被拒绝，原因是 zone 配置或请求本身不允许该请求。这类响应不包含 `x-brd-debug` 响应头。

#### `premium`

| `x-brd-error`                                                                                                                                      | 建议操作                                                                                                                                                       |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Targeting %HOST% requires Premium permissions. To enable 'Premium domains', go to your Web Unlocker zone configuration page: %ZONE\_EDIT\_URL% ... | 在 zone 配置中启用 [Premium Domains](/cn/scraping-automation/web-unlocker/features#web-unlocker-api-premium-domains)。错误消息中直接包含您 zone 编辑页面的链接。启用后，对同一域名的相同请求即可成功。 |

#### `feature_not_active`

| `x-brd-error`                              | 建议操作                                                                                                                                                                                                   |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Manual expect is not enabled for this zone | 请求使用了 zone 上未启用的自定义 Web Unlocker 功能，例如 `x-unblock-expect` 响应头。请启用对应的[自定义 Web Unlocker API 功能](/cn/scraping-automation/web-unlocker/features#自定义-web-unlocker-api)，或移除该请求头。注意：启用自定义功能后，zone 将按 100% 计费。 |

#### `ub_bad_endpoint_robots`

| `x-brd-error`                                                                                                                                                                                | 建议操作                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Request Failed (bad\_endpoint): Requested site is not available for immediate access mode in accordance with robots.txt. Ask your account manager to get full access for targeting this site | 请求的路径被目标网站的 `robots.txt` 禁止，而账户处于即时（免 KYC）访问模式，该模式遵守 `robots.txt`。请完成 [KYC 验证](/cn/general/account/limited-trial-restrictions)，或联系您的客户经理获取完整访问权限。完整访问权限的账户发送相同请求不会被此检查拦截。 |

#### 请求校验（仅 Direct API，真实外层 400）

| Body                                                                  | 建议操作                                                                                                                  |
| --------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `zone "..." not found`                                                | `zone` 值与您账户中的任何 zone 都不匹配。请在[控制面板](https://brightdata.com/cp/zones)中核对 zone 名称。同样的错误在原生代理下返回 `407` 和 `client_10002`。 |
| `{"error":"Request validation failed","error_code":"validation",...}` | 请求 body 格式错误，例如 URL 缺少 `https://`。请修正 `details` 中指出的字段。                                                               |

### HTTP 错误 401（仅 Direct API）

API key 认证发生在请求到达 unlocker 之前，因此这类错误返回**真实的外层 401**，带有纯文本 body，不包含 `x-brd-*` 响应头。

| Body                              | 原因                                          | 建议操作                                              |
| --------------------------------- | ------------------------------------------- | ------------------------------------------------- |
| `Auth method is not supported`    | `Authorization: Bearer` 响应头的值不是有效的 API key。 | 检查您的 [API key](/cn/api-reference/authentication)。 |
| `User authentication is required` | 缺少 `Authorization` 请求头。                     | 在请求中添加 `Authorization: Bearer <API key>`。         |

### HTTP 错误 403

访问受 Bright Data 政策限制。这类错误大多在 `x-brd-err-code` 中携带代理层代码，详见[代理错误目录](/cn/proxy-networks/errorCatalog)。

| `x-brd-err-code` | 触发条件                                                                                                                                                                                                 | 建议操作                                                                                                                      |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `policy_20020`   | 目标端口不受支持，例如 `:25` 或 `:8080`。                                                                                                                                                                         | 使用[支持的端口](/cn/proxy-networks/faqs)。                                                                                       |
| `client_10090`   | `zone` 值指向 Browser API（Scraping Browser）zone，该类型 zone 无法通过 Web Unlocker 请求接口使用。                                                                                                                      | 对该 zone 使用浏览器连接（参见 [Browser API](/cn/scraping-automation/scraping-browser/introduction)），或在 `zone` 中传入 Web Unlocker zone。 |
| *（不返回代码）*        | 目标是私有或保留地址，或被政策拦截。消息内容为 `Forbidden: You tried to target ... but got blocked. It can be related to your blacklist or whitelist settings or the target site is not allowed by Bright Data policy. ...` | 目标应为 Bright Data 政策允许的公共主机名，并检查 zone 的允许列表和拒绝列表。                                                                          |

### HTTP 错误 407

代理层认证失败。在原生代理下，407 是外层状态码，状态原因短语中带有摘要信息。在 Direct API 下，同样的 `407` 出现在 `x-brd-status-code` 中。

| `x-brd-err-code` | 状态行                                 | 原因                                                                       | 建议操作                                                                                                        |
| ---------------- | ----------------------------------- | ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| `client_10000`   | `407 Auth failed`                   | zone 密码错误或客户 ID 错误。                                                      | 在[控制面板](https://brightdata.com/cp/zones)中核对 zone 密码和客户 ID。                                                  |
| `client_10002`   | `407 Zone not found`                | zone 名称拼写错误、已停用或已删除。                                                     | 确认 zone 处于激活状态，或通过 [Get active zones](/cn/api-reference/account-management-api/Get_active_Zones) 列出所有 zone。 |
| `client_10010`   | `407 Proxy Authentication Required` | 未发送代理凭据。                                                                 | 将 `brd-customer-<id>-zone-<zone>:<password>` 作为代理用户名添加到请求中。                                                 |
| `client_10001`   | `407 Invalid Auth`                  | 请求参数携带在代理用户名中，因此即使 zone 名称和密码正确，格式错误的参数值（例如国家代码写成 `usa` 而不是 `us`）也会解析失败。 | 修改凭据前，先检查用户名中参数的格式。两位小写国家代码可以正确解析。                                                                          |

### HTTP 错误 429

#### `sr_rate_limit`

| `x-brd-error`                                          | 建议操作                                                                               |
| ------------------------------------------------------ | ---------------------------------------------------------------------------------- |
| The request was auto-throttled due to low success rate | 该目标的成功率下降后，Bright Data 的健康监控系统对请求进行了自动限流。请联系[支持团队](mailto:support@brightdata.com)。 |

### HTTP 错误 502

502 表示解锁尝试本身失败，原因在 `x-brd-error-code` 中。

#### `reject_block`

| `x-brd-error`                    | 建议操作                                                                             |
| -------------------------------- | -------------------------------------------------------------------------------- |
| captcha or protection page found | 检测到 CAPTCHA 或防护页面，因此响应被拒绝而未交付。请重试：每次尝试使用不同的 peer，对同一 URL 的相同请求在后续尝试中成功的情况是经过验证的。 |

#### `resolve_failed_*`

| `x-brd-error`          | 建议操作                                                                                                                            |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Captcha resolve failed | 尝试解决 CAPTCHA 但未完成。后缀标明了验证类型，例如 `resolve_failed_akamai_interstitial`。与 `reject_block` 一样，请重试。如果某个 URL 持续失败，请携带 `req_id` 向支持团队报告。 |

#### `http_status`

| `x-brd-error`                                      | 建议操作                                                                                                                    |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| response status was rejected: %STATUS% status code | 目标返回了表示拦截的 HTTP 状态码，因此响应被丢弃而未交付。目标网站自身返回的 429 也属于此类。每次尝试使用不同的 peer，因此值得重试一次。如果该代码持续出现，说明目标正在拦截当前配置：请携带 `req_id` 联系支持团队。 |

#### `expect_element`

| `x-brd-error`                                                     | 建议操作                                                                                                                                                                                                                                              |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| waiting for selector "%SELECTOR%" failed: timeout %MS%ms exceeded | 页面已加载，但 unlocker 等待的元素未在等待时间内出现。实际观测到的等待时间为 30 到 150 秒，因此客户端超时短于该范围会在错误返回前中止请求：请将超时设置为至少 180 秒。反复返回此代码的 URL 会持续返回该代码，因此请携带 `req_id` 向支持团队报告，而不是重试。如果启用了[手动 expect](/cn/scraping-automation/web-unlocker/features#手动-expect-元素)，请先确认您自己的选择器在页面上存在。 |

#### `navigation_timeout`

| `x-brd-error`              | 建议操作                                                |
| -------------------------- | --------------------------------------------------- |
| Navigation timeout @ %URL% | 渲染页面未在时间限制内完成导航。如果某个 URL 持续超时，请携带 `req_id` 向支持团队报告。 |

#### `domcontentloaded_event_timeout`

| `x-brd-error`                                        | 建议操作                                                                       |
| ---------------------------------------------------- | -------------------------------------------------------------------------- |
| Timed out waiting for window\.DomContentLoaded event | 渲染页面未在时间限制内触发 `DOMContentLoaded` 事件。如果某个 URL 持续返回此错误，请携带 `req_id` 向支持团队报告。 |

#### `document_load_failed`

| `x-brd-error`                 | 建议操作                                                                                                                                                                                                                       |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Navigation failed: %NET\_ERR% | 渲染导航在收到文档之前失败。消息中携带底层 Chrome 网络错误，例如 `net::ERR_EMPTY_RESPONSE` 或 `net::ERR_SSL_VERSION_OR_CIPHER_MISMATCH`。可在 [source.chromium.org](https://source.chromium.org) 上查询该名称以确定原因。当原因是目标网站自身的属性（例如 TLS 或加密套件不匹配）时，每次尝试都会返回相同结果。 |

#### `net_err_cert_date_invalid`

| `x-brd-error`                                                                                        | 建议操作                                                               |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Navigation failed: The SSL/TLS certificate presented by the server is not valid for the current date | 目标网站的 TLS 证书已过期或尚未生效。请在浏览器中打开该 URL 确认。每次尝试都会返回相同结果，目标网站侧的无效证书无法绕过。 |

#### `net_err_cert_common_name_invalid`

| `x-brd-error`                                                                                                   | 建议操作                                      |
| --------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| Navigation failed: The SSL/TLS certificate presented by the server doesn't match the domain name being accessed | 目标网站的 TLS 证书不覆盖所请求的主机名。请确认主机名，并在浏览器中检查证书。 |

#### `net_err_cert_authority_invalid`

| `x-brd-error`                                         | 建议操作                                       |
| ----------------------------------------------------- | ------------------------------------------ |
| Navigation failed: Invalid certificate on target site | 目标网站的 TLS 证书由不受信任或未知的证书颁发机构签发。请在浏览器中检查证书链。 |

#### `net_err_closed`

| `x-brd-error`                                                    | 建议操作                                                 |
| ---------------------------------------------------------------- | ---------------------------------------------------- |
| Navigation failed: Network connection was closed by other party. | 连接在响应完成前被对方关闭。如果某个 URL 持续返回此错误，请携带 `req_id` 向支持团队报告。 |

#### `rate_limit`

| `x-brd-error`                                                                                                  | 建议操作                                                                                                        |
| -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Navigation failed: Failed to open proxy tunnel (reason = "Unexpected Status 429 (ext\_proxy\_connect\_error)") | 建立连接时在 Bright Data 侧达到了速率限制。目标网站自身返回的速率限制会报告为 `http_status`，而不是此代码。请降低对该目标的请求速率；如果持续出现，请携带 `req_id` 联系支持团队。 |

#### `proxy_error`

| `x-brd-error`                                                                                                                                                                                         | 建议操作                                                                                              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Could not resolve host %HOST%. Check host name is correctly spelled and retry. If host is properly spelled or can only be resolved from a specific region contact brightdata support for DNS support. | 代理层无法完成请求，最常见原因是主机名无法解析。请检查主机名拼写。无法解析的主机名每次尝试都返回相同错误，因此尽管消息中建议重试，重试并没有帮助。如果该主机名只能从特定区域解析，请联系支持团队。 |

#### `no_peers`

| `x-brd-error`                    | 建议操作                                                                                                                          |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Unexpected Status 502 (no\_peer) | 没有可用于该请求的 peer。凡是定向到没有可用 peer 的国家的请求都会返回此错误，包括 Bright Data 在该国没有 peer 的有效 ISO 代码。请更改或移除 `country` 值：改用有可用 peer 的国家后，相同请求即可成功。 |

### HTTP 错误 503

服务不可用。浏览器检查失败或未完成。目标网站自身返回的 503 会原样交付，不带 `x-brd-error` 响应头。
