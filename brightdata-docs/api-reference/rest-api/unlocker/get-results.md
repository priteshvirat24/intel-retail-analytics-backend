> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Unlocker async response

> Use the Bright Data Web Unlocker API (98% success rate) async endpoint. GET /unblocker/get_result submits or retrieves a queued unlock request as JSON.



## OpenAPI

````yaml async-api-reference GET /unblocker/get_result
openapi: 3.1.0
info:
  title: Bright Data Unblocker and SERP API (Async)
  description: API for asynchronous web data collection using Unblocker and SERP engines.
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security:
  - bearerAuth: []
paths:
  /unblocker/get_result:
    get:
      parameters:
        - in: query
          name: response_id
          description: >-
            Defines the job id. Received in the response headers of your initial
            [async
            request](https://docs.brightdata.com/api-reference/rest-api/unlocker/request).
          required: true
          schema:
            type: string
          example: s4t7w3619285042ra9dke1m8qx
        - in: query
          name: zone
          description: The name of your Bright Data Unlocker zone.
          schema:
            type: string
          example: web_unlocker1
        - in: query
          name: customer
          description: Your Bright Data account ID.
          schema:
            type: string
          example: hl_xxxxxxxx
      responses:
        '200':
          description: OK
          content:
            application/json:
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

                  [USERNAME]-ip-1.1.1.1.1:[PASSWORD]  // proxy from dedicated
                  pool


                  To get a simple JSON response, use
                  https://geo.brdtest.com/mygeo.json .


                  More examples on
                  https://docs.brightdata.com/api-reference/introduction

        '202':
          description: Accepted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RequestPending'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Unauthorized'
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/NotFound'
      x-codeSamples:
        - lang: shell
          label: cURL
          source: |-
            # Wait ~20s before the first poll, 10s before the second, then 5s.
            # HTTP 202 means the job is still running; 200 returns the result.
            curl --request GET \
              --url "https://api.brightdata.com/unblocker/get_result?response_id=YOUR_RESPONSE_ID" \
              --header "Authorization: Bearer YOUR_API_KEY"
        - lang: python
          label: Python
          source: |-
            import time
            import requests

            url = "https://api.brightdata.com/unblocker/get_result"
            headers = {"Authorization": "Bearer YOUR_API_KEY"}
            params = {"response_id": "YOUR_RESPONSE_ID"}

            # Wait ~20s before the first poll, 10s before the second, then 5s.
            for delay in [20, 10] + [5] * 20:
                time.sleep(delay)
                response = requests.get(url, params=params, headers=headers)
                if response.status_code == 202:
                    continue  # still processing
                response.raise_for_status()
                print(response.json())
                break
            else:
                raise TimeoutError("Result was not ready in time")
        - lang: javascript
          label: JavaScript
          source: |-
            const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

            // Wait ~20s before the first poll, 10s before the second, then 5s.
            const delays = [20_000, 10_000, ...Array(20).fill(5_000)];

            for (const delay of delays) {
              await sleep(delay);

              const response = await fetch(
                "https://api.brightdata.com/unblocker/get_result?response_id=YOUR_RESPONSE_ID",
                { headers: { "Authorization": "Bearer YOUR_API_KEY" } },
              );

              if (response.status === 202) continue; // still processing

              console.log(await response.json());
              break;
            }
        - lang: go
          label: Go
          source: "package main\n\nimport (\n\t\"fmt\"\n\t\"io\"\n\t\"net/http\"\n\t\"time\"\n)\n\nfunc main() {\n\turl := \"https://api.brightdata.com/unblocker/get_result?response_id=YOUR_RESPONSE_ID\"\n\n\t// Wait ~20s before the first poll, 10s before the second, then 5s.\n\tdelays := append([]time.Duration{20 * time.Second, 10 * time.Second},\n\t\tmake([]time.Duration, 20)...)\n\tfor i := 2; i < len(delays); i++ {\n\t\tdelays[i] = 5 * time.Second\n\t}\n\n\tfor _, d := range delays {\n\t\ttime.Sleep(d)\n\n\t\treq, _ := http.NewRequest(\"GET\", url, nil)\n\t\treq.Header.Set(\"Authorization\", \"Bearer YOUR_API_KEY\")\n\n\t\tres, err := http.DefaultClient.Do(req)\n\t\tif err != nil {\n\t\t\tpanic(err)\n\t\t}\n\n\t\tif res.StatusCode == http.StatusAccepted { // still processing\n\t\t\tres.Body.Close()\n\t\t\tcontinue\n\t\t}\n\n\t\tbody, _ := io.ReadAll(res.Body)\n\t\tres.Body.Close()\n\t\tfmt.Println(string(body))\n\t\treturn\n\t}\n\n\tpanic(\"result was not ready in time\")\n}"
components:
  schemas:
    RequestPending:
      type: string
      example: Request is pending
    Unauthorized:
      type: string
      example: Invalid token
    NotFound:
      type: string
      example: Result not found
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        Use your Bright Data API Key as a Bearer token in the Authorization
        header.


        **How to authenticate:**

        1. Obtain your API Key from the [Bright Data account
        settings](https://brightdata.com/cp/setting/users)

        2. Include the API Key in the Authorization header of your requests

        3. Format: `Authorization: Bearer YOUR_API_KEY`


        **Example:**

        ```

        Authorization: Bearer b5648e1096c6442f60a6c4bbbe73f8d2234d3d8324554bd...

        ```


        > [Learn how to get your Bright Data API
        key](https://docs.brightdata.com/api-reference/authentication)
      bearerFormat: API Key

````