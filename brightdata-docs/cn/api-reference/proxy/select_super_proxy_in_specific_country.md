> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 在特定国家/地区选择超级代理

重要说明：本文仅适用于选择“超级代理”，这种情况很少需要。如果您想选择特定的标准代理（例如住宅代理、数据中心代理或 ISP 代理）：

* 在 **共享代理区域**，您可以在代理用户名中添加 '-country' 标志（也可加 '-city'），例如：`username-country-country_code-city-city_code`。国家代码为标准两字符代码。city\_code 仅允许小写且无空格，例如 `-city-sanfrancisco`。

* 在 **专用代理区域**，您可以通过以下步骤在区域配置页面中选择国家和城市：

  1. 添加一个新的代理区域，并将 IP 类型设置为“专用”

  2. 选择您希望此区域覆盖的域名

  3. 选择您希望分配到该区域的专用代理数量

  4. 选择您希望定向的国家

  5. 可选 - 选择完国家后，点击每个国家旁的“添加城市”以进行城市定向

  6. 为每个国家添加所选城市并保存区域

  7. 新的专用代理区域将根据您选择的国家和城市均匀分配所请求的 grproxy 数量

如果您确实需要我们的负载均衡器在特定国家提供超级代理：

<Note>
  如果未选择特定服务器国家，Bright Data 将自动选择最优负载均衡服务器以提高速度。如果速度是您的首要考虑，请谨慎使用此功能，因为长期使用可能对性能产生负面影响。
</Note>

选择超级代理国家的方法如下：`servercountry-{country}`.brd.superproxy.io，例如 `servercountry-gb.brd.superproxy.io`。

```sh Shell theme={null}
curl "https://example.com" --proxy servercountry-gb.brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>:<zone_password>
```
