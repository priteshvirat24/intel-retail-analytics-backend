> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Collect LinkedIn posts by URL

> Use the Bright Data Web Scraper API to collect LinkedIn Posts by URL. Calls the POST /datasets/v3/scrape endpoint and returns a snapshot ID.

## Query Parameters

<ParamField query="dataset_id" type="string" default="gd_lyy3tktm25m4avu764" required>
  The dataset ID used for this request.

  <Warning>
    Must be set to `gd_lyy3tktm25m4avu764` to collect **Posts by URL** data.
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
      The URL of the LinkedIn post to collect.
    </ParamField>
  </Expandable>

  #### Example

  ```json theme={null}
  {
    "input":[
      {"url":"https://www.linkedin.com/pulse/ab-test-optimisation-earlier-decisions-new-readout-de-b%C3%A9naz%C3%A9?trk=public_profile_article_view"},
      {"url":"https://www.linkedin.com/posts/orlenchner_scrapecon-activity-7180537307521769472-oSYN?trk=public_profile"},
      {"url":"https://www.linkedin.com/posts/karin-dodis_web-data-collection-for-businesses-bright-activity-7176601589682434049-Aakz?trk=public_profile"},
      {"url":"https://www.linkedin.com/pulse/getting-value-out-sunburst-guillaume-de-b%C3%A9naz%C3%A9?trk=public_profile_article_view"}
    ]
  }
  ```
</ParamField>

<ResponseExample>
  ```json 200 theme={null}
  [
    {
      "url": "https://de.linkedin.com/posts/bathildisheim_sport-inklusion-sportf%C3%BCralle-activity-7439619065922625537-K5QL",
      "id": "7439619065922625537",
      "user_id": "bat***dis***m",
      "use_url": "https://de.linkedin.com/company/bathildisheim?trk=public_post_feed-actor-image",
      "title": "#sp*** #i***usi*********für*********************weg************************",
      "headline": "Aus***chn*** fü********* Vi******************",
      "post_text": "Auszeichnung für gelebte Vielfalt im #Sport . Das Projekt Miteinander bewegt ist gemeinsam mit dem VfL Bad Wildungen mit dem Sonderpreis „Ländlicher Raum“ der Demokratie-Verstärker:innen ausgezeichnet worden. Verliehen wurde der Preis im Rahmen der Initiative „Offen für Vielfalt – Geschlossen gegen Ausgrenzung“ im Regierungspräsidium Kassel. Gewürdigt wurde das gemeinsame Projekt „Boxen ist für alle da“, das seit knapp einem Jahr im Landkreis Waldeck-Frankenberg angeboten wird. Die Auszeichnung macht sichtbar, was das Projekt in der Praxis zeigt: Sport ist weit mehr als Bewegung. Sport schafft Begegnung, stärkt Selbstvertrauen und verbindet Menschen mit unterschiedlichen Voraussetzungen. Gerade deshalb ist es wichtig, dass sportliche Angebote allen offenstehen. Bei „Boxen ist für alle da“ trainieren Menschen mit und ohne Behinderung gemeinsam. So entstehen nicht nur sportliche Erfahrungen, sondern auch Teilhabe, Zusammenhalt und ein selbstverständliches Miteinander. Dass dieses Engagement nun besonders für den ländlichen Raum gewürdigt wird, ist ein starkes Zeichen. Die Freude über den Preis ist groß. Denn er würdigt den gemeinsamen Einsatz für Inklusion, Vielfalt und demokratisches Miteinander im Sport. Ein herzlicher Dank gilt allen Beteiligten, Unterstützer:innen und natürlich den Teilnehmenden, die dieses Projekt mit Leben füllen. #Inklusion #SportFürAlle #bathildisheimbewegt Sebastian Gleim",
      "date_posted": "2026-03-17T10:30:06.724Z",
      "hashtags": [
        "#Sport",
        "#Inklusion",
        "#SportFürAlle",
        "#bathildisheimbewegt"
      ],
      "embedded_links": [
        "https://www.linkedin.com/feed/hashtag/sport",
        "https://www.linkedin.com/feed/hashtag/inklusion",
        "https://www.linkedin.com/feed/hashtag/sportfAeSralle",
        "https://www.linkedin.com/feed/hashtag/bathildisheimbewegt",
        "https://de.linkedin.com/in/sebastian-gleim-47063430a?trk=public_post-text"
      ],
      "images": [
        "https://media.licdn.com/dms/image/v2/D4D22AQGI_ALONwR9og/feedshare-shrink_800/B4DZz7WHjuKQAg-/0/1773743405596?e=2147483647&v=beta&t=dXPqg2rYvo3UwNHHx-irACA7lQ7GWovL4egJ3smyH3o"
      ],
      "videos": null,
      "num_likes": 2,
      "num_comments": 0,
      "more_articles_by_user": null,
      "more_relevant_posts": null,
      "top_visible_comments": null,
      "user_followers": 412,
      "user_posts": 0,
      "user_articles": 0,
      "post_type": "post",
      "account_type": "Organization",
      "post_text_html": "Auszeichnung für gelebte Vielfalt im <a class=\"link\" href=\"https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fsport&amp;trk=public_post-text\" target=\"_self\" data-tracking-control-name=\"public_post-text\" data-tracking-will-navigate>#Sport</a>. Das Projekt Miteinander bewegt ist gemeinsam mit dem VfL Bad Wildungen mit dem Sonderpreis „Ländlicher Raum“ der Demokratie-Verstärker:innen ausgezeichnet worden. Verliehen wurde der Preis im Rahmen der Initiative „Offen für Vielfalt – Geschlossen gegen Ausgrenzung“ im Regierungspräsidium Kassel.<br/>Gewürdigt wurde das gemeinsame Projekt „Boxen ist für alle da“, das seit knapp einem Jahr im Landkreis Waldeck-Frankenberg angeboten wird.<br/><br/>Die Auszeichnung macht sichtbar, was das Projekt in der Praxis zeigt: Sport ist weit mehr als Bewegung. Sport schafft Begegnung, stärkt Selbstvertrauen und verbindet Menschen mit unterschiedlichen Voraussetzungen. Gerade deshalb ist es wichtig, dass sportliche Angebote allen offenstehen.<br/><br/>Bei „Boxen ist für alle da“ trainieren Menschen mit und ohne Behinderung gemeinsam. So entstehen nicht nur sportliche Erfahrungen, sondern auch Teilhabe, Zusammenhalt und ein selbstverständliches Miteinander. Dass dieses Engagement nun besonders für den ländlichen Raum gewürdigt wird, ist ein starkes Zeichen.<br/>Die Freude über den Preis ist groß. Denn er würdigt den gemeinsamen Einsatz für Inklusion, Vielfalt und demokratisches Miteinander im Sport.<br/>Ein herzlicher Dank gilt allen Beteiligten, Unterstützer:innen und natürlich den Teilnehmenden, die dieses Projekt mit Leben füllen.<br/><br/><a class=\"link\" href=\"https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Finklusion&amp;trk=public_post-text\" target=\"_self\" data-tracking-control-name=\"public_post-text\" data-tracking-will-navigate>#Inklusion</a> <a class=\"link\" href=\"https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2FsportfAeSralle&amp;trk=public_post-text\" target=\"_self\" data-tracking-control-name=\"public_post-text\" data-tracking-will-navigate>#SportFürAlle</a> <a class=\"link\" href=\"https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fbathildisheimbewegt&amp;trk=public_post-text\" target=\"_self\" data-tracking-control-name=\"public_post-text\" data-tracking-will-navigate>#bathildisheimbewegt</a> <a class=\"link\" href=\"https://de.linkedin.com/in/sebastian-gleim-47063430a?trk=public_post-text\" target=\"_self\" data-tracking-control-name=\"public_post-text\" data-tracking-will-navigate>Sebastian Gleim</a>",
      "repost": null,
      "tagged_companies": [],
      "tagged_people": [
        {
          "link": "https://de.linkedin.com/in/sebastian-gleim-47063430a?trk=public_post-text",
          "name": "Sebastian G***m",
          "type": "people"
        }
      ],
      "user_title": null,
      "author_profile_pic": "htt***//m***a.l*********dms*********************mzL************************************************************************************************************************************************************",
      "num_connections": null,
      "video_duration": null,
      "external_link_data": null,
      "video_thumbnail": null,
      "document_cover_image": null,
      "document_page_count": null,
      "original_post_text": "Auszeichnung für gelebte Vielfalt im <a class=\"link\" href=\"https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fsport&amp;trk=public_post-text\" target=\"_self\" data-tracking-control-name=\"public_post-text\" data-tracking-will-navigate>#Sport</a>. Das Projekt Miteinander bewegt ist gemeinsam mit dem VfL Bad Wildungen mit dem Sonderpreis „Ländlicher Raum“ der Demokratie-Verstärker:innen ausgezeichnet worden. Verliehen wurde der Preis im Rahmen der Initiative „Offen für Vielfalt – Geschlossen gegen Ausgrenzung“ im Regierungspräsidium Kassel.\nGewürdigt wurde das gemeinsame Projekt „Boxen ist für alle da“, das seit knapp einem Jahr im Landkreis Waldeck-Frankenberg angeboten wird.\n\nDie Auszeichnung macht sichtbar, was das Projekt in der Praxis zeigt: Sport ist weit mehr als Bewegung. Sport schafft Begegnung, stärkt Selbstvertrauen und verbindet Menschen mit unterschiedlichen Voraussetzungen. Gerade deshalb ist es wichtig, dass sportliche Angebote allen offenstehen.\n\nBei „Boxen ist für alle da“ trainieren Menschen mit und ohne Behinderung gemeinsam. So entstehen nicht nur sportliche Erfahrungen, sondern auch Teilhabe, Zusammenhalt und ein selbstverständliches Miteinander. Dass dieses Engagement nun besonders für den ländlichen Raum gewürdigt wird, ist ein starkes Zeichen.\nDie Freude über den Preis ist groß. Denn er würdigt den gemeinsamen Einsatz für Inklusion, Vielfalt und demokratisches Miteinander im Sport.\nEin herzlicher Dank gilt allen Beteiligten, Unterstützer:innen und natürlich den Teilnehmenden, die dieses Projekt mit Leben füllen.\n\n<a class=\"link\" href=\"https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Finklusion&amp;trk=public_post-text\" target=\"_self\" data-tracking-control-name=\"public_post-text\" data-tracking-will-navigate>#Inklusion</a> <a class=\"link\" href=\"https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2FsportfAeSralle&amp;trk=public_post-text\" target=\"_self\" data-tracking-control-name=\"public_post-text\" data-tracking-will-navigate>#SportFürAlle</a> <a class=\"link\" href=\"https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fbathildisheimbewegt&amp;trk=public_post-text\" target=\"_self\" data-tracking-control-name=\"public_post-text\" data-tracking-will-navigate>#bathildisheimbewegt</a> <a class=\"link\" href=\"https://de.linkedin.com/in/sebastian-gleim-47063430a?trk=public_post-text\" target=\"_self\" data-tracking-control-name=\"public_post-text\" data-tracking-will-navigate>Sebastian Gleim</a>"
    }
  ]
  ```
</ResponseExample>


## OpenAPI

````yaml api-reference/sdk-specs/linkedin-posts-collect-by-url POST /datasets/v3/scrape
openapi: 3.0.0
info:
  title: Collect LinkedIn Posts by URL
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security: []
paths:
  /datasets/v3/scrape:
    post:
      summary: Collect LinkedIn Posts by URL
      description: >-
        Use the Bright Data Web Scraper API to collect LinkedIn Posts by URL.
        Submit one request and retrieve structured JSON records when the
        snapshot completes.
      parameters:
        - in: query
          name: dataset_id
          required: true
          schema:
            type: string
            default: gd_lyy3tktm25m4avu764
          description: Must be `gd_lyy3tktm25m4avu764` for this dataset.
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
                        example: >-
                          https://www.linkedin.com/feed/update/urn:li:activity:123
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
              --url 'https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lyy3tktm25m4avu764&include_errors=true' \
              --header "Authorization: Bearer YOUR_API_KEY" \
              --header "Content-Type: application/json" \
              --data '{"input": [{"url": "https://www.linkedin.com/feed/update/urn:li:activity:123"}]}'
        - lang: python
          label: Python
          source: >-
            import requests


            url =
            "https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lyy3tktm25m4avu764&include_errors=true"

            headers = {
                "Authorization": "Bearer YOUR_API_KEY",
                "Content-Type": "application/json",
            }

            payload = {
                "input": [
                    {
                        "url": "https://www.linkedin.com/feed/update/urn:li:activity:123"
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
                result = await client.scrape.linkedin.posts(url="https://www.linkedin.com/feed/update/urn:li:activity:123")
                print(result.data)
        - lang: javascript
          label: JavaScript
          source: >-
            const response = await
            fetch("https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lyy3tktm25m4avu764&include_errors=true",
            {
              method: "POST",
              headers: {
                "Authorization": "Bearer YOUR_API_KEY",
                "Content-Type": "application/json",
              },
              body: JSON.stringify({
                "input": [
                    {
                        "url": "https://www.linkedin.com/feed/update/urn:li:activity:123"
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
            client.scrape.linkedin.collectPosts(['https://www.linkedin.com/feed/update/urn:li:activity:123']);

            console.log(result);


            await client.close();
        - lang: php
          label: PHP
          source: >-
            <?php

            $ch =
            curl_init("https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lyy3tktm25m4avu764&include_errors=true");

            curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");

            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

            curl_setopt($ch, CURLOPT_HTTPHEADER, [
                "Authorization: Bearer YOUR_API_KEY",
                "Content-Type: application/json",
            ]);

            curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode([
                "input" => [
                    [
                        "url" => "https://www.linkedin.com/feed/update/urn:li:activity:123"
                    ]
                ]
            ]));


            $response = curl_exec($ch);

            curl_close($ch);

            echo $response;
        - lang: go
          label: Go
          source: "package main\n\nimport (\n\t\"bytes\"\n\t\"fmt\"\n\t\"io\"\n\t\"net/http\"\n)\n\nfunc main() {\n\tpayload := []byte(\"{\\\"input\\\": [{\\\"url\\\": \\\"https://www.linkedin.com/feed/update/urn:li:activity:123\\\"}]}\")\n\treq, _ := http.NewRequest(\"POST\", \"https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lyy3tktm25m4avu764&include_errors=true\", bytes.NewBuffer(payload))\n\treq.Header.Set(\"Authorization\", \"Bearer YOUR_API_KEY\")\n\treq.Header.Set(\"Content-Type\", \"application/json\")\n\n\tres, err := http.DefaultClient.Do(req)\n\tif err != nil { panic(err) }\n\tdefer res.Body.Close()\n\n\tbody, _ := io.ReadAll(res.Body)\n\tfmt.Println(string(body))\n}"
        - lang: java
          label: Java
          source: |-
            import java.net.URI;
            import java.net.http.HttpClient;
            import java.net.http.HttpRequest;
            import java.net.http.HttpResponse;

            public class Main {
                public static void main(String[] args) throws Exception {
                    String body = "{\"input\": [{\"url\": \"https://www.linkedin.com/feed/update/urn:li:activity:123\"}]}";
                    HttpRequest request = HttpRequest.newBuilder()
                        .uri(URI.create("https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lyy3tktm25m4avu764&include_errors=true"))
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
            URI.parse("https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_lyy3tktm25m4avu764&include_errors=true")

            request = Net::HTTP::Post.new(uri)

            request["Authorization"] = "Bearer YOUR_API_KEY"

            request["Content-Type"] = "application/json"

            request.body = {"input": [{"url":
            "https://www.linkedin.com/feed/update/urn:li:activity:123"}]}.to_json


            response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) {
            |http| http.request(request) }

            puts response.body

````