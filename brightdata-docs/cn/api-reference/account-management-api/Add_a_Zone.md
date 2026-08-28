> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 添加区域

> 使用 Bright Data 账户管理 API 添加区域。POST /zone 返回 200 OK，并以 JSON 形式返回区域或账户配置数据。

<Warning>只有拥有 **Admin** 或 **Ops** 角色的用户才能执行此操作。</Warning>

<Warning>此 API 可能会修改你的账户设置、损害你的运营或产生费用。</Warning>

<Tip>
  将你的 API key 粘贴到授权字段中。要获取 API key，请[创建账户](https://brightdata.com/?hs_signup=1\&utm_source=docs\&utm_campaign=playground)，并了解[如何生成新的 API key](/cn/api-reference/authentication#how-do-i-generate-a-new-api-key%3F)
</Tip>

## ISP 代理区域示例

创建 ISP 区域需要特定的参数组合。以下字段不是可选的。省略它们会在不报错的情况下创建错误的区域类型或计费方案。

<Warning>
  仅将 `zone.type` 设置为 `ISP` 会创建一个 **Datacenter 区域**，而不是 ISP 区域。你还必须将 `plan.pool_ip_type` 设置为 `static_res`。国家/地区代码必须为**小写**（例如 `us`、`gb`）。大写代码会返回一个具有误导性的 "no IPs available" 错误。
</Warning>

### 共享 ISP（按 GB 计费）

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

### 共享 ISP（无限带宽）

仅设置 `bandwidth: unlimited` **不会**激活无限计费。你还必须包含 `unl_bw_tiers: std`。

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

### 专用 ISP（无限带宽）

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

## Residential 代理区域

<Warning>
  **新的 Residential 区域需要通过 KYC 审核。** 对于 2026 年 7 月 7 日之后创建的 Residential 区域，仅允许已通过 KYC 验证的公司添加区域。来自尚未完成 KYC 的账户的请求将被阻止，并返回 HTTP 403 及合规错误。2026 年 7 月 7 日（含）之前创建的 Residential 区域不受影响，可继续正常使用。请从 [KYC 验证](https://brightdata.com/cp/kyc)开始，并参阅 [Residential 网络访问策略](/cn/proxy-networks/residential/network-access)。
</Warning>

在 2026 年 7 月 7 日之后创建任何 Residential 代理类型（共享轮换、IPv6 或专用）都需要 Bright Data 合规团队的 KYC 审核。对于这些新区域，没有自动或免 KYC 的途径。若未通过 KYC，请改为创建 [ISP](/cn/proxy-networks/isp/introduction) 或 [Datacenter](/cn/proxy-networks/data-center/introduction) 区域。

### Residential 403 合规错误

对于 2026 年 7 月 7 日之后创建的 Residential 区域，来自不符合条件账户的添加区域请求将返回 HTTP 403 及以下合规错误之一。2026 年 7 月 7 日（含）之前创建的区域不受影响。完整目录请参阅[代理错误目录](/cn/proxy-networks/errorCatalog#http-error-403)。

| 错误代码                        | 触发条件                 | 如何修复                                                                     |
| :-------------------------- | :------------------- | :----------------------------------------------------------------------- |
| `kyc_required`              | 使用公司邮箱但尚未完成 KYC 的账户。 | 开始 [KYC 验证](https://brightdata.com/cp/kyc)。由人工合规审核人员审批 Residential 访问权限。 |
| `business_account_required` | 使用个人邮箱的账户（非已验证公司）。   | 使用公司邮箱并联系 Bright Data 团队以确认企业资格。个人邮箱账户不具备 Residential 资格。                |

每个错误都会返回结构化的 JSON 响应体，便于集成程序根据稳定的 `code` 值进行分支处理。使用公司邮箱但未完成 KYC 的账户会收到 `kyc_required`：

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

使用个人邮箱的账户会收到 `business_account_required`，该错误不提供 KYC，因为个人账户不具备资格：

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

两个响应体都包含一个 `alternatives` 数组，其中给出了用于改为创建免 KYC 的 [ISP](/cn/proxy-networks/isp/introduction) 或 [Web Unlocker API](/cn/scraping-automation/web-unlocker/introduction) 区域的确切 `plan` 对象。要创建该 ISP 区域，请在 `POST /zone` 请求中用该 `plan` 对象替换 Residential 的 `plan`。


## OpenAPI

````yaml cn-openapi POST /zone
openapi: 3.0.1
info:
  title: Bright Data API
  description: 将 Bright Data API 集成到您的流程中，以实现高端的爬取精度
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security:
  - bearerAuth: []
paths:
  /zone:
    post:
      description: 添加新区域
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/NewZoneBody'
      responses:
        '201':
          description: 区域已添加
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
          description: 区域的名称
          type: string
        type:
          description: 区域类型，例如 serp、isp、mobile 等
          type: string
      example:
        name: zone-name
        type: serp
    Plan:
      required:
        - type
      type: object
      properties:
        type:
          description: 区域类型
          type: string
          enum:
            - static
            - resident
            - unblocker
            - browser_api
        domain_whitelist:
          description: 允许列表域名的空格分隔列表
          type: string
        ips_type:
          description: '`domain_whitelist` 为 `selective` 时必须提供'
          type: string
          enum:
            - shared
            - dedicated
            - selective
        bandwidth:
          description: '`bandwidth`: 对于 `unlimited`，启用无限带宽'
          type: string
          enum:
            - bandwidth
            - unlimited
        ip_alloc_preset:
          description: 设置为共享 - 按使用付费类型的区域
          type: string
          enum:
            - shared_block
            - shared_res_block
        ips:
          description: 分配给该区域的静态 IP 数量
          type: integer
          default: 0
        country:
          description: 指定要分配给区域的国家 IP，当 `ips_type=static` 时使用
          type: string
          default: any
        country_city:
          description: 国家代码加城市 (例如 “se-stockholm”) - 指定分配给区域的城市 IP，当 `ips_type=static` 时使用
          type: string
          default: any
        mobile:
          description: 添加移动代理区域时为 `true`，类型必须为 `resident`
          type: boolean
          default: 'false'
        serp:
          description: 添加 SERP API 区域时为 `true`
          type: boolean
          default: 'false'
        city:
          description: 启用城市定位权限时为 `true`
          type: boolean
          default: 'false'
        asn:
          description: 启用 ASN 定位权限时为 `true`
          type: boolean
          default: 'false'
        vip:
          description: 分配 `gIP`（IP 组）时为 `true`
          type: boolean
          default: 'false'
        vips_type:
          description: 添加 Residential 或 Mobile 区域时指定此参数
          type: string
          enum:
            - shared
            - domain
        vips:
          description: 分配给区域的 `gIP`（IP 组）数量
          type: integer
          default: '0'
        vip_country:
          description: 指定分配给区域的国家 IP，当 `ips_type=resident` 且 `vip=true` 时使用
          type: string
        vip_country_city:
          description: >-
            国家代码加城市 (例如 “se-stockholm”) - 指定分配给区域的城市 IP，当 `ips_type=resident` 且
            `vip=true` 时使用
          type: string
          default: any
        pool_ip_type:
          description: 当 `pool_ip_type` 设置为 `static_res` 时，区域将使用 ISP IP 而非数据中心 IP。
          type: string
        ub_premium:
          description: 设置为 `true` 时可访问高级域名
          type: boolean
          default: false
        solve_captcha_disable:
          description: 设置为 `true` 时将禁用验证码解决功能
          type: boolean
          default: true
        custom_headers:
          description: 设置为 `true` 时，允许用户在请求中包含自定义头
          type: boolean
          default: false
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        在 Authorization 头中使用您的 Bright Data API Key 作为 Bearer token。


        **认证方法:**

        1. 从 Bright Data 账户设置获取您的 API Key:
        https://brightdata.com/cp/setting/users

        2. 在请求的 Authorization 头中包含 API Key

        3. 格式: `Authorization: Bearer YOUR_API_KEY`


        **示例:**

        ```

        Authorization: Bearer
        b5648e1096c6442f60a6c4bbbe73f8d2234d3d8324554bd6a7ec8f3f251f07df

        ```


        了解如何获取 Bright Data API Key:
        https://docs.brightdata.com/cn/api-reference/authentication#如何生成新的-api-key？
      bearerFormat: API Key

````