> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 选择特定的 IP

> 配置 Bright Data 代理 REST API，在端口 44445 上选择特定的 IP，并提供参数和响应字段的参考。

该选项仅适用于分配了多个 IP 的区域。 要将分配给您的区域的特定 IP 作为目标，请使用 `-ip-ip_address` 请求参数。

```sh Shell theme={null}
curl "http://target.site" --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-ip-1.2.3.4:<zone_password>
```
