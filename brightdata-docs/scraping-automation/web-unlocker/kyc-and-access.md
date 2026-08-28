> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Web Unlocker API and KYC

> What the Bright Data Web Unlocker API reaches without KYC, which requests return ub_bad_endpoint_robots or a policy_ 403 and how to complete KYC.

The Bright Data Web Unlocker API works without KYC. The main restriction is that endpoints disallowed by a target's `robots.txt` are blocked until KYC is approved, and some targets additionally require special permission under Bright Data's compliance policy.

## What can I use without KYC?

Every Web Unlocker API capability below is available in immediate access mode, which is the mode every account starts in before KYC approval.

| Capability                                          | Without KYC  |
| --------------------------------------------------- | ------------ |
| Any endpoint allowed by the target's `robots.txt`   | Available    |
| Premium domains, custom features, country targeting | Available    |
| Direct API and native proxy access modes            | Available    |
| Endpoints disallowed by the target's `robots.txt`   | Requires KYC |
| Government websites                                 | Requires KYC |
| Domains in a blocked classification                 | Requires KYC |

## What requires KYC?

### Why does a request fail with ub\_bad\_endpoint\_robots?

Without KYC your account is in immediate access mode, which honors the target's `robots.txt`. Requesting a disallowed endpoint returns `ub_bad_endpoint_robots` with HTTP status 400:

```http ub_bad_endpoint_robots response theme={null}
X-Brd-Error-Code: ub_bad_endpoint_robots
X-Brd-Error: Request Failed (bad_endpoint): Requested site is not available for immediate access mode in accordance with robots.txt. Ask your account manager to get full access for targeting this site
```

Check the target's own rules before treating a block as a bug:

```bash Read the target robots.txt theme={null}
curl -s https://example.com/robots.txt
```

Some sites disallow their whole domain. `reddit.com/robots.txt` is `User-agent: *` followed by `Disallow: /`, so no Reddit endpoint is available in immediate access mode.

### Which targets require special permission?

Bright Data's compliance policy restricts three groups of targets no matter what the target's `robots.txt` allows:

* **Government websites.** Blocked by default and returns `policy_20051`. The match is not limited to `.gov` or `.gov.[country_code]` suffixes, so a government site on any domain still qualifies.
* **Domains in a blocked classification.** Bright Data classifies domains and blocks some classifications, and returns `policy_20000`. The response names the classification that matched.
* **Domains outside your approved use case.** After KYC, access is scoped to the use case the Bright Data compliance team approved. Requests outside that use case return an `Access denied` error naming the classified category.

All three return HTTP 403 with the code in `x-brd-err-code`, and KYC is the route to request access. For more on government targets, see [How do I target government websites?](/proxy-networks/faqs#how-do-i-target-government-websites) in the proxy FAQs.

## Which error codes relate to access?

The [Web Unlocker API error codes](/scraping-automation/web-unlocker/error-codes) reference and the [proxy errors catalog](/proxy-networks/errorCatalog) are the source of truth for every code below.

| Error Code               | Meaning                                                                                                                  | Suggested Action                                                                                                                                         |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ub_bad_endpoint_robots` | The requested endpoint is disallowed by the target's `robots.txt` and the account is in immediate access mode. HTTP 400. | Complete [KYC verification](/proxy-networks/residential/network-access#kyc-verification), or request an endpoint that `robots.txt` allows.               |
| `policy_20000`           | The target is classified in a category that Bright Data blocks. HTTP 403.                                                | Complete [KYC verification](/proxy-networks/residential/network-access#kyc-verification) and describe your use case.                                     |
| `policy_20050`           | The target is not permitted by Bright Data's compliance policy. HTTP 403.                                                | Complete [KYC verification](/proxy-networks/residential/network-access#kyc-verification). If your KYC is already approved, contact your account manager. |
| `policy_20051`           | The target is a government site and requires special permission. HTTP 403.                                               | Complete [KYC verification](/proxy-networks/residential/network-access#kyc-verification). If your KYC is already approved, contact your account manager. |

<Warning>
  `policy_20050` and `policy_20051` return the same `x-brd-error` text, "Forbidden: target site requires special permission. Contact Bright Data for assistance". Branch on `x-brd-err-code`, not on the message. Full text for every code is in the [proxy errors catalog](/proxy-networks/errorCatalog).
</Warning>

The status appears in a different place in each access mode. On the Direct API the outer response is `200` and the result status is in `x-brd-status-code`. On the native proxy the status is the response's own HTTP status, with the message in the status reason phrase. The `x-brd-error-code` value is the same in both modes. See [Web Unlocker API error codes](/scraping-automation/web-unlocker/error-codes#where-does-the-error-appear-in-each-access-mode) for the full comparison.

## How do I complete KYC?

1. **Add funds to your account balance.** KYC cannot be started in [Playground](/general/faqs#what-is-playground-mode) or [Limited Trial](/general/faqs#what-is-limited-trial-mode) mode.
2. **Add a user with a company email domain.** KYC applications are accepted only from registered businesses, so an account on a personal email domain cannot be approved.
3. **Submit the KYC form.** Describe your business and your use case, and attach a company registration document. Access is granted against the use case you describe, so describe it fully. [Start KYC verification](https://brightdata.com/cp/kyc)
4. **Wait for review.** A person reviews every submission, so approval is never instant. You are updated within 48 hours. Check the status in your control panel under **Settings > Profile**.

## FAQ

### Is KYC the same as account verification?

No. [Account verification](/general/account/limited-trial-restrictions) lifts Limited Trial rate and balance limits. KYC is a separate, human-reviewed compliance check. An HTTP 429 rate limit error points to account verification, while `ub_bad_endpoint_robots` points to KYC.

### Does KYC give unlimited access?

No. KYC is reviewed against the use case you submit, and access is granted for that use case. Targets that require special permission are assessed by the Bright Data compliance team case by case, and the [Acceptable Use Policy](https://brightdata.com/acceptable-use-policy) continues to apply.

### Can I use the Web Unlocker API while my KYC is under review?

Yes. The Web Unlocker API keeps working in immediate access mode while the Bright Data compliance team reviews your KYC submission. Only the requests listed in this page's capability table stay blocked until approval.

## Related

* [Web Unlocker API error codes](/scraping-automation/web-unlocker/error-codes): Every Web Unlocker API error code, grouped by HTTP status.
* [Browser API and KYC](/scraping-automation/scraping-browser/kyc-and-access): The same access rules for the Browser API.
* [Residential network access policy](/proxy-networks/residential/network-access): Why KYC exists and what the Bright Data compliance team reviews.
* [Proxy errors catalog](/proxy-networks/errorCatalog): Full text for every `policy_` code.
