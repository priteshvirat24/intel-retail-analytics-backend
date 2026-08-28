> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 网站管理员控制台

> 使用 collectors.txt 文件为您的域配置 BrightBot 行为

## 概述

<Info>
  要启用 BrightBot 在您的域上运行，请确保您的防火墙允许来自范围 **82.97.199.0/24** 的请求以及 **Brightbot 1.0** User-Agent。

  *注意：如果您的防火墙阻止 BrightBot 对允许的 URL 的请求，Bright Data 将暂停向您的域发送 BrightBot User-Agent，为期 7 天。*
</Info>

<Warning>
  **网络支持：** 目前，BrightBot User-Agent 和 `collectors.txt` 规则仅适用于通过 **Web Unlocker** 路由的流量。暂不支持 Browser API 和基于浏览器的 Data Collector 作业。
</Warning>

| 输入                                      | 描述                                                                              | 格式           |
| --------------------------------------- | ------------------------------------------------------------------------------- | ------------ |
| **个人信息 (Personal Information)** (`pii`) | 包含与已识别或可识别的自然人相关的信息的端点。BrightBot 将主动阻止从这些端点收集数据。                                | `URL / 文档对象` |
| **禁止 (Disallow)** (`disallow`)          | 列出互动端点模式，例如广告链接、点赞、评论和帖子。此指令使 BrightBot 能够阻止这些端点，符合 Bright Data 禁止从这些区域收集数据的准则。 | `URL / 文档对象` |
| **版权 (Copyright)** (`copyright`)        | 包含受版权保护材料的端点。BrightBot 将主动阻止从这些端点收集数据。                                          | `URL / 文档对象` |
| **私有 (Private)** (`private`)            | 内部或私有端点。BrightBot 将主动阻止从这些端点收集数据。                                               | `URL / 文档对象` |

## 示例

<CodeGroup>
  ```txt collectors.txt theme={null}
  // 可选，描述域名
  service: example.com

  // 包含与已识别或可识别的自然人相关的信息的端点。
  pii: /personal_info_1
  pii: /personal_info_2

  // 列出互动端点模式，例如广告链接、点赞、评论和帖子。
  disallow: /disallow_1
  disallow: /disallow_2

  // 包含受版权保护材料的端点。
  copyright: /copyright_1
  copyright: /copyright_2

  // 通配符 (*) 和字符串结束符 ($) 的功能与正则表达式完全相同，适用于所有指令。
  private: /*secret
  private: /private_2
  private: /private_3/*/private$
  ```
</CodeGroup>
