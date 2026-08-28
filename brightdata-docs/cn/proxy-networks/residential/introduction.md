> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 住宅代理简介

> Bright Data 住宅代理网络：每月 4 亿+ 住宅 IP，覆盖 195+ 国家，可作为真实用户进行浏览和数据收集。

Bright Data 的[住宅代理网络](https://www.bright.cn/proxy-types/residential-proxies)通过覆盖 195+ 国家的 4 亿+ 真实住宅 IP 路由您的流量，使目标网站将您的请求视为真实的本地用户。它专为访问那些会阻止数据中心和自动化流量的复杂、高度受保护网站而构建。

与数据中心代理不同，住宅代理通过真实用户拥有的真实设备路由请求，这些用户已明确选择加入网络并因参与而获得补偿。这使您的流量看起来源自您所定位位置的真实住宅连接。

```sh Native proxy access theme={null}
curl "http://brdtest.com/myip.json" \
  --proxy brd.superproxy.io:44445 \
  --proxy-user brd-customer-<customer_id>-zone-<zone_name>:<zone_password>
```

响应会报告出口 IP 及其位置。有关 Python、Node.js 和 cURL 示例，请参阅[发送您的第一个请求](/cn/proxy-networks/residential/send-your-first-request)。

## 住宅代理如何工作

当您通过住宅代理网络发送请求时，Bright Data 会将其路由通过您所选目标区域中的真实住宅设备。对于每个请求，网络会自动：

* 从目标位置选择适当的住宅 IP
* 管理 IP 可用性和轮换
* 在需要粘性会话时维持会话稳定性
* 处理网络级的可靠性和扩展

由于请求源自真实的家庭或移动连接，网站会将该流量视为真实的最终用户，而不是基于服务器的代理。

## 为什么使用住宅代理

在所有 Bright Data 代理类型中，住宅代理为您提供最广泛的 IP 池和最真实的痕迹：

* 在具有严格防机器人或反爬虫防护的网站上，成功率高于数据中心代理
* 访问本地化内容，如地区定价、语言变体和地理受限页面
* 4 亿+ 的 IP 池，降低命中被阻止或重复使用地址的几率
* 可从单个请求扩展到生产级工作负载的基础设施

## 何时应该使用住宅代理

住宅代理非常适合：

* 作为真实用户浏览复杂网站并与之交互
* 商业智能、市场研究和竞争对手监控
* 跨不同区域的广告验证和品牌保护
* 价格比较和产品可用性跟踪
* [数据中心代理](/cn/proxy-networks/data-center/introduction)或 [ISP 代理](/cn/proxy-networks/isp/introduction)返回低成功率或频繁被阻止的场景

如果您目前在使用数据中心代理或 ISP 代理时遇到访问问题，切换到住宅代理可以显著提高可靠性。

## 提供哪些地理定位

住宅代理网络支持细粒度定位。您可以按以下方式路由流量：

* 国家
* 州或地区（如支持）
* 城市
* 邮编（仅限美国）
* ASN 和运营商（取决于代理配置）

## 住宅代理网络的来源如何

Bright Data 的住宅代理网络基于明确的选择加入模式构建。每位参与者：

* 被告知其 IP 的使用方式
* 通过批准的应用程序提供同意
* 因参与而获得补偿

此模式使网络符合数据保护法规，并支持对住宅 IP 的负责任、透明使用。

## 常见问题

### Bright Data 拥有多少住宅 IP？

住宅代理网络提供覆盖 195+ 国家的 4 亿+ 住宅 IP，每月刷新。

### 住宅代理与 ISP 代理和数据中心代理有何不同？

住宅 IP 来自真实的最终用户设备，因此比数据中心代理更不容易被严格的防机器人系统阻止。ISP 代理提供数据中心速度和住宅注册的 IP，而住宅代理则提供最广泛的 IP 池和最真实的痕迹。

### 可以定位特定城市或邮编吗？

可以。您可以按国家、州或地区、城市、邮编（仅限美国）以及 ASN 或运营商进行定位，具体取决于您的配置。

### Bright Data 的住宅网络是否符合道德来源？

是的。每个 IP 都来自通过批准的应用程序选择加入的参与者，这些参与者被告知其 IP 的使用方式，并因参与而获得补偿。

<Tip>
  如果您需要一个完全托管的解除阻止解决方案，该方案超越基于 IP 的访问，自动处理网站特定的标头、Cookie、CAPTCHA、JavaScript 挑战和重试，请使用 [Web Unlocker API](/cn/scraping-automation/web-unlocker/introduction)。
</Tip>

## 相关内容

<CardGroup cols={2}>
  <Card title="快速开始" icon="rocket" href="/cn/proxy-networks/residential/quickstart">
    创建住宅代理 zone 并获取您的凭据。
  </Card>

  <Card title="发送您的第一个请求" icon="paper-plane" href="/cn/proxy-networks/residential/send-your-first-request">
    使用 Python、Node.js 或 cURL 路由您的第一个请求。
  </Card>

  <Card title="网络访问" icon="key" href="/cn/proxy-networks/residential/network-access">
    完成 KYC 并解锁完整的住宅访问权限。
  </Card>

  <Card title="配置您的代理" icon="sliders" href="/cn/proxy-networks/residential/configure-your-proxy">
    设置国家定位、会话控制和轮换。
  </Card>
</CardGroup>
