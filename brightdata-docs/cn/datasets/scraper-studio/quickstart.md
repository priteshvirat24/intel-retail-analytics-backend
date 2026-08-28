> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Bright Data Scraper Studio API 快速开始

> 通过三个步骤触发已发布的 Bright Data Scraper Studio 爬虫并下载结构化 JSON，提供 cURL、Node.js 和 Python 可复制示例。

本指南将向 Bright Data Scraper Studio API 发送您的第一个请求：从您自己的代码触发一个已发布的爬虫，并取回结构化 JSON。

<Note>
  **还没有爬虫？** 爬虫是您在此处触发的已发布抓取程序。先用几分钟构建一个，拿到它的 Collector ID（`c_...`）后再回到本页：

  * **最快，在终端或编码助手中：** [使用 Bright Data CLI 构建爬虫](/cn/datasets/scraper-studio/build-with-the-cli)。三条命令，由 AI Agent 编写爬虫。在 Claude Code、Cursor 或 Codex 中可原样运行。
  * **无需写代码，在控制面板中：** [使用 AI Agent 构建爬虫](/cn/datasets/scraper-studio/ai-agent)。
  * **完全掌控：** [在 IDE 中构建爬虫](/cn/datasets/scraper-studio/develop-a-scraper)。

  本快速开始从您已拥有 Collector ID 之后开始。
</Note>

Bright Data Scraper Studio API 围绕两个 HTTP 调用构建：

1. `POST /dca/trigger`，将一个或多个输入入队并返回一个快照 ID。
2. `GET /dca/dataset?id=<snapshot_id>`，在快照就绪后提供该快照。

<Tip>
  对于包含 1 到 10 个输入的爬虫，首条记录通常约需 3 分钟。
</Tip>

## 前置条件

* 一个已激活且已绑定支付方式的 [Bright Data 账户](https://brightdata.com/?hs_signup=1\&utm_source=docs)
* 一个来自 [账户设置 → API Tokens](https://brightdata.com/cp/setting) 的 **API token**
* 一个 **Collector ID**，来自您用 [CLI](/cn/datasets/scraper-studio/build-with-the-cli)、[AI Agent](/cn/datasets/scraper-studio/ai-agent) 或 [IDE](/cn/datasets/scraper-studio/develop-a-scraper) 构建的爬虫；该 ID 以 `c_` 开头

将这两个值设置为环境变量一次，即可在下方所有代码片段中复用：

```bash theme={null}
export BRIGHT_DATA_API_TOKEN="your_api_token_here"
export BRIGHT_DATA_COLLECTOR_ID="c_xxxxxxxxxxxxxxxx"
```

## 发送您的第一个请求

<Steps>
  <Step title="为每个调用进行身份验证">
    每个 Bright Data Scraper Studio API 调用都使用 bearer-token 身份验证。为每个请求添加以下请求头：

    ```http theme={null}
    Authorization: Bearer YOUR_BRIGHT_DATA_API_TOKEN
    ```

    缺失或无效的 token 会返回 `401 Unauthorized`。
  </Step>

  <Step title="触发您的爬虫">
    将您希望爬虫处理的输入作为 JSON 数组放入请求体。数组中的每个对象都必须匹配您构建爬虫时定义的输入 schema。默认 schema 是单个 `url` 字段。

    <CodeGroup>
      ```bash cURL theme={null}
      curl -X POST \
        "https://api.brightdata.com/dca/trigger?collector=$BRIGHT_DATA_COLLECTOR_ID&queue_next=1" \
        -H "Authorization: Bearer $BRIGHT_DATA_API_TOKEN" \
        -H "Content-Type: application/json" \
        -d '[
          {"url": "https://ecommerce-shop-brd.vercel.app/product/echo-portable-speaker"},
          {"url": "https://ecommerce-shop-brd.vercel.app/product/nimbus-cloud-storage"}
        ]'
      ```

      ```python Python theme={null}
      import os
      import requests

      API_TOKEN    = os.environ["BRIGHT_DATA_API_TOKEN"]
      COLLECTOR_ID = os.environ["BRIGHT_DATA_COLLECTOR_ID"]

      response = requests.post(
          f"https://api.brightdata.com/dca/trigger?collector={COLLECTOR_ID}&queue_next=1",
          headers={
              "Authorization": f"Bearer {API_TOKEN}",
              "Content-Type": "application/json",
          },
          json=[
              {"url": "https://ecommerce-shop-brd.vercel.app/product/echo-portable-speaker"},
              {"url": "https://ecommerce-shop-brd.vercel.app/product/nimbus-cloud-storage"},
          ],
      )
      response.raise_for_status()
      snapshot_id = response.json()["collection_id"]
      print(snapshot_id)  # j_abc123def456
      ```

      ```js Node.js theme={null}
      const triggerUrl =
        `https://api.brightdata.com/dca/trigger` +
        `?collector=${process.env.BRIGHT_DATA_COLLECTOR_ID}&queue_next=1`;

      const response = await fetch(triggerUrl, {
        method: "POST",
        headers: {
          Authorization: `Bearer ${process.env.BRIGHT_DATA_API_TOKEN}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify([
          { url: "https://ecommerce-shop-brd.vercel.app/product/echo-portable-speaker" },
          { url: "https://ecommerce-shop-brd.vercel.app/product/nimbus-cloud-storage" },
        ]),
      });

      const { collection_id: snapshotId } = await response.json();
      console.log(snapshotId); // j_abc123def456
      ```
    </CodeGroup>

    Bright Data Scraper Studio API 返回一个快照 ID：

    ```json theme={null}
    {
      "collection_id": "j_abc123def456"
    }
    ```

    请保存此 ID。您将在第 3 步中把它作为 `snapshot_id` 使用。

    <Note>
      `queue_next=1` 会立即运行您的输入。省略它（或设为 `0`）会将这些输入排在同一爬虫尚未完成的工作之后。
    </Note>
  </Step>

  <Step title="轮询直到就绪，然后下载">
    同一个 `/dca/dataset` 端点同时提供进行中和已就绪的响应。每 5 秒轮询一次，直到响应是一个 JSON 数组。

    <CodeGroup>
      ```bash cURL theme={null}
      # 每 5 秒轮询一次，直到响应是 JSON 数组（而非对象）。
      while :; do
        response=$(curl -s \
          "https://api.brightdata.com/dca/dataset?id=$SNAPSHOT_ID" \
          -H "Authorization: Bearer $BRIGHT_DATA_API_TOKEN")
        if [[ "${response:0:1}" == "[" ]]; then
          echo "$response" > results.json
          break
        fi
        sleep 5
      done
      ```

      ```python Python theme={null}
      import json
      import time

      while True:
          response = requests.get(
              f"https://api.brightdata.com/dca/dataset?id={snapshot_id}",
              headers={"Authorization": f"Bearer {API_TOKEN}"},
          )
          response.raise_for_status()
          body = response.json()
          if isinstance(body, list) and body:
              with open("results.json", "w") as f:
                  json.dump(body, f, indent=2)
              break
          time.sleep(5)
      ```

      ```js Node.js theme={null}
      const datasetUrl =
        `https://api.brightdata.com/dca/dataset?id=${snapshotId}`;

      while (true) {
        const response = await fetch(datasetUrl, {
          headers: { Authorization: `Bearer ${process.env.BRIGHT_DATA_API_TOKEN}` },
        });
        const body = await response.json();
        if (Array.isArray(body) && body.length > 0) {
          await fs.writeFile("results.json", JSON.stringify(body, null, 2));
          break;
        }
        await new Promise((r) => setTimeout(r, 5000));
      }
      ```
    </CodeGroup>

    在快照构建期间，响应是一个状态对象：

    ```json theme={null}
    { "status": "building" }
    ```

    快照就绪后，响应是一个 JSON 数组。默认情况下每个成功的输入对应一行：

    ```json theme={null}
    [
      {
        "url": "https://ecommerce-shop-brd.vercel.app/product/echo-portable-speaker",
        "title": "Echo Portable Speaker",
        "price": 49.99,
        "availability": "in stock",
        "input": { "url": "https://ecommerce-shop-brd.vercel.app/product/echo-portable-speaker" }
      },
      {
        "url": "https://ecommerce-shop-brd.vercel.app/product/nimbus-cloud-storage",
        "title": "Nimbus Cloud Storage",
        "price": 12.99,
        "availability": "in stock",
        "input": { "url": "https://ecommerce-shop-brd.vercel.app/product/nimbus-cloud-storage" }
      }
    ]
    ```

    确切的字段集取决于您构建爬虫时定义的输出 schema。
  </Step>
</Steps>

## 这需要多长时间？

首条记录通常在一分钟内到达，但总耗时取决于爬虫和目标站点。以一个典型的电商商品页爬虫为基准测量：

| 输入数量           | 典型实际耗时                                                                                               |
| -------------- | ---------------------------------------------------------------------------------------------------- |
| 1 到 10 个 URL   | 30 到 90 秒                                                                                            |
| 11 到 100 个 URL | 2 到 5 分钟                                                                                             |
| 100 个以上 URL    | 5 分钟以上。请改用[推送交付](/cn/api-reference/scraper-studio-api/Choose_a_delivery_type_on_request_level)，而非轮询。 |

对于长时间运行的作业，请将轮询替换为[推送交付目标](/cn/api-reference/scraper-studio-api/Choose_a_delivery_type_on_request_level)（webhook、S3、GCS、Azure、SFTP 或电子邮件），这样快照就绪时由 Bright Data 主动通知您。

## 这些 ID 分别代表什么？

Bright Data Scraper Studio 中会出现三个标识符。它们容易混淆，因为触发响应对某个值使用的名称，与另一个端点读取它时使用的名称不同。

| 术语                                     | 形如                   | 它标识什么                                                                       |
| -------------------------------------- | -------------------- | --------------------------------------------------------------------------- |
| **Collector ID**                       | `c_xxxxxxxxxxxxxxxx` | 已发布的爬虫定义。稳定不变。您将它作为 `/dca/trigger` 上的 `collector` 查询参数传入。                   |
| **Collection ID**（返回为 `collection_id`） | `j_xxxxxxxxxxxxxxxx` | 爬虫的一次运行。触发响应的字段名为 `collection_id`，但其他所有端点都以 `snapshot_id` 指代同一个值。它们是同一个字符串。 |
| **Dataset**                            | 一个 JSON 数组           | 一次运行产出的结果行。运行完成后 `/dca/dataset` 端点返回它。                                      |

<Tip>
  将触发响应中的 `collection_id` 视为其他所有地方的 `snapshot_id`。它们是同一个值的两个名称。
</Tip>

## 可能遇到哪些错误？

| 状态                         | 含义                          | 修复方法                                                                          |
| -------------------------- | --------------------------- | ----------------------------------------------------------------------------- |
| `401 Unauthorized`         | token 缺失、格式错误或已吊销           | 从 [账户设置 → API Tokens](https://brightdata.com/cp/setting) 重新复制                 |
| `404 Not Found`            | Collector ID 不存在，或您的账户无访问权限 | 在 [Scraper Studio](https://brightdata.com/cp/scrapers) 中打开该爬虫并重新复制 ID         |
| `422 Unprocessable Entity` | 请求体中的对象与爬虫的输入 schema 不匹配    | 对照爬虫的 **Inputs** 标签页确认字段名                                                     |
| `5xx`                      | Bright Data API 暂时性错误       | 使用指数退避重试，例如 1s、2s、4s                                                          |
| `[]`（空数组）                  | 快照没有任何行，或快照已过期              | 批处理结果保留 16 天，实时结果保留 7 天。参见 [规格说明](/cn/datasets/scraper-studio/specifications) |

## 使用生产级入门模板

以下开源仓库正是上面这些调用，并经过加固：环境变量配置、针对暂时性故障的重试/退避、库辅助函数和完整的 `README`。Fork 任意一个，30 秒内即可拥有一个可运行的客户端。

<CardGroup cols={2}>
  <Card title="Node.js 入门模板" icon="node-js" href="https://github.com/brightdata/bright-data-scraper-studio-nodejs-project">
    Node 18+、ES modules、dotenv、重试/退避，约 150 行代码
  </Card>

  <Card title="Python 入门模板" icon="python" href="https://github.com/brightdata/bright-data-scraper-studio-python-project">
    Python 3.8+、`requests`、`python-dotenv`、重试/退避，约 150 行代码
  </Card>
</CardGroup>

两个仓库都附带 CodeSandbox devcontainer，无需任何本地设置即可在浏览器中 fork 并运行。

## 后续步骤

<CardGroup cols={2}>
  <Card title="选择交付类型" icon="paper-plane" href="/cn/api-reference/scraper-studio-api/Choose_a_delivery_type_on_request_level">
    跳过轮询。让 Bright Data 在快照就绪时将结果推送到 webhook、S3、GCS 或电子邮件。
  </Card>

  <Card title="触发批量收集" icon="layer-group" href="/cn/api-reference/scraper-studio-api/Trigger_a_scraper_for_batch_collection_method">
    在单个请求中发送数百或数千个输入，并分批接收结果。
  </Card>

  <Card title="运行同步实时作业" icon="bolt" href="/cn/api-reference/scraper-studio-api/initiate-a-realtime-job/sync-realtime-job">
    适用于低输入量、对延迟敏感的工作负载。在单个 HTTP 调用中触发并接收结果。
  </Card>

  <Card title="构建新爬虫" icon="screwdriver-wrench" href="/cn/datasets/scraper-studio/build-with-the-cli">
    需要一个尚不存在的爬虫？用 CLI、AI Agent 或 IDE 构建一个。
  </Card>
</CardGroup>

## 常见问题

<AccordionGroup>
  <Accordion title="一开始要如何创建爬虫？">
    用以下三种路径之一构建 Scraper Studio 爬虫，然后在此处使用它返回的 Collector ID（`c_...`）：

    * **[Bright Data CLI](/cn/datasets/scraper-studio/build-with-the-cli)** 最快。运行 `bdata scraper create <url> "<要提取的数据>"`，AI Agent 会编写爬虫。该 CLI 在 Claude Code、Cursor 或 Codex 中可原样运行。
    * **[AI Agent](/cn/datasets/scraper-studio/ai-agent)** 在控制面板中根据一段自然语言提示词构建爬虫，无需写代码。
    * **[IDE](/cn/datasets/scraper-studio/develop-a-scraper)** 让您完全掌控爬虫代码。
  </Accordion>

  <Accordion title="Collection API 和 AI Flow API 有什么区别？">
    **Collection API**（`/dca/*`，即本页）运行一个现有爬虫来**获取数据**。
    **[AI Flow API](/cn/api-reference/scraper-studio-api/ai-flow/overview)** 运行 AI Agent 来**创建或自我修复**爬虫。
    大多数将 Bright Data Scraper Studio 集成进产品的开发者使用 Collection API。
  </Accordion>

  <Accordion title="我可以在同一个请求中发送不同形状的输入吗？">
    可以，只要数组中的每个对象都符合爬虫的输入 schema。如果您的爬虫同时接受 `url` 和 `keyword` 作为输入字段，您可以在一个请求中混用它们。未包含的字段被视为 `null`。
  </Accordion>

  <Accordion title="如何只重试失败的输入而不重新运行已成功的输入？">
    在 [My Scrapers](https://brightdata.com/cp/scrapers) 中打开快照并点击 **Last errors**，查看哪些输入失败及原因。在一个新的 `POST /dca/trigger` 调用中仅重新触发那些输入。
  </Accordion>

  <Accordion title="有速率限制吗？">
    有。每爬虫的并发限制按账户应用。当前限制参见 [规格说明](/cn/datasets/scraper-studio/specifications)。上面链接的入门模板已为暂时性 `5xx` 响应实现指数退避。
  </Accordion>
</AccordionGroup>
