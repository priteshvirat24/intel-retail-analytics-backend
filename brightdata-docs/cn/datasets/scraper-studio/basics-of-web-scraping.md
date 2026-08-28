> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Scraper Studio 网页爬取基础

> 了解 Bright Data Scraper Studio 中网页爬取的核心概念：导航、解析、worker 类型、阶段，以及如何应对规模化带来的封锁问题。

您在 Bright Data Scraper Studio 中构建的每个爬虫都由两部分组成：导航目标站点的 **interaction code（交互代码）** 和从所得 HTML 中提取结构化数据的 **parser code（解析器代码）**。本页将带您过一遍这些核心概念，让您能够自信地阅读、编写并调试爬虫。

## 前提条件

* 基础的 JavaScript 知识（变量、函数、异步控制流）
* 一个已激活的 [Bright Data 账户](https://www.bright.cn/)

## 爬虫的两个阶段是什么？

Bright Data Scraper Studio 爬虫在每个页面上分两个阶段运行：

1. **Interaction（交互）** 在站点内移动以到达数据。这包括发送 GET 或 POST 请求、跟随链接、处理分页、提交表单；在 Browser worker 上还包括点击、输入、滚动以及等待元素出现。
2. **Parsing（解析）** 读取页面 HTML（或捕获到的 JSON 负载）并返回一条结构化记录。

目标页面加载完成后，从交互代码中调用 `parse()`。这会运行解析器代码并返回其结果。随后调用 `collect()` 将记录追加到最终数据集：

```js theme={null}
let data = parse();
collect({
  url: new URL(location.href),
  title: data.title,
  links: data.links,
});
```

解析器代码本身使用 Cheerio（一个类 jQuery 的 API）来提取字段：

```js theme={null}
return {
  title: $('h1').text().trim(),
  links: $('a').toArray().map(e => new URL($(e).attr('href'))),
};
```

## 如何构建多阶段爬虫？

许多爬取任务需要多次跳转，例如"访问搜索页面，然后跟随每个结果 URL，再提取每个产品"。Bright Data Scraper Studio 通过 stages（阶段）来处理这种情况。每个阶段都是独立的浏览器会话，`next_stage({...})` 会将一个新输入排队给下一个阶段。

下面的示例对一个电商网站的搜索结果进行跨页爬取，并跟随每条列表进入其详情页。

**阶段 1：分发搜索结果页**

```js theme={null}
let search_url = `https://example.com/search?q=${input.keyword}`;
navigate(search_url);
let max_page = parse().max_page;
for (let i = 1; i <= max_page; i++) {
  let search_page = new URL(search_url);
  if (i > 1)
    search_page.searchParams.set('page', i);
  next_stage({search_page});
}
```

**阶段 2：从每个结果页分发列表 URL**

```js theme={null}
navigate(input.search_page);
let listings = parse().listings;
for (let listing_url of listings)
  next_stage({listing_url});
```

**阶段 3：收集最终的产品记录**

```js theme={null}
navigate(input.listing_url);
collect(parse());
```

流程如下：

1. 阶段 1 导航到搜索页并解析出总页数。
2. 阶段 1 对每个结果页调用一次 `next_stage({search_page})`，每次调用都会成为阶段 2 的一个新输入。
3. 阶段 2 导航到每个结果页并解析出所有列表 URL。
4. 阶段 2 对每条列表调用一次 `next_stage({listing_url})`，每次调用都会成为阶段 3 的一个新输入。
5. 阶段 3 导航到每个产品页并调用 `collect(parse())` 将记录加入数据集。

Bright Data Scraper Studio 会自动将各阶段并行到多个 worker 上，因此使用 `next_stage()` 分发比在单一阶段中串行翻页快得多。

## 应该使用哪种 worker 类型？

Bright Data Scraper Studio 提供两种 worker 类型：

* **Browser worker**：真实的无头浏览器。在页面通过 JavaScript 渲染数据，或需要点击、滚动、输入或捕获网络流量时使用。
* **Code worker**：原始 HTTP 请求。更快也更便宜，但无法运行 JavaScript 或与页面交互。

建议先用 Code worker。只有当所需数据不在原始 HTTP 响应中时，再切换到 Browser worker。您可以随时在同一爬虫上更换 worker 类型，但仅限浏览器使用的函数（`wait`、`click`、`scroll_*`、`tag_*`、`type` 等）在 Code worker 上调用时会抛错。完整列表参见 [Worker 类型](/cn/datasets/scraper-studio/worker-types)。

## Scraper Studio 如何处理封锁与 CAPTCHA？

规模化爬取每次都会遇到同一类防御：IP 封锁、速率限制、CAPTCHA、指纹识别和机器人检测。Bright Data Scraper Studio 通过 Bright Data 的[代理基础设施](/cn/proxy-networks/introduction)和 [Web Unlocker API](/cn/scraping-automation/web-unlocker) 路由每个请求，因此爬虫会：

* 根据爬虫设置在住宅、ISP、数据中心或移动 IP 之间轮换
* 自动用新的对端会话重试被封锁的请求
* 在您调用 `solve_captcha()` 时解决常见 CAPTCHA
* 在 Browser worker 上模拟真实浏览器指纹

您无需自行管理代理、会话或重试。专注于编写提取所需数据的爬虫代码，访问问题交给平台。

## 相关内容

<CardGroup cols={2}>
  <Card title="Worker 类型" icon="server" href="/cn/datasets/scraper-studio/worker-types">
    在 Browser worker 与 Code worker 之间做选择
  </Card>

  <Card title="Scraper Studio 函数参考" icon="code" href="/cn/datasets/scraper-studio/functions">
    交互命令与解析器命令的完整参考
  </Card>

  <Card title="开发爬虫" icon="wrench" href="/cn/datasets/scraper-studio/develop-a-scraper">
    在 IDE 中构建爬虫的分步演练
  </Card>

  <Card title="最佳实践" icon="list-check" href="/cn/datasets/scraper-studio/best-practices">
    构建快速、可靠爬虫的推荐模式
  </Card>
</CardGroup>
