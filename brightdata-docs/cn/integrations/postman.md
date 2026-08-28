> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 Postman 中使用 Bright Data

> 在 Postman 中使用 Bright Data 以优化 API 测试。本指南将向您展示如何配置代理，以实现安全、匿名和地理定位的 API 请求。

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

## 什么是 Postman？

Postman 是一个广泛使用的 API 平台，可以简化 API 的测试、开发和管理。它允许开发者发送请求、监控响应，并高效地组织工作流。将 Bright Data 与 Postman 集成可以确保匿名性、安全性，并支持在不同地理位置测试 API。

## 为什么在 Postman 中使用 Bright Data？

* **增强隐私**：隐藏您的 IP 地址，使 API 测试保持匿名。

* **地理特定测试**：使用 Bright Data 代理模拟来自不同国家的 API 请求。

* **提高安全性**：通过安全私密的连接保护您的 API 请求。

## 如何将 Bright Data 集成到 Postman

<Steps>
  <Step title="前提条件">
    1. **下载 Postman**：安装最新版本的 [Postman](https://www.postman.com/downloads/)。安装完成后，启动应用并登录您的账户。
    2. **获取 Bright Data 代理凭据**：
       * 登录您的 [Bright Data 控制面板](https://www.bright.cn/cn/cp/zones/page/plans) 以获取 **主机 (Host)**、**端口 (Port)**、**用户名 (Username)** 和 **密码 (Password)**。
       * 若需要地理定位代理，请修改用户名格式为 `your-username-country-XX`（例如 `your-username-country-US`）。
  </Step>

  <Step title="访问代理设置">
    1. 在 Postman 界面中，点击右上角的 **齿轮图标** 进入 **设置** 菜单。

    <Frame as="div">
      <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/postman1.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=f0bec662ba0b35a84d51ba9695873449" alt="" width="1920" height="1020" data-path="images/integrations/postman1.png" />
    </Frame>
  </Step>

  <Step title="配置 Bright Data 代理">
    1. 在左侧菜单中导航到 **Proxy** 选项卡。
    2. 如果 "**Use custom proxy configuration**" 尚未启用，请切换为 *On*。
    3. 输入您的 Bright Data 代理详细信息：
       * **类型 (Type)**：根据 Bright Data 配置选择 HTTP 或 HTTPS。
       * **主机 (Host)**：输入 `http://brd.superproxy.io/`。
       * **端口 (Port)**：使用 [Bright Data 控制面板](https://www.bright.cn/cn/cp/zones/page/plans) 提供的端口号。
       * **用户名 (Username)**：输入您的 Bright Data `username`。
       * **密码 (Password)**：输入您的 Bright Data `password`。
  </Step>

  <Step title="测试代理配置">
    1. 在 Postman 中创建一个新的请求，并将方法设置为 **GET**。
    2. 输入以下 URL 以测试代理：[https://httpbin.org/ip](https://httpbin.org/ip)。
    3. 点击 **Send** 以执行请求。

    如果响应中显示的是 Bright Data 代理的 IP 地址，则说明配置成功。
  </Step>
</Steps>

通过在 Postman 中集成 Bright Data 代理，您可以增强 API 测试工作流的隐私性和可靠性。无论是调试、开发还是扩展 API 任务，Bright Data 代理都能提供安全且匿名的连接。立即尝试，优化您的 API 项目！
