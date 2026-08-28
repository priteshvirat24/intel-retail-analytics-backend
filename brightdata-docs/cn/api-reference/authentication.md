> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 认证

> 学习如何使用 API 访问或原生访问方法认证 Bright Data。

Bright Data 确保对其服务的安全访问。

Bright Data 提供两种主要的认证方法：

1. **API 访问** - 使用 API key/token 认证并与 Bright Data 平台交互。
2. **原生访问** - 使用代理协议 `username` 和 `password` 认证并与 Bright Data 平台交互。

<Note>
  API 和原生访问方法的计费相同。使用费用根据每个 Bright Data 产品的定价计划收取。
</Note>

## 如何使用 API Key 进行认证？

API key 是用于认证 Bright Data API 的安全哈希令牌。我们在创建账户时会自动为您生成一个默认 key。\
您可以为不同用户和不同权限创建额外的 API key。

<Note>
  您可以随时在 [账户设置](https://www.bright.cn/cp/setting/users) 管理您的 API Key。
</Note>

### 如何在请求中传递 API Key？

示例请求：

```sh Sample Request theme={null}
curl --request POST \
  --url https://api.brightdata.com/request \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
    "zone": "my_unlocker_zone",
    "url": "https://example.com/page",
    "format": "json",
    "method": "GET",
    "country": "us",
    "data_format": "markdown"
  }'
```

此请求的关键部分是 `Authorization` 头：

```sh theme={null}
'Authorization: Bearer <token>'
```

这个 `<token>` 就是您的 **API key**，每个 API 请求都需要它。

### 如何生成新的 API Key？

生成新 API Key 的步骤如下：

<Steps>
  <Step title="登录">
    登录 Bright Data 控制面板并访问您的 [账户设置](https://www.bright.cn/cp/setting/users)。
  </Step>

  <Step title="点击 'Add API key'">
    在 API key 区域右上角点击 **Add API key** 按钮。

    <Warning>
      如果看不到 'API key' 区域，请切换到 **管理员账户**。只有管理员可以生成 API Key。\
      注意：每个用户只能生成一个 API Key。API Key 总数不能超过账户用户数。
    </Warning>
  </Step>

  <Step title="配置您的 API Key">
    设置用户、权限和到期日期（或选择“无限制”），然后点击 **保存**。
  </Step>

  <Step title="本地保存您的 API Key">
    <Warning>
      生成后，API Key 只会显示一次。请确保 **安全保存**。
    </Warning>
  </Step>
</Steps>

### API Key 的选项和配置是什么？

创建 API Key 时，您可以分配五种权限级别之一，以根据用户角色或使用场景控制访问并确保安全。[了解更多用户角色](/cn/api-reference/authentication#understanding-api-key-permissions)。

#### API Key 拥有哪些权限级别？

可选择 5 种权限来控制 API Key 访问：

* **管理员:** 完全访问账户，包括所有账单、财务、产品设置和配置。
* **财务:** 仅允许访问账单和财务页面。
* **运维:** 允许访问区域/产品配置，但限制账单访问。
* **限制:** 允许管理区域密码和 IP 白名单/黑名单。
* **用户:** 允许在区域/产品层级使用 API，但无权访问账单或产品配置页面。

#### API Key 有过期日期吗？

创建 API Key 时，可以设置其过期日期。超过过期日期的请求将被拒绝。

您也可以将过期日期设置为 `unlimited`，尽管可行，但强烈建议设置过期日期。

请咨询贵组织的信息或数据安全官员获取指导。

#### 如何查看 API Key 设置和配置？

您可以在 [账户设置](https://www.bright.cn/cp/setting/users) 查看和管理 API Key。

#### 为什么无法看到 API Key 的明文或复制它？

出于安全考虑，我们不允许查看具有 `admin` 权限的 API Key 的明文。创建后，您将被提供复制和保存 Key 的选项。

#### 可以刷新 API Key 吗？

可以。点击“刷新”后，我们将生成新的 API Key。刷新后，使用旧 Key 的请求将无法认证。

#### 应该在哪里保存具有管理员权限的 API Key?

API Key 类似密码，应谨慎处理并在受控访问下保存。请咨询 IT 或安全管理员，按照组织流程和规定保存 Key。

## 如何使用原生代理协议进行认证？

### 可以使用代理协议访问哪些产品区域？

代理协议支持访问：

* 所有代理网络（数据中心、ISP、住宅和移动）
* Web Unlocker
* Scraping 浏览器

### 如何使用原生代理用户名和密码进行认证？

示例原生访问请求：

```sh Sample Request theme={null}
curl "https://www.example.com" \
  -i --proxy brd.superproxy.io:44445 \
  --proxy-user brd-customer-[ACCOUNT_ID]-zone-[ZONE_NAME]:[ZONE_PASSWORD]
```

请求的关键部分是 `--proxy-user` 参数，它包含认证凭证：

```sh proxy-user theme={null}
brd-customer-[ACCOUNT_ID]-zone-[ZONE_NAME]:[ZONE_PASSWORD]
```

此参数由三个元素组合成单个字符串：

1. `ACCOUNT_ID` - 您的唯一客户标识符。
2. `ZONE_NAME` - 您创建的区域名称。
3. `ZONE_PASSWORD` - 与您的区域关联的密码。

三者组合形成完整的 proxy-user 值。

### 用户名/密码格式

* 所有参数区分大小写。
* 必须为连续字符串，不允许空格。
* 用户名子串之间用 `-` 分隔，用户名和密码之间用 `:` 分隔。

#### 账户 ID

账户 ID 是在创建 Bright Data 账户时自动生成的唯一标识符，用于认证和账户相关操作。

查找账户 ID 的步骤：

<Steps>
  <Step title={<>点击左侧菜单中的 <a href="https://www.bright.cn/cp/setting/customer_details">账户设置</a>。</>} />

  <Step title="打开个人资料标签页。" />

  <Step title="找到并复制您的账户 ID。" />
</Steps>

<Frame>
  <img src="https://mintcdn.com/brightdata/0sd4eqxAli7ENzfc/images/api-reference/authentication/account_id.png?fit=max&auto=format&n=0sd4eqxAli7ENzfc&q=85&s=e2e2e23c6fd9aa19087cfb6d0a5fbeec" alt="账户 ID" width="2754" height="678" data-path="images/api-reference/authentication/account_id.png" />
</Frame>

<Note>
  账户 ID 始终是以 `hl_###` 开头的文本字符串。
</Note>

#### 区域名称

区域是 Bright Data 为特定服务收集的配置集合。[了解更多关于区域的信息](/cn/api-reference/terminology#what-is-a-zone)。
区域名称由您在创建区域时 **唯一设置一次**，之后无法更改。

您可以访问 [我的区域](https://www.bright.cn/cp/zones) 查看所有区域名称。

#### 区域密码

每个 **区域** 都分配唯一密码，用于认证 API 和原生访问请求。

查看或更新区域密码的步骤：

<Steps>
  <Step title={<>在仪表板中打开 <a href="https://www.bright.cn/cp/zones">我的区域</a>。</>} />

  <Step title="进入配置标签页。" />

  <Step title="向下滚动到安全设置部分并展开。" />

  <Step title="复制当前密码，或根据需要生成新密码。" />
</Steps>

## API 访问 vs 原生访问 比较

| 功能                                                | API 访问                                                                                                                                                                                                                                                                                                                               | 原生访问                                                                                        |
| :------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------ |
| **用途**                                            | 与脚本、自动化工具或第三方 API 无缝集成                                                                                                                                                                                                                                                                                                               | 在浏览器、爬虫或兼容代理工具中直接使用代理连接                                                                     |
| **推荐产品**                                          | - [Web Unlocker API](/cn/scraping-automation/web-unlocker)<br />- [SERP](/cn/scraping-automation/serp-api)<br />- [Browsers](/cn/scraping-automation/scraping-browser)<br />- [Scrapers](/cn/datasets/scrapers/overview)<br />- [Functions](/cn/datasets/scraper-studio/introduction)<br />- [Marketplace](/cn/datasets/marketplace) | [Proxies](/cn/proxy-networks)                                                               |
| [**SSL 证书**](/cn/general/account/ssl-certificate) | 不需要                                                                                                                                                                                                                                                                                                                                  | 访问住宅网络 & Unlocker 时无需 KYC，需要 SSL 证书。更多信息[这里](/cn/proxy-networks/residential/network-access) |
| **连接方式**                                          | API 端点                                                                                                                                                                                                                                                                                                                               | 代理端点                                                                                        |
| **认证方式**                                          | [API key](/cn/api-reference/authentication#how-do-i-generate-a-new-api-key%3F)                                                                                                                                                                                                                                                       | `username:password`                                                                         |
| **输出选项**                                          | HTML 或 JSON                                                                                                                                                                                                                                                                                                                          | HTML                                                                                        |
