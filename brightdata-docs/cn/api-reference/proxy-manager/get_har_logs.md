> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 获取 HAR 日志

> 使用 Bright Data 代理管理器 API 获取 HAR 日志。更新本地代理管理器（默认端口 22999）配置并返回 JSON 状态。

**API 端点:** `GET` `/api/logs`

<ParamField query="limit" type="integar">
  从尾部获取的日志数量
</ParamField>

<ParamField query="skip" type="integar">
  从尾部跳过的日志数量
</ParamField>

<ParamField query="limit" type="integar">
  要获取的最大请求数
</ParamField>

<ParamField query="search" type="string">
  URL 的正则表达式搜索查询
</ParamField>

<ParamField query="port_from" type="string">
  端口号的下界
</ParamField>

<ParamField query="port_to" type="string">
  端口号的上界
</ParamField>

<ParamField query="status_code" type="string">
  按状态码筛选请求
</ParamField>

<ParamField query="sort" type="string">
  要排序的参数
</ParamField>

<ParamField query="sort_desc" type="boolean">
  是否按降序排序
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
