> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 发送第一个请求

> 我们以多种编程语言提供易于理解的代码示例，以便您了解如何使用Bright Data的代理产品发送第一个请求。

<Accordion title="本指南适用于所有代理产品" icon="check">
  1. 住宅代理
  2. 移动代理
  3. ISP代理
  4. 数据中心代理
  5. SERP API
  6. Browser API
  7. Web Unlocker API
</Accordion>

首先，请准备好代理凭据、用户名、密码以及主机名称。您可以在代理产品的访问参数或概述选项卡中找到这些凭据。

## 代码示例

准备好代理凭据后，请使用以下代码发送您的第一个请求：

<CodeGroup>
  ```sh cURL theme={null}
  curl "http://brdtest.com/myip.json" --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer_id>-zone-<zone_name>:<zone_password>
  ```

  ```javascript Node.js theme={null}
  #!/usr/bin/env node

  require('request-promise')({
      url: 'http://brdtest.com/myip.json',
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


  url = "http://brdtest.com/myip.json"
  response = requests.get(url, proxies=proxies)
  pprint.pprint(response.json())

  ```

  ```php PHP theme={null}

  <?php
  echo 'To enable your free eval account and get CUSTOMER, YOURZONE and '
      .'YOURPASS, please contact sales@brightdata.com';
  $curl = curl_init('http://brdtest.com/myip.json');
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

  puts 'To enable your free eval account and get CUSTOMER, YOURZONE and YOURPASS, please contact sales@brightdata.com'

  uri = URI.parse('http://brdtest.com/myip.json')
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
      Console.WriteLine(client.DownloadString("http://brdtest.com/myip.json"));
    }
  ```

  ```java Java theme={null}
  package example;

  import org.apache.http.HttpHost;
  import org.apache.http.client.fluent.*;

  public class Example {
      public static void main(String[] args) throws Exception {
          System.out.println("To enable your free eval account and get "
              +"CUSTOMER, YOURZONE and YOURPASS, please contact "
              +"sales@brightdata.com");
          HttpHost proxy = new HttpHost("brd.superproxy.io", 44445);
          String res = Executor.newInstance()
              .auth(proxy, "brd-customer-<customer_id>-zone-<zone_name>", "<zone_password>")
              .execute(Request.Get("http://brdtest.com/myip.json").viaProxy(proxy))
              .returnContent().asString();
          System.out.println(res);
      }
  }
  ```

  ```perl Perl theme={null}
  #!/usr/bin/perl

  print 'To enable your free eval account and get CUSTOMER, YOURZONE and '
      .'YOURPASS, please contact sales@brightdata.com';
  use LWP::UserAgent;
  my $agent = LWP::UserAgent->new();
  $agent->proxy(['http', 'https'], "http://brd-customer-<customer_id>-zone-<zone_name>:<zone_password>\@brd.superproxy.io:44445");
  print $agent->get('http://brdtest.com/myip.json')->content();
  ```

  ```vb VBA theme={null}
  Imports System.Net

  Module Module1
      Sub Main()
          Console.WriteLine("To enable your free eval account and get " & 
              "CUSTOMER, YOURZONE and YOURPASS, please contact " &
              "sales@brightdata.com")
          Dim Client As New WebClient
          Client.Proxy = New WebProxy("http://brd.superproxy.io:44445")
          Client.Proxy.Credentials = New NetworkCredential("brd-customer-<customer_id>-zone-<zone_name>", "<zone_password>")
          Console.WriteLine(Client.DownloadString("http://brdtest.com/myip.json"))
      End Sub
  End Module
  ```
</CodeGroup>

上面的代码是使用住宅代理向[http://brdtest.com/myip.json发送请求。](http://brdtest.com/myip.json发送请求。) 它会以JSON格式返回您的IP信息：

```json 输出 theme={null}
{
  "ip": "ALLOCATED_IP",
  "country": "PK",
  "asn": {
    "asnum": 203020,
    "org_name": "HostRoyale Technologies Pvt Ltd"
  },
  "geo": {
    "city": "Islamabad",
    "region": "IS",
    "region_name": "Islamabad",
    "postal_code": "44040",
    "latitude": 33.7233,
    "longitude": 73.0435,
    "tz": "Asia/Karachi",
    "lum_city": "islamabad",
    "lum_region": "is"
  }
}
```

现在，将“[https://brdtest.com/myip.json”替换为您选择的网站，然后](https://brdtest.com/myip.json”替换为您选择的网站，然后)...

完成了！
