> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 发送您的第一个请求

下面是一个使用 cURL 的最简单 Web Unlocker API 请求示例，该请求会返回一个 JSON:

```sh theme={null}
curl "https://geo.brdtest.com/welcome.txt" --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>:<zone_password>
```

您可以在代理区域的“访问参数”选项卡中找到您的 API 凭据，包括用户名（Customer\_ID）、区域名称和密码。

|                                                                                                                        |                                         |
| ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| `brd.superproxy.io`                                                                                                    | 我们的负载均衡器地址，它将为您的请求找到最快的超级代理             |
| <Tooltip tip="端口 44445 是推荐使用的代理端口，点击了解更多">[`44445`](/cn/general/faqs#which-port-shall-i-use-22225-or-33335) </Tooltip> | 我们的超级代理的基础设施端口，用于接收您的请求                 |
| `-user brd-customer-<customer_id>-zone-<zone_name>`                                                                    | 用户名验证。 它以最基本的形式定义了您的用户名以及您将在请求中使用哪个区域。  |
| `<zone_password>`                                                                                                      | 区域密码。 所有区域都有用于身份验证的密码                   |
| [https://geo.brdtest.com/welcome.txt](https://geo.brdtest.com/welcome.txt)                                             | 替换为您的目标域名。 这只是一个用于测试的服务器占位符。            |

有关所有 API 用例、集成和偏好的深入互动展示，请参阅我们的 API 示例页面:
[https://www.bright.cn/cp/zones/proxy\_examples](https://www.bright.cn/cp/zones/proxy_examples)

<Tip>
  您需要注册（免费）并登录 Bright Data 控制面板，才能访问此 API 工具。如果您添加了支付方式，您甚至会收到 5 美元的积分，以便开始使用！
</Tip>
