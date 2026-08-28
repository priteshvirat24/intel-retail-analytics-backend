> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 删除代理端口

> 使用Bright Data代理管理器API删除代理端口。在本地代理管理器端口22999上调用DELETE /api/proxies/{PORT}。

**API 端点:** `DELETE` `/api/proxies/{PORT}`

## 路径参数

<ParamField body="PORT" type="string" required>
  现有代理端口号
</ParamField>

<RequestExample>
  ```sh Shell theme={null}
  curl -X DELETE "http://127.0.0.1:22999/api/proxies/{PORT}"
  ```

  ```js NodeJS theme={null}
  #!/usr/bin/env node

  (async () => {
    const response = await fetch('http://127.0.0.1:22999/api/proxies/{PORT}', {
      method: 'DELETE',

    });
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

       .execute(Request.Delete("http://127.0.0.1:22999/api/proxies/{PORT}"))

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

        Method = HttpMethod.Delete,

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

  print('如果收到错误"ImportError: No module named requests"，请安装它：\n$ sudo pip install requests');

  import requests

  r = requests.delete('http://127.0.0.1:22999/api/proxies/{PORT}')

  print(r.content)

  ```
</RequestExample>
