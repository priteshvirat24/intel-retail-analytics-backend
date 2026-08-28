> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get dataset views

> List your dataset views with IDs, names and underlying dataset across 250+ domains so you can configure or update delivery settings for each subscription.

A dataset view is a saved, filtered subscription to a Bright Data marketplace dataset that delivers fresh records to your destination on a recurring schedule. Each view has a unique `id` (for example `v_id1`) which you pass to the view delivery settings endpoints.

Use the `id` returned here with:

* [Get view delivery settings](/api-reference/marketplace-dataset-api/get-view-delivery-settings) to inspect the current configuration.
* [Update view delivery settings](/api-reference/marketplace-dataset-api/update-view-delivery-settings) to change it.
* [Bulk update view delivery settings](/api-reference/marketplace-dataset-api/bulk-update-view-delivery-settings) to apply one configuration to many views at once.


## OpenAPI

````yaml api-reference/dca-api GET /datasets/views
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
  /datasets/views:
    get:
      description: >-
        Retrieves the customer's dataset views. A dataset view represents a
        saved filtered subscription to a dataset that can be delivered on a
        schedule. Use the returned `id` with the view delivery settings
        endpoints.
      responses:
        '200':
          description: List of dataset views
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: string
                      description: Unique identifier for the dataset view
                    name:
                      type: string
                      description: Customer-assigned name for the view
                    dataset_id:
                      type: string
                      description: ID of the underlying dataset
                    dataset_name:
                      type: string
                      description: Name of the underlying dataset
                    domain:
                      type: string
                      description: Primary domain of the dataset
              example:
                - id: v_id1
                  name: test1
                  dataset_id: gd_id1
                  dataset_name: Dataset One
                  domain: datasetonename.com
                - id: v_id2
                  name: test2
                  dataset_id: gd_id2
                  dataset_name: Dataset Two
                  domain: datasettwoname.com
        '401':
          description: Unauthorized - Invalid or missing API key
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: Unauthorized
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