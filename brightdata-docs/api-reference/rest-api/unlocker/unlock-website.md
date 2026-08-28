> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Web Unlocker API

> Use the Bright Data Web Unlocker API (98% success rate) to test and unlock websites in real time, bypassing anti-bot protections, proxies and CAPTCHAs.

Related guide: [Web Unlocker API Introduction](/scraping-automation/web-unlocker/introduction)

<a href="https://www.postman.com/bright-data-api/bright-data-api/request/f0g939o/unlock-website" target="_blank">
  <img alt="Run in Postman" height="32" width="128" noZoom src="https://run.pstmn.io/button.svg" />
</a>

<Card title="Bright Data Python SDK" icon="python" href="/api-reference/SDK" cta="Get Started">
  For an easy start using our tools check out our new Python SDK.
</Card>


## OpenAPI

````yaml api-reference/unlocker-rest-api POST /request
openapi: 3.0.1
info:
  title: Brightdata API
  description: >-
    Integrate Bright Data APIs to your pipeline and secure high-end scraping
    precision
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security:
  - bearerAuth: []
paths:
  /request:
    post:
      parameters:
        - in: query
          name: async
          description: Set this to `true` for asynchronous
          required: false
          schema:
            type: boolean
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PostBody'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessfulUnlockerResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTP400'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTP401'
      x-codeSamples:
        - lang: shell
          label: cURL
          source: |-
            curl --request POST \
              --url https://api.brightdata.com/request \
              --header "Authorization: Bearer YOUR_API_KEY" \
              --header "Content-Type: application/json" \
              --data '{
                "zone": "web_unlocker1",
                "url": "https://geo.brdtest.com/welcome.txt",
                "format": "raw"
              }' 
        - lang: python
          label: Python
          source: |-
            import requests

            url = "https://api.brightdata.com/request"
            headers = {
                "Authorization": "Bearer YOUR_API_KEY",
                "Content-Type": "application/json",
            }
            payload = {
                "zone": "web_unlocker1",
                "url": "https://geo.brdtest.com/welcome.txt",
                "format": "raw",
            }

            response = requests.post(url, headers=headers, json=payload)
            print(response.text)
        - lang: py
          label: Python SDK
          source: |-
            # Install: pip install brightdata-sdk
            from brightdata import BrightDataClient

            async with BrightDataClient(api_key="YOUR_API_KEY") as client:
                # Returns HTML by default
                result = await client.scrape_url("https://geo.brdtest.com/welcome.txt")

                # Or transform to markdown and route through a US proxy
                md = await client.scrape_url(
                    "https://geo.brdtest.com/welcome.txt",
                    data_format="markdown",
                    country="us",
                )

                print(result.data)
        - lang: javascript
          label: JavaScript
          source: |-
            const response = await fetch("https://api.brightdata.com/request", {
              method: "POST",
              headers: {
                "Authorization": "Bearer YOUR_API_KEY",
                "Content-Type": "application/json",
              },
              body: JSON.stringify({
                zone: "web_unlocker1",
                url: "https://geo.brdtest.com/welcome.txt",
                format: "raw",
              }),
            });

            const data = await response.text();
            console.log(data);
        - lang: js
          label: JavaScript SDK
          source: >-
            // Install: npm install @brightdata/sdk

            import { bdclient } from '@brightdata/sdk';


            const client = new bdclient({ apiKey: 'YOUR_API_KEY' });


            // Returns HTML by default

            const html = await
            client.scrapeUrl('https://geo.brdtest.com/welcome.txt');


            // Or transform to markdown and route through a US proxy

            const md = await
            client.scrapeUrl('https://geo.brdtest.com/welcome.txt', {
              dataFormat: 'markdown',
              country: 'us',
            });


            await client.close();
        - lang: php
          label: PHP
          source: |-
            <?php
            $ch = curl_init("https://api.brightdata.com/request");
            curl_setopt($ch, CURLOPT_POST, true);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            curl_setopt($ch, CURLOPT_HTTPHEADER, [
                "Authorization: Bearer YOUR_API_KEY",
                "Content-Type: application/json",
            ]);
            curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode([
                "zone"   => "web_unlocker1",
                "url"    => "https://geo.brdtest.com/welcome.txt",
                "format" => "raw",
            ]));

            $response = curl_exec($ch);
            curl_close($ch);
            echo $response;
        - lang: go
          label: Go
          source: "package main\n\nimport (\n\t\"bytes\"\n\t\"fmt\"\n\t\"io\"\n\t\"net/http\"\n)\n\nfunc main() {\n\tpayload := []byte(`{\"zone\":\"web_unlocker1\",\"url\":\"https://geo.brdtest.com/welcome.txt\",\"format\":\"raw\"}`)\n\n\treq, _ := http.NewRequest(\"POST\", \"https://api.brightdata.com/request\", bytes.NewBuffer(payload))\n\treq.Header.Set(\"Authorization\", \"Bearer YOUR_API_KEY\")\n\treq.Header.Set(\"Content-Type\", \"application/json\")\n\n\tres, err := http.DefaultClient.Do(req)\n\tif err != nil {\n\t\tpanic(err)\n\t}\n\tdefer res.Body.Close()\n\n\tbody, _ := io.ReadAll(res.Body)\n\tfmt.Println(string(body))\n}"
        - lang: java
          label: Java
          source: |-
            import java.net.URI;
            import java.net.http.HttpClient;
            import java.net.http.HttpRequest;
            import java.net.http.HttpResponse;

            public class UnlockerRequest {
                public static void main(String[] args) throws Exception {
                    String body = "{\"zone\":\"web_unlocker1\",\"url\":\"https://geo.brdtest.com/welcome.txt\",\"format\":\"raw\"}";

                    HttpRequest request = HttpRequest.newBuilder()
                        .uri(URI.create("https://api.brightdata.com/request"))
                        .header("Authorization", "Bearer YOUR_API_KEY")
                        .header("Content-Type", "application/json")
                        .POST(HttpRequest.BodyPublishers.ofString(body))
                        .build();

                    HttpResponse<String> response = HttpClient.newHttpClient()
                        .send(request, HttpResponse.BodyHandlers.ofString());

                    System.out.println(response.body());
                }
            }
        - lang: ruby
          label: Ruby
          source: >-
            require 'net/http'

            require 'json'

            require 'uri'


            uri = URI.parse("https://api.brightdata.com/request")

            request = Net::HTTP::Post.new(uri)

            request["Authorization"] = "Bearer YOUR_API_KEY"

            request["Content-Type"] = "application/json"

            request.body = {
              zone: "web_unlocker1",
              url: "https://geo.brdtest.com/welcome.txt",
              format: "raw"
            }.to_json


            response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) do
            |http|
              http.request(request)
            end


            puts response.body
components:
  schemas:
    PostBody:
      required:
        - zone
        - url
        - format
      type: object
      properties:
        zone:
          description: >-
            Zone identifier that defines your Bright Data product configuration.
            Each zone contains targeting rules, output preferences, and access
            permissions. 
             Manage zones at: https://brightdata.com/cp/zones
          type: string
          example: web_unlocker1
        url:
          description: >-
            Complete target URL to scrape. Must include protocol (http/https),
            be publicly accessible.
          type: string
          example: https://geo.brdtest.com/welcome.txt
        format:
          description: >-
            Response format: `raw` returns HTML content as string, `json`
            returns structured data.
          type: string
          enum:
            - raw
            - json
          example: json
        method:
          description: Method for requesting an HTML via proxy is `GET`.
          type: string
          default: GET
          example: GET
        country:
          description: >-
            Two-letter ISO 3166-1 country code for proxy location (e.g., `us`,
            `gb`, `de`, `ca`, `au`). If not specified, system auto-selects
            optimal location based on your zone configuration. 
             List of country codes: https://docs.brightdata.com/general/faqs#where-can-i-see-the-list-of-country-codes
          type: string
          example: us
        data_format:
          description: >-
            Additional response format transformation: `markdown` converts HTML
            content to clean markdown format, `screenshot` captures a PNG image
            of the rendered page.
          type: string
          enum:
            - markdown
            - screenshot
          example: markdown
        render:
          description: >-
            Set to `true` to force JavaScript rendering using a browser. Because
            this flag forces browser use, it can significantly increase response
            time, so use it only when a page requires JavaScript to load its
            content.
          type: string
          enum:
            - 'true'
            - 'false'
          example: 'true'
        debug:
          description: >-
            Set to `true` to return the `x-brd-debug` response header, which
            reports the request ID, traffic counters, billing status,
            destination IP and peer details for this request. See [Debugging Web
            Unlocker
            API](https://docs.brightdata.com/scraping-automation/web-unlocker/features#debugging-web-unlocker-api).
          type: boolean
          default: false
          example: true
    SuccessfulUnlockerResponse:
      type: object
      example:
        status_code: 200
        headers:
          access-control-allow-origin: '*'
          cache-control: no-store
          content-type: text/plain; charset=utf-8
          date: Sun, 18 May 2025 20:01:18 GMT
          server: nginx
          connection: close
          transfer-encoding: chunked
        body: >+

          Welcome to Bright Data! Here are your proxy details

          Country: US

          Latitude: 37.751

          Longitude: -97.822

          Timezone: America/Chicago

          ASN number: 20473

          ASN Organization name: AS-VULTR

          IP version: IPv4


          Common usage examples:


          [USERNAME]-country-us:[PASSWORD]  // US based Proxy

          [USERNAME]-country-us-state-ny:[PASSWORD]  // US proxy from NY

          [USERNAME]-asn-56386:[PASSWORD]  // proxy from ASN 56386

          [USERNAME]-ip-1.1.1.1.1:[PASSWORD]  // proxy from dedicated pool


          To get a simple JSON response, use https://geo.brdtest.com/mygeo.json
          .


          More examples on
          https://docs.brightdata.com/api-reference/introduction

    HTTP400:
      type: object
      example:
        error: Bad Request
    HTTP401:
      type: object
      example:
        error: User authentication is required
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        Use your Bright Data API Key as a Bearer token in the Authorization
        header.


        **How to authenticate:**

        1. Obtain your API Key from the Bright Data account settings at
        https://brightdata.com/cp/setting/users

        2. Include the API Key in the Authorization header of your requests

        3. Format: `Authorization: Bearer YOUR_API_KEY`


        **Example:**

        ```

        Authorization: Bearer
        b5648e1096c6442f60a6c4bbbe73f8d2234d3d8324554bd6a7ec8f3f251f07df

        ```


        Learn how to get your Bright Data API key:
        https://docs.brightdata.com/api-reference/authentication
      bearerFormat: API Key

````