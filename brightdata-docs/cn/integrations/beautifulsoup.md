> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何使用 Bright Data 与 BeautifulSoup

> 使用 Bright Data 和 BeautifulSoup 来增强您的网页爬取工作流程。本指南将指导您如何在 Python 脚本中集成 Bright Data 代理，以确保安全、可靠和匿名的数据采集。

<Accordion title="展开以获取您的 Bright Data 代理访问信息">
  ### 您的代理访问信息

  Bright Data 代理按“代理区域”（Proxy zones）进行分组。每个区域包含其对应的代理配置。&#x20;

  要获取代理区域的访问权限：&#x20;

  1. 登录 Bright Data 控制面板
  2. 选择现有代理区域或新建一个代理区域
  3. 点击新的区域名称，并选择 **概览（Overview）** 选项卡
  4. 在概览选项卡中，找到 **访问详情（Access details）**，并单击复制图标将代理访问信息复制到剪贴板&#x20;
  5. 您需要以下信息：代理主机（Proxy Host）、代理端口（Proxy Port）、代理区域用户名（Proxy Zone username）和代理区域密码（Proxy Zone password）
  6. 点击复制图标，将文本复制到剪贴板，并粘贴到您的工具的代理配置中&#x20;

  ### 访问详情示例

  <img src="https://mintcdn.com/brightdata/w0SvUEkwL-1dGVtS/snippets/accessdetails.png?fit=max&auto=format&n=w0SvUEkwL-1dGVtS&q=85&s=a3d4e920631ae105cb2f388c63bc5b5d" alt="" width="597" height="508" data-path="snippets/accessdetails.png" />

  ### 住宅代理访问

  要使用 Bright Data 的 **住宅代理（Residential Proxies）**，您必须是经过 KYC 验证的企业账户。请与 Bright Data 合规团队完成 KYC 验证；不存在自动或无需 KYC 的访问方式。尚未完成 KYC 时，请使用 ISP 或数据中心代理。[了解更多...](/proxy-networks/residential/network-access)

  ### 目标是搜索引擎？

  如果您的目标是 Google、Bing 或 Yandex 等搜索引擎，则需要使用专门的搜索引擎结果页（**SERP**）代理 API。请使用 Bright Data SERP API 来访问搜索引擎。\
  [点击此处了解 Bright Data SERP 代理 API。](/scraping-automation/serp-api/introduction)

  ### 避免工具中的 `PROXY ERROR`

  一些工具会使用搜索引擎作为代理测试目标：如果您的代理测试失败，这可能就是原因。请确保您的测试目标域名不是搜索引擎（此设置在工具配置中，而非 Bright Data 代理的控制范围内）。
</Accordion>

## 什么是 BeautifulSoup？

BeautifulSoup 是一个 Python 库，它简化了从 HTML 和 XML 文档中提取和整理数据的过程。结合 Bright Data 代理，它可以帮助您安全、匿名地爬取数据，并降低被检测和封锁的风险。

## 如何将 Bright Data 与 BeautifulSoup 集成

**步骤 0. 先决条件**

开始之前：

* 从 [python.org](https://www.python.org/) 下载最新的 Python 版本。

* 安装 BeautifulSoup 和 `requests` 库：

```bash theme={null}
     pip install beautifulsoup4 requests
```

**步骤 1. 设置代理**

登录 Bright Data 账户，并选择要使用的代理区域。在 **概览** 下的 **访问详情** 中，您可以找到获取访问信息所需的详细信息。\*\*\*\*&#x20;

1. 登录您的 [Bright Data 账户](https://www.bright.cn/cp/zones) 并获取代理凭据：

   * **主机**: [`http://brd.superproxy.io/`](http://brd.superproxy.io/)

   * **端口**: 44445

   * **用户名**: 您的 Bright Data 用户名。如果需要使用特定国家的代理，请修改用户名（例如：`your-username-country-US`）。

   * **密码**: 您的 Bright Data 代理区域密码。

2. 在您的脚本中定义代理详细信息：

```python theme={null}
import requests
from bs4 import BeautifulSoup

# Bright Data Proxy Configuration
proxy = {
    "http": "http://[USERNAME]:[PASSWORD]@[HOST]:[PORT]",
    "https": "http://[USERNAME]:[PASSWORD]@[HOST]:[PORT]"
}

# Target URL to verify the proxy
url = "https://httpbin.org/ip" 

try:
    # Send the request using the proxy
    response = requests.get(url, proxies=proxy, timeout=10)
    response.raise_for_status()  # Handle HTTP errors

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Print the formatted page content
    print("Response Content (IP Address):")
    print(soup.prettify())

except requests.exceptions.RequestException as e:
    print("Error occurred while using the proxy:", e)

```

**步骤 3. 验证输出**

如果 Bright Data 代理配置正确，您应该会在输出中看到代理的 IP 地址：

```json theme={null}
{
  "origin": "123.45.67.89"
}
```

将 Bright Data 代理与 BeautifulSoup 集成，可以让您更安全、匿名和高效地爬取数据。无论是提取结构化数据、访问受地理限制的内容，还是管理大规模爬取任务，Bright Data 都能确保可靠性和隐私保护。立即使用 Bright Data 和 BeautifulSoup 开始更智能的爬取吧！
