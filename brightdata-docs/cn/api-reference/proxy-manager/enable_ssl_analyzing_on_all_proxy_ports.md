> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 启用 SSL 分析（所有端口）

> Bright Data代理管理器API端点，用于启用SSL分析（所有端口）。端点：POST /api/enable_ssl，端口22999。

**API 端点：** `POST` `/api/enable_ssl`

<RequestExample>
  ```sh theme={null}
  curl -X POST "http://127.0.0.1:22999/api/enable_ssl"
  ```

  ```js NodeJS theme={null}
  #!/usr/bin/env node

  (async () => {
    const response = await fetch('http://127.0.0.1:22999/api/enable_ssl', {
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
       .execute(Request.Post("http://127.0.0.1:22999/api/enable_ssl"))
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
       RequestUri = new Uri("http://127.0.0.1:22999/api/enable_ssl")
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

  r = requests.post('http://127.0.0.1:22999/api/enable_ssl')

  print(r.content)
  ```
</RequestExample>
