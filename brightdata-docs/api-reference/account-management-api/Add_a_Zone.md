> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add a zone

> Use the Bright Data Account Management API to add a Zone. POST /zone returns 200 OK with zone or account configuration data as JSON.

<Warning>Only users with **Admin** or **Ops** roles can perform this action.</Warning>

<Warning>This API can modify your account settings, damage your operations or incur charges.</Warning>

<Tip>
  Paste your API key to the authorization field. To get an API key, [Create an account](https://brightdata.com/?hs_signup=1\&utm_source=docs\&utm_campaign=playground) and learn [how to generate an API key](/api-reference/authentication#how-do-i-generate-a-new-api-key%3F)
</Tip>

## ISP proxy zone examples

Creating an ISP zone requires specific parameter combinations. The fields below are not optional. Omitting them will silently create the wrong zone type or billing plan.

<Warning>
  Setting `zone.type` to `ISP` alone will create a **Datacenter zone**, not an ISP zone. You must also set `plan.pool_ip_type` to `static_res`. Country codes must be **lowercase** (e.g. `us`, `gb`). Uppercase codes return a misleading "no IPs available" error.
</Warning>

### Shared ISP (pay-per-GB)

```json theme={null}
{
  "zone": { "name": "my_isp_zone", "type": "ISP" },
  "plan": {
    "type": "static",
    "pool_ip_type": "static_res",
    "ips_type": "shared",
    "bandwidth": "bandwidth",
    "country": "us"
  }
}
```

### Shared ISP (unlimited bandwidth)

Setting `bandwidth: unlimited` alone **does not** activate unlimited billing. You must also include `unl_bw_tiers: std`.

```json theme={null}
{
  "zone": { "name": "my_isp_zone", "type": "ISP" },
  "plan": {
    "type": "static",
    "pool_ip_type": "static_res",
    "ips_type": "shared",
    "bandwidth": "unlimited",
    "unl_bw_tiers": "std",
    "country": "us"
  }
}
```

### Dedicated ISP (unlimited bandwidth)

```json theme={null}
{
  "zone": { "name": "my_isp_zone", "type": "ISP" },
  "plan": {
    "type": "static",
    "pool_ip_type": "static_res",
    "ips_type": "dedicated",
    "bandwidth": "unlimited",
    "unl_bw_tiers": "std",
    "country": "us",
    "ips": 10
  }
}
```

## Residential proxy zone

<Warning>
  **New Residential zones require KYC approval.** For Residential zones created after July 7, 2026, adding a zone is available only to KYC-verified companies. A request from an account that has not completed KYC is blocked and returns HTTP 403 with a compliance error. Residential zones created on or before July 7, 2026 are unaffected and continue to work as expected. Start at [KYC verification](https://brightdata.com/cp/kyc) and see the [Residential network access policy](/proxy-networks/residential/network-access).
</Warning>

Creating any Residential proxy type (shared rotating, IPv6 or dedicated) after July 7, 2026 requires KYC approval by the Bright Data compliance team. There is no automatic or no-KYC path for these new zones. Without KYC, create an [ISP](/proxy-networks/isp/introduction) or [Datacenter](/proxy-networks/data-center/introduction) zone instead.

### Dedicated Residential (gIP) zone

A dedicated Residential zone allocates a gIP (group of IPs) that is exclusive to a fixed list of target domains. Create one by setting `vips_type: "domain"` and including `domain_whitelist`.

<Warning>
  Dedicated Residential gIPs are **domain-restricted**. You must set `vips_type: "domain"` and include `domain_whitelist` (a space-separated list of target domains). `vip_country` applies only to dedicated zones. For a shared zone, set the country with the `-country` username flag instead. Country codes must be **lowercase** (e.g. `us`, `gb`).
</Warning>

The following payload creates a dedicated Residential zone with one US gIP scoped to `example.com`. This payload was verified working on July 9, 2026.

```json theme={null}
{
  "zone": { "name": "my_dedicated_resi_zone", "type": "resident" },
  "plan": {
    "type": "resident",
    "vips_type": "domain",
    "vips": 1,
    "vip_country": "us",
    "domain_whitelist": "example.com"
  }
}
```

The allocated gIP is exclusive to the domains listed in `domain_whitelist`. Requests to any other domain are routed through Bright Data's shared Datacenter proxies.

### Shared Residential country targeting

For shared Residential zones, country is not set with `vip_country`. Target countries at request level with the `-country-<code>` flag in the proxy username (for example `-country-us`), or set default countries in the control panel. See [How to configure your Residential proxy](/proxy-networks/residential/configure-your-proxy).

### Dedicated Residential gIP errors

An invalid dedicated Residential (gIP) payload returns one of the following errors.

| Error                                                                                                                                     | Cause                      | How to fix                                        |
| :---------------------------------------------------------------------------------------------------------------------------------------- | :------------------------- | :------------------------------------------------ |
| `Can't allocate required amount of gIPs. Dedicated gIPs are only supported with "vips_type": "domain" together with a "domain_whitelist"` | Wrong `vips_type` value    | Set `vips_type: "domain"`                         |
| `Can't allocate required amount of gIPs. Target domains ("domain_whitelist") are required to allocate dedicated gIPs`                     | Missing `domain_whitelist` | Add `domain_whitelist` with your target domain(s) |

### Residential 403 compliance errors

For Residential zones created after July 7, 2026, an Add-a-Zone request from an account that is not eligible returns HTTP 403 with one of the following compliance errors. Zones created on or before July 7, 2026 are not affected. See the [proxy errors catalog](/proxy-networks/errorCatalog#http-error-403) for the full catalog.

| Error code                  | When it fires                                       | How to fix                                                                                                                                          |
| :-------------------------- | :-------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| `kyc_required`              | A company-email account that has not completed KYC. | Start [KYC verification](https://brightdata.com/cp/kyc). A human compliance reviewer approves Residential access.                                   |
| `business_account_required` | A personal-email account (not a verified company).  | Use a corporate email and contact the Bright Data team to establish business eligibility. Personal-email accounts are not eligible for Residential. |

Each error returns a structured JSON body so integrations can branch on the stable `code` value. A company-email account without KYC receives `kyc_required`:

```json theme={null}
{
  "error": {
    "code": "kyc_required",
    "message": "Residential proxies are available to verified companies only, after KYC review, in accordance with Bright Data's compliance policy.",
    "action": "Start verification at brightdata.com/cp/kyc. Applications are reviewed by our compliance team.",
    "alternatives": [
      { "product": "ISP proxy", "plan": { "type": "static", "pool_ip_type": "static_res", "ips_type": "shared" } },
      { "product": "Web Unlocker API", "plan": { "type": "unblocker" } }
    ],
    "docs": "https://docs.brightdata.com/compliance/kyc"
  }
}
```

A personal-email account receives `business_account_required`, which does not offer KYC because personal accounts are not eligible:

```json theme={null}
{
  "error": {
    "code": "business_account_required",
    "message": "Residential proxies are available to verified companies only. Eligibility requires a corporate email and full verification with the Bright Data team.",
    "action": "Contact the Bright Data team with a corporate email to determine business eligibility for Residential access.",
    "alternatives": [
      { "product": "ISP proxy", "plan": { "type": "static", "pool_ip_type": "static_res", "ips_type": "shared" } },
      { "product": "Web Unlocker API", "plan": { "type": "unblocker" } }
    ],
    "docs": "https://docs.brightdata.com/compliance/kyc"
  }
}
```

Both bodies include an `alternatives` array with the exact `plan` objects to create a no-KYC [ISP](/proxy-networks/isp/introduction) or [Web Unlocker API](/scraping-automation/web-unlocker/introduction) zone instead. To create the ISP zone, send `POST /zone` with that `plan` object in place of the Residential one.


## OpenAPI

````yaml api-reference/openapi POST /zone
openapi: 3.0.1
info:
  title: Bright Data API
  description: >-
    Integrate Bright Data APIs to your pipeline and secure high-end scraping
    precision
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security:
  - bearerAuth: []
paths:
  /zone:
    post:
      description: Add a new zone
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/NewZoneBody'
      responses:
        '201':
          description: Zone added
components:
  schemas:
    NewZoneBody:
      required:
        - zone
        - plan
      type: object
      properties:
        zone:
          $ref: '#/components/schemas/Zone'
        plan:
          $ref: '#/components/schemas/Plan'
    Zone:
      required:
        - name
      type: object
      properties:
        name:
          description: The name of the zone
          type: string
        type:
          description: Zone Type, e.g. serp, isp, mobile, etc.
          type: string
      example:
        name: zone-name
        type: serp
    Plan:
      oneOf:
        - title: SERP API
          description: Creates a SERP API zone for scraping search engine results.
          type: object
          required:
            - type
            - serp
          properties:
            type:
              description: Must be `unblocker` for SERP API zones.
              type: string
              enum:
                - unblocker
            serp:
              description: Must be `true` to create a SERP API zone.
              type: boolean
              enum:
                - true
            country:
              description: >-
                Lowercase ISO 3166-1 alpha-2 country code (e.g. `us`, `gb`,
                `sg`). **Must be lowercase** — uppercase codes will return a
                misleading 'no IPs available' error. Use `any` to allow any
                country.
              type: string
              default: any
            solve_captcha_disable:
              description: When set to `true` it will disable captcha solving.
              type: boolean
              default: true
            custom_headers:
              description: >-
                When set to `true`, allows users to include custom headers in
                their requests.
              type: boolean
              default: false
        - title: Scraping Browser
          description: Creates a Scraping Browser zone.
          type: object
          required:
            - type
          properties:
            type:
              description: Must be `browser_api` for Scraping Browser zones.
              type: string
              enum:
                - browser_api
            country:
              description: >-
                Lowercase ISO 3166-1 alpha-2 country code (e.g. `us`, `gb`,
                `sg`). **Must be lowercase** — uppercase codes will return a
                misleading 'no IPs available' error. Use `any` to allow any
                country.
              type: string
              default: any
            custom_headers:
              description: >-
                When set to `true`, allows users to include custom headers in
                their requests.
              type: boolean
              default: false
        - title: Residential Proxy
          description: Creates a Residential proxy zone.
          type: object
          required:
            - type
          properties:
            type:
              description: Must be `resident` for Residential proxy zones.
              type: string
              enum:
                - resident
            country:
              description: >-
                Lowercase ISO 3166-1 alpha-2 country code (e.g. `us`, `gb`,
                `sg`). **Must be lowercase** — uppercase codes will return a
                misleading 'no IPs available' error. Use `any` to allow any
                country.
              type: string
              default: any
            city:
              description: '`true` when enabling City targeting permission.'
              type: boolean
              default: false
            asn:
              description: '`true` when enabling ASN targeting permission.'
              type: boolean
              default: false
            vip:
              description: '`true` when allocating gIP (group of IPs).'
              type: boolean
              default: false
            vips:
              description: Number of gIP (group of IPs) to allocate to the zone.
              type: integer
              default: 0
            vips_type:
              description: >-
                `shared` for shared (pay-per-usage) Residential. `domain` for
                dedicated gIPs, which require a `domain_whitelist`.
              type: string
              enum:
                - shared
                - domain
            vip_country:
              description: >-
                Lowercase ISO 3166-1 alpha-2 country code for dedicated gIP
                allocation. Only valid with `vips_type: domain`.
              type: string
            vip_country_city:
              description: >-
                Country code followed by city (e.g. `se-stockholm`). Required
                when `vip` is `true` and city targeting is needed.
              type: string
              default: any
            ip_alloc_preset:
              description: To set a zone with Shared - Pay per usage type.
              type: string
              enum:
                - shared_block
                - shared_res_block
            domain_whitelist:
              description: >-
                Space-separated list of target domains. Required when
                `vips_type` is `domain`. Dedicated Residential gIPs are
                exclusive to these domains.
              type: string
            custom_headers:
              description: >-
                When set to `true`, allows users to include custom headers in
                their requests.
              type: boolean
              default: false
        - title: Mobile Proxy
          description: >-
            Creates a Mobile proxy zone. Uses `resident` plan type with `mobile:
            true`.
          type: object
          required:
            - type
            - mobile
          properties:
            type:
              description: Must be `resident` for Mobile proxy zones.
              type: string
              enum:
                - resident
            mobile:
              description: Must be `true` to create a Mobile proxy zone.
              type: boolean
              enum:
                - true
            country:
              description: >-
                Lowercase ISO 3166-1 alpha-2 country code (e.g. `us`, `gb`,
                `sg`). **Must be lowercase** — uppercase codes will return a
                misleading 'no IPs available' error. Use `any` to allow any
                country.
              type: string
              default: any
            city:
              description: '`true` when enabling City targeting permission.'
              type: boolean
              default: false
            vip:
              description: '`true` when allocating gIP (group of IPs).'
              type: boolean
              default: false
            vips:
              description: Number of gIP (group of IPs) to allocate to the zone.
              type: integer
              default: 0
            vips_type:
              description: Type of gIP allocation.
              type: string
              enum:
                - shared
                - domain
            custom_headers:
              description: >-
                When set to `true`, allows users to include custom headers in
                their requests.
              type: boolean
              default: false
        - title: ISP Proxy – Shared (Pay-per-GB)
          description: >-
            Creates a shared ISP proxy zone billed per GB. `pool_ip_type:
            static_res` is required — omitting it silently creates a Datacenter
            zone instead.
          type: object
          required:
            - type
            - pool_ip_type
            - ips_type
            - country
          properties:
            type:
              description: Must be `static` for ISP proxy zones.
              type: string
              enum:
                - static
            pool_ip_type:
              description: >-
                Must be `static_res` to create an ISP proxy zone. Default is
                `dc` (Datacenter).
              type: string
              enum:
                - static_res
            ips_type:
              description: Must be `shared` for this zone type.
              type: string
              enum:
                - shared
            country:
              description: >-
                Lowercase ISO 3166-1 alpha-2 country code (e.g. `us`, `gb`,
                `sg`). **Must be lowercase** — uppercase codes will return a
                misleading 'no IPs available' error. Use `any` to allow any
                country.
              type: string
              default: any
            custom_headers:
              description: >-
                When set to `true`, allows users to include custom headers in
                their requests.
              type: boolean
              default: false
        - title: ISP Proxy – Shared (Unlimited Bandwidth)
          description: >-
            Creates a shared ISP proxy zone with unlimited bandwidth.
            `unl_bw_tiers: std` is required — without it, `bandwidth: unlimited`
            is silently ignored and the zone bills per GB.
          type: object
          required:
            - type
            - pool_ip_type
            - ips_type
            - bandwidth
            - unl_bw_tiers
            - country
          properties:
            type:
              description: Must be `static` for ISP proxy zones.
              type: string
              enum:
                - static
            pool_ip_type:
              description: Must be `static_res` to create an ISP proxy zone.
              type: string
              enum:
                - static_res
            ips_type:
              description: Must be `shared` for this zone type.
              type: string
              enum:
                - shared
            bandwidth:
              description: Must be `unlimited` to enable unlimited bandwidth billing.
              type: string
              enum:
                - unlimited
            unl_bw_tiers:
              description: >-
                **Required** to activate unlimited bandwidth billing. Without
                this field the zone defaults to pay-per-GB even if `bandwidth:
                unlimited` is set.
              type: string
              enum:
                - std
            country:
              description: >-
                Lowercase ISO 3166-1 alpha-2 country code (e.g. `us`, `gb`,
                `sg`). **Must be lowercase** — uppercase codes will return a
                misleading 'no IPs available' error. Use `any` to allow any
                country.
              type: string
              default: any
            custom_headers:
              description: >-
                When set to `true`, allows users to include custom headers in
                their requests.
              type: boolean
              default: false
        - title: ISP Proxy – Dedicated
          description: >-
            Creates a dedicated ISP proxy zone with unlimited bandwidth and a
            fixed number of IPs.
          type: object
          required:
            - type
            - pool_ip_type
            - ips_type
            - bandwidth
            - unl_bw_tiers
            - country
            - ips
          properties:
            type:
              description: Must be `static` for ISP proxy zones.
              type: string
              enum:
                - static
            pool_ip_type:
              description: Must be `static_res` to create an ISP proxy zone.
              type: string
              enum:
                - static_res
            ips_type:
              description: Must be `dedicated` for this zone type.
              type: string
              enum:
                - dedicated
            bandwidth:
              description: Must be `unlimited` for dedicated ISP zones.
              type: string
              enum:
                - unlimited
            unl_bw_tiers:
              description: '**Required** to activate unlimited bandwidth billing.'
              type: string
              enum:
                - std
            country:
              description: >-
                Lowercase ISO 3166-1 alpha-2 country code (e.g. `us`, `gb`,
                `sg`). **Must be lowercase** — uppercase codes will return a
                misleading 'no IPs available' error. Use `any` to allow any
                country.
              type: string
              default: any
            country_city:
              description: >-
                Country code followed by city (e.g. `se-stockholm`) to target a
                specific city.
              type: string
              default: any
            ips:
              description: Number of dedicated IPs to allocate to the zone.
              type: integer
            custom_headers:
              description: >-
                When set to `true`, allows users to include custom headers in
                their requests.
              type: boolean
              default: false
        - title: Datacenter Proxy – Shared
          description: Creates a shared Datacenter proxy zone.
          type: object
          required:
            - type
            - ips_type
          properties:
            type:
              description: Must be `static` for Datacenter proxy zones.
              type: string
              enum:
                - static
            pool_ip_type:
              description: >-
                Set to `dc` for Datacenter (default). Omitting this field also
                defaults to Datacenter.
              type: string
              enum:
                - dc
              default: dc
            ips_type:
              description: Must be `shared` for this zone type.
              type: string
              enum:
                - shared
            country:
              description: >-
                Lowercase ISO 3166-1 alpha-2 country code (e.g. `us`, `gb`,
                `sg`). **Must be lowercase** — uppercase codes will return a
                misleading 'no IPs available' error. Use `any` to allow any
                country.
              type: string
              default: any
            domain_whitelist:
              description: Space separated list of allowlisted domains
              type: string
            custom_headers:
              description: >-
                When set to `true`, allows users to include custom headers in
                their requests.
              type: boolean
              default: false
        - title: Datacenter Proxy – Dedicated
          description: >-
            Creates a dedicated Datacenter proxy zone with a fixed number of
            IPs.
          type: object
          required:
            - type
            - ips_type
            - ips
          properties:
            type:
              description: Must be `static` for Datacenter proxy zones.
              type: string
              enum:
                - static
            pool_ip_type:
              description: Set to `dc` for Datacenter (default).
              type: string
              enum:
                - dc
              default: dc
            ips_type:
              description: Must be `dedicated` for this zone type.
              type: string
              enum:
                - dedicated
            ips:
              description: Number of dedicated IPs to allocate to the zone.
              type: integer
            country:
              description: >-
                Lowercase ISO 3166-1 alpha-2 country code (e.g. `us`, `gb`,
                `sg`). **Must be lowercase** — uppercase codes will return a
                misleading 'no IPs available' error. Use `any` to allow any
                country.
              type: string
              default: any
            country_city:
              description: >-
                Country code followed by city (e.g. `se-stockholm`) to target a
                specific city.
              type: string
              default: any
            domain_whitelist:
              description: Space separated list of allowlisted domains
              type: string
            custom_headers:
              description: >-
                When set to `true`, allows users to include custom headers in
                their requests.
              type: boolean
              default: false
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        Use your Bright Data API Key as a Bearer token in the Authorization
        header.


        **How to authenticate:**

        1. Obtain your API Key from the Bright Data account settings at
        https://brightdata.com/cp/setting/users

        2. Include the API Key in the Authorization header of your requests

        3. Format: `Authorization: Bearer YOUR_API_KEY`


        **Example:**

        ```

        Authorization: Bearer
        b5648e1096c6442f60a6c4bbbe73f8d2234d3d8324554bd6a7ec8f3f251f07df

        ```


        Learn how to get your Bright Data API key:
        https://docs.brightdata.com/api-reference/authentication
      bearerFormat: API Key

````