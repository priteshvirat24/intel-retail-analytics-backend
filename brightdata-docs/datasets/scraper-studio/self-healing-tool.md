> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Fix scrapers with the Self-Healing tool

> Use the Bright Data Scraper Studio Self-Healing tool to fix broken scrapers and add or remove output fields from plain-language prompts in 1 click.

The Self-Healing tool is an AI-powered code refactor assistant in Bright Data Scraper Studio that rewrites parts of a scraper from a plain-language prompt. Use it when a target site changes and your scraper stops returning the expected data, or when you need to add or remove output fields without editing the JavaScript by hand.

<Tip>
  **When to use it:** the scraper stops returning expected data, the price or title field returns `undefined`, or you need to add new fields (`price`, `image`, `rating`) without writing code.
</Tip>

<Note>
  The Self-Healing tool is manual: you write the prompt and review the diff. To let Bright Data Scraper Studio fix a scraper on its own when its success rate drops or a supported error occurs, configure [Auto Self-Healing](/datasets/scraper-studio/auto-self-healing) on the scraper.
</Note>

## Prerequisites

* An active [Bright Data account](https://brightdata.com/)
* An existing scraper in Bright Data Scraper Studio (saved in development mode)
* Access to the Scraper Studio IDE

## How do I fix a scraper with the Self-Healing tool?

<Steps>
  <Step title="Open the Self-Healing tool">
    In the Bright Data Scraper Studio IDE, open the scraper you want to fix and locate the Self-Healing tool panel.

    <Frame>
      <img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/datasets/scraper-studio/self-healing-tool/self-healing-tool-location.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=3bd27d4180e3e9b625c5330c8d18c016" alt="Self-Healing tool location in the Scraper Studio IDE" width="2598" height="1902" data-path="images/datasets/scraper-studio/self-healing-tool/self-healing-tool-location.png" />
    </Frame>

    > **Expected result:** a text input field appears, ready to accept your instruction.

    <Frame>
      <img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/datasets/scraper-studio/self-healing-tool/refactor-collector.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=3c96296bab91ad177967c4da938e4893" alt="Refactor collector panel" width="1324" height="646" data-path="images/datasets/scraper-studio/self-healing-tool/refactor-collector.png" />
    </Frame>
  </Step>

  <Step title="Describe the fix or change you need">
    Type your request in plain language. Be specific about what is broken and which fields are affected.

    ```txt Example prompts theme={null}
    Add 'price' and 'image' fields to the output

    The 'price' value is returning 'undefined', please fix

    The 'price' field is returning incorrect data from HTML, switch to using tag_response() to capture '/api/price' instead
    ```

    > **Expected result:** the AI processes your prompt and produces a code diff in the editor.

    <Note>
      Refactoring can take up to 15 minutes. You do not need to stay on the page: Bright Data sends an email when the diff is ready, and you can review it at your convenience.

      <Frame>
        <img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/datasets/scraper-studio/self-healing-tool/email.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=fb39426badca7fc8650e78303c4e2c45" alt="Email notification when refactoring is complete" width="1582" height="1252" data-path="images/datasets/scraper-studio/self-healing-tool/email.png" />
      </Frame>
    </Note>
  </Step>

  <Step title="Review the proposed changes">
    Examine the AI-generated diff in the code template. Verify it matches your intent before accepting.

    * **Accept:** saves the changes to a draft
    * **Decline:** discards the suggestion; your original code remains unchanged

    > **Expected result:** if accepted, the editor shows the updated code and saves it to the draft.
  </Step>

  <Step title="Run a preview">
    After accepting, run a preview to confirm the scraper returns the expected data.

    <Frame>
      <img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/datasets/scraper-studio/self-healing-tool/run-a-preview.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=e8ffc0990063361e4ea48692553c6671" alt="Run a preview button in the IDE" width="3158" height="924" data-path="images/datasets/scraper-studio/self-healing-tool/run-a-preview.png" />
    </Frame>

    > **Expected result:** the output file contains the new or fixed fields with valid, non-undefined values.

    <Frame>
      <img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/datasets/scraper-studio/self-healing-tool/view-download.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=784e2b9eb41b8ae3572ce3b13fd30a7c" alt="View and download preview results" width="1457" height="1091" data-path="images/datasets/scraper-studio/self-healing-tool/view-download.png" />
    </Frame>
  </Step>

  <Step title="Save to production">
    Once the preview looks correct, save the scraper to production.

    <Frame>
      <img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/datasets/scraper-studio/self-healing-tool/save-to-production.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=80e9fd0c44cbecec3fef1fe85ea415f5" alt="Save to production button" width="550" height="301" data-path="images/datasets/scraper-studio/self-healing-tool/save-to-production.png" />
    </Frame>

    <Note>
      If you added or renamed fields, Bright Data Scraper Studio prompts you to update the output schema. Click **Update Schema**, then **Save to Production**.

      <Frame>
        <img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/datasets/scraper-studio/self-healing-tool/update-schema.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=ee58b4b50ec6cfae93679be2425606ba" alt="Update schema prompt" width="982" height="535" data-path="images/datasets/scraper-studio/self-healing-tool/update-schema.png" />
      </Frame>
    </Note>

    > **Expected result:** the refactored scraper is live and collecting data with the new configuration.
  </Step>
</Steps>

## Troubleshooting

| Problem                                    | Likely cause                   | Resolution                                                                             |
| ------------------------------------------ | ------------------------------ | -------------------------------------------------------------------------------------- |
| AI-generated code does not fix the issue   | Prompt was too vague           | Re-prompt with specific field names and an example error message                       |
| Preview still returns undefined values     | Target site structure changed  | Inspect the live page and include the expected HTML element or selector in your prompt |
| Changes do not appear after accepting      | Browser cache issue            | Refresh the IDE and re-check the development mode draft                                |
| The refactor runs for more than 15 minutes | Complex change or heavy prompt | Break the request into smaller prompts (one field at a time)                           |

## Frequently asked questions

<AccordionGroup>
  <Accordion title="Does the Self-Healing tool work on every scraper?">
    Yes. The Self-Healing tool works on any scraper saved in development mode in Bright Data Scraper Studio, regardless of whether the scraper was built by the AI Agent, from a template, or written from scratch in the IDE.
  </Accordion>

  <Accordion title="Can I undo a Self-Healing change?">
    Yes. Accepted changes go to a draft first; they only affect production after you click **Save to Production**. If you already saved to production, open the **Versions** menu on the scraper dashboard to roll back to an earlier version.
  </Accordion>

  <Accordion title="What happens if I change the output schema?">
    The Self-Healing tool can add or remove fields, but you must confirm the schema change before saving to production. Bright Data Scraper Studio prompts you with **Update Schema** when the new output no longer matches the current schema.
  </Accordion>
</AccordionGroup>

## Related

<CardGroup cols={2}>
  <Card title="Scraper Studio AI Agent" icon="robot" href="/datasets/scraper-studio/ai-agent">
    Build a new scraper from natural-language prompts
  </Card>

  <Card title="Develop a scraper" icon="wrench" href="/datasets/scraper-studio/develop-a-scraper">
    Build and edit scrapers directly in the IDE
  </Card>

  <Card title="Auto Self-Healing" icon="wand-magic-sparkles" href="/datasets/scraper-studio/auto-self-healing">
    Fix a scraper automatically from per-scraper trigger rules
  </Card>
</CardGroup>
