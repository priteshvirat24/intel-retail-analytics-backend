> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List browser session

> Use the Bright Data Browser API to list Browser Sessions. GET /browser_sessions returns 200 OK with active or historical session metadata as JSON.

<Accordion title="Example Usage URLs">
  ```txt Default: last 50 sessions sorted by timestamp desc theme={null}
  https://api.brightdata.com/browser_sessions
  ```

  ```txt Get first 25 finished sessions wrap theme={null}
  https://api.brightdata.com/browser_sessions?limit=25&status=finished
  ```

  ```txt Get all running sessions wrap theme={null}
  https://api.brightdata.com/browser_sessions?status=running
  ```

  ```txt Get all failed sessions wrap theme={null}
  https://api.brightdata.com/browser_sessions?status=failed
  ```

  ```txt Get sessions from a specific API zone wrap theme={null}
  https://api.brightdata.com/browser_sessions?api_name=scraping_browser1
  ```

  ```txt Sessions from a specific date range wrap theme={null}
  https://api.brightdata.com/browser_sessions?start_date=2025-12-01T00:00:00Z&end_date=2025-12-16T23:59:59Z
  ```

  ```txt Sessions for a specific target URL sorted by bandwidth wrap theme={null}
  https://api.brightdata.com/browser_sessions?target_url=example.com&sort=bandwidth&order=desc
  ```

  ```txt All sessions for a specific target URL wrap theme={null}
  https://api.brightdata.com/browser_sessions?target_url=amazon.com
  ```

  ```txt Failed sessions for a specific target URL wrap theme={null}
  https://api.brightdata.com/browser_sessions?target_url=linkedin.com&status=failed
  ```

  ```txt Sessions sorted by highest bandwidth wrap theme={null}
  https://api.brightdata.com/browser_sessions?sort=bandwidth&order=desc
  ```

  ```txt Sessions sorted by longest duration wrap theme={null}
  https://api.brightdata.com/browser_sessions?sort=duration&order=desc
  ```

  ```txt First page (100 sessions) wrap theme={null}
  https://api.brightdata.com/browser_sessions?limit=100&offset=0
  ```

  ```txt Second page (next 100 sessions) wrap theme={null}
  https://api.brightdata.com/browser_sessions?limit=100&offset=100
  ```
</Accordion>


## OpenAPI

````yaml GET /browser_sessions
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
  /browser_sessions:
    get:
      summary: List browser sessions
      description: Retrieve a list of browser sessions with filtering and pagination.
      parameters:
        - name: api_name
          in: query
          schema:
            type: string
          description: Name of the Browser API used
        - name: limit
          in: query
          schema:
            type: integer
            default: 50
            maximum: 100
          description: Number of sessions to return
        - name: offset
          in: query
          schema:
            type: integer
            default: 0
          description: Pagination offset
        - name: status
          in: query
          schema:
            type: string
            enum:
              - running
              - finished
              - failed
              - all
            default: all
          description: Filter by session status
        - name: start_date
          in: query
          schema:
            type: string
            format: date-time
          description: Start date filter
        - name: end_date
          in: query
          schema:
            type: string
            format: date-time
          description: End date filter
        - name: target_url
          in: query
          schema:
            type: string
          description: Filter by target url (e.g., example.com)
        - name: end_url
          in: query
          schema:
            type: string
          description: Filter by end url (e.g., https://www.example.com/example/sub)
        - name: sort
          in: query
          schema:
            type: string
            enum:
              - timestamp
              - duration
              - bandwidth
            default: timestamp
          description: 'Sort field: timestamp, duration, bandwidth'
        - name: order
          in: query
          schema:
            type: string
            enum:
              - asc
              - desc
            default: desc
          description: 'Sort order: `asc` or `desc`'
      responses:
        '200':
          description: List of sessions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BatchSessionResponse'
              examples:
                Success:
                  summary: ''
                  value:
                    sessions:
                      - session_id: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
                        api_name: scraping_browser1
                        status: finished
                        target_url: https://www.example.com
                        end_url: https://www.example.com/example/sub
                        navigations: 4
                        timestamp: '2025-12-16T18:53:41Z'
                        duration: 209.444
                        captcha: solved
                        bandwidth: 123456789
                        error: null
                      - session_id: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
                        api_name: scraping_browser1
                        status: failed
                        target_url: https://www.another-site.com
                        end_url: https://www.another-site.com/examplesubdomain
                        navigations: 3
                        timestamp: '2025-12-16T17:20:15Z'
                        duration: 45.2
                        captcha: none
                        bandwidth: 45678901
                        error:
                          code: unknown
                          message: Error
                      - session_id: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
                        api_name: scraping_browser1
                        status: running
                        target_url: null
                        end_url: null
                        navigations: 0
                        timestamp: '2025-12-16T19:05:30Z'
                        duration: null
                        captcha: none
                        bandwidth: 0
                        error: null
                    count: 3
                    total: 257
                    pagination:
                      offset: 0
                      limit: 50
                      has_more: true
                      next_offset: 50
                Empty:
                  summary: ''
                  value:
                    sessions: []
                    count: 0
                    total: 0
                    pagination:
                      offset: 0
                      limit: 50
                      has_more: false
                      next_offset: null
        '400':
          description: Invalid request parameters
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
              examples:
                Bad Request:
                  summary: Bad Request
                  value:
                    error: Invalid request parameters
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
              examples:
                Missing credentials:
                  summary: Missing credentials
                  value:
                    error: Credentials are missing
                Invalid credentials:
                  summary: Invalid credentials
                  value:
                    error: Invalid credentials
components:
  schemas:
    BatchSessionResponse:
      type: object
      properties:
        sessions:
          type: array
          items:
            $ref: '#/components/schemas/Session'
        count:
          type: integer
        total:
          type: integer
        pagination:
          $ref: '#/components/schemas/Pagination'
    ErrorMessage:
      type: object
      properties:
        error:
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
    Pagination:
      type: object
      properties:
        offset:
          type: integer
        limit:
          type: integer
        has_more:
          type: boolean
        next_offset:
          type: integer
          nullable: true
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