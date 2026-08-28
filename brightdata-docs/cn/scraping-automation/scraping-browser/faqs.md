> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Browser API 常见问题解答

> 查找关于 Bright Data Browser API 的常见问题答案，包括支持的语言、调试技巧和集成指南。

<AccordionGroup>
  <Accordion title="我可以选择 Browser API 抓取的国家吗？">
    Browser API 会自动为每个请求选择最佳的 IP 类型和位置，利用 Bright Data 的高级解锁功能。虽然可以指定位置，但通常不建议这样做，因为自动化系统能确保页面访问的最佳成功率。

    如果您需要从特定国家启动，可以在端点中的用户名后添加 `-country` 标志以及相应的两位 ISO 代码。完整说明和示例请参阅我们的[位置定位文档](/cn/scraping-automation/scraping-browser/features/proxy-location)。

    如果需要定位到特定区域（不仅仅是国家），请查看我们的[Proxy.setLocation 指南](/cn/scraping-automation/scraping-browser/features/proxy-location#geolocation-radius)。
  </Accordion>

  <Accordion title="Browser API 完全支持哪些编程语言和工具？">
    * Browser API 对以下组合提供完整原生支持：
      * **Node.js**: Puppeteer (原生), Playwright (原生), Selenium WebDriverJS
      * **Python**: Playwright for Python, Selenium WebDriver for Python
      * **Java**: Playwright for Java, Selenium WebDriver for Java
      * **C# (.NET)**: Playwright for .NET, Selenium WebDriver for .NET

    查看[代码示例](/cn/scraping-automation/scraping-browser/code-examples)页面以获取使用支持库的多种示例。
  </Accordion>

  <Accordion title="如何在其他语言和工具中使用 Browser API？">
    * Browser API 也可以通过社区或第三方库集成到其他语言：
      * **Java**: Puppeteer Java
      * **Ruby**: Puppeteer-Ruby, playwright-ruby-client, Selenium WebDriver for Ruby
      * **Go**: chromedp, playwright-go, Selenium WebDriver for Go
    * 对于未列出的语言，如果库支持远程 Chrome DevTools Protocol 或 WebDriver，也可以进行集成。

    <Note>
      为了获得最佳效果并访问完整功能集，请使用完全支持语言常见问题中列出的原生集成。
    </Note>
  </Accordion>

  <Accordion title="我如何查看验证码的状态？">
    您可以使用 CDP 功能等待验证码解决并检查其状态。详细说明和示例代码，请参阅此[指南](/cn/scraping-automation/scraping-browser/cdp-functions/custom#如何解决验证码)。

    例如，您可以在脚本中期望出现验证码的位置添加以下代码片段：

    <CodeGroup>
      ```sh NodeJS, Puppeteer theme={null}
      const client = await page.target().createCDPSession();  
      const {status} = await client.send('Captcha.solve', {detectTimeout: 30*1000});   
      console.log(`Captcha solve status: ${status}`)   
      ```
    </CodeGroup>
  </Accordion>

  <Accordion title="在 Browser API 会话中，我如何调试后台发生的事情？">
    您可以通过在本地启动 **Browser API Debugger** 来监控实时 Browser API 会话。这类似于在 Puppeteer 中将 headless 浏览器设置为 'FALSE'。

    **Browser API Debugger** 是一个有价值的资源，可让您与 Chrome Dev Tools 一起检查、分析和微调代码，从而实现更好的控制、可视性和效率。

    ## 我在哪里可以找到 Browser API Debugger？

    Browser API Debugger 可通过两种方式启动：

    * 通过控制面板手动启动
    * 通过脚本远程启动

          <Tabs>
            <Tab title="通过控制面板">
              您可以在 Bright Data [控制面板](https://www.bright.cn/cp/zones) 内轻松访问 Browser API Debugger。操作步骤如下：

              1. 在控制面板中，进入 [我的代理](https://www.bright.cn/cp/zones) 页面
              2. 点击您的 Browser API 代理
              3. 点击 **概览** 标签
              4. 在右侧，点击 "Chrome Dev Tools Debugger" 按钮 <img src="https://mintcdn.com/brightdata/S8tFtc_KJjCQxqv1/images/scraping-automation/scraping-browser/features/debugger/chrome-devtools-debugger.png?fit=max&auto=format&n=S8tFtc_KJjCQxqv1&q=85&s=af311142afae46229a68bcacfb2f4962" alt="chrome-devtools-debugger.png" width="1111" height="626" data-path="images/scraping-automation/scraping-browser/features/debugger/chrome-devtools-debugger.png" /> **调试器与 Chrome Dev Tools 入门**

              <Steps>
                <Step title="打开 Browser API 会话">
                  * 确保您有一个 **活动的** Browser API 会话
                  * 如果您还不知道如何启动 Browser API 会话，请参阅我们的[快速入门](/cn/scraping-automation/scraping-browser/introduction)指南。
                </Step>

                <Step title="启动调试器">
                  * 会话启动后，您可以启动调试器。
                  * 在 *概览* 标签中点击调试器按钮以打开 Browser API Debugger 界面（参见上图 [链接](#h_01H17FZAYFCAKBQ358JN5G2FQP)）
                </Step>

                <Step title="连接实时浏览器会话">
                  * 在调试器界面中，您会看到实时 Browser API 会话列表。
                  * 选择您希望调试的会话
                  * 点击会话链接或将其复制到浏览器中，这将建立调试器与所选会话之间的连接。
                </Step>
              </Steps>
            </Tab>

            <Tab title="通过代码（远程）">
              若要从脚本直接访问和启动调试器会话，需发送 CDP 命令：`Page.inspect`。

              <CodeGroup>
                ```js Puppeteer theme={null}
                // Node.js Puppeteer - 使用 devtools 检查页面  
                const page = await browser.newPage();  
                const client = await page.target().createCDPSession();  
                const {frameTree: {frame}} = await client.send('Page.getFrameTree', {});  
                const {url: inspectUrl} = await client.send('Page.inspect', {  
                    frameId: frame.id,  
                });  
                console.log(`Inspect session at ${inspectUrl}`);
                ```

                ```js Playwright theme={null}
                // Node.js Playwright - 使用 devtools 检查页面  
                const page = await browser.newPage();  
                const client = await page.context().newCDPSession(page);  
                const {frameTree: {frame}} = await client.send('Page.getFrameTree', {});  
                const {url: inspectUrl} = await client.send('Page.inspect', {  
                    frameId: frame.id,  
                });  
                console.log(`Inspect session at ${inspectUrl}`);
                ```

                ```Python Playwright theme={null}
                # Python Playwright - 使用 devtools 检查页面  
                page = await browser.new_page()  
                client = await page.context.new_cdp_session(page)  
                frame_tree = await client.send('Page.getFrameTree', {})  
                frame_id = frame_tree['frameTree']['frame']['id']  
                inspect = await client.send('Page.inspect', {'frameId': frame_id})  
                inspect_url = inspect['url']  
                print('Inspect session at', inspect_url)
                ```

                ```cs PuppeteerSharp theme={null}
                // C# PuppeteerSharp - 使用 devtools 检查页面  
                var page = await browser.NewPageAsync();  
                var client = await page.Target.CreateCDPSessionAsync();  
                var frameTree = await client.SendAsync("Page.getFrameTree");  
                var frameId = frameTree!["frameTree"]!["frame"]!["id"]!;  
                var inspect = await client.SendAsync("Page.inspect", new { frameId = frameId });  
                var inspectUrl = inspect["url"]!;  
                Console.WriteLine($"Inspect session at {inspectUrl}");
                ```

                ```cs Playwright theme={null}
                // C# Playwright - 使用 devtools 检查页面  
                var page = await browser.NewPageAsync();  
                var client = await page.Context.NewCDPSessionAsync(page);  
                var frameTree = await client.SendAsync("Page.getFrameTree");  
                var frameId = frameTree.Value  
                    .GetProperty("frameTree")  
                    .GetProperty("frame")  
                    .GetProperty("id")  
                    .GetString()!;  
                var inspect = await client.SendAsync("Page.inspect", new ()  
                {  
                    { "frameId", frameId },  
                });  
                var inspectUrl = inspect.Value  
                    .GetProperty("url")  
                    .GetString()!;  
                Console.WriteLine($"Inspect session at {inspectUrl}");
                ```
              </CodeGroup>
            </Tab>
          </Tabs>

      **利用 Chrome Dev Tools**

      * 连接实时会话后，您可以使用 [Chrome Dev Tools](https://chromedevtools.github.io/devtools-protocol/) 的强大功能。
      * 使用 Dev Tools 界面检查 HTML 元素、分析网络请求、调试 JavaScript 代码并监控性能。利用断点、控制台日志和其他调试技术识别和解决代码中的问题。 <img src="https://mintcdn.com/brightdata/S8tFtc_KJjCQxqv1/images/scraping-automation/scraping-browser/features/debugger/test-sites.png?fit=max&auto=format&n=S8tFtc_KJjCQxqv1&q=85&s=e4ae617f25eafd7b2a7253841583609b" alt="test-sites.png" width="955" height="411" data-path="images/scraping-automation/scraping-browser/features/debugger/test-sites.png" />
  </Accordion>

  <Accordion title="如何自动在本地启动 DevTools 以查看实时浏览器会话？">
    如果希望在每个会话中自动启动 DevTools 以查看实时浏览器会话，可以集成以下代码片段：

    ```js NodeJS - Puppeteer theme={null}
    // Node.js Puppeteer - 本地启动 devtools  

    // 除其他必要导入外添加以下依赖
    const { exec } = require('child_process');  
    const chromeExecutable = 'google-chrome';  

    // 将以下函数添加到脚本顶部  
    const delay = ms => new Promise(resolve => setTimeout(resolve, ms));  
    const openDevtools = async (page, client) => {  
        // 获取当前 frameId  
        const frameId = page.mainFrame()._id;  
        // 从 Browser API 获取 devtools URL  
        const { url: inspectUrl } = await client.send('Page.inspect', { frameId });  
        // 在本地 Chrome 中打开 devtools URL  
        exec(`"${chromeExecutable}" "${inspectUrl}"`, error => {  
            if (error)  
                throw new Error('无法打开 devtools: ' + error);  
        });  
        // 等待 devtools UI 加载  
        await delay(5000);  
    };  

    // 在导航到目标 URL 前添加这些行  
    const page = await browser.newPage();  
    const client = await page.target().createCDPSession();  
    await openDevtools(page, client);  
    await page.goto('http://example.com');

    ```
  </Accordion>

  <Accordion title="如何获取浏览器操作的截图？">
    <Tabs>
      <Tab title="触发截图">
        您可以随时通过在代码中添加以下内容轻松触发浏览器截图：

        ```js NodeJS theme={null}
        // node.js puppeteer - 保存截图到 screenshot.png 
        await page.screenshot({ path: 'screenshot.png', fullPage: true });
        ```

        Python 和 C# 截图方法见[这里](/cn/scraping-automation/scraping-browser/code-examples)。
      </Tab>

      <Tab title="本地启动 DevTools">
        查看我们完整章节关于[自动打开 DevTools](/cn/scraping-automation/scraping-browser/features/troubleshooting#scraping-browser-debugger)。
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="为什么某些页面的初次导航比其他页面更慢？">
    页面解锁存在大量“幕后”工作。

    某些网站只需几秒即可导航，而其他网站可能需要一到两分钟，因为它们需要更复杂的解锁流程。因此，我们建议将导航超时设置为“2 分钟”，以确保必要时导航能成功。

    可在脚本中 **page.goto** 调用前添加以下代码，将导航超时设置为 2 分钟。

    <CodeGroup>
      ```js Puppeteer theme={null}
      // node.js puppeteer - 导航到网站，超时 2 分钟  
      page.goto('<https://example.com>', { timeout: 2*60*1000 });  
      ```

      ```python Playwright theme={null}
      # python playwright - 导航到网站，超时 2 分钟   
      page.goto('<https://example.com>', timeout=2*60*1000)  
      ```

      ```cs PuppeteerSharp theme={null}
      // C# PuppeteerSharp - 导航到网站，超时 2 分钟   
      await page.GoToAsync("https://example.com", new NavigationOptions()  
      {  
          Timeout = 2*60*1000,  
      });
      ```
    </CodeGroup>
  </Accordion>

  <Accordion title="收到 Browser API 返回的错误时应该怎么办？">
    Browser API 返回的每个错误都包含一个用于说明失败原因的错误代码。请查看[错误代码页面](/cn/scraping-automation/scraping-browser/error-codes)，查找您收到的代码的含义以及建议操作。
  </Accordion>

  <Accordion title="Browser API 在出错时会返回哪些状态代码？">
    当请求失败时，Browser API 可能会返回特定的 HTTP 状态代码。以下是一些常见的错误代码、它们的含义以及建议操作：

    | 错误代码                            | 含义        | 建议操作                                                             |
    | :------------------------------ | :-------- | :--------------------------------------------------------------- |
    | Unexpected server response: 407 | 远程浏览器端口问题 | 请检查远程浏览器端口。Browser API 的正确端口为 `9222`。                            |
    | Unexpected server response: 403 | 认证错误      | 检查您的认证凭据（用户名、密码），并确认您使用的是 Bright Data 控制面板中正确的 "Browser API" 区域。 |
    | Unexpected server response: 503 | 服务不可用     | 我们可能正在扩展浏览器以满足需求，请 1 分钟后重试。                                      |
  </Accordion>

  <Accordion title="无法与 Browser API 建立连接，是连接问题吗？">
    如果遇到连接问题，可以通过以下端点使用 curl 测试本地 Browser API 连接：

    ```sh Shell theme={null}
    curl -v -u SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD https://brd.superproxy.io:9222/json/protocol
    ```

    #### 如果响应中返回 JSON：

    * 您的认证和 Browser API 连接成功，请确认脚本中使用的配置正确。
    * 如果仍无法连接 Browser API，请[联系支持](mailto:support@brightdata.com)获取进一步帮助。

    #### 如果响应中未返回 JSON：

    * 检查 Browser API 区域的认证信息，确保 USER 和 PASS 值正确。
    * 验证网络配置：确认网络或防火墙未阻止到 `https://brd.superproxy.io:9222` 的出站连接。
    * 如果问题仍然存在，请[联系支持](mailto:support@brightdata.com)获取进一步帮助。
  </Accordion>

  <Accordion title="如何将 Browser API 集成到 .NET Puppeteer Sharp？">
    使用 C# 集成 Browser API 需要修补 PuppeteerSharp 库以支持 websocket 认证，可按如下方式操作：

    ```cs C# PuppeteerSharp theme={null}
    using PuppeteerSharp;  
    using System.Net.WebSockets;  
    using System.Text;  
      
    // 设置认证凭据  
    var auth = "SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD";  
    // 构造带认证的 WebSocket URL  
    var ws = $"wss://{auth}@brd.superproxy.io:9222";  
    // 自定义 WebSocket 工厂函数  
    async Task<WebSocket> ws_factory(Uri url, IConnectionOptions options, CancellationToken cancellationToken)  
      
    {  
        var socket = new ClientWebSocket();  
        var user_info = url.UserInfo;  
        if (user_info != "")  
        {  
            var auth = Convert.ToBase64String(Encoding.Default.GetBytes(user_info));  
            socket.Options.SetRequestHeader("Authorization", $"Basic {auth}");  
        }  
      
        socket.Options.KeepAliveInterval = TimeSpan.Zero;  
        await socket.ConnectAsync(url, cancellationToken);  
        return socket;  
    }  
      
    var options = new ConnectOptions()  
    {  
        BrowserWSEndpoint = ws,  
        WebSocketFactory = ws_factory,  
    };  
      
    Console.WriteLine("Connecting to browser...");  
      
    using (var browser = await Puppeteer.ConnectAsync(options))  
    {  
        Console.WriteLine("Connected! Navigating...");  
        var page = await browser.NewPageAsync();  
        await page.GoToAsync("https://example.com");  
        Console.WriteLine("Navigated! Scraping data...");  
        var content = await page.GetContentAsync();  
        Console.WriteLine("Done!");  
        Console.WriteLine(content);  
    }
    ```
  </Accordion>

  <Accordion title="Browser API 的计费方式如何？">
    Browser API 计费简单：您仅需为通过 Browser API 传输的流量付费。

    Browser API 使用实例或时间不收取费用——仅按流量计费。

    不管使用哪个国家，流量按相同费率计费。由于按流量计费，您可能希望尽量减少流量。

    唯一例外是高级域名，每 GB 收费更高，因为 Bright Data 需要投入更多资源进行解锁。更多关于高级域名的信息请在 Browser API 配置页面查看。
  </Accordion>

  <Accordion title="如何降低 Browser API 的数据和带宽消耗？">
    为减少带宽使用并提高抓取效率，您可以：

    * 使用请求拦截或 CDP 自定义功能阻止不必要的资源，如图片、样式表和广告
    * 利用浏览器缓存
    * 遵循请求管理最佳实践

    实用技巧和代码示例请参阅我们的[**带宽优化指南**](/cn/scraping-automation/scraping-browser/code-examples#optimizing-bandwidth-usage-with-browser-api)<br />关于使用 CDP 自定义功能阻止广告的说明和代码，请参阅我们的自定义\*\*[广告拦截器](/cn/scraping-automation/scraping-browser/cdp-functions/custom#如何拦截广告)。\*\*
  </Accordion>

  <Accordion title="是否允许在 Browser API 中输入密码？">
    Bright Data 致力于仅收集公开可用的数据。为了遵守这一承诺，Browser API 默认配置为阻止任何尝试登录账户的操作，从而禁用密码输入。此限制有助于确保不会抓取任何非公开数据——包括仅在登录后才能访问的数据。如需参考，请查看我们的 [可接受使用政策](https://www.bright.cn/acceptable-use-policy) 。

    在某些情况下，可能可以覆盖此默认限制。如果您需要例外，必须首先完成我们的 [KYC（了解你的客户）流程](https://www.bright.cn/cp/kyc)。完成流程后，请直接联系我们的合规部门 [compliance@brightdata.com](mailto:compliance@brightdata.com) 提交请求（您也可以在 KYC 流程中一并申请权限）。
  </Accordion>

  <Accordion title="如何在 Browser API 会话中保持相同的 IP 地址？">
    Browser API 支持通过自定义 CDP 函数在多个浏览器会话中保持相同的 IP 地址。这允许您通过将连续请求关联到同一会话 ID 来重用同一个代理节点。

    有关实现细节和示例代码，请参阅我们的 [会话持久化文档](/cn/scraping-automation/scraping-browser/cdp-functions/custom#如何保持会话)
  </Accordion>

  <Accordion title="将代理集成到自动化脚本与使用 Browser API 有何不同？">
    **1. 将代理集成到自动化脚本**

    * 您在自己的脚本中直接设置代理，使用工具如 Puppeteer、Playwright 或 Selenium。
    * 您负责管理所有内容：浏览器设置、会话、扩展、反反爬挑战（CAPTCHA、指纹、请求头等）。
    * 提供完全控制和灵活性，但您需自行维护和排查所有复杂问题，包括解封和可扩展性。

    **2. 使用 Browser API**

    * 您将自动化脚本连接到运行在 Bright Data 云端的托管浏览器。
    * Bright Data 处理基础设施、扩展、反反爬/解封（CAPTCHA、指纹等）和代理轮换。
    * 您只需专注于抓取逻辑。对于复杂互动网站，更易于扩展。
    * 如果希望强大抓取而无需维护或构建自己的反反爬解决方案，这是理想选择。

    **总结：**
    通过直接代理集成，您掌控一切但需管理复杂性。使用 Browser API，Bright Data 处理最难的部分，您只需编写抓取流程。

    更多详情请参阅 [Browser API 介绍](/scraping-automation/scraping-browser/introduction)。
  </Accordion>

  <Accordion title="如何让 Browser API 抓取更快？">
    Browser API 的性能和优化由我们管理。我们一直致力于提升速度和可靠性。用户无法直接调整浏览器速度。

    在脚本中阻止不必要的网络请求（如图片、广告和分析脚本）可以减少数据使用，有时可能提升页面加载速度，但不保证更快加载。最可靠的好处是节省带宽。

    更多详情和示例代码，请参阅我们的 [带宽优化指南](/scraping-automation/scraping-browser/code-examples#optimizing-bandwidth-usage-with-browser-api)。
  </Accordion>

  <Accordion title="如何知道 Browser API 使用的代理类型？">
    默认情况下，Browser API 使用住宅代理（Residential proxies）。对于某些需要 KYC 的域名，如果需要合规，它可能会自动切换为数据中心代理（Datacenter proxies）。

    了解更多关于 KYC 和住宅代理访问的信息，请参阅 [这里](/proxy-networks/residential/network-access)。

    <Note>
      链接页面涵盖了住宅代理访问和 KYC 要求。关于 SSL 错误和其他代理类型的一些细节不适用于 Browser API。
    </Note>
  </Accordion>

  <Accordion title="如何使用 Playwright、Puppeteer 或 Selenium 连接 Browser API？">
    要连接 Browser API，您需要区域用户名和密码。

    * 对于 Playwright 和 Puppeteer，请使用 WebSocket (`wss://`) 端点连接，主机为 `brd.superproxy.io`，端口为 `9222`。
      * **示例连接 URL：**
        `wss://${AUTH}@brd.superproxy.io:9222`
    * 对于 Selenium，请使用 HTTPS 端点连接，主机为 `brd.superproxy.io`，端口为 `9515`。
      * **示例连接 URL：**
        `https://${AUTH}@brd.superproxy.io:9515`

    请参阅 [配置页面](/scraping-automation/scraping-browser/configuration) 获取使用各库连接的示例代码，并在连接 URL 中使用您的区域用户名和密码。

    <Warning>
      不要向设置中添加额外或自定义连接选项，这可能会破坏连接或降低性能。只需使用提供的 WebSocket 或 HTTPS 端点及您的区域凭证即可。
    </Warning>

    <Note>
      目前，连接 Browser API 的唯一方式是使用区域凭证（用户名和密码）的 WebSocket 或 HTTPS 端点。当前没有 REST API 连接方法。
    </Note>
  </Accordion>

  <Accordion title="代理 vs. Browser API，有何区别？我该使用哪个端点？">
    * 普通代理网络：
      您自行启动浏览器/进程，通过 `brd.superproxy.io:44445` 路由流量，并使用 `brd-customer-<CID>-zone-<ZONE>:<PASSWORD>` 进行认证。
    * Browser API（前称 Scraping Browser）：
      Bright Data 为您启动托管的云端 Chrome。您 **不** 启动 `puppeteer.launch()`，而是连接到远程浏览器：

    <CodeGroup>
      ```sh NodeJS, Puppeteer theme={null}
      const puppeteer = require('puppeteer-core');

      const AUTH = 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD';      // 在 Browser API Zone → Overview 中找到
      const WS  = `wss://${AUTH}@brd.superproxy.io:9222`; 

      (async () => {
          const browser = await puppeteer.connect({browserWSEndpoint: WS});
          const page = await browser.newPage();
          await page.goto('https://example.com', {timeout: 2*60*1000});
          console.log(await page.title());
          await browser.close();
      })(); 
      ```
    </CodeGroup>
  </Accordion>

  <Accordion title="我可以在单个 Browser API 会话中导航到多个 URL 吗？">
    可以 - Browser API 会话支持在同一域名内进行无限次导航。您可以在整个会话期间自由地在页面之间导航、点击链接、提交表单、滚动以及执行其他交互操作，只要所有导航都保持在同一域名内即可。

    若要在不同域名上启动抓取任务，您需要开始一个新会话。
  </Accordion>
</AccordionGroup>
