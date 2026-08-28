> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 升级代理管理器

> 使用Bright Data代理管理器API升级代理管理器。在本地代理管理器端口22999上调用POST /api/upgrade。

**API 端点:** `POST` `/api/upgrade`

<RequestExample>
  ```sh Shell theme={null}
  curl -X POST "http://127.0.0.1:22999/api/upgrade"
  ```

  ```js NodeJS theme={null}
  #!/usr/bin/env node

  (async () => {
    const response = await fetch('http://127.0.0.1:22999/api/upgrade', {
      method: 'POST',

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

       .execute(Request.Post("http://127.0.0.1:22999/api/upgrade"))

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

        Method = HttpMethod.Post,

       RequestUri = new Uri("http://127.0.0.1:22999/api/upgrade")

      };

      var response = await client.SendAsync(requestMessage);

      var responseString = await response.Content.ReadAsStringAsync();

      Console.WriteLine(responseString);

    }

  }
  ```

  ```python Python theme={null}
  #!/usr/bin/env python

  print('如果您收到错误消息 "ImportError: No module named requests",请安装它:\n$ sudo pip install requests');

  import requests


  r = requests.post('http://127.0.0.1:22999/api/upgrade')

  print(r.content)
  ```
</RequestExample>
