> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Download results

> Use the Bright Data Deep Lookup API to download Results. GET /request/{id}/download returns enriched records as JSON with 200 OK on success.

<Card title="Query Parameters">
  <ParamField query="format" type="string" default="json">
    Output format: `json` (default), `csv`, `excel`
  </ParamField>
</Card>

```bash theme={null}
curl -X GET "https://api.brightdata.com/datasets/deep_lookup/v1/request/ai_meu3z0171o8k9jc4dh/download?format=csv" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -o results.csv
```


## OpenAPI

````yaml api-reference/deep-lookup GET /request/{id}/download
openapi: 3.1.0
info:
  title: Bright Data Deep Lookup API
  description: >-
    The Bright Data Deep Lookup API lets you preview, refine, and execute
    research queries.

    Supports enrichment, cancellation, and exporting results in multiple
    formats.
  version: 1.0.0
servers:
  - url: https://api.brightdata.com/datasets/deep_lookup/v1
security:
  - bearerAuth: []
paths:
  /request/{id}/download:
    get:
      summary: Download Results
      description: Export results in JSON, CSV, or Excel.
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
            examples:
              - ai_meu3z0171o8k9jc4dh
        - in: query
          name: format
          description: '**Note:** Excel format is not currently available.'
          required: false
          schema:
            type: string
            enum:
              - json
              - csv
            default: json
            examples:
              - csv
      responses:
        '200':
          description: File download
          content:
            application/json: {}
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