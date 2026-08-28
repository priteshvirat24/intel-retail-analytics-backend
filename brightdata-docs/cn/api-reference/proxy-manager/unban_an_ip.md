> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 解除IP封禁

> 使用Bright Data代理管理器API解除IP封禁。在本地代理管理器端口22999上调用POST /api/proxies/{PORT}/unbanip。

**API 端点:** `POST` `/api/proxies/{PORT}/unbanip`

## 路径参数

<ParamField path="PORT" type="string" required>
  现有代理端口号
</ParamField>

## `POST` 请求体

<ParamField body="ip" type="string" required>
  要解禁的 IP。例如 `ip="1.2.1.2"`
</ParamField>

<ParamField body="domain" type="string">
  解禁该 IP 对指定域名的请求。
</ParamField>

<RequestExample>
  ```sh Shell theme={null}
  curl "http://127.0.0.1:22999/api/proxies/{PORT}/unbanip" -H "Content-Type: application/json" -d '{"ip":"1.2.1.2","domain":"example.com"}'
  ```

  ```js NodeJS theme={null}
  #!/usr/bin/env node

  (async () => {
    const response = await fetch('http://127.0.0.1:22999/api/proxies/{PORT}/unbanip', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
            'ip': '1.2.1.2',
            'domain': 'example.com'
        }),

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

     String body = "{\"ip\":\"1.2.1.2\",\"domain\":\"example.com\"}";

      String res = Executor.newInstance()

       .execute(Request.Post("http://127.0.0.1:22999/api/proxies/{PORT}/unbanip")

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

       RequestUri = new Uri("http://127.0.0.1:22999/api/proxies/{PORT}/unbanip"),

       Content = new StringContent(JsonConvert.SerializeObject(new {

         ip = "1.2.1.2",

         domain = "example.com"

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

   

  data = {'ip':'1.2.1.2','domain':'example.com'}

  r = requests.post('http://127.0.0.1:22999/api/proxies/{PORT}/unbanip', data=json.dumps(data))

  print(r.content)
  ```
</RequestExample>
