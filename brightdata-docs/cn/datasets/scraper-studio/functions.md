> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Scraper Studio 函数参考

> Bright Data Scraper Studio 交互与解析函数参考：导航、等待、选择器和解析辅助函数，含参数说明和 30 多个示例。

本参考文档记录了 Bright Data Scraper Studio IDE 中可用的每一个函数：控制浏览器会话的交互代码，以及将 HTML 转换为结构化记录的解析代码。每个函数都列出其参数、返回值和一个可运行的示例。

<Note>
  标有 **⭐** 的函数仅在 Browser worker 中有效，从 Code worker 调用时会抛出错误。完整列表见 [仅限浏览器的函数](#browser-only-functions)。
</Note>

## Scraper Studio 代码是如何组织的？

Bright Data Scraper Studio 抓取器使用两种代码类型：

| 代码类型 | 作用                            | 语言和库                           |
| ---- | ----------------------------- | ------------------------------ |
| 交互代码 | 导航目标站点：URL 请求、点击、滚动、等待和后台流量捕获 | JavaScript + Bright Data 浏览器命令 |
| 解析代码 | 从交互代码返回的 HTML 中提取并结构化数据       | JavaScript + Cheerio（`$`）      |

你可以通过 `parse()`（运行解析器）和 `collect()`（将一条记录追加到最终数据集）在两者之间传递数据。

## 交互函数

交互函数在抓取器的主 JavaScript 上下文中运行，并驱动浏览器或 HTTP 客户端。使用它们来导航、等待元素、与页面交互、捕获网络流量以及将数据移交给解析器。

### 全局对象

| 名称         | 类型     | 描述                                                                          |
| ---------- | ------ | --------------------------------------------------------------------------- |
| `input`    | object | 当前阶段的输入，由触发器或前一个 `next_stage()`/`run_stage()`/`rerun_stage()` 调用设置。         |
| `job`      | object | 有关当前作业的元数据（例如 `job.created`，作业开始时间戳）。                                       |
| `location` | object | 有关当前浏览器位置的信息。字段：`href`。                                                     |
| `parser`   | object | 由 `tag_response`、`tag_script` 及相关标记函数捕获的值，在 `wait_for_parser_value()` 之后可用。 |

```js theme={null}
navigate(input.url);
let {created} = job;
console.log('current url', location.href);
```

### 导航

#### `navigate`，在浏览器中加载 URL

将浏览器导航到某个 URL。默认情况下，404 状态会抛出 `dead_page` 错误；使用 `allow_status` 可覆盖此行为。

**参数**

| 参数                 | 类型           | 必填 | 默认值     | 描述                                                        |
| ------------------ | ------------ | -- | ------- | --------------------------------------------------------- |
| `url`              | string 或 URL | 是  | ,       | 目标 URL                                                    |
| `opt.wait_until`   | string       | 否  | `load`  | `load`、`domcontentloaded`、`networkidle0` 或 `networkidle2` |
| `opt.timeout`      | number       | 否  | `30000` | 导航超时（毫秒）                                                  |
| `opt.referer`      | string       | 否  | ,       | 要发送的 `Referer` 请求头                                        |
| `opt.allow_status` | number\[]    | 否  | `[]`    | 接受而不抛出错误的 HTTP 状态码                                        |
| `opt.fingerprint`  | object       | 否  | ,       | 覆盖浏览器指纹（`screen.width`、`screen.height`）                   |

```js theme={null}
navigate(input.url);
navigate('https://example.com');
navigate('https://example.com', {wait_until: 'domcontentloaded'});
navigate('https://example.com', {referer: 'https://google.com'});
navigate('https://example.com', {timeout: 45000});
navigate('https://example.com', {allow_status: [404]});
navigate('https://example.com', {
  fingerprint: {screen: {width: 400, height: 400}},
});
```

#### `request`，发起直接 HTTP 请求

不使用浏览器发送 HTTP 请求。可在 Code worker 上使用，或在 Browser worker 上使用（当你想绕过浏览器时）。

**参数**

| 参数                 | 类型              | 必填 | 描述                                              |
| ------------------ | --------------- | -- | ----------------------------------------------- |
| `url` \| `options` | string 或 object | 是  | URL 字符串，或包含 `url`、`method`、`headers`、`body` 的对象 |

```js theme={null}
let res = request('https://www.example.com');
let res = request({
  url: 'https://www.example.com',
  method: 'POST',
  headers: {'Content-type': 'application/json'},
  body: {hello: 'world'},
});
```

#### `next_stage`，为下一阶段排队输入

在新的浏览器会话中使用给定输入运行抓取器的下一个阶段。

**参数**

| 参数      | 类型     | 必填 | 描述           |
| ------- | ------ | -- | ------------ |
| `input` | object | 是  | 传递给下一阶段的输入对象 |

```js theme={null}
next_stage({url: 'https://example.com', page: 1});
```

#### `run_stage`，运行指定阶段

在新的浏览器会话中运行抓取器的某个命名阶段。

**参数**

| 参数      | 类型     | 必填 | 描述           |
| ------- | ------ | -- | ------------ |
| `stage` | number | 是  | 阶段索引（从 1 开始） |
| `input` | object | 是  | 传递给该阶段的输入对象  |

```js theme={null}
run_stage(2, {url: 'https://example.com', page: 1});
```

#### `rerun_stage`，用新输入重新运行当前阶段

使用新输入再次运行本阶段。用它来分散工作（例如，为分页中的每一页重新运行一次）。

```js theme={null}
rerun_stage({url: 'https://example.com/other-page'});
```

#### `load_sitemap`，从 XML 站点地图读取 URL

加载站点地图 XML 文件并返回 URL 列表。支持站点地图索引和 gzip 压缩的站点地图。

**参数**

| 参数            | 类型     | 必填 | 描述       |
| ------------- | ------ | -- | -------- |
| `options.url` | string | 是  | 站点地图 URL |

```js theme={null}
let {pages} = load_sitemap({url: 'https://example.com/sitemap.xml.gz'});
let {children} = load_sitemap({url: 'https://example.com/sitemap-index.xml'});
```

#### `resolve_url`，通过重定向追踪 URL

返回给定 URL 参数最终指向的 URL。

**参数**

| 参数    | 类型           | 必填 | 描述       |
| ----- | ------------ | -- | -------- |
| `url` | string 或 URL | 是  | 要解析的 URL |

```js theme={null}
let {href} = parse().anchor_elem_data;
collect({final_url: resolve_url(href)});
```

#### `redirect_history`，获取重定向链

返回自上次 `navigate()` 调用以来的 URL 重定向历史。

```js theme={null}
navigate('http://google.com');
let redirects = redirect_history();
// ['http://google.com', 'http://www.google.com', 'https://www.google.com/']
```

#### `response_headers`，读取最近一次响应的请求头

返回最近一次页面加载的响应头。

```js theme={null}
let headers = response_headers();
console.log('content-type', headers['content-type']);
```

#### `status_code`，读取最近一次响应的状态

返回最近一次页面加载的 HTTP 状态码。

```js theme={null}
collect({status_code: status_code()});
```

### 在页面上等待 ⭐

所有等待函数仅限 Browser worker。

#### ⭐ `wait`，等待元素出现

**参数**

| 参数            | 类型      | 必填 | 默认值     | 描述                   |
| ------------- | ------- | -- | ------- | -------------------- |
| `selector`    | string  | 是  | ,       | 要等待的 CSS 选择器         |
| `opt.timeout` | number  | 否  | `30000` | 超时（毫秒）               |
| `opt.hidden`  | boolean | 否  | `false` | 等待元素隐藏而非可见           |
| `opt.inside`  | string  | 否  | ,       | 要在其内部查找的 iframe 的选择器 |

```js theme={null}
wait('#welcome-splash');
wait('.search-results .product');
wait('[href^="/product"]');
wait('#welcome-splash', {timeout: 5000});
wait('#welcome-splash', {hidden: true});
wait('#welcome-splash', {inside: '#iframe_id'});
```

#### ⭐ `wait_any`，等待多个条件中的任意一个

等待任意一个匹配条件成功。当第一个选择器解析成功时返回。

```js theme={null}
wait_any(['#title', '#notfound']);
```

#### ⭐ `wait_visible`，等待元素可见

**参数**

| 参数            | 类型     | 必填 | 默认值     | 描述      |
| ------------- | ------ | -- | ------- | ------- |
| `selector`    | string | 是  | ,       | CSS 选择器 |
| `opt.timeout` | number | 否  | `30000` | 超时（毫秒）  |

```js theme={null}
wait_visible('#welcome-splash');
wait_visible('#welcome-splash', {timeout: 5000});
```

#### ⭐ `wait_hidden`，等待元素消失

**参数**

| 参数            | 类型     | 必填 | 默认值     | 描述      |
| ------------- | ------ | -- | ------- | ------- |
| `selector`    | string | 是  | ,       | CSS 选择器 |
| `opt.timeout` | number | 否  | `30000` | 超时（毫秒）  |

```js theme={null}
wait_hidden('#welcome-splash');
wait_hidden('#welcome-splash', {timeout: 5000});
```

#### ⭐ `wait_for_text`，等待文本内容

等待页面上的某个元素包含给定文本。

**参数**

| 参数         | 类型     | 必填 | 描述      |
| ---------- | ------ | -- | ------- |
| `selector` | string | 是  | CSS 选择器 |
| `text`     | string | 是  | 要等待的文本  |

```js theme={null}
wait_for_text('.location', 'New York');
```

#### `wait_for_parser_value`，等待解析器字段被填充

在 `tag_response()` 或 `tag_script()` 之后使用，以等待捕获的数据可用。

**参数**

| 参数            | 类型       | 必填 | 描述                  |
| ------------- | -------- | -- | ------------------- |
| `field`       | string   | 是  | 要等待的解析器字段路径         |
| `validate_fn` | function | 否  | 可选回调，当值有效时返回 `true` |
| `opt.timeout` | number   | 否  | 超时（毫秒）              |

```js theme={null}
wait_for_parser_value('profile');
wait_for_parser_value('listings.0.price', v => parseInt(v) > 0, {timeout: 5000});
```

#### ⭐ `wait_network_idle`，等待浏览器网络稳定

等待浏览器网络在给定时段内保持空闲。

**参数**

| 参数            | 类型     | 必填 | 默认值   | 描述                         |
| ------------- | ------ | -- | ----- | -------------------------- |
| `opt.timeout` | number | 否  | `500` | 所需的空闲毫秒数                   |
| `opt.ignore`  | array  | 否  | `[]`  | 用于排除请求的模式（string 或 RegExp） |

```js theme={null}
wait_network_idle();
wait_network_idle({
  timeout: 1e3,
  ignore: [/long_request/, 'https://example.com'],
});
```

#### ⭐ `wait_page_idle`，等待 DOM 变更停止

等待 DOM 树在给定时段内不发生任何变化。

**参数**

| 参数                 | 类型     | 必填 | 描述            |
| ------------------ | ------ | -- | ------------- |
| `opt.idle_timeout` | number | 否  | 所需的稳定毫秒数      |
| `opt.ignore`       | array  | 否  | 要从变更监控中排除的选择器 |

```js theme={null}
wait_page_idle();
wait_page_idle({
  ignore: ['.live-clock', '.carousel'],
  idle_timeout: 1000,
});
```

### 元素交互 ⭐

所有交互函数都需要 Browser worker。

#### ⭐ `click`，点击元素

点击元素，会先等待其出现。

**参数**

| 参数                | 类型             | 必填 | 描述                        |
| ----------------- | -------------- | -- | ------------------------- |
| `selector`        | string 或 array | 是  | CSS 选择器或 Shadow DOM 选择器路径 |
| `opt.coordinates` | `{x, y}`       | 否  | 点击距离给定页面坐标最近的匹配项          |

```js theme={null}
click('#show-more');
$('#show-more').click();

// Click the map pin closest to the center of a map
let box = bounding_box('#map');
let center = {x: (box.left + box.right) / 2, y: (box.top + box.bottom) / 2};
click('.map-pin', {coordinates: center});
```

#### ⭐ `right_click`，右键点击元素

与 `click` 相同，但使用鼠标右键。

```js theme={null}
right_click('#item');
```

#### ⭐ `hover`，悬停在元素上

将光标移动到元素上，会先等待其出现。

```js theme={null}
hover('#item');
```

#### ⭐ `mouse_to`，将光标移动到某个坐标

**参数**

| 参数  | 类型     | 必填 | 描述      |
| --- | ------ | -- | ------- |
| `x` | number | 是  | 目标 X 位置 |
| `y` | number | 是  | 目标 Y 位置 |

```js theme={null}
mouse_to(0, 0);
```

#### ⭐ `type`，向输入框输入文本

等待输入框出现，然后输入给定文本。

**参数**

| 参数            | 类型             | 必填 | 描述                    |
| ------------- | -------------- | -- | --------------------- |
| `selector`    | string         | 是  | CSS 选择器               |
| `text`        | string 或 array | 是  | 要输入的文本，或由字符串和特殊键组成的数组 |
| `opt.replace` | boolean        | 否  | 输入前清除现有文本             |

```js theme={null}
type('#location', 'New York');
type('#location', 'New York', {replace: true});
type('[id$=input-box]', 'search term');
type('#search', ['Some text', 'Enter']);
type('#search', ['Backspace']);
```

#### ⭐ `press_key`，按下特殊键

在当前聚焦的输入框中输入 Enter 或 Backspace 等特殊键。

```js theme={null}
press_key('Enter');
press_key('Backspace');
```

#### ⭐ `select`，从 select 元素中选取一个值

**参数**

| 参数         | 类型     | 必填 | 描述                     |
| ---------- | ------ | -- | ---------------------- |
| `selector` | string | 是  | `<select>` 元素的 CSS 选择器 |
| `value`    | string | 是  | 选项值或可见文本               |

```js theme={null}
select('#country', 'Canada');
```

#### ⭐ `scroll_to`，将元素滚动到视图中

滚动页面，使目标元素可见。默认使用自然滚动；传入 `immediate: true` 可直接跳转。

```js theme={null}
scroll_to('.author-profile');
scroll_to('top');
scroll_to('bottom');
scroll_to('top', {immediate: true});
```

#### ⭐ `scroll_to_all`，滚动经过每个匹配元素

```js theme={null}
scroll_to_all('.author-profiles');
```

#### ⭐ `load_more`，触发懒加载内容

滚动到列表底部以触发无限滚动加载。

**参数**

| 参数                     | 类型     | 必填 | 描述             |
| ---------------------- | ------ | -- | -------------- |
| `selector`             | string | 是  | 容纳懒加载项的容器元素    |
| `opt.children`         | string | 否  | 单个项目的选择器       |
| `opt.trigger_selector` | string | 否  | 显式"加载更多"按钮的选择器 |
| `opt.timeout`          | number | 否  | 超时（毫秒）         |

```js theme={null}
load_more('.search-results');
load_more('.search-results', {
  children: '.result-item',
  trigger_selector: '.btn-load-more',
  timeout: 10000,
});
```

#### ⭐ `close_popup`，在后台自动关闭弹窗

注册一个后台监视器，每当弹窗出现时将其关闭。推荐的模式见 [最佳实践](/cn/datasets/scraper-studio/best-practices)。

**参数**

| 参数                 | 类型     | 必填 | 描述                             |
| ------------------ | ------ | -- | ------------------------------ |
| `popup_selector`   | string | 是  | 弹窗容器的选择器                       |
| `close_selector`   | string | 是  | 关闭它的元素的选择器                     |
| `opt.click_inside` | string | 否  | 父 iframe 选择器，如果关闭按钮位于 iframe 内 |

```js theme={null}
close_popup('.popup', '.popup_close');
close_popup('iframe.with-popup', '.popup_close', {click_inside: 'iframe.with-popup'});
```

#### ⭐ `solve_captcha`，解决页面上的验证码

```js theme={null}
solve_captcha();
solve_captcha({type: 'simple', selector: '#image', input: '#input'});
```

#### ⭐ `bounding_box`，获取元素的页面坐标

返回第一个匹配元素相对于页面的边界框。

**参数**

| 参数         | 类型     | 必填 | 描述      |
| ---------- | ------ | -- | ------- |
| `selector` | string | 是  | CSS 选择器 |

```js theme={null}
let box = bounding_box('.product-list');
// box == {top, right, bottom, left, x, y, width, height}
```

#### `el_exists`，检查元素是否在页面上

**参数**

| 参数         | 类型     | 必填 | 默认值 | 描述              |
| ---------- | ------ | -- | --- | --------------- |
| `selector` | string | 是  | ,   | CSS 选择器         |
| `timeout`  | number | 否  | `0` | 最多等待 N 毫秒以等元素出现 |

```js theme={null}
el_exists('#example');            // true
el_exists('.does_not_exist');     // false
el_exists('.does_not_exist', 5e3); // false after 5 seconds
```

#### `el_is_visible`，检查元素是否可见

**参数**

| 参数         | 类型     | 必填 | 默认值 | 描述              |
| ---------- | ------ | -- | --- | --------------- |
| `selector` | string | 是  | ,   | CSS 选择器         |
| `timeout`  | number | 否  | `0` | 最多等待 N 毫秒以等元素可见 |

```js theme={null}
el_is_visible('#example');
el_is_visible('.is_not_visible', 5e3);
```

#### ⭐ `track_event_listeners`，开始跟踪浏览器事件监听器

必须在 `disable_event_listeners()` 之前调用。

```js theme={null}
track_event_listeners();
```

#### ⭐ `disable_event_listeners`，禁用事件监听器

阻止页面上所有事件监听器运行。

**参数**

| 参数            | 类型        | 必填 | 描述         |
| ------------- | --------- | -- | ---------- |
| `event_types` | string\[] | 否  | 要禁用的特定事件类型 |

```js theme={null}
disable_event_listeners();
disable_event_listeners(['hover', 'click']);
```

#### ⭐ `freeze_page`，停止后续的页面变更

强制页面停止变化，使 HTML 快照准确反映抓取器所看到的内容。实验性功能。

```js theme={null}
freeze_page();
```

### 网络与响应标记 ⭐

标记会捕获后台网络流量并将其暴露给解析器。所有 `tag_*` 函数仅限 Browser worker。

#### ⭐ `tag_response`，保存一个匹配的响应

保存来自某个匹配浏览器请求的响应数据。

**参数**

| 参数                | 类型                | 必填 | 描述                    |
| ----------------- | ----------------- | -- | --------------------- |
| `field`           | string            | 是  | 要填充的解析器字段名称           |
| `pattern`         | RegExp 或 function | 是  | URL 模式或匹配函数           |
| `opt.jsonp`       | boolean           | 否  | 解析 JSONP 响应体（尽可能自动检测） |
| `opt.allow_error` | boolean           | 否  | 捕获非 2xx 状态码的响应        |

```js theme={null}
tag_response('resp', /url/, {jsonp: true});
tag_response('resp', /url/, {allow_error: true});

tag_response('resp', (req, res) => {
  if (req.url.includes('/api/')) {
    return {
      request_body: req.body,
      request_headers: req.headers,
      response_body: res.body,
      response_headers: res.headers,
    };
  }
});

tag_response('teams', /\/api\/teams/);
navigate('https://example.com/sports');
let teams = parse().teams;
for (let team of teams)
  collect(team);
```

#### ⭐ `tag_all_responses`，保存每个匹配的响应

将每个匹配请求的响应数据保存为一个数组。

```js theme={null}
tag_all_responses('profiles', /\/api\/profile/);
navigate('https://example.com/sports');
let profiles = parse().profiles;
for (let profile of profiles)
  collect(profile);
```

#### ⭐ `tag_script`，提取嵌入在 `<script>` 标签中的 JSON

**参数**

| 参数         | 类型     | 必填 | 描述           |
| ---------- | ------ | -- | ------------ |
| `field`    | string | 是  | 解析器字段名称      |
| `selector` | string | 是  | script 标签选择器 |

```js theme={null}
tag_script('ssr_state', '#__SSR_DATA__');
navigate('https://example.com/');
collect(parse().ssr_state);
```

#### ⭐ `tag_window_field`，标记浏览器 `window` 上的一个值

**参数**

| 参数      | 类型     | 必填 | 描述               |
| ------- | ------ | -- | ---------------- |
| `field` | string | 是  | 解析器字段名称          |
| `key`   | string | 是  | 要读取的 `window` 属性 |

```js theme={null}
tag_window_field('initData', '__INIT_DATA__');
```

#### ⭐ `tag_image`，从 DOM 元素捕获图片 URL

```js theme={null}
tag_image('image', '#product-image');
```

#### ⭐ `tag_video`，从 DOM 元素捕获视频 URL

**参数**

| 参数             | 类型      | 必填 | 描述      |
| -------------- | ------- | -- | ------- |
| `field`        | string  | 是  | 解析器字段名称 |
| `selector`     | string  | 是  | 元素选择器   |
| `opt.download` | boolean | 否  | 下载视频文件  |

```js theme={null}
tag_video('video', '#product-video', {download: true});
```

#### ⭐ `tag_screenshot`，保存页面截图

**参数**

| 参数              | 类型      | 必填 | 描述         |
| --------------- | ------- | -- | ---------- |
| `field`         | string  | 是  | 解析器字段名称    |
| `opt.filename`  | string  | 否  | 输出文件名      |
| `opt.full_page` | boolean | 否  | 默认为 `true` |

```js theme={null}
tag_screenshot('html_screenshot', {filename: 'screen'});
tag_screenshot('view', {full_page: false});
```

#### ⭐ `tag_download`，捕获浏览器下载的文件

**参数**

| 参数    | 类型              | 必填 | 描述        |
| ----- | --------------- | -- | --------- |
| `url` | string 或 RegExp | 是  | 匹配下载请求的模式 |

```js theme={null}
let SEC = 1000;
let download = tag_download(/example.com\/foo\/bar/);
click('button#download');
let file1 = download.next_file({timeout: 10 * SEC});
let file2 = download.next_file({timeout: 20 * SEC});
collect({file1, file2});
```

#### ⭐ `tag_serp`，将页面解析为搜索引擎结果页

**参数**

| 参数      | 类型     | 必填 | 描述                      |
| ------- | ------ | -- | ----------------------- |
| `field` | string | 是  | 解析器字段名称                 |
| `type`  | string | 是  | 解析器类型：`google`、`bing` 等 |

```js theme={null}
tag_serp('serp_bing_results', 'bing');
tag_serp('serp_google_results', 'google');
```

#### ⭐ `capture_graphql`，捕获并重放 GraphQL 查询

捕获一个 GraphQL 请求，以便你可以用不同的变量重放它。

**参数**

| 参数                | 类型     | 必填 | 描述                                  |
| ----------------- | ------ | -- | ----------------------------------- |
| `options.payload` | object | 是  | 与目标请求负载匹配的键值对                       |
| `options.url`     | RegExp | 否  | GraphQL 端点的 URL 模式（默认为 `/graphql/`） |

```js theme={null}
let q = capture_graphql({
  payload: {id: 'ProfileQuery'},
});
navigate('https://example.com');

let [first_query, first_response] = q.wait_captured();
collect(first_response.data.profile);

let second = q.replay({
  variables: {other_id: 2},
});
collect(second.data.profile);
```

### 数据采集

#### `parse`，运行解析器代码

运行解析器代码并返回结构化结果。

```js theme={null}
let page_data = parse();
collect({
  title: page_data.title,
  price: page_data.price,
});
```

#### `collect`，向数据集追加一条记录

向抓取器的输出添加一条记录。

**参数**

| 参数            | 类型       | 必填 | 描述             |
| ------------- | -------- | -- | -------------- |
| `data_line`   | object   | 是  | 要采集的字段         |
| `validate_fn` | function | 否  | 遇到无效数据时抛出错误的回调 |

```js theme={null}
collect({price: data.price});
collect(product, p => {
  if (!p.title)
    throw new Error('Product is missing a title');
});
```

#### `set_lines`，设置输出行，覆盖先前的调用

每次调用 `set_lines()` 都会覆盖前一次调用。当抓取器采集部分数据，并且你希望在后续步骤抛出错误时交付最后已知状态时，此函数很有用。

**参数**

| 参数            | 类型        | 必填 | 描述          |
| ------------- | --------- | -- | ----------- |
| `lines`       | object\[] | 是  | 记录数组        |
| `validate_fn` | function  | 否  | 验证回调，每行运行一次 |

```js theme={null}
set_lines(products_so_far);
set_lines(products_so_far, p => {
  if (!p.price)
    throw new Error('Missing price');
});
```

#### `load_html`，将 HTML 字符串加载到 Cheerio

**参数**

| 参数     | 类型     | 必填 | 描述        |
| ------ | ------ | -- | --------- |
| `html` | string | 是  | 要解析的 HTML |

```js theme={null}
let $$ = load_html('<p id="p1">p1</p><p id="p2">p2</p>');
collect({data: $$('#p2').text()});
```

### 将一次抓取标记为失败

#### `bad_input`，将输入标记为无效

阻止任何重试并报告 `error_code=bad_input`。

```js theme={null}
bad_input();
bad_input('Missing search term');
```

#### `blocked`，将页面标记为已被阻止

报告站点拒绝访问。`error_code=blocked`。

```js theme={null}
blocked();
blocked('Login page was shown');
```

#### `dead_page`，将 URL 标记为失效链接

标记页面，以便在未来的采集中将其过滤掉。`error_code=dead_page`。

```js theme={null}
dead_page();
dead_page('Product was removed');
```

#### ⭐ `detect_block`，检测页面上的阻止情况

**参数**

| 参数                   | 类型              | 必填 | 描述            |
| -------------------- | --------------- | -- | ------------- |
| `resource.selector`  | string          | 是  | 要检查的元素        |
| `condition.exists`   | boolean         | 否  | 如果元素存在则失败     |
| `condition.has_text` | string 或 RegExp | 否  | 如果元素包含匹配文本则失败 |

```js theme={null}
detect_block({selector: '.foo'}, {exists: true});
detect_block({selector: '.bar'}, {has_text: 'text'});
detect_block({selector: '.baz'}, {has_text: /regex_pattern/});
```

### 会话与路由

#### `country`，通过特定国家/地区路由

**参数**

| 参数     | 类型     | 必填 | 描述              |
| ------ | ------ | -- | --------------- |
| `code` | string | 是  | 两字符 ISO 国家/地区代码 |

```js theme={null}
country('us');
```

#### ⭐ `proxy_location`，细粒度代理位置

除非你需要精确的地理控制，否则优先使用 `country()`。

**参数**

| 参数                      | 类型     | 必填 | 描述                  |
| ----------------------- | ------ | -- | ------------------- |
| `configuration.country` | string | 否  | 两字符 ISO 国家/地区代码     |
| `configuration.lat`     | number | 否  | 纬度，范围 `[-85, 85]`   |
| `configuration.long`    | number | 否  | 经度，范围 `[-180, 180]` |
| `configuration.radius`  | number | 否  | 半径（千米）              |

```js theme={null}
proxy_location({country: 'us'});
proxy_location({lat: 37.7749, long: 122.4194});
proxy_location({lat: 37.7749, long: 122.4194, country: 'US', radius: 100});
```

#### `preserve_proxy_session`，在子阶段之间复用代理会话

```js theme={null}
preserve_proxy_session();
```

#### `set_session_cookie`，为当前会话设置 cookie

**参数**

| 参数       | 类型     | 必填 | 描述        |
| -------- | ------ | -- | --------- |
| `domain` | string | 是  | Cookie 域  |
| `name`   | string | 是  | Cookie 名称 |
| `value`  | string | 是  | Cookie 值  |

```js theme={null}
set_session_cookie('example.com', 'session_id', 'abc123');
```

#### `set_session_headers`，设置额外的 HTTP 请求头

**参数**

| 参数        | 类型     | 必填 | 描述     |
| --------- | ------ | -- | ------ |
| `headers` | object | 是  | 请求头键值对 |

```js theme={null}
set_session_headers({'X-Custom-Header': 'value'});
```

### 浏览器配置 ⭐

仅限 Browser worker。

#### ⭐ `browser_size`，获取当前浏览器窗口大小

以像素返回 `{width, height}`。

```js theme={null}
let size = browser_size();
console.log(size.width, size.height);
```

#### ⭐ `emulate_device`，模拟移动设备

切换用户代理、屏幕分辨率和设备像素比，以匹配某个命名设备。

**参数**

| 参数       | 类型     | 必填 | 描述                           |
| -------- | ------ | -- | ---------------------------- |
| `device` | string | 是  | 设备名称，例如 `iPhone X`、`Pixel 2` |

```js theme={null}
emulate_device('iPhone X');
emulate_device('Pixel 2');
```

<Accordion title="支持的设备名称完整列表">
  * Blackberry PlayBook / landscape
  * BlackBerry Z30 / landscape
  * Galaxy Note 3 / landscape
  * Galaxy Note II / landscape
  * Galaxy S III / S5 / S8 / S9+（各含 landscape）
  * Galaxy Tab S4 / landscape
  * iPad / iPad Mini / iPad Pro / iPad Pro 11 / iPad (gen 6) / iPad (gen 7)（各含 landscape）
  * iPhone 4, 5, 6, 6 Plus, 7, 7 Plus, 8, 8 Plus, SE, X, XR, 11, 11 Pro, 11 Pro Max, 12 / 12 Mini / 12 Pro / 12 Pro Max, 13 / 13 Mini / 13 Pro / 13 Pro Max（各含 landscape）
  * JioPhone 2 / landscape
  * Kindle Fire HDX / landscape
  * LG Optimus L70 / landscape
  * Microsoft Lumia 550, 950（950 含 landscape）
  * Nexus 4, 5, 5X, 6, 6P, 7, 10（各含 landscape）
  * Nokia Lumia 520 / landscape，Nokia N9 / landscape
  * Pixel 2, 2 XL, 3, 4, 4a (5G), 5（各含 landscape）
  * Moto G4 / landscape
</Accordion>

#### ⭐ `font_exists`，检查浏览器字体支持

断言浏览器可以渲染给定的字体系列。

```js theme={null}
font_exists('Liberation Mono');
```

#### ⭐ `html_capture_options`，配置 HTML 捕获

控制 HTML 快照的捕获方式。

**参数**

| 参数                              | 类型      | 必填 | 描述          |
| ------------------------------- | ------- | -- | ----------- |
| `options.coordinate_attributes` | boolean | 否  | 将元素坐标作为属性嵌入 |

```js theme={null}
html_capture_options({
  coordinate_attributes: true,
});
```

#### `embed_html_comment`，向页面 HTML 注入注释

在 HTML 快照中嵌入元数据。

```js theme={null}
embed_html_comment('trace-id: asdf123');
```

### 调试与可观测性

#### `console`，从交互代码记录日志

```js theme={null}
console.log(1, 'brightdata', [1, 2], {key: 'value'});
console.error('something went wrong');
```

#### ⭐ `verify_requests`，监控失败的浏览器请求

在每个失败的浏览器请求上触发回调。

**参数**

| 参数         | 类型       | 必填 | 描述                                          |
| ---------- | -------- | -- | ------------------------------------------- |
| `callback` | function | 是  | 对每个失败的请求以 `{url, error, type, response}` 调用 |

```js theme={null}
verify_requests(({url, error, type, response}) => {
  if (response.status != 404 && type == 'Font')
    throw new Error('Font failed to load');
});
```

### 值构造函数

Bright Data Scraper Studio 为结构化输出字段提供了带类型的构造函数。

#### `Image`、`Video`、`Pdf`、`Doc`、`Money`

| 构造函数                     | 参数                           | 用途        |
| ------------------------ | ---------------------------- | --------- |
| `Image(src)`             | `src`：图片 URL 或 data URI      | 采集图片数据    |
| `Video(src)`             | `src`：视频 URL                 | 采集视频数据    |
| `Pdf(src)`               | `src`：PDF URL                | 采集 PDF 文件 |
| `Doc(src)`               | `src`：文档文件 URL               | 采集文档文件    |
| `Money(value, currency)` | `value`：数字，`currency`：ISO 代码 | 采集货币值     |

## **支持下载的文件类型**

Scraper Studio 支持通过媒体和文档字段构造函数下载文件。

使用方式：

* `new Image()` 用于图片文件
* `new Video()` 用于视频文件
* `new Pdf()` 用于 PDF 文件
* `new Doc()` 用于受支持的文档、文本、音频、视频和结构化文件类型

### `new Doc() ` **支持的内容类型**

`new Doc()` 支持以下内容类型：

```text theme={null}
application/json
application/pdf
application/rtf
application/vnd.openxmlformats-officedocument.wordprocessingml.document
application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
application/vnd.ms-excel
application/xml
application/vnd.oasis.opendocument.spreadsheet
audio/mp3
audio/mp4
audio/webm
text/csv
text/html
text/plain
text/vtt
text/xml
video/iso.segment
video/MP2T
video/mp2t
video/mp4
video/webm
```

示例：

```js theme={null}
let img = new Image('https://example.com/image.png');
let vid = new Video('https://example.com/video.mp4');
let pdf = new Pdf('https://example.com/document.pdf');
let doc = new Doc('https://example.com/file.csv');
let price = new Money(10, 'USD');

collect({
image: img, 
video: vid, 
pdf, 
document: doc, 
product_price: price
});
```

#### `URL`

标准 Node.js `URL` 类。

```js theme={null}
let u = new URL('https://example.com');
```

## 解析函数

解析代码在交互代码调用 `parse()` 之后运行。它接收捕获的 HTML 和任何已标记的数据，并向交互代码返回单条记录（或记录数组）。解析代码使用 Cheerio，一个与 jQuery 兼容的 HTML 解析器。

### 解析代码中可用的全局对象

| 名称         | 类型         | 描述                                              |
| ---------- | ---------- | ----------------------------------------------- |
| `$`        | Cheerio 实例 | 已加载页面 HTML                                      |
| `input`    | object     | 当前阶段输入                                          |
| `location` | object     | 当前浏览器位置；字段：`href`                               |
| `parser`   | object     | 在交互期间标记的值（来自 `tag_response`、`tag_script` 及相关函数） |

```js theme={null}
let url = input.url;
let current_url = location.href;
$('#example').text();
```

### Cheerio 辅助函数

Bright Data Scraper Studio 在标准 API 之上添加了自定义 Cheerio 方法。

#### `$(selector).text_sane()`，规范化空白字符

返回 `text()`，其中所有连续的空白字符被折叠为单个空格并去除首尾空白。

```js theme={null}
let name = $('a').text_sane();                   // "foo bar baz"
let raw  = $('a').text();                        // "foo   bar\n\n\t baz"
```

#### `$(selector).filter_includes(text)`，按文本内容筛选元素

将选择集筛选为文本包含给定子串的元素。可与 Cheerio API 的其余部分链式调用。

```js theme={null}
$('.selector').filter_includes('text').click();
```

### 解析器值构造函数

`Image`、`Video`、`PDF` 和 `Money` 在解析代码中同样可用，且工作方式相同。

```js theme={null}
let img = new Image('https://example.com/image.png');
let price = new Money(10, 'USD');
let p = new Pdf('https://example.com/document.pdf')
collect({image: img, product_price: price});
```

## **验证已下载媒体的类型**

使用 `validate_type` 检查已下载文件的内容是否与预期的媒体类型匹配。此选项由 `new Pdf()`、`new Image()` 和 `new Video()` 支持。

启用 `validate_type` 后，Scraper Studio 会在获取文件后对其进行验证。如果文件内容与预期类型不匹配，该字段将返回错误，而不是有效的已下载文件。

示例：

```javascript theme={null}
return {
  pdf: new Pdf('https://example.com/pdf', { validate_type: true }),
  image: new Image('https://example.com/image', { validate_type: true }),
  video: new Video('https://example.com/video', { validate_type: true }),
};
```

验证失败示例：

```json theme={null}
{
  "pdf": {
    "remote_url": "https://example.com/pdf",
    "error": "downloaded file type \"image\" does not match the expected \"pdf\" type",
    "validated_type": "image",
    "error_code": "wrong_file_type"
  }
}
```

<Tip>
  有关完整的 Cheerio API 文档，请参阅 [Cheerio 网站](https://cheerio.js.org/)。
</Tip>

## Shadow DOM 支持

接受选择器的交互命令也接受选择器**数组**，让你能够深入 Shadow DOM 树。可将其与 `click`、`wait`、`type` 及其他交互函数一起使用。

当你传入数组时：

* 其中一个选择器必须指向 shadow host 元素
* 它之后的每个选择器都在该 shadow root 内解析

```js theme={null}
click(['body', 'my-shadow-host', 'button.submit']);
```

在该示例中，`my-shadow-host` 是附加了 shadow root 的元素，而 `button.submit` 在该 shadow root 内解析。

## 仅限浏览器的函数

以下函数需要 Browser worker，从 Code worker 调用时会抛出 `not_supported_in_code_worker`。使用此列表来决定你的抓取器需要哪种 worker。

| 类别    | 函数                                                                                                                                                      |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 等待    | `wait`、`wait_any`、`wait_for_text`、`wait_visible`、`wait_hidden`、`wait_network_idle`、`wait_page_idle`                                                     |
| 交互    | `click`、`right_click`、`hover`、`mouse_to`、`type`、`press_key`、`select`、`scroll_to`、`scroll_to_all`、`load_more`、`close_popup`、`solve_captcha`              |
| 标记    | `tag_response`、`tag_all_responses`、`tag_script`、`tag_window_field`、`tag_image`、`tag_video`、`tag_screenshot`、`tag_download`、`tag_serp`、`capture_graphql` |
| 浏览器配置 | `browser_size`、`emulate_device`、`font_exists`、`html_capture_options`、`freeze_page`、`track_event_listeners`、`disable_event_listeners`                    |

请参阅 [Worker 类型](/cn/datasets/scraper-studio/worker-types) 以在 Browser worker 和 Code worker 之间做出选择。

## 相关内容

<CardGroup cols={2}>
  <Card title="最佳实践" icon="list-check" href="/cn/datasets/scraper-studio/best-practices">
    编写快速、可靠抓取器的推荐模式
  </Card>

  <Card title="Worker 类型" icon="server" href="/cn/datasets/scraper-studio/worker-types">
    何时使用 Browser worker 与 Code worker
  </Card>

  <Card title="网页抓取基础" icon="graduation-cap" href="/cn/datasets/scraper-studio/basics-of-web-scraping">
    核心概念：交互、解析、阶段和规模
  </Card>

  <Card title="开发抓取器" icon="wrench" href="/cn/datasets/scraper-studio/develop-a-scraper">
    在 IDE 中构建抓取器的逐步演示
  </Card>
</CardGroup>
