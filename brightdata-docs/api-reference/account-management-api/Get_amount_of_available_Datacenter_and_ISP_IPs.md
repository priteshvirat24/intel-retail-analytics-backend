> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Available Datacenter and ISP IPs

> Use the Bright Data Account Management API to available Datacenter and ISP IPs via GET /zone/count_available_ips, returning a 200 OK JSON response.

<Tip>
  Paste your API key to the authorization field. To get an API key, [Create an account](https://brightdata.com/?hs_signup=1\&utm_source=docs\&utm_campaign=playground) and learn [how to generate an API key](/api-reference/authentication#how-do-i-generate-a-new-api-key%3F)
</Tip>

<Accordion title="Plan Examples">
  * Available IPs for current Zone plan:

  ```sh theme={null}
  curl "https://api.brightdata.com/count_available_ips?zone=ZONE" -H "Authorization: Bearer API_KEY"
  ```

  * Abstract plan, dedicated IPs:

  ```sh dedicated IPs theme={null}
  curl "https://api.brightdata.com/count_available_ips?plan=\{\"ips_type\":\"dedicated\"\}" -H "Authorization: Bearer API_KEY"
  ```

  * Abstract plan, shared IPs located in United States:

  ```sh theme={null}
  curl "https://api.brightdata.com/count_available_ips?plan=\{\"country\":\"us\",\"ips_type\":\"shared\"\}" -H "Authorization: Bearer API_KEY"
  ```

  * Abstract plan, dedicated ips located in United States:

  ```sh theme={null}
  curl "https://api.brightdata.com/count_available_ips?plan=\{\"country\":\"us\",\"ips_type\":\"dedicated\"\}" -H "Authorization: Bearer API_KEY"
  ```

  * Abstract plan, shared IPs located in United States, Denver:

  ```sh theme={null}
  curl "https://api.brightdata.com/count_available_ips?plan=\{\"ips_type\":\"shared\",\"country_city\":\"us-denver\",\"city\":true\}" -H "Authorization: Bearer API_KEY"
  ```

  * Abstract plan, shared IPs located in US, exclusive for domains: amazon.com, fb.com:

  ```sh theme={null}
  curl "https://api.brightdata.com/count_available_ips?plan=\{\"ips_type\":\"selective\",\"country\":\"us\",\"domain_whitelist\":\"amazon.com%20fb.com\"\}" -H "Authorization: Bearer API_KEY"
  ```

  * Abstract plan, shared IPs located in US, geo IP databases: should persist in both maxmind and dbip:

  ```sh theme={null}
  curl "https://api.brightdata.com/count_available_ips?plan=\{\"ips_type\":\"shared\",\"country\":\"us\",\"geo_db\":\{\"maxmind\":true,\"dbip\":true\}\}" -H "Authorization: Bearer API_KEY"
  ```
</Accordion>


## OpenAPI

````yaml api-reference/openapi GET /zone/count_available_ips
openapi: 3.0.1
info:
  title: Bright Data API
  description: >-
    Integrate Bright Data APIs to your pipeline and secure high-end scraping
    precision
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security:
  - bearerAuth: []
paths:
  /zone/count_available_ips:
    get:
      parameters:
        - in: query
          name: zone
          description: name of the Zone
          required: false
          schema:
            type: string
        - in: query
          name: plan
          required: false
          schema:
            type: object
            properties:
              pool_ip_type:
                type: string
                description: >-
                  use in case you want to get the amount of ISP IPs available,
                  the default amount for that API endpoint is data center peer
                  IPs.
                default: static_res
              ips_type:
                type: string
                description: |+
                  type of IPs. 

                   `shared`: For shared 

                   `selective`: For selective 

                   `dedicated`: For dedicated 

              country:
                type: string
                description: IPs location country
              country_city:
                type: string
                description: defines the city location of the IPs
              city:
                type: boolean
                description: required with `country_city` parameter
              domain_whitelist:
                type: string
                description: |-
                  Space separated list of domains 

                   **Note**: for `curl` the spaces should be urlencoded : `d1.com%20d2.com`
              geo_db:
                type: object
                description: turns on/off using of the IP`s location databases
                properties:
                  maxmind:
                    type: boolean
                    default: true
                    description: use MaxMind IP location DB
                  dbip:
                    type: boolean
                    default: true
                    description: use DB-IP IP location DB
                  google:
                    type: boolean
                    default: true
                    description: use Google IP location DB
                  ip2location:
                    type: boolean
                    default: true
                    description: use IP2Location IP location DB
                  ipcn:
                    type: boolean
                    default: true
                    description: use ip.cn IP location DB
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                example:
                  count: 1234
components:
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