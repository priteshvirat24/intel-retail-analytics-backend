> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add zone password

> Use the Bright Data Account Management API to add Zone Password. POST /zone/add_password returns 200 OK with zone or account configuration data as JSON.

<Warning>Only users with **Admin** or **Ops** roles can perform this action.</Warning>

<Note>
  To add multiple passwords in a single request, pass an array of strings to the `password` field.
</Note>


## OpenAPI

````yaml api-reference/openapi POST /zone/add_password
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
  /zone/add_password:
    post:
      summary: Add Zone Password
      description: Add one or more passwords to a zone.
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
                  description: The name of the zone to add the password to.
                  type: string
                password:
                  description: >-
                    The password(s) to add. Pass a single string or an array of
                    strings to add multiple passwords.
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
          description: Invalid request. Check that the zone name and password are valid.
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