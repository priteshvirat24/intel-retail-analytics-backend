> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SERP API

> Use the Bright Data SERP API (31 languages) to extract structured results from Google, Bing, Yandex and DuckDuckGo with organic listings, ads and shopping data.

Related guide: [SERP API Introduction](/scraping-automation/serp-api/introduction)

<a href="https://www.postman.com/bright-data-api/bright-data-api/request/kpq952m/google-search" target="_blank">
  <img alt="Run in Postman" height="32" width="128" noZoom src="https://run.pstmn.io/button.svg" />
</a>

<Card title="Bright Data Python SDK" icon="python" href="/api-reference/SDK" cta="Get Started">
  For an easy start using our tools check out our new Python SDK.
</Card>


## OpenAPI

````yaml api-reference/serp-rest-api POST /request
openapi: 3.0.1
info:
  title: Brightdata SERP API
  description: >-
    Integrate Bright Data SERP APIs to your pipeline and secure high-end
    scraping precision
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
                $ref: '#/components/schemas/SuccessfulSERPResponse'
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
              --data '{"zone": "serp_api1", "url": "https://www.google.com/search?q=pizza", "format": "json"}'
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
                "zone": "serp_api1",
                "url": "https://www.google.com/search?q=pizza",
                "format": "json"
            }

            response = requests.post(url, headers=headers, json=payload)
            print(response.text)
        - lang: py
          label: Python SDK
          source: |-
            # Install: pip install brightdata-sdk
            from brightdata import BrightDataClient

            async with BrightDataClient(api_key="YOUR_API_KEY") as client:
                # Search Google, Bing or Yandex with one method call
                google = await client.search.google(query="best laptops 2026", num_results=20)
                bing   = await client.search.bing(query="python tutorial")
                yandex = await client.search.yandex(query="AI news")

                print(google.data)
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
                "zone": "serp_api1",
                "url": "https://www.google.com/search?q=pizza",
                "format": "json"
            }),
            });

            const data = await response.text();
            console.log(data);
        - lang: js
          label: JavaScript SDK
          source: |-
            // Install: npm install @brightdata/sdk
            import { bdclient } from '@brightdata/sdk';

            const client = new bdclient({ apiKey: 'YOUR_API_KEY' });

            // Search Google, Bing or Yandex with one method call
            const google = await client.search.google('best laptops 2026');
            const bing   = await client.search.bing('python tutorial');
            const yandex = await client.search.yandex('AI news');

            await client.close();
        - lang: php
          label: PHP
          source: |-
            <?php
            $ch = curl_init("https://api.brightdata.com/request");
            curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            curl_setopt($ch, CURLOPT_HTTPHEADER, [
                "Authorization: Bearer YOUR_API_KEY",
                "Content-Type: application/json",
            ]);
            curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode([
                "zone" => "serp_api1",
                "url" => "https://www.google.com/search?q=pizza",
                "format" => "json"
            ]));

            $response = curl_exec($ch);
            curl_close($ch);
            echo $response;
        - lang: go
          label: Go
          source: "package main\n\nimport (\n\t\"bytes\"\n\t\"fmt\"\n\t\"io\"\n\t\"net/http\"\n)\n\nfunc main() {\n\tpayload := []byte(\"{\\\"zone\\\": \\\"serp_api1\\\", \\\"url\\\": \\\"https://www.google.com/search?q=pizza\\\", \\\"format\\\": \\\"json\\\"}\")\n\treq, _ := http.NewRequest(\"POST\", \"https://api.brightdata.com/request\", bytes.NewBuffer(payload))\n\treq.Header.Set(\"Authorization\", \"Bearer YOUR_API_KEY\")\n\treq.Header.Set(\"Content-Type\", \"application/json\")\n\n\tres, err := http.DefaultClient.Do(req)\n\tif err != nil { panic(err) }\n\tdefer res.Body.Close()\n\n\tbody, _ := io.ReadAll(res.Body)\n\tfmt.Println(string(body))\n}"
        - lang: java
          label: Java
          source: |-
            import java.net.URI;
            import java.net.http.HttpClient;
            import java.net.http.HttpRequest;
            import java.net.http.HttpResponse;

            public class Main {
                public static void main(String[] args) throws Exception {
                    String body = "{\"zone\": \"serp_api1\", \"url\": \"https://www.google.com/search?q=pizza\", \"format\": \"json\"}";
                    HttpRequest request = HttpRequest.newBuilder()
                        .uri(URI.create("https://api.brightdata.com/request"))
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


            uri = URI.parse("https://api.brightdata.com/request")

            request = Net::HTTP::Post.new(uri)

            request["Authorization"] = "Bearer YOUR_API_KEY"

            request["Content-Type"] = "application/json"

            request.body = {"zone": "serp_api1", "url":
            "https://www.google.com/search?q=pizza", "format": "json"}.to_json


            response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) {
            |http| http.request(request) }

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
          example: serp_api1
        url:
          description: >-
            Complete target URL to scrape. Must include protocol (http/https),
            be publicly accessible.
          type: string
          example: https://www.google.com/search?q=pizza
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
    SuccessfulSERPResponse:
      type: object
      example:
        general:
          search_engine: google
          query: pizza
          results_cnt: 1200000000
          search_time: 0.45
          language: en
          location: United States
          mobile: false
          basic_view: false
          search_type: text
          page_title: pizza - Google Search
          timestamp: '2026-02-19T09:23:10.353Z'
        input:
          original_url: http://www.google.com/search?q=pizza&hl=en&gl=us
        organic:
          - link: https://www.pizzahut.com/
            source: Pizza Hut
            display_link: https://www.pizzahut.com
            title: Pizza Hut | Delivery & Carryout - No One OutPizzas The Hut!
            description: >-
              Discover classic & new menu items, find deals and enjoy seamless
              ordering for delivery and carryout. No One OutPizzas the Hut®.
            snippet_highlighted_words:
              - classic & new menu items
            icon: data:image/png;base64 ...
            image: data:image/jpeg;base64 ...
            image_alt: pizza from www.pizzahut.com
            image_base64: data:image/jpeg;base64 ...
            rank: 1
            global_rank: 4
          - link: https://www.dominos.com/
            source: Domino's
            display_link: https://www.dominos.com
            title: 'Domino''s: Pizza Delivery & Carryout, Pasta, Wings & More'
            description: >-
              Order pizza, pasta, sandwiches & more online for carryout or
              delivery from Domino's. View menu, find locations, track orders.
              Sign up for Domino's email ...
            snippet_highlighted_words:
              - >-
                Order pizza, pasta, sandwiches & more online for carryout or
                delivery
            icon: data:image/png;base64, ...
            rank: 2
            global_rank: 5
          - link: https://en.wikipedia.org/wiki/Pizza
            source: Wikipedia
            display_link: https://en.wikipedia.org › wiki › Pizza
            title: Pizza
            description: >-
              Pizza is an Italian dish typically consisting of a flat base of
              leavened wheat-based dough topped with tomato, cheese, and other
              ingredients, baked at a ...Read more
            snippet_highlighted_words:
              - >-
                an Italian dish typically consisting of a flat base of leavened
                wheat-based dough
            icon: data:image/png;base64 ...
            image: data:image/jpeg;base64 ...
            image_alt: pizza from en.wikipedia.org
            image_base64: data:image/jpeg;base64 ...
            rank: 3
            global_rank: 6
        perspectives:
          - title: Barstool Pizza Review - Flour + Water Pizzeria (San Francisco, CA)
            author: One Bite Pizza Reviews · YouTube
            source: Pizza reviews & rankings
            date: 97.3K+ views · 10 hours ago
            link: https://www.youtube.com/watch?v=7iWWdSsTI0I
            image: https://img.youtube.com/vi/7iWWdSsTI0I/hqdefault.jpg
            image_url: https://img.youtube.com/vi/7iWWdSsTI0I/hqdefault.jpg
          - title: Are there any just Sicilian style pizza places?
            author: Pizzaholics · Facebook
            source: Pizza enthusiast
            date: 8 reactions · 9 hours ago
            link: >-
              https://www.facebook.com/groups/742034912983989/posts/2424981814689282/
            image: >-
              https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTAPzkwKJX8rct5LhEtAN6p-ypb5UjDiHn0aZ8e9S6nS8tPmROY_1E2gFxXeus&usqp=CAI&s
            image_url: >-
              https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTAPzkwKJX8rct5LhEtAN6p-ypb5UjDiHn0aZ8e9S6nS8tPmROY_1E2gFxXeus&usqp=CAI&s
          - title: Top Pizza in the Bay Area
            author: Cesar Hernandez, Soleil Ho
            source: San Francisco Chronicle
            date: 2 weeks ago
            link: https://www.sfchronicle.com/projects/2023/best-pizza-sf-bay-area/
            image: >-
              https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSPGyTJpaRNE8ruXgkLdHkPFLVu5T7ykcJezvyYa07SUmrk7T0XaSntO19GBw&usqp=CAI&s
            image_url: >-
              https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSPGyTJpaRNE8ruXgkLdHkPFLVu5T7ykcJezvyYa07SUmrk7T0XaSntO19GBw&usqp=CAI&s
        knowledge:
          name: Pizza
          summary: Dish
          subtitle: Dish
        overview:
          title: Pizza
          kgmid: /m/0663v
        snack_pack_map:
          image: data:image/png;base64 ...
          image_base64: data:image/png;base64 ...
          link: >-
            https://www.google.com/search?q=pizza&sca_esv=9559f81e103ba33b&hl=en&gl=us&udm=1&lsack=fdaWadL4D5OP9u8P8LrdoAI&sa=X&ved=2ahUKEwiSq-PSneWSAxWTh_0HHXBdFyQQtgN6BAgdEAM
        snack_pack:
          - cid: '2036127367591792815'
            name: Hunt Brothers Pizza
            image: data:image/png;base64 ...
            image_base64: data:image/png;base64 ...
            reviews_cnt: 1
            type: Pizza
            price: $
            work_status: Pit stop for pizza & chicken wings
            address: Hollister, MO
            rank: 1
            global_rank: 1
        pagination:
          pages:
            - page: 2
              start: 10
              link: >-
                https://www.google.com/search?q=pizza&sca_esv=9559f81e103ba33b&hl=en&gl=us&ei=fdaWadL4D5OP9u8P8LrdoAI&start=10&sa=N&sstk=Af77f_chnDKNIlZ0IppYwCTGX-8AsCUfZH2WQB4kzsZIYRjsE5mqBJMEdWa84P7jgf603q2kg3ocZLtVg3UcaoXgLxAF8bRxzTc64g&ved=2ahUKEwiSq-PSneWSAxWTh_0HHXBdFyQQ8tMDegQICxAE
            - page: 3
              start: 20
              link: >-
                https://www.google.com/search?q=pizza&sca_esv=9559f81e103ba33b&hl=en&gl=us&ei=fdaWadL4D5OP9u8P8LrdoAI&start=20&sa=N&sstk=Af77f_chnDKNIlZ0IppYwCTGX-8AsCUfZH2WQB4kzsZIYRjsE5mqBJMEdWa84P7jgf603q2kg3ocZLtVg3UcaoXgLxAF8bRxzTc64g&ved=2ahUKEwiSq-PSneWSAxWTh_0HHXBdFyQQ8tMDegQICxAG
            - page: 4
              start: 30
              link: >-
                https://www.google.com/search?q=pizza&sca_esv=9559f81e103ba33b&hl=en&gl=us&ei=fdaWadL4D5OP9u8P8LrdoAI&start=30&sa=N&sstk=Af77f_chnDKNIlZ0IppYwCTGX-8AsCUfZH2WQB4kzsZIYRjsE5mqBJMEdWa84P7jgf603q2kg3ocZLtVg3UcaoXgLxAF8bRxzTc64g&ved=2ahUKEwiSq-PSneWSAxWTh_0HHXBdFyQQ8tMDegQICxAI
          current_page: 1
          next_page: 2
          next_page_start: 10
          next_page_link: >-
            https://www.google.com/search?q=pizza&sca_esv=9559f81e103ba33b&hl=en&gl=us&ei=fdaWadL4D5OP9u8P8LrdoAI&start=10&sa=N&sstk=Af77f_chnDKNIlZ0IppYwCTGX-8AsCUfZH2WQB4kzsZIYRjsE5mqBJMEdWa84P7jgf603q2kg3ocZLtVg3UcaoXgLxAF8bRxzTc64g&ved=2ahUKEwiSq-PSneWSAxWTh_0HHXBdFyQQ8tMDegQICxAE
        related:
          - text: Pizza wiki
            link: >-
              https://www.google.com/search?sca_esv=9559f81e103ba33b&hl=en&gl=us&q=Pizza+wiki&sa=X&ved=2ahUKEwiSq-PSneWSAxWTh_0HHXBdFyQQ1QJ6BAhLEAE
            rank: 1
            global_rank: 17
          - text: Pizza open
            link: >-
              https://www.google.com/search?sca_esv=9559f81e103ba33b&hl=en&gl=us&q=Pizza+open&sa=X&ved=2ahUKEwiSq-PSneWSAxWTh_0HHXBdFyQQ1QJ6BAhfEAE
            rank: 2
            global_rank: 18
          - text: Pizza Hut near me
            link: >-
              https://www.google.com/search?sca_esv=9559f81e103ba33b&hl=en&gl=us&q=Pizza+Hut+near+me&sa=X&ved=2ahUKEwiSq-PSneWSAxWTh_0HHXBdFyQQ1QJ6BAheEAE
            rank: 3
            global_rank: 19
        people_also_ask:
          - question: What's the 2 hour rule for pizza?
            question_type: featured
            answer_source: Green Lantern Pizza
            answer_link: >-
              https://greenlanternpizza.com/blog/how-long-does-pizza-last/#:~:text=Sitting%20out%20at%20Room%20Temperature,-How%20long%20can&text=The%20United%20States%20Department%20of,two%20hours%20before%20tossing%20it.
            answer_display_link: >-
              https://greenlanternpizza.com › blog ›
              how-long-does-pi...https://greenlanternpizza.com › blog ›
              how-long-does-pi...
            answers:
              - type: answer
                value:
                  text: >-
                    Sitting out at Room Temperature The United States Department
                    of Agriculture (USDA) strongly recommends following the
                    “two-hour rule” when leaving food out, meaning you shouldn't
                    let pizza or takeout sit at room temperature for over two
                    hours before tossing it.Jan 29, 2025
                rank: 1
            rank: 1
            global_rank: 7
    HTTP400:
      type: string
      example: Bad Request
    HTTP401:
      type: string
      example: User authentication is required
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