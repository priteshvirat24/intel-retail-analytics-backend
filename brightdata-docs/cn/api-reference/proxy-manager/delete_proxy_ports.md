> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 删除代理端口（多个）

> Bright Data代理管理器API端点，用于删除代理端口（多个）。端点：POST /api/proxies/delete，端口22999。

**API 端点:** `POST /api/proxies/delete`

## `POST` 请求体

<ParamField body="ports" type="array" required>
  端口数组
</ParamField>

<RequestExample>
  ```sh Shell theme={null}
  curl "http://127.0.0.1:22999/api/proxies/delete" -H "Content-Type: application/json" -d '{"ports":[24000,24001]}'
  ```

  ```js NodeJS theme={null}
  #!/usr/bin/env node

  (async () => {
    const response = await fetch('http://127.0.0.1:22999/api/proxies/delete', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({'ports':[24000,24001]}),
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

     String body = "{\"ports\":[24000,24001]}";

      String res = Executor.newInstance()

       .execute(Request.Post("http://127.0.0.1:22999/api/proxies/delete")

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

       RequestUri = new Uri("http://127.0.0.1:22999/api/proxies/delete"),

       Content = new StringContent(JsonConvert.SerializeObject(new {

         ports = [ 24000, 24001 ]

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


  data = {'ports':[24000,24001]}

  r = requests.post('http://127.0.0.1:22999/api/proxies/delete', data=json.dumps(data))

  print(r.content)
  ```
</RequestExample>
