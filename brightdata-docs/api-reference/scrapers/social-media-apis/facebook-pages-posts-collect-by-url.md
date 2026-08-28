> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Collect page posts by URL

> Use the Bright Data Web Scraper API to collect Page Posts by URL. Calls the POST /datasets/v3/scrape endpoint and returns a snapshot ID.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_lkaxegm826bjpoo9m5" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_lkaxegm826bjpoo9m5` to collect **Facebook page posts** data.
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
      The URL of the Facebook page to collect posts from.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {"url": "https://www.facebook.com/NASA"},
      {"url": "https://www.facebook.com/Meta"}
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "url": "https://www.facebook.com/reel/1417029756382510/",
      "post_id": "1325707186087218",
      "user_url": "https://www.facebook.com/delish",
      "user_username_raw": "delish",
      "content": "Sweet niblets! This just unlocked a childhood memory",
      "date_posted": "2026-03-21T19:01:34.000Z",
      "hashtags": null,
      "num_comments": 1,
      "num_shares": 2,
      "num_likes_type": { "num": 34, "type": "Like" },
      "page_name": "Delish",
      "profile_id": "100059438474191",
      "page_intro": "Fun eats every day of the week.",
      "page_category": "News & media website",
      "page_logo": "https://...",
      "page_external_website": "likeshop.me/delish",
      "page_likes": null,
      "page_followers": 21000000,
      "page_is_verified": true,
      "original_post": { "user_avatar_image": null },
      "attachments": [
        {
          "attachment_url": "https://...",
          "id": "1417029756382510",
          "thumbnail_url": "https://...",
          "type": "Video",
          "url": "https://...",
          "video_length": "15509",
          "video_url": "https://..."
        }
      ],
      "page_url": "https://www.facebook.com/delish",
      "header_image": "https://...",
      "avatar_image_url": "https://...",
      "profile_handle": "delish",
      "is_sponsored": false,
      "shortcode": "1325707186087218",
      "video_view_count": 24093,
      "likes": 39,
      "post_type": "Reel",
      "following": 19,
      "count_reactions_type": [
        { "reaction_count": 34, "type": "Like" },
        { "reaction_count": 4, "type": "Haha" }
      ],
      "is_page": true,
      "play_count": 45717
    }
  ]
  ```
</ResponseExample>


## OpenAPI

````yaml api-reference/sdk-specs/facebook-pages-posts-collect-by-url POST /datasets/v3/scrape
openapi: 3.0.0
info:
  title: Collect Page Posts by URL
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security: []
paths:
  /datasets/v3/scrape:
    post:
      summary: Collect Page Posts by URL
      description: >-
        Use the Bright Data Web Scraper API to collect Page Posts by URL. Submit
        the request and retrieve the data as structured JSON records once the
        job completes.
      parameters:
        - in: query
          name: dataset_id
          required: true
          schema:
            type: string
            default: gd_lkaxegm826bjpoo9m5
          description: Must be `gd_lkaxegm826bjpoo9m5` for this dataset.
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
              --url 'https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lkaxegm826bjpoo9m5&include_errors=true' \
              --header "Authorization: Bearer YOUR_API_KEY" \
              --header "Content-Type: application/json" \
              --data '{"input": [{"url": "https://www.facebook.com/NASA"}, {"url": "https://www.facebook.com/Meta"}]}'
        - lang: python
          label: Python
          source: >-
            import requests


            url =
            "https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lkaxegm826bjpoo9m5&include_errors=true"

            headers = {
                "Authorization": "Bearer YOUR_API_KEY",
                "Content-Type": "application/json",
            }

            payload = {
                "input": [
                    {
                        "url": "https://www.facebook.com/NASA"
                    },
                    {
                        "url": "https://www.facebook.com/Meta"
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
                result = await client.scrape.facebook.posts_by_profile(url="https://www.facebook.com/nasa", num_of_posts=10)
                print(result.data)
        - lang: javascript
          label: JavaScript
          source: >-
            const response = await
            fetch("https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lkaxegm826bjpoo9m5&include_errors=true",
            {
              method: "POST",
              headers: {
                "Authorization": "Bearer YOUR_API_KEY",
                "Content-Type": "application/json",
              },
              body: JSON.stringify({
                "input": [
                    {
                        "url": "https://www.facebook.com/NASA"
                    },
                    {
                        "url": "https://www.facebook.com/Meta"
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
            client.scrape.facebook.collectPostsByProfile(['https://www.facebook.com/nasa']);

            console.log(result);


            await client.close();
        - lang: php
          label: PHP
          source: >-
            <?php

            $ch =
            curl_init("https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lkaxegm826bjpoo9m5&include_errors=true");

            curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");

            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

            curl_setopt($ch, CURLOPT_HTTPHEADER, [
                "Authorization: Bearer YOUR_API_KEY",
                "Content-Type: application/json",
            ]);

            curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode([
                "input" => [
                    [
                        "url" => "https://www.facebook.com/NASA"
                    ],
                    [
                        "url" => "https://www.facebook.com/Meta"
                    ]
                ]
            ]));


            $response = curl_exec($ch);

            curl_close($ch);

            echo $response;
        - lang: go
          label: Go
          source: "package main\n\nimport (\n\t\"bytes\"\n\t\"fmt\"\n\t\"io\"\n\t\"net/http\"\n)\n\nfunc main() {\n\tpayload := []byte(\"{\\\"input\\\": [{\\\"url\\\": \\\"https://www.facebook.com/NASA\\\"}, {\\\"url\\\": \\\"https://www.facebook.com/Meta\\\"}]}\")\n\treq, _ := http.NewRequest(\"POST\", \"https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lkaxegm826bjpoo9m5&include_errors=true\", bytes.NewBuffer(payload))\n\treq.Header.Set(\"Authorization\", \"Bearer YOUR_API_KEY\")\n\treq.Header.Set(\"Content-Type\", \"application/json\")\n\n\tres, err := http.DefaultClient.Do(req)\n\tif err != nil { panic(err) }\n\tdefer res.Body.Close()\n\n\tbody, _ := io.ReadAll(res.Body)\n\tfmt.Println(string(body))\n}"
        - lang: java
          label: Java
          source: |-
            import java.net.URI;
            import java.net.http.HttpClient;
            import java.net.http.HttpRequest;
            import java.net.http.HttpResponse;

            public class Main {
                public static void main(String[] args) throws Exception {
                    String body = "{\"input\": [{\"url\": \"https://www.facebook.com/NASA\"}, {\"url\": \"https://www.facebook.com/Meta\"}]}";
                    HttpRequest request = HttpRequest.newBuilder()
                        .uri(URI.create("https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lkaxegm826bjpoo9m5&include_errors=true"))
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
            URI.parse("https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lkaxegm826bjpoo9m5&include_errors=true")

            request = Net::HTTP::Post.new(uri)

            request["Authorization"] = "Bearer YOUR_API_KEY"

            request["Content-Type"] = "application/json"

            request.body = {"input": [{"url": "https://www.facebook.com/NASA"},
            {"url": "https://www.facebook.com/Meta"}]}.to_json


            response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) {
            |http| http.request(request) }

            puts response.body

````