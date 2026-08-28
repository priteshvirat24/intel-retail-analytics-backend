> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 获取区域中分配的gIP

> Bright Data代理管理器API端点用于获取区域中分配的gIP。端点：端口22999上的GET /api/allocated_vips。

**API 端点:** `GET` `/api/allocated_vips`

## 查询参数

<ParamField query="zone" type="string">
  住宅/移动专属区域名称
</ParamField>

<ResponseExample>
  ```json Sample Response theme={null}
  {
      "ips": [
          "gIP_1",
          "gIP_2"
      ]
  }
  ```
</ResponseExample>

<RequestExample>
  ```sh Shell theme={null}
  curl "http://127.0.0.1:22999/api/allocated_vips?zone=ZONE"
  ```

  ```js NodeJS theme={null}
  #!/usr/bin/env node

  (async () => {
    const response = await fetch('http://127.0.0.1:22999/api/allocated_vips?zone=ZONE');
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
       .execute(Request.Get("http://127.0.0.1:22999/api/allocated_vips?zone=ZONE"))
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
       RequestUri = new Uri("http://127.0.0.1:22999/api/allocated_vips?zone=ZONE")
      };

      var response = await client.SendAsync(requestMessage);
      var responseString = await response.Content.ReadAsStringAsync();

      Console.WriteLine(responseString);
    }
  }
  ```

  ```python Python theme={null}
  #!/usr/bin/env python

  print('If you get error "ImportError: No module named requests", please install it:\n$ sudo pip install requests');

  import requests

   

  r = requests.get('http://127.0.0.1:22999/api/allocated_vips?zone=ZONE')

  print(r.content)
  ```
</RequestExample>
