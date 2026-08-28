> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 拒绝列表或允许列表 IP 和域

## 定义

* 允许列表 (Allowlist) 是**允许**访问您的区域 (Zone) 的 IP 地址列表。
* 拒绝列表 (Denylist) 是**拒绝**访问您的区域 (Zone) 的 IP 地址列表。

<Note>
  允许列表应包含您**向您公司或云网络中的代理发起请求**的 IP 地址。该列表**不应**包含 Bright Data 提供的代理的 IP。
</Note>

## 如何配置允许列表和拒绝列表

有两种方式可以配置允许列表和拒绝列表：通过控制面板或使用 Bright Data 账户管理 API。

***

### 如何通过控制面板配置允许列表和拒绝列表

1. 登录您的 Bright Data 账户控制面板。
2. 选择您要修改的区域 (Zone)，然后转到“概览 (Overview)”选项卡。
3. 在“概览 (Overview)”选项卡下，在 **访问详情 (Access Details)** 部分，有一个编辑图标可用于编辑列表。
4. 点击编辑图标。

<img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/proxy-networks/faqs/editAllowlist.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=ecb6b23549e3c6bc2be7789aaf3fc119" alt="editAllowlist.png" width="1321" height="578" data-path="images/proxy-networks/faqs/editAllowlist.png" />

5. 这将带您进入“配置 (Configuration)”选项卡，在“安全设置 (Security settings)”下编辑列表：

<img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/proxy-networks/faqs/whitelist-blacklist.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=71d845b5fdcf78f37e13767cea788313" alt="whitelist-blacklist.png" width="557" height="490" data-path="images/proxy-networks/faqs/whitelist-blacklist.png" />

添加您将允许使用您的代理区域访问的所有相关 IP 和域。

***

### 如何通过 Bright Data 账户管理 API 配置允许列表和拒绝列表

以下 API 将使您能够控制和管理您的允许列表和拒绝列表：

* [将 IP 添加到区域允许列表](/cn/api-reference/account-management-api/allowlist-ip)
* [从区域允许列表中移除 IP](/cn/api-reference/account-management-api/remove-ip-from-zone-allowlist)
* [将 IP 添加到区域拒绝列表](/cn/api-reference/account-management-api/denylist-ip)
* [从区域拒绝列表中移除 IP](/cn/api-reference/account-management-api/remove-ip-from-zone-denylist)
* [从区域允许列表/拒绝列表中移除域](/cn/api-reference/account-management-api/remove-domain-from-zone-allowlist-or-denylist)
* [将域添加到区域允许列表/拒绝列表](/cn/api-reference/account-management-api/allowlist-or-denylist-domains)

***

## 允许列表和拒绝列表定义的最佳实践是什么？

* 准确的允许列表可防止滥用您的 Bright Data 代理，保护您的操作和资金。有关更多信息，请参阅[此视频](https://www.bright.cn/static/video/howto/blacklist_system_explanation.mp4?md5=153602994-22bce32a\&hver=2)。
* 您可以添加到允许列表的 IP/域数量**没有限制**，我们也支持 IP 范围。
* 当您从公共云工作时，您的爬虫会在不同的 IP 上生成，允许列表将需要不断变化和调整以适应传入请求的源 IP。为防止不断更改，我们建议您为与 Bright Data 交互的云操作设置一个永久性出站 IP。请咨询您的云提供商以获取可用解决方案。常见解决方案是为出站通信设置 NAT 网关。
* 为了更轻松地管理和控制，我们建议使用通配符和模式在您的列表中定义域或 IP 范围。

***

### 我们支持哪些用于允许列表和拒绝列表配置的通配符和模式？

我们支持以下域名和 IP/子网/掩码的模式：

| 模式                  | 描述                                                    | 示例                                             |
| ------------------- | ----------------------------------------------------- | ---------------------------------------------- |
| `*` (星号)            | 匹配所有字符串                                               | `*` - 将匹配所有 IP/域                               |
| `*` (星号)            | 嵌入在字符串中，将匹配所有子字符串（前缀）                                 | `*.mycompany.net` 将匹配所有以 `.mycompany.net` 结尾的域 |
| `*` (星号)            | 嵌入在字符串中，将匹配所有子字符串（后缀）                                 | `sub.mycompany.*` 将匹配所有后缀（如 net、com、us 等）      |
| `a.b.c.d`           | a、b、c、d 都是 0-255 之间的数字，此模式表示单个 IP 地址                  | `195.55.35.112`                                |
| `a.b.c.0/24`        | 此模式表示整个 /24 子网，意味着所有以 a.b.c 为前缀且“d”数字为 0-255 的 IP 地址。 | `195.55.35.0/24 `                              |
| `a.b.c.d - x.y.z.w` | a.b.c.d 和 x.y.z.w 之间的 IP 范围                           | `10.20.30.40-10.20.30.50`                      |
| `a.b.c.d/x.y.z.w`   | 网络掩码 (Netmask)：网络掩码将 IP 地址分隔为网络和主机部分。类似于子网的使用。        | `10.20.30.40/255.255.252.0`                    |
