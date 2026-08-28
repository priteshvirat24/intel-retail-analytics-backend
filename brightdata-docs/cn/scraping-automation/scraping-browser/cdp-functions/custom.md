> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 自定义 CDP 函数

> Bright Data Browser API 自定义 CDP 函数参考，在标准 Chrome DevTools Protocol 之上扩展解封锁与会话控制能力。

## 如何解决验证码

使用 Browser API 浏览页面时，我们集成的验证码解算器默认会**自动解算所有验证码**。您可以使用以下自定义 CDP 函数在代码中监控此自动解算过程。

<Note>
  如果您想通过控制面板完全禁用验证码解算器，请参阅[禁用验证码解算器](/cn/scraping-automation/scraping-browser/features/captcha-solver)功能。
</Note>

<Note>
  验证码解算后，如有表单需要提交，则默认情况下会提交。
</Note>

## 验证码解算器 - 自动解算

<AccordionGroup>
  <Accordion title="Captcha.solve">
    使用此命令返回验证码已解算、解算失败或未检测到之后的状态。

    <CodeGroup>
      ```js Captcha.solve theme={null}
      Captcha.solve({
          detectTimeout?: number // 解算器检测验证码的超时时间（毫秒）
          options?: CaptchaOptions[] // 验证码解算的配置选项
      }) : SolveResult
      ```

      ```js SolveResult theme={null}
      SolveResult : {
        status: SolveStatus // 检测与解算状态
        type?: string // 检测到的验证码类型
        error?: string // 验证码未解算时的错误信息
      }
      ```

      ```js SolveStatus theme={null}
      SolveStatus : string enum {
        "not_detected" // 未检测到验证码
        "solve_finished" // 验证码解算成功
        "solve_failed" // 检测到验证码，但解算失败
        "invalid" // 出现异常
      }
      ```
    </CodeGroup>

    **示例**

    <CodeGroup>
      ```js NodeJS - Puppeteer theme={null}
      const page = await browser.newPage();
      const client = await page.createCDPSession();
      await page.goto('https://site-with-captcha.com/');

      // 注意 1：如果未找到验证码，将在 detectTimeout 之后返回 not_detected 状态
      // 注意 2：验证码解算后，如有表单需要提交，则默认情况下会提交

      const {status} = await client.send('Captcha.solve', {detectTimeout: 30*1000});
      console.log(`Captcha solve status: ${status}`)
      ```

      ```python Python - Playwright theme={null}
      page = await browser.new_page()
      client = await page.context.new_cdp_session(page)
      await page.goto('https://site-with-captcha.com/')

      # 注意 1：如果未找到验证码，将在 detectTimeout 之后返回 not_detected 状态
      # 注意 2：验证码解算后，如有表单需要提交，则默认情况下会提交

      solve_result = await client.send('Captcha.solve', { 'detectTimeout': 30*1000 })
      status = solve_result['status']
      print(f'Captcha solve status: {status}')
      ```

      ```c# C# - PuppeteerSharp theme={null}
      var page = await browser.NewPageAsync();
      var client = page.Client;
      await page.GoToAsync(url);
      var result = await client.SendAsync("Captcha.solve", new
      {
          detectTimeout = 10 * 1000,
      });
      var status = result.Value.GetProperty("status").GetString();
      Log($"Captcha solve status: {status}");
      ```

      ```c# C# - Playwright theme={null}
      var page = await browser.NewPageAsync();
      var cdpSession = await page.Context.NewCDPSessionAsync(page);
      await page.GotoAsync(url);
      var result = await cdpSession.SendAsync("Captcha.solve", new Dictionary<string, object>
      {
          ["detectTimeout"] = 10 * 1000
      });
      var status = result.Value.GetProperty("status").GetString();
      Log($"Captcha solve status: {status}");
      ```
    </CodeGroup>

    <Note>
      如果验证码解算失败，请尝试重试。如果问题持续存在，请提交支持请求并详细说明您遇到的具体问题。
    </Note>
  </Accordion>

  <Accordion title="用于验证码状态的自定义 CDP 命令">
    使用以下命令可以精确定位验证码解算流程中更具体的阶段：

    |                         |                         |
    | ----------------------- | ----------------------- |
    | `Captcha.detected`      | Browser API 已遇到验证码并开始解算 |
    | `Captcha.solveFinished` | Browser API 成功解算了验证码    |
    | `Captcha.solveFailed`   | Browser API 解算验证码失败     |
    | `Captcha.waitForSolve`  | Browser API 等待验证码解算器完成  |

    **示例**

    <Tabs>
      <Tab title="异步">
        以下代码建立 CDP 会话、监听验证码事件并处理超时：

        <CodeGroup>
          ```js NodeJS - Puppeteer theme={null}
          // Node.js - Puppeteer - 等待验证码解算事件
          const client = await page.target().createCDPSession();
          await new Promise((resolve, reject)=>{
            client.on('Captcha.solveFinished', resolve);
            client.on('Captcha.solveFailed', ()=>reject(new Error('Captcha failed')));
            setTimeout(reject, 5 * 60 * 1000, new Error('Captcha solve timeout'));
          });
          ```

          ```python Python - Playwright theme={null}
          # Python - Playwright - 等待验证码解算事件
          client = await page.context.new_cdp_session(page)
          client.on('Captcha.detected', lambda c: print('Captcha detected', c))
          client.on('Captcha.solveFinished', lambda _: print('Captcha solved!'))
          client.on('Captcha.solveFailed', lambda _: print('Captcha failed!'))
          ```
        </CodeGroup>
      </Tab>

      <Tab title="同步">
        <Warning>
          Selenium 不像 Puppeteer 和 Playwright 那样支持由服务端驱动的异步事件。
        </Warning>

        `Captcha.waitForSolve` 命令会等待 Browser API 的验证码解算器完成。

        ```python Python - Selenium theme={null}
        # Python Selenium - 导航后等待验证码自动解算
        driver.execute('executeCdpCommand', {
            'cmd': 'Captcha.waitForSolve',
            'params': {},
        })
        ```
      </Tab>
    </Tabs>
  </Accordion>
</AccordionGroup>

## 验证码解算器 - 手动控制

如果您想手动配置或完全禁用我们默认的验证码解算器，改为手动调用解算器或自行解算，请参阅以下 CDP 命令与功能。

<AccordionGroup>
  <Accordion title="Captcha.setAutoSolve">
    此命令用于控制验证码的自动解算。您可以禁用自动解算，或为不同的验证码类型配置算法并手动触发：

    <CodeGroup>
      ```js Captcha.setAutoSolve theme={null}
      Captcha.setAutoSolve({
        autoSolve: boolean // 导航后是否自动解算验证码
        options?: CaptchaOptions[] // 验证码自动解算的配置选项
      }) : void
      ```

      ```js CaptchaOptions theme={null}
      CaptchaOptions : {
        type: string // 验证码类型
        disabled?: boolean // 对指定验证码禁用检测与解算
        ... // 与验证码类型相关的其他选项
      }
      ```
    </CodeGroup>

    在会话内**完全**禁用自动解算器的 CDP 命令示例：

    <CodeGroup>
      ```js NodeJS - Puppeteer theme={null}
      // Node.js Puppeteer - 完全禁用验证码自动解算器
      const page = await browser.newPage();
      const client = await page.target().createCDPSession();
      await client.send('Captcha.setAutoSolve', { autoSolve: false })
      ```

      ```python Python - Playwright theme={null}
      # Python Playwright - 完全禁用验证码自动解算器
      page = await browser.new_page()
      client = await page.context.new_cdp_session(page)
      await client.send('Captcha.setAutoSolve', {'autoSolve': False})
      ```

      ```python - Selenium theme={null}
      # Python Selenium - 完全禁用验证码自动解算器
      driver.execute('executeCdpCommand', {
          'cmd': 'Captcha.setAutoSolve',
          'params': {'autoSolve': False},
      })
      ```
    </CodeGroup>
  </Accordion>

  <Accordion title="仅对特定验证码类型禁用自动解算器 - 示例">
    <CodeGroup>
      ```js NodeJS - Puppeteer theme={null}
      // Node.js Puppeteer - 仅对 ReCaptcha 禁用验证码自动解算器
      const page = await browser.newPage();
      const client = await page.target().createCDPSession();
      await client.send('Captcha.setAutoSolve', {
          autoSolve: true,
          options: [{
              type: 'usercaptcha',
              disabled: true,
          }],
      });
      ```

      ```python Python - Playwright theme={null}
      # Python Playwright - 仅对 ReCaptcha 禁用验证码自动解算器
      page = await browser.new_page()
      client = await page.context.new_cdp_session(page)
      await client.send('Captcha.setAutoSolve', {
          'autoSolve': True,
          'options': [{
              'type': 'usercaptcha',
              'disabled': True,
          }],
      })
      ```
    </CodeGroup>
  </Accordion>

  <Accordion title="手动解算验证码 - 示例">
    <CodeGroup>
      ```js NodeJS - Puppeteer theme={null}
      // Node.js Puppeteer - 导航后手动解算验证码
      const page = await browser.newPage();
      const client = await page.target().createCDPSession();
      await client.send('Captcha.setAutoSolve', { autoSolve: false });
      await page.goto('https://site-with-captcha.com', { timeout: 2*60*1000 });
      const {status} = await client.send('Captcha.solve', { detectTimeout: 30*1000 });
      console.log('Captcha solve status:', status);
      ```

      ```python Python - Playwright theme={null}
      # Python Playwright - 导航后手动解算验证码
      page = await browser.new_page()
      client = await page.context.new_cdp_session(page)
      await client.send('Captcha.setAutoSolve', {'autoSolve': False})
      await page.goto('https://site-with-captcha.com', timeout=2*60_000)
      solve_result = await client.send('Captcha.solve', {'detectTimeout': 30_000})
      print('Captcha solve status:', solve_result['status'])
      ```

      ```python Python - Selenium theme={null}
      # Python Selenium - 导航后手动解算验证码
      driver.execute('executeCdpCommand', {
          'cmd': 'Captcha.setAutoSolve',
          'params': {'autoSolve': False},
      })
      driver.get('https://site-with-captcha.com')
      solve_result = driver.execute('executeCdpCommand', {
          'cmd': 'Captcha.solve',
          'params': {'detectTimeout': 30_000},
      })
      print('Captcha solve status:', solve_result['value']['status'])
      ```
    </CodeGroup>
  </Accordion>

  <Accordion title="其他验证码类型的 CaptchaOptions">
    对于以下三种验证码类型，我们支持使用以下额外选项来控制和配置自动解算算法。

    <Tabs>
      <Tab title="CF Challenge">
        ```js CF Challenge theme={null}
        timeout: 40000
        selector: '#challenge-body-text, .challenge-form'
        check_timeout: 300
        error_selector: '#challenge-error-title'
        success_selector: '#challenge-success[style*=inline]'
        check_success_timeout: 300
        btn_selector: '#challenge-stage input[type=button]'
        cloudflare_checkbox_frame_selector: '#turnstile-wrapper iframe'
        checkbox_area_selector: '.ctp-checkbox-label .mark'
        wait_timeout_after_solve: 500
        wait_networkidle: {timeout: 500}
        ```
      </Tab>

      <Tab title="HCaptcha">
        ```js HCaptcha theme={null}
        detect_selector:
          '#cf-hcaptcha-container, #challenge-hcaptcha-wrapper .hcaptcha-box, .h-captcha'
        pass_proxy: true
        submit_form: true
        submit_selector: '#challenge-form body > form[action*="internalcaptcha/captchasubmit"]'
        value_selector: '.h-captcha textarea[id^="h-captcha-response"]'

        ```
      </Tab>

      <Tab title="usercaptcha (reCAPTCHA)">
        ```js UserCaptcha (reCAPTCHA) theme={null}
        { // reCAPTCHA（type=usercaptcha）的配置键与默认值
          type: 'usercaptcha',
          // 用于获取 sitekey 和/或 action 的选择器
          selector: '.g-recaptcha, .recaptcha',
          // 用于查找 sitekey 的属性
          sitekey_attributes: ['data-sitekey', 'data-key'],
          // 用于查找 action 的属性
          action_attributes: ['data-action'],
          // 检测选择器
          detect_selector: `
            .g-recaptcha[data-sitekey] > *,
            .recaptcha > *,
            iframe[src*="www.google.com/recaptcha/api2"],
            iframe[src*="www.recaptcha.net/recaptcha/api2"],
            iframe[src*="www.google.com/recaptcha/enterprise"]`,
          // 用于填入响应代码的元素
          reponse_selector: '#g-recaptcha-response, .g-recaptcha-response',
          // 解算验证码后解算器是否应自动提交表单
          submit_form: true,
          // 提交按钮的选择器
          submit_selector: '[type=submit]',
        }
        ```
      </Tab>
    </Tabs>
  </Accordion>
</AccordionGroup>

## 如何仿真设备

<AccordionGroup>
  <Accordion title="Emulation.getSupportedDevices">
    使用此命令获取所有可仿真设备的列表。此方法返回一个设备选项数组，可与 setDevice 命令一起使用。

    ```js 示例 theme={null}
    const devices = await client.send("Emulation.getSupportedDevices");
    console.log(devices);
    ```
  </Accordion>

  <Accordion title="Emulation.setDevice">
    获取上述支持的设备列表后，您可以使用 Emulation.setDevice 命令仿真特定设备。此命令会更改屏幕宽度、高度、userAgent 和 devicePixelRatio 以匹配指定的设备。

    <CodeGroup>
      ```js 用法 theme={null}
      await client.send("Emulation.setDevice", { device: "[device_name]" });
      ```

      ```js 示例 theme={null}
      await client.send("Emulation.setDevice", { device: "Vivo X200 Pro" });
      ```
    </CodeGroup>

    ### 横向模式

    如果您想将方向更改为横向（适用于支持横向的设备），请在 `device_name` 后添加字符串 `landscape`。

    ```js 示例 theme={null}
    await client.send("Emulation.setDevice", { device: "Vivo X200 Pro landscape" });
    ```
  </Accordion>
</AccordionGroup>

## 如何拦截广告

启用 `AdBlock` 功能可以在广告下载之前拦截广告和跟踪器请求，从而**减少带宽使用**并**提升广告密集型网站的性能**。

### 广告拦截器 CDP 命令

* `Unblocker.enableAdBlock` – 启用广告拦截器（默认：关闭）
* `Unblocker.disableAdBlock` – 禁用广告拦截器

#### 广告拦截器参数

| 参数        | 类型         | 说明                                                                                                                 |
| --------- | ---------- | ------------------------------------------------------------------------------------------------------------------ |
| `version` | `string`   | 拦截引擎版本。传入 `'2'`（推荐）以使用带有最新过滤列表的当前引擎。省略时使用旧版引擎。                                                                     |
| `mode`    | `string`   | 可选，需要 `version: '2'`。拦截覆盖范围：`'ads'`（默认）拦截广告网络；`'full'` 还会拦截跟踪器和分析工具，覆盖范围最广、带宽降幅最大；`'none'` 禁用内置列表，仅拦截 `list` 中的域名。 |
| `list`    | `string[]` | 可选，需要 `version: '2'`。在 `mode` 覆盖范围之外**额外**拦截的自定义域名。每一项都会拦截对该域名及其所有子域名的请求。                                          |

<Tip>
  请在导航至目标页面之前启用广告拦截。
</Tip>

```js 示例 theme={null}
const client = await page.createCDPSession();

await client.send('Unblocker.enableAdBlock', { version: '2' });

// 覆盖范围最广（广告 + 跟踪器）：
// await client.send('Unblocker.enableAdBlock', { version: '2', mode: 'full' });

// 额外拦截自定义域名：
// await client.send('Unblocker.enableAdBlock', { version: '2', list: ['annoying-widget.example.com'] });

await page.goto('https://example.com');
```

<Note>
  被拦截的请求会在浏览器的 DevTools 控制台中以 `Resource was blocked by ad-blocking` 消息报告。
</Note>

查看完整的[广告拦截示例脚本](https://github.com/luminati-io/sbr-examples/blob/main/nodejs/puppeteer-ad-block/scrape.js)。

## 如何拦截 Cookie 同意横幅

`CookieBlock` 功能会拦截常见第三方同意管理平台（CMP）的脚本，使 Cookie 同意横幅不会加载，您无需在自动化流程中查找并点击“接受”按钮。

### Cookie 拦截器 CDP 命令

* `Unblocker.enableCookieBlock` – 启用 Cookie 同意拦截（默认：关闭）
* `Unblocker.disableCookieBlock` – 禁用 Cookie 同意拦截

#### Cookie 拦截器参数

| 参数     | 类型         | 说明                                                     |
| ------ | ---------- | ------------------------------------------------------ |
| `list` | `string[]` | 可选。在内置 CMP 覆盖范围之外**额外**拦截的自定义域名。每一项都会拦截对该域名及其所有子域名的请求。 |

<Tip>
  请在导航至目标页面之前启用 Cookie 拦截。
</Tip>

```js 示例 theme={null}
const client = await page.createCDPSession();

await client.send('Unblocker.enableCookieBlock');

// 额外拦截站点专用的同意脚本：
// await client.send('Unblocker.enableCookieBlock', { list: ['cmp.example.com'] });

await page.goto('https://example.com');
```

<Note>
  内置覆盖范围可拦截由常见第三方 CMP 提供的横幅。网站自行托管的横幅不在覆盖范围内，如需拦截这类横幅，请找出提供同意脚本的域名（例如在 DevTools 的 Network 标签页中查看），并按上面的示例将其传入 `list` 参数。
</Note>

## 如何保持会话

使用此命令可以在多个浏览会话中重用同一个代理节点。这在需要保持会话一致性（如保留浏览器状态或基于 IP 的连续性）的场景中非常有用。

### 会话持久化 CDP 命令

* `Proxy.useSession` – 将会话与特定的 session ID 关联。
* `sessionId` – 唯一标识您的会话的字符串。

<Note>
  请在导航至目标页面之前使用此 CDP 命令。
</Note>

```js 示例 theme={null}
const client = await page.createCDPSession();
await client.send('Proxy.useSession', { sessionId });
await page.goto('https://geo.brdtest.com/mygeo.json');
```

<Tip>
  查看完整的[会话持久化示例脚本](https://github.com/luminati-io/sbr-examples/blob/main/nodejs/puppeteer-proxy-session/scrape.js)。
</Tip>

## 获取会话 ID

使用此命令检索当前浏览器会话的唯一 ID。当您需要通过 [Session Logs API](/cn/api-reference/browser-api/get-session) 查询会话日志时（例如排查错误、异常行为或高带宽使用情况），此命令非常有用。

### 会话 ID CDP 命令

* `Browser.getSessionId`

```js 示例（Puppeteer） theme={null}
const page = await browser.newPage();
const client = await page.target().createCDPSession();
const result = await client.send('Browser.getSessionId');
const sessionId = result.sessionId;
console.log('Current session ID:', sessionId);
```

```json 返回值 theme={null}
{
  "sessionId": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
}
```

## 如何下载文件

您可以使用自定义的 Download CDP 域在 Browser API 流程中自动化文件下载。这对于需要在浏览器自动化过程中直接下载文件（例如 CSV、PDF）的工作流非常有用。

### 文件下载 CDP 命令

* `Download.enable` – 启用指定内容类型的文件下载。
* `Download.downloadRequest` – 当请求产生下载时触发。
* `Download.getLastCompleted` – 获取上一次完成的下载信息。
* `Download.getDownloadedBody` – 获取实际下载的文件内容。

```js 示例 theme={null}
const client = await page.createCDPSession();

// 启用二进制文件（如 CSV）的下载
await client.send('Download.enable', { allowedContentTypes: ['application/octet-stream'] });

// 发起文件下载
await Promise.all([
  new Promise(resolve => client.once('Download.downloadRequest', resolve)),
  page.click(selector),
]);

// 下载完成后：
const { id } = await client.send('Download.getLastCompleted');
const { body, base64Encoded } = await client.send('Download.getDownloadedBody', { id });
const fs = require('fs');
fs.writeFileSync('./downloaded_file.csv', base64Encoded ? Buffer.from(body, 'base64') : body);
```

<Tip>
  查看完整的[文件下载示例脚本](https://github.com/luminati-io/sbr-examples/blob/main/nodejs/puppeteer-file-download/scrape.js)。
</Tip>

## 更快的文本输入

对于需要快速或批量文本输入的场景，请使用自定义的 Input.type CDP 命令。这种方法比标准 CDP 文本输入方法快得多，非常适合需要高速输入或处理大量文本的自动化任务。

### 快速文本输入 CDP 命令

* `Input.type` - 向当前聚焦的元素发送按键或模拟输入指定文本。

```js 示例 theme={null}
const client = await page.createCDPSession();

// 聚焦输入元素
await page.focus('input');

// 输入消息
await client.send('Input.type', {
  text: 'what is the best place to try pizza and pasta?'
});
```

## 自定义客户端 SSL/TLS 证书

在特定域名认证需要时，使用此命令安装自定义客户端 SSL/TLS 证书。这些证书在**单个** Browser API 会话期间有效，会话结束后会自动移除。

<AccordionGroup>
  <Accordion title="Browser.addCertificate">
    ```javascript theme={null}
    Browser.addCertificate(params: {
      cert: string // base64 编码的证书文件
      pass: string // 证书密码
    }) : void
    ```
  </Accordion>

  <Accordion title="代码示例">
    * 将示例值 `SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD` 替换为您有效的 Browser API 凭据。
    * 将 `client.pfx` 替换为您证书文件的实际路径。该文件应为 .pfx 格式的有效 SSL/TLS 客户端证书。
    * 将 `secret` 替换为该证书的实际密码。

          <CodeGroup>
            ```js NodeJS - Puppeteer theme={null}
            const puppeteer = require('puppeteer-core');
            const fs = require('fs/promises');
            const {
              AUTH = 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD',
              TARGET_URL = 'https://example.com',
              CERT_FILE = 'client.pfx',
              CERT_PASS = 'secret',
            } = process.env;
            async function scrape(url = TARGET_URL, file = CERT_FILE, pass = CERT_PASS) {
              if (AUTH == 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD') {
                throw new Error(`Provide Browser API credentials in AUTH`
                    + ` environment variable or update the script.`);
              }
              console.log(`Connecting to Browser...`);
              const browserWSEndpoint = `wss://${AUTH}@brd.superproxy.io:9222`;
              const browser = await puppeteer.connect({ browserWSEndpoint });
              try {
                console.log(`Connected! Installing ${file} certificate...`);
                const page = await browser.newPage();
                const client = await page.createCDPSession();
                const cert = (await fs.readFile(CERT_FILE)).toString('base64');
                await client.send('Browser.addCertificate', { cert, pass });
                console.log(`Installed! Navigating to ${url}...`);
                await page.goto(url, { timeout: 2 * 60 * 1000 });
                console.log(`Navigated! Scraping page content...`);
                const data = await page.content();
                console.log(`Scraped! Data: ${data}`);
              } finally {
                await browser.close();
              }
            }
            scrape();
            ```

            ```python Python - Selenium theme={null}
            from os import environ
            from base64 import standard_b64encode
            from selenium.webdriver import Remote, ChromeOptions as Options
            from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection as Connection
            AUTH = environ.get('AUTH', default='SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD')
            TARGET_URL = environ.get('TARGET_URL', default='https://example.com')
            CERT_FILE = environ.get('CERT_FILE', default='client.pfx')
            CERT_PASS = environ.get('CERT_PASS', default='secret')
            def scrape(url=TARGET_URL, file=CERT_FILE, pswd=CERT_PASS):
                if AUTH == 'SBR_ZONE_FULL_USERNAME:SBR_ZONE_PASSWORD':
                   raise Exception('Provide Browser API credentials in AUTH '
                                'environment variable or update the script.')
                print('Connecting to Browser...')
                server_addr = f'https://{AUTH}@brd.superproxy.io:9515'
                connection = Connection(server_addr, 'goog', 'chrome')
                driver = Remote(connection, options=Options())
                try:
                    print(f'Connected! Installing {file} certificate...')
                    with open(file, 'rb') as f:
                        cert = standard_b64encode(f.read()).decode()
                    driver.execute('executeCdpCommand', {
                        'cmd': 'Browser.addCertificate',
                        'params': {'cert': cert, 'pass': pswd},
                    })
                    print(f'Installed! Navigating to {url}...')
                    driver.get(url)
                    print('Navigated! Scraping page content...')
                    data = driver.page_source
                    print(f'Scraped! Data: {data}')
                finally:
                    driver.quit()
            scrape()
            ```
          </CodeGroup>
  </Accordion>
</AccordionGroup>
