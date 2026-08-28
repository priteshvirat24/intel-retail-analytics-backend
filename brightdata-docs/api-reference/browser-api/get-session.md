> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get browser session

> Use the Bright Data Browser API to get a Browser Session. GET /browser_sessions/{session_id} returns 200 OK with session metadata as JSON.



## OpenAPI

````yaml GET /browser_sessions/{session_id}
openapi: 3.1.0
info:
  title: Browser Sessions API
  description: ''
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security:
  - bearerAuth: []
paths:
  /browser_sessions/{session_id}:
    get:
      summary: Get single browser session
      description: Retrieve details of a specific browser session using its session_id.
      parameters:
        - name: session_id
          in: path
          required: true
          description: >-
            Unique session identifier. 


            > To retrieve the `session_id` of your current browser session, use
            [`Browser.getSessionId`](https://docs.brightdata.com/scraping-automation/scraping-browser/cdp-functions/custom#getting-session-id)
            CDP command.
          schema:
            type: string
      responses:
        '200':
          description: Session retrieved successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SingleSessionResponse'
              examples:
                Finished:
                  summary: Finished Session
                  value:
                    session:
                      session_id: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
                      api_name: scraping_browser1
                      status: finished
                      timestamp: '2025-12-16T18:53:41Z'
                      target_url: https://www.example.com
                      end_url: https://www.example.com/example/sub/domain
                      navigations: 4
                      duration: 209.444
                      captcha: solved
                      bandwidth: 123456789
                      error: null
                Failed:
                  summary: Failed Session
                  value:
                    session:
                      session_id: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
                      api_name: scraping_browser1
                      status: failed
                      timestamp: '2025-12-16T18:53:41Z'
                      target_url: https://www.example.com
                      end_url: https://www.example.com/example/sub
                      navigations: 3
                      duration: 209.444
                      captcha: none
                      bandwidth: 123456789
                      error:
                        code: unknown
                        message: Error
                Running:
                  summary: Running Session
                  value:
                    session:
                      session_id: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
                      api_name: scraping_browser1
                      status: running
                      timestamp: '2025-12-16T18:53:41Z'
                      target_url: null
                      end_url: null
                      navigations: 0
                      duration: null
                      captcha: none
                      bandwidth: 0
                      error: null
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
              examples:
                Invalid Format:
                  summary: Invalid session_id format
                  value:
                    error: Invalid session_id format
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
              examples:
                Missing Credentials:
                  summary: Missing Credentials
                  value:
                    error: Credentials are missing
        '404':
          description: Session not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SessionNotFound'
              examples:
                '':
                  summary: ''
                  value:
                    error: Session not found
                    session_id: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
components:
  schemas:
    SingleSessionResponse:
      type: object
      properties:
        session:
          $ref: '#/components/schemas/Session'
    ErrorMessage:
      type: object
      properties:
        error:
          type: string
    SessionNotFound:
      type: object
      properties:
        error:
          type: string
        session_id:
          type: string
    Session:
      type: object
      properties:
        session_id:
          type: string
          description: Unique session identifier
        api_name:
          type: string
          description: Name of the Browser API used
        status:
          type: string
          enum:
            - running
            - finished
            - failed
          description: 'Session status. Values: `running`, `finished`, `failed`'
        target_url:
          type: string
          nullable: true
          description: Target url from initial navigation
        end_url:
          type: string
          nullable: true
          description: The last url before the session closed
        navigations:
          type: integer
          description: Number of page navigations performed
        timestamp:
          type: string
          format: date-time
          description: Session start time in ISO 8601 format
        duration:
          type: number
          nullable: true
          description: Total session duration in seconds
        captcha:
          type: string
          enum:
            - solved
            - none
            - failed
            - detected
          description: 'Captcha status. Values: `solved`, `none`, `failed`, `detected`'
        bandwidth:
          type: integer
          description: Total billable bandwidth in bytes
        error:
          description: null for running sessions or finished session with no error
          oneOf:
            - $ref: '#/components/schemas/ErrorObject'
            - type: 'null'
    ErrorObject:
      type: object
      properties:
        code:
          type: string
        message:
          type: string
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