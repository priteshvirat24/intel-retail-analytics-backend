> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Agent Builder MCP server integration

> Connect OpenAI Agent Builder to the Bright Data MCP server (60+ tools) to build AI agents with real-time web search, scraping and structured data access.

<Card title="Building an AI startup?" cta="Learn more" href="https://brightdata.com/ai/ai-startups-program" icon="rocket-launch" iconType="duotone" arrow="true">
  You might be eligible for our Startup Program. Get fully funded access to the infrastructure you're reading about right now (up to \$20K value).
</Card>

**Requirements:**

* [Bright Data account](https://brightdata.com/?hs_signup=1\&utm_source=docs)
* OpenAI Account with a [verified organization](https://help.openai.com/en/articles/10910291-api-organization-verification)

<Steps>
  <Step title="Create a new flow">
    Go to [Agent Builder](https://platform.openai.com/agent-builder) and create a new flow

    <img src="https://mintcdn.com/brightdata/5sJgYq9iW-Vo_7rr/images/Screenshot2025-10-10at10.27.55.png?fit=max&auto=format&n=5sJgYq9iW-Vo_7rr&q=85&s=d2a01b3168c6893dfa7f1ce7aa628e27" alt="Agent Builder MCP Server Integration" width="1431" height="510" data-path="images/Screenshot2025-10-10at10.27.55.png" />
  </Step>

  <Step title="Click on the agent node">
    <img src="https://mintcdn.com/brightdata/5sJgYq9iW-Vo_7rr/images/Screenshot2025-10-10at10.30.51.png?fit=max&auto=format&n=5sJgYq9iW-Vo_7rr&q=85&s=d5976fe7f250e820a05f9ffe1f10a8dc" alt="Agent Builder MCP Server Integration" width="1339" height="618" data-path="images/Screenshot2025-10-10at10.30.51.png" />

    After clicking the agent node, the agent configuration panel will appear on the left side of the screen.
  </Step>

  <Step title="Click on Tools to add the MCP">
    <img src="https://mintcdn.com/brightdata/5sJgYq9iW-Vo_7rr/images/Screenshot2025-10-10at10.32.45.png?fit=max&auto=format&n=5sJgYq9iW-Vo_7rr&q=85&s=6a2d661ee2579fdb4759d4ce65d2c42b" alt="Agent Builder MCP Server Integration" width="375" height="529" data-path="images/Screenshot2025-10-10at10.32.45.png" />
  </Step>

  <Step title="Choose MCP and add the Bright Data MCP server">
    Copy and paste the following URL into the URL section:

    ```http theme={null}
    https://mcp.brightdata.com/mcp?token=YOUR_API_KEY
    ```

    Replace `YOUR_API_KEY` with your actual Bright Data API key.

    <Note>
      You can copy this URL with a pre-filled API key from your [control panel](https://brightdata.com/cp/mcp)
    </Note>

    Then click the Connect button.

    <img src="https://mintcdn.com/brightdata/5sJgYq9iW-Vo_7rr/images/Screenshot2025-10-10at10.40.55.png?fit=max&auto=format&n=5sJgYq9iW-Vo_7rr&q=85&s=9ea53ee4e9d2af8a4966ecd3586cfdb0" alt="Agent Builder MCP Server Integration" width="524" height="668" data-path="images/Screenshot2025-10-10at10.40.55.png" />
  </Step>

  <Step title="Choose your preferred tools and add them">
    Here you can choose the relevant tools you want to expose to the agent, or add all of them by clicking the Add button.

    <img src="https://mintcdn.com/brightdata/5sJgYq9iW-Vo_7rr/images/Screenshot2025-10-10at10.44.46.png?fit=max&auto=format&n=5sJgYq9iW-Vo_7rr&q=85&s=8097c3fc0506a306bb67ec580b16025d" alt="Agent Builder MCP Server Integration" width="522" height="566" data-path="images/Screenshot2025-10-10at10.44.46.png" />
  </Step>

  <Step title="Configure your agent with a name and instructions">
    Give your agent a name, provide an instruction set, choose the reasoning effort level, and click the Preview button to test it.

    <img src="https://mintcdn.com/brightdata/5sJgYq9iW-Vo_7rr/images/Screenshot2025-10-10at10.48.31.png?fit=max&auto=format&n=5sJgYq9iW-Vo_7rr&q=85&s=9a88d7f85801d5287b52e44bd76bc09a" alt="Agent Builder MCP Server Integration" width="356" height="556" data-path="images/Screenshot2025-10-10at10.48.31.png" />
  </Step>

  <Step title="Test your agent">
    Ask your agent any question that requires real-time web data and get an instant answer.

    <img src="https://mintcdn.com/brightdata/5sJgYq9iW-Vo_7rr/images/Screenshot2025-10-10at10.52.31.png?fit=max&auto=format&n=5sJgYq9iW-Vo_7rr&q=85&s=539f67c417dc1812e378d976683f1086" alt="Screenshot 2025-10-10 at 10.52.31.png" width="1672" height="746" data-path="images/Screenshot2025-10-10at10.52.31.png" />
  </Step>
</Steps>
