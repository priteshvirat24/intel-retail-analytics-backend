> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Scraper Studio Auto Self-Healing

> Configure Auto Self-Healing in Bright Data Scraper Studio to fix a scraper automatically when its success rate drops or 1 of 6 supported errors occurs.

Use the **Auto Self-Healing** tab to let Bright Data Scraper Studio try to fix a scraper on its own when collection quality drops or a supported scraper error occurs. Auto Self-Healing jobs do not cost credits.

Auto Self-Healing is configured per scraper. Once enabled, Bright Data Scraper Studio monitors that scraper's runs and starts a healing job whenever the trigger rules you set are met.

<Note>
  Auto Self-Healing runs without you asking. To fix a scraper on demand from a plain-language prompt instead, use the [Self-Healing tool](/datasets/scraper-studio/self-healing-tool) in the Scraper Studio IDE.
</Note>

## How do I open Auto Self-Healing settings?

1. Open **My Scrapers** in Bright Data Scraper Studio.
2. Select the scraper you want to configure.
3. Open the **Auto Self-Healing** tab.
4. Configure the general settings, trigger rules and notifications.
5. Click **Save**.

Saved settings apply to future runs of that scraper. Runs that already completed are not reprocessed.

## Which general settings control Auto Self-Healing?

| Setting                      | Options | What it does                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Enable Auto self healing** | On, Off | Turns Auto Self-Healing on or off for this scraper. When On, Bright Data Scraper Studio can start healing jobs as soon as the trigger rules are met.                                                                                                                                                                                                                                                                    |
| **Auto save code**           | On, Off | Controls whether Bright Data Scraper Studio saves the code the healing process generates. When On, any successful healing job saves the newly extracted code to production and updates the collector's template version. When Off, the healing job still runs but the generated code is not saved, and the users you select under **Notifications** get an email so they can review the suggested fix before saving it. |

<Warning>
  **Auto save code** writes straight to production. A successful healing job saves the new code and bumps the collector's template version with no human review, so the next run collects with AI-written code. Turn it on only when you accept that. Leave it Off to keep a review step before any fix reaches production.
</Warning>

## Which trigger rules start a healing job?

Trigger rules decide when Auto Self-Healing starts for the scraper you are configuring. **Success Rate Threshold** and **Minimum Inputs Threshold** are required fields.

| Trigger rule                      | Default | What it controls                                                                                                                                                                                          |
| --------------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Success Rate Threshold (%)**    | `40`    | The success rate below which Auto Self-Healing triggers. At `40`, a healing job can start once the scraper's success rate falls below 40 percent.                                                         |
| **Trigger Frequency**             | Per Day | Whether Bright Data Scraper Studio checks once per day (**Per Day**) or on every job run (**Per Job**).                                                                                                   |
| **Minimum Inputs Threshold**      | `10`    | The minimum number of job inputs required before Auto Self-Healing triggers. A run smaller than this never starts a healing job, so a handful of failures in a tiny run does not count as a quality drop. |
| **Cooldown Period (hours)**       | `3`     | The minimum hours to wait between consecutive Auto Self-Healing triggers for this scraper.                                                                                                                |
| **Max Auto-Healing Jobs Per Day** | `8`     | The maximum number of Auto Self-Healing jobs allowed for this scraper in one day.                                                                                                                         |

A healing job that fails still counts against **Max Auto-Healing Jobs Per Day** and still starts the **Cooldown Period**.

## Which error codes trigger Auto Self-Healing?

Auto Self-Healing starts only for these six scraper error codes:

* `crawl_error`
* `parse_error`
* `bad_cmd_arg`
* `dead_page`
* `bad_input`
* `bad_navigate`

A scraper that fails with any other error code does not start Auto Self-Healing, even when every trigger rule is met. For what each code means and how to resolve it by hand, see [Scraper Studio error codes](/datasets/scraper-studio/error-codes).

## Where do I see status and notifications?

The **Status** section of the **Auto Self-Healing** tab reports this scraper's healing-job activity. Before any healing job has run it reads `No auto healing jobs were triggered`.

The **Notifications** section has a **Select users to notify** picker listing the users on your account. Selected users get email when Auto Self-Healing is triggered, when it completes and when it needs attention. Add at least one user when **Auto save code** is Off, because the review email is the only way a suggested fix reaches a person.

## FAQ

### How is Auto Self-Healing different from the Self-Healing tool?

Auto Self-Healing runs on its own against trigger rules you configure per scraper. The [Self-Healing tool](/datasets/scraper-studio/self-healing-tool) is manual: you open a scraper in the Scraper Studio IDE, describe the fix in plain language and review the diff before accepting it. Auto Self-Healing needs no prompt.

### Does Auto Self-Healing change my scraper without asking?

Only when **Auto save code** is On. With **Auto save code** Off, Bright Data Scraper Studio still runs the healing job but does not save the generated code, and emails the users selected under **Notifications** to review the suggested fix first.

### Why did Auto Self-Healing not start after my scraper failed?

Check the failure's error code first. Auto Self-Healing starts only for the six error codes listed on this page, so a scraper that fails with any other code never triggers it. If the code is supported, check the other trigger rules set on the scraper: the run may have had fewer inputs than **Minimum Inputs Threshold**, or the scraper may still be inside its **Cooldown Period** or have already hit **Max Auto-Healing Jobs Per Day**. Failed healing jobs count toward both limits.

### Can I configure Auto Self-Healing through the API?

Not yet. The Auto Self-Healing rules are set in the control panel only. The [AI Flow API](/api-reference/scraper-studio-api/ai-flow/overview) can start a self-healing job on demand with [Trigger Self-Healing](/api-reference/scraper-studio-api/ai-flow/trigger-self-healing), but it does not expose the trigger rules on this page.

### Do the settings affect runs that already finished?

No. Auto Self-Healing settings apply to future runs of the scraper. Runs that already completed are not changed or reprocessed.

## Related

<CardGroup cols={2}>
  <Card title="Self-Healing tool" icon="wand-magic-sparkles" href="/datasets/scraper-studio/self-healing-tool">
    Fix a scraper on demand from a plain-language prompt
  </Card>

  <Card title="Scraper Studio error codes" icon="triangle-exclamation" href="/datasets/scraper-studio/error-codes">
    What each scraper error code means and how to resolve it
  </Card>

  <Card title="Trigger Self-Healing API" icon="code" href="/api-reference/scraper-studio-api/ai-flow/trigger-self-healing">
    Start a self-healing job from the AI Flow API
  </Card>

  <Card title="Initiate collection and delivery" icon="paper-plane" href="/datasets/scraper-studio/initiate-collection-and-delivery-options">
    Run a production scraper and configure delivery
  </Card>
</CardGroup>
