> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# VS Code MCP server integration

> Connect VS Code MCP-enabled chat to the Bright Data MCP server (60+ tools) to give GitHub Copilot real-time web search, scraping and structured data tools.

<Card title="Building an AI startup?" cta="Learn more" href="https://brightdata.com/ai/ai-startups-program" icon="rocket-launch" iconType="duotone" arrow="true">
  You might be eligible for our Startup Program. Get fully funded access to the infrastructure you're reading about right now (up to \$20K value).
</Card>

## Quick Install

Click the button below to automatically install and configure the Bright Data MCP server in VS Code:

## Self-hosted MCP

<Steps>
  <Step title="Prerequisites">
    Before you begin, ensure you have the following:

    * [Node.js ](https://nodejs.org/en/download) is installed and up to date
    * [A Bright Data account](https://brightdata.com/?hs_signup=1\&utm_source=docs)  (new users get free credit for testing, and then you can pay as you go)
    * **An API key** from the [user settings page](https://brightdata.com/cp/setting/users) (New users receive an **API key** in the welcome email.)

    <Tip>
      If you prefer to use a different zone name, you can specify it with the `WEB_UNLOCKER_ZONE `environment variable in your configuration
    </Tip>
  </Step>

  <Step title="Basic Configuration">
    Click on the Vs code logo to automatically install the Bright Data MCP:

    <a href="vscode:mcp/install?%7B%22name%22%3A%22the-web-mcp%22%2C%22type%22%3A%22stdio%22%2C%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22%40brightdata%2Fmcp%22%5D%2C%22env%22%3A%7B%22API_TOKEN%22%3A%22%24input%3Aapi-token%22%7D%7D" target="_blank">
      <img src="https://mintcdn.com/brightdata/w0SvUEkwL-1dGVtS/visual-studio-code-svgrepo-com.svg?fit=max&auto=format&n=w0SvUEkwL-1dGVtS&q=85&s=cccfaa4a4f07cdb90715cc438d6987a5" alt="Install in VS Code" noZoom={true} height="0" className="mr-auto" title="" style={{ width: "5%", margin: "0", padding: "0" }} data-path="visual-studio-code-svgrepo-com.svg" />
    </a>
  </Step>
</Steps>
