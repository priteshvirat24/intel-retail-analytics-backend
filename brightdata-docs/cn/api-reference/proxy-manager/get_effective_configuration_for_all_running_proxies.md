> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 获取运行中代理的有效配置

> Bright Data 代理管理器API端点，用于获取正在运行的代理的有效配置。端点：GET /api/proxies_running，端口22999。

**API 端点：** `GET` `/api/proxies_running`

<ResponseExample>
  ```JSON Sample Response theme={null}
  [
      {
          "port": 24000,
          "zone": "ZONE",
          "proxy_type": "persist",
          "customer": "CUSTOMER",
          "password": "password",
          "whitelist_ips":[]
      }
  ]
  ```
</ResponseExample>

<RequestExample>
  ```sh Shell theme={null}
  curl "http://127.0.0.1:22999/api/proxies_running"
  ```

  ```js NodeJS theme={null}
  #!/usr/bin/env node

  (async () => {
    const response = await fetch('http://127.0.0.1:22999/api/proxies_running');
    const data = await response.text();
    console.log(data);
  })();
  ```

  ```java Java theme={null}
  package example;

   

  import org.apache.http.HttpHost;

  import org.apache.http.client.fluent.\*;

   

  public class Example {

    public static void main(String[] args) throws Exception {

      String res = Executor.newInstance()

       .execute(Request.Get("http://127.0.0.1:22999/api/proxies_running"))

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
       RequestUri = new Uri("http://127.0.0.1:22999/api/proxies_running")
      };

      var response = await client.SendAsync(requestMessage);
      var responseString = await response.Content.ReadAsStringAsync();

      Console.WriteLine(responseString);
    }
  }
  ```

  ```python Python theme={null}
  #!/usr/bin/env python

  print('如果出现错误 "ImportError: No module named requests"，请安装它：\n$ sudo pip install requests');

  import requests


  r = requests.get('http://127.0.0.1:22999/api/proxies_running')

  print(r.content)
  ```
</RequestExample>
