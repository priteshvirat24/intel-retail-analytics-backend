> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Filter dataset (JSON or file uploads)

> Use the Bright Data Marketplace Dataset API to filter Dataset (JSON or File Uploads). Spans 250+ domains in the Bright Data marketplace.

The Filter endpoint of the Bright Data Marketplace Dataset API can filter a dataset against thousands of values stored in a CSV or JSON file. Upload one or more files in multipart mode and reference each filename in your filter.

<Tip>
  Paste your API key into the authorization field. To get an API key, [Create an account](https://brightdata.com/?hs_signup=1\&utm_source=docs\&utm_campaign=playground) and learn [how to generate an API key](/api-reference/authentication#how-do-i-generate-a-new-api-key%3F).
</Tip>

## How does file-based filtering work?

Use file uploads when you need to filter against large value lists, such as including or excluding 100k+ company IDs:

* Upload CSV or JSON files in `multipart/form-data` mode and reference each filename in your filter.
* Each file holds up to 10,000 data rows, and the whole request can be up to 200 MiB.
* The Filter job runs asynchronously and returns a `snapshot_id` to download once it completes.

For the async job flow, limits, pricing and error codes, see [Filter dataset (async)](/api-reference/marketplace-dataset-api/filter-dataset).

## How do I format the CSV or JSON file?

<Tabs>
  <Tab title="CSV">
    * First line must be a header matching the field name in your filter.
    * Each following line contains a single value.

    ```csv Example: industries.csv theme={null}
    industries:value
    Accounting
    Ad Network
    Advertising
    ```
  </Tab>

  <Tab title="JSON">
    * Must be an array of objects, each with a key matching the field name in your filter.

    ```json Example industries.json theme={null}
    [
      {"industries:value": "Accounting"},
      {"industries:value": "Ad Network"},
      {"industries:value": "Advertising"}
    ]
    ```
  </Tab>
</Tabs>

***

## How do I reference a file in the filter?

When using file uploads, set the filter's `value` field to the filename:

```json Example theme={null}
{
  "operator": "and",
  "filters": [
    {
      "name": "industries:value",
      "operator": "includes",
      "value": "industries.csv"
    }
  ]
}
```

File references work only with the operators `in`, `not_in`, `includes`, `not_includes`, `array_includes` and `not_array_includes`. For the full operator table and field types, see the [filter syntax reference](/api-reference/marketplace-dataset-api/filter-syntax#which-operators-read-csv-or-json-files%3F).

***

## Filter with multiple files

```bash theme={null}
curl \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: multipart/form-data" \
  -F "files[]=@/path/to/industries.csv" \
  -F "files[]=@/path/to/regions.csv" \
  -F "filter={\"operator\":\"and\",\"filters\":[{\"name\":\"industries:value\",\"operator\":\"includes\",\"value\":\"industries.csv\"},{\"name\":\"region\",\"operator\":\"in\",\"value\":\"regions.csv\"}]}" \
  "https://api.brightdata.com/datasets/filter?dataset_id=gd_l1vijqt9jfj7olije"
```

## Troubleshoot file uploads

| Issue                     | Possible Solution                                                                                                        |
| :------------------------ | :----------------------------------------------------------------------------------------------------------------------- |
| **"File not found"**      | Make sure the filename in your filter exactly matches the uploaded file name.                                            |
| **"Invalid file format"** | Check CSV header matches the filter field name, or ensure JSON is an array of objects.                                   |
| **"Field not found"**     | Verify field exists in dataset. Use [Get Dataset Metadata](/api-reference/marketplace-dataset-api/get-dataset-metadata). |

## Related

* [Dataset API overview](/api-reference/marketplace-dataset-api/overview)
* [Filter dataset (async)](/api-reference/marketplace-dataset-api/filter-dataset)
* [Filter syntax reference](/api-reference/marketplace-dataset-api/filter-syntax)
* [Get Dataset List](/api-reference/marketplace-dataset-api/get-dataset-list)
* [Get Dataset Metadata](/api-reference/marketplace-dataset-api/get-dataset-metadata)


## OpenAPI

````yaml api-reference/filter-csv-json POST /datasets/filter
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
          required: true
          in: query
          description: ID of the dataset to filter (required in multipart/form-data mode)
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
components:
  schemas:
    FilterDatasetBody:
      type: object
      required:
        - filter
      properties:
        filter:
          $ref: '#/components/schemas/DatasetFilter'
        files:
          type: array
          description: >-
            CSV or JSON files referenced by name in the filter, sent as
            multipart file parts. The cURL samples use the array-notation alias
            files[].
          items:
            type: string
            format: binary
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
    DatasetFilter:
      anyOf:
        - $ref: '#/components/schemas/DatasetFilterItem'
          title: Single field filter
        - $ref: '#/components/schemas/DatasetFilterGroup'
          title: Filters group
        - $ref: '#/components/schemas/DatasetFilterItemNoVal'
          title: Single field filter w/out value
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

        Authorization: Bearer
        b5648e1096c6442f60a6c4bbbe73f8d2234d3d8324554bd6a7ec8f3f251f07df

        ```


        Learn how to get your Bright Data API key:
        https://docs.brightdata.com/api-reference/authentication
      bearerFormat: API Key

````