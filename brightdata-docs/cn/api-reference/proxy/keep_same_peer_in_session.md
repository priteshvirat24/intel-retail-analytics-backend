> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 禁用节点轮换

您可以在会话中使用的节点离线时避免为会话分配新的节点。使用此选项参数时，如果会话中使用的节点离线，您的请求将返回 `502` 错误码，并显示以下错误信息：

```sh Error Message theme={null}
502 Proxy Error: server_error Failed to establish connection with peer
```

此工作流程对于由真实 PC 和移动设备组成的住宅和移动代理区域非常有用。

使用方法是在会话名称后添加 `-const`，例如 `-session-mystring12345-const`。

```sh Shell theme={null}
curl "http://target.site" --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-session-mystring12345-const:<zone_password>
```
