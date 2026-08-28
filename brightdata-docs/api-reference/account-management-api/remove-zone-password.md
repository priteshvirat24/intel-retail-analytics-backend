> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Remove zone password

> Use the Bright Data Account Management API to remove Zone Password. POST /zone/remove_password returns 200 OK with zone or account configuration data as JSON.

<Warning>Only users with **Admin** or **Ops** roles can perform this action.</Warning>

<Warning>
  A zone must always have at least one password. This request will fail if removing the specified password(s) would leave the zone with no passwords.
</Warning>

<Note>
  To remove multiple passwords in a single request, pass an array of strings to the `password` field.
</Note>


## OpenAPI

````yaml api-reference/openapi POST /zone/remove_password
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
  /zone/remove_password:
    post:
      summary: Remove Zone Password
      description: >-
        Remove one or more passwords from a zone. At least one password must
        remain on the zone — this request will fail if it would leave the zone
        with no passwords.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              required:
                - zone
                - password
              type: object
              properties:
                zone:
                  description: The name of the zone to remove the password from.
                  type: string
                password:
                  description: >-
                    The password(s) to remove. Pass a single string or an array
                    of strings to remove multiple passwords.
                  type: array
                  items:
                    type: string
            example:
              zone: my_zone
              password:
                - 123@Abc
                - 456$Abc
      responses:
        '200':
          description: OK
        '400':
          description: >-
            Invalid request. This may occur if the removal would leave the zone
            with no passwords.
        '401':
          description: Unauthorized. Invalid or missing API key.
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