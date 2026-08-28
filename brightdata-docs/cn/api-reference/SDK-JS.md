> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# JavaScript SDK

> 安装并使用 Bright Data JavaScript SDK 从 Node.js 抓取 URL、搜索 Google/Bing/Yandex、调用平台 scrapers，并连接 Browser API。

本指南介绍如何安装 Bright Data JavaScript SDK 并在 Node.js 中抓取 URL、运行搜索、调用平台专用 scrapers（LinkedIn、Amazon、Instagram 等）、连接 Browser API 与 Scraper Studio。

### 安装包

打开终端并运行：

```bash theme={null}
npm install @brightdata/sdk
```

在你的代码文件中，导入包并发起第一次请求：

```javascript theme={null}
import { bdclient } from '@brightdata/sdk';

const client = new bdclient({ apiKey: 'YOUR_API_KEY' });

const html = await client.scrapeUrl('https://example.com');
const google = await client.search.google('pizza restaurants');

console.log(google);
await client.close();
```

### 发起抓取和网络搜索

<CodeGroup>
  ```javascript search(...) theme={null}
  import { bdclient } from '@brightdata/sdk';

  const client = new bdclient({ apiKey: 'YOUR_API_KEY' });

  const google = await client.search.google('best laptops 2026');
  const bing = await client.search.bing('python tutorial');
  const yandex = await client.search.yandex('AI news');

  console.log({ google, bing, yandex });
  await client.close();
  ```

  ```javascript scrape(...) theme={null}
  import { bdclient } from '@brightdata/sdk';

  const client = new bdclient({ apiKey: 'YOUR_API_KEY' });

  const html = await client.scrapeUrl('https://example.com');
  const md = await client.scrapeUrl('https://example.com', {
      dataFormat: 'markdown',
      country: 'us',
  });

  console.log({ html, md });
  await client.close();
  ```
</CodeGroup>

### 平台 scrapers 与数据集

按 URL 采集主流平台数据，或按参数发现内容。

<CodeGroup>
  ```javascript LinkedIn theme={null}
  import { bdclient } from '@brightdata/sdk';

  const client = new bdclient({ apiKey: 'YOUR_API_KEY' });

  // 按 URL 采集
  const profiles = await client.scrape.linkedin.collectProfiles([
      'https://www.linkedin.com/in/satyanadella/',
  ]);
  const companies = await client.scrape.linkedin.collectCompanies([
      'https://www.linkedin.com/company/bright-data',
  ]);
  const jobs = await client.scrape.linkedin.collectJobs([
      'https://www.linkedin.com/jobs/view/123456',
  ]);
  const posts = await client.scrape.linkedin.collectPosts([
      'https://www.linkedin.com/feed/update/urn:li:activity:123',
  ]);

  // 按参数发现
  const byKeyword = await client.scrape.linkedin.discoverJobs(
      [{ keyword: 'python developer', location: 'New York', remote: true }],
      {}
  );
  const byName = await client.scrape.linkedin.discoverProfiles(
      [{ firstName: 'John', lastName: 'Doe' }],
      {}
  );
  const compPosts = await client.scrape.linkedin.discoverCompanyPosts(
      [{ url: 'https://www.linkedin.com/company/bright-data' }],
      {}
  );
  const userPosts = await client.scrape.linkedin.discoverUserPosts(
      [{ url: 'https://www.linkedin.com/in/satyanadella' }],
      {}
  );
  ```

  ```javascript Amazon theme={null}
  import { bdclient } from '@brightdata/sdk';

  const client = new bdclient({ apiKey: 'YOUR_API_KEY' });

  // 按 URL 采集
  const products = await client.scrape.amazon.collectProducts(
      ['https://www.amazon.com/dp/B0D77BX8Y4'],
      {}
  );
  const reviews = await client.scrape.amazon.collectReviews(
      ['https://www.amazon.com/dp/B0D77BX8Y4'],
      {}
  );
  const sellers = await client.scrape.amazon.collectSellers(
      ['https://www.amazon.com/sp?seller=AXXX'],
      {}
  );

  // 按参数发现
  const byKeyword = await client.scrape.amazon.discoverProductsByKeyword(
      [{ keyword: 'wireless headphones' }],
      {}
  );
  const byCategory = await client.scrape.amazon.discoverProductsByCategoryURL(
      ['https://amazon.com/s?category=electronics'],
      {}
  );
  const byBSUrl = await client.scrape.amazon.discoverProductsByBestSellerURL(
      ['https://amazon.com/gp/bestsellers/electronics'],
      {}
  );

  // 一次调用编排（触发、轮询并返回）
  const result = await client.scrape.amazon.products([
      'https://www.amazon.com/dp/B0D77BX8Y4',
  ]);
  ```

  ```javascript Instagram theme={null}
  const profiles = await client.scrape.instagram.collectProfiles([
      'https://www.instagram.com/natgeo/',
  ]);
  const posts = await client.scrape.instagram.collectPosts([
      'https://www.instagram.com/p/ABC123/',
  ]);
  const reels = await client.scrape.instagram.collectReels([
      'https://www.instagram.com/reel/XYZ789/',
  ]);
  const comments = await client.scrape.instagram.collectComments([
      'https://www.instagram.com/p/ABC123/',
  ]);
  ```

  ```javascript Facebook theme={null}
  const profilePosts = await client.scrape.facebook.collectPostsByProfile([
      'https://www.facebook.com/nasa',
  ]);
  const groupPosts = await client.scrape.facebook.collectPostsByGroup([
      'https://www.facebook.com/groups/example',
  ]);
  const postByUrl = await client.scrape.facebook.collectPostsByUrl([
      'https://www.facebook.com/post/123456',
  ]);
  const comments = await client.scrape.facebook.collectComments([
      'https://www.facebook.com/post/123456',
  ]);
  const reels = await client.scrape.facebook.collectReels([
      'https://www.facebook.com/nasa',
  ]);
  ```

  ```javascript TikTok theme={null}
  const profiles = await client.scrape.tiktok.collectProfiles([
      'https://www.tiktok.com/@tiktok',
  ]);
  const posts = await client.scrape.tiktok.collectPosts([
      'https://www.tiktok.com/@user/video/7433494424040017194',
  ]);
  const comments = await client.scrape.tiktok.collectComments([
      'https://www.tiktok.com/@user/video/7216019547806092550',
  ]);
  ```

  ```javascript YouTube theme={null}
  const videos = await client.scrape.youtube.collectVideos([
      'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
  ]);
  ```

  ```javascript Reddit theme={null}
  const posts = await client.scrape.reddit.collectPosts([
      'https://www.reddit.com/r/technology/top/',
  ]);
  ```

  ```javascript ChatGPT / Perplexity / Digikey / Pinterest theme={null}
  const chatgpt = await client.scrape.chatGPT.search([
      'What are the latest trends in AI?',
  ]);
  const perplexity = await client.scrape.perplexity.search([
      'Latest breakthroughs in battery tech?',
  ]);
  const parts = await client.scrape.digikey.collectProducts([
      'https://www.digikey.com/en/products/detail/abc',
  ]);
  const pins = await client.scrape.pinterest.collectPosts([
      'https://www.pinterest.com/pin/123456',
  ]);
  ```
</CodeGroup>

### Discover API

一次调用即可搜索网页并返回 AI 排序的结果，或者手动触发与轮询。

```javascript theme={null}
// 一次调用：搜索、轮询并返回 AI 排序结果
const result = await client.discover('AI trends 2026', {
    intent: 'latest technology developments',
});
// result.data 形如 [{ title, link, description, relevance_score }]

// 手动：触发、等待并获取
const job = await client.discoverTrigger('SaaS pricing', {
    intent: 'competitor pricing strategies',
});
await job.wait({ timeout: 60_000 });
const data = await job.fetch();
```

### Scraper Studio

通过 SDK 运行您的自定义 Scraper Studio 采集器。

```javascript theme={null}
// 一次调用即可运行并获取结果
const results = await client.scraperStudio.run('c_your_collector_id', {
    input: { url: 'https://example.com/product/1' },
});
// results 形如 [{ input, data, error, responseId, elapsedMs }]

// 手动：触发、等待并获取
const job = await client.scraperStudio.trigger('c_your_collector_id', {
    url: 'https://example.com/product/1',
});
const data = await job.waitAndFetch();

// 查询状态
const status = await client.scraperStudio.status('j_abc123');
// status.status 取值为 'queued' | 'running' | 'done' | 'failed'
```

### Browser API

将 Playwright 连接到 Bright Data 的云端浏览器。

```javascript theme={null}
import { bdclient } from '@brightdata/sdk';
import { chromium } from 'playwright';

const client = new bdclient({
    apiKey: 'YOUR_API_KEY',
    browserUsername: 'brd-customer-xxxx-zone-scraping_browser1',
    browserPassword: 'YOUR_ZONE_PASSWORD',
});

const browser = await chromium.connectOverCDP(client.browser.getConnectUrl());
const page = await browser.newPage();
await page.goto('https://example.com');
await browser.close();
await client.close();
```

### Datasets API

查询并下载 Bright Data 126+ 数据集中的任意一项。

```javascript theme={null}
const ds = client.datasets;

// 查询，然后下载
const snapshotId = await ds.instagramProfiles.query(
    { url: 'https://www.instagram.com/natgeo/' },
    { records_limit: 10 }
);
const rows = await ds.instagramProfiles.download(snapshotId);

// 整个数据集目录使用相同模式
await ds.amazonProducts.query({ url: 'https://amazon.com/dp/B123' });
await ds.linkedinProfiles.query({ url: 'https://linkedin.com/in/johndoe' });
await ds.imdbMovies.query({}, { records_limit: 50 });
await ds.redditPosts.query({ subreddit: 'technology' });
await ds.glassdoorReviews.query({ company: 'Bright Data' });

// 获取字段元数据
const meta = await ds.instagramProfiles.getMetadata();
```

### 客户端与方法参数

<AccordionGroup>
  <Accordion title="Client" description="客户端参数" icon="circle-info">
    | 参数                  | 类型        | 说明                                                            | 默认值      |
    | ------------------- | --------- | ------------------------------------------------------------- | -------- |
    | `apiKey`            | `string`  | 你的 API key（也可通过 `BRIGHTDATA_API_KEY` 环境变量提供）                  | .        |
    | `autoCreateZones`   | `boolean` | 当 zone 不存在时自动创建                                               | `true`   |
    | `webUnlockerZone`   | `string`  | 自定义 Web Unlocker zone 名称                                      | .        |
    | `serpZone`          | `string`  | 自定义 SERP zone 名称                                              | .        |
    | `browserUsername`   | `string`  | Browser API 用户名（也可通过 `BRIGHTDATA_BROWSERAPI_USERNAME` 环境变量提供） | .        |
    | `browserPassword`   | `string`  | Browser API 密码（也可通过 `BRIGHTDATA_BROWSERAPI_PASSWORD` 环境变量提供）  | .        |
    | `logLevel`          | `string`  | 日志级别                                                          | `'INFO'` |
    | `structuredLogging` | `boolean` | 使用结构化 JSON 日志                                                 | `true`   |
    | `verbose`           | `boolean` | 启用详细日志                                                        | `false`  |

    ```javascript theme={null}
    const client = new bdclient({
        apiKey: 'YOUR_API_KEY',
        autoCreateZones: true,
        webUnlockerZone: 'unlocker_zone1',
        serpZone: 'serp_zone1',
        browserUsername: 'brd-customer-xxxx-zone-scraping_browser1',
        browserPassword: 'YOUR_ZONE_PASSWORD',
        logLevel: 'INFO',
        structuredLogging: true,
        verbose: false,
    });
    ```
  </Accordion>

  <Accordion title="Search" description="高级搜索参数" icon="magnifying-glass-chart">
    使用 SERP API 搜索网页。

    | 参数                     | 类型                                     | 说明                     | 默认值        |
    | ---------------------- | -------------------------------------- | ---------------------- | ---------- |
    | `query`                | `string \| string[]`                   | 搜索查询字符串或查询数组           | .          |
    | `options.searchEngine` | `'google' \| 'bing' \| 'yandex'`       | 搜索引擎                   | `'google'` |
    | `options.zone`         | `string`                               | Zone 标识（如为 null 则自动配置） | .          |
    | `options.format`       | `'json' \| 'raw'`                      | 响应格式                   | `'raw'`    |
    | `options.method`       | `string`                               | HTTP 方法                | `'GET'`    |
    | `options.country`      | `string`                               | 两位字母国家代码               | `''`       |
    | `options.dataFormat`   | `'markdown' \| 'screenshot' \| 'html'` | 返回内容格式                 | `'html'`   |
    | `options.concurrency`  | `number`                               | 最大并发 worker 数          | `10`       |
    | `options.timeout`      | `number (ms)`                          | 请求超时                   | `30000`    |
  </Accordion>

  <Accordion title="Scrape" description="高级抓取参数" icon="spider">
    使用 Web Unlocker API 抓取单个 URL 或 URL 列表。

    | 参数                    | 类型                                     | 说明                     | 默认值      |
    | --------------------- | -------------------------------------- | ---------------------- | -------- |
    | `url`                 | `string \| string[]`                   | 单个 URL 字符串或 URL 数组     | .        |
    | `options.zone`        | `string`                               | Zone 标识（如为 null 则自动配置） | .        |
    | `options.format`      | `'json' \| 'raw'`                      | 响应格式                   | `'raw'`  |
    | `options.method`      | `string`                               | HTTP 方法                | `'GET'`  |
    | `options.country`     | `string`                               | 两位字母国家代码               | `''`     |
    | `options.dataFormat`  | `'markdown' \| 'screenshot' \| 'html'` | 返回内容格式                 | `'html'` |
    | `options.concurrency` | `number`                               | 最大并发 worker 数          | `10`     |
    | `options.timeout`     | `number (ms)`                          | 请求超时                   | `30000`  |
  </Accordion>

  <Accordion title="saveResults" description="将内容保存到本地文件" icon="floppy-disk">
    | 参数                 | 类型                         | 说明                   | 默认值 |
    | ------------------ | -------------------------- | -------------------- | --- |
    | `content`          | `any`                      | 要保存的内容               | .   |
    | `options.filename` | `string`                   | 输出文件名（如为 null 则自动生成） | .   |
    | `options.format`   | `'json' \| 'csv' \| 'txt'` | 文件格式                 | .   |
  </Accordion>
</AccordionGroup>

### 错误处理

<AccordionGroup>
  <Accordion title="日志" description="启用高级日志" icon="ballot">
    在 Client 中启用 `VERBOSE` 可获取高级日志（见客户端参数）。使用 `listZones()` 函数可查询可用 zones。
  </Accordion>

  <Accordion title="身份验证" description="Bright Data 身份验证" icon="rectangle-barcode">
    创建一个 [Bright Data](https://www.bright.cn/) 账户并复制您的 API key。前往 [账户设置](https://www.bright.cn/cp/setting/users)，并确保您的 API key 拥有 **管理员权限**。
  </Accordion>
</AccordionGroup>

### 资源

<CardGroup cols="3">
  <Card title="GitHub" icon="github" iconType="light" href="https://github.com/brightdata/bright-data-sdk-js?tab=readme-ov-file" cta>
    访问 Bright Data SDK 的 GitHub 仓库
  </Card>
</CardGroup>
