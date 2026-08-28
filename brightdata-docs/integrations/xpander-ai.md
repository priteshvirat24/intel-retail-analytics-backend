> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to set up Bright Data with xpander.ai

> Integrate Bright Data with xpander.ai to give enterprise AI agents reliable web access and structured data extraction from public websites. Spans 195 countries.

<Card title="Building an AI startup?" cta="Learn more" href="https://brightdata.com/ai/ai-startups-program" icon="rocket-launch" iconType="duotone" arrow="true">
  You might be eligible for our Startup Program. Get fully funded access to the infrastructure you're reading about right now (up to \$20K value).
</Card>

[xpander.ai](https://xpander.ai/) is a Backend-as-a-Service platform for building autonomous AI agents. It is a no-code solution designed to help enterprise developers efficiently build, test, and deploy AI agents. It also comes with an open-source SDK to programmatically build and run AI agents.

## Available Bright Data Tools

<Card>
  <CardGroup cols={1}>
    <Card title="Start Data Collection Job by Dataset ID" icon="1">
      Launches a scraping job for a specified dataset using the Scraperss.
    </Card>

    <Card title="Execute Proxy Request by URL" icon="2">
      Sends an HTTP request through Bright Data’s proxy network for accessing the content of any web page.
    </Card>

    <Card title="Download Dataset Snapshot by ID" icon="3">
      Downloads a snapshot of a dataset in various formats, passing the data to the AI.
    </Card>
  </CardGroup>
</Card>

## How to Integrate Bright Data With xpander.ai

<Steps>
  <Step title="Prerequisites" stepNumber="0">
    * [xpander.ai account](https://app.xpander.ai/login)
    * [Bright Data API key](/api-reference/authentication#api-key)
  </Step>

  <Step title="Create a new agent" stepNumber="1">
    1. In your [profile dashboard](https://app.xpander.ai/agents) and press the “New Agent” button to add a new agent:

    <Frame>
      <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/xpander-ai/new-agent-button.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=fceebc949769dea8ddd6f65ea2735ab0" alt="Clicking the “Agents > New Agent” button" data-og-width="2048" width="2048" data-og-height="624" height="624" data-path="images/integrations/xpander-ai/new-agent-button.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/xpander-ai/new-agent-button.png?w=280&fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=bfd3c4660c778e1be7acd3776982bd51 280w, https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/xpander-ai/new-agent-button.png?w=560&fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=dcd18172bdaa45221db2f05c829b1f76 560w, https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/xpander-ai/new-agent-button.png?w=840&fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=6458dfc4abe49bc9c5ba060b3266d7a6 840w, https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/xpander-ai/new-agent-button.png?w=1100&fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=6ae95c5507c5606aa647a35bea579200 1100w, https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/xpander-ai/new-agent-button.png?w=1650&fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=6e02a221bc6af288df5a2428ccf16d42 1650w, https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/xpander-ai/new-agent-button.png?w=2500&fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=499ea42d515fd17c3b821bc168453705 2500w" />
    </Frame>
  </Step>

  <Step title="Basic Configuration" stepNumber="2">
    1. Choose an appropriate name for your agent. For example, if you want to create a web scraping agent, you can call it “Web Scraper Agent”.

    <Frame>
      <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/xpander-ai/new-agent-name.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=95dc67fb1eb54549b82393c33e6b5f23" alt="Calling the new agent “Web Scraper Agent”" width="3054" height="1495" data-path="images/integrations/xpander-ai/new-agent-name.png" />
    </Frame>

    2. Leave all other settings in the “General” tab as they are. The defaults are enough for a simple setup like this one. By default, xpander.ai will use [OpenAI’s GPT-4o as the LLM model](https://openai.com/index/hello-gpt-4o/).
  </Step>

  <Step title="Add Bright Data integration tools" stepNumber="3">
    1. Go to the “Tools” tab on your agent’s page, then click the “Add tools” button:

    <Frame>
      <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/xpander-ai/add-tools-button.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=c726e9e6003117c4c140b5a9aec6231f" alt="Clicking the “Add tools” button" width="3054" height="1491" data-path="images/integrations/xpander-ai/add-tools-button.png" />
    </Frame>

    2. Search for “bright data” on the right side panel and select the Bright Data integration:

    <Frame>
      <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/xpander-ai/select-bright-data-connector.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=39632947789b651e0706f0e19d88732b" alt="Selecting the Bright Data connector" width="825" height="495" data-path="images/integrations/xpander-ai/select-bright-data-connector.png" />
    </Frame>
  </Step>

  <Step title="Configure the Bright Data Connector" stepNumber="4">
    The following modal will show up:

    <Frame>
      <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/xpander-ai/connector-configuration-form.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=ed0a601236d549fc9a9a39cf18d8d91e" alt="Filling out the Bright Data connector configuration form" width="1176" height="1485" data-path="images/integrations/xpander-ai/connector-configuration-form.png" />
    </Frame>

    Fill it out as follows:

    | Configuration Option | Value                                          |
    | :------------------- | :--------------------------------------------- |
    | Connector name       | Bright Data Connector (or any name you prefer) |
    | Authentication mode  | API Key                                        |
    | Authentication scope | Integration user                               |
    | API Key              | \[Your Bright Data API key]                    |
    | Authentication type  | Bearer                                         |

    Once everything is filled in, press the “Save” button.
  </Step>

  <Step title="Select the Bright Data Tools" stepNumber="5">
    Now, you will be prompted to select the specific Bright Data tools you want to enable in your agent:

    <Frame>
      <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/xpander-ai/select-bright-data-tools.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=d41d86c017165693614fe81eef89731f" alt="Selecting the Bright Data tools to enable" width="790" height="657" data-path="images/integrations/xpander-ai/select-bright-data-tools.png" />
    </Frame>

    We recommend selecting all tools to unlock full web scraping capabilities. As of this writing, the available tools are:

    * **Start Data Collection Job by Dataset ID**: Launches a scraping job for a specified dataset using the [Scraperss](https://brightdata.com/products/web-scraper).
    * **Execute Proxy Request by URL**: Sends an HTTP request through [Bright Data’s proxy network](https://brightdata.com/proxy-types/) for accessing the content of any web page.
    * **Download Dataset Snapshot by ID**: Downloads a snapshot of a dataset in various formats, passing the data to the AI.
  </Step>

  <Step title="Add the Tools to Your Agent" stepNumber="6">
    Once you have selected the desired tools, click the “Add to agent” button in the bottom-right corner:

    <Frame>
      <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/xpander-ai/add-to-agent-button.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=31856f9ab4b658d1bb9daf16939c2dec" alt="Clicking the “Add to agent” button" width="811" height="127" data-path="images/integrations/xpander-ai/add-to-agent-button.png" />
    </Frame>

    The “Tools” tab of your agent will now show the Bright Data connector with the tools you configured:

    <Frame>
      <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/xpander-ai/configured-bright-data-tools.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=8e6d49f4e93505384b4f553e69d129fd" alt="Note the configured Bright Data tools" width="1163" height="622" data-path="images/integrations/xpander-ai/configured-bright-data-tools.png" />
    </Frame>

    Notice that you can click on any tool to view or adjust its configuration.

    Fantastic! Your AI agent is now fully integrated with Bright Data tools and ready to scrape the web.
  </Step>

  <Step title="Specialize Your AI Scraping Agent" stepNumber="7">
    Now that your agent has access to the Bright Data tools for web scraping, give it a custom [system prompt](https://www.promptlayer.com/glossary/system-prompt). This tells the agent what it is and how it should operate.

    To do this, click on the “Instructions” tab and paste something like the following into the “System prompt” textarea:

    ```text theme={null}
    You are an AI agent capable of grounding your responses by scraping data from the web
    ```

    <Frame>
      <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/xpander-ai/agent-system-prompt.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=336b045b868b5616754e6c00d887761b" alt="Adding a system prompt to your agent" width="1144" height="1178" data-path="images/integrations/xpander-ai/agent-system-prompt.png" />
    </Frame>

    For more specialized agents, you can also add custom rules and goals.

    Amazing! Your xpander scraping agent is ready.
  </Step>

  <Step title="View the Agent Graph" stepNumber="8">
    Click on the “Agent graph” button to view your current AI agent workflow:

    <Frame>
      <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/xpander-ai/agent-graph.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=d5b4ab5bdc8364d87f434c179d2baf2b" alt="The agent graph" width="1759" height="1161" data-path="images/integrations/xpander-ai/agent-graph.png" />
    </Frame>

    You will see a single agent with access to the three configured Bright Data tools for web scraping.

    Well done! All that is left is to test the agent and see it in action.
  </Step>

  <Step title="Send a Prompt to Your Agent" stepNumber="9">
    Go back to the “Tester Chat” tab and try out your agent with a prompt like this:

    ```text theme={null}
    Search for top 3 headphones under $100 and provide me info from their PDP's
    ```

    This instructs your web scraping agent to dynamically look online for the top 3 headphones priced under \$100 and retrieve information directly from their [product detail pages (PDPs)](https://www.dynamicyield.com/glossary/product-detail-page/).

    As you can imagine, a standard LLM would be able to handle this kind of task without access to dedicated scraping tools like those provided by Bright Data.

    Paste the prompt into the chat input and send it to your agent:

    <Frame>
      <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/xpander-ai/ai-scraping-agent-in-action.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=9bd2b7ecc7eb71fd23acd4ade8287ab1" alt="The AI scraping agent in action" width="1080" height="486" data-path="images/integrations/xpander-ai/ai-scraping-agent-in-action.png" />
    </Frame>
  </Step>

  <Step title="Analyze the Agent's Response" stepNumber="10">
    The agent uses the LLM and Bright Data tools to:

    1. Perform a web search and find the top 3 headphones.
    2. For each product, start a data collection job and download data from Amazon.
    3. Summarize the information into a short, accurate response, complete with real-world links to the Amazon product detail pages.
  </Step>

  <Step title="Inspect the Tool Calls" stepNumber="11">
    If you expand one of the tool sections in the interface, you will see something like this:

    <Frame>
      <img src="https://mintcdn.com/brightdata/z2V3XghEDR2bikNt/images/integrations/xpander-ai/tool-call-io-details.png?fit=max&auto=format&n=z2V3XghEDR2bikNt&q=85&s=2e87ba23f86f6f861a21de5e13309679" alt="The I/O details from a tool call" width="1657" height="1029" data-path="images/integrations/xpander-ai/tool-call-io-details.png" />
    </Frame>

    This proves that, behind the scenes, the AI agent automatically detected which Bright Data tools to use to complete the task. In detail, it called them with the right parameters to fetch fresh scraped data (in this case, directly from Amazon product pages).
  </Step>
</Steps>

Et voilà! You now have a fully functional scraping agent on xpander.ai, powered by Bright Data’s AI data infrastructure.
