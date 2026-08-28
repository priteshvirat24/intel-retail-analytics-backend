> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Browser API 故障排除

> 获取 Bright Data Browser API 的故障排除技巧。 了解如何使用调试器，以及如何使用 Chrome 开发工具分析和优化网络抓取。

## Browser API Debugger

网络抓取项目通常需要与目标网站进行复杂的交互，调试对于识别和解决开发过程中发现的问题至关重要。 Browser API Debugger 是一项宝贵的资源，它使您能够与 Chrome 浏览器开发工具一起检查、分析和微调代码，从而实现更好的控制、可见性和效率。

### 在哪里可以找到

可通过以下两种方法启动我们的 Browser API Debugger：

1. 通过控制面板手动启动
2. 通过脚本远程启动

请在下面选择您喜欢的方式，了解更多信息：

<Tabs>
  <Tab title="通过控制面板手动启动">
    可以在 Bright Data 控制面板中轻松访问 Browser API Debugger。 请按照以下步骤操作：

    1. 在控制面板中，转到我的代理视图
    2. 点击您的 Browser API 代理
    3. 点击访问参数选项卡
    4. 在右侧点击 “Chrome 开发工具调试器”按钮

    <Frame>
      <img src="https://mintcdn.com/brightdata/S8tFtc_KJjCQxqv1/images/scraping-automation/scraping-browser/features/debugger/chrome-devtools-debugger.png?fit=max&auto=format&n=S8tFtc_KJjCQxqv1&q=85&s=af311142afae46229a68bcacfb2f4962" alt="chrome-devtools-debugger.png" width="1111" height="626" data-path="images/scraping-automation/scraping-browser/features/debugger/chrome-devtools-debugger.png" />
    </Frame>

    ### Debugger 和 Chrome 开发工具入门

    <Steps>
      <Step title="打开 Browser API 会话">
        * 确保有一个活跃的 Browser API 会话
        * 如果您还不知道如何启动 Browser API 会话，请参阅我们的快速入门指南。
      </Step>

      <Step title="启动 Debugger">
        * 会话启动并运行后，就可以启动 Debugger 了。
        * 点击访问参数选项卡中的 Debugger 按钮，启动 Browser API Debugger 界面（参见上面的截图）
      </Step>

      <Step title="连接您的实时浏览器会话">
        * 在 Debugger 界面中，您将看到实时 Browser API 会话的列表。
        * 选择要调试的首选会话
        * 点击会话链接或将其复制/粘贴到所选浏览器中，这将在 Debugger 和所选会话之间建立连接。

        <Frame>
          <img src="https://mintcdn.com/brightdata/S8tFtc_KJjCQxqv1/images/scraping-automation/scraping-browser/features/debugger/all-set.png?fit=max&auto=format&n=S8tFtc_KJjCQxqv1&q=85&s=e4b32702bf177b6c91b8b1c245468197" alt="" width="825" height="496" data-path="images/scraping-automation/scraping-browser/features/debugger/all-set.png" />
        </Frame>
      </Step>
    </Steps>
  </Tab>

  <Tab title="通过脚本远程启动">
    要直接从你的脚本访问并启动调试器会话，你需要发送 CDP 命令：`Page.inspect`。

    请参阅以下示例：

    <CodeGroup>
      ```js NodeJS theme={null}
      // Puppeteer - Inspect page using devtools
      const page = await browser.newPage();
      const client = await page.target().createCDPSession();
      const {frameTree: {frame}} = await client.send('Page.getFrameTree', {});
      const {url: inspectUrl} = await client.send('Page.inspect', {
          frameId: frame.id,
      });
      console.log(`Inspect session at ${inspectUrl}`);

      // Playwright - Inspect page using devtools
      const page = await browser.newPage();
      const client = await page.context().newCDPSession(page);
      const {frameTree: {frame}} = await client.send('Page.getFrameTree', {});
      const {url: inspectUrl} = await client.send('Page.inspect', {
          frameId: frame.id,
      });
      console.log(`Inspect session at ${inspectUrl}`);
      ```

      ```python Python theme={null}
      # Playwright - Inspect page using devtools
      page = await browser.new_page()
      client = await page.context.new_cdp_session(page)
      frame_tree = await client.send('Page.getFrameTree', {})
      frame_id = frame_tree['frameTree']['frame']['id']
      inspect = await client.send('Page.inspect', {'frameId': frame_id})
      inspect_url = inspect['url']
      print('Inspect session at', inspect_url)
      ```

      ```cs C# theme={null}
      // PuppeteerSharp - Inspect page using devtools
      var page = await browser.NewPageAsync();
      var client = await page.Target.CreateCDPSessionAsync();
      var frameTree = await client.SendAsync("Page.getFrameTree");
      var frameId = frameTree!["frameTree"]!["frame"]!["id"]!;
      var inspect = await client.SendAsync("Page.inspect", new { frameId = frameId });
      var inspectUrl = inspect["url"]!;
      Console.WriteLine($"Inspect session at {inspectUrl}");

      // Playwright - Inspect page using devtools
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

### 利用 Chrome 开发工具

* 将 Browser API Debugger 连接到实时会话后，您就可以使用 Chrome 开发工具的强大功能了。
* 利用开发工具界面检查 HTML 元素、分析网络请求、调试 JavaScript 代码并监控性能。 利用断点、控制台日志和其他调试技术来识别和解决代码中的问题。

<Frame>
  <img src="https://mintcdn.com/brightdata/S8tFtc_KJjCQxqv1/images/scraping-automation/scraping-browser/features/debugger/test-sites.png?fit=max&auto=format&n=S8tFtc_KJjCQxqv1&q=85&s=e4ae617f25eafd7b2a7253841583609b" alt="test-sites.png" width="955" height="411" data-path="images/scraping-automation/scraping-browser/features/debugger/test-sites.png" />
</Frame>

### 在本地自动启动开发工具以查看实时浏览器会话

如果您想在每次会话中自动启动开发工具以查看实时浏览器会话，可以集成以下代码片段：

```js NodeJS - Puppeteer theme={null}
// Launch devtools locally

const { exec } = require('child_process');
const chromeExecutable = 'google-chrome';

const delay = ms => new Promise(resolve => setTimeout(resolve, ms));
const openDevtools = async (page, client) => {
    // get current frameId
    const frameId = page.mainFrame()._id;
    // get URL for devtools from Browser API
    const { url: inspectUrl } = await client.send('Page.inspect', { frameId });
    // open devtools URL in local chrome
    exec(`"${chromeExecutable}" "${inspectUrl}"`, error => {
        if (error)
            throw new Error('Unable to open devtools: ' + error);
    });
    // wait for devtools ui to load
    await delay(5000);
};

const page = await browser.newPage();
const client = await page.target().createCDPSession();
await openDevtools(page, client);
await page.goto('http://example.com');
```

### Debugger 演示

下面就来看看 Browser API Debugger 的运行情况

<Frame>
  <iframe width="660" height="350" src="https://www.youtube.com/embed/68Kom7tS-QY" title="Debugger 演示" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />
</Frame>

## 错误代码

查看 [Browser API 错误代码完整列表](/cn/scraping-automation/scraping-browser/error-codes)，包含每个代码的含义以及建议的操作。

## 常见问题解答

查看我们关于 Browser API 的 [常见问题解答](/cn/scraping-automation/scraping-browser/faqs)

## 怎么做

了解更多关于浏览器自动化的 [常用库导航函数](/cn/scraping-automation/scraping-browser/code-examples) 以及专门针对 Browser API 的示例
