> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何配置您的住宅代理

> 轻松配置 Bright Data 住宅代理设置。了解如何设置 IP 类型、启用地理位置定向、管理长会话节点等高级选项。

首先进入您想配置的代理的配置选项卡。

## 代理类型

**为您的代理区域选择四种代理类型（IP 类型）之一：**

<CardGroup cols={4}>
  <Card title="共享 IPv4 代理" icon="square-1">
    全球轮换的 **IPv4** 真实设备代理。
  </Card>

  <Card title="共享 IPv4 & IPv6 代理" icon="square-2">
    全球轮换的 **IPv4 & IPv6** 真实设备代理组合池。
    我们的 “Mega Pool”。
  </Card>

  <Card title="共享 IPv6 代理" icon="square-3">
    全球轮换的 **IPv6** 真实设备代理。
  </Card>

  <Card title="独享代理" icon="square-4">
    具有特定域名独享访问权限的代理集合，几乎不轮换。
  </Card>
</CardGroup>

***

## 选择正确的住宅代理

我们在住宅代理网络中提供 4 种类型的代理：

共享代理：

1. Shared IPv4
2. Shared IPv4+IPv6 ("Mega pool")
3. Shared IPv6

独享代理：

4. Dedicated residential proxies

## 住宅网络访问权限

访问住宅网络需经 Bright Data 合规团队 KYC 批准，仅向已验证企业开放。这适用于所有住宅代理类型，包括共享、IPv6 和专用代理。更多信息请参见：\
[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。

## 配置共享住宅代理（轮换代理）

Bright Data 会在您的每次请求中自动分配新的代理。您可以通过控制面板设置和代理用户名参数中的代理选项控制共享代理的行为以及轮换方式。

最常用的设置是地理位置定向，允许您将请求通过指定位置的代理路由。您可以选择一个默认位置——所有请求将通过该位置路由。

<Tip>
  最佳实践：为您希望定向的每个地理位置设置一个单独的住宅代理区域。
</Tip>

### 地理位置解析选项

地理位置定向允许根据 `country`、`city`、`state`、`zip code` 或 `ASN` 定向。您可以在地理位置设置的下拉菜单中选择解析级别：

<Frame>
  <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/proxy-networks/residential/geotargeting.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=a257172a1920f073aca663714e45bfa4" alt="Geolocation Targeting" width="511" height="203" data-path="images/proxy-networks/residential/geotargeting.png" />
</Frame>

### 共享池默认国家选择

在共享池配置中选择国家后，我们将仅从这些位置分配代理。您可选择无（表示从池中随机分配代理）、一个或多个国家。\
[阅读更多...](/cn/api-reference/proxy/geolocation-targeting#default-countries-selection)

您可以覆盖默认选择或在轮换时显式分配特定国家，使用 ISO-3166 国家代码并在代理用户名中加入 `-country` 标记。

[FAQ: 哪里可以查看国家代码列表？](/cn/general/faqs#where-can-i-see-the-list-of-country-codes)

***

## 如何配置 IPv4+IPv6 共享住宅代理："Mega Pool"

### 介绍：IPv6

Bright Data 现在支持其住宅网络中的 IPv6。IPv6 代理的设置与 IPv4 代理非常相似。

IPv6 是互联网协议的最新版本，为解决 IPv4 地址不足而开发。IPv6 使用 128 位地址，可提供超过 340 百万亿亿亿（3.4×10³⁸）个唯一 IP 地址。

我们提供哪些 IPv6 住宅代理池类型？

Bright Data 提供两种 IPv6 住宅代理池：

1. 组合 IPv4+IPv6（Mega Pool），共享轮换代理
2. 仅 IPv6 共享轮换代理

我们目前不在数据中心或 ISP 网络提供 IPv6 代理。

### IPv6 住宅网络有多大？

我们已经在全球住宅代理网络中支持 IPv6。约有 150,000 个节点可用，并持续增长。这些代理被收集到我们的“共享轮换池”中。

### 什么是 IPv6 访问政策？

IPv6 代理遵守<u>住宅网络访问政策</u>，仅向通过 KYC 验证并符合资格的客户开放。

### 我可以使用哪些 IPv6 住宅代理选项？

我们支持所有 IPv4 选项，但以下除外：

| Targeting Option | Description  |
| :--------------- | :----------- |
| `gip`            | 不支持 gIP 定向   |
| `asn`            | 不支持 ASN 定向   |
| `zip`            | 不支持 ZIP 代码定向 |
| `ip`             | 不支持显式 IP 定向  |
| `carrier`        | 不支持移动运营商定向   |
| `os`             | 不支持显式操作系统定向  |

如果您在用户名中包含这些参数，且区域设为 IPv6，我们会忽略这些参数并继续处理请求。

完整选项列表：\
<u>[https://docs.brightdata.com/cn/proxy-networks/config-options](https://docs.brightdata.com/cn/proxy-networks/config-options)</u>

### 如果我使用 IPv6 代理访问仅支持 IPv4 的目标主机会怎样？

如果目标域没有 IPv6 地址，您的请求将返回 HTTP 502，并带有 Bright Data 错误头（`x-brd-err-code`）：`target_40011`。\
您应改用 IPv4 代理重试。

完整错误列表：\
<u>[https://docs.brightdata.com/cn/proxy-networks/errorCatalog#target-40011](https://docs.brightdata.com/cn/proxy-networks/errorCatalog#target-40011)</u>

### 我可以在 IPv4 和 IPv6 区域之间切换吗？

可以。您可以随时自由切换。从选择协议开始，该协议将影响区域使用的所有代理。

### IPv6 流量费用会变吗？

目前 IPv6 流量与 IPv4 费用相同。账单将按协议版本分开计算。

### 访问详情或凭据会因为 IPv6 而改变吗？

不会。主机、端口、用户名、密码均保持一致。不支持的参数会被忽略。

### 我可以使用 IPv6 访问 Bright Data 代理服务吗？

不能。我们仅允许 IPv4 访问代理网关。使用 IPv6 会导致 DNS 错误，例如无法解析域名 brd.superproxy.io。

示例 curl 调用：

```sh theme={null}
curl -i --proxy brd.superproxy.io:44445 --proxy-user brd-customer-*******-zone-residential_proxy21:********** "https://geo.brdtest.com/welcome.txt?product=resi&method=native" -g -6
```

错误响应：

```sh theme={null}
curl: (5) Could not resolve proxy: brd.superproxy.io
```

#### IPv6 是否需要设置允许列表和拒绝列表？

不需要。因为访问 Bright Data 代理的连接必须是 IPv4，列表也保持 IPv4 形式。

## 配置独享住宅代理访问

独享住宅代理仅在 Bright Data 合规团队 KYC 批准之后开放。在您的账户完成 KYC 验证之前，控制面板中的"独享"选项保持禁用状态。
更多信息：
[住宅网络访问政策](/cn/proxy-networks/residential/network-access)

### IP 组 `gIPs`

<Note>
  仅在 **独享** 模式适用
</Note>

`gIP` 包含 6–90 个具有相同属性的 IP，用于专门访问区域“配置”中选择的域名。

<Frame>
  <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/proxy-networks/residential/gips.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=7adac028e351fee19c858690c15617fa" alt="Geolocation Targeting" width="526" height="124" data-path="images/proxy-networks/residential/gips.png" />
</Frame>

***

### 域名

<Warning>
  仅在 **独享** 模式适用
</Warning>

定义您的代理要独享访问的域名。对这些域的所有请求都通过您的独享代理处理。

例如：如果列表中包含 a.com 与 b.com
– a.com 与 b.com 的请求始终走您的独享代理
– c.com 请求将走 Bright Data 数据中心代理

<Frame>
  <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/proxy-networks/residential/domains.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=4fff3d30e2ab0aad044f2e05f540961a" alt="Domains" width="518" height="130" data-path="images/proxy-networks/residential/domains.png" />
</Frame>

***

## 高级选项

### 对不可用节点的自动故障切换

如果我们无法为您的请求连接到代理节点，我们会将请求路由到另一个可用节点。当您选择了默认国家时，自动故障切换将不会生效：如果我们无法在您选择的国家找到节点，请求将会以错误告终。

启用自动故障切换后，无论某个特定节点是否可用，都能确保请求得以执行。

#### 使用 IPv6 代理访问未提供 IPv6 地址的目标网站时的自动故障切换

为确保连续性，我们启用了从 IPv6 到 IPv4 的自动故障切换，您可以在区域的高级设置中将其配置为开启或关闭（默认：`ON`）。

当切换为“开启”（默认）时，如果目标网站未发布 IPv6 地址，我们会通过同一位置的可用 IPv4 代理来路由请求。若未启用此开关，在尝试访问未提供 IPv6 地址的目标主机时，将会出现错误： [https://docs.brightdata.com/cn/proxy-networks/errorCatalog#target-40011](https://docs.brightdata.com/cn/proxy-networks/errorCatalog#target-40011)

***

### 特殊端口与协议

端口 `80` 和 `443` 默认可用，支持 HTTP、HTTPS 和 SOCKS5 协议。
我们在数据中心代理网络支持所有 `1024` 以上的端口。
[阅读更多...](/cn/proxy-networks/faqs#how-to-see-supported-ports-and-protocols)

<Accordion title="请求开放更多端口">
  Bright Data 可以根据请求支持额外端口。每个新增端口的请求都会经过 Bright Data 合规团队的专门且额外的审核流程。
  如果您需要额外的端口权限，可以联系 Bright Data 支持团队。
  以下是需要 Bright Data 合规审核后才能启用的端口示例：

  | Port | Protocol |
  | ---- | -------- |
  | `70` | HTTP     |
  | `98` | HTTPS    |
</Accordion>

### 区域使用限制

为您的区域设置使用限制：您可以限制支出或流量。这为您的预算和带宽消耗提供了额外的控制层，主要适用于我们的旋转共享池代理。

#### 如何设置区域使用限制

在代理页面设置使用限制：

1. 打开 [My proxies](https://brightdata.com/cp/zones) 页面。
2. 点击您要限制的代理。
3. 打开 **Access parameters** 标签页。
4. 滚动到 **Limit**（默认为无限制）。
5. 点击 **edit**。
6. 启用支出或流量限制。
7. 通过选择以下之一设置您想要的限制：`$/day`、`$/month`、`bytes/day` 或 `bytes/month`。
8. 点击 **update**。

<Note>
  达到限制时，区域可能会被暂停、发出告警或两者同时发生，具体取决于您的配置。该限制每 15 分钟检查一次，因此可能不会立即生效。如果流量较高，使用统计数据可能会滞后。您可以使用区域 **Statistics** 表中的 **recalc** 按钮重新计算这些数据。
</Note>

要查看某个区域相对于其限制的消耗量，请在控制面板中查看您的区域使用情况。如需更多详情，请参阅[使用监控](/cn/general/usage-monitoring/Usage)和[带宽使用限制常见问题](/cn/general/faqs)。有关共享池带宽公平性的背景信息，请参阅[公平使用额度](/cn/general/usage-monitoring/fair_use_allowance)。
