> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何配置您的数据中心代理

> 通过本指南了解如何配置您的数据中心代理设置、选择 IP 类型、设置地理定位目标以及启用高级功能。

要访问您的代理配置，请在 **“配置”** 选项卡中打开您的区域。

## IP 类型

Bright Data 提供 3 种类型的数据中心代理：

<Card title="共享" icon="square-1" horizontal="true">
  轮换代理，使用约 40,000 个代理池，按使用 GB 付费。
</Card>

<Card title="共享无限" icon="square-2" horizontal="true">
  一组特定的代理，与其他用户共享，具有无限带宽，按代理付费。
</Card>

<Card title="独享无限" icon="square-3" horizontal="true">
  一组特定的代理，供您独享，具有无限带宽，按代理付费。
</Card>

## 共享（轮换）代理配置

### 默认国家选择

在共享代理池配置中选择国家/地区时，我们将仅分配您选择的国家/地区的代理。您可以选择不选（这意味着我们将从代理池中分配下一个随机代理）、一个或多个国家/地区。 [了解更多...](/cn/api-reference/proxy/geolocation-targeting#默认国家选择)

要在轮换期间为您的节点选择特定国家/地区，请在代理用户名参数中使用带 ISO-3166 国家/地区代码的标记 `-country`。

[常见问题解答：可以在哪里查看国家代码列表？](/cn/general/faqs#可以在哪里查看国家代码列表？)

## 共享和独享无限代理配置

### IP 数量

<Tip>
  对于无限代理，我们将根据您为每个区域购买的代理数量提供折扣。您购买得越多，每个代理的费用就越低。点击您的区域设置中的 **“费率”** 链接查看费率。
</Tip>

将分配的 IP 数量作为您的可用 IP 池。

### 国家/地区选择

地理定位目标允许您定位特定的 `Country`（国家/地区）。

从下拉菜单中选择首选国家/地区。

一旦选择，我们将从这些国家/地区分配代理。如果我们没有足够的代理来满足您的要求，我们将分配我们拥有的数量，您可以提交完整数量代理的订单（我们不允许单个代理订单 - 我们只接受批量订单）。

更改此选择意味着重新分配代理，这将产生 **刷新费用** 。

### 多国选择是如何运作的？

如果您选择多个国家/地区，我们将在分配时在 **可用国家/地区** 中分配代理。例如：如果您选择德国、法国和意大利的代理，我们将提供这些国家/地区中 **任一** 个的代理。我们将尝试在您选择的国家/地区中均匀分配，但是如果其中一个国家/地区的代理数量不足，一些国家/地区的代理数量会比其他国家/地区多。

因此，参考该示例，如果您请求来自德国、法国和意大利的 30 个代理，而我们在意大利只有 6 个可用代理，您将获得：12 个来自德国的代理，12 个来自法国的代理和 6 个来自意大利的代理。

<Frame>
  <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/proxy-networks/data-center/geotargeting.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=f849e3eb3e6630cdd9e2c95dfb6ba930" alt="Geolocation Targeting" width="572" height="358" data-path="images/proxy-networks/data-center/geotargeting.png" />
</Frame>

### 更改国家/地区

可以更改您为代理选择的国家/地区。一旦您更改国家/地区，Bright Data 将从选定的国家/地区分配新的代理。由于这是代理的替换，您将收到一个新的 IP。

更改国家/地区类似于 IP 刷新操作，并收取相同的费用。

## 访问您分配的代理 IP 地址

在所有代理类型中，您都可以通过以下步骤下载、查看和复制已分配给您的 IP：

1. 导航到 [区域页面](https://www.bright.cn/cp/zones)。
2. 选择一个已分配 IP 的区域。
3. 在概览选项卡中，单击 **“下载”**、**“查看”** 或 **“复制”**。

<img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/proxy-networks/data-center/configure-your-proxy/your-proxy-list.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=31997c6595461a3b94ce0c4f8b873cd4" alt="your-proxy-list" width="1465" height="607" data-path="images/proxy-networks/data-center/configure-your-proxy/your-proxy-list.png" />

***

## 高级选项

### 自动故障转移

如果您的请求无法到达代理节点，我们会将请求路由到另一个可用的节点。当您选择默认国家/地区时，自动故障转移不适用：如果我们无法找到您所选国家/地区的节点，请求将因错误而失败。

启用自动故障转移可确保请求执行，无论特定节点的可用性如何。

***

### 特殊端口和协议

默认情况下，端口 `80` 和 `443` 可用，支持 HTTP 和 HTTPS 及 SOCKS5 协议。我们的数据中心代理网络还支持所有高于 `1024` 的端口。 [了解有关端口和协议的更多信息...](/cn/proxy-networks/faqs#如何查看支持的端口和协议)

<Accordion title="请求其他端口">
  Bright Data 可以根据请求支持其他端口。在支持新端口的每个请求之后，都将进行与 Bright Data 合规团队的专门和额外的合规流程。
  如果您需要额外的端口权限，可以联系 Bright Data 支持团队。
  激活前需要 Bright Data 合规性审核的端口示例：

  | 端口   | 协议    |
  | ---- | ----- |
  | `70` | HTTP  |
  | `98` | HTTPS |
</Accordion>

### 区域使用限制

为您的区域设置使用限制：您可以限制支出或流量。这为您的预算和带宽消耗提供了额外的控制层，主要针对我们的轮换共享代理池。
