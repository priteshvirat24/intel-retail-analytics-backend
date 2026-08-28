> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update general setting

> Use the Bright Data Proxy Manager API to update General Setting. Calls PUT /api/settings on the local Proxy Manager port 22999.

**API Endpoint:** `PUT` `/api/settings`

## `PUT` Body:

<ParamField body="zone" type="string">
  Default zone
</ParamField>

<ParamField body="www_whitelist_ips" type="array">
  Allowlist ip list for granting access to browser admin UI
</ParamField>

<ParamField body="whitelist_ips" type="array">
  Default for all proxies allowlist ip list for granting access to them
</ParamField>

<ParamField body="logs" type="integer">
  Number of request logs to store
</ParamField>

<ParamField body="request_stats" type="boolean">
  Enable requests statistics
</ParamField>

<ResponseExample>
  ```JSON Sample Response theme={null}
  {
      "customer":"CUSTOMER",
      "zone":"ZONE",
      "password":"password",
      "www_whitelist_ips":[],
      "whitelist_ips":[],
      "fixed_whitelist_ips":[],
      "read_only":false,
      "config":"/home/user/proxy_manager/.luminati.json",
      "test_url":"http://brdtest.com/myip.json",
      "logs":1000,
      "log":"notice",
      "har_limit":1024,
      "request_stats":true,
      "dropin":true,
      "pending_ips":[],
      "pending_www_ips":[],
      "zagent":false,
      "sync_config":true
  }
  ```
</ResponseExample>

<RequestExample>
  ```sh Shell theme={null}
  curl -X PUT "http://127.0.0.1:22999/api/settings" -H "Content-Type: application/json" -d '{"zone":"ZONE","www_whitelist_ips":[],"whitelist_ips":[],"logs":1000,"request_stats":true}'
  ```

  ```js NodeJS theme={null}
  #!/usr/bin/env node

  (async () => {
    const response = await fetch('http://127.0.0.1:22999/api/settings', {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({'zone': 'ZONE','www_whitelist_ips':[],'whitelist_ips':[],'logs':1000,'request_stats':true}),
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

     String body = "{\"zone\":\"ZONE\",\"www_whitelist_ips\":[],\"whitelist_ips\":[],\"logs\":1000,\"request_stats\":true}";

      String res = Executor.newInstance()

       .execute(Request.Put("http://127.0.0.1:22999/api/settings")

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

        Method = HttpMethod.Put,

       RequestUri = new Uri("http://127.0.0.1:22999/api/settings"),

       Content = new StringContent(JsonConvert.SerializeObject(new {

           zone = "ZONE", www_whitelist_ips = [], whitelist_ips = [], logs = 1000, request_stats = true

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

   

  data = {'zone': 'ZONE','www_whitelist_ips':[],'whitelist_ips':[],'logs':1000,'request_stats':True}

  r = requests.put('http://127.0.0.1:22999/api/settings', data=json.dumps(data))

  print(r.content)

  ```
</RequestExample>
