> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 异步请求

> 在本文中，我们将解释同步请求和异步请求的区别，突出异步流程的优势，并通过示例描述关键参数。

<Note>
  异步请求由 **Web Unlocker API** 和 **SERP API** 两款产品支持
</Note>

## 异步请求 VS 同步请求

处理 Web Unlocker API 和 SERP API 请求有两种方式：

* `default` **同步请求** - 发送请求并立即获得实时响应
* **异步请求** - 发送请求（无需等待立即响应），稍后通过指定 API 端点获取结果。回调时间通常为 5 分钟内，但高峰期可能长达 8 小时。响应自请求发送之时起最多存储 48 小时。

<Tip>
  异步请求推荐用于高流量请求，且 **不** 需要立即或实时响应，可以等待几分钟一次性获取所有响应。
</Tip>

### 为什么要使用异步请求？

* 成功率 99.99%
* 稳定性
* 灵活性 - 可以在自己选择的时间获取请求结果（无需在发送请求后立即等待响应）

### 工作原理

使用异步模式发送请求和接收响应是一个两步流程：

* **发送请求** - 请求包含搜索参数，返回 `response_ID`，并作为直接请求（即该请求将计费）。
* **收集响应** - 请求包含 `response_ID`，且不收费（即该请求不会计费）。如果调用仍在处理中的 `response_ID`，将收到 102 状态码。

<Note>
  我们自请求发送之时起最多存储 48 小时的响应。
</Note>

### 开始使用

<Steps>
  <Step title="启用 &#x22;异步请求&#x22;">
    在你的 Web Unlocker API 或 SERP API [zone](https://www.bright.cn/cp/zones) 中，进入“高级设置”，启用“异步请求”开关。

    <img src="https://mintcdn.com/brightdata/S8tFtc_KJjCQxqv1/images/scraping-automation/serp-api/asynchronous-requests/async_request_CP.png?fit=max&auto=format&n=S8tFtc_KJjCQxqv1&q=85&s=8f53a7f86abc9320071b47d284adff26" alt="" width="969" height="510" data-path="images/scraping-automation/serp-api/asynchronous-requests/async_request_CP.png" />
  </Step>

  <Step title="[可选] 设置 webhook（POST 或 GET）">
    你将在此处收到未来请求状态的通知

    <Note>
      webhook 也可按单个请求设置（参见下方“初始请求参数”）
    </Note>
  </Step>

  <Step title="发送异步请求">
    请求语法与同步请求略有不同，需要使用 [API key](/cn/api-reference/authentication#如何生成新的-api-key？) 进行认证。基本示例如下（更多请求参数见下方）：

    ```sh theme={null}
    curl -i --silent --compressed "https://api.brightdata.com/unblocker/req?customer=[ACCOUNT_ID]&zone=[zone_name]" \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer [API_KEY]" \
      -d '{"country":"us","query":{"q":"pizza","num":"100","hl":"en","gl":"au"}}'
    ```

    上述请求返回的响应中包含 `x-response-id` 头部，该 ID 为此请求的 `RESPONSE_ID`，将在下一步收集结果时使用。

    <Note>
      你可以在脚本中初始化请求时轻松保存 `RESPONSE_ID`，方法如下：

      ```js theme={null}
      RESPONSE_ID=$(
      	curl -i --silent --compressed "[https://api.brightdata.com/unblocker/req?customer=[ACCOUNT_ID]&zone=[zone_name]](https://api.brightdata.com/unblocker/req?customer=%5BACCOUNT_ID%5D&zone=%5BZONE_NAME%5D)" -H "Content-Type: application/json" -H "Authorization: Bearer API_KEY" -d '{"country":"us","query":{"q":"pizza","num":"100","hl":"en","gl":"au"}}' | sed -En 's/^x-response-id: (.*)/\1/p' | tr -d '\r'
      )
      ```
    </Note>
  </Step>

  <Step title="Webhook 通知">
    如果已设置 webhook，当请求准备就绪时你将立即收到通知，参数包括：`status`、`response_id`、`request_url` 和 `hook_data`（可选 - 如果请求中使用了 `webhook_data` 参数）。

    <Tip>
      ### 允许我们的 webhook IP

      异步 webhook 通知来自一对稳定 IP，请确保允许这些 IP：

      1. `100.27.150.189`
      2. `18.214.10.85`
    </Tip>
  </Step>

  <Step title="收集结果">
    使用步骤 3 获取的 `RESPONSE_ID`，发送如下请求：

    ```sh theme={null}
    curl -i --silent --compressed "https://api.brightdata.com/unblocker/get_result?customer=[ACCOUNT_ID]&zone=[zone_name]&response_id=${[RESPONSE_ID]}" \
       -H "Authorization: Bearer [API_KEY]"
    ```
  </Step>
</Steps>

## API - 创建请求 - `POST /{unblocker|serp}/req`

```sh Example theme={null}
curl -i --silent --compressed "https://api.brightdata.com/unblocker/req?customer=[ACCOUNT_ID]&zone=[zone_name]" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer [API_KEY]" \
  -d '{"url":"https://example.com?foo=bar","country":"us"}'
```

### 参数

<Warning>
  (\*) 必填参数
</Warning>

| 参数              | 类型               | 描述                                                        |
| --------------- | ---------------- | --------------------------------------------------------- |
| url (\*)        | String           | 请求的 URL                                                   |
| method          | String           | 请求使用的 HTTP 方法                                             |
| headers         | Object           | 请求使用的头部信息                                                 |
| body            | String or Object | 请求体。如果为对象，则序列化为 JSON，并将 Content-Type 设置为 application/json |
| country         | String           | 请求使用的国家（2 位字母代码）                                          |
| webhook\_url    | String           | 接收任务状态通知的 URL。如果不想设置默认 webhook 或希望每个请求 URL 不同，请使用此参数      |
| webhook\_method | String           | webhook\_url 使用的 HTTP 方法（GET 或 POST）                      |
| webhook\_data   | Any              | 随任务状态通知发送的数据                                              |

### SERP 特定参数

| 参数         | 类型          | 描述   |
| ---------- | ----------- | ---- |
| query (\*) | Object      |      |
| brd\_json  | 1 or "html" | 响应格式 |

```sh SERP Example theme={null}
curl -i --silent --compressed "https://api.brightdata.com/unblocker/req?customer=[ACCOUNT_ID]&zone=[zone_name]" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer [API_KEY]" \
  -d '{"country":"us","query":{"q":"pizza","num":"100","hl":"en","gl":"au"},"brd_json":"1"}'
```

## API - 收集响应 - `GET /{unblocker|serp}/get_result`

注意：`response_id` 来源于请求创建响应的 `x-response-id` 头部

```sh Example theme={null}
curl -k -v --compressed "https://api.brightdata.com/unblocker/get_result?customer={ACCOUNT_ID&zone={ASYNC_ZONE}&response_id={response_id}" \
  -H "Authorization: Bearer {API_Key}" \
  -o {Your_result_ouput_file}
```

### 参数

<Warning>
  (\*) 必填参数
</Warning>

| 参数                | 描述                   |
| ----------------- | -------------------- |
| response\_id (\*) | 任务 ID，在初始异步请求的响应头中获得 |

## 单个请求中的多查询

<Note>
  仅 SERP API
</Note>

异步请求支持在单个 API 请求中使用 `multi` 参数发送 2 个并行查询请求，而非 `query`。

这些并行请求使用相同的 peer IP 和会话，可用于收集额外数据、对比测试等，例如使用不同参数/值发送一对请求。它们使用相同 IP 和会话。

**条件：**

1. 仅支持启用异步的 zone（如上所示）
2. 仅支持 Google 搜索
3. 限制为 2 个请求
4. 按 2 个请求计费

**参数使用示例：**

<CodeGroup>
  ```js Same Keyword theme={null}
  multi: [
    {"keyword":"pizza","num":20},
    {"keyword":"pizza","num":100}
  ]
  ```

  ```js Different Keyword theme={null}
  multi: [
    {"keyword":"pizza"},
    {"keyword":"burger"}
  ]
  ```
</CodeGroup>

**请求示例：**

```sh Sample Request theme={null}
curl -v --compressed "https://api.brightdata.com/unblocker/req" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer {API_KEY}" \
  -d "{\"zone\":\"\$ZONE\",\"country\":\"us\",\"multi\":[{\"keyword\":\"pizza\",\"num\":20},{\"keyword\":\"pizza\",\"num\":100}]}"
```
