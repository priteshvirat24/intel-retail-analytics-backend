> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 获取区域中分配的IP

> 使用 Bright Data 代理管理器 API 获取区域中已分配的 IP。在本地代理管理器端口 22999 上调用 GET /api/allocated_ips。

**API 端点:** `GET` `/api/allocated_ips`

## 查询参数

<ParamField query="zone" type="string">
  静态（数据中心/ISP）区域名称
</ParamField>

<ResponseExample>
  ```JSON 示例响应 theme={null}
  {
      "ips": [
          "10.0.0.1",
          "20.0.0.1"
      ]
  }
  ```
</ResponseExample>

<RequestExample>
  ```sh Shell theme={null}
  curl "http://127.0.0.1:22999/api/allocated_ips?zone=ZONE"
  ```

  ```js NodeJS theme={null}
  #!/usr/bin/env node

  (async () => {
    const response = await fetch('http://127.0.0.1:22999/api/allocated_ips?zone=ZONE');
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

       .execute(Request.Get("http://127.0.0.1:22999/api/allocated_ips?zone=ZONE"))

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

       RequestUri = new Uri("http://127.0.0.1:22999/api/allocated_ips?zone=ZONE")

      };

      var response = await client.SendAsync(requestMessage);

      var responseString = await response.Content.ReadAsStringAsync();

      Console.WriteLine(responseString);

    }

  }

  ```

  ```python Python theme={null}
  #!/usr/bin/env python

  print('如果出现错误 "ImportError: No module named requests"，请安装它:\n$ sudo pip install requests');

  import requests


  r = requests.get('http://127.0.0.1:22999/api/allocated_ips?zone=ZONE')

  print(r.content)
  ```
</RequestExample>
