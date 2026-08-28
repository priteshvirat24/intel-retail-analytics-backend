> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 获取最近状态

> 使用 Bright Data 代理管理器 API 获取最近状态。在本地代理管理器端口 22999 上调用 GET /api/recent_stats。

**API 端点:** `GET /api/recent_stats`

<ResponseExample>
  ```JSON 示例响应 theme={null}
  {
      "ports": {},
      "status_code": [],
      "hostname": [],
      "protocol": [],
      "total": 0,
      "success": 0,
      "ssl_enable":true}
  ```
</ResponseExample>

<RequestExample>
  ```sh Shell theme={null}
  curl "http://127.0.0.1:22999/api/recent_stats"
  ```

  ```js NodeJS theme={null}
  #!/usr/bin/env node

  (async () => {
    const response = await fetch('http://127.0.0.1:22999/api/recent_stats');
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

          String res = Executor.newInstance().execute(
              Request.Get("http://127.0.0.1:22999/api/recent_stats")
          ).returnContent().asString();

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
              RequestUri = new Uri("http://127.0.0.1:22999/api/recent_stats")
          };

          var response = await client.SendAsync(requestMessage);
          var responseString = await response.Content.ReadAsStringAsync();
          Console.WriteLine(responseString);
      }
  }
  ```

  ```python Python theme={null}
  #!/usr/bin/env python

  print('如果收到错误 "ImportError: No module named requests",请安装:\n$ sudo pip install requests');

  import requests


  r = requests.get('http://127.0.0.1:22999/api/recent_stats')

  print(r.content)
  ```
</RequestExample>
