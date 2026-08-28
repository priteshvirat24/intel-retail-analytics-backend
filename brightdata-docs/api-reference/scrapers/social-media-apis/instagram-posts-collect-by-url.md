> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Collect Instagram posts by URL

> Use the Bright Data Web Scraper API to collect Instagram posts by URL. Calls the POST /datasets/v3/scrape endpoint and returns a snapshot ID.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_lk5ns7kz21pck8jpis" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_lk5ns7kz21pck8jpis` to collect **Posts by URL** data.
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
      The URL of the Instagram posts to collect.
    </ParamField>
  </Expandable>

  #### Example

  ```json wrap theme={null}
  {
    "input": [
      {"url":"https://www.instagram.com/p/Cuf4s0MNqNr"},
      {"url":"https://www.instagram.com/p/DP861NijuwE"}
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "url": "https://www.instagram.com/p/DIWPWGpsUQX",
      "user_posted": "limabijus",
      "description": "Coleção Laços 💝 Argolinhas cravejadas com micro zircônias em cores R$35,00\n\nParcelamos suas compras em até 12x no cartão \n\nFRETE FIXO PARA TODO PARÁ R$13,00 FRETE FIXO PARA TODO O BRASIL R$27,00\n\nCatálogo no link da bio.\n\n*Aceitamos todos os cartões\n*Pix\n\nLoja aberta das 08:00 as 18:30 Trav. Oriental do mercado. Rua ao lado da antiga Big Ben\n\n#açoinoxidável #açocirurgico #colarfolheado #joia",
      "hashtags": [
        "#a",
        "#a",
        "#colarfolheado",
        "#joia"
      ],
      "num_comments": 0,
      "date_posted": "2025-04-12T13:03:14.000Z",
      "likes": 51,
      "photos": [
        "https://scontent-dfw5-2.cdninstagram.com/v/t51.2885-15/489610375_18494864488028192_2686112351885091669_n.jpg?stp=dst-jpg_e35_p1080x1080_sh0.08_tt6&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2QGaMKgfOzjq0wPKSDzaCmtVKzedbmcC6K7R8nhooYRtxVg3ff27v7SxrDXsxdo2W7k&_nc_ohc=0MufbR7woQgQ7kNvwFygZL-&_nc_gid=nqIS79fttxt1Dm7FA1KvtA&edm=ANTKIIoBAAAA&ccb=7-5&oh=00_AfzNULCN5FUuEctA0H8JoRjWCeySVi7on4V_3tyVANwEgA&oe=69BD2DFE&_nc_sid=d885a2",
        "https://scontent-dfw5-2.cdninstagram.com/v/t51.2885-15/490407159_18494864497028192_459288836599671444_n.jpg?stp=dst-jpg_e35_p1080x1080_sh0.08_tt6&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2QGaMKgfOzjq0wPKSDzaCmtVKzedbmcC6K7R8nhooYRtxVg3ff27v7SxrDXsxdo2W7k&_nc_ohc=8c3OWbQMg_UQ7kNvwGA-4tO&_nc_gid=nqIS79fttxt1Dm7FA1KvtA&edm=ANTKIIoBAAAA&ccb=7-5&oh=00_AfzoD8Lfn2JLSIGWOpgggWRS0lM_Nq-kBOJbsWniZW1-Pg&oe=69BD36E2&_nc_sid=d885a2",
        "https://scontent-dfw5-2.cdninstagram.com/v/t51.2885-15/489022963_18494864506028192_5811983443590937317_n.jpg?stp=dst-jpg_e35_p1080x1080_sh0.08_tt6&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2QGaMKgfOzjq0wPKSDzaCmtVKzedbmcC6K7R8nhooYRtxVg3ff27v7SxrDXsxdo2W7k&_nc_ohc=dmtlFzwSrRAQ7kNvwF3cFW1&_nc_gid=nqIS79fttxt1Dm7FA1KvtA&edm=ANTKIIoBAAAA&ccb=7-5&oh=00_AfxkO5-J0PJ3blG-0l-j2FfZ8JbfvEFMNlkjuFfGyTcbDw&oe=69BD411D&_nc_sid=d885a2",
        "https://scontent-dfw5-2.cdninstagram.com/v/t51.2885-15/490092032_18494864515028192_1690521244685472282_n.jpg?stp=dst-jpg_e35_p1080x1080_sh0.08_tt6&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2QGaMKgfOzjq0wPKSDzaCmtVKzedbmcC6K7R8nhooYRtxVg3ff27v7SxrDXsxdo2W7k&_nc_ohc=qBpqqD5ZCl0Q7kNvwEDczAS&_nc_gid=nqIS79fttxt1Dm7FA1KvtA&edm=ANTKIIoBAAAA&ccb=7-5&oh=00_AfxTqMfbDWwQY0NuZGyko_XxDlqKSGGZhgNQiSpZOjQnTA&oe=69BD3BB2&_nc_sid=d885a2"
      ],
      "videos": null,
      "location": [
        "Capanema",
        "Pará",
        "Brasil"
      ],
      "latest_comments": null,
      "post_id": "3609139641052120087",
      "discovery_input": null,
      "has_handshake": null,
      "shortcode": "DIWPWGpsUQX",
      "content_type": "Carousel",
      "pk": "3609139641052120087",
      "content_id": "DIWPWGpsUQX",
      "engagement_score_view": null,
      "thumbnail": "https://scontent-dfw5-2.cdninstagram.com/v/t51.2885-15/489610375_18494864488028192_2686112351885091669_n.jpg?stp=c0.147.1284.1284a_dst-jpg_e35_s640x640_sh0.08_tt6&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2QGaMKgfOzjq0wPKSDzaCmtVKzedbmcC6K7R8nhooYRtxVg3ff27v7SxrDXsxdo2W7k&_nc_ohc=0MufbR7woQgQ7kNvwFygZL-&_nc_gid=nqIS79fttxt1Dm7FA1KvtA&edm=ANTKIIoBAAAA&ccb=7-5&oh=00_AfxVSxvfL2zQbtGYyRFK9C75gO2TcK0jY6bsl6Xo1WM0dA&oe=69BD2DFE&_nc_sid=d885a2",
      "video_view_count": null,
      "product_type": null,
      "coauthor_producers": null,
      "tagged_users": null,
      "video_play_count": null,
      "followers": 20674,
      "posts_count": 9676,
      "profile_image_link": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/637167000_18562755475028192_7282452674783054648_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2QGaMKgfOzjq0wPKSDzaCmtVKzedbmcC6K7R8nhooYRtxVg3ff27v7SxrDXsxdo2W7k&_nc_ohc=w2D-l-4t3yAQ7kNvwG5fhmo&_nc_gid=nqIS79fttxt1Dm7FA1KvtA&edm=ANTKIIoBAAAA&ccb=7-5&oh=00_AfwK9IApnYM8GUqE3WY6EC9TiyKRaRbL6JS9314NMLywrQ&oe=69BD3DFE&_nc_sid=d885a2",
      "is_verified": true,
      "is_paid_partnership": false,
      "partnership_details": {
        "profile_id": null,
        "profile_url": null,
        "username": null
      },
      "user_posted_id": "312860191",
      "post_content": [
        {
          "alt_text": "Photo by Lima Bijus on April 12, 2025.",
          "id": "3609139634257469948",
          "index": 0,
          "type": "Photo",
          "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.2885-15/489610375_18494864488028192_2686112351885091669_n.jpg?stp=dst-jpg_e35_p1080x1080_sh0.08_tt6&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2QGaMKgfOzjq0wPKSDzaCmtVKzedbmcC6K7R8nhooYRtxVg3ff27v7SxrDXsxdo2W7k&_nc_ohc=0MufbR7woQgQ7kNvwFygZL-&_nc_gid=nqIS79fttxt1Dm7FA1KvtA&edm=ANTKIIoBAAAA&ccb=7-5&oh=00_AfzNULCN5FUuEctA0H8JoRjWCeySVi7on4V_3tyVANwEgA&oe=69BD2DFE&_nc_sid=d885a2"
        },
        {
          "alt_text": "Photo by Lima Bijus on April 12, 2025.",
          "id": "3609139634265835747",
          "index": 1,
          "type": "Photo",
          "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.2885-15/490407159_18494864497028192_459288836599671444_n.jpg?stp=dst-jpg_e35_p1080x1080_sh0.08_tt6&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2QGaMKgfOzjq0wPKSDzaCmtVKzedbmcC6K7R8nhooYRtxVg3ff27v7SxrDXsxdo2W7k&_nc_ohc=8c3OWbQMg_UQ7kNvwGA-4tO&_nc_gid=nqIS79fttxt1Dm7FA1KvtA&edm=ANTKIIoBAAAA&ccb=7-5&oh=00_AfzoD8Lfn2JLSIGWOpgggWRS0lM_Nq-kBOJbsWniZW1-Pg&oe=69BD36E2&_nc_sid=d885a2"
        },
        {
          "alt_text": "Photo by Lima Bijus on April 12, 2025.",
          "id": "3609139634257389672",
          "index": 2,
          "type": "Photo",
          "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.2885-15/489022963_18494864506028192_5811983443590937317_n.jpg?stp=dst-jpg_e35_p1080x1080_sh0.08_tt6&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2QGaMKgfOzjq0wPKSDzaCmtVKzedbmcC6K7R8nhooYRtxVg3ff27v7SxrDXsxdo2W7k&_nc_ohc=dmtlFzwSrRAQ7kNvwF3cFW1&_nc_gid=nqIS79fttxt1Dm7FA1KvtA&edm=ANTKIIoBAAAA&ccb=7-5&oh=00_AfxkO5-J0PJ3blG-0l-j2FfZ8JbfvEFMNlkjuFfGyTcbDw&oe=69BD411D&_nc_sid=d885a2"
        },
        {
          "alt_text": "Photo by Lima Bijus on April 12, 2025.",
          "id": "3609139634257475832",
          "index": 3,
          "type": "Photo",
          "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.2885-15/490092032_18494864515028192_1690521244685472282_n.jpg?stp=dst-jpg_e35_p1080x1080_sh0.08_tt6&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2QGaMKgfOzjq0wPKSDzaCmtVKzedbmcC6K7R8nhooYRtxVg3ff27v7SxrDXsxdo2W7k&_nc_ohc=qBpqqD5ZCl0Q7kNvwEDczAS&_nc_gid=nqIS79fttxt1Dm7FA1KvtA&edm=ANTKIIoBAAAA&ccb=7-5&oh=00_AfxTqMfbDWwQY0NuZGyko_XxDlqKSGGZhgNQiSpZOjQnTA&oe=69BD3BB2&_nc_sid=d885a2"
        }
      ],
      "audio": {
        "audio_asset_id": null,
        "ig_artist_id": null,
        "ig_artist_username": null,
        "original_audio_title": null
      },
      "profile_url": "https://www.instagram.com/limabijus",
      "videos_duration": null,
      "images": [
        {
          "id": "360***963***746******",
          "url": "htt***//s***ten*********cdn*********************885************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************"
        },
        {
          "id": "360***963***583******",
          "url": "htt***//s***ten*********cdn*********************885************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************"
        },
        {
          "id": "360***963***738******",
          "url": "htt***//s***ten*********cdn*********************885************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************"
        },
        {
          "id": "360***963***747******",
          "url": "htt***//s***ten*********cdn*********************885************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************"
        }
      ],
      "alt_text": "Photo by Lima Bijus on April 12, 2025.",
      "photos_number": 4,
      "audio_url": null
    }
  ]
  ```
</ResponseExample>


## OpenAPI

````yaml api-reference/sdk-specs/instagram-posts-collect-by-url POST /datasets/v3/scrape
openapi: 3.0.0
info:
  title: Collect Instagram posts by URL
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security: []
paths:
  /datasets/v3/scrape:
    post:
      summary: Collect Instagram posts by URL
      description: >-
        Use the Bright Data Web Scraper API to collect Instagram posts by URL.
        Submit one request and retrieve structured JSON records when the
        snapshot completes.
      parameters:
        - in: query
          name: dataset_id
          required: true
          schema:
            type: string
            default: gd_lk5ns7kz21pck8jpis
          description: Must be `gd_lk5ns7kz21pck8jpis` for this dataset.
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
                        example: https://www.instagram.com/p/Cuf4s0MNqNr
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
              --url 'https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lk5ns7kz21pck8jpis&include_errors=true' \
              --header "Authorization: Bearer YOUR_API_KEY" \
              --header "Content-Type: application/json" \
              --data '{"input": [{"url": "https://www.instagram.com/p/Cuf4s0MNqNr"}, {"url": "https://www.instagram.com/p/DP861NijuwE"}]}'
        - lang: python
          label: Python
          source: >-
            import requests


            url =
            "https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lk5ns7kz21pck8jpis&include_errors=true"

            headers = {
                "Authorization": "Bearer YOUR_API_KEY",
                "Content-Type": "application/json",
            }

            payload = {
                "input": [
                    {
                        "url": "https://www.instagram.com/p/Cuf4s0MNqNr"
                    },
                    {
                        "url": "https://www.instagram.com/p/DP861NijuwE"
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
                result = await client.scrape.instagram.posts(url="https://www.instagram.com/p/Cuf4s0MNqNr")
                print(result.data)
        - lang: javascript
          label: JavaScript
          source: >-
            const response = await
            fetch("https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lk5ns7kz21pck8jpis&include_errors=true",
            {
              method: "POST",
              headers: {
                "Authorization": "Bearer YOUR_API_KEY",
                "Content-Type": "application/json",
              },
              body: JSON.stringify({
                "input": [
                    {
                        "url": "https://www.instagram.com/p/Cuf4s0MNqNr"
                    },
                    {
                        "url": "https://www.instagram.com/p/DP861NijuwE"
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
            client.scrape.instagram.collectPosts(['https://www.instagram.com/p/Cuf4s0MNqNr']);

            console.log(result);


            await client.close();
        - lang: php
          label: PHP
          source: >-
            <?php

            $ch =
            curl_init("https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lk5ns7kz21pck8jpis&include_errors=true");

            curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");

            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

            curl_setopt($ch, CURLOPT_HTTPHEADER, [
                "Authorization: Bearer YOUR_API_KEY",
                "Content-Type: application/json",
            ]);

            curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode([
                "input" => [
                    [
                        "url" => "https://www.instagram.com/p/Cuf4s0MNqNr"
                    ],
                    [
                        "url" => "https://www.instagram.com/p/DP861NijuwE"
                    ]
                ]
            ]));


            $response = curl_exec($ch);

            curl_close($ch);

            echo $response;
        - lang: go
          label: Go
          source: "package main\n\nimport (\n\t\"bytes\"\n\t\"fmt\"\n\t\"io\"\n\t\"net/http\"\n)\n\nfunc main() {\n\tpayload := []byte(\"{\\\"input\\\": [{\\\"url\\\": \\\"https://www.instagram.com/p/Cuf4s0MNqNr\\\"}, {\\\"url\\\": \\\"https://www.instagram.com/p/DP861NijuwE\\\"}]}\")\n\treq, _ := http.NewRequest(\"POST\", \"https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lk5ns7kz21pck8jpis&include_errors=true\", bytes.NewBuffer(payload))\n\treq.Header.Set(\"Authorization\", \"Bearer YOUR_API_KEY\")\n\treq.Header.Set(\"Content-Type\", \"application/json\")\n\n\tres, err := http.DefaultClient.Do(req)\n\tif err != nil { panic(err) }\n\tdefer res.Body.Close()\n\n\tbody, _ := io.ReadAll(res.Body)\n\tfmt.Println(string(body))\n}"
        - lang: java
          label: Java
          source: |-
            import java.net.URI;
            import java.net.http.HttpClient;
            import java.net.http.HttpRequest;
            import java.net.http.HttpResponse;

            public class Main {
                public static void main(String[] args) throws Exception {
                    String body = "{\"input\": [{\"url\": \"https://www.instagram.com/p/Cuf4s0MNqNr\"}, {\"url\": \"https://www.instagram.com/p/DP861NijuwE\"}]}";
                    HttpRequest request = HttpRequest.newBuilder()
                        .uri(URI.create("https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lk5ns7kz21pck8jpis&include_errors=true"))
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
            URI.parse("https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lk5ns7kz21pck8jpis&include_errors=true")

            request = Net::HTTP::Post.new(uri)

            request["Authorization"] = "Bearer YOUR_API_KEY"

            request["Content-Type"] = "application/json"

            request.body = {"input": [{"url":
            "https://www.instagram.com/p/Cuf4s0MNqNr"}, {"url":
            "https://www.instagram.com/p/DP861NijuwE"}]}.to_json


            response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) {
            |http| http.request(request) }

            puts response.body

````