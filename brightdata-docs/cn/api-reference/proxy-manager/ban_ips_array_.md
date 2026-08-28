> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 禁止多个IP（数组）

> 使用 Bright Data 代理管理器 API 来禁止多个 IP 地址（数组）。端点：POST /api/proxies/{PORT}/banips，端口 22999。

**API 端点:** `POST` `/api/proxies/{PORT}/banips`

## 路径参数

<ParamField body="PORT" type="string" required>
  现有代理端口号
</ParamField>

## `POST` 请求体

<ParamField body="ips" type="array" required>
  要封禁的 IP 地址。例如 \["10.0.0.1","20.0.0.1"]
</ParamField>

<ParamField body="domain" type="string">
  针对发送到指定域名的请求封禁该 IP
</ParamField>

<ParamField body="ms" type="integer">
  封禁该 IP 的时长（毫秒）
</ParamField>

<RequestExample>
  ```sh Shell theme={null}
  curl "http://127.0.0.1:22999/api/proxies/{PORT}/banips" -H "Content-Type: application/json" -d '{"ips":["10.0.0.1","20.0.0.1"],"domain":"example.com","ms":60000}'
  ```

  ```js NodeJS theme={null}
  #!/usr/bin/env node
  (async () => {
    const response = await fetch('http://127.0.0.1:22999/api/proxies/{PORT}/banips', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({'ips':['10.0.0.1','20.0.0.1'],'domain':'example.com','ms':60000}),
    });
    const data = await response.text();
    console.log(data);
  })();
  ```

  ```java Java theme={null}
  package example;


  import org.apache.http.HttpHost;
  import org.apache.http.client.fluent.\*;


  public class Example {

    public static void main(String[] args) throws Exception {

      String body = "{\"ips\":[\"10.0.0.1\",\"20.0.0.1\"],\"domain\":\"example.com\",\"ms\":60000}";
      String res = Executor.newInstance()
          .execute(Request.Post("http://127.0.0.1:22999/api/proxies/{PORT}/banips")
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
       RequestUri = new Uri("http://127.0.0.1:22999/api/proxies/{PORT}/banips"),
       Content = new StringContent(JsonConvert.SerializeObject(new {
         ips = [ "10.0.0.1","20.0.0.1" ],
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


  data = {'ips':['10.0.0.1','20.0.0.1'],'domain':'example.com','ms':60000}
  r = requests.post('http://127.0.0.1:22999/api/proxies/{PORT}/banips', data=json.dumps(data))

  print(r.content)
  ```
</RequestExample>
