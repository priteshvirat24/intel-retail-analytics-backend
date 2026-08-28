> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 地理位置定向

> 地理位置定向允许您根据 `国家`、`城市`、`州`、`ASN` 或 `邮政编码` 定向特定位置

## 国家定向

您可以通过在用户名中添加国家代码来定向特定国家，例如 `username-country-country_code`。仅使用小写的两字母国家代码。

```sh Shell theme={null}
curl "https://example.com" --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-country-us:<zone_password>
```

### 默认国家选择

在所有 Bright Data 共享池代理中：数据中心、ISP、住宅和移动共享池（也称为“旋转代理”），我们在区域配置期间提供默认国家选择。选择国家后，Bright Data 将尝试从所选默认国家分配一个节点。分配顺序如下：

如果配置了默认国家：

1. 从 **默认国家** 列表中随机选择一个国家。

2. 尝试在该国家分配一个节点

3. 如果找到节点：将请求路由到该节点

4. 如果未找到节点：请求失败并返回错误

如果 **未选择默认国家**，Bright Data 将从池中分配一个随机代理节点并通过其路由请求。

### 欧盟国家定向

Bright Data 代理网络以及我们的 Web Unlocker API 允许通过 `-country-eu` 标志专门从 **欧盟成员国** 随机选择节点。需要定向欧盟节点时，这将比仅从单个欧盟国家定向更能提高成功率，同时仍保持节点在欧盟范围内。

## 城市定向

<Note> 城市定向在住宅和移动代理中效果最佳。数据中心和 ISP 代理的城市定向已被弃用，不再可用。 </Note>

您可以通过在用户名中添加城市名称来定向某个国家内的特定城市，例如 `username-country-country_code-city-city_code`。city\_code 仅允许小写且不能有空格，例如 `-city-sanfrancisco`。

```sh Shell theme={null}
curl "https://example.com" --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-country-us-city-sanfrancisco:<zone_password>
```

## 州定向

<Note> 仅限住宅代理 </Note>

对于相关国家（如美国和澳大利亚），您可以通过 `username-country-country_code-state-state_code` 定向某个国家内的州。仅使用小写的两字母州代码。

<CodeGroup>
  ```sh Country: USA theme={null}
  curl "https://example.com" --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-country-us-state-ny:<zone_password> 
  ```

  ```sh Country: Australia theme={null}
  curl "https://example.com" --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-country-au-state-wa:<zone_password>
  ```
</CodeGroup>

## ASN 定向

<Note> 仅限住宅代理 </Note>

您可以从 [ASN 列表](http://bgp.potaroo.net/cidr/autnums.html) 中定向特定 ASN。选择 ASN 的国家方式如下：`-asn-ASN_NUMBER`

```sh Shell theme={null}
curl "https://example.com" --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-asn-56386:<zone_password>
```

## 邮政编码定向

<Note> 仅限住宅代理 </Note>

您可以通过特定区域的邮政编码定向代理节点。例如，定向来自美国孟菲斯且邮政编码为 12345 的 IP：

```sh Shell theme={null}
curl "https://example.com" --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-city-memphis-zip-12345:<zone_password>
```
