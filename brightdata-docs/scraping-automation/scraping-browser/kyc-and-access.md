> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Browser API and KYC

> What the Bright Data Browser API reaches without KYC, which navigations return brob or brul and how to complete KYC verification in 4 steps.

The Bright Data Browser API works without KYC. The main restriction is that URLs disallowed by a target's `robots.txt` are blocked until KYC is approved, password entry is disabled by default and some targets are restricted by Bright Data's compliance policy.

## What can I use without KYC?

Every Browser API capability below is available in immediate access mode, which is the mode every account starts in before KYC approval.

| Capability                                                 | Without KYC                            |
| ---------------------------------------------------------- | -------------------------------------- |
| Navigating to any URL allowed by the target's `robots.txt` | Available                              |
| CAPTCHA solving, country targeting, session persistence    | Available                              |
| URLs disallowed by the target's `robots.txt`               | Requires KYC                           |
| Government websites                                        | Requires KYC                           |
| Domains in a blocked classification                        | Requires KYC                           |
| Targets restricted by Bright Data (`brul`)                 | Requires compliance approval           |
| Password entry                                             | Requires KYC, then compliance approval |

## What requires KYC?

### Why does a navigation fail with brob?

Without KYC your account is in immediate access mode, which honors the target's `robots.txt`. Navigating to a disallowed URL fails with `brob`.

<Warning>
  `brob` is not an HTTP status. The Browser API rejects the navigation at the CDP layer, so `page.goto()` throws instead of returning a response, and checking `response.status()` never sees it. This behavior is the same in Puppeteer, Playwright and raw CDP.
</Warning>

The Browser API returns this message on the thrown error:

```text brob error message theme={null}
Protocol error (Page.navigate): Requested URL (https://www.reddit.com/r/programming/) is restricted in accordance with robots.txt. Ask your account manager to get full access for targeting this site (brob). Learn more: https://docs.brightdata.com/scraping-automation/scraping-browser/error-codes#access-and-permissions
```

Because the navigation throws, catch `brob` instead of reading a status code:

```javascript Catch brob in Puppeteer theme={null}
import puppeteer from 'puppeteer-core';

const AUTH = 'USER:PASS';
const browser = await puppeteer.connect({
  browserWSEndpoint: `wss://${AUTH}@brd.superproxy.io:9222`,
});

try {
  const page = await browser.newPage();
  await page.goto('https://www.reddit.com/r/programming/', { waitUntil: 'domcontentloaded' });
  console.log(await page.title());
} catch (err) {
  if (err.message.includes('(brob)')) {
    console.error('URL is disallowed by the target robots.txt in immediate access mode.');
  } else {
    throw err;
  }
} finally {
  await browser.close();
}
```

Check the target's own rules before treating a block as a bug:

```bash Read the target robots.txt theme={null}
curl -s https://example.com/robots.txt
```

Some sites disallow their whole domain. `reddit.com/robots.txt` is `User-agent: *` followed by `Disallow: /`, so no Reddit URL is available in immediate access mode.

### What does brul mean?

`brul` means Bright Data restricts the target, independently of the target's `robots.txt`. KYC alone does not lift a `brul` block. If access to the restricted target is required, request permission from [compliance@brightdata.com](mailto:compliance@brightdata.com) and describe your use case.

### Which targets are blocked regardless of robots.txt?

Bright Data's compliance policy restricts three groups of targets no matter what the target's `robots.txt` allows:

* **Government websites.** Blocked by default. The match is not limited to `.gov` or `.gov.[country_code]` suffixes, so a government site on any domain still qualifies. See [How do I target government websites?](/proxy-networks/faqs#how-do-i-target-government-websites) in the proxy FAQs.
* **Domains in a blocked classification.** Bright Data classifies domains and blocks some classifications. The response names the classification that matched.
* **Domains outside your approved use case.** After KYC, access is scoped to the use case the Bright Data compliance team approved. Requests outside that use case return an `Access denied` error naming the classified category.

KYC is the route to request access to any of these three groups.

### Can the Browser API enter passwords?

No, not by default. Password entry is disabled so that no data behind a login is collected, in line with the Bright Data [Acceptable Use Policy](https://brightdata.com/acceptable-use-policy). To request an exception, complete KYC first, then contact [compliance@brightdata.com](mailto:compliance@brightdata.com). You can also request password entry during the KYC submission itself.

## Which error codes relate to access?

Both access codes below are listed under [Access and permissions](/scraping-automation/scraping-browser/error-codes#access-and-permissions) in the Browser API error codes reference, which is the source of truth for every Browser API code.

| Error Code | Meaning                                                                                   | Suggested Action                                                                                                                         |
| ---------- | ----------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `brob`     | The target's `robots.txt` disallows this URL and the account is in immediate access mode. | Complete [KYC verification](/proxy-networks/residential/network-access#kyc-verification), or navigate to a URL that `robots.txt` allows. |
| `brul`     | Bright Data restricts the target.                                                         | If access to the restricted target is required, request permission from [compliance@brightdata.com](mailto:compliance@brightdata.com).   |

## How do I complete KYC?

1. **Add funds to your account balance.** KYC cannot be started in [Playground](/general/faqs#what-is-playground-mode) or [Limited Trial](/general/faqs#what-is-limited-trial-mode) mode.
2. **Add a user with a company email domain.** KYC applications are accepted only from registered businesses, so an account on a personal email domain cannot be approved.
3. **Submit the KYC form.** Describe your business and your use case, and attach a company registration document. Access is granted against the use case you describe, so describe it fully. Password entry can be requested here too. [Start KYC verification](https://brightdata.com/cp/kyc)
4. **Wait for review.** A person reviews every submission, so approval is never instant. You are updated within 48 hours. Check the status in your control panel under **Settings > Profile**.

## FAQ

### Is KYC the same as account verification?

No. [Account verification](/general/account/limited-trial-restrictions) lifts Limited Trial rate and balance limits. KYC is a separate, human-reviewed compliance check. An HTTP 429 rate limit error points to account verification, while `brob` points to KYC.

### Does KYC give unlimited access?

No. KYC is reviewed against the use case you submit, and access is scoped to that use case. Password entry requires Bright Data compliance approval on top of KYC, and `brul` targets are assessed by the compliance team case by case.

### Can I use the Browser API while my KYC is under review?

Yes. The Browser API keeps working in immediate access mode while the Bright Data compliance team reviews your KYC submission. Only the navigations listed in this page's capability table stay blocked until approval.

### Which proxy network does the Browser API use?

The Browser API uses Residential proxies by default. For some domains that require KYC, the Browser API may switch to Datacenter proxies automatically for compliance, which can change peer geolocation and cost.

<Note>
  The [Residential network access policy](/proxy-networks/residential/network-access) covers Residential zone access and its KYC requirements. Some details on that page, including SSL errors and other proxy types, do not apply to the Browser API.
</Note>

## Related

* [Browser API error codes](/scraping-automation/scraping-browser/error-codes): Every Browser API error code, grouped into four categories.
* [Web Unlocker API and KYC](/scraping-automation/web-unlocker/kyc-and-access): The same access rules for the Web Unlocker API.
* [Residential network access policy](/proxy-networks/residential/network-access): Why KYC exists and what the Bright Data compliance team reviews.
* [Browser API FAQs](/scraping-automation/scraping-browser/faqs): Password entry, proxy types and other common questions.
