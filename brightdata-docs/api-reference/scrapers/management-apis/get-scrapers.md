> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get all scrapers

> Use the Bright Data Web Scraper API to list every scraper on your account. GET /datasets/v3/scrapers returns each scraper's dataset ID and name as JSON.



## OpenAPI

````yaml api-reference/dca-api get /datasets/v3/scrapers
openapi: 3.1.0
info:
  title: Brightdata API
  description: API for interaction with datasets marketplace
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security:
  - bearerAuth: []
paths:
  /datasets/v3/scrapers:
    get:
      description: >-
        Get a list of all scrapers available to your account. Each scraper is
        identified by a dataset ID and a display name. Use the returned `id` as
        the `dataset_id` parameter in the trigger and management endpoints.
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: string
                      description: >-
                        Dataset ID of the scraper, used as the `dataset_id`
                        parameter in the trigger and management endpoints
                    name:
                      type: string
                      description: Human-readable name of the scraper
              examples:
                scrapers:
                  value:
                    - id: gd_mq5dtosp2eq0rjny2e
                      name: Ergobaby Products
                    - id: gd_mq5hrug82ex2tzuad
                      name: Primally Pure Products
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

        Authorization: Bearer YOUR_API_KEY

        ```


        Learn how to get your Bright Data API key:
        https://docs.brightdata.com/api-reference/authentication
      bearerFormat: API Key

````