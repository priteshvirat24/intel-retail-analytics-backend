> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何通过 Bright Data 设置 Entra ID（原 Azure Active Directory）SSO 和配置

* 应用程序准备工作
* 设置 SSO
* 设置 SCIM 配置

## 应用程序准备工作

* 访问 [https://entra.microsoft.com/](https://entra.microsoft.com/) 并登录账户。
* 创建企业应用程序：

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/entra-sso/entra_1.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=0b6841796c55c9bc15a9ab79b3e3c2da" alt="" width="1827" height="928" data-path="images/general/authentication/entra-sso/entra_1.png" />

* 点击“创建自己的应用程序”
* 输入应用程序名称
* 选择“集成其他未在应用库中列出的应用程序（非库应用程序）”
* 点击“创建”

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/entra-sso/entra_2.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=c54195cfb5f04ee5783b13b680a0a3f3" alt="" width="1827" height="929" data-path="images/general/authentication/entra-sso/entra_2.png" />

## 设置 SSO

<Warning>
  **强制启用 Entra SSO 会禁用基于密码的登录。**

  当您的组织强制启用 Entra SSO 后，账户下所有用户的基于密码的登录和密码重置邮件都将被禁用。用户必须通过 Microsoft Entra 登录。

  * 在 Bright Data 登录页面输入邮箱地址后，会自动将用户重定向到 Entra 登录页面。
  * 成功通过 Entra 登录后，用户将被重定向回 Bright Data。
  * 密码重置请求**不会**生成邮件。
</Warning>

* 访问 [https://brightdata.com，并登录账户。](https://brightdata.com，并登录账户。)
* 在左侧菜单中选择“设置”->“账户设置”->“密码和身份验证”，并启用“Microsoft Entra ID (Azure AD) ”

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/entra-sso/entra_3.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=49122c8887f2864721e76cf3417eae6d" alt="" width="1727" height="919" data-path="images/general/authentication/entra-sso/entra_3.png" />

* 从“应用程序注册”视图中选择应用程序。
* 将“应用程序（客户端）ID”复制到“客户端 ID”
* 将“目录（租户）ID”复制到“OAuth2 颁发者（租户）”
* 转到“添加证书或密钥”

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/entra-sso/entra_4.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=34bafc2f22a857fd03ddcffc43b9a6f3" alt="" width="1824" height="930" data-path="images/general/authentication/entra-sso/entra_4.png" />

* 在密钥界面，点击“新建客户端密钥”
* 填写描述信息
* 点击“添加”

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/entra-sso/entra_5.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=6bda5e8c9185fe4c7a4a23a2ba8b2604" alt="" width="1823" height="930" data-path="images/general/authentication/entra-sso/entra_5.png" />

* 创建密钥后，将密钥值复制到“客户端密钥”。
* 复制“登录重定向 URI”，供后续步骤使用

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/entra-sso/entra_6.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=fac7a9990338572c0795e7deb2d9ac96" alt="" width="1828" height="929" data-path="images/general/authentication/entra-sso/entra_6.png" />

* 在“身份验证”界面，点击“添加平台”并选择“Web”

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/entra-sso/entra_7.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=03d219b2b73488b1499be7d1a7903892" alt="" width="1825" height="930" data-path="images/general/authentication/entra-sso/entra_7.png" />

* 将之前复制的“登录重定向 URI”粘贴到“重定向 URI”中，然后点击“配置”以保存设置：

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/entra-sso/entra_8.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=07b000914d880bbf2791e23f23a3bd51" alt="" width="1825" height="930" data-path="images/general/authentication/entra-sso/entra_8.png" />

* 在 BrighData 控制面板中激活 EntraID 集成并测试登录情况：

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/entra-sso/entra_9.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=16e434e6e3156dae471546f30aecb4c3" alt="" width="892" height="916" data-path="images/general/authentication/entra-sso/entra_9.png" />

## 设置 SCIM 配置

* 从 BrightData EntraID 设置的 SCIM 部分复制“身份验证令牌”：

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/entra-sso/entra_10.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=4649683170006ad94dd8aea0825fb30c" alt="" width="671" height="878" data-path="images/general/authentication/entra-sso/entra_10.png" />

* 从“企业应用程序”视图中选择应用程序并转到“配置”设置：

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/entra-sso/entra_11.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=22303e8f6bc9b20e268377e8ed180c6e" alt="" width="1559" height="930" data-path="images/general/authentication/entra-sso/entra_11.png" />

* 在“管理”菜单下选择“配置”：

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/entra-sso/entra_12.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=51632271bbd37f64e274b5ae9e4786d5" alt="" width="1557" height="931" data-path="images/general/authentication/entra-sso/entra_12.png" />

* 选择“自动”配置模式
* 在“租户 URL”中填入“[https://www.bright.cn/users/auth/scim”](https://www.bright.cn/users/auth/scim”)
* 在“密钥令牌”中填入之前从 BrightData 控制面板设置中复制的值
* 测试连接状态。 右上角应会显示成功提示
  保存设置

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/entra-sso/entra_13.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=f88b5c584438faf81a75cbf2a3b2aa95" alt="" width="1823" height="931" data-path="images/general/authentication/entra-sso/entra_13.png" />

* 返回“概述”选项卡，点击“开始配置”。
* 您可以在“按需配置”页面测试配置，但需要先在“用户和群组”页面为 BrightData 应用程序分配用户：

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/entra-sso/entra_14.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=3566b35a83bf0411537b82c099b04498" alt="" width="1825" height="930" data-path="images/general/authentication/entra-sso/entra_14.png" />

## 故障排除

<AccordionGroup>
  <Accordion title="用户收不到密码重置邮件，应该怎么办？">
    如果您的组织已**强制启用 Entra SSO**，则不会发送密码重置邮件，因为在强制启用 SSO 的账户上，基于密码的身份验证已被禁用。

    登录方法：

    1. 访问 [Bright Data 登录页面](https://brightdata.com/cp)。
    2. 输入用户的邮箱地址。
    3. 系统会自动将用户重定向到 Microsoft Entra 登录页面。
    4. 成功通过 Entra 登录后，用户将被重定向回 Bright Data。

    如果访问问题仍然存在，请联系您组织的 IT / Entra 管理员。他们负责管理您公司一侧的 Entra SSO 配置。
  </Accordion>

  <Accordion title="为什么用户会被重定向到一个无法识别的 Microsoft 登录页面？">
    当强制启用 Entra SSO 时，这是预期行为。Bright Data 登录页面会检测与您组织 Entra 租户关联的邮箱域名，并将用户重定向到您配置的 Microsoft Entra 登录页面。
  </Accordion>
</AccordionGroup>
