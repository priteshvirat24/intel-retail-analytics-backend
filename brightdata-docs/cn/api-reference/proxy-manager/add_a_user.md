> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 添加用户

**API 端点:** `POST` `/api/lpm_user`

## `POST` 正文

<ParamField body="电子邮件" type="字符串" 必填项>
  要添加的用户电子邮件地址
</ParamField>

<RequestExample>
  ```sh Shell theme={null}
  curl "http://127.0.0.1:22999/api/lpm_user" -H "Content-Type: application/json" -d '{"email":"test@example.com"}'
  ```

  ```js NodeJS theme={null}
  #!/usr/bin/env node
  require('request-promise')({
      method: 'POST',
      url: 'http://127.0.0.1:22999/api/lpm_user',
      json: {'email':'test@example.com'}

  }).then(function(data){ console.log(data); },

  function(err){ console.error(err); });
  ```

  ```java Java theme={null}
  package example;
  import org.apache.http.HttpHost;
  import org.apache.http.client.fluent.*;


  public class Example {
   public static void main(String[] args) throws Exception {

   String body = "{\"email\":\"test@example.com\"}";

   String res = Executor.newInstance()
   .execute(Request.Post("http://127.0.0.1:22999/api/lpm_user")
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

   RequestUri = new Uri("http://127.0.0.1:22999/api/lpm_user"),

   Content = new StringContent(JsonConvert.SerializeObject(new {

   email = "test@example.com"

   }), Encoding.UTF8, "application/json"))

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

  data = {'email':'test@example.com'}
  r = requests.post('http://127.0.0.1:22999/api/lpm_user', data=json.dumps(data))

  print(r.content)
  ```
</RequestExample>
