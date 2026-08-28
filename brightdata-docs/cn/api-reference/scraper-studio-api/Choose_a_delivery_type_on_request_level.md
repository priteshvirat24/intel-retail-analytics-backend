> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 在请求级别选择交付类型

与其为每种交付类型创建重复的爬虫，您可以使用 API 为每个任务选择交付类型。

<Frame>
  <img src="https://mintcdn.com/brightdata/0sd4eqxAli7ENzfc/images/api-reference/web-scraper-ide/Choose_a_delivery_type_on_request_level/hero-image.png?fit=max&auto=format&n=0sd4eqxAli7ENzfc&q=85&s=38a69cbd22918cfb14a42bcfe6b61bd4" alt="hero-image.png" width="1308" height="371" data-path="images/api-reference/web-scraper-ide/Choose_a_delivery_type_on_request_level/hero-image.png" />
</Frame>

<Steps>
  <Step title="更新您的爬虫">
    确保您的爬虫已更新到最新版本以提高成功率

    <Frame>
      <img src="https://mintcdn.com/brightdata/0sd4eqxAli7ENzfc/images/api-reference/web-scraper-ide/Choose_a_delivery_type_on_request_level/update-available.png?fit=max&auto=format&n=0sd4eqxAli7ENzfc&q=85&s=69084a9fa4c4c4e55f2ec8e9c86495cf" alt="update-available.png" width="1624" height="354" data-path="images/api-reference/web-scraper-ide/Choose_a_delivery_type_on_request_level/update-available.png" />
    </Frame>
  </Step>

  <Step title="将交付类型设置为批处理">
    <Frame>
      <img src="https://mintcdn.com/brightdata/0sd4eqxAli7ENzfc/images/api-reference/web-scraper-ide/Choose_a_delivery_type_on_request_level/type-batch.png?fit=max&auto=format&n=0sd4eqxAli7ENzfc&q=85&s=c62cfa06b6e5e54db7515891d5266b59" alt="type-batch.png" width="1613" height="353" data-path="images/api-reference/web-scraper-ide/Choose_a_delivery_type_on_request_level/type-batch.png" />

      <img src="https://mintcdn.com/brightdata/0sd4eqxAli7ENzfc/images/api-reference/web-scraper-ide/Choose_a_delivery_type_on_request_level/on-completion.png?fit=max&auto=format&n=0sd4eqxAli7ENzfc&q=85&s=3a0fb1c852560777644aaa2c0e6a9640" alt="on-completion.png" width="940" height="287" data-path="images/api-reference/web-scraper-ide/Choose_a_delivery_type_on_request_level/on-completion.png" />
    </Frame>

    当交付类型设置为实时时，批处理 API 将返回以下错误消息。

    ```json Error theme={null}
    "error": "Cannot trigger a batch job with a real-time scraper. Use /trigger_immediate endpoint instead"
    ```
  </Step>

  <Step title="使用首选 API 触发爬虫">
    <Tabs>
      <Tab title="启动批处理任务">
        `dca/trigger`

        [为批处理收集方法触发爬虫](/api-reference/scraper-studio-api/Trigger_a_scraper_for_batch_collection_method)

        <CodeGroup>
          ```sh Shell theme={null}
          curl "https://api.brightdata.com/dca/trigger?collector=ID_COLLECTOR&queue_next=1" -H "Content-Type: application/json" -H "Authorization: Bearer API_KEY" -d '[{"url":"https://targetwebsite.com/product_id/"}]'
          ```

          ```json Sample Response theme={null}
          {
              "collection_id":"j_l3daejgw1wnpjxxxxx",
              "start_eta":"2022-05-19T17:28:48.056Z"
          }
          ```
        </CodeGroup>
      </Tab>

      <Tab title="启动实时任务">
        `dca/trigger_immediate`

        [为实时收集触发爬虫](/api-reference/scraper-studio-api/Receive_data_from_real_time_work_scraper)

        <CodeGroup>
          ```sh Shell theme={null}
          curl "https://api.brightdata.com/dca/trigger_immediate?collector=ID_COLLECTOR" -H "Content-Type: application/json" -H "Authorization: Bearer API_KEY" -d '{"url":"https://targetwebsite.com/product_id/"}'
          ```

          ```json Sample Response theme={null}
          {
              "response_id":"z2805t1652973963340rg6252xxxxxx"
          }
          ```
        </CodeGroup>
      </Tab>
    </Tabs>

    <Note>
      批处理响应以 `j_****` 开头，实时响应以 `z****` 开头
    </Note>
  </Step>

  <Step title="接收数据">
    * [接收批处理数据](/api-reference/scraper-studio-api/Receive_batch_data)
    * [从实时爬虫接收数据](/api-reference/scraper-studio-api/Receive_data_from_real_time_work_scraper)
  </Step>
</Steps>
