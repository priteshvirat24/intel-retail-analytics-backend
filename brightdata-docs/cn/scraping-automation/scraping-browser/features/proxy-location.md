> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 地理位置定向

> 针对特定国家或地理位置的节点进行精确的地理定向数据采集。

<Tip>
  Browser API 会自动为你的会话选择最佳节点位置，因此在**大多数**情况下无需手动配置。仅在访问受地区限制或特定位置的数据时需要手动地理定向。
</Tip>

* [**国家**](/cn/scraping-automation/scraping-browser/features/proxy-location#country) - 从特定国家的节点发起请求
* [**地理半径**](/cn/scraping-automation/scraping-browser/features/proxy-location#geolocation-radius) – 使用精确的纬度、经度和半径来模拟真实物理位置，实现更精细的地理定向数据采集。

## Country

在 Bright Data endpoint 中，将 `-country` 标志添加在你的 `USER` 凭据之后，并跟上该国家的 2 字母 ISO 代码。

例如，使用 Puppeteer 的美国 Browser API：

<CodeGroup>
  ```sh NodeJS, Puppeteer theme={null}
  const SBR_WS_ENDPOINT = `wss://${USERNAME-country-us:PASSWORD}@brd.superproxy.io:9222`;
  ```
</CodeGroup>

**欧盟区域**
你可以与“国家”定向相同的方式，通过在请求中将 "eu" 添加在 "country" 后（即："-country-eu"）来定向整个欧盟区域。

使用 -country-eu 发出的请求会使用以下自动包含在 "eu" 区域中的国家的 IP：
`AL, AZ, KG, BA, UZ, BI, XK, SM, DE, AT, CH, UK, GB,IE, IM, FR, ES, NL, IT, PT, BE, AD, MT, MC, MA, LU, TN, DZ, GI, LI, SE, DK, FI, NO, AX, IS, GG, JE, EU, GL, VA, FX, FO.`

## Geolocation radius

使用 `Proxy.setLocation` 函数可根据精确的纬度、经度和半径动态更改代理位置。

### Parameters

<ParamField path="lat" type="float">
  指定所需代理位置的纬度。
</ParamField>

<ParamField path="lon" type="float">
  指定所需代理位置的经度。
</ParamField>

<ParamField path="strict" type="boolean" default="true">
  定义在指定距离内无可用节点时的行为。

  `strict: true` - 系统将仅在指定距离内搜索可用节点。

  `strict: false` - 如果指定距离内无可用节点，我们将自动扩大距离并寻找最近的可用节点。
</ParamField>

### Usage

应在导航至目标站点之前调用 `Proxy.setLocation` 命令。这样可确保在执行任何数据请求之前代理位置已根据指定参数准确设置。

**如何运行示例**

你需要在控制面板中获取 Browser API 凭据。
将其以 `SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD` 格式作为环境变量 `AUTH` 传入。

<CodeGroup>
  ```sh Shell theme={null}
  export AUTH=brd-customer-<customer_id>-zone-<zone_name>:<zone_password>
  ```

  ```sh CMD theme={null}
  set AUTH=brd-customer-<customer_id>-zone-<zone_name>:<zone_password>
  ```

  ```powershell Powershell theme={null}
  $Env:AUTH = 'brd-customer-<customer_id>-zone-<zone_name>:<zone_password>'
  ```
</CodeGroup>

<Tip>你也可以传入 `TARGET_URL` 环境变量来更改默认目标网站。</Tip>

### Code Examples

在采集前更改代理位置

<Tip>请选择你偏好的技术栈</Tip>

<CodeGroup>
  ```js NodeJS - Playwright theme={null}
  #!/usr/bin/env node
  const playwright = require('playwright');
  const {
      AUTH = 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD',
      TARGET_URL = 'https://geo.brdtest.com/mygeo.json',
      LOCATION = 'amsterdam',
  } = process.env;

  const LOCATIONS = Object.freeze({
      amsterdam: { lat: 52.377956, lon: 4.897070 },
      london: { lat: 51.509865, lon: -0.118092 },
      new_york: { lat: 40.730610, lon: -73.935242 },
      paris: { lat: 48.864716, lon: 2.349014 },
  });

  async function scrape(url = TARGET_URL, location = LOCATION) {
      if (AUTH == 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD') {
          throw new Error(`Provide Browser API credentials in AUTH`
              + ` environment variable or update the script.`);
      }
      if (!LOCATIONS[location]) {
          throw new Error(`Unknown location`);
      }
      const { lat, lon } = LOCATIONS[location];
      console.log(`Connecting to Browser...`);
      const endpointURL = `wss://${AUTH}@brd.superproxy.io:9222`;
      const browser = await playwright.chromium.connectOverCDP(endpointURL);
      try {
          console.log(`Connected! Changing proxy location`
              + ` to ${location} (${lat}, ${lon})...`);
          const page = await browser.newPage();
          const client = await page.context().newCDPSession(page);
          await client.send('Proxy.setLocation', {
              lat, lon,
              distance: 50 /* kilometers */,
              strict: true,
          });
          console.log(`Navigating to ${url}...`);
          await page.goto(url, { timeout: 2 * 60 * 1000 });
          console.log(`Navigated! Scraping data...`);
          const data = await page.$eval('body', el => el.innerText);
          console.log(`Scraped! Data:`, JSON.parse(data));
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

  ```js NodeJS - Puppeteer theme={null}
  #!/usr/bin/env node
  const puppeteer = require('puppeteer-core');
  const {
      AUTH = 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD',
      TARGET_URL = 'https://geo.brdtest.com/mygeo.json',
      LOCATION = 'amsterdam',
  } = process.env;

  const LOCATIONS = Object.freeze({
      amsterdam: { lat: 52.377956, lon: 4.897070 },
      london: { lat: 51.509865, lon: -0.118092 },
      new_york: { lat: 40.730610, lon: -73.935242 },
      paris: { lat: 48.864716, lon: 2.349014 },
  });

  async function scrape(url = TARGET_URL, location = LOCATION) {
      if (AUTH == 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD') {
          throw new Error(`Provide Browser API credentials in AUTH`
              + ` environment variable or update the script.`);
      }
      if (!LOCATIONS[location]) {
          throw new Error(`Unknown location`);
      }
      const { lat, lon } = LOCATIONS[location];
      console.log(`Connecting to Browser...`);
      const browserWSEndpoint = `wss://${AUTH}@brd.superproxy.io:9222`;
      const browser = await puppeteer.connect({ browserWSEndpoint });
      try {
          console.log(`Connected! Changing proxy location`
              + ` to ${location} (${lat}, ${lon})...`);
          const page = await browser.newPage();
          const client = await page.createCDPSession();
          await client.send('Proxy.setLocation', {
              lat, lon,
              distance: 50 /* kilometers */,
              strict: true,
          });
          console.log(`Navigating to ${url}...`);
          await page.goto(url, { timeout: 2 * 60 * 1000 });
          console.log(`Navigated! Scraping data...`);
          const data = await page.$eval('body', el => el.innerText);
          console.log(`Scraped! Data:`, JSON.parse(data));
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

  ```js NodeJS - Selenium theme={null}
  #!/usr/bin/env node
  const { Builder, Browser, By } = require('selenium-webdriver');
  const {
      AUTH = 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD',
      TARGET_URL = 'https://geo.brdtest.com/mygeo.json',
      LOCATION = 'amsterdam',
  } = process.env;

  const LOCATIONS = Object.freeze({
      amsterdam: { lat: 52.377956, lon: 4.897070 },
      london: { lat: 51.509865, lon: -0.118092 },
      new_york: { lat: 40.730610, lon: -73.935242 },
      paris: { lat: 48.864716, lon: 2.349014 },
  });

  async function scrape(url = TARGET_URL, location = LOCATION) {
      if (AUTH == 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD') {
          throw new Error(`Provide Browser API credentials in AUTH`
              + ` environment variable or update the script.`);
      }
      if (!LOCATIONS[location]) {
          throw new Error(`Unknown location`);
      }
      const { lat, lon } = LOCATIONS[location];
      console.log(`Connecting to Browser...`);
      const server = `https://${AUTH}@brd.superproxy.io:9515`;
      const driver = await new Builder()
          .forBrowser(Browser.CHROME)
          .usingServer(server)
          .build();
      try {
          console.log(`Connected! Changing proxy location`
              + ` to ${location} (${lat}, ${lon})...`);
          await driver.sendAndGetDevToolsCommand('Proxy.setLocation', {
              lat, lon,
              distance: 50 /* kilometers */,
              strict: true,
          });
          console.log(`Navigating to ${url}...`);
          await driver.get(url);
          console.log(`Navigated! Scraping data...`);
          const body = await driver.findElement(By.css('body'));
          const data = await body.getText();
          console.log(`Scraped! Data:`, JSON.parse(data));
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

## 如何获取代理地理位置

使用此命令可获取分配给当前浏览器会话的代理节点的精确地理位置信息。这有助于你在本地记录和验证所分配节点的位置。

### 代理地理位置 CDP 命令

* `Proxy.getGeolocation`

<Note>
  请在导航到目标页面之后使用该 CDP 命令。
</Note>

```js Example (Puppeteer) theme={null}
const page = await browser.newPage();
const client = await page.createCDPSession();
await page.goto('https://example.com');
const geolocation = await client.send('Proxy.getGeolocation');
console.log('Proxy Geolocation:', geolocation);
```

```json Returns theme={null}
{
  "result": {
    "ip_version": 4,
    "country": "us",
    "asn": {
      "asnum": 7018,
      "org_name": "AT&T Enterprises, LLC"
    },
    "geo": {
      "city": "Rogers",
      "city_slug": "rogers",
      "region": "ar",
      "region_slug": "ar",
      "region_name": "Arkansas",
      "postal_code": "72758",
      "latitude": 36.3174,
      "longitude": -94.1548,
      "tz": "America/Chicago"
    }
  }
}
```
