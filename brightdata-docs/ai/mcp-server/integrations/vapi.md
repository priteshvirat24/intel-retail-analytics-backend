> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Vapi AI MCP server integration

> Connect Vapi AI voice agents to the Bright Data MCP server (60+ tools) to give voice assistants real-time web search, scraping and structured data retrieval.

<Card title="Building an AI startup?" cta="Learn more" href="https://brightdata.com/ai/ai-startups-program" icon="rocket-launch" iconType="duotone" arrow="true">
  You might be eligible for our Startup Program. Get fully funded access to the infrastructure you're reading about right now (up to \$20K value).
</Card>

## Watch the demo

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/UFk2CEYLscM" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## Quick Install

To integrate Bright Data into Vapi AI, add the following MCP server URL to your Vapi tools:

```http theme={null}
https://mcp.brightdata.com/sse?token=<your-api-token>
```

## How to set up Vapi AI

<Steps>
  <Step title="Prerequisites">
    Before you begin, ensure you have the following:

    * [A Vapi AI account](https://vapi.ai) (sign up if you don't have one)
    * [A Bright Data account](https://brightdata.com/?hs_signup=1\&utm_source=docs) (new users get free credit for testing, and then you can pay as you go)
    * **An API key** from the [user settings page](https://brightdata.com/cp/setting/users) (New users receive an **API key** in the welcome email.)

    <Tip>
      If you prefer to use a different zone name, you can specify it with the `unlocker` url parameter variable in your configuration
    </Tip>
  </Step>

  <Step title="Login to Vapi AI">
    Navigate to [vapi.ai](https://vapi.ai) and log in to your account.
  </Step>

  <Step title="Claim Your Bright Data API Key">
    Log in to your Bright Data account and navigate to the [user settings page](https://brightdata.com/cp/setting/users) to retrieve your API key.
  </Step>

  <Step title="Access Tools in Vapi">
    In your Vapi dashboard, click on **Tools** in the navigation menu.

    <img src="https://mintcdn.com/brightdata/5sJgYq9iW-Vo_7rr/Screenshot2025-10-20at15.04.00.png?fit=max&auto=format&n=5sJgYq9iW-Vo_7rr&q=85&s=a0be681c144e12afd54519573f1dc261" alt="Setup Guide" width="508" height="762" data-path="Screenshot2025-10-20at15.04.00.png" />
  </Step>

  <Step title="Create a New Tool">
    Click on **Create tool** button to start adding the Bright Data MCP integration.

    <img src="https://mintcdn.com/brightdata/5sJgYq9iW-Vo_7rr/images/Screenshot2025-10-20at15.06.29.png?fit=max&auto=format&n=5sJgYq9iW-Vo_7rr&q=85&s=d1c357ccc1924ff7311942e82baf8a97" alt="Setup Guide" width="257" height="288" data-path="images/Screenshot2025-10-20at15.06.29.png" />
  </Step>

  <Step title="Choose MCP">
    Select **MCP** as the tool type from the available options.

    <img src="https://mintcdn.com/brightdata/5sJgYq9iW-Vo_7rr/images/Screenshot2025-10-20at15.06.56.png?fit=max&auto=format&n=5sJgYq9iW-Vo_7rr&q=85&s=f6d52316b8ddbfbc4cdff85f65b09945" alt="Setup Guide" width="268" height="815" data-path="images/Screenshot2025-10-20at15.06.56.png" />
  </Step>

  <Step title="Configure the MCP Server">
    Configure your tool with the following settings:

    * **Name**: `brightdata`
    * **MCP Server URL**: `https://mcp.brightdata.com/sse?token=<your-api-token>`
    * Set the timeout to 120 seconds to avoid getting errors.

    Replace `<your-api-token>` with your actual API token from Bright Data.

    <img src="https://mintcdn.com/brightdata/5sJgYq9iW-Vo_7rr/images/Screenshot2025-10-20at14.59.04.png?fit=max&auto=format&n=5sJgYq9iW-Vo_7rr&q=85&s=59e5b0c01a97e4f37d30d6331b048d89" alt="Setup Guide" width="1275" height="910" data-path="images/Screenshot2025-10-20at14.59.04.png" />
  </Step>

  <Step title="Add Tool to Assistant">
    Navigate to your assistant settings and add the newly created Bright Data tool to enable the integration.

    <img src="https://mintcdn.com/brightdata/5sJgYq9iW-Vo_7rr/images/Screenshot2025-10-20at15.09.52.png?fit=max&auto=format&n=5sJgYq9iW-Vo_7rr&q=85&s=135dcd28f105850acc3acf31bc88aece" alt="Setup Guide" width="1276" height="600" data-path="images/Screenshot2025-10-20at15.09.52.png" />
  </Step>

  <Step title="Test the Integration">
    Verify the integration works correctly by:

    * Testing through the Vapi chat interface
    * Making a test web call to your assistant

    You should see the Bright Data tools available and responding to your requests.

    <img src="https://mintcdn.com/brightdata/5sJgYq9iW-Vo_7rr/images/Screenshot2025-10-20at15.10.55.png?fit=max&auto=format&n=5sJgYq9iW-Vo_7rr&q=85&s=ea0fc0c8ae63281a61da56cce7fc8e5c" alt="Setup Guide" width="417" height="803" data-path="images/Screenshot2025-10-20at15.10.55.png" />
  </Step>
</Steps>

## What's Next?

Now that you've integrated Bright Data with Vapi AI, you can:

* Use web scraping capabilities directly in your voice AI conversations
* Use [Vapi's workflows](https://docs.vapi.ai/workflows/quickstart) for creating more complex voice AI agents
* Access real-time data from various sources
* Enhance your assistant with powerful data collection features

For more information about Bright Data's MCP capabilities, visit the [Bright Data documentation](https://brightdata.com/products/web-scraper/mcp).
