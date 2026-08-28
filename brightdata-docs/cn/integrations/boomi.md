> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何使用Boomi设置Bright Data

> 了解如何使用Bright Data合作伙伴连接器将Bright Data的网页抓取和数据收集API连接到Boomi流程。

# Translation to Simplified Chinese

[Bright Data 合作伙伴连接器](https://help.boomi.com/searchResults?q=bright%20data)允许您直接在 Boomi 流程中从 Bright Data 的爬取和数据收集 API 检索数据。您可以与 SERP、Dataset、Scraper 和 Web Unlocker API 集成，以在不离开 Boomi 平台的情况下构建端到端的公共网络数据工作流。

<Note>
  Bright Data 合作伙伴连接器由 Bright Data 开发和维护。客户支持通过 Boomi 支持门户处理，其中工单被分流至 Bright Data。
</Note>

## 支持的对象

连接器支持以下对象类型，每个都通过执行操作访问：

| 对象       | 描述                              |
| -------- | ------------------------------- |
| Dataset  | 访问带有筛选和快照检索的市场数据集               |
| Scraper  | 提交网络爬取作业并异步检索结果                 |
| Unlocker | 通过代理和解锁服务访问受保护的网络内容             |
| SERP     | 检索来自 Google、Bing 和其他搜索引擎的搜索结果页面 |

## 先决条件

开始之前，请确保您具有：

* 有效的 Bright Data 账户
* 从 [Bright Data 控制面板](https://www.bright.cn/cp/setting/users)生成的 API 密钥，具有用于您打算使用���服务的权限

## 连接您的 Bright Data 账户

<Steps>
  <Step title="打开连接配置">
    在您的 Boomi 流程中，添加新的 **Bright Data 合作伙伴连接器**组件并导航到**连接**选项卡。
  </Step>

  <Step title="设置基础 URL">
    输入 Bright Data API 基础 URL：

    ```
    https://api.brightdata.com
    ```

    仅在需要指向不同端点（如用于测试或区域部署）时自定义此值。
  </Step>

  <Step title="输入您的 API 密钥">
    将您的 Bright Data API 密钥粘贴到 **API Token** 字段中。连接器使用此密钥进行 Bearer 身份验证。
  </Step>

  <Step title="测试连接">
    单击**测试连接**以验证您的设置。如果测试成功，保存连接。如果失败，请查看您的基础 URL 和 API 密钥，然后再次测试。
  </Step>
</Steps>

## 配置操作

每个操作定义连接器如何与特定 Bright Data 对象交互。为您的集成所需的每个操作/对象组合创建单独的操作组件。

所有对象类型都使用**执行**操作。

### 选项选项卡字段

| 字段     | 描述                                                |
| ------ | ------------------------------------------------- |
| 连接器操作  | 对所有 Bright Data 操作设置为**执行**                       |
| 对象     | 使用**导入**按钮导入。选择 Dataset、Scraper、Unlocker 或 SERP   |
| 请求配置文件 | 接受动态内容结构的灵活 XML/XSD 模式                            |
| 响应配置文件 | 连接器返回的 JSON 配置文件                                  |
| 跟踪方向   | 选择**输入文档**或**输出文档**                               |
| 错误行为   | 启用以在您的流程中处理失败的操作，而不仅仅报告它们                         |
| 请求有效负载 | 可选的文档级别请求覆盖。接受 JSON、URL 查询样式或换行符分隔的 `key=value` 对 |

## 对象特定行为

### Dataset

连接器根据是否存在 `snapshot_id` 在两种模式之一中运行：

* **模式 A（筛选）：** 未提供 `snapshot_id`。根据您的查询参数筛选市场数据集。
* **模式 B（快照）：** 提供了以 `snap_` 开头的 `snapshot_id`。连接器每 10 秒轮询一次，最多重试 25 次，直到快照就绪。

```json theme={null}
{
  "dataset_id": "gd_l1viktl72bvl7bjuj0",
  "filter": {
    "name": "name",
    "operator": "=",
    "value": "Or Lenchner"
  }
}
```

### Scraper

* **模式 A（触发）：** 未提供 `snapshot_id`。提交新的爬取作业并返回 `snapshot_id`。
* **模式 B（快照）：** 提供了以 `s_` 开头的 `snapshot_id`。连接器轮询完成情况并下载结果。

```json theme={null}
{
  "dataset_id": "gd_l1viktl72bvl7bjuj0",
  "url": "https://www.linkedin.com/in/orlenchner",
  "discover_by": "profile_url"
}
```

### Unlocker

需要 `url` 参数来绕过网站限制。支持 `method`、`country` 和 `body` 参数。

```json theme={null}
{
  "zone": "web_unlocker1",
  "url": "https://geo.brdtest.com/welcome.txt",
  "format": "json",
  "method": "GET",
  "country": "us",
  "data_format": "markdown"
}
```

### SERP

需要 `engine` 和 `query` 参数。在单个请求中支持使用逗号分隔列表的多个引擎。

```json theme={null}
{
  "zone": "serp_api1",
  "url": "https://www.google.com/search?q=BrightData",
  "format": "json",
  "method": "GET",
  "country": "us",
  "data_format": "markdown"
}
```

<Note>
  连接器以 JSON 格式返回所有数据。如果基础 API 返回非 JSON 内容（如 HTML 或 CSV），连接器会将原始内容包装在 JSON 结构中，以便在 Boomi 中进行一致处理。
</Note>

## 发行说明

**版本 1.0.0**

初始版本。通过执行操作支持 Dataset、Scraper、Unlocker 和 SERP 对象类型。

```
```
