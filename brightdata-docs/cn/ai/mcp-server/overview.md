> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# MCP 服务器概览

> 使用 Bright Data MCP 服务器让 AI 智能体实时访问公共网页数据，每月 5,000 次免费请求，无需搭建任何基础设施。

<Card title="Building an AI startup?" cta="Learn more" href="https://brightdata.com/ai/ai-startups-program" icon="rocket-launch" iconType="duotone" arrow="true">
  You might be eligible for our Startup Program. Get fully funded access to the infrastructure you're reading about right now (up to \$20K value).
</Card>

**Bright Data MCP 服务器**通过 Model Context Protocol（MCP）让 AI 智能体和助手实时访问公共网页数据。将其连接到 Claude、Cursor 或任何兼容 MCP 的客户端，您的智能体便可搜索、抓取和读取实时网页，而无需自行构建或维护数据管道。

MCP 服务器运行在 Web Unlocker API 之上，因此每个请求都会自动处理代理轮换、反爬虫挑战和验证码破解。每个新账户每月包含 5,000 次免费请求。您可以通过两种方式运行该服务器：全托管的远程服务器，或自托管的本地实例。

<Card title="免费开始使用" icon="rocket" href="https://www.bright.cn/?hs_signup=1&utm_source=docs" cta="立即注册">
  开始使用 Bright Data MCP 服务器，每月 **5,000 次请求**，完全免费。
</Card>

## 选择您的 MCP 服务器

<CardGroup>
  <Card title="远程（托管）MCP" icon="cloud" href="/cn/ai/mcp-server/remote/quickstart" cta="快速开始">
    在云端启动一个全托管 MCP 服务器，无需任何设置。
  </Card>

  <Card title="本地（自托管）MCP" icon="house" href="/cn/ai/mcp-server/local/quickstart" cta="快速开始">
    在本地或私有云中部署您自己的 MCP 服务器实例。
  </Card>
</CardGroup>

<Tip>
  **优化您的 token 使用：** 使用[工具组](/cn/ai/mcp-server/tools)（例如 `groups=ecommerce,social`）或单个工具（例如 `tools=web_data_amazon_product`）仅选择您需要的工具。这样可以减少上下文大小并最大化您的使用额度。
</Tip>

## 探索 MCP 服务器资源

<CardGroup>
  <Card title="工具" icon="wrench" horizontal href="/cn/ai/mcp-server/tools">
    了解 MCP 服务器中可用的内置工具。
  </Card>

  <Card title="常见问题" icon="book-open" horizontal href="/cn/ai/mcp-server/faqs">
    获取有关 MCP 服务器的常见问题解答。
  </Card>

  <Card title="使用示例" icon="code" horizontal href="/cn/ai/mcp-server/usage-examples">
    通过实际示例加速您的实现过程。
  </Card>

  <Card title="集成" icon="puzzle-piece" horizontal href="/cn/ai/mcp-server/integrations/overview">
    将 MCP 服务器与 Claude、Cursor 等领先的 AI 平台连接。
  </Card>

  <Card title="源代码" icon="github" horizontal href="https://github.com/brightdata/brightdata-mcp?tab=readme-ov-file#-usage-examples">
    在 GitHub 上探索 MCP 服务器的源代码。
  </Card>
</CardGroup>

<Note>
  MCP 免费套餐就是账户级[免费套餐](/cn/general/account/billing-and-pricing/free-tier)，即每月 5,000 个信用额度，从单一共享池中扣除，因为 MCP 服务器运行在 Web Unlocker API 之上。对于团队账户，该免费额度会在整个账户的所有用户之间共享。如需额外额度，请联系您的客户经理。
</Note>
