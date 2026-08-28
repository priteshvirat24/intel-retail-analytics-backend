> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 同步触发爬虫进行实时数据采集

> 触发同步实时 Scraper Studio 采集。POST /dca/crawl 会保持请求打开，直到爬虫完成或达到超时，然后以 JSON 形式直接返回数据。

同步实时端点会保持 HTTP 请求处于打开状态，直到爬虫完成或达到 `timeout`，然后以 JSON 形式直接返回采集到的数据。这与[异步实时端点](/cn/api-reference/scraper-studio-api/initiate-a-realtime-job/async-realtime-job)不同，后者会立即返回一个 `response_id`。

<Warning>
  你只能触发**单输入** API。确保有效载荷是**一个对象，而不是对象数组**。
</Warning>

## 超时行为

`timeout` 查询参数的取值必须在 `25s` 到 `50s` 之间。

* 如果爬虫在超时时间内完成，响应返回 `200 OK` 以及采集到的数据。
* 如果到达超时时爬虫仍在运行，响应返回 `202 Accepted` 以及一个 `response_id`。使用该 `response_id` 调用[实时数据端点](/cn/api-reference/scraper-studio-api/Receive_data_from_real_time_work_scraper)以异步方式获取结果。

## 何时使用同步实时

在以下情况下使用**同步实时**（`POST /dca/crawl`）：

* 你需要在同一个 HTTP 请求中获得结果。
* 你只发送单个输入。
* 你的客户端可以保持请求打开，直到采集完成。
* 采集通常在配置的超时时间内完成。

在以下情况下使用[**异步实时**](/cn/api-reference/scraper-studio-api/initiate-a-realtime-job/async-realtime-job)（`POST /dca/trigger_immediate`）：

* 你希望先触发采集，稍后再获取结果。
* 你不希望保持 HTTP 请求处于打开状态。

在以下情况下使用[**批量采集**](/cn/api-reference/scraper-studio-api/Trigger_a_scraper_for_batch_collection_method)：

* 你需要在一次运行中处理多个输入。


## OpenAPI

````yaml api-reference/web-scraper-ide-rest-api POST /dca/crawl
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
  /dca/crawl:
    post:
      description: >-
        Trigger a synchronous real-time run of a Scraper Studio collector.


        The request stays open until the scraper finishes or the `timeout` is
        reached, then returns the collected data directly as JSON. This is the
        difference from the [async real-time
        endpoint](/api-reference/scraper-studio-api/initiate-a-realtime-job/async-realtime-job),
        which returns a `response_id` immediately.


        If the scraper is still running when the `timeout` is reached, the
        response returns `202 Accepted` with a `response_id`. Use that
        `response_id` with the [Realtime Data
        endpoint](/api-reference/scraper-studio-api/Receive_data_from_real_time_work_scraper)
        to retrieve the result asynchronously.
      parameters:
        - name: collector
          in: query
          required: true
          schema:
            type: string
            example: c_abc123
          description: A unique identification of the collector to run
        - name: timeout
          in: query
          required: true
          schema:
            type: string
            example: 50s
          description: >-
            How long the request stays open while waiting for the result. Must
            be between 25s and 50s. If the scraper finishes within the timeout,
            the response returns `200 OK` with the collected data. If the
            scraper is still running when the timeout is reached, the response
            returns `202 Accepted` with a `response_id`.
        - name: version
          in: query
          schema:
            type: string
          description: Set to `dev` to trigger the development version of the scraper
      requestBody:
        required: true
        description: >-
          A single input object. The fields must match the input schema defined
          for the collector. A URL-based scraper may require `url`, while a
          search scraper may require fields such as `keyword` and `location`.
        content:
          application/json:
            schema:
              type: object
              additionalProperties: true
              description: >-
                Single input object whose fields match the collector input
                schema.
              properties:
                url:
                  type: string
                  format: uri
                  description: >-
                    Example field for collectors that take a target URL. Replace
                    with the fields your collector expects.
            examples:
              request:
                value:
                  url: https://www.ebay.com/itm/326972541236
      responses:
        '200':
          description: OK
          content:
            application/json:
              examples:
                response:
                  value:
                    - product_title: >-
                        Apple iPad 11th Gen, 128 GB, Wi-Fi + 5G, 11 in - Silver
                        - BRAND NEW SEALED
                      price:
                        value: 324.99
                        currency: USD
                        symbol: $
                      condition: >-
                        New: A brand-new, unused, unopened, undamaged item in
                        its original packaging (where packaging is ...
                      seller_feedback_percentage: 100% positive feedback
                      seller_items_sold: 173 items sold
                      seller_since: Joined Nov 2012
                      item_specifics:
                        brand: Apple
                        model: Apple iPad (11th generation)
                        processor_model: Apple A16 Bionic
                        operating_system: iPadOS
                      storage_options: []
                      seller_ratings:
                        accurate_description: '--'
                        shipping_cost: '--'
                        shipping_speed: '--'
                        communication: '4.9'
                      product_images:
                        - >-
                          https://i.ebayimg.com/images/g/4a8AAeSw7x5pboS0/s-l1600.webp
                        - >-
                          https://i.ebayimg.com/images/g/4a8AAeSw7x5pboS0/s-l1600.webp
                      feedback_count: 36
                      financing_options:
                        monthly_payment:
                          value: 13.99
                          currency: USD
                          symbol: $
                        payment_plan_duration: (12 monthly payment plan)
                        apr: 13.99%
                      input:
                        url: https://www.ebay.com/itm/326972541236
                      seller_namestest: jwc8109
        '202':
          description: Timeout waiting for crawl results
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: Error code indicating the type of timeout
                  message:
                    type: string
                    description: >-
                      Detailed message about the timeout and instructions for
                      polling results
                  response_id:
                    type: string
                    description: >-
                      Unique identifier for the response to be used for polling
                      results
                required:
                  - error
                  - message
                  - response_id
              example:
                error: crawl_results_timeout
                message: >-
                  Timed out waiting for crawl results (timeout=NaNs). The page
                  crawl is continuing in the background, you can poll a GET
                  request to
                  https://api.brightdata.com/dca/get_result?response_id=ID until
                  the result is ready
                response_id: RESPONSE_ID
      x-codeSamples:
        - lang: py
          label: Python SDK
          source: |-
            # Install: pip install brightdata-sdk
            from brightdata import BrightDataClient

            async with BrightDataClient(api_key="YOUR_API_KEY") as client:
                # Run and get results in one call (sync)
                data = await client.scraper_studio.run(
                    collector="c_abc123",
                    input={"url": "https://www.ebay.com/itm/326972541236"},
                )
                print(data)
        - lang: js
          label: JavaScript SDK
          source: >-
            // Install: npm install @brightdata/sdk

            import { bdclient } from '@brightdata/sdk';


            const client = new bdclient({ apiKey: 'YOUR_API_KEY' });


            // Run and get results in one call (sync)

            const results = await
            client.scraperStudio.run('c_your_collector_id', {
              input: { url: 'https://www.ebay.com/itm/326972541236' },
            });


            console.log(results);


            await client.close();
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