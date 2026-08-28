> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Collect videos by URL

> Use the Bright Data Web Scraper API to collect Videos by URL. POST /datasets/v3/scrape starts a scraping job that returns the data as structured JSON records.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_lk56epmy2i5g7lzu0k" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_lk56epmy2i5g7lzu0k` to collect **YouTube videos** data.
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
      The YouTube video URL to collect data from.
    </ParamField>

    <ParamField body="country" type="string">
      The country to use for the request.
    </ParamField>

    <ParamField body="transcription_language" type="string">
      The language for video transcription.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"},
      {"url": "https://www.youtube.com/watch?v=4L_m0m3bEtE"}
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "url": "https://www.youtube.com/watch?v=4L_m0m3bEtE",
      "title": "Video Title Here",
      "youtuber": "@channelname",
      "video_url": "https://...",
      "video_length": 96,
      "likes": 18,
      "views": 1648,
      "date_posted": "2025-04-18T05:26:16.000Z",
      "description": "Video description...",
      "num_comments": 0,
      "subscribers": 4810000,
      "video_id": "4L_m0m3bEtE",
      "channel_url": "https://www.youtube.com/@channelname",
      "preview_image": "https://i.ytimg.com/vi/4L_m0m3bEtE/maxresdefault.jpg",
      "shortcode": "4L_m0m3bEtE",
      "verified": true,
      "handle_name": "Channel Name",
      "is_sponsored": false,
      "quality": "hd1080",
      "transcript": "...",
      "tags": ["tag1", "tag2"],
      "is_age_restricted": false
    }
  ]
  ```
</ResponseExample>


## OpenAPI

````yaml api-reference/sdk-specs/youtube-videos-collect-by-url POST /datasets/v3/scrape
openapi: 3.0.0
info:
  title: Collect Videos by URL
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security: []
paths:
  /datasets/v3/scrape:
    post:
      summary: Collect Videos by URL
      description: >-
        Use the Bright Data Web Scraper API to collect Videos by URL. POST
        /datasets/v3/scrape starts a scraping job that returns the data as
        structured JSON records.
      parameters:
        - in: query
          name: dataset_id
          required: true
          schema:
            type: string
            default: gd_lk56epmy2i5g7lzu0k
          description: Must be `gd_lk56epmy2i5g7lzu0k` for this dataset.
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
                        example: https://www.youtube.com/watch?v=dQw4w9WgXcQ
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
              --url 'https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lk56epmy2i5g7lzu0k&include_errors=true' \
              --header "Authorization: Bearer YOUR_API_KEY" \
              --header "Content-Type: application/json" \
              --data '{"input": [{"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}, {"url": "https://www.youtube.com/watch?v=4L_m0m3bEtE"}]}'
        - lang: python
          label: Python
          source: >-
            import requests


            url =
            "https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lk56epmy2i5g7lzu0k&include_errors=true"

            headers = {
                "Authorization": "Bearer YOUR_API_KEY",
                "Content-Type": "application/json",
            }

            payload = {
                "input": [
                    {
                        "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                    },
                    {
                        "url": "https://www.youtube.com/watch?v=4L_m0m3bEtE"
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
                result = await client.scrape.youtube.videos(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", transcription_language="English")
                print(result.data)
        - lang: javascript
          label: JavaScript
          source: >-
            const response = await
            fetch("https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lk56epmy2i5g7lzu0k&include_errors=true",
            {
              method: "POST",
              headers: {
                "Authorization": "Bearer YOUR_API_KEY",
                "Content-Type": "application/json",
              },
              body: JSON.stringify({
                "input": [
                    {
                        "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                    },
                    {
                        "url": "https://www.youtube.com/watch?v=4L_m0m3bEtE"
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
            client.scrape.youtube.collectVideos(['https://www.youtube.com/watch?v=dQw4w9WgXcQ']);

            console.log(result);


            await client.close();
        - lang: php
          label: PHP
          source: >-
            <?php

            $ch =
            curl_init("https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lk56epmy2i5g7lzu0k&include_errors=true");

            curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");

            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

            curl_setopt($ch, CURLOPT_HTTPHEADER, [
                "Authorization: Bearer YOUR_API_KEY",
                "Content-Type: application/json",
            ]);

            curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode([
                "input" => [
                    [
                        "url" => "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                    ],
                    [
                        "url" => "https://www.youtube.com/watch?v=4L_m0m3bEtE"
                    ]
                ]
            ]));


            $response = curl_exec($ch);

            curl_close($ch);

            echo $response;
        - lang: go
          label: Go
          source: "package main\n\nimport (\n\t\"bytes\"\n\t\"fmt\"\n\t\"io\"\n\t\"net/http\"\n)\n\nfunc main() {\n\tpayload := []byte(\"{\\\"input\\\": [{\\\"url\\\": \\\"https://www.youtube.com/watch?v=dQw4w9WgXcQ\\\"}, {\\\"url\\\": \\\"https://www.youtube.com/watch?v=4L_m0m3bEtE\\\"}]}\")\n\treq, _ := http.NewRequest(\"POST\", \"https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lk56epmy2i5g7lzu0k&include_errors=true\", bytes.NewBuffer(payload))\n\treq.Header.Set(\"Authorization\", \"Bearer YOUR_API_KEY\")\n\treq.Header.Set(\"Content-Type\", \"application/json\")\n\n\tres, err := http.DefaultClient.Do(req)\n\tif err != nil { panic(err) }\n\tdefer res.Body.Close()\n\n\tbody, _ := io.ReadAll(res.Body)\n\tfmt.Println(string(body))\n}"
        - lang: java
          label: Java
          source: |-
            import java.net.URI;
            import java.net.http.HttpClient;
            import java.net.http.HttpRequest;
            import java.net.http.HttpResponse;

            public class Main {
                public static void main(String[] args) throws Exception {
                    String body = "{\"input\": [{\"url\": \"https://www.youtube.com/watch?v=dQw4w9WgXcQ\"}, {\"url\": \"https://www.youtube.com/watch?v=4L_m0m3bEtE\"}]}";
                    HttpRequest request = HttpRequest.newBuilder()
                        .uri(URI.create("https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lk56epmy2i5g7lzu0k&include_errors=true"))
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
            URI.parse("https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lk56epmy2i5g7lzu0k&include_errors=true")

            request = Net::HTTP::Post.new(uri)

            request["Authorization"] = "Bearer YOUR_API_KEY"

            request["Content-Type"] = "application/json"

            request.body = {"input": [{"url":
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}, {"url":
            "https://www.youtube.com/watch?v=4L_m0m3bEtE"}]}.to_json


            response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) {
            |http| http.request(request) }

            puts response.body

````