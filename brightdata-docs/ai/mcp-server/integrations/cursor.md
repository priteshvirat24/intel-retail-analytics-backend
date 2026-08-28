> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cursor MCP server integration

> Connect Cursor IDE to the Bright Data MCP server (60+ tools) in either hosted or self-hosted mode, for AI coding assistant web search and scraping.

<Card title="Building an AI startup?" cta="Learn more" href="https://brightdata.com/ai/ai-startups-program" icon="rocket-launch" iconType="duotone" arrow="true">
  You might be eligible for our Startup Program. Get fully funded access to the infrastructure you're reading about right now (up to \$20K value).
</Card>

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
    Go to Cursor -> Click the gear icon -> Tools & Integrations -> Add Custom MCP -> include the following:

    ```json expandable theme={null}
    {
        "mcpServers": {
        "brightdata-mcp": {
            "command": "npx",
            "args": ["-y", "@brightdata/mcp"],
            "env": {
            "API_TOKEN": "<your API token>"
            }
        }
        }
    }
    ```

    <Frame>
      <img src="https://mintcdn.com/brightdata/5sJgYq9iW-Vo_7rr/images/Screenshot2025-07-14at13.50.57.png?fit=max&auto=format&n=5sJgYq9iW-Vo_7rr&q=85&s=b45b0fd381570a6ec4619de710a18914" alt="Screenshot 2025-07-14 at 13.50.57.png" title="Screenshot 2025-07-14 at 13.50.57.png" width="1453" height="602" data-path="images/Screenshot2025-07-14at13.50.57.png" />
    </Frame>

    Then you need to see:

    <Frame>
      <img src="https://mintcdn.com/brightdata/5sJgYq9iW-Vo_7rr/images/Screenshot2025-07-14at14.18.16.png?fit=max&auto=format&n=5sJgYq9iW-Vo_7rr&q=85&s=8181d25cf09203efb21645492de98628" alt="Screenshot 2025-07-14 at 14.18.16.png" title="Screenshot 2025-07-14 at 14.18.16.png" width="386" height="153" data-path="images/Screenshot2025-07-14at14.18.16.png" />
    </Frame>
  </Step>
</Steps>
