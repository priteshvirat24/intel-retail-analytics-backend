> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Collect reels by profile URL

> Use the Bright Data Web Scraper API to collect Reels by Profile URL. Calls the POST /datasets/v3/scrape endpoint and returns a snapshot ID.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_lyclm3ey2q6rww027t" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_lyclm3ey2q6rww027t` to collect **Facebook reels** data.
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
      The URL of the Facebook profile to collect reels from.
    </ParamField>

    <ParamField body="num_of_posts" type="number">
      The number of recent reels to collect. Missing value indicates no limit.
    </ParamField>

    <ParamField body="posts_to_not_include" type="string[]">
      Post IDs not to include.
    </ParamField>

    <ParamField body="start_date" type="string">
      Start date filter `MM-DD-YYYY` (should be earlier than "end\_date").
    </ParamField>

    <ParamField body="end_date" type="string">
      End date filter `MM-DD-YYYY` (should be later than "start\_date").
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {"url": "https://www.facebook.com/MrBeast6000", "num_of_posts": 10},
      {"url": "https://www.facebook.com/NASA", "start_date": "01-01-2025", "end_date": "03-01-2025"}
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "url": "https://www.facebook.com/reel/2128461008004479",
      "post_id": "1417440860423673",
      "user_url": "https://www.facebook.com/tmcnewsbr",
      "user_username_raw": "Radio Transamerica FM",
      "content": "Increase in US-Iran tensions...",
      "date_posted": "2026-04-06T00:00:00.000Z",
      "hashtags": ["#guerra", "#eua"],
      "num_comments": 2,
      "num_shares": 0,
      "video_view_count": 582,
      "likes": 3,
      "page_name": "Radio Transamerica FM",
      "profile_id": "100064733164731",
      "page_logo": "https://...",
      "page_likes": 0,
      "page_followers": 1200000,
      "thumbnail": "https://...",
      "page_url": "https://www.facebook.com/tmcnewsbr",
      "profile_handle": "tmcnewsbr",
      "shortcode": "2128461008004479",
      "length": 13.888,
      "audio": "AVAILABLE",
      "video_url": "https://..."
    }
  ]
  ```
</ResponseExample>


## OpenAPI

````yaml api-reference/sdk-specs/facebook-reels-collect-by-url POST /datasets/v3/scrape
openapi: 3.0.0
info:
  title: Collect Reels by Profile URL
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security: []
paths:
  /datasets/v3/scrape:
    post:
      summary: Collect Reels by Profile URL
      description: >-
        Use the Bright Data Web Scraper API to collect Reels by Profile URL.
        Submit the request and retrieve the data as structured JSON records once
        the job completes.
      parameters:
        - in: query
          name: dataset_id
          required: true
          schema:
            type: string
            default: gd_lyclm3ey2q6rww027t
          description: Must be `gd_lyclm3ey2q6rww027t` for this dataset.
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
                        example: https://www.facebook.com/nasa
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
              --url 'https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lyclm3ey2q6rww027t&include_errors=true' \
              --header "Authorization: Bearer YOUR_API_KEY" \
              --header "Content-Type: application/json" \
              --data '{"input": [{"url": "https://www.facebook.com/MrBeast6000", "num_of_posts": 10}, {"url": "https://www.facebook.com/NASA", "start_date": "01-01-2025", "end_date": "03-01-2025"}]}'
        - lang: python
          label: Python
          source: >-
            import requests


            url =
            "https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lyclm3ey2q6rww027t&include_errors=true"

            headers = {
                "Authorization": "Bearer YOUR_API_KEY",
                "Content-Type": "application/json",
            }

            payload = {
                "input": [
                    {
                        "url": "https://www.facebook.com/MrBeast6000",
                        "num_of_posts": 10
                    },
                    {
                        "url": "https://www.facebook.com/NASA",
                        "start_date": "01-01-2025",
                        "end_date": "03-01-2025"
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
                result = await client.scrape.facebook.reels(url="https://www.facebook.com/nasa")
                print(result.data)
        - lang: javascript
          label: JavaScript
          source: >-
            const response = await
            fetch("https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lyclm3ey2q6rww027t&include_errors=true",
            {
              method: "POST",
              headers: {
                "Authorization": "Bearer YOUR_API_KEY",
                "Content-Type": "application/json",
              },
              body: JSON.stringify({
                "input": [
                    {
                        "url": "https://www.facebook.com/MrBeast6000",
                        "num_of_posts": 10
                    },
                    {
                        "url": "https://www.facebook.com/NASA",
                        "start_date": "01-01-2025",
                        "end_date": "03-01-2025"
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


            const result = await
            client.scrape.facebook.collectReels(['https://www.facebook.com/nasa']);

            console.log(result);


            await client.close();
        - lang: php
          label: PHP
          source: >-
            <?php

            $ch =
            curl_init("https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lyclm3ey2q6rww027t&include_errors=true");

            curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");

            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

            curl_setopt($ch, CURLOPT_HTTPHEADER, [
                "Authorization: Bearer YOUR_API_KEY",
                "Content-Type: application/json",
            ]);

            curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode([
                "input" => [
                    [
                        "url" => "https://www.facebook.com/MrBeast6000",
                        "num_of_posts" => 10
                    ],
                    [
                        "url" => "https://www.facebook.com/NASA",
                        "start_date" => "01-01-2025",
                        "end_date" => "03-01-2025"
                    ]
                ]
            ]));


            $response = curl_exec($ch);

            curl_close($ch);

            echo $response;
        - lang: go
          label: Go
          source: "package main\n\nimport (\n\t\"bytes\"\n\t\"fmt\"\n\t\"io\"\n\t\"net/http\"\n)\n\nfunc main() {\n\tpayload := []byte(\"{\\\"input\\\": [{\\\"url\\\": \\\"https://www.facebook.com/MrBeast6000\\\", \\\"num_of_posts\\\": 10}, {\\\"url\\\": \\\"https://www.facebook.com/NASA\\\", \\\"start_date\\\": \\\"01-01-2025\\\", \\\"end_date\\\": \\\"03-01-2025\\\"}]}\")\n\treq, _ := http.NewRequest(\"POST\", \"https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lyclm3ey2q6rww027t&include_errors=true\", bytes.NewBuffer(payload))\n\treq.Header.Set(\"Authorization\", \"Bearer YOUR_API_KEY\")\n\treq.Header.Set(\"Content-Type\", \"application/json\")\n\n\tres, err := http.DefaultClient.Do(req)\n\tif err != nil { panic(err) }\n\tdefer res.Body.Close()\n\n\tbody, _ := io.ReadAll(res.Body)\n\tfmt.Println(string(body))\n}"
        - lang: java
          label: Java
          source: |-
            import java.net.URI;
            import java.net.http.HttpClient;
            import java.net.http.HttpRequest;
            import java.net.http.HttpResponse;

            public class Main {
                public static void main(String[] args) throws Exception {
                    String body = "{\"input\": [{\"url\": \"https://www.facebook.com/MrBeast6000\", \"num_of_posts\": 10}, {\"url\": \"https://www.facebook.com/NASA\", \"start_date\": \"01-01-2025\", \"end_date\": \"03-01-2025\"}]}";
                    HttpRequest request = HttpRequest.newBuilder()
                        .uri(URI.create("https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lyclm3ey2q6rww027t&include_errors=true"))
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
            URI.parse("https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lyclm3ey2q6rww027t&include_errors=true")

            request = Net::HTTP::Post.new(uri)

            request["Authorization"] = "Bearer YOUR_API_KEY"

            request["Content-Type"] = "application/json"

            request.body = {"input": [{"url":
            "https://www.facebook.com/MrBeast6000", "num_of_posts": 10}, {"url":
            "https://www.facebook.com/NASA", "start_date": "01-01-2025",
            "end_date": "03-01-2025"}]}.to_json


            response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) {
            |http| http.request(request) }

            puts response.body

````