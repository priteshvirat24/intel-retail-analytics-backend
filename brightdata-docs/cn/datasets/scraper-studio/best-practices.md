> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Scraper Studio IDE 最佳实践

> Bright Data Scraper Studio IDE 最佳实践：无效页面检测、请求合并、分页、弹窗、超时、重试与解析器代码。

本指南介绍 Bright Data Scraper Studio 团队推荐的编码模式，帮助您在 IDE 中编写快速、可靠的爬虫。每个章节都对比一种常见错误与推荐写法，并解释原因。

## 如何可靠地检测无效页面？

使用 `navigate()` 时，添加 `dead_page()` 条件，避免爬虫对不存在的页面进行重试。Bright Data Scraper Studio 会自动将 HTTP 404 响应标记为无效，但许多站点会返回 200 加一个"未找到"模板，因此需要您自行检测。

不要把 `wait()` 包在 `try/catch` 中，再从 `catch` 块里调用 `dead_page()`。`wait()` 抛错只能说明选择器在超时窗口内未出现，并不能证明页面真的不存在。

<CodeGroup>
  ```js Bad theme={null}
  try {
    // 即使页面已无效，也会等待 30 秒查找 'ok-selector'
    wait('ok-selector');
  } catch (e) {
    // 仅凭 wait 超时无法证明页面无效
    dead_page("Page doesn't exist");
  }
  ```

  ```js Good theme={null}
  wait('ok-selector, 404-selector');
  if (el_exists('404-selector'))
    dead_page();
  ```
</CodeGroup>

## 如何减少对浏览器的请求次数？

`click`、`type`、`el_exists`、`el_is_visible`、`wait`、`wait_visible` 等交互命令都会向浏览器发送一次请求。请把多个选择器合并到一次调用中，而不是串联多次调用。

<CodeGroup>
  ```js Bad theme={null}
  if (!(el_exists('#price1')) || el_exists('#price2')
    || el_exists('#price3') || el_exists('#discount'))
  {
      dead_page('No price found');
  }
  ```

  ```js Good theme={null}
  if (!el_exists('#price1, #price2, #price3, #discount'))
    dead_page('No price found');
  ```
</CodeGroup>

## 如何在不阻碍并行化的前提下处理分页？

当站点有分页结果、您又需要每一页的数据时，应在根页面上为每一页调用一次 `rerun_stage()`。不要在每页内顺序爬取分页时再调用 `rerun_stage()`，那样会把工作串行化，Bright Data Scraper Studio 无法并行处理请求。

<CodeGroup>
  ```js Bad theme={null}
  navigate(input.url);
  let $ = load_html(html());
  let next_page_url = $('.next_page').attr('href');
  rerun_stage({url: next_page_url});
  ```

  ```js Good theme={null}
  let url = new URL(input.url);
  if (input.page)
      url.searchParams.set('page', input.page);
  navigate(url);
  // 只有当本阶段被针对某一页重新运行时，input.page 才存在。
  // 根页面上 input.page 为 undefined，逻辑会继续向下分发。
  if (input.page)
      return;

  let $ = load_html(html());
  let total_products = +$('.total_pages').text();
  let total_pages = Math.ceil(total_products / 20);
  total_pages = Math.min(total_pages, 50);

  for (let page = 2; page <= total_pages; page++)
      rerun_stage({url: input.url, page});
  ```
</CodeGroup>

避免在单个会话中收集所有页面。每个会话有 16MB 的结果大小限制，该限制统计会话中累积的全部数据，包括所有已收集的行、解析结果、子项和解析器元数据，而不仅仅是渲染页面的大小。为每一页调用一次 `rerun_stage({url: input.url, page})`，即可让每个会话只处理一页，并使每个会话保持在限制之内。

## 如何在不等待的情况下关闭弹窗？

使用 `close_popup('popup_selector', 'close_button_selector')` 注册一个后台监视器，让它在弹窗出现时自动关闭。不要在每次交互前用 `wait_visible()` 轮询弹窗：弹窗可能随时出现，而显式等待会给每一步都增加延迟。

<CodeGroup>
  ```js Bad theme={null}
  navigate('https://example.com');
  try {
    wait_visible('.cky-btn-accept', {timeout: 5000});
    click('.cky-btn-accept');
  } catch (e) {
      console.log('Accept cookies button does not exist, continue');
  }
  ```

  ```js Good theme={null}
  // 在后台运行，不会给每一步增加延迟。
  // 监视器会在每次交互前自动检查弹窗。
  close_popup('.cky-btn-accept', '.cky-btn-accept');
  navigate('https://example.com');
  click('.open-product-full-info');
  ```
</CodeGroup>

## 解析前如何等待已标记的响应？

使用 `tag_response()` 捕获后台 API 调用后，紧接着调用 `wait_for_parser_value()` 以确保请求在读取 `parser` 之前已经完成。否则，解析器可能在响应到达之前就运行，导致 `parser.<字段>` 为 `undefined`。

<CodeGroup>
  ```js Bad theme={null}
  tag_response('product', /api\/product/);
  navigate('https://example.com');

  // 解析器代码：
  // 请求可能尚未完成，product 可能是 undefined
  let {product} = parser;
  return product.data;
  ```

  ```js Good theme={null}
  tag_response('product', /api\/product/);
  navigate('https://example.com');
  wait_for_parser_value('product');

  // 解析器代码：
  let {product} = parser;
  return product.data;
  ```

  ```js Good (链式导航) theme={null}
  tag_response('product', /api\/product/);
  navigate('https://example.com');

  // wait_for_parser_value 会返回值，方便在交互代码中使用
  let product = wait_for_parser_value('product');
  navigate(product.reviews_url);
  tag_html('reviews_html');

  // 解析器代码：
  let {product, reviews_html} = parser;
  let $ = load_html(reviews_html);
  let reviews = $('.review').toArray().map(v => $(v).text());
  return {
    ...product.data,
    reviews,
  };
  ```
</CodeGroup>

## 是否应该抛出自定义错误信息？

不应该。让 Bright Data Scraper Studio 的内置错误自然冒出。内置错误会附带选择器、超时时间和阶段信息，比手写的 "Page not loaded properly" 更有用。只有当您要检查平台无法自行识别的、领域相关的条件时（例如缺少产品标题），才需要抛出自定义错误。

<CodeGroup>
  ```js Bad theme={null}
  try {
    wait('selector1');
    // some code
    wait('selector2');
    // some code
  } catch (e) {
    throw "Page not loaded properly"
  }
  ```

  ```js Good theme={null}
  // Crawler error: waiting for selector "selector1" failed: timeout 30000ms exceeded
  wait('selector1');
  // some code
  wait('selector2');
  // some code
  ```

  ```js Good (领域相关检查) theme={null}
  if (!el_exists('.product-title'))
      throw new Error('Failed to load product page');
  ```
</CodeGroup>

## 如何在不过度延长超时的前提下应对响应慢的站点？

大多数等待保持默认的 30 秒超时即可。如果某个特定页面长期较慢，可将超时上调到 45 或 60 秒。不要超过 60 秒：原因通常是 peer 较慢，而 Bright Data Scraper Studio 在页面报告超时错误后会自动用新的 peer 会话重试。

<CodeGroup>
  ```js Bad theme={null}
  // 120 秒太长；平台无法回收卡住的 peer
  wait('selector', {timeout: 120000});
  ```

  ```js Good theme={null}
  wait('selector');                       // 默认 30 秒
  wait('selector', {timeout: 45000});     // 略慢的页面用 45 秒
  wait('selector', {timeout: 60000});     // 长期较慢的页面用 60 秒
  ```
</CodeGroup>

## 是否应该自己写重试循环？

不应该。Bright Data Scraper Studio 在任务层面会用新的 peer 会话进行重试。在爬虫内部写自定义重试循环会复用同一个会话，而这正是第一次失败的根源。报告错误，把重试交给平台。

<CodeGroup>
  ```js Bad theme={null}
  let counter = input.counter || 5;
  while (counter > 1) {
    try {
      wait('selector', {timeout: 500});
      click('selector');
      type('selector');
      // some code
      break;
    } catch (e) {
      // rerun_stage 会创建新会话，但这种模式会消耗额外 CPM
      return rerun_stage({...input, counter: --counter});
    }
  }
  ```

  ```js Good theme={null}
  navigate('https://example.com');
  wait('h1');
  ```
</CodeGroup>

## 是否应该在解析器表达式外面包 try/catch？

不应该。改用可选链（`?.`）和空值合并（`??`）。属性访问外面包一层静默的 `try/catch` 会掩盖真实的 bug；包在 `wait()` 外的 `try/catch` 则会浪费浏览器时间。

<CodeGroup>
  ```js Bad theme={null}
  try {
    const example = obj.prop;
  } catch (e) {}
  ```

  ```js Bad theme={null}
  // 无谓地浪费浏览器时间
  try { wait('selector'); } catch (e) {}
  try { wait_network_idle({timeout: 8000}); } catch (e) {}
  try { wait_page_idle(); } catch (e) {}
  ```

  ```js Good theme={null}
  const example = object?.prop;
  const example2 = object.prop ?? undefined;
  const example3 = object.prop ? object.prop : undefined;
  ```
</CodeGroup>

## 解析器代码中如何从一组元素提取值？

使用 `toArray().map()` 而不是 `each()`。前者更短、返回真正的数组，并且作为单一表达式可读性更好。

<CodeGroup>
  ```js Bad theme={null}
  const links = [];
  $('.card.product-wrapper').each(function (i, el) {
    links.push({url: $(this).find('h4 a').attr('href')});
  })
  return links;
  ```

  ```js Good theme={null}
  const links = $('.card.product-wrapper').toArray().map(v => ({
    url: $(v).find('h4 a').attr('href'),
  }));
  ```
</CodeGroup>

## 解析器代码中如何规范化文本？

调用 `$(selector).text_sane()`。Bright Data Scraper Studio 在 Cheerio 原型上扩展了这个方法：它会把每一段连续空白折叠为单个空格并对结果进行 trim。对于数字提取，使用正则去掉非数字。

<CodeGroup>
  ```js Bad theme={null}
  $.prototype.clearText = function () {
    return this.text().replace(/\s+/g, ' ').trim();
  }
  ```

  ```js Good theme={null}
  let name = $('a').text_sane();

  // 仅提取数字时：
  let value = +$('a').text().replace(/\D+/g, '');
  ```
</CodeGroup>

## 相关内容

<CardGroup cols={2}>
  <Card title="Scraper Studio 函数参考" icon="code" href="/cn/datasets/scraper-studio/functions">
    Bright Data Scraper Studio 交互命令与解析器命令的完整参考
  </Card>

  <Card title="Worker 类型" icon="server" href="/cn/datasets/scraper-studio/worker-types">
    为您的爬虫在 Browser worker 与 Code worker 之间做选择
  </Card>
</CardGroup>
