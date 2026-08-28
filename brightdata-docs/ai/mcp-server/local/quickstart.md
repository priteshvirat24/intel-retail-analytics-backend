> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to set up local (self-hosted) MCP

> Set up a self-hosted Bright Data MCP server: step-by-step installation, configuration and connection to AI agents like Claude or Cursor in under 10 minutes.

<Card title="Building an AI startup?" cta="Learn more" href="https://brightdata.com/ai/ai-startups-program" icon="rocket-launch" iconType="duotone" arrow="true">
  You might be eligible for our Startup Program. Get fully funded access to the infrastructure you're reading about right now (up to \$20K value).
</Card>

<Steps>
  <Step title="Prerequisites">
    Before you begin, make sure you have the following:

    <CardGroup cols={2}>
      <Card title="Bright Data Account" icon="user" href="https://brightdata.com/?hs_signup=1&utm_source=docs">
        *Sign up for free and receive **5,000 requests** per month at no cost.*
      </Card>

      <Card title="Your Bright Data API Key" icon="key" href="https://brightdata.com/cp/setting">
        *New users receive their API key in the welcome email.*
      </Card>
    </CardGroup>

    <Card title="Node.js" icon="node-js" href="https://nodejs.org/en/download">
      *Ensure Node.js is installed and up to date.*
    </Card>

    <Tip>
      No username is required. The self-hosted MCP server authenticates with your `API_TOKEN` only. Usernames (format: `brd-customer-{customer_id}-zone-{zone_name}`) are for native proxy access, not MCP. If a third-party tool asks for a username, leave it empty.
    </Tip>
  </Step>

  <Step title="Choose Your Client">
    Select and configure your preferred MCP client:

    * <a href="/ai/mcp-server/integrations/claude#self-hosted-mcp"><span style={{ display: "inline-flex", alignItems: "center", gap: "4px" }}>{<svg xmlns="http://www.w3.org/2000/svg" fillRule="evenodd" clipRule="evenodd" imageRendering="optimizeQuality" shapeRendering="geometricPrecision" textRendering="geometricPrecision" viewBox="0 0 512 509.64" width="24" height="24"><path fill="#D77655" d="M115.612 0h280.775C459.974 0 512 52.026 512 115.612v278.415c0 63.587-52.026 115.612-115.613 115.612H115.612C52.026 509.639 0 457.614 0 394.027V115.612C0 52.026 52.026 0 115.612 0"></path><path fill="#FCF2EE" fillRule="nonzero" d="m142.27 316.619 73.655-41.326 1.238-3.589-1.238-1.996-3.589-.001-12.31-.759-42.084-1.138-36.498-1.516-35.361-1.896-8.897-1.895-8.34-10.995.859-5.484 7.482-5.03 10.717.935 23.683 1.617 35.537 2.452 25.782 1.517 38.193 3.968h6.064l.86-2.451-2.073-1.517-1.618-1.517-36.776-24.922-39.81-26.338-20.852-15.166-11.273-7.683-5.687-7.204-2.451-15.721 10.237-11.273 13.75.935 3.513.936 13.928 10.716 29.749 23.027 38.848 28.612 5.687 4.727 2.275-1.617.278-1.138-2.553-4.271-21.13-38.193-22.546-38.848-10.035-16.101-2.654-9.655c-.935-3.968-1.617-7.304-1.617-11.374l11.652-15.823 6.445-2.073 15.545 2.073 6.547 5.687 9.655 22.092 15.646 34.78 24.265 47.291 7.103 14.028 3.791 12.992 1.416 3.968 2.449-.001v-2.275l1.997-26.641 3.69-32.707 3.589-42.084 1.239-11.854 5.863-14.206 11.652-7.683 9.099 4.348 7.482 10.716-1.036 6.926-4.449 28.915-8.72 45.294-5.687 30.331h3.313l3.792-3.791 15.342-20.372 25.782-32.227 11.374-12.789 13.27-14.129 8.517-6.724 16.1-.001 11.854 17.617-5.307 18.199-16.581 21.029-13.75 17.819-19.716 26.54-12.309 21.231 1.138 1.694 2.932-.278 44.536-9.479 24.062-4.347 28.714-4.928 12.992 6.066 1.416 6.167-5.106 12.613-30.71 7.583-36.018 7.204-53.636 12.689-.657.48.758.935 24.164 2.275 10.337.556h25.301l47.114 3.514 12.309 8.139 7.381 9.959-1.238 7.583-18.957 9.655-25.579-6.066-59.702-14.205-20.474-5.106-2.83-.001v1.694l17.061 16.682 31.266 28.233 39.152 36.397 1.997 8.999-5.03 7.102-5.307-.758-34.401-25.883-13.27-11.651-30.053-25.302-1.996-.001v2.654l6.926 10.136 36.574 54.975 1.895 16.859-2.653 5.485-9.479 3.311-10.414-1.895-21.408-30.054-22.092-33.844-17.819-30.331-2.173 1.238-10.515 113.261-4.929 5.788-11.374 4.348-9.478-7.204-5.03-11.652 5.03-23.027 6.066-30.052 4.928-23.886 4.449-29.674 2.654-9.858-.177-.657-2.173.278-22.37 30.71-34.021 45.977-26.919 28.815-6.445 2.553-11.173-5.789 1.037-10.337 6.243-9.2 37.257-47.392 22.47-29.371 14.508-16.961-.101-2.451h-.859l-98.954 64.251-17.618 2.275-7.583-7.103.936-11.652 3.589-3.791 29.749-20.474-.101.102z"></path></svg>} Claude</span></a>
    * <a href="/integrations/n8n#self-hosted-mcp-integration"><span style={{ display: "inline-flex", alignItems: "center", gap: "4px" }}>{<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 228 120"><path fill="#EA4B71" fillRule="evenodd" d="M204 48c-11.183 0-20.58-7.649-23.244-18h-27.508a12 12 0 0 0-11.836 10.027l-.987 5.919A23.94 23.94 0 0 1 132.626 60a23.94 23.94 0 0 1 7.799 14.054l.987 5.919A12 12 0 0 0 153.248 90h3.508C159.42 79.649 168.817 72 180 72c13.255 0 24 10.745 24 24s-10.745 24-24 24c-11.183 0-20.58-7.649-23.244-18h-3.508c-11.732 0-21.744-8.482-23.673-20.054l-.987-5.919A12 12 0 0 0 116.752 66h-9.508C104.58 76.351 95.183 84 84 84s-20.58-7.649-23.244-18H47.244C44.58 76.351 35.183 84 24 84 10.745 84 0 73.255 0 60s10.745-24 24-24c11.183 0 20.58 7.649 23.244 18h13.512C63.42 43.649 72.817 36 84 36s20.58 7.649 23.244 18h9.508a12 12 0 0 0 11.836-10.027l.987-5.919C131.504 26.482 141.516 18 153.248 18h27.508C183.42 7.649 192.817 0 204 0c13.255 0 24 10.745 24 24s-10.745 24-24 24m0-12c6.627 0 12-5.373 12-12s-5.373-12-12-12-12 5.373-12 12 5.373 12 12 12M24 72c6.627 0 12-5.373 12-12s-5.373-12-12-12-12 5.373-12 12 5.373 12 12 12m72-12c0 6.627-5.373 12-12 12s-12-5.373-12-12 5.373-12 12-12 12 5.373 12 12m96 36c0 6.627-5.373 12-12 12s-12-5.373-12-12 5.373-12 12-12 12 5.373 12 12" clipRule="evenodd"></path></svg>} n8n</span></a>
  </Step>

  <Step title="Quick Examples">
    Try these example prompts with your MCP server:

    <AccordionGroup>
      <Accordion title="Extract real-time data from Google" iconType="sharp-solid">
        “Extract all flight times departing from JFK Airport to Heathrow in the next 24 hours.”
      </Accordion>

      <Accordion title="Extract company data from LinkedIn">
        “Extract the Bright Data overview section from LinkedIn.”
      </Accordion>

      <Accordion title="Extract dynamic data from eBay">
        “Go to ebay.com, click the ‘Shop by category’ button in the navigation bar, and extract all categories.”
      </Accordion>
    </AccordionGroup>
  </Step>
</Steps>

<Card title="Advanced Configuration" cta="Click here" icon="sliders" href="/ai/mcp-server/local/advanced">
  See the Advanced Configuration page for more details.
</Card>
