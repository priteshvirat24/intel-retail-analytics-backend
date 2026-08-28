> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Zone statistics

> Use the Bright Data Account Management API to zone Statistics. GET /zone/ips returns 200 OK with zone or account configuration data as JSON.

<Tip>
  Paste your API key to the authorization field. To get an API key, [Create an account](https://brightdata.com/?hs_signup=1\&utm_source=docs\&utm_campaign=playground) and learn [how to generate an API key](/api-reference/authentication#how-do-i-generate-a-new-api-key%3F)
</Tip>

```json Response when "ip_per_country=true" theme={null}
{
    "gb":198,
    "de":282,
    "br":418,
    "au":115,
    "jp":292,
    "nl":421,
    "uz":333,
    "il":517,
    "kg":566,
    "az":498,
    "lv":484,
    "tw":372,
    "sg":184
}
```


## OpenAPI

````yaml api-reference/openapi GET /zone/ips
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
  /zone/ips:
    get:
      description: Get Zone Static (Datacenter/ISP) IPs
      parameters:
        - in: query
          name: zone
          description: Zone name
          required: true
          schema:
            type: string
        - in: query
          name: ip_per_country
          description: get the total amount of IPs per country
          required: false
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                example:
                  ips:
                    - ip: 1.1.1.1
                      maxmind: au
                      ext:
                        dbip: au
                        ip2location: au
                        google: us
                    - ip: 1.1.1.1
                      maxmind: au
                      ext:
                        dbip: au
                        ip2location: au
                        google: us
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