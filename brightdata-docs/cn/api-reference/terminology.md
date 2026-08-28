> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 术语

## 区域（Zones）

区域是配置和管理 Bright Data 产品的基础。每个区域代表一个特定的产品或设置，例如 Residential、Mobile、Datacenter 或 Web Unlocker API。你可以在 [这里](https://www.bright.cn/cp/zones) 访问你的区域。

<img src="https://mintcdn.com/brightdata/0sd4eqxAli7ENzfc/images/bright-data-zones.png?fit=max&auto=format&n=0sd4eqxAli7ENzfc&q=85&s=7153eceb1ce91ee8aab71e0c19f8a15a" alt="bright-data-zones.png" width="4400" height="3176" data-path="images/bright-data-zones.png" />

### 什么是区域？

区域是一个逻辑容器，用于定义 Bright Data 产品的行为。当你启用一个产品时，会创建一个对应的区域。每个区域都包含其独立的配置设置，例如：

* 目标规则（例如国家、城市、ASN）
* 输出格式
* Headers 和请求行为
* 访问权限

### 在工作流程中使用区域

你可以为同一产品创建多个区域，以支持不同的用例、目标或运营需求。这使你在管理流量时拥有更多控制和灵活性。

示例用例：

* `zone_1` 用于抓取 example.com
* `zone_2` 用于抓取 anotherexample.com

通过将流量分离到不同区域，你可以：

* 为每个目标或工作流程应用唯一设置
* 独立监控使用情况和性能
* 简化调试和优化
* 保持更整洁、组织良好的配置

<Tip>
  你可以随时重命名你的区域，以更好地反映其用途或目标。
</Tip>

## 快照（Snapshot）

Snapshot 在 Bright Data 中表示在触发时保存的数据收集状态。它用于跟踪、管理和检索在特定 dataset 运行期间收集的精准数据。

### 什么是 Snapshot？

Snapshot 是一次数据收集事件的记录。每次 dataset 被触发（无论是手动触发还是通过 API），都会创建一个 snapshot 来存储该次运行的结果和输入。

Snapshot 特别适用于：

* 需要从先前运行中检索历史数据
* 希望验证触发采集时使用了哪些输入
* 以分批方式交付数据时，用于跟踪生成了多少部分

### 示例场景

* 你触发了 dataset 来采集某电商网站的商品列表。系统会自动创建 snapshot，其中记录了结果和输入（例如 URL、filters、headers）。
* 你请求以批次方式交付数据。你可以使用 snapshot 检查生成了多少部分，并确保交付设置符合你的要求。

### Snapshot ID

Snapshot ID 是分配给特定数据 [snapshot](#snapshot) 的唯一标识符。
示例：`s_manlyn268d2p9hdmx`

## 数据集（Dataset）

在 Bright Data 中，[dataset](https://www.bright.cn/products/datasets) 指用于特定用例（例如电商、社交媒体、房地产等）而收集和组织的结构化数据集合。这些 dataset 可在 Dataset Marketplace 中获取。

### Dataset ID

Dataset ID 是分配给 Dataset Marketplace 中每个 [dataset](#dataset) 的唯一标识符。它用于识别和访问特定 dataset，以进行数据检索和管理。

你可以通过 [dataset lists API endpoint](/cn/api-reference/marketplace-dataset-api/get-dataset-list) 获取所有 Scraper APIs 的 Dataset ID 列表，以查看可用的数据集。
