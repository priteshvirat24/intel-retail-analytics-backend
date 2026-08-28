> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# FAQs

> 关于 Bright Data 代理浏览器扩展（端口 44445）的常见问题，包括登录问题、SSL 证书兼容性和 Chrome 设置步骤。

<AccordionGroup>
  <Accordion title="为什么一直出现登录信息？">
    Bright Data 使用Cookie来记住您的登录凭据，以提供最佳用户体验。如果您使用定期从设备中删除Cookie的第三方扩展程序，那么您会经常看到登录消息。
  </Accordion>

  <Accordion title="我升级到了新的 Bright Data SSL 证书，但扩展程序停止运行了">
    浏览器扩展程序支持端口 `44445` 上的新版 SSL 证书。请确保使用端口 `44445` 和 `brightdata_root_ca_44445.crt` 进行连接。请参阅[根证书迁移指南](/cn/general/account/ssl-certificate-migration)。
  </Accordion>

  <Accordion title="如何避免收到登录消息？">
    在右上角，您可以点击“删除 Cookie”。此操作从您的设备中删除除了Bright Data 和 Google 的 Cookie 之外的所有 Cookie，以便您可以不间断地使用我们的服务并让浏览器扩展程序保持活动状态。

    <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/scraping-automation/browser-extension/faqs/delete-cookies.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=2b12bd7cd72d60eb186b81f4e70af7a9" alt="delete-cookies.png" width="384" height="529" data-path="images/scraping-automation/browser-extension/faqs/delete-cookies.png" />
  </Accordion>

  <Accordion title="该扩展程序是否可以在隐身模式下运行？">
    > **是！**

    Bright Data 扩展程序在常规模式和隐身模式下均适用。

    要在 Chrome 上启用隐身支持，请执行以下操作：

    * 在 chrome 地址栏中输入 chrome://extensions
    * 确保勾选允许隐身

          <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/scraping-automation/browser-extension/faqs/allow-in-incognito.gif?s=4b220f4bc6100ddc3b906bc75da796c1" alt="allow-in-incognito.gif" width="1536" height="990" data-path="images/scraping-automation/browser-extension/faqs/allow-in-incognito.gif" />
  </Accordion>

  <Accordion title="何时应使用自定义标头？">
    自定义标头主要是为了使请求更加具体。当您需要将自定义参数与请求一起传递到目标站点时，您应该使用它。每个标头都应包含名称和值，您可以根据需要添加任意数量的标头。
  </Accordion>

  <Accordion title="为什么我在安装扩展程序时收到“错误”消息？">
    安装扩展程序时出现代理错误的原因可能是：

    * 未选择区域。确保正确填写表格。
    * 您的账户已被“禁用”。您可以在控制面板上轻松查看此信息: [https://www.bright.cn/cp](https://www.bright.cn/cp)
    * 您的余额为负数。请在您的账单部分查看此信息。[Billing](https://www.bright.cn/cp/billing)
    * Bright Data 网络状态问题。您可以在此处查看网络在线状态: [https://www.bright.cn/cp/status](https://www.bright.cn/cp/status)
  </Accordion>

  <Accordion title="该扩展程序可以与Browser API配合使用吗？">
    不可以。Browser API 不是代理产品，不兼容扩展程序。
  </Accordion>

  <Accordion title="多台机器是否可以在同一个账户上使用该扩展程序？">
    是。登录同一账户的扩展程序数量没有限制。
  </Accordion>

  <Accordion title="我是否可以在不提供我的账户凭据的情况下让其他人使用该扩展程序？">
    > **是！**

    他们需要转到扩展程序安装页面并使用您希望他们访问的区域的客户名称、区域名称和区域密钥登录。他们需要转到扩展程序安装页面并使用您希望他们访问的区域的客户名称、区域名称和区域密钥登录。所有区域信息均可在区域部分中找到。 [extension setup page](https://www.bright.cn/cp/bext), [Zones](https://www.bright.cn/cp/zones)

    您也可以使用此链接来自动插入访客登录凭据：

    ```
    https://www.bright.cn/cp/bext?customer=customer_id&zone=zone_name&key=ZONE-KEY
    ```
  </Accordion>

  <Accordion title="如何使用 Bright Data 扩展程序授予电子邮箱访问权限？">
    此工作流程与在与浏览器集成时允许访问代理管理器有关。通过更新代理管理器的配置文件来授予访问权限。

    这可以通过发送下一个 API 命令来完成：

    ```sh theme={null}
    curl -X POST "http://<remote-server-IP>:22999/api/proxies" -v -H "Content-Type: application/json" -d '{ "proxy": { "customer": "<account_ID>", "zone": "<zone>", "password":"<zone_password>", "multiply_users": true, "users": ["<email>"], "bw_limit": { "days": 100000, "bytes": 9000000000 } }, "create_users": true }'
    ```

    1. 将 `remote-server-IP` 更改为安装代理管理器的服务器 IP地址，如果是本地安装，则更改为 `127.0.0.1`。
    2. 将 `account_ID` 更改为您在设置页面上的账户 ID [settings page](https://www.bright.cn/cp/setting/customer_details)
    3. 将 `zone`, `zone_password`更改为区域页面的相关访问参数: [https://www.bright.cn/cp/zones](https://www.bright.cn/cp/zones)
    4. 将 `email` 更改为用户的电子邮箱。

    命令发送后，一封包含说明和凭据的详细电子邮件将发送至 `email`。

    在 API 输出中，还提供用户的密码以及端口号等附加信息。可以在下一个示例中查看：

    <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/scraping-automation/browser-extension/faqs/user-credentials.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=78550481e71cf923603b9e83ed4c4455" alt="user-credentials.png" width="591" height="58" data-path="images/scraping-automation/browser-extension/faqs/user-credentials.png" />

    用户现在可以通过安装扩展程序来访问代理。[extension](https://www.bright.cn/products/proxy-browser-extension).

    5. 安装后，选择“通过代理管理器连接”
           <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/scraping-automation/browser-extension/faqs/connect-through-proxy-manager.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=cdcf3aa53c623bb7adb3e5e80932bc0c" alt="connect-through-proxy-manager.png" width="315" height="437" data-path="images/scraping-automation/browser-extension/faqs/connect-through-proxy-manager.png" />

    6. 输入代理管理器服务器的IP地址以及相关的端口，例如：
           <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/scraping-automation/browser-extension/faqs/proxy-manager-ip.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=eec9924bfcce19aafaf49c1dbc3eeace" alt="proxy-manager-ip.png" width="319" height="425" data-path="images/scraping-automation/browser-extension/faqs/proxy-manager-ip.png" />

    7. 选择“完成”。然后，点击“登录”。
           <img src="https://mintcdn.com/brightdata/8FBihMtdCDBVIPQS/images/scraping-automation/browser-extension/faqs/sign-in.png?fit=max&auto=format&n=8FBihMtdCDBVIPQS&q=85&s=2552450a2eae997a71b392d109ee5ed0" alt="sign-in.png" width="463" height="59" data-path="images/scraping-automation/browser-extension/faqs/sign-in.png" />

    8. 输入收到的凭据。
  </Accordion>
</AccordionGroup>
