> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 刷新代理管理器端口会话

> Bright Data 代理管理器 API 端点，用于刷新代理管理器端口会话。端点：GET /api/refresh_sessions/{PORT}，端口号为 22999。

**API 端点:** `GET` `/api/refresh_sessions/{PORT}`

## 路径参数

<ParamField path="PORT" type="string" required>
  现有代理端口号
</ParamField>

<RequestExample>
  ```sh Shell theme={null}
  curl "http://127.0.0.1:22999/api/refresh_sessions/{PORT}"
  ```

  ```js NodeJS theme={null}
  #!/usr/bin/env node

  (async () => {
    const response = await fetch('http://127.0.0.1:22999/api/refresh_sessions/{PORT}');
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

       .execute(Request.Get("http://127.0.0.1:22999/api/refresh_sessions/{PORT}"))

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

       RequestUri = new Uri("http://127.0.0.1:22999/api/refresh_sessions/{PORT}")

      };

      var response = await client.SendAsync(requestMessage);

      var responseString = await response.Content.ReadAsStringAsync();

      Console.WriteLine(responseString);

    }

  }
  ```

  ```python Python theme={null}
  #!/usr/bin/env python


  import requests



  r = requests.get('http://127.0.0.1:22999/api/refresh_sessions/{PORT}')

  print(r.content)
  ```
</RequestExample>
