> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 故障排除

> 本节涵盖在直接使用 Bright Data 的 Web Unlocker API、SERP API、Scrapers、Marketplace Dataset API 和 Web Scraper IDE 时可能遇到的错误。

## 代理网络故障排除

代理网络的错误代码及描述可以在[这里](/cn/proxy-networks/errorCatalog)找到

## 数据集 API 错误

### 200 成功（带错误/状态信息）

虽然从技术上讲这是一个成功的 HTTP 状态，但这些响应携带指示操作中正在进行的过程或特定失败的消息，需要开发者注意。

| 消息                                                                           | 相关端点                                     | 原因                                | 建议操作                                                                     |
| :--------------------------------------------------------------------------- | :--------------------------------------- | :-------------------------------- | :----------------------------------------------------------------------- |
| `{status: "STATUS", message: "Snapshot is not ready yet, try again in 10s"}` | `GET /datasets/v3/snapshot/:snapshot_id` | 快照仍在构建或处理中。                       | 这是一个临时状态。请在建议的延迟后再次轮询该端点（例如 `10s`）。                                      |
| `{status: "building", message: "Snapshot is building, try again in 10s"}`    | `GET /datasets/v3/snapshot/:snapshot_id` | 快照正在构建中。                          | 在建议的延迟后再次轮询端点。                                                           |
| `{status: "failed", error_message: "ERROR_MESSAGE"}`                         | `GET /datasets/v3/progress/:snapshot_id` | 集合或快照操作失败。                        | 检查具体的 `ERROR_MESSAGE` 了解详细信息。审核您的集合设置和输入。                                |
| `Something went wrong. Our team is looking into it.`                         | `GET /datasets/v3/progress/:snapshot_id` | 监控期间发生内部系统错误。                     | 这表明是 Bright Data 端的问题。您无需立即采取行动，但如果问题持续，请联系支持。                           |
| `Account is suspended`                                                       | `GET /datasets/v3/progress/:snapshot_id` | 您的 Bright Data 账户已被暂停，通常由于账户余额不足。 | 充值账户余额。如果暂停超过 24 小时，之前分配的静态 IP 可能会被释放。请访问 Bright Data Zones 页面获取更新后的 IP。 |
| `Account is new, please activate it in account settings. URL`                | `GET /datasets/v3/progress/:snapshot_id` | 新创建的账户需要激活。                       | 登录 Bright Data 账户设置并完成激活过程。                                              |
| `No data found in discovery`                                                 | `GET /datasets/v3/progress/:snapshot_id` | 集合的发现阶段未产生任何数据。                   | 审核您的发现配置和目标设置。                                                           |
| `Snapshot is empty`                                                          | `GET /datasets/v3/progress/:snapshot_id` | 已完成的快照不包含数据。                      | 检查集合过程和数据集配置以确保正在收集数据。                                                   |
| `Failed to deliver snapshot`                                                 | `GET /datasets/v3/progress/:snapshot_id` | 在将收集到的数据交付到存储过程中出现错误。             | 审核您的交付选项并重试。如果问题持续，请联系支持。                                                |
| `Failed to download response`                                                | `GET /datasets/v3/progress/:snapshot_id` | 尝试下载响应时发生错误。                      | 可能是临时网络问题或 Bright Data 端的问题。重试请求。                                        |
| `Failed to trigger collector`                                                | `GET /datasets/v3/progress/:snapshot_id` | 内部错误阻止了收集器触发。                     | 重试请求。如果问题持续，请联系支持。                                                       |
| `Internal server error`                                                      | `GET /datasets/v3/progress/:snapshot_id` | 通用内部服务器错误。                        | 重试请求。如果问题持续，请联系支持。                                                       |
| `Input validation failed: DETAILS`                                           | `GET /datasets/v3/progress/:snapshot_id` | 输入存在内部验证错误。                       | 对照 API 文档审核您的输入。如果输入正确，请联系支持。                                            |

### 202 已接受

**原因:** 请求已被接受以进行处理，但操作尚未完成。通常这是指资源正在准备或构建的临时状态。

| 消息                                                                           | 相关端点                                     | 原因          | 建议操作                                |
| :--------------------------------------------------------------------------- | :--------------------------------------- | :---------- | :---------------------------------- |
| `{status: "STATUS", message: "Snapshot is not ready yet, try again in 10s"}` | `GET /datasets/v3/snapshot/:snapshot_id` | 快照仍在构建或处理中。 | 这是一个临时状态。请在建议的延迟后再次轮询该端点（例如 `10s`）。 |
| `{status: "building", message: "Snapshot is building, try again in 10s"}`    | `GET /datasets/v3/snapshot/:snapshot_id` | 快照正在构建中。    | 在建议的延迟后再次轮询端点。                      |

### 400 错误请求

**原因:** 您的请求无效、格式错误或包含不正确的参数。这是常见的客户端错误，表示请求构建存在问题。

| 消息                                                                                                                                     | 相关端点                                                                                     | 原因                           | 建议操作                                         |
| :------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------- | :--------------------------- | :------------------------------------------- |
| `{validation_errors: [ERRORS]}`                                                                                                        | Scrapers Library 多个端点, `GET /datasets/v3/snapshots`, Marketplace Dataset API             | 请求输入的通用验证失败；ERRORS 数组提供具体细节。 | 检查 ERRORS 数组中的具体验证问题并修正请求内容。                 |
| `dataset missing`                                                                                                                      | `POST /datasets/v3/trigger`                                                              | 请求中缺少必要的数据集 ID 或名称。          | 确保请求中包含数据集标识符。                               |
| `Invalid attachments`                                                                                                                  | `POST /datasets/v3/trigger`                                                              | 提供的附件无效。                     | 验证附件的格式和内容。                                  |
| `This dataset is not allowed for API`                                                                                                  | `POST /datasets/v3/trigger`                                                              | 指定的数据集不能通过 API 触发。           | 确认数据集已配置为允许 API 访问。                          |
| `This dataset is not ready yet`                                                                                                        | `POST /datasets/v3/trigger`                                                              | 数据集仍在准备中或未处于活动状态。            | 等待数据集准备就绪后再尝试触发集合。                           |
| `No data to trigger`                                                                                                                   | `POST /datasets/v3/trigger`                                                              | 数据集没有定义有效输入或配置以启动集合。         | 确保数据集定义了有效输入。                                |
| `Should be at least LIMIT inputs`                                                                                                      | `POST /datasets/v3/trigger`                                                              | 请求未满足最少输入数量要求。               | 提供至少指定的 `LIMIT` 数量输入。                        |
| `Snapshot is expired`                                                                                                                  | `GET /datasets/v3/snapshot/:snapshot_id`, `POST /datasets/v3/deliver/:snapshot_id`       | 您尝试访问的快照已过有效期。               | 触发新的集合以生成新的快照。                               |
| `Snapshot is empty`                                                                                                                    | `GET /datasets/v3/snapshot/:snapshot_id`, `POST /datasets/v3/deliver/:snapshot_id`       | 收集的快照不包含数据。                  | 检查集合过程和数据集配置以确保正在收集数据。                       |
| `Snapshot is not ready`                                                                                                                | `GET /datasets/v3/snapshot/:snapshot_id/parts`, `POST /datasets/v3/deliver/:snapshot_id` | 快照仍在处理中或未准备好下载/交付。           | 等待快照完成处理。您可以通过“Monitor progress”端点监控状态。      |
| `Snapshot input does not exist`                                                                                                        | `GET /datasets/v3/snapshot/:snapshot_id/input`                                           | 与快照相关的输入文件未找到。               | 验证 `snapshot_id` 并确保输入文件成功生成。                |
| `Snapshot is not running`                                                                                                              | `POST /datasets/v3/snapshot/:snapshot_id/cancel`                                         | 尝试取消未激活的集合。                  | 在尝试取消前检查集合状态。                                |
| `Deliver options are missing`                                                                                                          | `POST /datasets/v3/deliver/:snapshot_id`                                                 | 未提供必要的交付配置（如目的地信息）。          | 确保请求中包含所有必要的交付选项。                            |
| `Snapshot is too big for single file delivery`                                                                                         | `POST /datasets/v3/deliver/:snapshot_id`                                                 | 收集的数据超过单文件交付限制。              | 考虑将快照分多部分交付或调整集合范围。                          |
| `Batch size should be at least MIN_BATCH_SIZE`                                                                                         | `POST /datasets/v3/deliver/:snapshot_id`                                                 | 指定的交付批量大小低于最小允许值。            | 将 `batch_size` 至少增加到 `MIN_BATCH_SIZE`。       |
| `Type <span class="math-inline">\{init\_types\.compr\_update is no longer supported\. Use '</span>{init_types.discover_all}' instead.` | Marketplace Dataset API                                                                  | 请求的操作类型已弃用。                  | 更新请求以使用推荐的操作类型 `${init_types.discover_all}`。 |
| `Type ${init_types.update_existing} is no longer supported.`                                                                           | Marketplace Dataset API                                                                  | 请求的操作类型不再支持。                 | 使用受支持的操作类型。                                  |
| `Type ${init_types.discover_new} is no longer supported.`                                                                              | Marketplace Dataset API                                                                  | 请求的操作类型不再支持。                 | 使用受支持的操作类型。                                  |
| `Initiation reason is required.`                                                                                                       | Marketplace Dataset API                                                                  | 请求缺少必要的启动原因。                 | 在请求中包含 `initiation reason`。                  |
| `This feature is not available.`                                                                                                       | Marketplace Dataset API                                                                  | 数据集不支持请求的功能。                 | 检查数据集功能并相应调整请求。                              |
| `This dataset was rejected.`                                                                                                           | Marketplace Dataset API                                                                  | 数据集被拒绝，无法处理。                 | 此数据集无法使用。有关更多信息，请联系 Bright Data 支持。          |
| `This dataset is not ready.`                                                                                                           | Marketplace Dataset API                                                                  | 数据集未准备好处理。                   | 等待数据集准备就绪。                                   |
| `This dataset does not support discovery. Supported types: ['${init_types.url_collection}']`                                           | Marketplace Dataset API                                                                  | 数据集不支持请求的发现类型。               | 使用受支持的发现类型，如 `url_collection`。               |
| `Incorrect discovery collector id.`                                                                                                    | Marketplace Dataset API                                                                  | 请求中提供的发现收集器 ID 无效。           | 验证发现收集器 ID。                                  |
| `View not found.`                                                                                                                      | Marketplace Dataset API                                                                  | 请求的视图不可用。                    | 检查视图名称和数据集可用视图。                              |
| `This dataset does not support collection.`                                                                                            | Marketplace Dataset API                                                                  | 数据集不支持请求的集合操作。               | 使用数据集支持的操作类型。                                |
| `Batch size must be at least 1000.`                                                                                                    | Marketplace Dataset API                                                                  | 请求中指定的批量大小低于最小允许值。           | 将 `batch_size` 至少增加到 1000。                   |
| `{error: 'Snapshot failed'}`                                                                                                           | Marketplace Dataset API                                                                  | 快照操作失败。                      | 审查集合过程以查明潜在问题。                               |
| `{error: 'Invalid snapshot type'}`                                                                                                     | Marketplace Dataset API                                                                  | 请求中提供的快照类型无效。                | 使用有效的快照类型。                                   |

### 401 未授权

**原因:** 请求缺少有效的 API 认证凭据。

| 消息             | 相关端点                    | 原因                      | 建议操作                       |
| :------------- | :---------------------- | :---------------------- | :------------------------- |
| `Unauthorized` | Marketplace Dataset API | 提供的 API key 或认证凭据无效或缺失。 | 确保 API key 和认证凭据正确并包含在请求中。 |

### 402 需要付款

**原因:** 您的账户余额不足以处理请求的 API 操作。

| 消息                                                                                                                                                                                | 相关端点                    | 原因             | 建议操作                            |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------- | :------------- | :------------------------------ |
| `{error: 'Your current balance is insufficient to process this data collection request. Please add funds to your account or adjust your request to continue. ($220 is missing)'}` | Marketplace Dataset API | 用户账户余额不足以处理请求。 | 向 Bright Data 账户充值或调整请求参数以降低费用。 |

### 403 禁止访问

**原因:** 您没有权限访问请求的 API 资源，或者请求被 Bright Data 策略阻止。

| 消息                     | 相关端点                    | 原因               | 建议操作                 |
| :--------------------- | :---------------------- | :--------------- | :------------------- |
| `Access denied.`       | Marketplace Dataset API | 用户没有访问该资源的必要权限。  | 检查账户权限并确保您可以访问请求的资源。 |
| `Cannot skip billing.` | Marketplace Dataset API | 用户尝试跳过计费，这是不允许的。 | 计费                   |

### 404 未找到

**原因:** 您尝试访问的特定 API 资源在系统中不存在。当尝试访问数据集、快照、交付或不存在的一般请求时，可能会遇到此错误。

| 消息                        | 相关端点                                                 | 原因                                | 建议操作                           |
| :------------------------ | :--------------------------------------------------- | :-------------------------------- | :----------------------------- |
| `dataset does not exist`  | `POST /datasets/v3/trigger`, Marketplace Dataset API | 指定的数据集 ID 或名称未找到。                 | 再次检查请求中的数据集标识符。                |
| `Snapshot does not exist` | Scrapers Library 多个端点, Marketplace Dataset API       | 提供的 snapshot\_id 不对应现有快照。         | 验证 snapshot\_id。它可能错误、过期或从未存在。 |
| `Delivery does not exist` | `GET /datasets/v3/delivery/:delivery_id`             | 提供的 delivery\_id 未找到。             | 确认 delivery\_id 是否正确。          |
| `Request not found`       | Web Scraper IDE API, Marketplace Dataset API         | 请求中指定的 request ID 或其他请求详情未在系统中找到。 | 验证请求详情，确保其有效。                  |
| `Page not found`          | 无效 URL，可能表示 URL 已损坏或失效（特定于 Web Unlocker API）         | 验证 URL 是否正确且有效。                   |                                |

### 422 无法处理的实体

**原因:** API 请求格式正确，但由于提供的数据存在语义错误，无法处理。

| 消息                                                     | 相关端点                    | 原因                     | 建议操作                 |
| :----------------------------------------------------- | :---------------------- | :--------------------- | :------------------- |
| `{error: 'Provided filter did not match any records'}` | Marketplace Dataset API | 请求中提供的过滤器未匹配数据集中的任何记录。 | 调整过滤器条件以匹配数据集中存在的记录。 |

### 429 请求过多

**原因:** 当使用 API 时，您已超出速率限制或账户/数据集允许的最大并行任务数。

| 消息                                                                                    | 相关端点                                                       | 原因                                                                         | 建议操作                                            |
| :------------------------------------------------------------------------------------ | :--------------------------------------------------------- | :------------------------------------------------------------------------- | :---------------------------------------------- |
| `You have too many running jobs for this dataset.`                                    | `POST /datasets/v3/trigger`                                | 已达到该数据集集合任务的并发限制。                                                          | 等待一些正在运行的任务完成。对于大规模工作负载，可考虑将多个输入合并为单个集合请求以减少并发。 |
| `{error: 'Maximum limit of ${max_parallel_jobs} jobs per dataset has been exceeded'}` | Marketplace Dataset API                                    | 超过该数据集允许的最大并行任务数。                                                          | 减少并发任务数量，或等待现有任务完成后再启动新任务。                      |
|                                                                                       | 此错误代码意味着速率限制（罕见）并由 Bright Data 自动限流（特定于 Web Unlocker API）。 | 需要协助时，请提交工单或发送邮件至 [support@brightdata.com](mailto:support@brightdata.com)。 | 确认 delivery\_id 是否正确。                           |

### 500 内部服务器错误

**原因:** Bright Data API 服务器发生意外错误。这些是服务器端问题，通常超出您的直接控制范围。

| 消息                      | 相关端点                                                                         | 原因              | 建议操作                                                         |
| :---------------------- | :--------------------------------------------------------------------------- | :-------------- | :----------------------------------------------------------- |
| `Internal server error` | Scrapers Library 多个端点, `GET /datasets/v3/snapshots`, Marketplace Dataset API | 发生一般的未处理服务器端错误。 | 这通常是临时问题。请在短时间后重试请求。如果问题持续，请联系 Bright Data 支持并提供请求详情和任何错误信息。 |
| `Internal error.`       | Marketplace Dataset API                                                      | 服务器发生意外错误。      | 这是服务器端问题。请重试请求。如果问题持续，请联系 Bright Data 支持。                    |

### 502 错误网关

**原因:** Bright Data API 服务器从上游服务器收到无效响应。

| 消息                                                                                           | 相关端点                    | 原因               | 建议操作                            |
| :------------------------------------------------------------------------------------------- | :---------------------- | :--------------- | :------------------------------ |
| `Unexpected error. The server encountered an unexpected error while processing the request.` | Marketplace Dataset API | 服务器在处理请求时遇到意外错误。 | 这通常是临时服务器端问题。重试请求。如果问题持续，请联系支持。 |

### 503 服务不可用

| 消息                    | 相关端点                 | 原因                | 建议操作                                  |
| :-------------------- | :------------------- | :---------------- | :------------------------------------ |
| `Service Unavailable` | 特定于 Web Unlocker API | 浏览器检查失败或未完成浏览器检查。 | 这表明服务暂时不可用或浏览器渲染问题。重试请求。如果问题持续，请联系支持。 |

## 数据集 API 错误

### 400 - 错误请求

表示请求无效或无法处理。

| 错误消息                                                                                                | 原因                              |
| :-------------------------------------------------------------------------------------------------- | :------------------------------ |
| `{validation_errors: ["filter.name is required"]}`                                                  | 请求缺少必要的过滤器参数（例如 `filter.name`）。 |
| `{validation_errors: ["Invalid input provided"]}`                                                   | 请求中提供的输入无效。                     |
| `Type ${init_types.compr_update} is no longer supported. Use '${init_types.discover_all}' instead.` | 请求的操作类型已弃用。                     |
| `Type ${init_types.update_existing} is no longer supported.`                                        | 请求的操作类型不再支持。                    |
| `Type ${init_types.discover_new} is no longer supported.`                                           | 请求的操作类型不再支持。                    |
| `Initiation reason is required.`                                                                    | 请求缺少必要的启动原因。                    |
| `This feature is not available.`                                                                    | 数据集不支持请求的功能。                    |
| `This dataset was rejected.`                                                                        | 数据集被拒绝，无法处理。                    |
| `This dataset is not ready.`                                                                        | 数据集未准备好处理。                      |
| `This dataset does not support discovery. Supported types: ['${init_types.url_collection}']`        | 数据集不支持请求的发现类型。                  |
| `Incorrect discovery collector id.`                                                                 | 请求中提供的发现收集器 ID 无效。              |
| `View not found.`                                                                                   | 请求的视图不可用。                       |
| `This dataset does not support collection.`                                                         | 数据集不支持请求的集合操作。                  |
| `Batch size must be at least 1000.`                                                                 | 请求中指定的批量大小低于最小允许值。              |
| `{error: 'Snapshot failed'}`                                                                        | 快照操作失败。                         |
| `{error: 'Snapshot not ready'}`                                                                     | 快照尚未准备好处理。                      |
| `{error: 'Invalid snapshot type'}`                                                                  | 请求中提供的快照类型无效。                   |
| `{validation_errors: [e.message]}`                                                                  | 发生验证错误，具体消息包含在响应中。              |

***

### 401 - 未授权

表示用户无权访问请求的资源。

| 错误消息           | 原因                      |
| :------------- | :---------------------- |
| `Unauthorized` | 提供的 API key 或认证凭据无效或缺失。 |

***

### 402 - 需要付款

表示用户账户余额不足以处理请求。

| 错误消息                                                                                                                                                                              | 原因             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------- |
| `{error: 'Your current balance is insufficient to process this data collection request. Please add funds to your account or adjust your request to continue. ($220 is missing)'}` | 用户账户余额不足以处理请求。 |

***

### 403 - 禁止访问

表示用户没有权限访问请求的资源。

| 错误消息                   | 原因               |
| :--------------------- | :--------------- |
| `Access denied.`       | 用户没有访问该资源的必要权限。  |
| `Cannot skip billing.` | 用户尝试跳过计费，这是不允许的。 |

***

### 404 - 未找到

表示请求的资源无法找到。

| 错误消息                            | 原因                   |
| :------------------------------ | :------------------- |
| `{error: 'Dataset not found'}`  | 指定的数据集 ID 不存在。       |
| `{error: 'Snapshot not found'}` | 指定的 snapshot ID 不存在。 |
| `Dataset does not exist.`       | 请求中引用的数据集不存在。        |
| `Request not found.`            | 指定的 request ID 不存在。  |

***

### 422 - 无法处理的实体

表示请求格式正确，但由于语义错误无法处理。

| 错误消息                                                   | 原因                     |
| :----------------------------------------------------- | :--------------------- |
| `{error: 'Provided filter did not match any records'}` | 请求中提供的过滤器未匹配数据集中的任何记录。 |

***

### 429 - 请求过多

表示用户已超出速率限制或最大并行任务数。

| 错误消息                                                                                  | 原因                   |
| :------------------------------------------------------------------------------------ | :------------------- |
| `{error: 'Maximum limit of ${max_parallel_jobs} jobs per dataset has been exceeded'}` | 用户已超出该数据集允许的最大并行任务数。 |

***

### 500 - 内部服务器错误

表示服务器发生意外错误。

| 错误消息              | 原因          |
| :---------------- | :---------- |
| `Internal error.` | 服务器发生了意外错误。 |

***

### 502 - 错误网关

表示服务器从上游服务器收到无效响应。

| 错误消息              | 原因               |
| :---------------- | :--------------- |
| Unexpected error. | 服务器在处理请求时遇到意外错误。 |
