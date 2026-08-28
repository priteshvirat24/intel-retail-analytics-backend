> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 重启代理管理器

> 使用 Bright Data 代理管理器 API 重启代理管理器。在本地代理管理器端口 22999 上调用 POST /api/restart。

**API 端点：** `POST` `/api/restart`

<RequestExample>
  ```sh Shell theme={null}
  curl -X POST "http://127.0.0.1:22999/api/restart"
  ```

  ```js NodeJS theme={null}
  #!/usr/bin/env node

  (async () => {
    const response = await fetch('http://127.0.0.1:22999/api/restart', {
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

       .execute(Request.Post("http://127.0.0.1:22999/api/restart"))

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

       RequestUri = new Uri("http://127.0.0.1:22999/api/restart")

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


  r = requests.post('http://127.0.0.1:22999/api/restart')

  print(r.content)
  ```
</RequestExample>
