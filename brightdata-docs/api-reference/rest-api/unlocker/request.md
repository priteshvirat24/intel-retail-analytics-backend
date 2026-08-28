> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Unlocker async request

> Use the Bright Data Web Unlocker API (98% success rate) async endpoint. POST /unblocker/req submits or retrieves a queued unlock request as JSON.



## OpenAPI

````yaml async-api-reference POST /unblocker/req
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
  /unblocker/req:
    post:
      parameters:
        - in: query
          name: zone
          description: The name of your Bright Data Unlocker zone.
          required: true
          schema:
            type: string
          example: web_unlocker1
        - in: query
          name: customer
          description: Your Bright Data account ID.
          schema:
            type: string
          example: hl_xxxxxxxx
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - url
              properties:
                url:
                  description: Defines the url of the request
                  type: string
                  format: uri
                  example: https://geo.brdtest.com/welcome.txt
                method:
                  description: Defines the HTTP method of the request
                  type: string
                headers:
                  description: Defines headers to be used in the request
                  type: object
                body:
                  description: >-
                    Defines body to be sent with request. If an object is
                    specified, it is serialized to JSON, and Content-Type header
                    is set to application/json.
                  oneOf:
                    - type: string
                      description: Raw request body as a string.
                    - type: object
                      description: Request body as a JSON object.
                country:
                  description: Defines country to be used for request (2-letters code)
                  type: string
                  example: US
                webhook_url:
                  description: >-
                    Defines the URL to which the job status notification will be
                    sent. If you don’t want to setup a default webhook or prefer
                    the URL to be different per request, use this.
                  type: string
                  format: uri
                webhook_method:
                  description: >-
                    Defines the HTTP method to use with the webhook_url (GET or
                    POST)
                  type: string
                webhook_data:
                  description: >-
                    Defines the data that will be sent with job status
                    notification
                debug:
                  description: >-
                    Set to `true` to return the `x-brd-debug` header. The header
                    is returned by `GET /unblocker/get_result` when you collect
                    the response, not on this submit call. See [Debugging Web
                    Unlocker
                    API](https://docs.brightdata.com/scraping-automation/web-unlocker/features#debugging-web-unlocker-api).
                  type: boolean
                  default: false
                  example: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/JobResponse'
      x-codeSamples:
        - lang: shell
          label: cURL
          source: |-
            curl --request POST \
              --url "https://api.brightdata.com/unblocker/req?zone=web_unlocker1" \
              --header "Authorization: Bearer YOUR_API_KEY" \
              --header "Content-Type: application/json" \
              --data '{
                "url": "https://geo.brdtest.com/welcome.txt"
              }'

            # => {"response_id":"s4t7w3619285042ra9dke1m8qx"}
            # Keep the response_id: you need it to collect the result.
        - lang: python
          label: Python
          source: |-
            import requests

            url = "https://api.brightdata.com/unblocker/req"
            headers = {
                "Authorization": "Bearer YOUR_API_KEY",
                "Content-Type": "application/json",
            }
            payload = {
                "url": "https://geo.brdtest.com/welcome.txt",
            }

            response = requests.post(url, params={"zone": "web_unlocker1"},
                                     headers=headers, json=payload)
            response.raise_for_status()

            # Keep the response_id: you need it to collect the result.
            response_id = response.json()["response_id"]
            print(response_id)
        - lang: javascript
          label: JavaScript
          source: |-
            const response = await fetch(
              "https://api.brightdata.com/unblocker/req?zone=web_unlocker1",
              {
                method: "POST",
                headers: {
                  "Authorization": "Bearer YOUR_API_KEY",
                  "Content-Type": "application/json",
                },
                body: JSON.stringify({
                  url: "https://geo.brdtest.com/welcome.txt",
                }),
              },
            );

            // Keep the response_id: you need it to collect the result.
            const { response_id } = await response.json();
            console.log(response_id);
        - lang: go
          label: Go
          source: "package main\n\nimport (\n\t\"bytes\"\n\t\"encoding/json\"\n\t\"fmt\"\n\t\"net/http\"\n)\n\nfunc main() {\n\tpayload := []byte(`{\"url\":\"https://geo.brdtest.com/welcome.txt\"}`)\n\n\treq, _ := http.NewRequest(\"POST\",\n\t\t\"https://api.brightdata.com/unblocker/req?zone=web_unlocker1\",\n\t\tbytes.NewBuffer(payload))\n\treq.Header.Set(\"Authorization\", \"Bearer YOUR_API_KEY\")\n\treq.Header.Set(\"Content-Type\", \"application/json\")\n\n\tres, err := http.DefaultClient.Do(req)\n\tif err != nil {\n\t\tpanic(err)\n\t}\n\tdefer res.Body.Close()\n\n\t// Keep the ResponseID: you need it to collect the result.\n\tvar job struct {\n\t\tResponseID string `json:\"response_id\"`\n\t}\n\tjson.NewDecoder(res.Body).Decode(&job)\n\tfmt.Println(job.ResponseID)\n}"
components:
  schemas:
    JobResponse:
      type: object
      properties:
        response_id:
          description: Defines the job id.
          type: string
          example: s4t7w3619285042ra9dke1m8qx
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