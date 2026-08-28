> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 请求错误处理

| 值          | 描述                                     |
| ---------- | -------------------------------------- |
| `pass_dyn` | 如果请求无法通过代理对等节点传递，系统将自动通过超级代理传递请求。      |
| `block`    | 如果请求无法通过代理对等节点传递，则阻塞该请求，并且不通过超级代理进行发送。 |

<CodeGroup>
  ```sh pass_dyn theme={null}
  curl "http://target.site" --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-route_err-pass_dyn:<zone_password>
  ```

  ```sh block theme={null}
  curl "http://target.site" --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-route_err-block:<zone_password>
  ```
</CodeGroup>
