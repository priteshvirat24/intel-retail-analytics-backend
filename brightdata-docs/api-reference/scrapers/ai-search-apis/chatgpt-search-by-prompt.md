> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Search by prompt

> Use the Bright Data AI Search API to search by Prompt. POST /datasets/v3/scrape triggers a job that returns structured AI search results as JSON.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_m7aof0k82r803d5bjm" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_m7aof0k82r803d5bjm` to collect **ChatGPT Search - Search by Prompt** data.
  </Warning>
</ParamField>

<ParamField query="notify" type="boolean" default={false}>
  Whether to send notifications when the request is completed.
</ParamField>

<ParamField query="include_errors" type="boolean" default={true}>
  Whether to include errors in the response.
</ParamField>

## Request Body

<ParamField body="input" type="object[]" required>
  An array of input objects.

  <Expandable title="properties">
    <ParamField body="url" type="string" required>
      The ChatGPT page URL. Must be set to `https://chatgpt.com/`.
    </ParamField>

    <ParamField body="prompt" type="string" required>
      The search prompt. Each prompt triggers a separate ChatGPT search query. Maximum 4,096 characters.
    </ParamField>

    <ParamField body="country" type="string">
      Country from which to perform the search.
    </ParamField>

    <ParamField body="index" type="number">
      Unique ID for tracking each crawl request.
    </ParamField>

    <ParamField body="require_sources" type="boolean">
      If set to `true` and sources are not found in the page, an error message is returned instead of the record.
    </ParamField>

    <ParamField body="additional_prompt" type="string">
      A follow-up input sent after receiving the first answer, aiming to clarify, expand, or refine the initial response. The result is returned as `additional_answer_text`.
    </ParamField>

    <ParamField body="web_search" type="boolean" default={true}>
      Permission to run an external web search during the run. If set to `true` (default), the Web Search button is enabled and the model may click it. If `false`, the button is never clicked and the model will not trigger a web search. This field is a **permission, not a guarantee**: setting `true` does not mean a search will happen. Read `web_search_triggered` in the response to know whether a search actually ran. See [Query fan-out and web search control](/datasets/scrapers/concepts/query-fan-out).
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {"url": "https://chatgpt.com/", "prompt": "Top hotels in New York", "country": "us", "web_search": true},
      {"url": "https://chatgpt.com/", "prompt": "What are the biggest business trends to watch in the next five years?"}
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "url": "https://chatgpt.com/?q=Top%20hotels%20in%20New%20York",
      "prompt": "Top hotels in New York",
      "answer_text": "Here are some of the top-rated hotels in New York City...",
      "answer_text_markdown": "## Top Hotels in New York City\n\n1. **The Plaza** - Iconic luxury...",
      "answer_html": "<div>...</div>",
      "model": "gpt-4o",
      "web_search_triggered": true,
      "citations": [
        {
          "title": "Best Hotels in NYC 2024",
          "url": "https://www.travelandleisure.com/best-hotels-nyc",
          "position": 1
        }
      ],
      "search_sources": [
        {
          "url": "https://www.travelandleisure.com/best-hotels-nyc",
          "title": "Best Hotels in NYC",
          "favicon": "https://www.travelandleisure.com/favicon.ico"
        }
      ],
      "links_attached": [
        {
          "url": "https://www.theplazany.com",
          "text": "The Plaza",
          "position": 0
        }
      ],
      "recommendations": [],
      "references": [],
      "country": "us",
      "is_map": true,
      "shopping_visible": false,
      "prompt_sent_at": "2024-12-15T10:30:00.000Z",
      "index": null
    }
  ]
  ```
</ResponseExample>


## OpenAPI

````yaml api-reference/sdk-specs/chatgpt-search-by-prompt POST /datasets/v3/scrape
openapi: 3.0.0
info:
  title: Search by Prompt
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security: []
paths:
  /datasets/v3/scrape:
    post:
      summary: Search by Prompt
      description: >-
        Use the Bright Data AI Search API to search by Prompt. POST
        /datasets/v3/scrape triggers a job that returns structured AI search
        results as JSON.
      parameters:
        - in: query
          name: dataset_id
          required: true
          schema:
            type: string
            default: gd_m7aof0k82r803d5bjm
          description: Must be `gd_m7aof0k82r803d5bjm` for this dataset.
        - in: query
          name: notify
          required: false
          schema:
            type: boolean
            default: false
          description: Send notifications when the request is completed.
        - in: query
          name: include_errors
          required: false
          schema:
            type: boolean
            default: true
          description: Include errors in the response.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - input
              properties:
                input:
                  type: array
                  description: >-
                    Array of input objects. See `Request Body` below for the
                    supported fields.
                  items:
                    type: object
                    required:
                      - url
                    properties:
                      url:
                        type: string
                        example: null
      responses:
        '200':
          description: OK. See response example below the parameters.
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
      x-codeSamples:
        - lang: shell
          label: cURL
          source: |-
            curl --request POST \
              --url 'https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_m7aof0k82r803d5bjm&include_errors=true' \
              --header "Authorization: Bearer YOUR_API_KEY" \
              --header "Content-Type: application/json" \
              --data '{"input": [{"url": "https://chatgpt.com/", "prompt": "Top hotels in New York", "country": "us", "web_search": true}, {"url": "https://chatgpt.com/", "prompt": "What are the biggest business trends to watch in the next five years?"}]}'
        - lang: python
          label: Python
          source: >-
            import requests


            url =
            "https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_m7aof0k82r803d5bjm&include_errors=true"

            headers = {
                "Authorization": "Bearer YOUR_API_KEY",
                "Content-Type": "application/json",
            }

            payload = {
                "input": [
                    {
                        "url": "https://chatgpt.com/",
                        "prompt": "Top hotels in New York",
                        "country": "us",
                        "web_search": true
                    },
                    {
                        "url": "https://chatgpt.com/",
                        "prompt": "What are the biggest business trends to watch in the next five years?"
                    }
                ]
            }


            response = requests.post(url, headers=headers, json=payload)

            print(response.text)
        - lang: py
          label: Python SDK
          source: |-
            # Install: pip install brightdata-sdk
            from brightdata import BrightDataClient

            async with BrightDataClient(api_key="YOUR_API_KEY") as client:
                result = await client.scrape.chatgpt.prompt(prompt="What are the latest trends in AI?", web_search=True)
                print(result.data)
        - lang: javascript
          label: JavaScript
          source: >-
            const response = await
            fetch("https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_m7aof0k82r803d5bjm&include_errors=true",
            {
              method: "POST",
              headers: {
                "Authorization": "Bearer YOUR_API_KEY",
                "Content-Type": "application/json",
              },
              body: JSON.stringify({
                "input": [
                    {
                        "url": "https://chatgpt.com/",
                        "prompt": "Top hotels in New York",
                        "country": "us",
                        "web_search": true
                    },
                    {
                        "url": "https://chatgpt.com/",
                        "prompt": "What are the biggest business trends to watch in the next five years?"
                    }
                ]
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


            const result = await client.scrape.chatGPT.search(['What are the
            latest trends in AI?']);

            console.log(result);


            await client.close();
        - lang: php
          label: PHP
          source: >-
            <?php

            $ch =
            curl_init("https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_m7aof0k82r803d5bjm&include_errors=true");

            curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");

            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

            curl_setopt($ch, CURLOPT_HTTPHEADER, [
                "Authorization: Bearer YOUR_API_KEY",
                "Content-Type: application/json",
            ]);

            curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode([
                "input" => [
                    [
                        "url" => "https://chatgpt.com/",
                        "prompt" => "Top hotels in New York",
                        "country" => "us",
                        "web_search" => true
                    ],
                    [
                        "url" => "https://chatgpt.com/",
                        "prompt" => "What are the biggest business trends to watch in the next five years?"
                    ]
                ]
            ]));


            $response = curl_exec($ch);

            curl_close($ch);

            echo $response;
        - lang: go
          label: Go
          source: "package main\n\nimport (\n\t\"bytes\"\n\t\"fmt\"\n\t\"io\"\n\t\"net/http\"\n)\n\nfunc main() {\n\tpayload := []byte(\"{\\\"input\\\": [{\\\"url\\\": \\\"https://chatgpt.com/\\\", \\\"prompt\\\": \\\"Top hotels in New York\\\", \\\"country\\\": \\\"us\\\", \\\"web_search\\\": true}, {\\\"url\\\": \\\"https://chatgpt.com/\\\", \\\"prompt\\\": \\\"What are the biggest business trends to watch in the next five years?\\\"}]}\")\n\treq, _ := http.NewRequest(\"POST\", \"https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_m7aof0k82r803d5bjm&include_errors=true\", bytes.NewBuffer(payload))\n\treq.Header.Set(\"Authorization\", \"Bearer YOUR_API_KEY\")\n\treq.Header.Set(\"Content-Type\", \"application/json\")\n\n\tres, err := http.DefaultClient.Do(req)\n\tif err != nil { panic(err) }\n\tdefer res.Body.Close()\n\n\tbody, _ := io.ReadAll(res.Body)\n\tfmt.Println(string(body))\n}"
        - lang: java
          label: Java
          source: |-
            import java.net.URI;
            import java.net.http.HttpClient;
            import java.net.http.HttpRequest;
            import java.net.http.HttpResponse;

            public class Main {
                public static void main(String[] args) throws Exception {
                    String body = "{\"input\": [{\"url\": \"https://chatgpt.com/\", \"prompt\": \"Top hotels in New York\", \"country\": \"us\", \"web_search\": true}, {\"url\": \"https://chatgpt.com/\", \"prompt\": \"What are the biggest business trends to watch in the next five years?\"}]}";
                    HttpRequest request = HttpRequest.newBuilder()
                        .uri(URI.create("https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_m7aof0k82r803d5bjm&include_errors=true"))
                        .header("Authorization", "Bearer YOUR_API_KEY")
                        .header("Content-Type", "application/json")
                        .method("POST", HttpRequest.BodyPublishers.ofString(body))
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


            uri =
            URI.parse("https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_m7aof0k82r803d5bjm&include_errors=true")

            request = Net::HTTP::Post.new(uri)

            request["Authorization"] = "Bearer YOUR_API_KEY"

            request["Content-Type"] = "application/json"

            request.body = {"input": [{"url": "https://chatgpt.com/", "prompt":
            "Top hotels in New York", "country": "us", "web_search": true},
            {"url": "https://chatgpt.com/", "prompt": "What are the biggest
            business trends to watch in the next five years?"}]}.to_json


            response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) {
            |http| http.request(request) }

            puts response.body

````