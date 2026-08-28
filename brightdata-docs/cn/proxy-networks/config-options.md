> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 代理配置选项

本文档说明如何使用**代理用户名参数**配置 Bright Data 代理行为。通过修改代理用户名，您可以直接从代码中控制代理定位、IP 轮换、DNS 解析、会话处理和路由行为。

这种方法允许进行高度精细的代理控制，而无需更改仪表板设置或基础设施。

## 代理网络身份验证

Bright Data 代理访问使用**代理用户名和密码**进行身份验证。这些凭据是在 Bright Data 控制面板中创建代理区域时生成的。

每个代理区域代表一个特定的代理产品（数据中心、ISP 或住宅）及其基本配置。

### 通过代理用户名和密码进行本机访问

创建 Bright Data 代理区域后，您将获得：

* **代理用户名**
* **代理密码**

代理用户名不仅仅是一个标识符，它还定义了**代理的行为方式**。

**代理用户名**由以下部分组成：

* 您的账户 ID
* 您的区域名称
* 可选配置参数

#### 代理用户名结构

`brd-customer-[customerID]-zone-[zone name]-[optional parameters]`

<Warning>
  创建代理区域后，您**无法更改区域名称**。如果需要更改区域名称，必须创建新区域。代理只能在**两个区域类型相同**的情况下从一个区域转移到另一个区域。
</Warning>

通过**添加可选参数和修改用户名**，您可以直接从应用程序代码以非常精细的方式控制 Bright Data 的代理系统。

下面的部分描述了可用的配置选项。完整的列表可在 [代理 API 参考文档](/api-reference/proxy/) 中获得。

## 与第三方工具集成

Bright Data 代理可与各种第三方工具、自动化框架、浏览器和 HTTP 客户端集成。为了简化集成，Bright Data 在控制面板中提供现成的请求示例。

您可以在此处访问这些示例：[https://www.bright.cn/cp/zones/proxy\_examples](https://www.bright.cn/cp/zones/proxy_examples)

这些示例帮助您：

* 构造正确的代理请求
* 验证凭据
* 测试定位和轮换行为
* 将代理集成到现有工具和工作流中

## 代理定位选项

这些设置让您轻松配置特定国家、州、城市、邮编和 ASN 的代理。

<Note>
  数据中心和 ISP 代理仅支持国家定位
</Note>

| 参数           | 描述                                                                                                    | 示例用户名                                                                      |
| ------------ | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| -country-xx  | 使用两字母代码选择国家，或使用 `eu` 表示欧盟中的随机国家。国家代码列表在 [这里](/general/faqs#where-can-i-see-the-list-of-country-codes) | `brd-customer-<customer_id>-zone-<zone_name>-country-us`                   |
|              |                                                                                                       |                                                                            |
| -state-xxxxx | 使用两字母代码定位美国的一个州。必须包括美国作为国家。                                                                           | `brd-customer-<customer_id>-zone-<zone_name>-country-us-state-ny`          |
| -city-xxxxx  | 定位城市。必须包括国家（例如 username-country-fr-city-paris）。不要使用空格（例如 -city-sanfrancisco）                          | `brd-customer-<customer_id>-zone-<zone_name>-country-us-city-sanfrancisco` |
| -zip-xxxxx   | 定位美国邮编。使用 5 位邮编                                                                                       | `brd-customer-<customer_id>-zone-<zone_name>-city-memphis-zip-37501`       |
| -asn-xxxxx   | 从 [列表](https://bgp.potaroo.net/cidr/autnums.html) 定位一个 ASN                                            | `brd-customer-<customer_id>-zone-<zone_name>-asn-56386`                    |
| -os-xxxxx    | 仅适用于住宅代理。允许定位 `Windows`、`MacOS` 或 `android`                                                           | `brd-customer-<customer_id>-zone-<zone_name>-os-windows`                   |

## 控制代理的 DNS

DNS 解析���定了**在发送请求之前域名的解析位置**。

Bright Data 允许您控制 DNS 解析是否发生：

* 在代理对等端
* 在 Bright Data 的超级代理服务器上

| 功能          | 参数                       | 描述                                                                                                                                   | 示例用户名                                                   |
| ----------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------- |
| 选择 DNS 解析位置 | -dns-local 或 -dns-remote | 让您选择 DNS 是在代理连接到网站的 `remote` 上解析，还是在 Bright Data 服务器（"超级代理"）的 `local` 上解析。更多信息 [这里](/api-reference/proxy/configuring_dns_resolution) | `brd-customer-<customer_id>-zone-<zone_name>-dns-local` |

## 控制代理轮换

以下选项允许您设置如何在区域内的代理之间进行轮换，或附加到特定代理，以及如果对等端由于某种原因不可用时应该执行什��操作。
有关 IP 轮换如何与我们的代理产品配合使用的更多信息，以及以下选项的进一步说明，请参见 [此文章](/api-reference/proxy/rotate_ips)

| 功能                  | 参数              | 描述                                                                         | 示例用户名                                                                    |
| ------------------- | --------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| 为多个请求保持相同 IP 或轮换 IP | -session-xxxxxx | 每个唯一的会话 ID 将获得唯一的 IP，可用于重复定位相同 IP 或强制轮换。建议用于实现程序化 IP 轮换。                   | `brd-customer-<customer_id>-zone-<zone_name>-session-mystring12345`      |
| 选择特定 IP             | -ip-x.x.x.x     | 仅适用于分配了专用 IP 的区域                                                           | `brd-customer-<customer_id>-zone-<zone_name>-ip-1.2.3.4`                 |
| 选择特定 IP 组（gIP）      | -gip-xxxxxx     | 仅适用于专用住宅代理。                                                                | `brd-customer-<customer_id>-zone-<zone_name>-gip-us_7922_fl_hollywood_0` |
| 跟踪个别响应              | -c\_tag-xxxxxx  | 在请求中包含唯一的 c\_tag 标志。响应中，业务会在标头中回显相同的标记。这种无缝交换确保每个响应都绑定到其相应的请求，消除混淆并简化数据管理。 | `brd-customer-<customer_id>-zone-<zone_name>-c_tag-<C_TAG_VALUE>`        |
| 绑定到会话中的对等端          | -const          | 为会话使用相同的对等端。如果对等端不可用，将返回 502 错误，显示"no peer available"                      | `brd-customer-<customer_id>-zone-<zone_name>-const`                      |

## 控制"超级代理"

超级代理是 Bright Data 的路由服务器，负责选择和管理实际的代理对等端（数据中心、ISP 或住宅）。

> 修改超级代理参数**很少需要**，应仅在高级路由场景中进行。

| 功能             | 参数                | 描述                                                                                      | 示例用户名                                                                    |
| -------------- | ----------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| 直接从超级代理发送请求    | -direct           | 强制从 Bright Data 的超级代理服务器（而不是实际代理对等端）发送请求                                                | `brd-customer-<customer_id>-zone-<zone_name>-direct`                     |
| 选择特定国家中的超级代理   | session-xxxxxx    | 仅适用于选择超级代理，这很少需要。更多详情 [这里](/api-reference/proxy/select_super_proxy_in_specific_country) | [示例](/api-reference/proxy/select_super_proxy_in_specific_country)        |
| 选择特定 IP 组（gIP） | gip-xxxxxx        | 仅适用于专用住宅代理。                                                                             | `brd-customer-<customer_id>-zone-<zone_name>-gip-us_7922_fl_hollywood_0` |
| 阻止超级代理绕过       | -route\_err-block | 不允许 Bright Data 从我们的超级代理服务器发出请求。这意味着如果由于合规问题我们无法通过对等端处理请求，它将返回错误                        | `brd-customer-<customer_id>-zone-<zone_name>-route_err_block`            |

要查找导航和其他文档页面，请获取位置如下的 **llms.txt** 文件：[https://docs.brightdata.com/llms.txt](https://docs.brightdata.com/llms.txt)
