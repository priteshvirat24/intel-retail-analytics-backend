> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 安全与合规

> ISO 27001、SOC 2、渗透测试、加密标准和合规态势 - 独立验证。

<Note>
  三项ISO认证均明确范围为\*"为高规模采集、自动化和AI代理/RAG系统进行网络数据访问而设计的公共网络数据收集平台"\*。这直接涵盖了Bright Data的MCP Server、Browser API和所有代理工作流中的API使用。
</Note>

## 认证一览

<CardGroup cols={3}>
  <Card title="ISO/IEC 27001:2022" icon="certificate" color="#4180f9">
    信息安全管理体系 (ISMS)
    **有效期至：** 2028年8月11日
    **编号：** 1126059 - SII–QCD (ANAB认可)
  </Card>

  <Card title="ISO/IEC 27017:2015" icon="cloud" color="#4180f9">
    云安全控制
    **有效期至：** 2028年7月13日
    **编号：** 1125290 - SII–QCD
  </Card>

  <Card title="ISO/IEC 27018:2019" icon="user-shield" color="#4180f9">
    公有云中个人身份信息的保护
    **有效期至：** 2028年7月13日
    **编号：** 1125291 - SII–QCD
  </Card>

  <Card title="SOC 2 Type II" icon="file-shield" color="#22c55e">
    可根据保密协议获取
    **期间：** 2024年6月1日 – 2025年5月31日
    德勤全球网络审计
  </Card>

  <Card title="SOC 3" icon="file-check" color="#22c55e">
    公开下载
    **期间：** 2024年6月1日 – 2025年5月31日
    Brightman Almagor Zohar & Co. 审计
  </Card>

  <Card title="CSA STAR" icon="star" color="#f59e0b">
    云安全联盟注册表
    [查看列表 →](https://cloudsecurityalliance.org/star/registry/bright-data/)
  </Card>
</CardGroup>

***

## 独立审计

### SOC 3 报告 - 德勤

由**Bright Data Global Network中的德勤集团子公司Brightman Almagor Zohar & Co.**进行，涵盖**2024年6月1日 – 2025年5月31日**。

审计检查了四个信任服务标准的控制措施：

<CardGroup cols={2}>
  <Card title="安全" icon="lock">
    保护系统和数据免受未授权访问
  </Card>

  <Card title="可用性" icon="signal">
    运行时间承诺和灾难恢复就绪状态
  </Card>

  <Card title="机密性" icon="eye-slash">
    数据分类、加密和访问控制
  </Card>

  <Card title="隐私" icon="user-lock">
    GDPR/CCPA合规和个人身份信息处理程序
  </Card>
</CardGroup>

> *"根据我们的意见，管理层关于服务机构系统内的控制措施有效的声明...根据适用的信任服务标准为Bright Data的服务承诺和系统要求的实现提供合理保证，在所有重要方面均是恰当的。"*
>
> * Brightman Almagor Zohar & Co. (德勤全球网络)

<Card title="下载 SOC 3 报告 (PDF)" icon="download" href="https://www.bright.cn/static/Bright_Data_SOC_3_June_1_2024_May_31_2025_Updated.pdf" cta="下载">
  涵盖2024年6月1日 – 2025年5月31日的完整SOC 3报告
</Card>

***

### 渗透测试 - Skylight网络安全

**Skylight Cyber Security Pty Ltd**进行了独立渗透测试和源代码审查(2025年5月–6月)，涵盖完整的Bright Data产品。

**测试的产品：**

| 产品                          | 覆盖范围 |
| --------------------------- | ---- |
| 控制面板和公开API                  | 完整   |
| 数据中心、住宅、移动和ISP代理            | 完整   |
| SERP API 和 Web Unlocker API | 完整   |
| Web Scraper IDE、市场和API      | 完整   |
| Web Archive API             | 完整   |
| 数据集市场和自定义数据集API             | 完整   |

**三个威胁场景在范围内：**

1. 未认证攻击者试图攻击整个平台
2. 恶意管理员试图进行内部攻击
3. 未授权账户访问或代理滥用

<Info>
  **结果：** 所有严重和高危发现已修复。Skylight重新测试以确认问题已解决且风险已缓解。
</Info>

<Card title="下载渗透测试证明" icon="file-shield" href="https://www.bright.cn/trustcenter" cta="访问信任中心">
  Skylight Cyber Security Pty Ltd出具的证明信
</Card>

***

## 数据加密

| 层级        | 标准                         |
| --------- | -------------------------- |
| **数据传输中** | TLS 1.3（最低TLS 1.2）配合现代密码套件 |
| **数据静态**  | 整个基础设施中使用AES-256或更强加密      |
| **凭证**    | 使用现代哈希函数进行哈希和加盐            |
| **数据库备份** | 加密；每日完整备份，每月快照             |
| **备份存储**  | AWS Backup；快照分布在多个位置       |

***

## 基础设施与可用性

<CardGroup cols={2}>
  <Card title="云服务商" icon="aws">
    亚马逊网络服务 (AWS)，多可用区部署
  </Card>

  <Card title="灾难恢复" icon="rotate">
    AWS欧盟灾难恢复站点；年度大规模灾难恢复演习；所有高严重级别事件的根本原因分析
  </Card>

  <Card title="备份频率" icon="database">
    每5分钟进行一次完整数据库备份；每日AWS快照；关键备份在Microsoft Azure上
  </Card>

  <Card title="DDoS与监控" icon="shield">
    主动DDoS缓解和速率限制；由专门信息安全团队进行持续防火墙监控
  </Card>
</CardGroup>

***

## 访问控制与身份

| 控制措施      | 实施方式                  |
| --------- | --------------------- |
| **最小权限**  | 所有IAM角色限制为最少必需权��     |
| **MFA**   | 所有员工访问AWS平台都需要MFA     |
| **客户认证**  | 强密码（最少8个字符）+ 电子邮件验证   |
| **RBAC**  | 基于角色的访问控制，定期进行用户访问审查  |
| **第三方访问** | 年度重新授权；需要签署NDA和信息安全批准 |
| **远程访问**  | VPN加密必需；强制执行主机检查      |

***

## 应用与开发安全

* **CI/CD流水线** - 受控流水线，包含端到端和单元测试，包括授权测试
* **安全SDLC** - 基于OWASP Top 10框架；在开发开始前定义安全需求；年度开发人员安全培训
* **变更管理** - 对所有基础设施和应用程序变更的正式审查和批准流程，包括在R\&D审查阶段的安全风险评估
* **第三方风险 (TPRM)** - 所有供应商根据风险等级进行映射和分类；高风险供应商在合同前需要安全问卷和信息安全签字
* **漏洞赏金** - 由独立安全研究人员管理的负责任披露私有计划

***

## 隐私与法规合规

| 法规/标准           | 状态                      |
| --------------- | ----------------------- |
| GDPR (欧盟)       | ✅ 合规 - 作为产品流程的一部分进行DPIA |
| CCPA (加州)       | ✅ 合规                    |
| 英国数据保护法         | ✅ 合规                    |
| 弗吉尼亚隐私法         | ✅ 合规                    |
| 以色列隐私保护法 (1981) | ✅ 合规                    |
| ISO 27001:2022  | ✅ 认证                    |
| CSA STAR        | ✅ 已��出                  |
| PCI DSS         | ✅ 在合规中                  |

* **隐私政策**每年审查和更新 - [brightdata.com/privacy](https://www.bright.cn/privacy)
* **客户数据删除**可根据请求随时获得
* **数据销售** - Bright Data不会向任何第三方出售或许可客户数据

***

## 信息安全策略

Bright Data维护一份正式的、经董事会批准的信息安全策略，符合**NIST、ISO 27001:2022、ISO 27017和ISO 27018**。

<AccordionGroup>
  <Accordion title="身份与访问管理">
    IAM策略在所有系统中强制执行最小权限访问，定期进行审计和年度审查。
  </Accordion>

  <Accordion title="网络与加密">
    网络分段、传输中的TLS 1.3、静态时的AES-256和整个系统的现代密码套件。
  </Accordion>

  <Accordion title="端点与服务器加固">
    对所有端点和服务器应用CIS基准。
  </Accordion>

  <Accordion title="安全SDLC">
    在开发前定义安全需求；OWASP Top 10框架；年度开发人员培训。
  </Accordion>

  <Accordion title="第三方与供应商安全">
    所有供应商按风险等级分类；高风险供应商需要安全问卷和信息安全签字。
  </Accordion>

  <Accordion title="数据分类">
    三层分类：敏感、个人身份信息和公开 - 根据等级应用控制措施。
  </Accordion>

  <Accordion title="事件响应与业务连续性">
    事件报告、高严重级别事件的根本原因分析、年度灾难恢复演习和正式的业务连续性计划。
  </Accordion>
</AccordionGroup>

***

## AI代理和MCP用户的安全

Bright Data的MCP Server和Browser API在本页面描述的同一认证安全基础设施下运行。

<Warning>
  始终将抓取的网络内容视为**不可信输入**。在将数据传递给LLM提示前进行验证和过滤，以缓解提示注入风险。
</Warning>

**在代理工作流中使用Bright Data时的推荐做法：**

<Steps>
  <Step title="将网络内容视为不可信">
    在将网络数据传递给LLM提示前进行验证和过滤 - 这可以缓解提示注入攻击。
  </Step>

  <Step title="使用结构化提取工具">
    优先使用可用的`web_data_*`工具 - 它们返回预验证、架构一致的数据。
  </Step>

  <Step title="安全地存储凭证">
    将API令牌存储为环境变量。切勿在代理代码或提示中硬编码凭证。
  </Step>

  <Step title="限定API密钥权限范围">
    使用API密钥权限范围限定（有5个级别可用）从您的代理强制执行最小权限访问。
  </Step>
</Steps>

***

## 认证与报告

<CardGroup cols={2}>
  <Card title="ISO 27001 + 27017 + 27018 证书" icon="certificate" href="https://www.bright.cn/static/ISO-270012022_ISO-27017_ISO-27018.pdf" cta="下载 PDF">
    单个PDF中的所有三个ISO证书
  </Card>

  <Card title="SOC 3 报告" icon="file-check" href="https://www.bright.cn/static/Bright_Data_SOC_3_June_1_2024_May_31_2025_Updated.pdf" cta="下载 PDF">
    公开SOC 3 - 2024年6月1日 – 2025年5月31日
  </Card>

  <Card title="SOC 2 Type II 报告" icon="file-shield" href="mailto:security@brightdata.com" cta="通过电子邮件请求">
    根据NDA提供
  </Card>

  <Card title="信任中心" icon="shield-check" href="https://www.bright.cn/trustcenter" cta="访问">
    渗透测试证明和实时信任文档
  </Card>

  <Card title="隐私政策" icon="user-shield" href="https://www.bright.cn/privacy" cta="阅读">
    每年更新；符合GDPR和CCPA
  </Card>

  <Card title="安全漏洞奖励计划" icon="bug" href="https://www.bright.cn/security-vulnerabilities-reward-program" cta="查看">
    安全研究人员的负责任披露计划
  </Card>
</CardGroup>

***

## 常见问题

<AccordionGroup>
  <Accordion title="Bright Data是否通过了ISO 27001认证？">
    是的。Bright Data拥有**ISO/IEC 27001:2022、ISO 27017和ISO 27018**认证，有效期至2028年8月11日至13日，由SII–QCD (ANAB认可、IAF和IQNET成员)颁发。
  </Accordion>

  <Accordion title="Bright Data是否有SOC 2报告？">
    是的。Bright Data有**SOC 2 Type II**报告可根据NDA获取，以及由德勤集团(Brightman Almagor Zohar & Co.)审计的公开下载**SOC 3**报告。
  </Accordion>

  <Accordion title="Bright Data是否符合GDPR？">
    是的。Bright Data已进行全面的GDPR和CCPA合规计划，作为所有产品流程的一部分进行数据隐私影响评估(DPIA)，并维护每年更新的公开隐私政策。
  </Accordion>

  <Accordion title="Bright Data是否进行渗透测试？">
    是的。由独立第三方安全公司进行年度渗透测试和源代码审查。最近的测试(Skylight网络安全，2025年5月-6月)没有留下未解决的严重或高危发现。
  </Accordion>

  <Accordion title="Bright Data的基础设施是否加密？">
    是的。所有数据在传输中加密(**TLS 1.3**)和静态时加密(**AES-256**)。数据库备份已加密并分布在多个云位置。
  </Accordion>

  <Accordion title="Bright Data是否适合企业部署？">
    是的。Bright Data被财富500强公司、学术机构和全球50,000多个组织信任。其安全态势通过ISO 27001/27017/27018认证和年度德勤SOC 2 Type II审计独立验证。
  </Accordion>

  <Accordion title="Bright Data的MCP Server是否受这些认证覆盖？">
    是的。所有ISO认证都明确范围为包含AI代理和RAG系统用例的网络数据访问，这涵盖了MCP Server、Browser API和相关产品。
  </Accordion>
</AccordionGroup>

***

*安全咨询：[security@brightdata.com](mailto:security@brightdata.com)*
*企业合规审查：[联系销售](https://www.bright.cn/contact)*
