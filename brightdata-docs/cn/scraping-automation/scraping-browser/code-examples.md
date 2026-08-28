> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 浏览器 API 代码示例

> 通过详细代码示例，探索如何使用 Bright Data 的浏览器 API 与各种技术（包括 Playwright、Puppeteer 和 Selenium）配合使用。

下面是浏览器 API 在各种场景和库中的使用示例。

<Warning>
  请确保在继续之前安装所需的库
</Warning>

## 几分钟内发出您的第一个请求

使用这些现成的代码示例，您可以在几分钟内测试浏览器 API。

<CardGroup cols={3}>
  <Card title="Nodejs Puppeteer 示例" icon="code" iconType="regular" href="https://github.com/luminati-io/bright-data-scraping-browser-nodejs-puppeteer-project" cta="在不到 2 分钟内尝试浏览器 API" />

  <Card title="Node.js Playwright 示例" icon="code" iconType="regular" href="https://github.com/luminati-io/bright-data-scraping-browser-nodejs-playwright-project" cta="在不到 2 分钟内尝试浏览器 API" />

  <Card title="Node.js Selenium 示例" icon="code" iconType="regular" href="https://github.com/luminati-io/bright-data-scraping-browser-nodejs-selenium-project" cta="在不到 2 分钟内尝试浏览器 API" />
</CardGroup>

<Tabs>
  <Tab title="基础">
    对目标页面进行简单爬取

    ### 选择您偏好的技术栈

    <Tabs>
      <Tab title="NodeJS">
        <CodeGroup>
          ```js Playwright theme={null}
          #!/usr/bin/env node
          const playwright = require('playwright');
          const {
              AUTH = 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD',
              TARGET_URL = 'https://example.com',
          } = process.env;

          async function scrape(url = TARGET_URL) {
              if (AUTH == 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD') {
                  throw new Error(`Provide Browser API credentials in AUTH`
                      + ` environment variable or update the script.`);
              }
              console.log(`Connecting to Browser...`);
              const endpointURL = `wss://${AUTH}@brd.superproxy.io:9222`;
              const browser = await playwright.chromium.connectOverCDP(endpointURL);
              try {
                  console.log(`Connected! Navigating to ${url}...`);
                  const page = await browser.newPage();
                  await page.goto(url, { timeout: 2 * 60 * 1000 });
                  console.log(`Navigated! Scraping page content...`);
                  const data = await page.content();
                  console.log(`Scraped! Data: ${data}`);
              } finally {
                  await browser.close();
              }
          }

          if (require.main == module) {
              scrape().catch(error => {
                  console.error(error.stack || error.message || error);
                  process.exit(1);
              });
          }
          ```

          ```js Puppeteer theme={null}
          #!/usr/bin/env node
          const puppeteer = require('puppeteer-core');
          const {
              AUTH = 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD',
              TARGET_URL = 'https://example.com',
          } = process.env;

          async function scrape(url = TARGET_URL) {
              if (AUTH == 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD') {
                  throw new Error(`Provide Browser API credentials in AUTH`
                      + ` environment variable or update the script.`);
              }
              console.log(`Connecting to Browser...`);
              const browserWSEndpoint = `wss://${AUTH}@brd.superproxy.io:9222`;
              const browser = await puppeteer.connect({ browserWSEndpoint });
              try {
                  console.log(`Connected! Navigating to ${url}...`);
                  const page = await browser.newPage();
                  await page.goto(url, { timeout: 2 * 60 * 1000 });
                  console.log(`Navigated! Scraping page content...`);
                  const data = await page.content();
                  console.log(`Scraped! Data: ${data}`);
              } finally {
                  await browser.close();
              }
          }

          function getErrorDetails(error) {
              if (error.target?._req?.res) {
                  const {
                      statusCode,
                      statusMessage,
                  } = error.target._req.res;
                  return `Unexpected Server Status ${statusCode}: ${statusMessage}`;
              }
          }

          if (require.main == module) {
              scrape().catch(error => {
                  console.error(getErrorDetails(error)
                      || error.stack
                      || error.message
                      || error);
                  process.exit(1);
              });
          }
          ```

          ```js Selenium theme={null}
          #!/usr/bin/env node
          const { Builder, Browser } = require('selenium-webdriver');
          const {
              AUTH = 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD',
              TARGET_URL = 'https://example.com',
          } = process.env;

          async function scrape(url = TARGET_URL) {
              if (AUTH == 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD') {
                  throw new Error(`Provide Browser API credentials in AUTH`
                      + ` environment variable or update the script.`);
              }
              console.log(`Connecting to Browser...`);
              const server = `https://${AUTH}@brd.superproxy.io:9515`;
              const driver = await new Builder()
                  .forBrowser(Browser.CHROME)
                  .usingServer(server)
                  .build();
              try {
                  console.log(`Connected! Navigating to ${url}...`);
                  await driver.get(url);
                  console.log(`Navigated! Scraping page content...`);
                  const data = await driver.getPageSource();
                  console.log(`Scraped! Data: ${data}`);
              } finally {
                  await driver.quit();
              }
          }

          if (require.main == module) {
              scrape().catch(error => {
                  console.error(error.stack || error.message || error);
                  process.exit(1);
              });
          }
          ```
        </CodeGroup>
      </Tab>

      <Tab title="Python">
        <CodeGroup>
          ```python Playwright - Async theme={null}
          #!/usr/bin/env python3
          import asyncio
          from os import environ
          from playwright.async_api import Playwright, async_playwright

          AUTH = environ.get('AUTH', default='SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD')
          TARGET_URL = environ.get('TARGET_URL', default='https://example.com')


          async def scrape(playwright: Playwright, url=TARGET_URL):
              if AUTH == 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD':
                  raise Exception('Provide Browser API credentials in AUTH ' +
                                  'environment variable or update the script.')
              print('Connecting to Browser...')
              endpoint_url = f'wss://{AUTH}@brd.superproxy.io:9222'
              browser = await playwright.chromium.connect_over_cdp(endpoint_url)
              try:
                  print(f'Connected! Navigating to {url}...')
                  page = await browser.new_page()
                  await page.goto(url, timeout=2*60_000)
                  print('Navigated! Scraping page content...')
                  data = await page.content()
                  print(f'Scraped! Data: {data}')
              finally:
                  await browser.close()


          async def main():
              async with async_playwright() as playwright:
                  await scrape(playwright)


          if __name__ == '__main__':
              asyncio.run(main())

          ```

          ```python Playwright - Sync theme={null}
          #!/usr/bin/env python3
          from os import environ
          from playwright.sync_api import Playwright, sync_playwright

          AUTH = environ.get('AUTH', default='SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD')
          TARGET_URL = environ.get('TARGET_URL', default='https://example.com')


          def scrape(playwright: Playwright, url=TARGET_URL):
              if AUTH == 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD':
                  raise Exception('Provide Browser API credentials in AUTH ' +
                                  'environment variable or update the script.')
              print('Connecting to Browser...')
              endpoint_url = f'wss://{AUTH}@brd.superproxy.io:9222'
              browser = playwright.chromium.connect_over_cdp(endpoint_url)
              try:
                  print(f'Connected! Navigating to {url}...')
                  page = browser.new_page()
                  page.goto(url, timeout=2*60_000)
                  print('Navigated! Scraping page content...')
                  data = page.content()
                  print(f'Scraped! Data: {data}')
              finally:
                  browser.close()


          def main():
              with sync_playwright() as playwright:
                  scrape(playwright)


          if __name__ == '__main__':
              main()

          ```

          ```python Selenium theme={null}
          #!/usr/bin/env python3
          from os import environ
          from selenium.webdriver import Remote, ChromeOptions as Options
          from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection as Connection

          AUTH = environ.get('AUTH', default='SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD')
          TARGET_URL = environ.get('TARGET_URL', default='https://example.com')


          def scrape(url=TARGET_URL):
              if AUTH == 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD':
                  raise Exception('Provide Browser API credentials in AUTH ' +
                                  'environment variable or update the script.')
              print('Connecting to Browser...')
              server_addr = f'https://{AUTH}@brd.superproxy.io:9515'
              connection = Connection(server_addr, 'goog', 'chrome')
              driver = Remote(connection, options=Options())
              try:
                  print(f'Connected! Navigating to {url}...')
                  driver.get(url)
                  print('Navigated! Scraping page content...')
                  data = driver.page_source
                  print(f'Scraped! Data: {data}')
              finally:
                  driver.quit()


          if __name__ == '__main__':
              scrape()

          ```

          ```python Selenium - Mobile-agent theme={null}
          #!/usr/bin/env python3 
          from os import environ 
          from selenium.webdriver import Remote, ChromeOptions as Options 
          from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection as Connection 

          AUTH = environ.get('AUTH', default='SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD') 
          TARGET_URL = environ.get('TARGET_URL', default='https://httpbin.org/user-agent') 
          USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1' 
          SCREEN_WIDTH = 390 
          SCREEN_HEIGHT = 844 
          DEVICE_SCALE_FACTOR = 3 

          def scrape(url=TARGET_URL): 
              if AUTH == 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD': 
                  raise Exception('Provide Browser API credentials in AUTH ' + 
                                  'environment variable or update the script.') 
              print('Connecting to Browser...') 
              server_addr = f'https://{AUTH}@brd.superproxy.io:9515' 
              connection = Connection(server_addr, 'goog', 'chrome') 
              driver = Remote(connection, options=Options()) 
              try: 
                  print(f'Connected! Emulating mobile...') 
                  driver.execute('executeCdpCommand', { 
                      'cmd': 'Emulation.setUserAgentOverride', 
                      'params': { 
                          'userAgent': USER_AGENT, 
                      }, 
                  }) 
                  driver.execute('executeCdpCommand', { 
                      'cmd': 'Emulation.setDeviceMetricsOverride', 
                      'params': { 
                          'width': SCREEN_WIDTH, 
                          'height': SCREEN_HEIGHT, 
                          'deviceScaleFactor': DEVICE_SCALE_FACTOR, 
                          'mobile': True, 
                      }, 
                  }) 
                  print(f'Navigating to {url}...') 
                  driver.get(url) 
                  print('Navigated! Checking screen and user-agent...') 
                  driver.get_screenshot_as_file('./page.png') 
                  ua = driver.execute_script('return navigator.userAgent') 
                  print(f'User-Agent is {ua}') 
              finally: 
                  driver.quit() 


          if __name__ == '__main__': 
              scrape()

          ```
        </CodeGroup>
      </Tab>

      <Tab title="C#">
        <CodeGroup>
          ```cs Puppeteer theme={null}
          using PuppeteerSharp;
          using System.Net.WebSockets;
          using System.Text;

          class Scraper
          {

              private string _auth;

              public Scraper(string auth)
              {
                  _auth = auth;
              }

              private async Task<IBrowser> Connect()
              {
                  if (_auth == "SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD")
                  {
                      throw new Exception("Provide Browser API credentials in AUTH"
                              + " environment variable or update the script.");
                  }
                  var options = new ConnectOptions()
                  {
                      BrowserWSEndpoint = "wss://brd.superproxy.io:9222",
                      WebSocketFactory = async (uri, options, cToken) =>
                      {
                          var socket = new ClientWebSocket();
                          var authBytes = Encoding.UTF8.GetBytes(_auth);
                          var authHeader = "Basic " + Convert.ToBase64String(authBytes);
                          socket.Options.SetRequestHeader("Authorization", authHeader);
                          socket.Options.KeepAliveInterval = TimeSpan.Zero;
                          await socket.ConnectAsync(uri, cToken);
                          return socket;
                      },
                  };
                  return await Puppeteer.ConnectAsync(options);
              }

              public async Task Scrape(string url)
              {
                  Log("Connecting to Browser...");
                  var browser = await Connect();
                  try {
                      Log($"Connected! Navigating to {url}...");
                      var page = await browser.NewPageAsync();
                      await page.GoToAsync(url, /* timeout= */ 2 * 60 * 1000);
                      Log("Navigated! Scraping page content...");
                      var data = await page.GetContentAsync();
                      Log($"Scraped! Data: {data}");
                  } finally {
                      await browser.CloseAsync();
                  }
              }

              private static string Env(string name, string defaultValue)
              {
                  return Environment.GetEnvironmentVariable(name) ?? defaultValue;
              }

              private static void Log(string message)
              {
                  Console.WriteLine(message);
              }

              public static async Task Main()
              {
                  var auth = Env("AUTH", "SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD");
                  var url = Env("TARGET_URL", "https://example.com");
                  var scraper = new Scraper(auth);
                  await scraper.Scrape(url);
              }

          }
          ```

          ```cs Selenium theme={null}
          using OpenQA.Selenium;
          using OpenQA.Selenium.Chrome;
          using OpenQA.Selenium.Remote;

          class Scraper
          {

              private string _auth;

              public Scraper(string auth)
              {
                  _auth = auth;
              }

              private IWebDriver Connect()
              {
                  if (_auth == "SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD")
                  {
                      throw new Exception("Provide Browser API credentials in AUTH"
                              + " environment variable or update the script.");
                  }
                  var uri = new Uri($"https://{_auth}@brd.superproxy.io:9515");
                  var executor = new HttpCommandExecutor(uri, TimeSpan.FromSeconds(60));
                  var cdpCommand = new HttpCommandInfo(HttpCommandInfo.PostCommand,
                          "/session/{sessionId}/goog/cdp/execute");
                  executor.TryAddCommand("cdp", cdpCommand);
                  var capabilities = new ChromeOptions().ToCapabilities();
                  return new RemoteWebDriver(executor, capabilities);
              }

              public void Scrape(string url)
              {
                  Log("Connecting to Browser...");
                  var driver = Connect();
                  try {
                      Log($"Connected! Navigating to {url}...");
                      driver.Navigate().GoToUrl(url);
                      Log("Navigated! Scraping page content...");
                      var data = driver.PageSource;
                      Log($"Scraped! Data: {data}");
                  } finally {
                      driver.Quit();
                  }
              }

              private static string Env(string name, string defaultValue)
              {
                  return Environment.GetEnvironmentVariable(name) ?? defaultValue;
              }

              private static void Log(string message)
              {
                  Console.WriteLine(message);
              }

              public static void Main()
              {
                  var auth = Env("AUTH", "SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD");
                  var url = Env("TARGET_URL", "https://example.com");
                  var scraper = new Scraper(auth);
                  scraper.Scrape(url);
              }

          }
          ```
        </CodeGroup>
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="验证码">
    打开页面并等待验证码解决

    ### 选择您偏好的技术栈

    <Tabs>
      <Tab title="NodeJS">
        <CodeGroup>
          ```js Playwright theme={null}
          #!/usr/bin/env node
          const playwright = require('playwright');
          const {
              AUTH = 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD',
              TARGET_URL = 'https://example.com',
          } = process.env;

          async function scrape(url = TARGET_URL) {
              if (AUTH == 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD') {
                  throw new Error(`Provide Browser API credentials in AUTH`
                      + ` environment variable or update the script.`);
              }
              console.log(`Connecting to Browser...`);
              const endpointURL = `wss://${AUTH}@brd.superproxy.io:9222`;
              const browser = await playwright.chromium.connectOverCDP(endpointURL);
              try {
                  console.log(`Connected! Navigating to ${url}...`);
                  const page = await browser.newPage();
                  const client = await page.context().newCDPSession(page);
                  await page.goto(url, { timeout: 2 * 60 * 1000 });
                  console.log(`Navigated! Waiting captcha to detect and solve...`);
                  const { status } = await client.send('Captcha.waitForSolve', {
                      detectTimeout: 10 * 1000,
                  });
                  console.log(`Captcha status: ${status}`);
              } finally {
                  await browser.close();
              }
          }

          if (require.main == module) {
              scrape().catch(error => {
                  console.error(error.stack || error.message || error);
                  process.exit(1);
              });
          }
          ```

          ```js Puppeteer theme={null}
          #!/usr/bin/env node
          const puppeteer = require('puppeteer-core');
          const {
              AUTH = 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD',
              TARGET_URL = 'https://example.com',
          } = process.env;

          async function scrape(url = TARGET_URL) {
              if (AUTH == 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD') {
                  throw new Error(`Provide Browser API credentials in AUTH`
                      + ` environment variable or update the script.`);
              }
              console.log(`Connecting to Browser...`);
              const browserWSEndpoint = `wss://${AUTH}@brd.superproxy.io:9222`;
              const browser = await puppeteer.connect({ browserWSEndpoint });
              try {
                  console.log(`Connected! Navigating to ${url}...`);
                  const page = await browser.newPage();
                  const client = await page.createCDPSession();
                  await page.goto(url, { timeout: 2 * 60 * 1000 });
                  console.log(`Navigated! Waiting captcha to detect and solve...`);
                  const { status } = await client.send('Captcha.waitForSolve', {
                      detectTimeout: 10 * 1000,
                  });
                  console.log(`Captcha status: ${status}`);
              } finally {
                  await browser.close();
              }
          }

          function getErrorDetails(error) {
              if (error.target?._req?.res) {
                  const {
                      statusCode,
                      statusMessage,
                  } = error.target._req.res;
                  return `Unexpected Server Status ${statusCode}: ${statusMessage}`;
              }
          }

          if (require.main == module) {
              scrape().catch(error => {
                  console.error(getErrorDetails(error)
                      || error.stack
                      || error.message
                      || error);
                  process.exit(1);
              });
          }
          ```

          ```js Selenium theme={null}
          #!/usr/bin/env node
          const { Builder, Browser } = require('selenium-webdriver');
          const {
              AUTH = 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD',
              TARGET_URL = 'https://example.com',
          } = process.env;

          async function scrape(url = TARGET_URL) {
              if (AUTH == 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD') {
                  throw new Error(`Provide Browser API credentials in AUTH`
                      + ` environment variable or update the script.`);
              }
              console.log(`Connecting to Browser...`);
              const server = `https://${AUTH}@brd.superproxy.io:9515`;
              const driver = await new Builder()
                  .forBrowser(Browser.CHROME)
                  .usingServer(server)
                  .build();
              try {
                  console.log(`Connected! Navigating to ${url}...`);
                  await driver.get(url);
                  console.log(`Navigated! Waiting captcha to detect and solve...`);
                  const { status } = await driver.sendAndGetDevToolsCommand('Captcha.waitForSolve', {
                      detectTimeout: 10000,
                  });
                  console.log(`Captcha status: ${status}`);
              } finally {
                  await driver.quit();
              }
          }

          if (require.main == module) {
              scrape().catch(error => {
                  console.error(error.stack || error.message || error);
                  process.exit(1);
              });
          }
          ```
        </CodeGroup>
      </Tab>

      <Tab title="Python">
        <CodeGroup>
          ```python Playwright - Async theme={null}
          #!/usr/bin/env python3
          import asyncio
          from os import environ
          from playwright.async_api import Playwright, async_playwright

          AUTH = environ.get('AUTH', default='SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD')
          TARGET_URL = environ.get('TARGET_URL', default='https://example.com')


          async def scrape(playwright: Playwright, url=TARGET_URL):
              if AUTH == 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD':
                  raise Exception('Provide Browser API credentials in AUTH ' +
                                  'environment variable or update the script.')
              print('Connecting to Browser...')
              endpoint_url = f'wss://{AUTH}@brd.superproxy.io:9222'
              browser = await playwright.chromium.connect_over_cdp(endpoint_url)
              try:
                  print(f'Connected! Navigating to {url}...')
                  page = await browser.new_page()
                  client = await page.context.new_cdp_session(page)
                  await page.goto(url, timeout=2*60_000)
                  print('Navigated! Waiting captcha to detect and solve...')
                  result = await client.send('Captcha.waitForSolve', {
                      'detectTimeout': 10 * 1000,
                  })
                  status = result['status']
                  print(f'Captcha status: {status}')
              finally:
                  await browser.close()


          async def main():
              async with async_playwright() as playwright:
                  await scrape(playwright)


          if __name__ == '__main__':
              asyncio.run(main())

          ```

          ```python Playwright - Sync theme={null}
          #!/usr/bin/env python3
          from os import environ
          from playwright.sync_api import Playwright, sync_playwright

          AUTH = environ.get('AUTH', default='SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD')
          TARGET_URL = environ.get('TARGET_URL', default='https://example.com')


          def scrape(playwright: Playwright, url=TARGET_URL):
              if AUTH == 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD':
                  raise Exception('Provide Browser API credentials in AUTH ' +
                                  'environment variable or update the script.')
              print('Connecting to Browser...')
              endpoint_url = f'wss://{AUTH}@brd.superproxy.io:9222'
              browser = playwright.chromium.connect_over_cdp(endpoint_url)
              try:
                  print(f'Connected! Navigating to {url}...')
                  page = browser.new_page()
                  client = page.context.new_cdp_session(page)
                  page.goto(url, timeout=2*60_000)
                  print('Navigated! Waiting captcha to detect and solve...')
                  result = client.send('Captcha.waitForSolve', {
                      'detectTimeout': 10 * 1000,
                  })
                  status = result['status']
                  print(f'Captcha status: {status}')
              finally:
                  browser.close()


          def main():
              with sync_playwright() as playwright:
                  scrape(playwright)


          if __name__ == '__main__':
              main()

          ```

          ```python Selenium theme={null}
          #!/usr/bin/env python3
          from os import environ
          from selenium.webdriver import Remote, ChromeOptions as Options
          from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection as Connection

          AUTH = environ.get('AUTH', default='SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD')
          TARGET_URL = environ.get('TARGET_URL', default='https://example.com')


          def scrape(url=TARGET_URL):
              if AUTH == 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD':
                  raise Exception('Provide Browser API credentials in AUTH ' +
                                  'environment variable or update the script.')
              print('Connecting to Browser...')
              server_addr = f'https://{AUTH}@brd.superproxy.io:9515'
              connection = Connection(server_addr, 'goog', 'chrome')
              driver = Remote(connection, options=Options())
              try:
                  print(f'Connected! Navigating to {url}...')
                  driver.get(url)
                  print('Navigated! Waiting captcha to detect and solve...')
                  result = driver.execute('executeCdpCommand', {
                      'cmd': 'Captcha.waitForSolve',
                      'params': {'detectTimeout': 10 * 1000},
                  })
                  status = result['value']['status']
                  print(f'Captcha status: {status}')
              finally:
                  driver.quit()


          if __name__ == '__main__':
              scrape()

          ```
        </CodeGroup>
      </Tab>

      <Tab title="C#">
        <CodeGroup>
          ```cs Puppeteer theme={null}
          using PuppeteerSharp;
          using System.Net.WebSockets;
          using System.Text;

          class Scraper
          {

              private string _auth;

              public Scraper(string auth)
              {
                  _auth = auth;
              }

              private async Task<IBrowser> Connect()
              {
                  if (_auth == "SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD")
                  {
                      throw new Exception("Provide Browser API credentials in AUTH"
                              + " environment variable or update the script.");
                  }
                  var options = new ConnectOptions()
                  {
                      BrowserWSEndpoint = "wss://brd.superproxy.io:9222",
                      WebSocketFactory = async (uri, options, cToken) =>
                      {
                          var socket = new ClientWebSocket();
                          var authBytes = Encoding.UTF8.GetBytes(_auth);
                          var authHeader = "Basic " + Convert.ToBase64String(authBytes);
                          socket.Options.SetRequestHeader("Authorization", authHeader);
                          socket.Options.KeepAliveInterval = TimeSpan.Zero;
                          await socket.ConnectAsync(uri, cToken);
                          return socket;
                      },
                  };
                  return await Puppeteer.ConnectAsync(options);
              }

              public async Task Scrape(string url)
              {
                  Log("Connecting to Browser...");
                  var browser = await Connect();
                  try {
                      Log($"Connected! Navigating to {url}...");
                      var page = await browser.NewPageAsync();
                      var client = await page.Target.CreateCDPSessionAsync();
                      await page.GoToAsync(url, /* timeout= */ 2 * 60 * 1000);
                      Log("Navigated! Waiting captcha to detect and solve...");
                      var result = await client.SendAsync("Captcha.waitForSolve", new
                      {
                          detectTimeout = 10 * 1000,
                      });
                      var status = (string) result["status"]!;
                      Log($"Captcha status: {status}");
                  } finally {
                      await browser.CloseAsync();
                  }
              }

              private static string Env(string name, string defaultValue)
              {
                  return Environment.GetEnvironmentVariable(name) ?? defaultValue;
              }

              private static void Log(string message)
              {
                  Console.WriteLine(message);
              }

              public static async Task Main()
              {
                  var auth = Env("AUTH", "SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD");
                  var url = Env("TARGET_URL", "https://example.com");
                  var scraper = new Scraper(auth);
                  await scraper.Scrape(url);
              }

          }
          ```

          ```cs Selenium theme={null}
          using OpenQA.Selenium;
          using OpenQA.Selenium.Chrome;
          using OpenQA.Selenium.Remote;

          class Scraper
          {

              private string _auth;

              public Scraper(string auth)
              {
                  _auth = auth;
              }

              private WebDriver Connect()
              {
                  if (_auth == "SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD")
                  {
                      throw new Exception("Provide Browser API credentials in AUTH"
                              + " environment variable or update the script.");
                  }
                  var uri = new Uri($"https://{_auth}@brd.superproxy.io:9515");
                  var executor = new HttpCommandExecutor(uri, TimeSpan.FromSeconds(60));
                  var cdpCommand = new HttpCommandInfo(HttpCommandInfo.PostCommand,
                          "/session/{sessionId}/goog/cdp/execute");
                  executor.TryAddCommand("cdp", cdpCommand);
                  var capabilities = new ChromeOptions().ToCapabilities();
                  return new RemoteWebDriver(executor, capabilities);
              }

              public void Scrape(string url)
              {
                  Log("Connecting to Browser...");
                  var driver = Connect();
                  try {
                      Log($"Connected! Navigating to {url}...");
                      driver.Navigate().GoToUrl(url);
                      Log("Navigated! Waiting captcha to detect and solve...");
                      var result = (Dictionary<string, object>) driver.ExecuteCustomDriverCommand("cdp", new ()
                      {
                          {"cmd", "Captcha.solve"},
                          {"params", new Dictionary<string, object>(){
                              {"detectTimeout", 10000},
                          }},
                      }) as Dictionary<string, object>;
                      var status = (string) result!["status"];
                      Log($"Captcha status: {status}");
                  } finally {
                      driver.Quit();
                  }
              }

              private static string Env(string name, string defaultValue)
              {
                  return Environment.GetEnvironmentVariable(name) ?? defaultValue;
              }

              private static void Log(string message)
              {
                  Console.WriteLine(message);
              }

              public static void Main()
              {
                  var auth = Env("AUTH", "SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD");
                  var url = Env("TARGET_URL", "https://example.com");
                  var scraper = new Scraper(auth);
                  scraper.Scrape(url);
              }

          }

          ```
        </CodeGroup>
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="高级">
    检查爬取会话，使用 JS 代码片段进行高级爬取

    ### 选择您偏好的技术栈

    <Tabs>
      <Tab title="NodeJS">
        <CodeGroup>
          ```js Playwright theme={null}
          #!/usr/bin/env node
          const playwright = require('playwright');
          const {
              AUTH = 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD',
              TARGET_URL = 'https://example.com',
          } = process.env;

          async function scrape(url = TARGET_URL) {
              if (AUTH == 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD') {
                  throw new Error(`Provide Browser API credentials in AUTH`
                      + ` environment variable or update the script.`);
              }
              console.log(`Connecting to Browser...`);
              const endpointURL = `wss://${AUTH}@brd.superproxy.io:9222`;
              const browser = await playwright.chromium.connectOverCDP(endpointURL);
              try {
                  console.log(`Connected! Starting inspect session...`);
                  const page = await browser.newPage();
                  const client = await page.context().newCDPSession(page);
                  const { frameTree: { frame } } = await client.send('Page.getFrameTree');
                  const { url: inspectUrl } = await client.send('Page.inspect', {
                      frameId: frame.id,
                  });
                  console.log(`You can inspect this session at: ${inspectUrl}.`);
                  console.log(`Scraping will continue in 10 seconds...`);
                  await sleep(10);
                  console.log(`Navigating to ${url}...`);
                  await page.goto(url, { timeout: 2 * 60 * 1000 });
                  console.log(`Navigated! Scraping paragraphs...`);
                  const data = await page.$$eval('p', els => els.map(el => el.innerText));
                  console.log(`Scraped! Data:`, data);
                  console.log(`Session will be closed in 1 minute...`);
                  await sleep(60);
              } finally {
                  console.log(`Closing session.`);
                  await browser.close();
              }
          }

          function sleep(seconds) {
              return new Promise(resolve => setTimeout(resolve, seconds * 1000));
          }

          if (require.main == module) {
              scrape().catch(error => {
                  console.error(error.stack || error.message || error);
                  process.exit(1);
              });
          }
          ```

          ```js Puppeteer theme={null}
          #!/usr/bin/env node
          const puppeteer = require('puppeteer-core');
          const {
              AUTH = 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD',
              TARGET_URL = 'https://example.com',
          } = process.env;

          async function scrape(url = TARGET_URL) {
              if (AUTH == 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD') {
                  throw new Error(`Provide Browser API credentials in AUTH`
                      + ` environment variable or update the script.`);
              }
              console.log(`Connecting to Browser...`);
              const browserWSEndpoint = `wss://${AUTH}@brd.superproxy.io:9222`;
              const browser = await puppeteer.connect({ browserWSEndpoint });
              try {
                  console.log(`Connected! Starting inspect session...`);
                  const page = await browser.newPage();
                  const client = await page.createCDPSession();
                  const { frameTree: { frame } } = await client.send('Page.getFrameTree');
                  const { url: inspectUrl } = await client.send('Page.inspect', {
                      frameId: frame.id,
                  });
                  console.log(`You can inspect this session at: ${inspectUrl}.`);
                  console.log(`Scraping will continue in 10 seconds...`);
                  await sleep(10);
                  console.log(`Navigating to ${url}...`);
                  await page.goto(url, { timeout: 2 * 60 * 1000 });
                  console.log(`Navigated! Scraping paragraphs...`);
                  const data = await page.$$eval('p', els => els.map(el => el.innerText));
                  console.log(`Scraped! Data:`, data);
                  console.log(`Session will be closed in 1 minute...`);
                  await sleep(60);
              } finally {
                  console.log(`Closing session.`);
                  await browser.close();
              }
          }

          function sleep(seconds) {
              return new Promise(resolve => setTimeout(resolve, seconds * 1000));
          }

          function getErrorDetails(error) {
              if (error.target?._req?.res) {
                  const {
                      statusCode,
                      statusMessage,
                  } = error.target._req.res;
                  return `Unexpected Server Status ${statusCode}: ${statusMessage}`;
              }
          }

          if (require.main == module) {
              scrape().catch(error => {
                  console.error(getErrorDetails(error)
                      || error.stack
                      || error.message
                      || error);
                  process.exit(1);
              });
          }
          ```

          ```js Selenium theme={null}
          #!/usr/bin/env node
          const { Builder, Browser, By } = require('selenium-webdriver');
          const {
              AUTH = 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD',
              TARGET_URL = 'https://example.com',
          } = process.env;

          async function scrape(url = TARGET_URL) {
              if (AUTH == 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD') {
                  throw new Error(`Provide Browser API credentials in AUTH`
                      + ` environment variable or update the script.`);
              }
              console.log(`Connecting to Browser...`);
              const server = `https://${AUTH}@brd.superproxy.io:9515`;
              const driver = await new Builder()
                  .forBrowser(Browser.CHROME)
                  .usingServer(server)
                  .build();
              const cdp = (name, params = {}) => driver.sendAndGetDevToolsCommand(name, params);
              try {
                  console.log(`Connected! Starting inspect session...`);
                  const { frameTree: { frame } } = await cdp('Page.getFrameTree');
                  const { url: inspectUrl } = await cdp('Page.inspect', {
                      frameId: frame.id,
                  });
                  console.log(`You can inspect this session at: ${inspectUrl}.`);
                  console.log(`Scraping will continue in 10 seconds...`);
                  await sleep(10);
                  console.log(`Navigating to ${url}...`);
                  await driver.get(url);
                  console.log(`Navigated! Scraping paragraphs...`);
                  const paragraphs = await driver.findElements(By.css('p'));
                  const data = await driver.executeScript(els => els.map(el => el.innerText), paragraphs);
                  console.log(`Scraped! Data:`, data);
                  console.log(`Session will be closed in 1 minute...`);
                  await sleep(60);
              } finally {
                  console.log(`Closing session.`);
                  await driver.quit();
              }
          }

          function sleep(seconds) {
              return new Promise(resolve => setTimeout(resolve, seconds * 1000));
          }

          if (require.main == module) {
              scrape().catch(error => {
                  console.error(error.stack || error.message || error);
                  process.exit(1);
              });
          }
          ```
        </CodeGroup>
      </Tab>

      <Tab title="Python">
        <CodeGroup>
          ```python Playwright - Async theme={null}
          #!/usr/bin/env python3
          import asyncio
          from os import environ
          from playwright.async_api import Playwright, async_playwright

          AUTH = environ.get('AUTH', default='SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD')
          TARGET_URL = environ.get('TARGET_URL', default='https://example.com')


          async def scrape(playwright: Playwright, url=TARGET_URL):
              if AUTH == 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD':
                  raise Exception('Provide Browser API credentials in AUTH ' +
                                  'environment variable or update the script.')
              print('Connecting to Browser...')
              endpoint_url = f'wss://{AUTH}@brd.superproxy.io:9222'
              browser = await playwright.chromium.connect_over_cdp(endpoint_url)
              try:
                  print('Connected! Starting inspect session...')
                  page = await browser.new_page()
                  client = await page.context.new_cdp_session(page)
                  frames = await client.send('Page.getFrameTree')
                  frame_id = frames['frameTree']['frame']['id']
                  inspect = await client.send('Page.inspect', {
                      'frameId': frame_id,
                  })
                  inspect_url = inspect['url']
                  print(f'You can inspect this session at: {inspect_url}.')
                  print('Scraping will continue in 10 seconds...')
                  await asyncio.sleep(10)
                  print(f'Navigating to {url}...')
                  await page.goto(url, timeout=2*60_000)
                  print('Navigated! Scraping paragraphs...')
                  data = await page.eval_on_selector_all(
                      'p', 'els => els.map(el => el.innerText)')
                  print('Scraped! Data', data)
                  print('Session will be closed in 1 minute...')
                  await asyncio.sleep(60)
              finally:
                  print('Closing session.')
                  await browser.close()


          async def main():
              async with async_playwright() as playwright:
                  await scrape(playwright)


          if __name__ == '__main__':
              asyncio.run(main())

          ```

          ```python Playwright - Sync theme={null}
          #!/usr/bin/env python3
          from os import environ
          from time import sleep
          from playwright.sync_api import Playwright, sync_playwright

          AUTH = environ.get('AUTH', default='SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD')
          TARGET_URL = environ.get('TARGET_URL', default='https://example.com')


          def scrape(playwright: Playwright, url=TARGET_URL):
              if AUTH == 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD':
                  raise Exception('Provide Browser API credentials in AUTH ' +
                                  'environment variable or update the script.')
              print('Connecting to Browser...')
              endpoint_url = f'wss://{AUTH}@brd.superproxy.io:9222'
              browser = playwright.chromium.connect_over_cdp(endpoint_url)
              try:
                  print('Connected! Starting inspect session...')
                  page = browser.new_page()
                  client = page.context.new_cdp_session(page)
                  frames = client.send('Page.getFrameTree')
                  frame_id = frames['frameTree']['frame']['id']
                  inspect = client.send('Page.inspect', {
                      'frameId': frame_id,
                  })
                  inspect_url = inspect['url']
                  print(f'You can inspect this session at: {inspect_url}.')
                  print('Scraping will continue in 10 seconds...')
                  sleep(10)
                  print(f'Navigating to {url}...')
                  page.goto(url, timeout=2*60_000)
                  print('Navigated! Scraping paragraphs...')
                  data = page.eval_on_selector_all(
                      'p', 'els => els.map(el => el.innerText)')
                  print('Scraped! Data', data)
                  print('Session will be closed in 1 minute...')
                  sleep(60)
              finally:
                  print('Closing session.')
                  browser.close()


          def main():
              with sync_playwright() as playwright:
                  scrape(playwright)


          if __name__ == '__main__':
              main()

          ```

          ```python Selenium theme={null}
          #!/usr/bin/env python3
          from os import environ
          from time import sleep
          from selenium.webdriver import Remote, ChromeOptions as Options
          from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection as Connection
          from selenium.webdriver.common.by import By

          AUTH = environ.get('AUTH', default='SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD')
          TARGET_URL = environ.get('TARGET_URL', default='https://example.com')


          def scrape(url=TARGET_URL):
              if AUTH == 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD':
                  raise Exception('Provide Browser API credentials in AUTH ' +
                                  'environment variable or update the script.')
              print('Connecting to Browser...')
              server_addr = f'https://{AUTH}@brd.superproxy.io:9515'
              connection = Connection(server_addr, 'goog', 'chrome')
              driver = Remote(connection, options=Options())

              def cdp(cmd, params={}):
                  return driver.execute('executeCdpCommand', {
                      'cmd': cmd,
                      'params': params,
                  })['value']
              try:
                  print('Connected! Starting inspect session...')
                  frames = cdp('Page.getFrameTree')
                  frame_id = frames['frameTree']['frame']['id']
                  inspect = cdp('Page.inspect', {
                      'frameId': frame_id,
                  })
                  inspect_url = inspect['url']
                  print(f'You can inspect this session at: {inspect_url}.')
                  print('Scraping will continue in 10 seconds...')
                  sleep(10)
                  print(f'Navigating to {url}...')
                  driver.get(url)
                  print('Navigated! Scraping paragraphs...')
                  paragraphs = driver.find_elements(By.TAG_NAME, 'p')
                  data = driver.execute_script(
                      'return arguments[0].map(el => el.innerText)', paragraphs)
                  print('Scraped! Data', data)
                  print('Session will be closed in 1 minute...')
                  sleep(60)
              finally:
                  print('Closing session.')
                  driver.quit()


          if __name__ == '__main__':
              scrape()

          ```
        </CodeGroup>
      </Tab>

      <Tab title="C#">
        <CodeGroup>
          ```cs Puppeteer theme={null}
          using PuppeteerSharp;
          using System.Net.WebSockets;
          using System.Text;

          class Scraper
          {

              private string _auth;

              public Scraper(string auth)
              {
                  _auth = auth;
              }

              private async Task<IBrowser> Connect()
              {
                  if (_auth == "SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD")
                  {
                      throw new Exception("Provide Browser API credentials in AUTH"
                              + " environment variable or update the script.");
                  }
                  var options = new ConnectOptions()
                  {
                      BrowserWSEndpoint = "wss://brd.superproxy.io:9222",
                      WebSocketFactory = async (uri, options, cToken) =>
                      {
                          var socket = new ClientWebSocket();
                          var authBytes = Encoding.UTF8.GetBytes(_auth);
                          var authHeader = "Basic " + Convert.ToBase64String(authBytes);
                          socket.Options.SetRequestHeader("Authorization", authHeader);
                          socket.Options.KeepAliveInterval = TimeSpan.Zero;
                          await socket.ConnectAsync(uri, cToken);
                          return socket;
                      },
                  };
                  return await Puppeteer.ConnectAsync(options);
              }

              public async Task Scrape(string url)
              {
                  Log("Connecting to Browser...");
                  var browser = await Connect();
                  try {
                      Log("Connected! Starting inspect session...");
                      var page = await browser.NewPageAsync();
                      var client = await page.Target.CreateCDPSessionAsync();
                      var frames = await client.SendAsync("Page.getFrameTree");
                      var frameId = (string) frames!["frameTree"]!["frame"]!["id"]!;
                      var inspect = await client.SendAsync("Page.inspect",
                              new { frameId = frameId });
                      var inspectUrl = (string) inspect!["url"]!;
                      Log($"You can inspect this session at: {inspectUrl}");
                      Log("Scraping will continue in 10 seconds...");
                      await Task.Delay(10 * 1000);
                      Log($"Navigating to {url}...");
                      await page.GoToAsync(url, /* timeout= */ 2 * 60 * 1000);
                      Log("Navigated! Scraping paragraphs...");
                      var paragraphs = await page.QuerySelectorAllHandleAsync("p");
                      var data = await paragraphs.EvaluateFunctionAsync(
                              "els => els.map(el => el.innerText)");
                      Log($"Scraped! Data: {data}");
                      Log("Session will be closed in 1 minute...");
                      await Task.Delay(60 * 1000);
                  } finally {
                      Log("Closing session.");
                      await browser.CloseAsync();
                  }
              }

              private static string Env(string name, string defaultValue)
              {
                  return Environment.GetEnvironmentVariable(name) ?? defaultValue;
              }

              private static void Log(string message)
              {
                  Console.WriteLine(message);
              }

              public static async Task Main()
              {
                  var auth = Env("AUTH", "SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD");
                  var url = Env("TARGET_URL", "https://example.com");
                  var scraper = new Scraper(auth);
                  await scraper.Scrape(url);
              }

          }

          ```

          ```cs Selenium theme={null}
          using OpenQA.Selenium;
          using OpenQA.Selenium.Chrome;
          using OpenQA.Selenium.Remote;

          class Scraper
          {

              private string _auth;

              public Scraper(string auth)
              {
                  _auth = auth;
              }

              private WebDriver Connect()
              {
                  if (_auth == "SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD")
                  {
                      throw new Exception("Provide Browser API credentials in AUTH"
                              + " environment variable or update the script.");
                  }
                  var uri = new Uri($"https://{_auth}@brd.superproxy.io:9515");
                  var executor = new HttpCommandExecutor(uri, TimeSpan.FromSeconds(60));
                  var cdpCommand = new HttpCommandInfo(HttpCommandInfo.PostCommand,
                          "/session/{sessionId}/goog/cdp/execute");
                  executor.TryAddCommand("cdp", cdpCommand);
                  var capabilities = new ChromeOptions().ToCapabilities();
                  return new RemoteWebDriver(executor, capabilities);
              }

              public void Scrape(string url)
              {
                  Log("Connecting to Browser...");
                  var driver = Connect();
                  try {
                      Log("Connected! Starting inspect session...");
                      var frames = Cdp(driver, "Page.getFrameTree");
                      var frameId = frames.Get<string>("frameTree", "frame", "id");
                      var inspect = Cdp(driver, "Page.inspect", new (){
                          {"frameId", frameId},
                      });
                      var inspectUrl = inspect.Get<string>("url");
                      Log($"You can inspect this session at: {inspectUrl}");
                      Log("Scraping will continue in 10 seconds...");
                      Thread.Sleep(10 * 1000);
                      Log($"Navigating to {url}...");
                      driver.Navigate().GoToUrl(url);
                      Log("Navigated! Scraping paragraphs...");
                      var paragraphs = driver.FindElements(By.CssSelector("p"));
                      var data = (IEnumerable<object>) driver.ExecuteScript(
                              "return arguments[0].map(el => el.innerText);", paragraphs);
                      Log($"Scraped! Data: [{string.Join(", ", data)}]");
                      Log("Session will be closed in 1 minute...");
                      Thread.Sleep(60 * 1000);
                  } finally {
                      Log("Closing session.");
                      driver.Quit();
                  }
              }

              private Dictionary<string, object> Cdp(WebDriver driver, string cmd, Dictionary<string, object>? args = null)
              {
                  var result = driver.ExecuteCustomDriverCommand("cdp", new ()
                  {
                      {"cmd", cmd},
                      {"params", args ?? new ()},
                  });
                  return (Dictionary<string, object>) result;
              }

              private static string Env(string name, string defaultValue)
              {
                  return Environment.GetEnvironmentVariable(name) ?? defaultValue;
              }

              private static void Log(string message)
              {
                  Console.WriteLine(message);
              }

              public static void Main()
              {
                  var auth = Env("AUTH", "SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD");
                  var url = Env("TARGET_URL", "https://example.com");
                  var scraper = new Scraper(auth);
                  scraper.Scrape(url);
              }

          }

          static class DictionaryUtility {
              static public T Get<T>(this Dictionary<string, object> dict, params string[] path)
              {
                  object result = dict;
                  foreach (var name in path)
                  {
                      if (result is Dictionary<string, object> obj)
                          result = obj[name];
                      else
                          throw new Exception("Wrong type");
                  }
                  return (T) result;
              }
          }

          ```
        </CodeGroup>
      </Tab>
    </Tabs>
  </Tab>
</Tabs>

***

## 使用 Browser API 优化带宽使用

在优化您的网页爬取项目时，节省带宽至关重要。请参考以下提示和指南，在脚本中使用节省带宽的技巧，确保高效、资源友好的爬取。

### **避免不必要的媒体内容**

下载不必要的媒体（图片、视频）是常见的带宽消耗。您可以直接在脚本中阻止这些资源。

<Note>
  由于反爬虫机制的影响，阻止资源有时可能会影响页面加载。如果在阻止资源后出现问题，请在联系支持之前恢复您的阻止逻辑。
</Note>

<Tabs>
  <Tab title="阻止所有图片">
    <CodeGroup>
      ```js NodeJS - Puppeteer theme={null}
       const page = await browser.newPage();  
        
        // Enable request interception  
        await page.setRequestInterception(true);  
        
        // Listen for requests  
        page.on('request', (request) => {  
          if (request.resourceType() === 'image') {  
            // If the request is for an image, block it  
            request.abort();  
          } else {  
            // If it's not an image request, allow it to continue  
            request.continue();  
         }  
       });
      ```

      ```python Selenium theme={null}
      # Set the preference to not load images  
      prefs = {"profile.managed_default_content_settings.images": 2}  
      chrome_options.add_experimental_option("prefs", prefs)  
        
      # Create a new Chrome browser instance with the defined options  
      driver = webdriver.Chrome(options=chrome_options)  
        
      driver.get('https://example.com')
      ```
    </CodeGroup>
  </Tab>

  <Tab title="阻止特定图片格式">
    ```js theme={null}
     const page = await browser.newPage();  
      
      // Enable request interception  
      await page.setRequestInterception(true);  
      
      // Listen for requests  
      page.on('request', (interceptedRequest) => {  
      
        // Check if the request URL ends with '.png' or '.jpg'  
        if (  
          interceptedRequest.url().endsWith('.png') ||  
          interceptedRequest.url().endsWith('.jpg')  
        ) {  
      
          // If the request is for a PNG or JPG image, block it  
          interceptedRequest.abort();  
        } else {  
          // If it's not a PNG or JPG image request, allow it to continue  
          interceptedRequest.continue();  
       }  
     });
    ```
  </Tab>

  <Tab title="阻止图片和字体">
    ```js Playwright theme={null}
     // Create a new context with specific resource types blocked  
      const context = await browser.newContext({  
        fetchResourceTypesToBlock: ['image', 'font']  
      });  
      
      const page = await context.newPage();  
      
      // Navigate to a webpage  
      await page.goto('https://example.com');
    ```
  </Tab>
</Tabs>

***

### **阻止不必要的网络请求**

仅阻止媒体类型的请求并不总能降低带宽使用量。一些网站的广告位会不断刷新广告，另一些网站使用实时竞价机制，如果某个广告加载失败，会持续寻找新的广告。

在这种情况下，识别并阻止这些特定的网络请求非常重要。这样可以减少网络请求的数量，从而降低带宽使用。

```js Example theme={null}
 const blocked_resources = [
     "image",
     "stylesheet",
     "font",
     "media",
     "svg"
 ];
 
 const blocked_urls = [
     'www.googletagmanager.com/gtm.js',
     'cdn.adapex.io/hb',
     'pagead2.googlesyndication.com/',
 ];
 
 await page.setRequestInterception(true);
 
 page.on('request', request => {
     counter++;
     const is_url_blocked = blocked_urls.some(p => request.url().includes(p));
     const is_resource_blocked = blocked_resources.includes(request.resourceType());
     if (is_url_blocked || is_resource_blocked) {
         request.abort();
     } else {
         request.continue();
     }
 });
```

***

### **高效使用缓存页面**

抓取任务中的一个常见低效问题是在单个会话中重复下载同一页面。

利用缓存页面——先前抓取页面的版本——可以显著提高抓取效率，因为它可用于避免对同一域名的重复网络请求。这不仅通过避免冗余获取节省带宽，还能确保与预加载内容的交互更快、更流畅。

#### **代码示例**

<Note>
  本示例中使用的选择器（.product-name、.product-price、.product-link、.apply-coupon-button）是通用占位符。请根据您要抓取的网站的实际 HTML 结构进行更新。
  同时，请确保将 [**https://example.com**](https://example.com) 替换为您的目标 URL。
</Note>

```js Puppeteer theme={null}
const puppeteer = require('puppeteer-core');
const AUTH = 'USER:PASS';
const SBR_WS_ENDPOINT = `wss://${AUTH}@brd.superproxy.io:9222`;

async function scrapeProductDetails(link) {
    console.log('Connecting to Scraping Browser...');
    const browser = await puppeteer.connect({
        browserWSEndpoint: SBR_WS_ENDPOINT,
    });
    try {
        console.log(`Connected! Navigating to: ${link}`);
        await page.goto(link, { timeout: 2 * 60 * 1000 });

        // Wait for and extract product name
        await page.waitForSelector('.product-name', { timeout: 30000 });
        const productName = await page.$eval('.product-name', el => el.textContent.trim());

        // Try to apply coupon if button exists
        const couponButton = await page.$('.apply-coupon-button');
        if (couponButton) {
            await couponButton.click();
        }

        // Extract price
        await page.waitForSelector('.product-price', { timeout: 30000 });
        const productPrice = await page.$eval('.product-price', el => el.textContent.trim());

        return { productName, productPrice, link };
    } catch (error) {
        console.error(`Error scraping ${link}:`, error.message);
        return null;
    } finally {
        await browser.close();
    }
}

async function main() {
    console.log('Connecting to Scraping Browser...');
    const browser = await puppeteer.connect({
        browserWSEndpoint: SBR_WS_ENDPOINT,
    });

    try {
        console.log('Connected! Navigating to listing page...');
        const page = await browser.newPage();
        await page.goto('https://example.com', {
            timeout: 2 * 60 * 1000
        });

        await page.waitForSelector('.product-link', { timeout: 30000 });

        // Extract product links from the listing page
        const productLinks = await page.$$eval('.product-link', links =>
            links.map(link => link.href).slice(0, 10) // Limit to first 10 for testing
        );

        console.log(`Found ${productLinks.length} products`);
        await browser.close();

        // Scrape product details in parallel
        const productDetailsPromises = productLinks.map(link => scrapeProductDetails(link));
        const productDetails = await Promise.all(productDetailsPromises);

        // Filter out any null results from failed scrapes
        const validProductDetails = productDetails.filter(details => details !== null);

        console.log('Scraped product details:', validProductDetails);
    } catch (error) {
        console.error('Error during the main process:', error);
    }
}

main();
```

***

### **其他策略**

* **限制请求量：** 仅抓取所需数据。
* **并发控制：** 避免同时打开过多页面，这可能会导致资源过载。
* **会话管理：** 正确关闭会话以节省资源和带宽。
* **优先使用 API：** 在可用时使用官方 API——它们通常对带宽的消耗较小。
* **增量抓取：** 仅抓取新的或更新的内容，而不是每次抓取整个数据集。

***
