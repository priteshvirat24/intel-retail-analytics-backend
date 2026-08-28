> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Total cost & bandwidth for a zone

> Returns 200 OK with billed cost, bandwidth and usage for a Zone over a date range. Matches the Control Panel Usage Overview and your invoice.

<Warning id="to-is-exclusive">
  **The `to` parameter is exclusive.** The day specified in `to` is **not** included in the result. To match a calendar month shown in the Control Panel or on your invoice, set `to` to the first day of the **following** month. For example, `from=2026-04-01&to=2026-05-01` returns all of April 2026.
</Warning>

<Note>
  This endpoint is scoped to a single zone and cannot return Web Scraper API or Scraper Studio cost data (those are keyed by `dataset_id` / collector ID, not by zone name). For multi-product or WSA / Scraper Studio breakdowns, use [Cost breakdown export](/api-reference/account-management-api/Export_cost_breakdown).
</Note>

<Tip>
  Paste your API key to the authorization field. To get an API key, [Create an account](https://brightdata.com/?hs_signup=1\&utm_source=docs\&utm_campaign=playground) and learn [how to generate an API key](/api-reference/authentication#how-do-i-generate-a-new-api-key%3F).
</Tip>

## Reproduce your monthly invoice

To retrieve the exact billed cost and usage for a calendar month as shown in the Control Panel and on your invoice, set `from` to the first day of the month and `to` to the first day of the **following** month:

```bash theme={null}
# Returns billed usage for all of April 2026
curl -H "Authorization: Bearer YOUR_API_KEY" \
  "https://api.brightdata.com/zone/cost?zone=YOUR_ZONE&from=2026-04-01&to=2026-05-01"
```

Using `to=2026-04-30` would omit the last day of the month. Always set `to` to the day **after** the last day you want included.

## Reconciling with raw request logs

The values returned by this endpoint are the source of truth for billing. They match the Control Panel's Usage Overview and your invoice. If you compare these values against raw request logs you collect yourself (e.g., access logs forwarded to Logz, CloudWatch, or another sink), expect differences of a few percent. Raw logs may capture requests that were never committed to the billing database because of async aggregation timing or transient network issues. Your invoice always reflects the values returned by this endpoint.

## Related endpoints

* [Bandwidth stats for a Zone](/api-reference/account-management-api/Get_the_bandwidth_stats_for_a_Zone). Bandwidth only, no cost.
* [Bandwidth stats for all your Zones](/api-reference/account-management-api/Get_the_bandwidth_stats_for_all_your_Zones). Aggregate across zones.


## OpenAPI

````yaml api-reference/openapi GET /zone/cost
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
  /zone/cost:
    get:
      description: >-
        Returns billed cost, bandwidth, and usage stats for a Zone over a date
        range. Values match the Control Panel's Usage Overview and your
        invoice. 

         **Note:** the `to` parameter is **exclusive**. The day specified is not included. See the page below for invoice reconciliation guidance.
      parameters:
        - in: query
          name: zone
          description: Zone name (e.g., `se_midware`).
          required: true
          schema:
            type: string
        - in: query
          name: from
          description: Inclusive start date in `YYYY-MM-DD` format.
          required: false
          schema:
            type: string
            format: date
        - in: query
          name: to
          description: >-
            **Exclusive** end date in `YYYY-MM-DD` format. The day specified is
            NOT included in the result. 

             To match a calendar month shown in the Control Panel or on your invoice, set `to` to the first day of the **following** month (e.g., `from=2026-04-01&to=2026-05-01` returns all of April 2026).
          required: false
          schema:
            type: string
            format: date
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                example:
                  ID:
                    back_m2:
                      bw: 0
                      cost: 0
                    back_m1:
                      bw: 36557298
                      cost: 0
                    back_m0:
                      bw: 1219004
                      cost: 0
                    back_d2:
                      bw: 82190
                      cost: 0
                    back_d1:
                      bw: 0
                      cost: 0
                    back_d0:
                      bw: 0
                      cost: 0
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