> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Collect reels by URL

> Use the Bright Data Web Scraper API to collect Reels by URL. POST /datasets/v3/scrape starts a scraping job that returns the data as structured JSON records.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_lyclm20il4r5helnj" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_lyclm20il4r5helnj` to collect **Reels by URL** data.
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
      The URL of the Instagram reels to collect.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input":[
      {"url":"https://www.instagram.com/reel/C5Rdyj_q7YN/"},
      {"url":"https://www.instagram.com/reel/C85BZjeSHuO"}
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "url": "https://www.instagram.com/reel/DVNLU52gCAP/",
      "user_posted": "lanceoca",
      "description": "clingy naman ng bebe na yan 😂😂",
      "hashtags": null,
      "num_comments": 6,
      "date_posted": "2026-02-26T03:23:20.000Z",
      "likes": 3,
      "views": 388,
      "video_play_count": 1890,
      "top_comments": [
        {
          "avatar": "https://scontent-phl2-1.cdninstagram.com/v/t51.2885-19/365460701_613557573974169_4246269411584735337_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby45NTcuYzIifQ&_nc_ht=scontent-phl2-1.cdninstagram.com&_nc_cat=109&_nc_oc=Q6cZ2QH2Km-HWtG_kFjSkWI-wtXI14TUgdgZN3CffFjRE0mZMwRZwsr6ISXIttcetnv45fU&_nc_ohc=1sksn4DLF60Q7kNvwGVdyy-&_nc_gid=1nVoOKHoCkOl8-av4Iwgkg&edm=ANTKIIoBAAAA&ccb=7-5&oh=00_AfznARNQ0EpZxuYD13_j-z1x5gVSXJzuDNLf27ksGkq9Gg&oe=69BD27FC&_nc_sid=d885a2",
          "comment": "So handsome😍😍😍😍",
          "date_of_comment": "2026-03-05T03:12:12.000Z",
          "likes": null,
          "num_replies": 0,
          "replies": [],
          "user_commenting": "jgmagboo"
        },
        {
          "avatar": "https://scontent-phl2-1.cdninstagram.com/v/t51.82787-19/604381380_17846853735621432_1417364464978583437_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4zMjAuYzIifQ&_nc_ht=scontent-phl2-1.cdninstagram.com&_nc_cat=100&_nc_oc=Q6cZ2QH2Km-HWtG_kFjSkWI-wtXI14TUgdgZN3CffFjRE0mZMwRZwsr6ISXIttcetnv45fU&_nc_ohc=wxn_bgzeNMoQ7kNvwGZZc1t&_nc_gid=1nVoOKHoCkOl8-av4Iwgkg&edm=ANTKIIoBAAAA&ccb=7-5&oh=00_AfzilHku95q5GuC9yL0SW82MZL569Zijwn6C6K-V26ohaA&oe=69BD2DE4&_nc_sid=d885a2",
          "comment": "😢hello handsome",
          "date_of_comment": "2026-03-02T22:51:50.000Z",
          "likes": null,
          "num_replies": 0,
          "replies": [],
          "user_commenting": "mavic6620"
        },
        {
          "avatar": "https://scontent-phl2-1.cdninstagram.com/v/t51.2885-19/487313612_1015621063797112_1603884341697763156_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-phl2-1.cdninstagram.com&_nc_cat=104&_nc_oc=Q6cZ2QH2Km-HWtG_kFjSkWI-wtXI14TUgdgZN3CffFjRE0mZMwRZwsr6ISXIttcetnv45fU&_nc_ohc=FDBy91MOg4AQ7kNvwFSG43x&_nc_gid=1nVoOKHoCkOl8-av4Iwgkg&edm=ANTKIIoBAAAA&ccb=7-5&oh=00_Afw_I5Ji5g_FizTfUahhtB2N5dlEHBfF785jDNFXxxLPzw&oe=69BD245E&_nc_sid=d885a2",
          "comment": "Hi there..😍😍🔥",
          "date_of_comment": "2026-02-28T02:47:21.000Z",
          "likes": "1",
          "num_replies": 0,
          "replies": [],
          "user_commenting": "lajas621"
        },
        {
          "avatar": "https://scontent-phl2-1.cdninstagram.com/v/t51.82787-19/589404006_17927065818169590_4230007312536318761_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby43MjAuYzIifQ&_nc_ht=scontent-phl2-1.cdninstagram.com&_nc_cat=106&_nc_oc=Q6cZ2QH2Km-HWtG_kFjSkWI-wtXI14TUgdgZN3CffFjRE0mZMwRZwsr6ISXIttcetnv45fU&_nc_ohc=3cCCnbM9pjkQ7kNvwFuVke7&_nc_gid=1nVoOKHoCkOl8-av4Iwgkg&edm=ANTKIIoBAAAA&ccb=7-5&oh=00_AfyMahn5ck5AEFFmQUrEH1I7VIWpWjok0AU4EwOZtOwpuw&oe=69BD1C6F&_nc_sid=d885a2",
          "comment": "Wow❤️❤️❤️",
          "date_of_comment": "2026-02-26T08:15:44.000Z",
          "likes": null,
          "num_replies": 0,
          "replies": [],
          "user_commenting": "jennalyn294"
        },
        {
          "avatar": "https://scontent-phl2-1.cdninstagram.com/v/t51.82787-19/643610031_18394067647195478_6467437205157259761_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4zMjAuYzIifQ&_nc_ht=scontent-phl2-1.cdninstagram.com&_nc_cat=102&_nc_oc=Q6cZ2QH2Km-HWtG_kFjSkWI-wtXI14TUgdgZN3CffFjRE0mZMwRZwsr6ISXIttcetnv45fU&_nc_ohc=R1RL_k362XwQ7kNvwHO8U39&_nc_gid=1nVoOKHoCkOl8-av4Iwgkg&edm=ANTKIIoBAAAA&ccb=7-5&oh=00_AfxLuxMSr1rcvJEsa2UrMoP8Lz-wVzC72xQZ1W3-1byjSA&oe=69BD02EE&_nc_sid=d885a2",
          "comment": "iloveyou ❤️❤️❤️😘",
          "date_of_comment": "2026-02-26T06:42:50.000Z",
          "likes": null,
          "num_replies": 0,
          "replies": [],
          "user_commenting": "mhat.memoracion"
        },
        {
          "avatar": "https://scontent-phl2-1.cdninstagram.com/v/t51.82787-19/611627622_18554417668038304_6341390296922072598_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-phl2-1.cdninstagram.com&_nc_cat=104&_nc_oc=Q6cZ2QH2Km-HWtG_kFjSkWI-wtXI14TUgdgZN3CffFjRE0mZMwRZwsr6ISXIttcetnv45fU&_nc_ohc=AJwRgGMf_coQ7kNvwHWBhko&_nc_gid=1nVoOKHoCkOl8-av4Iwgkg&edm=ANTKIIoBAAAA&ccb=7-5&oh=00_Afy9MgvDJ_Jv-SVLKAiJVtHaCVrfqmpEtjYOoBCyj_OKjA&oe=69BD0E87&_nc_sid=d885a2",
          "comment": "Kennyyyyy! 😍😍",
          "date_of_comment": "2026-02-26T03:55:43.000Z",
          "likes": null,
          "num_replies": 0,
          "replies": [],
          "user_commenting": "thatsellengayle"
        }
      ],
      "post_id": "3840775872235708431_497234441",
      "thumbnail": "https://scontent-phl2-1.cdninstagram.com/v/t51.71878-15/642489697_931785695971440_3837333144664180149_n.jpg?stp=dst-jpg_e15_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi42NDB4MTEzNi5zZHIuZjcxODc4Lm5mcmFtZV9jb3Zlcl9mcmFtZS5jMiJ9&_nc_ht=scontent-phl2-1.cdninstagram.com&_nc_cat=100&_nc_oc=Q6cZ2QH2Km-HWtG_kFjSkWI-wtXI14TUgdgZN3CffFjRE0mZMwRZwsr6ISXIttcetnv45fU&_nc_ohc=ld-onItfzFIQ7kNvwEGAIZT&_nc_gid=1nVoOKHoCkOl8-av4Iwgkg&edm=ANTKIIoBAAAA&ccb=7-5&oh=00_Afz7i42LKF1TExXZOoZv8OQ6YEd-kZEdzAyk_rUMlaztEw&oe=69BD27F2&_nc_sid=d885a2",
      "shortcode": "DVNLU52gCAP",
      "content_id": "3840775872235708431_497234441_497234441",
      "product_type": "clips",
      "coauthor_producers": [],
      "tagged_users": [],
      "length": "15.033",
      "video_url": "https://scontent-phl2-1.cdninstagram.com/o1/v/t16/f2/m69/AQO1SuMyUcs1QWW58Fau44ndzK-6SmNd445DizWdt8WagvA2o9UAYpZcn6CfH_Wp3E9pH-k4PDImZiE6IJf87aVm.mp4?strext=1&_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-phl2-1.cdninstagram.com&_nc_ohc=fra74Acli5UQ7kNvwG-BbIe&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NDkxMzUwMjQxMDE5MjYsImFzc2V0X2FnZV9kYXlzIjoxNywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjE1LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=2267dea350fbd465&_nc_vs=HBksFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HSFE0LXlXa1JiMzJYa3dEQU9yaEtYTkZyOHRxYnNwVEFRQUYVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0ZDNENBQjg2Q0VFNTU3RkU5NDZBQUYzNTNGNDFGNkI3X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbM6JiSlaniPxUCKAJDMywXQC4Q5WBBiTcYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=1nVoOKHoCkOl8-av4Iwgkg&_nc_ss=8&_nc_zt=28&oh=00_Afws7Cm4DuKLxHAjheCqUW1fe2al52lZbgUNRHbiXa_H0g&oe=69BD1196",
      "audio_url": "https://www.instagram.com/reels/audio/613780965138542",
      "posts_count": 2319,
      "followers": 94671,
      "following": null,
      "user_profile_url": "htt***//w***ins*********m/l*********",
      "is_paid_partnership": false,
      "is_verified": true,
      "profile_image_link": "https://scontent-mia5-1.cdninstagram.com/v/t51.82787-19/523513088_18520152235018442_1378657946459904137_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-mia5-1.cdninstagram.com&_nc_cat=102&_nc_oc=Q6cZ2QEI4iViNi0YUmtNR4gwjlifNoniCz1nfEs1XGRXQW5VtoNDlwCKdVe_ayxZrKVC3JI&_nc_ohc=jOf5V5nROFYQ7kNvwFvWJah&_nc_gid=2ag63x5Aw5-NL2Fq6v6jhw&edm=APs17CUBAAAA&ccb=7-5&oh=00_Afy_XwPZFp_gUapVcrmQwXkvlRmt0xThqroTeB2ERmWtBQ&oe=69BD0AE6&_nc_sid=10d13b"
    }
  ]
  ```
</ResponseExample>


## OpenAPI

````yaml api-reference/sdk-specs/instagram-reels-collect-by-url POST /datasets/v3/scrape
openapi: 3.0.0
info:
  title: Collect Reels by URL
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security: []
paths:
  /datasets/v3/scrape:
    post:
      summary: Collect Reels by URL
      description: >-
        Use the Bright Data Web Scraper API to collect Reels by URL. POST
        /datasets/v3/scrape starts a scraping job that returns the data as
        structured JSON records.
      parameters:
        - in: query
          name: dataset_id
          required: true
          schema:
            type: string
            default: gd_lyclm20il4r5helnj
          description: Must be `gd_lyclm20il4r5helnj` for this dataset.
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
                        example: https://www.instagram.com/reel/C5Rdyj_q7YN/
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
              --url 'https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lyclm20il4r5helnj&include_errors=true' \
              --header "Authorization: Bearer YOUR_API_KEY" \
              --header "Content-Type: application/json" \
              --data '{"input": [{"url": "https://www.instagram.com/reel/C5Rdyj_q7YN/"}, {"url": "https://www.instagram.com/reel/C85BZjeSHuO"}]}'
        - lang: python
          label: Python
          source: >-
            import requests


            url =
            "https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lyclm20il4r5helnj&include_errors=true"

            headers = {
                "Authorization": "Bearer YOUR_API_KEY",
                "Content-Type": "application/json",
            }

            payload = {
                "input": [
                    {
                        "url": "https://www.instagram.com/reel/C5Rdyj_q7YN/"
                    },
                    {
                        "url": "https://www.instagram.com/reel/C85BZjeSHuO"
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
                result = await client.scrape.instagram.reels(url="https://www.instagram.com/reel/C5Rdyj_q7YN/")
                print(result.data)
        - lang: javascript
          label: JavaScript
          source: >-
            const response = await
            fetch("https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lyclm20il4r5helnj&include_errors=true",
            {
              method: "POST",
              headers: {
                "Authorization": "Bearer YOUR_API_KEY",
                "Content-Type": "application/json",
              },
              body: JSON.stringify({
                "input": [
                    {
                        "url": "https://www.instagram.com/reel/C5Rdyj_q7YN/"
                    },
                    {
                        "url": "https://www.instagram.com/reel/C85BZjeSHuO"
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
            client.scrape.instagram.collectReels(['https://www.instagram.com/reel/C5Rdyj_q7YN/']);

            console.log(result);


            await client.close();
        - lang: php
          label: PHP
          source: >-
            <?php

            $ch =
            curl_init("https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lyclm20il4r5helnj&include_errors=true");

            curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");

            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

            curl_setopt($ch, CURLOPT_HTTPHEADER, [
                "Authorization: Bearer YOUR_API_KEY",
                "Content-Type: application/json",
            ]);

            curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode([
                "input" => [
                    [
                        "url" => "https://www.instagram.com/reel/C5Rdyj_q7YN/"
                    ],
                    [
                        "url" => "https://www.instagram.com/reel/C85BZjeSHuO"
                    ]
                ]
            ]));


            $response = curl_exec($ch);

            curl_close($ch);

            echo $response;
        - lang: go
          label: Go
          source: "package main\n\nimport (\n\t\"bytes\"\n\t\"fmt\"\n\t\"io\"\n\t\"net/http\"\n)\n\nfunc main() {\n\tpayload := []byte(\"{\\\"input\\\": [{\\\"url\\\": \\\"https://www.instagram.com/reel/C5Rdyj_q7YN/\\\"}, {\\\"url\\\": \\\"https://www.instagram.com/reel/C85BZjeSHuO\\\"}]}\")\n\treq, _ := http.NewRequest(\"POST\", \"https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lyclm20il4r5helnj&include_errors=true\", bytes.NewBuffer(payload))\n\treq.Header.Set(\"Authorization\", \"Bearer YOUR_API_KEY\")\n\treq.Header.Set(\"Content-Type\", \"application/json\")\n\n\tres, err := http.DefaultClient.Do(req)\n\tif err != nil { panic(err) }\n\tdefer res.Body.Close()\n\n\tbody, _ := io.ReadAll(res.Body)\n\tfmt.Println(string(body))\n}"
        - lang: java
          label: Java
          source: |-
            import java.net.URI;
            import java.net.http.HttpClient;
            import java.net.http.HttpRequest;
            import java.net.http.HttpResponse;

            public class Main {
                public static void main(String[] args) throws Exception {
                    String body = "{\"input\": [{\"url\": \"https://www.instagram.com/reel/C5Rdyj_q7YN/\"}, {\"url\": \"https://www.instagram.com/reel/C85BZjeSHuO\"}]}";
                    HttpRequest request = HttpRequest.newBuilder()
                        .uri(URI.create("https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lyclm20il4r5helnj&include_errors=true"))
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
            URI.parse("https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lyclm20il4r5helnj&include_errors=true")

            request = Net::HTTP::Post.new(uri)

            request["Authorization"] = "Bearer YOUR_API_KEY"

            request["Content-Type"] = "application/json"

            request.body = {"input": [{"url":
            "https://www.instagram.com/reel/C5Rdyj_q7YN/"}, {"url":
            "https://www.instagram.com/reel/C85BZjeSHuO"}]}.to_json


            response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) {
            |http| http.request(request) }

            puts response.body

````