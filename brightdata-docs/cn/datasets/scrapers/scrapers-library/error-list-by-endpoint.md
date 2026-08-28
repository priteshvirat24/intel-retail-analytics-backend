> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 按端点分类的错误代码

> 系统中的错误代码列表，按具体端点分类

## 触发采集

`POST` `/datasets/v3/trigger`

`“触发采集”端点相关的错误代码`

| http\_status\_code | 消息                                                                        |
| :----------------: | ------------------------------------------------------------------------- |
|         400        | `{validation_errors: [ERRORS]}`                                           |
|                    | `dataset missing` 数据集缺失                                                   |
|                    | Invalid attachments 无效附件                                                  |
|                    | This dataset is not allowed for API 此数据集不允许通过 API 使用                      |
|                    | This dataset is not ready yet 数据集尚未准备好                                    |
|                    | No data to trigger 无可触发的数据                                                |
|                    | Should be at least `LIMIT` inputs 输入数量应至少为 `LIMIT`                        |
|         404        | `dataset does not exist` 数据集不存在                                           |
|         429        | 您对该数据集的运行任务过多。请等待部分任务完成，或考虑将多个输入合并为单个请求。运行任务数: `RUNNING_JOBS>=JOBS_LIMIT` |
|         500        | Internal server error 内部服务器错误                                             |

## 下载快照

`GET` `/datasets/v3/snapshot/:snapshot_id`

`“下载快照”端点相关的错误代码`

| http\_status\_code | 消息                                                                                             |
| :----------------: | ---------------------------------------------------------------------------------------------- |
|         202        | `{status: "STATUS", message: "Snapshot is not ready yet, try again in 10s"}` 快照尚未准备好，请 10 秒后重试 |
|                    | `{status: "building", message: "Snapshot is building, try again in 10s"}` 快照正在构建，请 10 秒后重试     |
|         400        | `{validation_errors: [ERRORS]}`                                                                |
|                    | Snapshot is expired 快照已过期                                                                      |
|                    | Snapshot is empty 快照为空                                                                         |
|         404        | Snapshot does not exist 快照不存在                                                                  |
|         500        | Internal server error 内部服务器错误                                                                  |

## 计算交付分片数量

`GET` `/datasets/v3/snapshot/:snapshot_id/parts`

`“计算交付分片数量”端点相关的错误代码`

| http\_status\_code | 消息                              |
| :----------------: | ------------------------------- |
|         400        | `{validation_errors: [ERRORS]}` |
|                    | Snapshot is not ready 快照未准备好    |
|         404        | Snapshot does not exist 快照不存在   |
|         500        | Internal server error 内部服务器错误   |

## 获取触发快照的输入文件

`GET` `/datasets/v3/snapshot/:snapshot_id/input`

`“获取触发快照的输入文件”端点相关的错误代码`

| http\_status\_code | 消息                                    |
| :----------------: | ------------------------------------- |
|         400        | Snapshot input does not exist 快照输入不存在 |
|         404        | Snapshot does not exist 快照不存在         |
|         500        | Internal server error 内部服务器错误         |

## 取消采集

`POST` `/datasets/v3/snapshot/:snapshot_id/cancel`

`“取消采集”端点相关的错误代码`

| http\_status\_code | 消息                            |
| :----------------: | ----------------------------- |
|         400        | Snapshot is not running 快照未运行 |
|         404        | Snapshot does not exist 快照不存在 |
|         500        | Internal server error 内部服务器错误 |

## 监控进度

`GET` `/datasets/v3/progress/:snapshot_id`

`“监控进度”端点相关的错误代码`

| http\_status\_code | 消息                                                                                |
| :----------------: | --------------------------------------------------------------------------------- |
|         404        | Snapshot does not exist 快照不存在                                                     |
|         500        | Internal server error 内部服务器错误                                                     |
|         200        | \{status: "failed", error\_message: "ERROR\_MESSAGE"} 任务失败，错误信息: "ERROR\_MESSAGE" |
|                    | Something went wrong. Our team is looking into it. 出现问题，团队正在处理                    |
|                    | Account is suspended 账户已被暂停                                                       |
|                    | Account is new, please activate it in account settings. URL 账户为新账户，请在账户设置中激活      |
|                    | No data found in discovery 发现中未找到数据                                               |
|                    | Snapshot is empty 快照为空                                                            |
|                    | Failed to deliver snapshot 快照交付失败                                                 |
|                    | Failed to download response 下载响应失败                                                |
|                    | Failed to trigger collector 触发收集器失败                                               |
|                    | Internal Server Error 内部服务器错误                                                     |
|                    | Input validation failed: DETAILS 输入验证失败: DETAILS                                  |

## 监控交付

`GET` `/datasets/v3/delivery/:delivery_id`

`“监控交付”端点相关的错误代码`

| http\_status\_code | 消息                            |
| :----------------: | ----------------------------- |
|         404        | Delivery does not exist 交付不存在 |
|         500        | Internal server error 内部服务器错误 |

## 将收集的数据交付到存储

`POST` `/datasets/v3/deliver/:snapshot_id`

`“将收集的数据交付到存储”端点相关的错误代码`

| http\_status\_code | 消息                                                                       |
| :----------------: | ------------------------------------------------------------------------ |
|         400        | `{validation_errors: [ERRORS]}`                                          |
|                    | Snapshot is not ready 快照未准备好                                             |
|                    | Snapshot is expired 快照已过期                                                |
|                    | Deliver options are missing 缺少交付选项                                       |
|                    | Snapshot is empty 快照为空                                                   |
|                    | Snapshot is too big for single file delivery 快照过大，无法单文件交付                |
|                    | Batch size should be at least `MIN_BATCH_SIZE` 批量大小应至少为 `MIN_BATCH_SIZE` |
|         404        | Snapshot does not exist 快照不存在                                            |
|         500        | Failed to deliver snapshot 快照交付失败                                        |
|                    | Internal server error 内部服务器错误                                            |

## 获取快照列表

`GET` `/datasets/v3/snapshots`

`“获取快照列表”端点相关的错误代码`

| http\_status\_code | 消息                              |
| :----------------: | ------------------------------- |
|         400        | `{validation_errors: [ERRORS]}` |
|         500        | Internal server error 内部服务器错误   |
