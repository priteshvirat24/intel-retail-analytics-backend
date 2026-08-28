> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get proxies pending replacement

> Use the Bright Data Account Management API to get Proxies Pending Replacement via GET /zone/proxies_pending_replacement, returning a 200 OK JSON response.



## OpenAPI

````yaml api-reference/openapi GET /zone/proxies_pending_replacement
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
  /zone/proxies_pending_replacement:
    get:
      tags:
        - Proxy
      description: >-
        Get list of all proxies in the provided zone, which are pending
        replacement
      parameters:
        - name: zone
          in: query
          description: Zone
          schema:
            type: string
      responses:
        '200':
          description: JSON body of pending IP replacements per zone
          content:
            application/json:
              schema:
                type: object
                properties:
                  ZoneName:
                    type: object
                    properties:
                      type:
                        type: string
                        example: zone1
                      ips_to_replace:
                        type: integer
                        example: 1
                      ips_list:
                        type: array
                        items:
                          type: object
                          properties:
                            due_date:
                              type: string
                              format: date
                            ips:
                              type: array
                              items:
                                type: object
                                properties:
                                  ip:
                                    type: string
                                    format: ipv4
                                  country:
                                    type: string
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