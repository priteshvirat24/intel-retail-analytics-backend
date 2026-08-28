> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SERP API Bing 查询参数

> 使用 Bright Data 的 SERP API 配置 Bing 搜索查询，包括本地化、地理位置、分页、设备定向和自定义数据输出选项的参数。

<Warning>
  [Microsoft Bing Search APIs 将于 2025 年 8 月 11 日退役](https://learn.microsoft.com/en-us/lifecycle/announcements/bing-search-api-retirement)。Bright Data SERP API 对于 Bing 域名仍将继续支持。
  [Bing API 到 Bright Data SERP API 迁移指南](/cn/scraping-automation/serp-api/parsed-json-results/bing-to-bright-data-serp-migration-guide)。
</Warning>

## Search

<AccordionGroup>
  <Accordion title="Localization" icon="flag">
    ### `setLang`

    用于用户界面字符串的语言。您可以使用 2 字母或 4 字母语言代码，推荐使用 4 字母代码。

    ```sh theme={null}
    curl --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer-id>-zone-<zone-name>:<zone-password> "https://www.bing.com/search?q=pizza&setLang=en-US"
    ```
  </Accordion>

  <Accordion title="Geo-Location" icon="location-dot">
    ### `location`

    搜索来源的位置。应与 `lat`（纬度）和 `lon`（经度）参数一起使用。

    ```sh theme={null}
    curl --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer-id>-zone-<zone-name>:<zone-password> "https://www.bing.com/search?q=pizza&location=New+York%2C+New+York%2C+United+States&lat=40.7001958&lon=-74.1087142"
    ```

    ### `cc`

    返回结果所在国家/地区的 2 字母国家代码。

    ```sh theme={null}
    curl --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer-id>-zone-<zone-name>:<zone-password> "https://www.bing.com/search?q=pizza&cc=us"
    ```

    ### `mkt`

    返回搜索结果的市场。

    ```sh theme={null}
    curl --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer-id>-zone-<zone-name>:<zone-password> "https://www.bing.com/search?q=pizza&mkt=en-US"
    ```
  </Accordion>

  <Accordion title="Pagination" icon="file">
    ### `count`

    此属性已被 Bing 弃用，不再支持。

    ### `first`

    用于指示在返回结果前跳过多少条搜索结果的偏移量。默认值为 1。

    将此参数与 `count` 参数一起使用以分页。例如，将 `count` 设置为 10、`first` 设置为 1 可获取第一页结果。
    每一页递增 10，例如 1、11、21。
    多个页面之间可能存在重叠结果。

    > #### 示例：
    >
    > `first=1`（默认）— 第一页结果\
    > `first=11` — 第二页结果\
    > `first=21` — 第三页结果，依此类推。

    ```sh theme={null}
    curl --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer-id>-zone-<zone-name>:<zone-password> "https://www.bing.com/search?q=pizza&first=11"
    ```
  </Accordion>

  <Accordion title="Filters" icon="filter">
    ### `safesearch`

    用于过滤网页、图片和视频中的成人内容。

    > **可能的过滤值如下：**\
    > `safesearch=off` — 返回包含成人文本和图片，但不包含成人视频的内容\
    > `safesearch=moderate` — 返回包含成人文本，但不包含成人图片或视频的网页\
    > `safesearch=strict` — 不返回成人文本、图片或视频

    默认值为 Moderate。

    注意：如果请求来自 Bing 的成人政策要求必须设置为 Strict 的市场，则 Bing 会忽略 safesearch 的值并强制使用 Strict。

    ```sh theme={null}
    curl --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer-id>-zone-<zone-name>:<zone-password> "https://www.bing.com/search?q=pizza&safesearch=off"
    ```
  </Accordion>

  <Accordion title="Device" icon="mobile-screen-button">
    ### `brd_mobile`

    定义在 user-agent 中代表的设备类型。

    默认或 `brd_mobile=0` 会生成随机桌面 user-agent，而 `brd_mobile=1` 会生成随机移动设备 user-agent。

    > **指定移动平台可使用以下值：**\
    > `brd_mobile=ios` - iPhone user-agent（别名 `brd_mobile=iphone`）\
    > `brd_mobile=ipad` - iPad user-agent（别名 `brd_mobile=ios_tablet`）\
    > `brd_mobile=android` - Android 手机\
    > `brd_mobile=android_tablet` - Android 平板

    ```sh theme={null}
    curl --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer-id>-zone-<zone-name>:<zone-password> "https://www.bing.com/search?q=pizza&brd_mobile=1"
    ```
  </Accordion>

  <Accordion title="Browser" icon="table-columns">
    ### `brd_browser`

    定义在 user-agent 中表示的浏览器类型。\
    可与 `brd_mobile` 一起使用以获取对应的移动浏览器。\
    默认会提供随机浏览器。

    > **指定浏览器可使用以下值：**\
    > `brd_browser=chrome` - Google Chrome\
    > `brd_browser=safari` - Safari\
    > `brd_browser=firefox` - Mozilla Firefox（与 `brd_mobile=1` 不兼容）

    ```sh theme={null}
    curl --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer-id>-zone-<zone-name>:<zone-password> "https://www.bing.com/search?q=pizza&brd_browser=chrome"
    ```
  </Accordion>
</AccordionGroup>
