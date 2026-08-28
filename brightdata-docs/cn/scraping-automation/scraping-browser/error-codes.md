> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Browser API 错误代码

> Bright Data Browser API 错误代码参考，分为四个类别，包含每个代码的含义以及建议的解决操作。

本参考页面列出了 Bright Data Browser API 的错误代码，按四个类别分组，并给出每个代码的含义以及建议的操作。

当请求失败时，Browser API 会返回一个特定的错误代码。请在下方表格中查找该代码，并按照“建议操作”列执行。

## 访问与权限

这些错误表示访问或权限问题。请求被阻止的原因，可能是您的 Browser API 区域需要更改配置，也可能是目标受到 Bright Data 合规保护措施的限制。

| <div className="min-w-[250px]">错误代码</div> | 含义                    | 建议操作                                                                                                        |
| ----------------------------------------- | --------------------- | ----------------------------------------------------------------------------------------------------------- |
| `brob`                                    | 目标被 robots.txt 阻止。    | robots.txt 是目标网站的限制，用于定义爬虫可以访问和不可以访问的内容。如需解除限制，请完成 [KYC 验证](/cn/proxy-networks/residential/network-access)。 |
| `brul`                                    | 目标受 Bright Data 限制。   | 如需访问被阻止的资源，请通过 [compliance@brightdata.com](mailto:compliance@brightdata.com) 向合规部门申请权限。                     |
| `custom_headers`                          | 客户没有更改标头或 Cookie 的权限。 | 在您的 Browser API 区域配置中启用 **Custom headers and cookies**（自定义标头和 Cookie）。                                      |
| `wrong_customer_name`                     | 用户名无效。                | 在 Bright Data 控制面板中核实您的用户名是否正确。                                                                             |
| `zone_not_found`                          | 指定的区域不存在或未激活。         | 确认您在 Bright Data 控制面板中使用的是正确且已激活的“Browser API”区域。                                                           |
| `wrong_password`                          | 区域密码不正确。              | 在 Bright Data 控制面板中核实您的区域密码是否正确。                                                                            |
| `missing_credentials`                     | 缺少身份验证凭据。             | 在您的脚本中添加有效的 Browser API 凭据。                                                                                 |

## 代理错误

这些错误表示 Browser API 与底层代理网络之间存在路由或连接问题。它们通常发生在代理网络难以建立或维持稳定连接时。

| <div className="min-w-[250px]">错误代码</div> | 含义                                                 | 建议操作                         |
| ----------------------------------------- | -------------------------------------------------- | ---------------------------- |
| `no_peers`                                | 无法与对等节点建立连接。                                       | 稍后重试，或移除对等节点限制（国家/地区、会话、位置）。 |
| `proxy_no_peer`                           | 无法与对等节点建立连接。                                       | 稍后重试，或移除对等节点限制（国家/地区、会话、位置）。 |
| `reserve_no_result`                       | 目标国家/地区没有可用的对等节点。                                  | 尝试移除或更改国家/地区定向。              |
| `geo_no_navigation`                       | 导航前无法解析地理位置（在导航到页面前调用 `Proxy.getGeolocation` 时发生）。 | 先导航到某个页面，然后重试。               |
| `proxy_cooling_peers`                     | 由于分配的对等节点处于冷却期，没有可用的对等节点。                          | 稍后重试，或移除对等节点限制（国家/地区、会话、位置）。 |
| `proxy_no_peers_cooling`                  | 由于分配的对等节点处于冷却期，没有可用的对等节点。                          | 稍后重试，或移除对等节点限制（国家/地区、会话、位置）。 |
| `proxy_timeout`                           | 代理连接超时。                                            | 稍后重试。                        |

### `proxy_error` 消息

`proxy_error` 代码属于上述代理错误，但它涵盖了多种代理端情况。具体原因会在随附的消息中说明：

| 消息               | 建议操作        |
| ---------------- | ----------- |
| 该国家/地区不允许用于定向。   | 尝试其他国家/地区。  |
| 代理无法解析目标网站主机。    | 检查该网站是否可访问。 |
| 代理连接超时。          | 稍后重试。       |
| 对等节点未能与目标网站建立连接。 | 稍后重试。       |

## 会话限制

Browser API 会话有时间限制，以确保最佳性能。当会话运行时间过长、长时间闲置或访问多个域名时，会发生这些错误。为避免这些错误，请将任务拆分为较短的会话，并及时关闭连接。

| <div className="min-w-[250px]">错误代码</div> | 含义                         | 建议操作                                 |
| ----------------------------------------- | -------------------------- | ------------------------------------ |
| `session_timeout`                         | 会话达到 60 分钟上限。              | 缩短会话时间；拆分为多个会话。                      |
| `network_inactivity_timeout`              | 会话在 5 分钟无网络活动后被终止。         | 抓取完成后断开与浏览器的连接（对于 WebDriver，还需删除会话）。 |
| `client_timeout`                          | 客户端到浏览器的连接未在规定时间内建立（30 秒）。 | 检查您的网络连接并重试。                         |
| `navigate_domains_limit`                  | 会话仅限于一个域名。                 | 每个域名开启一个新会话。                         |

## 浏览器与目标网站

这些错误发生在浏览器层，原因是脚本命令无效、超时或意外崩溃。如需解决，请调试您的自动化代码或重试会话。

| <div className="min-w-[250px]">错误代码</div> | 含义                                    | 建议操作                                                     |
| ----------------------------------------- | ------------------------------------- | -------------------------------------------------------- |
| `cdp_cmd_timeout`                         | 发送给浏览器的命令超时。                          | 重试该命令。                                                   |
| `browser_disconnected`                    | 浏览器因临时内部错误而断开连接。                      | 重试，或建立新会话。                                               |
| `no_free_workers`                         | 没有可用的浏览器来处理请求。这发生在建立浏览器连接之前，通常表示临时问题。 | 稍后重试。如果问题持续存在，请联系 [支持团队](mailto:support@brightdata.com)。 |
| `worker_disconnect`                       | 浏览器工作节点崩溃，或发生内部基础设施故障。                | 重试，或建立新会话。                                               |
| `job_killed`                              | 浏览器会话因基础设施故障而被关闭。                     | 重试，或建立新会话。                                               |
| `page_navigated_error`                    | 导航过程中发生错误，通常与内部问题有关。                  | 重试，或建立新会话。                                               |

### `cdp_error` 消息

`cdp_error` 代码属于上述浏览器与目标网站错误，但它涵盖了多种浏览器端情况。具体原因会在随附的消息中说明：

| 消息                                             | 建议操作                            |
| ---------------------------------------------- | ------------------------------- |
| 浏览器目标或会话已关闭，无法接受命令。                            | 修复代码中的脚本错误（通常由缺少 `await` 语句引起）。 |
| CDP 命令使用错误（例如，向 `Fetch.dropRequests` 传递了无效参数）。 | 核实命令名称及其参数对该 CDP 命令是否有效且格式正确。   |

## Chromium 网络错误 (net::ERR\_\*)

当浏览器无法访问或加载目标网站时，会返回一个以 `net::ERR_` 为前缀的标准 Chrome 网络错误。这些错误与您在普通 Chrome 浏览器中看到的相同，通常反映目标网站的状态。例如，网站暂时宕机、无法访问或 TLS 证书无效。

错误响应格式：

```text theme={null}
Error: net::ERR_CONNECTION_CLOSED at https://example.com
```

由于这些是 Chrome 原生错误，可能的代码有很多。要了解特定错误及其原因，请在 [source.chromium.org](https://source.chromium.org) 上搜索确切的错误名称。

<Note>
  **需要更多帮助？** 如需进一步协助，请联系 [support@brightdata.com](mailto:support@brightdata.com)。
</Note>
