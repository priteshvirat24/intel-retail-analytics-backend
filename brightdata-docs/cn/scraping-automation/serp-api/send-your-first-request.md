> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 使用 Bright Data 的 SERP API 发送您的第一个请求

> 通过易于理解的代码示例，逐步指导您发送第一个 SERP API 请求

## 几分钟内发送您的第一个请求

使用此现成代码示例，可在几分钟内测试 SERP API。

<CardGroup cols={3}>
  <Card title="Postman 示例" icon="user-astronaut" iconType="regular" href="https://www.postman.com/bright-data-api/bright-data-api/request/kpq952m/google-search" cta="在 1 分钟内尝试 SERP API" />

  <Card title="Node.js 示例" icon="code" iconType="regular" href="https://github.com/luminati-io/bright-data-serp-api-nodejs-project" cta="在 2 分钟内尝试 SERP API" />

  <Card title="Python 示例" icon="code" iconType="regular" href="https://github.com/luminati-io/bright-data-web-unlocker-python-project" cta="在 5 分钟内尝试 SERP API" />
</CardGroup>

Bright Data 提供两种访问 SERP API 的方法，两者提供 **相同** 结果，同时适应不同客户的工作流程：

<CardGroup cols={2}>
  <Card title="直接 API 访问（推荐）" href="/cn/scraping-automation/serp-api/send-your-first-request#direct-api-access-recommended">
    纯 REST API 方法，便于访问并实现直接集成。
  </Card>

  <Card title="基于代理的本地访问" href="/cn/scraping-automation/serp-api/send-your-first-request#native-proxy-based-access">
    适用于依赖代理路由的工作流程。
  </Card>
</CardGroup>

## 直接 API 访问（推荐）

一种简单、RESTful 的方式与 Bright Data 的 SERP API 交互。直接 API 访问抽象了代理管理，让您通过单一端点发送请求，确保使用简单且易于集成 REST API。

### 最适合：

* 集中端点：通过单一 RESTful 端点访问 SERP API。
* 简化直接集成：无需管理代理或路由。
* 单一 API key 认证：安全易用，替代用户名密码管理。

### 发送您的第一个请求

在 [设置](/cn/scraping-automation/serp-api/quickstart) SERP API zone 后，您将在 zone 的 **Overview** 标签页中找到工作请求示例和 API key：

<Frame>
  <img src="https://mintcdn.com/brightdata/S8tFtc_KJjCQxqv1/images/scraping-automation/serp-api/send-your-first-request/serp_api_zone_overview_code_example.png?fit=max&auto=format&n=S8tFtc_KJjCQxqv1&q=85&s=64bb0d6172264568a991a0967d2a3d76" alt="SERP API Overview 标签页" width="1504" height="831" data-path="images/scraping-automation/serp-api/send-your-first-request/serp_api_zone_overview_code_example.png" />
</Frame>

以下是简单 SERP API cURL 请求示例：

```sh Direct API access - cURL theme={null}
curl -H "Content-Type: application/json" -H "Authorization: Bearer [INSERT_YOUR_API_KEY]" -d '{"zone": "[INSERT_YOUR_SERP_API_ZONE_NAME]","url": "[INSERT_YOUR_TARGET_URL]", "format": "raw"}' https://api.brightdata.com/request
```

### 请求说明

1. API 端点: [`https://api.brightdata.com/request`](https://api.brightdata.com/request)
2. Authorization Header: `Authorization: Bearer [INSERT YOUR API key]`

   * API key 可在 SERP API zone 中找到
3. Payload:

   * `zone`：您的 SERP API **zone 名称**
   * `url`：完整 SERP 目标 URL（包含查询参数）
   * `format`：定义响应格式，使用 `raw` 可获取目标站点的原始响应

### 生成 Bright Data API key

Bright Data API key 是通过直接 API 访问 SERP API 的安全认证令牌。创建新的 SERP API zone 时，API key 会自动生成，可在 zone 的 **Overview** 标签页中找到：

<Frame>
  <img src="https://mintcdn.com/brightdata/S8tFtc_KJjCQxqv1/images/scraping-automation/serp-api/send-your-first-request/serp_api_zone_overview_api_token.png?fit=max&auto=format&n=S8tFtc_KJjCQxqv1&q=85&s=eec1306e0ef8b8fc395a8680ce5a4482" alt="SERP API key" width="1504" height="831" data-path="images/scraping-automation/serp-api/send-your-first-request/serp_api_zone_overview_api_token.png" />
</Frame>

**生成新的 API key：**

* 前往 [账户设置](https://www.bright.cn/cp/setting/users)
* 向下滚动并点击 “Add API key”
* 按屏幕提示完成流程

<Tip>
  强烈建议为 API key 设置过期时间以提高安全性
</Tip>

<Warning>
  API key 仅在屏幕上显示一次，请确保复制并安全存储
</Warning>

## 基于代理的本地访问

访问 SERP API 时，需要提供以下凭据：

1. Customer ID
2. SERP API zone 名称
3. SERP API 密码
4. Bright Data SSL 证书

#### Customer ID

Customer ID 可在欢迎邮件中找到，或点击控制面板右上角账户首字母查看，或点击此处：[账户设置](https://www.bright.cn/cp/setting/customer_details)

#### Zone 名称和密码

在控制面板 Web Unlocker API zone 的 Overview 标签页中找到 zone 名称和密码

#### Bright Data SSL 证书

<Warning>
  设置 Bright Data SSL 证书以防止 SSL 错误
</Warning>

SSL 证书可在 zone Overview 顶部菜单的 “SSL certificate” 向导中下载。更多说明见：[SSL 证书](/cn/general/account/ssl-certificate#how-to-download-the-ssl-certificate)

或者，可以选择 [忽略 SSL 错误](/cn/general/account/ssl-certificate#how-to-ignore-ssl-errors)

#### SERP API：HTTPS 代理示例代码

获取 API 凭据后，使用以下代码发送第一个请求：

<CodeGroup>
  ```sh cURL theme={null}
  curl "https://www.google.com/search?q=pizza" --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>:<zone_password> -k
  ```

  ```js Node.js theme={null}
  #!/usr/bin/env node

  require('request-promise')({
      url: 'https://www.google.com/search?q=pizza',
      proxy: 'http://brd-customer-<customer_id>-zone-<zone_name>:<zone_password>@brd.superproxy.io:44445',
    })
    .then(function (data) {
        console.log(data);
      },
      function (err) {
        console.error(err);
      });
  ```

  ```python Python theme={null}
  import pprint
  import requests

  host = 'brd.superproxy.io'
  port = 44445

  username = 'brd-customer-<customer_id>-zone-<zone_name>'
  password = '<zone_password>'

  proxy_url = f'http://{username}:{password}@{host}:{port}'

  proxies = {
      'http': proxy_url,
      'https': proxy_url
  }

  url = "https://www.google.com/search?q=pizza&brd_json=1"
  response = requests.get(url, proxies=proxies, verify=False)
  pprint.pprint(response.json())
  ```

  ```php PHP theme={null}
  <?php
  echo '要启用免费试用账户并获取 CUSTOMER, YOURZONE 和 YOURPASS，请联系 sales@brightdata.com';
  $curl = curl_init('https://www.google.com/search?q=pizza');
  curl_setopt($curl, CURLOPT_PROXY, 'http://brd.superproxy.io:44445');
  curl_setopt($curl, CURLOPT_PROXYUSERPWD, 'brd-customer-<customer_id>-zone-<zone_name>:<zone_password>');
  curl_exec($curl);
  ?>
  ```

  ```ruby Ruby theme={null}
  #!/usr/bin/ruby

  require 'uri'
  require 'net/http'
  require 'net/https'

  puts '要启用免费试用账户并获取 CUSTOMER, YOURZONE 和 YOURPASS，请联系 sales@brightdata.com'

  uri = URI.parse('https://www.google.com/search?q=pizza')
  proxy = Net::HTTP::Proxy('brd.superproxy.io', 44445, 'brd-customer-<customer_id>-zone-<zone_name>', '<zone_password>')

  req = Net::HTTP::Get.new(uri)

  result = proxy.start(uri.host,uri.port, :use_ssl => uri.scheme == 'https') do |http|
      http.request(req)
  end

  puts result.body
  ```

  ```cs C# theme={null}
  using System;
  using System.Net;

  class Example {
    static void Main() {
      var client = new WebClient();
      client.Proxy = new WebProxy("brd.superproxy.io:44445");
      client.Proxy.Credentials = new NetworkCredential(
        "brd-customer-<customer_id>-zone-<zone_name>",
        "<zone_password>"
      );
      Console.WriteLine(client.DownloadString("https://www.google.com/search?q=pizza"));
    }
  ```

  ```java Java theme={null}
  package example;

  import org.apache.http.HttpHost;
  import org.apache.http.client.fluent.*;

  public class Example {
      public static void main(String[] args) throws Exception {
          System.out.println("要启用免费试用账户并获取 CUSTOMER, YOURZONE 和 YOURPASS，请联系 sales@brightdata.com");
          HttpHost proxy = new HttpHost("brd.superproxy.io", 44445);
          String res = Executor.newInstance()
              .auth(proxy, "brd-customer-<customer_id>-zone-<zone_name>", "<zone_password>")
              .execute(Request.Get("https://www.google.com/search?q=pizza").viaProxy(proxy))
              .returnContent().asString();
          System.out.println(res);
      }
  }
  ```

  ```perl Perl theme={null}
  #!/usr/bin/perl

  print '要启用免费试用账户并获取 CUSTOMER, YOURZONE 和 YOURPASS，请联系 sales@brightdata.com';
  use LWP::UserAgent;
  my $agent = LWP::UserAgent->new();
  $agent->proxy(['http', 'https'], "http://brd-customer-<customer_id>-zone-<zone_name>:<zone_password>\@brd.superproxy.io:44445");
  print $agent->get('https://www.google.com/search?q=pizza')->content();
  ```

  ```vb VBA theme={null}
  Imports System.Net

  Module Module1
      Sub Main()
          Console.WriteLine("要启用免费试用账户并获取 CUSTOMER, YOURZONE 和 YOURPASS，请联系 sales@brightdata.com")
          Dim Client As New WebClient
          Client.Proxy = New WebProxy("http://brd.superproxy.io:44445")
          Client.Proxy.Credentials = New NetworkCredential("brd-customer-<customer_id>-zone-<zone_name>", "<zone_password>")
          Console.WriteLine(Client.DownloadString("https://www.google.com/search?q=pizza"))
      End Sub
  End Module
  ```
</CodeGroup>
