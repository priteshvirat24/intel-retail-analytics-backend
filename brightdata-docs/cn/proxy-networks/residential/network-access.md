> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 住宅网络访问政策

> Bright Data 住宅代理需经合规团队人工审核 KYC，仅向已验证的企业开放，没有自动或即时访问。

Bright Data 住宅代理仅向通过 Bright Data 合规团队人工审核 KYC（了解您的客户）的已验证企业开放。不存在任何自动、即时或自助的住宅网络访问方式。

<Note>
  **现有区域不受影响。** 2026 年 7 月 7 日（含）之前创建的住宅区域将照常工作。KYC 要求仅适用于 2026 年 7 月 7 日之后创建的新住宅区域。已通过住宅访问验证的客户将保留其访问权限，一切照旧。
</Note>

## 谁可以访问住宅网络？

住宅访问仅授予已注册的企业，且必须在 Bright Data 合规团队审核并批准您的 KYC 提交之后。

* **仅限已验证企业。** 您必须以已注册公司的名义注册，并验证公司邮箱域名。使用个人邮箱（例如 Gmail 或 Outlook）的账户无法获得住宅访问权限。
* **人工审核 KYC。** 每一项住宅申请都由 Bright Data 合规团队人工审核，绝不会自动、即时或自助批准。
* **适用于所有住宅代理类型。** 对于 2026 年 7 月 7 日之后创建的新住宅区域，每种代理类型都需要 KYC 批准：共享轮换 IPv4、IPv4 与 IPv6 "Mega Pool"、IPv6 以及专用住宅代理。
* **现有区域继续工作。** 2026 年 7 月 7 日（含）之前创建的住宅区域一切照旧。KYC 要求仅适用于 2026 年 7 月 7 日之后创建的新住宅区域，已通过住宅访问验证的客户无需重新申请。

<Warning>
  数据中心和 ISP 网络上也存在部分限制。例如，所有网络均阻止访问政府网站。具体错误请参见[代理错误目录](/cn/proxy-networks/errorCatalog)。
</Warning>

## 无需 KYC 可以使用什么？

如果您尚未完成 KYC，或您的使用案例不需要住宅 IP，可以使用以下替代方案，它们均无需 KYC：

* **[ISP 代理](/cn/proxy-networks/isp/introduction)**：提供静态、以住宅名义注册的 IP，具备数据中心的速度与稳定性，适用于广告验证、质量保证和长会话工作负载。
* **[数据中心代理](/cn/proxy-networks/data-center/introduction)**：提供快速、低成本的共享或专用 IP，适用于对反爬防护要求不高的网站的高并发请求。
* **[Web Unlocker API](/cn/scraping-automation/web-unlocker/introduction)**：全托管的解锁产品，自动处理请求头、Cookie、验证码和重试，按成功请求计费。

这些是住宅代理的替代方案，并非受限或试用版的住宅模式。

<span id="residential-proxy-network-policy" />

## 住宅代理网络政策

Bright Data 全天候 24/7 监控住宅网络流量，以确保网络符合其[可接受使用政策](https://www.bright.cn/acceptable-use-policy)。由于住宅 IP 来自主动选择加入的真实用户，访问权限仅限于合规团队在 KYC 中批准的使用案例。

* 对超出您已批准使用案例的域名或类别的请求将被阻止，并返回带有分类类别的 `Access denied` 错误。
* 不属于您已批准使用案例的受限 HTTP 方法和目标同样会被阻止。
* 如需扩大可定位的网站和方法范围，请与合规团队及时更新您的 KYC 使用案例。

<span id="kyc-verification" />

## KYC 验证

KYC（了解您的客户）是住宅网络访问的强制性人工审核验证步骤。Bright Data 合规团队在授予访问权限前会验证您的公司和使用案例。由于每一项提交都由人工审核，访问权限绝不会即时授予。

### 如何申请住宅访问

1. 登录您的 Bright Data 账户，并添加一个使用**公司邮箱域名**的用户。KYC 申请仅接受来自已注册企业的提交。

2. 向账户余额添加资金。[Playground](/cn/general/faqs#what-is-playground-mode) 或 [Limited Trial](/cn/general/faqs#what-is-limited-trial-mode) 模式下无法进行 KYC。

3. 提交 KYC 表单，附上关于您业务和采集使用案例的详细信息以及公司注册文件。

   [开始 KYC 验证](https://www.bright.cn/cp/kyc)

4. Bright Data 合规团队审核您的提交。您将通过邮件收到审核结果，并可在控制面板的**账户设置 > 个人资料**中查看状态。

<AccordionGroup>
  <Accordion title="为什么住宅代理需要 KYC？">
    住宅 IP 地址与 100% 主动选择加入 Bright Data 网络的真实用户相关联。KYC（了解您的客户）让 Bright Data 合规团队在您通过这些真实节点转发流量之前验证您的业务和使用案例。这使网络符合最高的伦理与合规标准，并保护 IP 背后的用户。住宅访问仅在此人工审核之后授予，因此没有自动或即时批准。
  </Accordion>

  <Accordion title="我用个人邮箱注册，能使用住宅代理吗？">
    不能。住宅代理仅向已验证企业开放。KYC 申请仅接受来自拥有公司邮箱域名的已注册企业，因此个人邮箱账户（例如 Gmail、Outlook 或 iCloud）无法获批住宅访问。请添加一个使用公司邮箱域名的用户，然后提交 KYC。在没有 KYC 的情况下，您仍可使用 [ISP 代理](/cn/proxy-networks/isp/introduction)、[数据中心代理](/cn/proxy-networks/data-center/introduction) 和 [Web Unlocker API](/cn/scraping-automation/web-unlocker/introduction)。
  </Accordion>

  <Accordion title="可以把现有的 ISP 或数据中心区域切换为住宅吗？">
    仅在 KYC 批准之后。在 Bright Data 合规团队批准您的 KYC 提交之前，创建或转换住宅区域将被阻止。在 KYC 审核期间，您现有的 ISP 和数据中心区域照常工作。
  </Accordion>

  <Accordion title="KYC 验证流程是怎样的？">
    提交有关您本人及采集使用案例的详细信息，以便 Bright Data 合规团队验证您的资格。开始 KYC 流程：

    [开始 KYC 验证](https://www.bright.cn/cp/kyc)

    <Warning>
      在 [Playground](/cn/general/faqs#what-is-playground-mode)/[Limited Trial](/cn/general/faqs#what-is-limited-trial-mode) 模式下无法进行 KYC。该流程仅在账户余额添加真实资金后可开始。
    </Warning>
  </Accordion>

  <Accordion title="KYC 审核需要多久？" defaultOpen="false">
    填写表单只需几分钟。批准不是自动的：Bright Data 合规团队会审核每一项提交。提交后，审核将进入合规流程，您可在控制面板的**账户设置 > 个人资料**中查看状态。我们会在您完成流程后的 48 小时内更新您的 KYC 状态。
  </Accordion>

  <Accordion title="如何知道我的 KYC 已批准？" defaultOpen="false">
    您可随时在控制面板的**设置 > 个人资料**中查看 KYC 状态，显示为"账户验证状态"。审核完成后，关于提交及批准或拒绝的通知也会发送到您的邮箱。
  </Accordion>

  <Accordion title="必须完成 KYC 才能使用住宅网络吗？">
    是的。所有住宅网络访问都需要 KYC 批准，并由 Bright Data 合规团队审核。不存在任何自动或无需 KYC 的住宅代理访问方式。在没有 KYC 的情况下，请使用 [ISP 代理](/cn/proxy-networks/isp/introduction)、[数据中心代理](/cn/proxy-networks/data-center/introduction) 或 [Web Unlocker API](/cn/scraping-automation/web-unlocker/introduction)。
  </Accordion>

  <Accordion title="这是一次性流程吗？">
    KYC 信息记录在 Bright Data 系统中，以便合规团队在未来需要时再次审查您的使用案例。Bright Data 全天候 24/7 监控网络，必要时可能会联系您以获取额外的澄清或信息，从而确保网络安全。
  </Accordion>

  <Accordion title="谁有资格进行 KYC 流程？">
    Bright Data 接受来自拥有公司域名的已注册企业的 KYC 申请。要提交 KYC 请求，请在账户上验证一个公司邮箱地址。
  </Accordion>

  <Accordion title="我需要提供哪些信息？">
    KYC 流程需要一些关于您业务的基本信息，例如使用案例描述和一般联系方式。您分享的业务和使用案例信息越详细，Bright Data 合规与伦理团队就越容易评估并批准您的请求。如有需要，我们会跟进要求进一步澄清、验证或身份确认。
  </Accordion>

  <Accordion title="为什么可能需要我提供身份证明？">
    作为验证的一部分，Bright Data 合规团队可能要求提供有效的政府颁发身份证件（如驾照或护照）以验证联系人身份。由于 Bright Data 的 IP 地址与 100% 真实节点相关联，验证身份是保持网络安全可靠的重要环节。
  </Accordion>

  <Accordion title="需要安排视频通话吗？">
    Bright Data 合规团队可能要求进行简短的视频通话，以验证有关您业务或预期使用案例的额外信息。此步骤确保审核过程符合政策与伦理标准。
  </Accordion>

  <Accordion title="什么是公司注册表或公司注册证书？">
    公司注册表（也称"注册证书"）由政府部门用于证明新企业的注册。它通常包含公司的正式信息，包括公司名称、注册办公地址和公司注册标识符。它通常可供公司法律顾问或财务部门使用，并可作为注册证明进行分享。
  </Accordion>

  <Accordion title="KYC 审核期间可以使用 Bright Data 服务吗？">
    可以。在您的 KYC 请求审核期间，您可使用所有其他 Bright Data 产品和服务，包括 [ISP 代理](/cn/proxy-networks/isp/introduction)、[数据中心代理](/cn/proxy-networks/data-center/introduction) 和 [Web Unlocker API](/cn/scraping-automation/web-unlocker/introduction)。
  </Accordion>

  <Accordion title="如果住宅 KYC 被拒，还能使用数据中心和 ISP 吗？">
    可以。如果您的 KYC 未通过，您仍可根据 Bright Data [许可协议](https://www.bright.cn/license) 使用其他 Bright Data 产品和服务。
  </Accordion>

  <Accordion title="KYC 视频通话会涉及什么？">
    在通话中，Bright Data 合规团队会进一步了解您的公司和业务活动，确认您的使用案例和具体需求，并可能查看相关系统和工作流程，以便 Bright Data 尽可能准确地支持您的需求。
  </Accordion>

  <Accordion title="如果我没有 LinkedIn 或网站怎么办？">
    验证流程需要审查公司网站和活跃的在线存在。如果您除 LinkedIn 外还有其他形式的在线存在（例如作品集、GitHub 或其他业务资料），请在提交申请时一并分享。
  </Accordion>

  <Accordion title="如果我不想进行视频通话怎么办？">
    如果您被要求进行视频通话，这是强制性步骤。它帮助 Bright Data 合规团队验证您的身份并理解您的使用案例。不完成通话，将无法授予住宅网络访问权限。
  </Accordion>

  <Accordion title="可以将 Bright Data 用于个人项目吗？">
    不可以。Bright Data 是 B2B 平台，仅支持与业务相关的使用案例。个人项目（如出于兴趣或副业的采集）不会获批。
  </Accordion>

  <Accordion title="哪些使用案例是不允许的？">
    请参见 Bright Data [可接受使用政策](https://www.bright.cn/acceptable-use-policy)。
  </Accordion>

  <Accordion title="我提交了 KYC 但没有收到回复，该怎么办？">
    请在提交 KYC 后 48 小时内等待更新。如果超过此时间，请在控制面板的**账户设置 > 个人资料**中查看状态，或联系您的客户经理或 Bright Data 支持团队。
  </Accordion>
</AccordionGroup>
