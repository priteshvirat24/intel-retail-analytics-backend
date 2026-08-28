> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 获取被封禁的IP

> 使用Bright Data代理管理器API获取被封禁的IP。在本地代理管理器端口22999上调用GET /api/banlist/{PORT}。

**API 端点:** `GET` `/api/banlist/{PORT}`

<ParamField query="full" type="boolean">
  `full=true` 参数是可选的，可用于提供禁止列表中每个条目的其他详细信息
</ParamField>

<ResponseExample>
  ```JSON Sample Response theme={null}
  {
      "ips": [
          "10.20.30.40",
          "50.60.70.80|example.com"
      ]
  }
  ```
</ResponseExample>

<RequestExample>
  ```sh Shell theme={null}
  curl "http://127.0.0.1:22999/api/banlist/{PORT}?full=true"
  ```

  ```js NodeJS theme={null}
  #!/usr/bin/env node

  (async () => {
    const response = await fetch('http://127.0.0.1:22999/api/banlist/{PORT}?full=true');
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
       .execute(Request.Get("http://127.0.0.1:22999/api/banlist/{PORT}?full=true"))
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

       RequestUri = new Uri("http://127.0.0.1:22999/api/banlist/{PORT}?full=true")

      };

      var response = await client.SendAsync(requestMessage);

      var responseString = await response.Content.ReadAsStringAsync();

      Console.WriteLine(responseString);

    }

  }
  ```

  ```python Python theme={null}
  #!/usr/bin/env python

  print('如果您收到错误 "ImportError: No module named requests"，请安装它：\n$ sudo pip install requests');

  import requests

   

  r = requests.get('http://127.0.0.1:22999/api/banlist/{PORT}?full=true')

  print(r.content)
  ```
</RequestExample>
