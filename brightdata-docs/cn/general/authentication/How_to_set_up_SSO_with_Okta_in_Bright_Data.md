> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在 Bright Data 中设置 Okta SSO？

**要求**

* 具有管理员权限的 Okta 组织账户
* 具有管理员权限的 Bright Data 账户

<Warning>
  **强制启用 Okta SSO 会禁用基于密码的登录。**

  当您的组织强制启用 Okta SSO 后，账户下所有用户的基于密码的登录和密码重置邮件都将被禁用。用户必须通过 Okta 登录。如果出现访问问题，请联系您的 IT / Okta 管理员。
</Warning>

**步骤：**

1. 在 Okta 管理员控制面板中，选择“应用程序 > 应用程序”

```sh theme={null}
https://[your_domain]-admin.okta.com/admin/apps/active
```

2. 点击“创建应用程序集成”

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/okta_1.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=f07424c2d9aaa4d22925cc3cb0f9a17e" alt="mceclip0.png" width="612" height="234" data-path="images/general/authentication/okta_1.png" />

3. 选择“OIDC - OpenID 连接”作为登录方法

4. 选择“Web 应用程序”作为应用程序类型，然后点击“下一步”

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/okta_2.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=bb4a94c762fbf40c2aa65152e247b230" alt="mceclip1.png" width="853" height="739" data-path="images/general/authentication/okta_2.png" />

5. 此时，系统会跳转至新的 Web 应用程序集成页面。 您可以在该页面中为应用程序集成命名（建议使用“Bright Data 控制面板”这一名称）。

6. 在“授权类型”中，同时选择隐式授权和授权码

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/okta_3.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=3257204b5d377f268997fc97513d15b7" alt="mceclip0.png" width="932" height="554" data-path="images/general/authentication/okta_3.png" />

7. 进入 Bright Data 控制面板: [https://www.bright.cn/cp/setting](https://www.bright.cn/cp/setting)

8. 打开 OKTA 配置对话框

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/okta_4.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=7bf0d60bcadc135b5027d967c583864c" alt="mceclip1.png" width="460" height="420" data-path="images/general/authentication/okta_4.png" />

9. 复制“登录重定向 URI”

**<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/okta_5.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=6fedc0f3909a5e03cbb622cafcdca07e" alt="mceclip2.png" width="630" height="630" data-path="images/general/authentication/okta_5.png" />**

10. 将其粘贴到 OKTA 新应用程序设置中的相应字段

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/okta_6.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=82142217dd02546084260d965f5247b9" alt="mceclip3.png" width="964" height="625" data-path="images/general/authentication/okta_6.png" />

11. 对“退出 URI”执行相同操作

12. 在“分配”中，选择所需的访问级别

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/okta_7.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=73c80b9abf46afd4f99c609b25c0c180" alt="mceclip6.png" width="894" height="291" data-path="images/general/authentication/okta_7.png" />

13. 点击“保存”

14. 系统随即跳转至新的应用程序集成设置页面。

将客户端 ID、客户端密钥和 Okta 域名复制到 Bright Data 控制面板中的 OKTA 设置对话框。

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/okta_8.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=a2f6b84e2fd8c347ee7eaf868c4281f7" alt="mceclip4.png" width="769" height="582" data-path="images/general/authentication/okta_8.png" />

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/okta_9.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=b16209c4c35e7f5cec86fbdf36319d38" alt="mceclip5.png" width="613" height="630" data-path="images/general/authentication/okta_9.png" />

15. 点击“激活”。

如果选择“允许所有人访问”，请跳过第 16 步

16. 进入“分配”选项卡，分配可使用此集成的用户

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/okta_10.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=7e59f843a7556b257810a97f5adcbef0" alt="mceclip6.png" width="767" height="721" data-path="images/general/authentication/okta_10.png" />

17. 进入 Bright Data 设置页面，确保所有需要访问该集成的用户均已添加。

我们正在努力开发用户配置支持功能，目前需要您手动管理。

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/okta_11.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=1cc13b26548accdd4ac6a24830ee15f0" alt="mceclip7.png" width="829" height="547" data-path="images/general/authentication/okta_11.png" />

***以下为可选步骤， 旨在确保用户能够通过其控制面板或 Okta Chrome 扩展程序启动身份验证。***

18. 向下滚动到“常规设置”，然后点击编辑

19. 进行以下设置：

* 登录发起者：Okta 或应用程序
* 应用程序可见性：向用户显示应用程序图标
* 登录流程：重定向到应用程序以启动登录（符合 OIDC 标准）
* 从控制面板复制“启动登录 URI”

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/okta_12.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=79c326cb7a4583fd41ac0f84f967cc52" alt="mceclip8.png" width="619" height="632" data-path="images/general/authentication/okta_12.png" />

<img src="https://mintcdn.com/brightdata/hiKWnoPeUYwLvmyy/images/general/authentication/okta_13.png?fit=max&auto=format&n=hiKWnoPeUYwLvmyy&q=85&s=4799d6f347f9b9231bb5db89c7bdaef6" alt="mceclip9.png" width="771" height="609" data-path="images/general/authentication/okta_13.png" />

20. 保存更改。 **至此，集成配置已经完成，可以使用了。**

**注意事项**

* Okta 域名应使用应用程序集成设置中显示的域名 (yourcompany.okta.com)，而非管理员界面中看到的域名 (yourcompany-admin.okta.com)

* 请确保向 Bright Data 提供的凭据正确无误，我们无法验证这些凭据。

* 登录重定向 URI 是确保 SSO 功能正常运行的必要条件

* 如果希望通过 Okta Chrome 扩展程序或 Okta 控制面板使用该功能，需要配置启动登录 URI
