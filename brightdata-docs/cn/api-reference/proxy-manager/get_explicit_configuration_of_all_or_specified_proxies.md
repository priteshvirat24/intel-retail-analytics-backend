> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 获取代理的显式配置

> Bright Data代理管理器API端点，用于获取代理的显式配置。端点：端口22999上的GET /api/proxies/{PORT}。

**API 端点:** `GET` `/api/proxies/{PORT}`

<ParamField path="PORT" type="string">
  PORT 参数是可选的。您可以跳过它以获取所有代理\*
</ParamField>

<ResponseExample>
  ```JSON Sample Response theme={null}
  [
      {"port": 24000,
      "zone": "ZONE",
      "proxy_type": "persist",
      "customer": "CUSTOMER",
      "password": "password",
      "whitelist_ips": []
      },
      {
          "port": 44445,
          "zone": "ZONE",
          "listen_port": 44445,
          "customer": "CUSTOMER",
          "password":"password"
      }
  ]
  ```
</ResponseExample>

<RequestExample>
  ```sh Shell theme={null}
  curl "http://127.0.0.1:22999/api/proxies/{PORT}"
  ```

  ```js NodeJS theme={null}
  #!/usr/bin/env node

  (async () => {
    const response = await fetch('http://127.0.0.1:22999/api/proxies/{PORT}');
    const data = await response.text();
    console.log(data);
  })();
  ```

  ```java Java theme={null}
  package example;

   

  import org.apache.http.HttpHost;
  import org.apache.http.client.fluent.*;

   

  public class Example {

    public static void main(String[] args) throws Exception {

      String res = Executor.newInstance()

       .execute(Request.Get("http://127.0.0.1:22999/api/proxies/{PORT}"))

       .returnContent().asString();

      System.out.println(res)

    }

  }
  ```

  ```cs C# theme={null}
  using System;

  using System.Net;

  using System.Net.Http;

  using System.Net.Http.Headers;

   

  public class Program {

    public static async Task Main() {

      var client = new HttpClient();

      var requestMessage = new HttpRequestMessage {

        Method = HttpMethod.Get,

       RequestUri = new Uri("http://127.0.0.1:22999/api/proxies/{PORT}")

      };

      var response = await client.SendAsync(requestMessage);

      var responseString = await response.Content.ReadAsStringAsync();

      Console.WriteLine(responseString);

    }

  }
  ```

  ```python Python theme={null}
  #!/usr/bin/env python

  print('如果您收到错误 "ImportError: No module named requests"，请安装它:\n$ sudo pip install requests');

  import requests

   

  r = requests.get('http://127.0.0.1:22999/api/proxies/{PORT}')

  print(r.content)
  ```
</RequestExample>
