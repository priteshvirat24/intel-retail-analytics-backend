> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Understanding the AI Scraper Studio APIs

> Use Bright Data Scraper Studio AI Flow APIs to create scrapers with AI, monitor job progress and update existing scrapers with the Self-Healing tool.

The AI Scraper Studio API is a set of endpoints that let you create Scraper Studio scrapers with AI and update existing scrapers using Self-Healing tool, without using the UI. This page explains which endpoint to call and in what order.

Both flows are asynchronous: you start an AI job, then check its progress until it completes.

## Workflow 1: Create a new scraper with AI

Use these endpoints when you want AI to generate a scraper (schema + code) from scratch for a target site.

1. Create the scraper entity<br />→ <Badge color="blue">Create scraper template</Badge>
2. Start the AI generation job (schema + code)<br />→ <Badge color="blue">Trigger AI Flow to create code</Badge>
3. Poll until the AI job finishes and returns the result<br />→ <Badge color="blue">AI job progress</Badge>

## Workflow 2: Update an existing scraper with Self-Healing

Use these endpoints when you already have a scraper and want to fix or modify it using a prompt.

1. Start a Self-Healing refactor job<br />→ <Badge color="blue">Trigger Self-Healing</Badge>
2. Poll until the refactor job finishes or pauses for user input<br />→ <Badge color="blue">Self-Healing job progress</Badge>
3. If progress returns `status: "pending_answer"`, approve or reject the proposed diff<br />→ <Badge color="blue">Resume Self-Healing job</Badge>
4. After the scraper is ready, initiate collection<br />→ <Badge color="blue">Initiate collection</Badge>

Once created or updated, run it using the standard Scraper Studio API initiation endpoints (manual trigger, schedule, queue, etc.).

<Columns cols={2}>
  <Tip>
    **Not sure which to use?**

    * No scraper yet → [Workflow 1](#workflow-1-create-a-new-scraper-with-ai)
    * Scraper needs changes → [Workflow 2](#workflow-2-update-an-existing-scraper-with-self-healing)
  </Tip>

  <Tip>
    **New to the API?**

    See: <a href="/datasets/scraper-studio/quickstart" target="_blank">Getting started with the API</a>
  </Tip>
</Columns>
