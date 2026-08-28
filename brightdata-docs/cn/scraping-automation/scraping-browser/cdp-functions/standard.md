> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 标准CDP函数

> 了解 Scraping Brower 的基本 CDP 函数，从 cookie 设置到国家/地区定位。 学习使用这些常见的 Puppeteer 和 Playwright 命令来优化网络抓取。

Scraping Brower 支持 CDP，因此所有 `puppeteer` 函数/功能都可以在我们的浏览器中运行。您可以在puppeteer官方文档页面上找到所有 [puppeteer API 文档](https://pptr.dev/)和使用示例。我们还添加了一些Bright Data特定[的自定义CDP事件](/scraping-automation/scraping-browser/cdp-functions/custom)，这些事件也非常有用。

下文介绍一些常见的浏览器导航函数，可帮助您入门。

<AccordionGroup>
  <Accordion title="获取页面HTML">
    ```js NodeJS - Puppeteer theme={null}
    const page = await browser.newPage();  
    await page.goto('https://example.com');  
    const html = await page.content();
    ```

    更多信息请见: [https://pptr.dev/api/puppeteer.page.content](https://pptr.dev/api/puppeteer.page.content)
  </Accordion>

  <Accordion title="点击元素">
    ```js NodeJS - Puppeteer theme={null}
    // node.js puppeteer   
    const page = await page.newPage();  
    await page.goto('https://example.com');  
    await page.click('a[href]');
    ```

    更多信息请见: [https://pptr.dev/api/puppeteer.page.click](https://pptr.dev/api/puppeteer.page.click)
  </Accordion>

  <Accordion title="滚动到页面底部">
    有时您可能需要将视窗滚动到底部，例如激活“无限滚动”时。具体方法如下：

    ```js NodeJS - Puppeteer theme={null}
    // node.js puppeteer   
    const page = await page.newPage();  
    await page.goto('https://example.com');  
    await page.evaluate(()=>window.scrollBy(0, window.innerHeight));
    ```
  </Accordion>

  <Accordion title="截屏">
    <CodeGroup>
      ```js NodeJS - Puppeteer theme={null}
      // More info at https://pptr.dev/api/puppeteer.page.screenshot  
      await page.screenshot({ path: 'screenshot.png', fullPage: true });
      ```

      ```python Python - Playwright theme={null}
      # More info at <https://playwright.dev/python/docs/screenshots>  
      await page.screenshot(path='screenshot.png', full_page=True)
      ```

      ```cs C# - PuppeteerSharp theme={null}
      await page.ScreenshotAsync("screenshot.png", new ()  
      {  
          FullPage = true,  
      });
      ```
    </CodeGroup>

    <Note>
      运行上述示例脚本时，以上屏幕截图将作为“screenshot.png”保存在您的文件中。
    </Note>
  </Accordion>

  <Accordion title="设置Cookie">
    请注意，此功能仅支持完成KYC验证流程的客户。

    ```js NodeJS Puppeteer theme={null}
    const page = await browser.newPage();  
    await page.setCookie({name: 'LANG', value: 'en-US', domain: 'example.com'});  
    await page.goto('https://example.com');
    ```

    更多信息请见：[https://pptr.dev/api/puppeteer.page.setcookie](https://pptr.dev/api/puppeteer.page.setcookie)
  </Accordion>

  <Accordion title="屏蔽端点">
    可以屏蔽不需要的端点以节省带宽。 请参阅下面的相关示例：

    ```js NodeJS - Puppeteer theme={null}
    // connect to a remote browser...
    const blockedUrls = ['*doubleclick.net*'];
    const page = await browser.newPage();
    const client = await page.target().createCDPSession();
    await client.send('Network.enable');
    await client.send('Network.setBlockedURLs', {urls: blockedUrls});
    await page.goto('https://washingtonpost.com');
    ```
  </Accordion>

  <Accordion title="国家/地区定位">
    使用 Scraping Brower 时，可使用与我们的其他代理产品相同的国家/地区定位参数。

    设置脚本时，在 Bright Data 端点的 “USER” 凭据后添加`-country`标志，然后添加该国家/地区的2个字母的 [ISO代码](https://www.nationsonline.org/oneworld/country_code_list.htm)。

    ```js theme={null}
    const SBR_WS_ENDPOINT = `wss://${USER-country-us:PASS}@brd.superproxy.io:9222`;
    ```

    在以上示例中，我们在脚本中的Bright Data端点添加了-country-us，因此我们的请求将来自美国(“us”)。

    #### 欧盟地区

    您可以按照与上文“国家/地区”相同的方式定位整个欧盟地区，只需在请求中的“country”后添加“eu”即可: `-country-eu`

    使用`-country-eu`发送的请求将使用来自以下某一国家/地区的IP，这些国家/地区将自动包含在 “eu” 境内:

    ```sh 国家/地区 theme={null}
    AL、AZ、KG、BA、UZ、BI、XK、SM、DE、AT、CH、UK、GB、IE、IM、FR、ES、NL、IT、PT、BE、AD、MT、MC、MA、LU、TN、DZ、GI、LI、SE、DK、FI、NO、AX、IS、GG、JE、EU、GL、VA、FX、FO
    ```

    <Note>
      欧盟国家/地区的分配是随机的。
    </Note>
  </Accordion>
</AccordionGroup>
