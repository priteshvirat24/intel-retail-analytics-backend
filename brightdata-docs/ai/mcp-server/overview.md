> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# MCP server overview

> Use the Bright Data MCP server to give AI agents real-time access to public web data with 5,000 free requests per month and zero infrastructure setup.

<Card title="Building an AI startup?" cta="Learn more" href="https://brightdata.com/ai/ai-startups-program" icon="rocket-launch" iconType="duotone" arrow="true">
  You might be eligible for our Startup Program. Get fully funded access to the infrastructure you're reading about right now (up to \$20K value).
</Card>

The **Bright Data MCP server** gives AI agents and assistants real-time access to public web data through the Model Context Protocol (MCP). Connect it to Claude, Cursor or any MCP-compatible client, and your agent can search, scrape and read live web pages without you building or maintaining data pipelines.

The MCP server runs on the Web Unlocker API, so every request handles proxy rotation, anti-bot challenges and CAPTCHA solving automatically. Every new account includes 5,000 free requests per month. You can run the server two ways: a fully managed remote server, or a self-hosted local instance.

<Card title="Get started for free" icon="rocket" href="https://brightdata.com/?hs_signup=1&utm_source=docs" cta="Sign up now">
  Start using the Bright Data MCP server with **5,000 requests** per month, completely free.
</Card>

## Choose your MCP server

<CardGroup>
  <Card title="Remote (hosted) MCP" icon="cloud" href="/ai/mcp-server/remote/quickstart" cta="Quick start">
    Launch a fully managed MCP server in the cloud, no setup required.
  </Card>

  <Card title="Local (self-hosted) MCP" icon="house" href="/ai/mcp-server/local/quickstart" cta="Quick start">
    Set up your own MCP server instance on-premise or in your private cloud.
  </Card>
</CardGroup>

<Tip>
  **Optimize your token usage:** Select only the tools you need using [tool groups](/ai/mcp-server/tools) (e.g., `groups=ecommerce,social`) or individual tools (e.g., `tools=web_data_amazon_product`). This reduces context size and maximizes your usage.
</Tip>

## Explore MCP server resources

<CardGroup>
  <Card title="Tools" icon="wrench" horizontal href="/ai/mcp-server/tools">
    Discover the built-in tools available for your MCP server.
  </Card>

  <Card title="FAQs" icon="book-open" horizontal href="/ai/mcp-server/faqs">
    Get quick answers to frequently asked MCP server questions.
  </Card>

  <Card title="Usage examples" icon="code" horizontal href="/ai/mcp-server/usage-examples">
    Learn from practical examples to accelerate your implementation.
  </Card>

  <Card title="Integrations" icon="puzzle-piece" horizontal href="/ai/mcp-server/integrations/overview">
    Connect the MCP server with leading AI platforms like Claude, Cursor and more.
  </Card>

  <Card title="Source code" icon="github" horizontal href="https://github.com/brightdata/brightdata-mcp?tab=readme-ov-file#-usage-examples">
    Explore the MCP server source code on GitHub.
  </Card>
</CardGroup>

<Note>
  The MCP free tier is the same account-level [free tier](/general/account/billing-and-pricing/free-tier) of 5,000 credits per month, drawn from a single shared pool, because the MCP server runs on the Web Unlocker API. For team accounts, that free tier is shared across all users within the account. If you require additional credits, please contact your account manager.
</Note>
