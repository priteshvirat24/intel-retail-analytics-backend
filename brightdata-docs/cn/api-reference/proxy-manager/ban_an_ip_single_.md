> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 禁用IP

> 使用Bright Data代理管理器API来封禁IP。在本地代理管理器端口22999上调用POST /api/proxies/{PORT}/banip。

**API 端点:** `POST` `/api/proxies/{PORT}/banip`

## 路径参数

<ParamField body="PORT" type="string" required>
  现有代理端口号
</ParamField>

## `POST` 请求体

<ParamField body="ip" type="string" required>
  要封禁的IP。例如 `1.2.1.2`
</ParamField>

<ParamField body="domain" type="string">
  为指定域名的请求封禁该IP
</ParamField>

<ParamField body="ms" type="integer">
  将IP封禁指定的毫秒数
</ParamField>

<RequestExample>
  ```sh Shell theme={null}
  curl "http://127.0.0.1:22999/api/proxies/{PORT}/banip" -H "Content-Type: application/json" -d '{"ip":"1.2.1.2","domain":"example.com","ms":60000}'
  ```

  ```js NodeJS theme={null}
  #!/usr/bin/env node

  (async () => {
    const response = await fetch('http://127.0.0.1:22999/api/proxies/{PORT}/banip', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({'ip':'1.2.1.2','domain':'example.com','ms':60000}),
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
     String body = "{\"ip\":\"1.2.1.2\",\"domain\":\"example.com\",\"ms\":60000}";
      String res = Executor.newInstance()
       .execute(Request.Post("http://127.0.0.1:22999/api/proxies/{PORT}/banip")
       .bodyString(body, ContentType.APPLICATION_JSON))
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
       RequestUri = new Uri("http://127.0.0.1:22999/api/proxies/{PORT}/banip"),
       Content = new StringContent(JsonConvert.SerializeObject(new {
         ip = "1.2.1.2",
         domain = "example.com",
         ms = 60000
       }), Encoding.UTF8, "application/json")
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
  import json


  data = {'ip':'1.2.1.2','domain':'example.com','ms':60000}
  r = requests.post('http://127.0.0.1:22999/api/proxies/{PORT}/banip', data=json.dumps(data))

  print(r.content)
  ```
</RequestExample>
