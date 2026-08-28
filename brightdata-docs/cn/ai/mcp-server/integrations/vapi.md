> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Vapi AI MCP 服务器集成

> 如何将 Vapi AI 与 Bright Data 的 MCP 服务器集成，以增强 AI 功能。

## 演示

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/UFk2CEYLscM" title="YouTube 视频播放器" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## 快速安装

要将 Bright Data 集成到 Vapi AI，请在 Vapi 工具中添加以下 MCP 服务器 URL：

```
https://mcp.brightdata.com/sse?token=<your-api-token>
```

## 设置指南

<Steps>
  <Step title="前提条件">
    开始之前，请确保您拥有以下内容：

    * [Vapi AI 账户](https://vapi.ai)（如果没有，请注册）
    * [Bright Data 账户](https://www.bright.cn/?hs_signup=1\&utm_source=docs)（新用户可获得测试用免费额度，然后按使用付费）
    * **API 密钥**，可在 [用户设置页面](https://www.bright.cn/cp/setting/users) 获取（新用户将在欢迎邮件中收到 **API 密钥**）

    <Tip>
      如果您希望使用不同的区域名称，可以在配置中通过 `unlocker` URL 参数指定
    </Tip>
  </Step>

  <Step title="登录 Vapi AI">
    访问 [vapi.ai](https://vapi.ai) 并登录您的账户。
  </Step>

  <Step title="获取 Bright Data API 密钥">
    登录 Bright Data 账户，前往 [用户设置页面](https://www.bright.cn/cp/setting/users) 获取您的 API 密钥。
  </Step>

  <Step title="访问 Vapi 工具">
    在 Vapi 仪表盘中，点击导航菜单中的 **工具**。

    <img src="https://mintcdn.com/brightdata/5sJgYq9iW-Vo_7rr/Screenshot2025-10-20at15.04.00.png?fit=max&auto=format&n=5sJgYq9iW-Vo_7rr&q=85&s=a0be681c144e12afd54519573f1dc261" alt="Screenshot 2025-10-20 at 15.04.00.png" width="508" height="762" data-path="Screenshot2025-10-20at15.04.00.png" />
  </Step>

  <Step title="创建新工具">
    点击 **创建工具** 按钮，开始添加 Bright Data MCP 集成。

    <img src="https://mintcdn.com/brightdata/5sJgYq9iW-Vo_7rr/images/Screenshot2025-10-20at15.06.29.png?fit=max&auto=format&n=5sJgYq9iW-Vo_7rr&q=85&s=d1c357ccc1924ff7311942e82baf8a97" alt="Screenshot 2025-10-20 at 15.06.29.png" width="257" height="288" data-path="images/Screenshot2025-10-20at15.06.29.png" />
  </Step>

  <Step title="选择 MCP">
    在可选工具类型中选择 **MCP**。

    <img src="https://mintcdn.com/brightdata/5sJgYq9iW-Vo_7rr/images/Screenshot2025-10-20at15.06.56.png?fit=max&auto=format&n=5sJgYq9iW-Vo_7rr&q=85&s=f6d52316b8ddbfbc4cdff85f65b09945" alt="Screenshot 2025-10-20 at 15.06.56.png" width="268" height="815" data-path="images/Screenshot2025-10-20at15.06.56.png" />
  </Step>

  <Step title="配置 MCP 服务器">
    使用以下设置配置工具：

    * **名称**: `brightdata`
    * **MCP 服务器 URL**: `https://mcp.brightdata.com/sse?token=<your-api-token>`
    * 将超时时间设置为 120 秒，以避免出现错误。

    将 `<your-api-token>` 替换为您在 Bright Data 获取的实际 API 密钥。

    <img src="https://mintcdn.com/brightdata/5sJgYq9iW-Vo_7rr/images/Screenshot2025-10-20at14.59.04.png?fit=max&auto=format&n=5sJgYq9iW-Vo_7rr&q=85&s=59e5b0c01a97e4f37d30d6331b048d89" alt="Screenshot 2025-10-20 at 14.59.04.png" width="1275" height="910" data-path="images/Screenshot2025-10-20at14.59.04.png" />
  </Step>

  <Step title="将工具添加到助手">
    前往助手设置，将新创建的 Bright Data 工具添加以启用集成。

    <img src="https://mintcdn.com/brightdata/5sJgYq9iW-Vo_7rr/images/Screenshot2025-10-20at15.09.52.png?fit=max&auto=format&n=5sJgYq9iW-Vo_7rr&q=85&s=135dcd28f105850acc3acf31bc88aece" alt="Screenshot 2025-10-20 at 15.09.52.png" width="1276" height="600" data-path="images/Screenshot2025-10-20at15.09.52.png" />
  </Step>

  <Step title="测试集成">
    验证集成是否正常工作：

    * 通过 Vapi 聊天界面测试
    * 向助手发起测试网页请求

    您应该能看到 Bright Data 工具可用并响应请求。

    <img src="https://mintcdn.com/brightdata/5sJgYq9iW-Vo_7rr/images/Screenshot2025-10-20at15.10.55.png?fit=max&auto=format&n=5sJgYq9iW-Vo_7rr&q=85&s=ea0fc0c8ae63281a61da56cce7fc8e5c" alt="Screenshot 2025-10-20 at 15.10.55.png" width="417" height="803" data-path="images/Screenshot2025-10-20at15.10.55.png" />
  </Step>
</Steps>

## 接下来做什么？

现在您已将 Bright Data 与 Vapi AI 集成，您可以：

* 在语音 AI 对话中直接使用网页抓取功能
* 使用 [Vapi 的工作流](https://docs.vapi.ai/workflows/quickstart) 创建更复杂的语音 AI 助手
* 访问各种来源的实时数据
* 利用强大的数据收集功能增强您的助手

欲了解 Bright Data MCP 功能的更多信息，请访问 [Bright Data 文档](https://www.bright.cn/products/web-scraper/mcp)。
