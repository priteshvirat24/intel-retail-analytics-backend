> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 代理和 IP 轮换控制

> 代理 IP 轮换是如何工作的，以及如何配置或控制它。

## 共享池中的默认代理 IP 轮换

共享池代理，也称为“旋转代理”，可用于所有 Bright Data 代理网络：数据中心、ISP、住宅和移动。

默认情况下，Bright Data 会根据您的配置，从区域内可用代理中随机分配一个代理。

例如：如果您选择定向特定国家，例如加拿大，使用 `-country=ca` 参数，我们将在池中所有位于加拿大的代理中随机分配一个代理。

下一次请求将被定向到不同的代理，以此类推，从我们的池中随机选择。在高频率执行请求或多个调用代理时，可能会重复使用相同的代理 IP。

## 专用代理区域中的默认代理 IP 轮换

当您配置一组专用代理时，这些代理将按照以下方式专属分配给您：

1. 在数据中心和 ISP 网络中：代理对所有域名都是专属的。
2. 在住宅和移动网络中：对 **特定域名** 专属。

在专用代理区域中，我们将轮换到下一个可用代理来处理下一次请求。

### 什么是“静态住宅”代理？

“静态住宅代理”是由互联网服务提供商 (ISP) 注册的托管在数据中心的代理，并具有固定的静态 IP 地址。在 Bright Data 中，我们称这些代理为“ISP 代理”，而非“静态住宅”。

### 专用住宅代理的轮换

由于住宅代理的可用性会有所不同，我们将多个代理分组到一个称为 `gIP` 的组中。这个 `gIP` 拥有唯一标识符，并且分配给它的节点（组成员）将根据您指定的配置进行选择。例如：如果您需要针对 [http://example.com](http://example.com) 提供 3 个专用住宅 IP，我们将提供 3 个 `gIP`，并轮换它们来处理您的请求。

## 使用显式代理发送多次请求：`ip`

要将请求显式定向到特定代理，请在代理区域用户名请求中使用 `-ip` 参数。这适用于在不同连接上执行一系列请求（例如一系列 `curl` 请求）。

## 使用相同代理发送多次请求：`session`

要在多次请求中保持相同的代理 IP，请使用 `-session` 参数，并提供您创建和控制的会话标识符。每个携带相同 `-session` 值的请求将被转发到 **相同的代理 IP**。

`-session` 参数的值由您生成和控制，但其格式应仅包含字母数字字符。使用特殊字符如 `-` 或 `*` 将导致错误。

如果您使用原生代理访问（在代码库或第三方工具中使用代理 ip:port 和凭证），则将会话参数嵌入用户名参数，如下所示，使用会话标识 `mystring12345`。如果使用我们的代理 REST API，则请求 `body` 中的 `session` 参数应携带会话标识值。

```sh Shell theme={null}
curl "http://target.site" --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-session-mystring12345:<zone_password>
```

## 在节点不可用时禁用代理轮换

默认行为是在节点不可用时将您的请求转向另一个节点，以保持操作流畅。如果您希望仅使用单个节点进行会话，并在节点不可用时让请求失败，请在 `session` 参数中添加 `-const` 选项。

使用 `-const` 选项时，如果节点不可用，将收到 `HTTP 502` 错误。

```sh Shell theme={null}
curl "http://target.site" --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-session-mystring12345-const:<zone_password>
```

## 会话上下文丢失

以下描述了会话上下文可能丢失的场景，随后请求将由 **不同** 的代理执行。

### 会话空闲时间

会话空闲时间为 5 分钟。如果两次连续请求之间的空闲时间超过 5 分钟，即使第二次请求携带与第一次相同的 `session` 参数，也将使用从池中随机选择的代理。

### 会话来源必须来自相同全球区域

为保持相同会话，必须确保发出请求的调用进程不会在全球区域间切换。我们识别三个全球区域：

1. AMER：北美、中美和南美
2. EMEA：欧洲、中东和非洲
3. APAC：亚洲和太平洋

示例：如果您发出两次连续请求，一次来自加拿大的 **公司服务器**（AMER 区域），一次来自法国的 **公司服务器**，即使两次请求都携带相同的 `session` 参数，也将由不同的代理节点执行。

### 其他参数必须相同

如果两次连续请求携带不同的国家、城市或任何其他参数：会话上下文将丢失，即使它们携带相同的 `session` 参数。

### 会话丢失的错误处理

默认情况下，如果会话丢失或重置，Bright Data 将随机分配一个代理给您的请求。如果希望避免默认分配并改为报错，请在请求中使用 `-const` 参数。如果同一节点因任何原因无法用于两次连续请求，则第二次请求将导致 `HTTP Error 502`。

```sh Shell theme={null}
curl "http://target.site" --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-session-mystring12345-const:<zone_password>
```

## 跟踪请求及其响应（C-Tag）

我们实现了一个可选功能，可大大帮助跟踪和关联请求及其对应的响应，更多信息请参见以下文章：[更多关于 C-Tag 的信息](/cn/api-reference/proxy/c-tag)
