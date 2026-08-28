> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 直接从超级代理发送请求

> 配置 Bright Data 代理 REST API，在端口 44445 上直接从超级代理发送请求，并提供参数和响应字段的参考。

您可以选择直接从超级代理而不是对等 IP 执行请求。 在这种情况下，通过在请求授权字符串中添加 `-direct`，请求的 IP 将是超级代理的 IP。

```sh Shell theme={null}
curl "http://target.site" --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-direct:<zone_password>
```
