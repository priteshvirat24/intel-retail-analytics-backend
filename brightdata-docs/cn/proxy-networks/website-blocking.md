> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 克服网站封锁

> 查看有关如何克服网站封锁和错误的一般建议

排除错误的第一步是检查整个网络错误响应——其中可能包含有关错误来源的重要信息，甚至可能提供解决问题的指示。

要分析完整的响应，您可以在终端运行 `curl` 命令，并添加 `-v` 或 `-i` 选项。这些选项会使 `curl` 以详细模式运行，并打印出请求和响应的头部信息。

```
curl -v [rest of curl command options]
```

## 通用建议

### IP 地址

在处理 IP 时，需要考虑的主要因素包括：

* **地理位置**：通常最好使对等 IP 的国家与目标网站所在的国家匹配。\
  使用更具体的定位也可能有所帮助：
  城市比州（省）更具体，州（省）比国家更具体。

* **IP 池类型**：如果目标网站对同一 IP 发送多个请求不敏感，可以使用共享 IP（Shared IP）以降低成本。\
  如果目标网站对此敏感，则使用专用 IP（Dedicated IP）可能会有所帮助。

* **质量**：Bright Data 除了提供自动化爬取解决方案外，还提供 4 种常规代理网络。按照被检测难度从低到高排列如下：\
  数据中心（Data Center）-> ISP 代理（ISP）-> 住宅代理（Residential）-> 移动代理（Mobile）

  如果某个网络持续被屏蔽，尝试使用下一个更难检测的代理类型可能有助于绕过封锁。

* **一致性**：对于单个 URL 的爬取，应频繁轮换 IP 以避免触发速率限制。如果希望模拟真实用户访问，可以参考下方的建议来保持 IP 的一致性。

### 会话（Sessions）

* 如果您希望模拟真实用户，应该使用会话 ID 作为用户名参数：\
  [代理和 IP 轮换控制](/api-reference/proxy/rotate_ips#using-the-same-proxy-for-multiple-requests-session)

  这表明，对于具有相同会话 ID 的请求，您希望保持相同的 IP。\
  在使用住宅代理（Residential）或移动代理（Mobile）等轮换网络时，这样做可以使您的行为更接近普通用户。

* 如果您的用例是单次爬取，您仍然可以使用该参数，但方式有所不同：
  * 当会话 ID 更改时，表示您希望使用不同于上次的 IP。
  * 在 60 秒内遍历多个会话 ID，可以让您轮换已分配的 IP。

### 请求方法 / 指纹（Request Method / Fingerprint）

* **请求方法**：“普通用户”通常会使用浏览器访问网站。您可以直接将代理集成到常规浏览器中，或者使用我们的扩展程序（[点击这里](https://chrome.google.com/webstore/detail/bright-data/efohiadmkaogdhibjbmeppjpebenaool?hl=en)）。

  如果您使用的是其他集成方式，例如浏览器自动化或直接 API 请求，请务必注意这一点，并尽可能让您的请求看起来像真实的浏览器，以避免被检测。

* **指纹（Fingerprint）**：让请求看起来像真实用户的一部分是发送合适的 请求头（Headers） 和 Cookies，但另一部分是确保您的请求具有真实浏览器的属性。

  您可以在网上找到许多相关资源，我们还提供 Web Unlocker API 和 Browser API，这些工具可以自动处理所有这些细节，帮助您绕过检测。

## 自动化解决方案

如果您发现我们的代理解决方案（数据中心、ISP、住宅、移动代理）都无法满足您的需求，我们建议尝试 [自动化爬取解决方案](/scraping-automation/introduction)，特别是 Web Unlocker API。该 API 可自主管理上述所有措施，并提供更多优化，以确保更高的成功率。
