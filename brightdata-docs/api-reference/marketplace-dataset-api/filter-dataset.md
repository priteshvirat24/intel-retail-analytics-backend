> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Filter dataset (BETA)

> Run async filter jobs on 250+ Bright Data Marketplace datasets. Returns a snapshot_id to download, with CSV/JSON uploads up to 200 MiB.

The Filter endpoint of the Bright Data Marketplace Dataset API runs a large or file-based filter job against any of 250+ Marketplace datasets and returns a `snapshot_id` you can download once the job completes.

<Tip>
  Paste your API key into the authorization field. To get an API key, [create an account](https://brightdata.com/?hs_signup=1\&utm_source=docs\&utm_campaign=playground) and learn [how to generate an API key](/api-reference/authentication#how-do-i-generate-a-new-api-key%3F).
</Tip>

## When should I use Filter?

Use Filter for bulk or file-driven jobs where asynchronous processing is acceptable:

* Bulk exports of more than 1,000 records.
* Filtering against large value lists from CSV or JSON files, such as excluding 100k+ company IDs.
* Datasets not yet supported by Search.
* Scheduled or background pipelines where async is fine.

For sub-second real-time lookups on supported datasets, use [Search](/api-reference/marketplace-dataset-api/search-dataset) instead.

## How does Filter work?

* A call to the Filter endpoint starts an async job and creates a snapshot of the filtered data in your account.
* The maximum job time is 5 minutes. Jobs that run longer are cancelled.
* Charges apply per record in the snapshot, at the standard Marketplace rate of \$2.5 CPM.
* Filter works on all 250+ Marketplace datasets.
* Filter groups support a maximum nesting depth of 3 levels.

## How do I authenticate?

Filter uses Bearer token authentication. Pass your API key in the `Authorization` header:

```bash theme={null}
Authorization: Bearer YOUR_API_KEY
```

Get your key from [account settings](/api-reference/authentication#how-do-i-generate-a-new-api-key%3F).

## Limits

| Limit                     | Value             | Description                                                                                                 |
| ------------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------- |
| **Max rows per file**     | 10,000            | Each uploaded CSV/JSON file can contain up to 10,000 data rows. The header row is not counted.              |
| **Max files per request** | No limit          | Attach as many files as needed in one multipart request, as long as the total stays within the 200 MiB cap. |
| **Max request size**      | 200 MiB           | Total size of all uploaded files and form data combined. Requests over 200 MiB are rejected.                |
| **Job timeout**           | 5 minutes         | If filtering does not complete within 5 minutes the job is cancelled.                                       |
| **Filter nesting depth**  | 3 levels          | Maximum depth for nested filter groups using `and`/`or`.                                                    |
| **Max parallel jobs**     | 100 per dataset   | Up to 100 Filter jobs can run at once per dataset.                                                          |
| **Rate limit**            | 120 requests/hour | Maximum number of Filter API calls per hour.                                                                |

## How do I call Filter?

Filter has two modes: JSON for plain filters and multipart for file uploads.

### JSON mode (no file uploads)

Send all parameters (`dataset_id`, `records_limit` and `filter`) in the JSON body. Set `Content-Type` to `application/json`:

```bash theme={null}
curl -X POST "https://api.brightdata.com/datasets/filter" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "dataset_id": "gd_l1viktl72bvl7bjuj0",
    "records_limit": 100,
    "filter": {
      "name": "name",
      "operator": "=",
      "value": "John"
    }
  }'
```

Filter returns a `snapshot_id`:

```json theme={null}
{ "snapshot_id": "s_abc123..." }
```

### Multipart mode (file uploads)

Send `dataset_id` and `records_limit` as query parameters, and send `filter` and the uploaded files in the form-data body. Set `Content-Type` to `multipart/form-data`:

```bash theme={null}
curl -X POST "https://api.brightdata.com/datasets/filter?dataset_id=gd_l1vijqt9jfj7olije&records_limit=100" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: multipart/form-data" \
  -F 'filter={"operator":"and","filters":[{"name":"industries:value","operator":"includes","value":"industries.csv"}]}' \
  -F 'files[]=@/path/to/industries.csv'
```

To exclude 100k+ values, split them into files of up to 10,000 rows each and attach them all in a single request:

```bash theme={null}
curl -X POST "https://api.brightdata.com/datasets/filter?dataset_id=gd_l1vijqt9jfj7olije&records_limit=5000" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: multipart/form-data" \
  -F 'filter={"operator":"and","filters":[{"name":"company_id","operator":"not_in","value":"exclude1.csv"},{"name":"company_id","operator":"not_in","value":"exclude2.csv"},{"name":"company_id","operator":"not_in","value":"exclude3.csv"}]}' \
  -F 'files[]=@exclude1.csv' \
  -F 'files[]=@exclude2.csv' \
  -F 'files[]=@exclude3.csv'
```

For CSV and JSON file format rules, file references and upload troubleshooting, see [Filter dataset with CSV/JSON files](/api-reference/marketplace-dataset-api/filter-dataset-with-csv-json-files).

## What does Filter return?

Filter returns a `snapshot_id`. Use it to download the filtered records via the snapshot API once the job completes:

* [Get snapshot metadata](/api-reference/marketplace-dataset-api/get-snapshot-meta)
* [Download the file by snapshot\_id](/api-reference/marketplace-dataset-api/download-the-file-by-snapshot_id)

## How much does Filter cost?

Filter costs \$2.5 CPM (per 1,000 records returned), the same rate as the Marketplace. There is no charge when the filter returns 0 records.

## What errors can Filter return?

| Status | Meaning                                                                            | What to do                                                                                                  |
| ------ | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `400`  | Bad filter or params                                                               | Check field names with [Get dataset metadata](/api-reference/marketplace-dataset-api/get-dataset-metadata). |
| `401`  | Bad or missing API key                                                             | Check your Bearer token.                                                                                    |
| `402`  | Not enough funds                                                                   | Top up your balance or reduce `records_limit`.                                                              |
| `404`  | Unknown `dataset_id`                                                               | Confirm the dataset ID.                                                                                     |
| `422`  | Filter matched 0 records                                                           | Loosen your filter or check field values.                                                                   |
| `429`  | Too many parallel jobs (max 100 per dataset) or rate limit hit (120 requests/hour) | Back off and retry.                                                                                         |

## Filter syntax

The `filter` object, its operators, filter groups and nesting rules are shared with the [Search endpoint](/api-reference/marketplace-dataset-api/search-dataset) and documented in one place. See the [filter syntax reference](/api-reference/marketplace-dataset-api/filter-syntax) for the full operator list, filter groups, up to three levels of nesting and CSV/JSON file references.

## Related

* [Dataset API overview](/api-reference/marketplace-dataset-api/overview)
* [Search dataset (sync)](/api-reference/marketplace-dataset-api/search-dataset)
* [Filter syntax reference](/api-reference/marketplace-dataset-api/filter-syntax)
* [Filter dataset with CSV/JSON files](/api-reference/marketplace-dataset-api/filter-dataset-with-csv-json-files)
* [Get dataset metadata](/api-reference/marketplace-dataset-api/get-dataset-metadata)


## OpenAPI

````yaml api-reference/dca-api POST /datasets/filter
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
  /datasets/filter:
    post:
      description: Create a dataset snapshot based on a provided filter
      parameters:
        - name: dataset_id
          in: query
          description: ID of the dataset to filter (required in multipart/form-data mode)
          required: false
          schema:
            type: string
            example: gd_l1viktl72bvl7bjuj0
        - name: records_limit
          description: Limit the number of records to be included in the snapshot
          in: query
          required: false
          schema:
            type: integer
            example: 1000
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - dataset_id
                - filter
              properties:
                dataset_id:
                  type: string
                  description: ID of the dataset to filter
                  example: gd_l1viktl72bvl7bjuj0
                records_limit:
                  type: integer
                  description: Limit the number of records to be included in the snapshot
                  example: 1000
                filter:
                  $ref: '#/components/schemas/DatasetFilter'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/FilterDatasetBody'
      responses:
        '200':
          description: Job of creating the snapshot successfully started
          content:
            application/json:
              schema:
                type: object
                properties:
                  snapshot_id:
                    type: string
                    description: ID of the snapshot
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ValidationErrorBody'
              example:
                validation_errors:
                  - '"filter.filters[0].invalid_prop" is not allowed'
                  - '"records_limit" must be a positive number'
        '402':
          description: Not enough funds to create the snapshot
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorBody'
              example:
                error: >-
                  Your current balance is insufficient to process this data
                  collection request. Please add funds to your account or adjust
                  your request to continue. ($1 is missing)
        '422':
          description: Provided filter did not match any records
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorBody'
              example:
                error: Provided filter did not match any records
        '429':
          description: Too many parallel jobs
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorBody'
              example:
                error: Maximum limit of 100 jobs per dataset has been exceeded
      x-codeSamples:
        - lang: shell
          label: cURL
          source: |-
            curl --request POST \
              --url 'https://api.brightdata.com/datasets/filter?dataset_id=gd_l1vikfnt1wgvvqz95w' \
              --header "Authorization: Bearer YOUR_API_KEY" \
              --header "Content-Type: application/json" \
              --data '{"filter": {"name": "url", "operator": "=", "value": "https://www.instagram.com/natgeo/"}, "records_limit": 10}'
        - lang: python
          label: Python
          source: >-
            import requests


            url =
            "https://api.brightdata.com/datasets/filter?dataset_id=gd_l1vikfnt1wgvvqz95w"

            headers = {
                "Authorization": "Bearer YOUR_API_KEY",
                "Content-Type": "application/json",
            }

            payload = {
                "filter": {
                    "name": "url",
                    "operator": "=",
                    "value": "https://www.instagram.com/natgeo/"
                },
                "records_limit": 10
            }


            response = requests.post(url, headers=headers, json=payload)

            print(response.text)
        - lang: py
          label: Python SDK
          source: |-
            # Install: pip install brightdata-sdk
            from brightdata import BrightDataClient

            async with BrightDataClient(api_key="YOUR_API_KEY") as client:
                # Quick sample — no filter needed
                snapshot_id = await client.datasets.imdb_movies.sample(records_limit=5)

                # Or filter with criteria
                snapshot_id = await client.datasets.instagram_profiles.query(
                    url="https://www.instagram.com/natgeo/",
                    records_limit=10,
                )

                # Same pattern works on all 126+ datasets
                await client.datasets.amazon_products.sample(records_limit=10)
                await client.datasets.linkedin_profiles.sample(records_limit=10)
        - lang: javascript
          label: JavaScript
          source: >-
            const response = await
            fetch("https://api.brightdata.com/datasets/filter?dataset_id=gd_l1vikfnt1wgvvqz95w",
            {
              method: "POST",
              headers: {
                "Authorization": "Bearer YOUR_API_KEY",
                "Content-Type": "application/json",
              },
              body: JSON.stringify({
                "filter": {
                    "name": "url",
                    "operator": "=",
                    "value": "https://www.instagram.com/natgeo/"
                },
                "records_limit": 10
            }),

            });


            const data = await response.text();

            console.log(data);
        - lang: js
          label: JavaScript SDK
          source: >-
            // Install: npm install @brightdata/sdk

            import { bdclient } from '@brightdata/sdk';


            const client = new bdclient({ apiKey: 'YOUR_API_KEY' });


            const ds = client.datasets;


            // Query a dataset and return a snapshot_id you can download

            const snapshotId = await ds.instagramProfiles.query(
              { url: 'https://www.instagram.com/natgeo/' },
              { records_limit: 10 },
            );


            // Same pattern works on all 126+ datasets

            await ds.amazonProducts.query({ url: 'https://amazon.com/dp/B123'
            });

            await ds.imdbMovies.query({}, { records_limit: 50 });


            await client.close();
        - lang: php
          label: PHP
          source: >-
            <?php

            $ch =
            curl_init("https://api.brightdata.com/datasets/filter?dataset_id=gd_l1vikfnt1wgvvqz95w");

            curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");

            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

            curl_setopt($ch, CURLOPT_HTTPHEADER, [
                "Authorization: Bearer YOUR_API_KEY",
                "Content-Type: application/json",
            ]);

            curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode({
                "filter": {
                    "name": "url",
                    "operator": "=",
                    "value": "https://www.instagram.com/natgeo/"
                },
                "records_limit": 10
            }));


            $response = curl_exec($ch);

            curl_close($ch);

            echo $response;
        - lang: go
          label: Go
          source: "package main\n\nimport (\n\t\"bytes\"\n\t\"fmt\"\n\t\"io\"\n\t\"net/http\"\n)\n\nfunc main() {\n\tpayload := []byte(\"{\\\"filter\\\": {\\\"name\\\": \\\"url\\\", \\\"operator\\\": \\\"=\\\", \\\"value\\\": \\\"https://www.instagram.com/natgeo/\\\"}, \\\"records_limit\\\": 10}\")\n\treq, _ := http.NewRequest(\"POST\", \"https://api.brightdata.com/datasets/filter?dataset_id=gd_l1vikfnt1wgvvqz95w\", bytes.NewBuffer(payload))\n\treq.Header.Set(\"Authorization\", \"Bearer YOUR_API_KEY\")\n\treq.Header.Set(\"Content-Type\", \"application/json\")\n\n\tres, err := http.DefaultClient.Do(req)\n\tif err != nil { panic(err) }\n\tdefer res.Body.Close()\n\n\tbody, _ := io.ReadAll(res.Body)\n\tfmt.Println(string(body))\n}"
        - lang: java
          label: Java
          source: |-
            import java.net.URI;
            import java.net.http.HttpClient;
            import java.net.http.HttpRequest;
            import java.net.http.HttpResponse;

            public class Main {
                public static void main(String[] args) throws Exception {
                    String body = "{\"filter\": {\"name\": \"url\", \"operator\": \"=\", \"value\": \"https://www.instagram.com/natgeo/\"}, \"records_limit\": 10}";
                    HttpRequest request = HttpRequest.newBuilder()
                        .uri(URI.create("https://api.brightdata.com/datasets/filter?dataset_id=gd_l1vikfnt1wgvvqz95w"))
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


            uri =
            URI.parse("https://api.brightdata.com/datasets/filter?dataset_id=gd_l1vikfnt1wgvvqz95w")

            request = Net::HTTP::Post.new(uri)

            request["Authorization"] = "Bearer YOUR_API_KEY"

            request["Content-Type"] = "application/json"

            request.body = {"filter": {"name": "url", "operator": "=", "value":
            "https://www.instagram.com/natgeo/"}, "records_limit": 10}.to_json


            response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) {
            |http| http.request(request) }

            puts response.body
components:
  schemas:
    DatasetFilter:
      anyOf:
        - $ref: '#/components/schemas/DatasetFilterItem'
          title: Single field filter
        - $ref: '#/components/schemas/DatasetFilterGroup'
          title: Filters group
        - $ref: '#/components/schemas/DatasetFilterItemNoVal'
          title: Single field filter w/out value
    FilterDatasetBody:
      type: object
      required:
        - filter
      properties:
        filter:
          $ref: '#/components/schemas/DatasetFilter'
    ValidationErrorBody:
      type: object
      properties:
        validation_errors:
          type: array
          items:
            type: string
    ErrorBody:
      type: object
      properties:
        error:
          type: string
    DatasetFilterItem:
      type: object
      required:
        - name
        - operator
        - value
      additionalProperties: false
      properties:
        name:
          type: string
          description: Field name to filter by
        operator:
          type: string
          enum:
            - '='
            - '!='
            - '>'
            - <
            - '>='
            - <=
            - in
            - not_in
            - includes
            - not_includes
            - array_includes
            - not_array_includes
        value:
          description: Value to filter by
          oneOf:
            - type: string
            - type: number
            - type: boolean
            - type: object
            - type: array
              items:
                oneOf:
                  - type: string
                  - type: number
                  - type: boolean
      example:
        name: name
        operator: '='
        value: John
    DatasetFilterGroup:
      type: object
      required:
        - operator
        - filters
      additionalProperties: false
      properties:
        operator:
          type: string
          enum:
            - and
            - or
        combine_nested_fields:
          type: boolean
          description: >-
            For arrays of objects: if true, all filters must match within a
            single object
        filters:
          type: array
          items:
            $ref: '#/components/schemas/DatasetFilter'
      example:
        operator: and
        filters:
          - name: name
            operator: '='
            value: John
          - name: age
            operator: '>'
            value: '30'
    DatasetFilterItemNoVal:
      type: object
      required:
        - name
        - operator
      additionalProperties: false
      properties:
        name:
          type: string
          description: Field name to filter by
        operator:
          type: string
          enum:
            - is_null
            - is_not_null
      example:
        name: reviews_count
        operator: is_not_null
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