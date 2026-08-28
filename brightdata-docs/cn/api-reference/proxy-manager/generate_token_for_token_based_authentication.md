> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 生成 API 密钥

> 生成一个Bright Data代理管理器API密钥用于基于令牌的身份验证。端点：端口22999上的GET /api/gen_token。

**API 端点:** `GET` `/api/gen_token`

<ResponseExample>
  ```json Sample Response theme={null}
  {
      "token": "RZD9vaQQaL6En7"
  }
  ```
</ResponseExample>

<RequestExample>
  ```sh Shell theme={null}
  curl "http://127.0.0.1:22999/api/gen_token"
  ```

  ```js NodeJS theme={null}
  #!/usr/bin/env node

  (async () => {
    const response = await fetch('http://127.0.0.1:22999/api/gen_token');
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

       .execute(Request.Get("http://127.0.0.1:22999/api/gen_token"))

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
              RequestUri = new Uri("http://127.0.0.1:22999/api/gen_token")
          };

          var response = await client.SendAsync(requestMessage);
          var responseString = await response.Content.ReadAsStringAsync();

          Console.WriteLine(responseString);
      }
  }
  ```

  ```python Python theme={null}
  #!/usr/bin/env python

  print('如果出现错误"ImportError: No module named requests"，请安装它：\n$ sudo pip install requests');

  import requests


  r = requests.get('http://127.0.0.1:22999/api/gen_token')

  print(r.content)
  ```
</RequestExample>
