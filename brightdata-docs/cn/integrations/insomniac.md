> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何将 Bright Data 与 Insomniac 集成

> 使用 Bright Data 代理与 Insomniac 集成，可提升自动化效率，提供安全匿名连接，降低被检测风险，并确保操作更顺畅。

<Accordion title="展开以获取您的 Bright Data 代理访问信息">
  ### 您的代理访问信息

  Bright Data 代理按“代理区域”（Proxy zones）进行分组。每个区域包含其对应的代理配置。&#x20;

  要获取代理区域的访问权限：&#x20;

  1. 登录 Bright Data 控制面板
  2. 选择现有代理区域或新建一个代理区域
  3. 点击新的区域名称，并选择 **概览（Overview）** 选项卡
  4. 在概览选项卡中，找到 **访问详情（Access details）**，并单击复制图标将代理访问信息复制到剪贴板&#x20;
  5. 您需要以下信息：代理主机（Proxy Host）、代理端口（Proxy Port）、代理区域用户名（Proxy Zone username）和代理区域密码（Proxy Zone password）
  6. 点击复制图标，将文本复制到剪贴板，并粘贴到您的工具的代理配置中&#x20;

  ### 访问详情示例

  <img src="https://mintcdn.com/brightdata/w0SvUEkwL-1dGVtS/snippets/accessdetails.png?fit=max&auto=format&n=w0SvUEkwL-1dGVtS&q=85&s=a3d4e920631ae105cb2f388c63bc5b5d" alt="" width="597" height="508" data-path="snippets/accessdetails.png" />

  ### 住宅代理访问

  要使用 Bright Data 的 **住宅代理（Residential Proxies）**，您必须是经过 KYC 验证的企业账户。请与 Bright Data 合规团队完成 KYC 验证；不存在自动或无需 KYC 的访问方式。尚未完成 KYC 时，请使用 ISP 或数据中心代理。[了解更多...](/proxy-networks/residential/network-access)

  ### 目标是搜索引擎？

  如果您的目标是 Google、Bing 或 Yandex 等搜索引擎，则需要使用专门的搜索引擎结果页（**SERP**）代理 API。请使用 Bright Data SERP API 来访问搜索引擎。\
  [点击此处了解 Bright Data SERP 代理 API。](/scraping-automation/serp-api/introduction)

  ### 避免工具中的 `PROXY ERROR`

  一些工具会使用搜索引擎作为代理测试目标：如果您的代理测试失败，这可能就是原因。请确保您的测试目标域名不是搜索引擎（此设置在工具配置中，而非 Bright Data 代理的控制范围内）。
</Accordion>

## 什么是 Insomniac？

Insomniac 是一款在线采购工具，可通过其多会话浏览器隐藏你的数字足迹。Insomniac 浏览器允许你为每个标签页配置不同的代理，从而为每个标签应用不同的 IP 地址，保护在线隐私。

<Tip>
  使用用户名中的 `-session` 参数，可在整个浏览会话中保持 IP 一致。这很重要，因为 Bright Data 代理默认每次请求都会轮换 IP。[了解更多](/proxy-networks/faqs#how-to-use-the-same-ip-for-an-extended-period-of-time-and-how-long-can-i-keep-it-long-session)

  新用户应从 ISP 或数据中心代理开始，这些代理无需 KYC。住宅代理仅向通过 KYC 验证的企业账户开放。详见[住宅网络访问政策](/cn/proxy-networks/residential/network-access)。
</Tip>

## 如何使用 Bright Data 代理设置 Insomniac

### 选择重复使用代理还是每次轮换新代理？

Bright Data 提供两类主要代理：

1. 代理轮换池
2. 固定代理集（可共享或专用）

如果选择 Datacenter、ISP 或共享住宅代理池，Insomniac 浏览器无需处理轮换，Bright Data 会在每次会话中自动分配新代理。

如果需要固定代理（如管理社交媒体账户），可将所有代理加载到 Insomniac 中，并按需配置轮换逻辑。

## Insomniac 浏览器设置

* 下载并安装 Insomniac 浏览器
* 打开 **Insomniac 浏览器**
* 点击 **Global sess.**

<Frame>
  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/Insomniac_setup_1.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=b3b53bae3c461bf0e92c3452da8c0feb" alt="Insomniac_setup_1.png" width="1615" height="651" data-path="images/integrations/Insomniac_setup_1.png" />
</Frame>

* 点击 **Proxy List**

<Frame>
  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/Insomniac_setup_2.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=f2dd773e774115650e4b290b0281a415" alt="Insomniac_setup_2.png" width="1389" height="652" data-path="images/integrations/Insomniac_setup_2.png" />
</Frame>

* 将打开设置窗口，粘贴你的代理配置

<Frame>
  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/Insomniac_setup_3.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=62c3015f6cb7ffc492f895b0b0f9d94f" alt="Insomniac_setup_3.png" width="1404" height="829" data-path="images/integrations/Insomniac_setup_3.png" />
</Frame>

所需格式为 **逗号分隔**：`host,port,user,password`

## 将 Insomniac 与 Bright Data 代理集成

* 进入 Bright Data 控制面板并点击 **Create a Zone**
* 选择你的配置
* 点击 **Save**
* 区域包含你的代理设置及连接信息

如需使用 Bright Data 的轮换功能，每次会话使用不同代理，将控制面板的设置复制到 Insomniac 即可。

<Frame>
  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/Insomniac_setup_4.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=4d40a281f326e54ae82acb668be190b3" alt="Insomniac_setup_4.png" width="1444" height="690" data-path="images/integrations/Insomniac_setup_4.png" />
</Frame>

如需加载特定的 Datacenter 或 ISP 固定代理，请在 Bright Data 控制面板的 Zone Overview 标签页点击 **Download** 下载代理列表。弹出窗口提供三种格式，Insomniac 需要逗号分隔格式（现可通过替换冒号实现）：

<Frame>
  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/Insomniac_setup_5_brd_dc_iplistdwnld.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=c6fd459cf4cf1f0e794b6b6137cd7f82" alt="Insomniac_setup_5_brd_dc_iplistdwnld.png" width="1513" height="838" data-path="images/integrations/Insomniac_setup_5_brd_dc_iplistdwnld.png" />
</Frame>

使用文本编辑器打开文件，通过“查找替换”将所有冒号替换为逗号（在记事本中使用 `Ctrl+H`）：

<Frame>
  <img src="https://mintcdn.com/brightdata/jeaQWxFKde5jgPN8/images/integrations/Insomniac_setup_7_proxylist_notepad.png?fit=max&auto=format&n=jeaQWxFKde5jgPN8&q=85&s=6f6ff80faa04a4bcd888ccd1eb52aa5a" alt="insomniac_setup_7_proxylist_notepad.png" width="1423" height="723" data-path="images/integrations/Insomniac_setup_7_proxylist_notepad.png" />
</Frame>

复制粘贴列表后，Insomniac 中会出现多个代理条目，可根据需求配置轮换逻辑。

## 将多个 Proxy Manager 端口与 Insomniac 集成

* 下载 [Proxy Manager](https://www.bright.cn/products/proxy-manager)
* 点击 **Add new Proxy** 创建新端口
* 选择新端口（24XXX）
* 在端口设置中打开 **General** 标签
* 在 **Multiply proxy port** 字段选择创建的端口数量，生成多个代理端口
* 你的表格应包含以下列：
  * Custom Name: 为每个代理添加名称
  * Host: 127.0.0.1
  * Port: 24XXX
  * Username、Password 和 Tags: 保持空白（Proxy Manager 已通过 Super Proxy 验证）
* 将文件另存为 **CSV** 格式
* 在 Insomniac **Proxy per tab** 扩展中选择 **Manage Proxy list** -> **Add bulk proxies**
* 选择 **Import proxy list** 并上传 CSV 文件

<Warning>
  **重要提示**：

  如果使用 Bright Data 的住宅代理、Web Unlocker API 或 SERP API，需要安装 SSL 证书以启用目标网站的端到端安全连接。

  简单安装方法，请参考 [此指南](/general/account/ssl-certificate#installation-of-the-ssl-certificate)。
</Warning>
