> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 禁止IP（所有端口）

> 使用Bright Data代理管理器API来禁止IP（所有端口）。在本地代理管理器端口22999上调用POST /api/banip。

API 端点: `POST` `/api/banip`

## `POST` 请求体

<ParamField body="ip" type="string" required>
  要封禁的 IP。例如 `1.2.1.2`
</ParamField>

<ParamField body="domain" type="string">
  封禁该 IP 向指定域名发送请求
</ParamField>

<ParamField body="ms" type="integer">
  封禁该 IP 的持续时间（毫秒）
</ParamField>

<RequestExample>
  ```sh Shell theme={null}
  curl "http://127.0.0.1:22999/api/banip" -H "Content-Type: application/json" -d '{"ip":"1.2.1.2","domain":"example.com","ms":60000}'
  ```

  ```js NodeJS theme={null}
  #!/usr/bin/env node

  (async () => {
    const response = await fetch('http://127.0.0.1:22999/api/banip', {
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

  import org.apache.http.client.fluent.\*;

   

  public class Example {

   public static void main(String[] args) throws Exception {

    String body = "{\"ip\":\"1.2.1.2\",\"domain\":\"example.com\",\"ms\":60000}";

    String res = Executor.newInstance()

     .execute(Request.Post("http://127.0.0.1:22999/api/banip")

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

     RequestUri = new Uri("http://127.0.0.1:22999/api/banip"),

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
  r = requests.post('http://127.0.0.1:22999/api/banip', data=json.dumps(data))

  print(r.content)
  ```
</RequestExample>
