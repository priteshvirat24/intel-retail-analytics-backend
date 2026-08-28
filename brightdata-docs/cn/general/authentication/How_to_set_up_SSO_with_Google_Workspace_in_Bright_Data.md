> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 Bright Data 中设置 Google Workspace SSO？

> 在 Google Cloud Console 中创建 OAuth 客户端 ID，为 Bright Data 配置 Google Workspace OIDC SSO；采用手动用户预置并通过 hd 声明强制校验托管域。

本指南说明如何使用 OIDC 为 Bright Data 配置 Google Workspace SSO：在 Google Cloud Console 中创建 OAuth 客户端 ID，并在 Bright Data 控制面板中手动预置用户。

<Note>
  Bright Data 的 Google Workspace SSO 在 **Google Cloud Console** (`console.cloud.google.com`) 中配置，而不是在 Google Workspace 管理控制台中配置。该功能与公共的 **使用 Google 账号继续** 登录按钮是两个完全独立的功能。
</Note>

**要求**

* 与您的 Google Workspace 组织关联的 Google Cloud 项目，且具有配置 OAuth 同意屏幕与创建 OAuth 客户端 ID 的权限（通常为项目所有者或编辑者）
* 具有管理员权限的 Bright Data 账户
* 所有需要通过 SSO 登录的 Bright Data 用户必须事先在 Bright Data 控制面板的 **账户设置 → 用户** 中存在。Bright Data 的 Google Workspace SSO 采用手动预置，不支持 SCIM 或 JIT 预置。

<Warning>
  **强制启用 Google Workspace SSO 会禁用基于密码的登录。**

  当您的组织强制启用 Google Workspace SSO 后，账户下所有用户的基于密码的登录和密码重置邮件都将被禁用。用户必须通过 Google 登录。如果出现访问问题，请联系您的 IT / Workspace 管理员。
</Warning>

## 配置 OAuth 同意屏幕

1. 使用具有 Google Workspace 组织项目访问权限的账号登录 [Google Cloud Console](https://console.cloud.google.com/)。
2. 在左侧导航中，进入 **API 和服务 → OAuth 同意屏幕**。
3. 将 **用户类型** 设置为 **内部 (Internal)**，确保只有您 Workspace 内的成员可以登录。
4. 填写必填字段（应用名称、用户支持邮箱、开发者联系信息）。
5. 保存。

## 创建 OAuth 客户端 ID

6. 在 Google Cloud Console 中，进入 **API 和服务 → 凭据**。
7. 点击 **创建凭据 → OAuth 客户端 ID**。
8. 将 **应用类型** 设置为 **Web 应用**。
9. 为客户端命名。我们推荐使用 `Bright Data Control Panel`。
10. **已获授权的重定向 URI** 暂时留空。下一节会从 Bright Data 复制重定向 URI 粘贴到此处。
11. 点击 **创建**。Google 会显示包含 **客户端 ID** 与 **客户端密钥** 的对话框，请复制这两个值。

## 配置 Bright Data

12. 在新标签页中打开 Bright Data [控制面板](https://www.bright.cn/cp/setting)，进入 **账户设置 → 密码与身份验证**。
13. 在 **配置单点登录 (Configure Single Sign-On)** 部分，点击 **Google Workspace**。
14. 在对话框中粘贴：
    * 步骤 11 中的 **Client ID**
    * 步骤 11 中的 **Client Secret**
    * **Workspace Domain**。您的 Google Workspace 主域名（例如 `yourcompany.com`）。
15. 复制对话框中显示的只读 **Sign-in redirect URI**。其形式为 `https://www.bright.cn/users/auth/google_workspace/<customer_id>/done`。

## 将重定向 URI 粘贴回 Google

16. 返回您在步骤 7 创建的 Google Cloud Console OAuth 客户端 ID。
17. 在 **已获授权的重定向 URI** 下，点击 **添加 URI**，粘贴步骤 15 中的 **Sign-in redirect URI**。
18. 点击 **保存**。

## 激活并测试

19. 返回 Bright Data 控制面板的 **Google Workspace** 对话框。
20. 点击 **激活 (Activate)**。
21. 退出 Bright Data 并通过 Google Workspace SSO 重新登录进行测试。使用的账号邮箱必须同时存在于您的 Google Workspace **和** Bright Data 控制面板的 **账户设置 → 用户** 中。

## 添加 SSO 登录用户

Bright Data 的 Google Workspace SSO 采用 **手动预置**，不支持 SCIM 或 JIT 自动创建用户。用户登录前需要：

1. 在 Bright Data 控制面板中，进入 **账户设置 → 用户**。
2. 添加该用户的邮箱地址。该邮箱必须与用户在 Google Workspace 中的主邮箱一致。
3. 设置该用户的角色。

当该用户首次通过 Google Workspace SSO 登录时，Bright Data 会基于此前预添加的邮箱自动创建用户记录。

## 注意事项

* OAuth 同意屏幕 **必须** 设置为 **内部 (Internal)** 用户类型。**外部 (External)** 同意屏幕会允许任何 Google 账号尝试登录。
* **Workspace Domain** 字段会强制校验 OIDC 的 `hd`（hosted domain，托管域）声明。仅当用户 Google 账号属于已配置的 Workspace Domain 时才能成功登录。
* Google Workspace SSO 与公共的 **使用 Google 账号继续** 登录按钮是 **完全独立** 的功能。两者使用不同的客户端 ID、重定向 URI 与预置流程。请参阅 [Google OAuth 2.0](/cn/general/authentication/How_to_set_up_SSO_with_Okta_in_Bright_Data#google-oauth-20)。
* 如果您在 Google Cloud Console 中轮换了 Client Secret，请同步在 Bright Data 对话框中更新，否则登录将失败并返回 `invalid_client` 错误。
* Bright Data 对话框中的 Sign-in redirect URI 必须与 Google Cloud Console 中 **已获授权的重定向 URI** 列表完全一致，否则会返回 `redirect_uri_mismatch` 错误。

***

## SSO 技术参考

如需完整的企业 SSO 技术参考（包括 OIDC 参数与各受支持身份提供商的预置方式对比），请参阅 Okta SSO 页面的 [SSO 技术参考](/cn/general/authentication/How_to_set_up_SSO_with_Okta_in_Bright_Data#sso-technical-reference) 章节。

### Google Workspace 特定参数

| 参数         | 取值                                                   |
| ---------- | ---------------------------------------------------- |
| 协议         | OpenID Connect (OIDC)                                |
| 应用类型       | Web 应用，在 Google Cloud Console → API 和服务 → 凭据 中创建     |
| 必需 scopes  | `openid profile email`                               |
| 用户标识       | `email` 声明                                           |
| 托管域强制校验    | 每次回调都会校验 `hd` 声明。仅来自已配置的 Workspace Domain 的邮箱可成功登录。  |
| OAuth 同意屏幕 | 必须为 **内部 (Internal)** 用户类型                           |
| 预置方式       | 手动。请在首次登录前先在 Bright Data 控制面板的 **账户设置 → 用户** 中预添加用户。 |
