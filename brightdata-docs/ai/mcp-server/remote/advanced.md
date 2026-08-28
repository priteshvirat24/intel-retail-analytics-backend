> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Remote MCP server advanced configuration

> Customize the remote Bright Data MCP server (60+ tools): configure auth tokens, switch proxies, tune timeouts and enable advanced tools per session.

<Card title="Building an AI startup?" cta="Learn more" href="https://brightdata.com/ai/ai-startups-program" icon="rocket-launch" iconType="duotone" arrow="true">
  You might be eligible for our Startup Program. Get fully funded access to the infrastructure you're reading about right now (up to \$20K value).
</Card>

## MCP Server Modes

Bright Data's MCP server offers two modes to suit different needs:

* **Rapid (Free)** - Quickly scrape search results and unlock any public webpage as clean Markdown.
* **Pro** - Access advanced scraping, structured data from top platforms (Amazon, LinkedIn, X, Instagram, etc.), and full browser automation. Built for dynamic and large-scale use cases.
* **Groups** - Unlock targeted capabilities with pre-built bundles. Whether you're monitoring competitors, analyzing social trends, or automating browsers, select the exact tool groups your project requires.
* **Tools** -  Fine-tune your toolkit. Cherry-pick individual tools to supplement your Groups or build a completely custom setup for specialized use cases.

<Tip>
  **Rapid (Free)** mode is enabled by default and is **recommended** for everyday browsing and data needs.
</Tip>

***

## How to configure the remote MCP server

When using a remote MCP server, you can configure advanced options by passing query parameters to your endpoint:

<ParamField query="unlocker" default="mcp_unlocker" type="string">
  Use a custom zone name for web scraping.

  > **For example:** `&unlocker=my_zone_name`
</ParamField>

<ParamField query="browser" default="mcp_browser" type="string">
  Use a custom zone name for browser automation.

  > **For example:** `&browser=my_browser_zone`
</ParamField>

<ParamField query="pro" default="0" type="number">
  Enable advanced (Pro) processing.

  > **For example:** `&pro=1`

  <Tip>
    Use `&pro=1` to enable **Pro mode**.
  </Tip>
</ParamField>

<ParamField query="groups" default type="string">
  Select pre-built tool bundles tailored to your domain. Comma-separated list of group IDs.

  > **For example:** `&groups=browser,ecommerce,social`

  <Tip>
    Available groups: `ecommerce`, `social`, `browser`, `finance`, `business`, `research`, `app_stores`, `travel`, `advanced_scraping`, `geo`, `code`
  </Tip>
</ParamField>

<ParamField query="tools" default type="string">
  Handpick individual tools to complement your groups selection. Comma-separated list of tool names.

  > **For example:** `&tools=scrape_as_markdown,web_data_linkedin_person_profile`

  <Warning>
    Using `groups` or `tools` overrides `pro=1`. Tool selection takes priority over Pro mode.
  </Warning>
</ParamField>

### Example configurations

<CodeGroup>
  ```sh SSE - Pro Mode (All Tools) theme={null}
  https://mcp.brightdata.com/sse?token=YOUR_API_TOKEN&pro=1
  ```

  ```sh SSE - Tool Groups theme={null}
  https://mcp.brightdata.com/sse?token=YOUR_API_TOKEN&groups=browser,ecommerce,social
  ```

  ```sh SSE - Custom Tools theme={null}
  https://mcp.brightdata.com/sse?token=YOUR_API_TOKEN&groups=browser&tools=web_data_linkedin_person_profile,scrape_as_html
  ```

  ```sh HTTP - Pro Mode (All Tools) theme={null}
  https://mcp.brightdata.com/mcp?token=YOUR_API_TOKEN&pro=1
  ```

  ```sh HTTP - Tool Groups theme={null}
  https://mcp.brightdata.com/mcp?token=YOUR_API_TOKEN&groups=browser,ecommerce,social
  ```

  ```sh HTTP - Custom Tools theme={null}
  https://mcp.brightdata.com/mcp?token=YOUR_API_TOKEN&groups=browser&tools=web_data_linkedin_person_profile,scrape_as_html
  ```
</CodeGroup>

***
