> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a proxy port

> Use the Bright Data Proxy Manager API to update a Proxy Port. Calls PUT /api/proxies/{PORT} on the local Proxy Manager port 22999.

**API endpoint:** `PUT` `/api/proxies/{PORT}`

## Path Parameter

<ParamField path="PORT" type="string" required>
  Existing proxy port number
</ParamField>

## `PUT` body

<ParamField body="proxy" type="User Object">
  <Expandable title="properties">
    <ParamField body="port" type="integer">
      Port for the HTTP proxy
    </ParamField>

    <ParamField body="proxy_type" type="string">
      Set to `persist` to save proxy into the configuration file.
    </ParamField>

    <ParamField body="multiply" type="integer">
      Multiply the port definition given number of times
    </ParamField>

    <ParamField body="multiply_users" type="boolean" />

    <ParamField body="users" type="array">
      List of `user`s `[string]`. This option has to be used along with `multiply_users`
    </ParamField>

    <ParamField body="ssl" type="boolean">
      Enable SSL analyzing
    </ParamField>

    <ParamField body="tls_lib" type="string">
      Choose the SSL library

      | value      | description      |
      | ---------- | ---------------- |
      | `open_ssl` | Open SSL Library |
      | `flex_tls` | Flex TLS Library |
    </ParamField>

    <ParamField body="iface" type="string">
      Interface or IP to listen on
    </ParamField>

    <ParamField body="customer" type="string">
      Customer name
    </ParamField>

    <ParamField body="zone" type="string">
      Zone name
    </ParamField>

    <ParamField body="password" type="string">
      Zone password
    </ParamField>

    <ParamField body="proxy" type="string">
      Hostname or IP of super proxy
    </ParamField>

    <ParamField body="proxy_port" type="integer">
      Super proxy port
    </ParamField>

    <ParamField body="proxy_connection_type" type="string">
      Determines what kind of connection will be used between Proxy Manager and Super Proxy

      |         |   |
      | ------- | - |
      | `http`  |   |
      | `https` |   |
      | `socks` |   |
    </ParamField>

    <ParamField body="proxy_retry" type="integer">
      Automatically retry on super proxy failure
    </ParamField>

    <ParamField body="insecure" type="boolean">
      Enable SSL connection/analyzing to insecure hosts
    </ParamField>

    <ParamField body="country" type="string">
      Country
    </ParamField>

    <ParamField body="state" type="string">
      State
    </ParamField>

    <ParamField body="city" type="string">
      City
    </ParamField>

    <ParamField body="asn" type="string">
      ASN
    </ParamField>

    <ParamField body="ip" type="string">
      Data Center IP
    </ParamField>

    <ParamField body="vip" type="integer">
      gIP
    </ParamField>

    <ParamField body="ext_proxies" type="array">
      A list of proxies from external vendors. Format: \[username:password@]ip\[:port]

      * proxy\[string]
    </ParamField>

    <ParamField body="ext_proxy_username" type="string">
      Default username for external vendor ips
    </ParamField>

    <ParamField body="ext_proxy_password" type="string">
      Default password for external vendor ips
    </ParamField>

    <ParamField body="ext_proxy_port" type="integer">
      Default port for external vendor ips
    </ParamField>

    <ParamField body="dns" type="string">
      DNS resolving

      |          |   |
      | -------- | - |
      | `local`  |   |
      | `remote` |   |
    </ParamField>

    <ParamField body="reverse_lookup_dns" type="boolean">
      Process reverse lookup via DNS
    </ParamField>

    <ParamField body="reverse_lookup_file" type="string">
      Process reverse lookup via file
    </ParamField>

    <ParamField body="reverse_lookup_values" type="array">
      Process reverse lookup via value
    </ParamField>

    <ParamField body="session" type="string">
      Session for all proxy requests
    </ParamField>

    <ParamField body="sticky_ip" type="boolean">
      Use session per requesting host to maintain IP per host
    </ParamField>

    <ParamField body="pool_size" type="integer" />

    <ParamField body="rotate_session" type="boolean">
      Session pool size
    </ParamField>

    <ParamField body="throttle" type="integer">
      Throttle requests above given number
    </ParamField>

    <ParamField body="rules" type="array">
      Proxy request rules
    </ParamField>

    <ParamField body="route_err" type="string">
      Block or allow requests to be automatically sent through super proxy on error
    </ParamField>

    <ParamField body="smtp" type="array" />

    <ParamField body="override_headers" type="string" />

    <ParamField body="os" type="string">
      Operating System of the Peer IP
    </ParamField>

    <ParamField body="headers" type="array">
      Request headers
    </ParamField>

    * name\[string]
    * value\[string]

    <ParamField body="debug" type="string">
      Request debug info

      |        |   |
      | ------ | - |
      | `full` |   |
      | `none` |   |
    </ParamField>

    <ParamField body="lpm_auth" type="string">
      x-lpm-authorization header
    </ParamField>

    <ParamField body="const" type="boolean" />

    <ParamField body="socket_inactivity_timeout" type="integer" />

    <ParamField body="multiply_ips" type="boolean" />

    <ParamField body="multiply_vips" type="boolean" />

    <ParamField body="max_ban_retries" type="integer" />

    <ParamField body="preset" type="string" />

    <ParamField body="ua" type="boolean">
      Unblocker Mobile UA
    </ParamField>

    <ParamField body="timezone" type="string">
      Timezone ID to be used by the browser
    </ParamField>

    <ParamField body="resolution" type="string">
      Browser screen size
    </ParamField>

    <ParamField body="webrtc" type="string">
      WebRTC plugin behavior in the browser
    </ParamField>

    <ParamField body="bw_limit" type="object">
      BW limit params

      * days \[integer]
      * bytes \[integer]
      * renewable\[boolean] - Renew limit of bytes each period or use single period and stop usage once last day of period is reached. Default is true
    </ParamField>
  </Expandable>
</ParamField>

<ResponseExample>
  ```JSON Sample Response theme={null}
  {
      "port":24000,
      "zone":"ZONE",
      "proxy_type":"persist",
      "customer":"CUSTOMER",
      "password":"password",
      "whitelist_ips":[]
  }
  ```
</ResponseExample>

<RequestExample>
  ```sh Shell theme={null}
  curl -X PUT "http://127.0.0.1:22999/api/proxies/{PORT}" -H "Content-Type: application/json" -d '{"proxy":{"port":24000,"zone":"ZONE","proxy_type":"persist","customer":"CUSTOMER","password":"password","whitelist_ips":[]}}'
  ```

  ```js NodeJS theme={null}
  #!/usr/bin/env node

  (async () => {
    const response = await fetch('http://127.0.0.1:22999/api/proxies/{PORT}', {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({'proxy':{'port':24000,'zone': 'ZONE','proxy_type':'persist','customer':'CUSTOMER','password':'password','whitelist_ips':[]}}),
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

     String body = "{\"proxy\":{\"port\":24000,\"zone\":\"ZONE\",\"proxy_type\":\"persist\",\"customer\":\"CUSTOMER\",\"password\":\"password\",\"whitelist_ips\":[]}}";

      String res = Executor.newInstance()

       .execute(Request.Put("http://127.0.0.1:22999/api/proxies/{PORT}")

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
       RequestUri = new Uri("http://127.0.0.1:22999/api/proxies/{PORT}"),
       Content = new StringContent(JsonConvert.SerializeObject(new {
         proxy = new {
           port = 24000, zone = "ZONE", proxy_type = "persist", customer = "CUSTOMER", password = "password", whitelist_ips = []
         }
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

  import requests
  import json


  data = {'proxy':{'port':24000,'zone': 'ZONE','proxy_type':'persist','customer':'CUSTOMER','password':'password','whitelist_ips':[]}}

  r = requests.put('http://127.0.0.1:22999/api/proxies/{PORT}', data=json.dumps(data))

  print(r.content)
  ```
</RequestExample>
