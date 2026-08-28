> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenAI SDK 集成

> 如何将 OpenAI 与 Bright Data 的 MCP 服务器集成，以增强 AI 功能。

## 托管 MCP

<Steps>
  <Step title="获取 API 密钥">
    1. 前往 [Bright Data 用户设置](https://www.bright.cn/cp/setting/users)
    2. 复制您的 API 密钥（格式类似：`2dceb1aa0***************************`）
  </Step>

  <Step title="配置 MCP 服务器">
    ```python expandable theme={null}
    from openai import OpenAI

    client = OpenAI()

    resp = client.responses.create(
      model="gpt-4o",
      tools=[
        {
          "type": "mcp",
          "server_label": "BrightData",
          "server_url": "https://mcp.brightdata.com/sse?token=API_TOKEN",
          "require_approval": "never",
        },
      ],
      input="巴黎的天气如何？",
    )

    print(resp.output_text)
    ```
  </Step>

  <Step title="测试功能是否正常">
    1. 问您的 AI：“你能在 Google 上搜索‘今天的天气’吗？”
    2. Claude 会请求权限 - 点击“允许”
    3. 您应能看到结果！
  </Step>

  <Step title="监控使用情况">
    1. 在 Bright Data 控制面板的 [我的区域](https://www.bright.cn/cp/zones) 查看 API 使用情况
    2. 免费套餐每月包含 5,000 次请求
  </Step>
</Steps>
