> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get HAR logs

> Use the Bright Data Proxy Manager API to get HAR Logs. Updates the local Proxy Manager (default port 22999) configuration and returns a JSON status.

API endpoint: `GET` `/api/logs`

<ParamField query="limit" type="integar">
  Number of logs to get from tail
</ParamField>

<ParamField query="skip" type="integar">
  Number of logs to get from tail
</ParamField>

<ParamField query="limit" type="integar">
  Maximum number of requests to be fetched
</ParamField>

<ParamField query="search" type="string">
  regex search query for the URL
</ParamField>

<ParamField query="port_from" type="string">
  lower bound for port number
</ParamField>

<ParamField query="port_to" type="string">
  upper bound for port number
</ParamField>

<ParamField query="status_code" type="string">
  filter requests by status code
</ParamField>

<ParamField query="sort" type="string">
  parameter to be sorted by
</ParamField>

<ParamField query="sort_desc" type="boolean">
  is descending sorting direction
</ParamField>

<RequestExample>
  ```sh Shell theme={null}
  curl "http://127.0.0.1:22999/api/logs"
  ```

  ```js NodeJS theme={null}
  #!/usr/bin/env node

  (async () => {
    const response = await fetch('http://127.0.0.1:22999/api/logs');
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
       .execute(Request.Get("http://127.0.0.1:22999/api/logs"))
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

       RequestUri = new Uri("http://127.0.0.1:22999/api/logs")

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

   

  r = requests.get('http://127.0.0.1:22999/api/logs')

  print(r.content)
  ```
</RequestExample>
