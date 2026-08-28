> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SERP API DuckDuckGo 查询参数

> Configure DuckDuckGo search queries with Bright Data's SERP API, including parameters for localization, safe search, time range, and device targeting, tailored to meet your data extraction needs.

## 搜索

<AccordionGroup>
  <Accordion title="本地化" icon="flag">
    ### `kl`

    用于定义搜索国家/地区和语言的国家/地区和语言代码。 点击此处查看完整列表:\
    [https://api.brightdata.com/serp/duckduckgo/kl\_values](https://api.brightdata.com/serp/duckduckgo/kl_values)

    ```sh theme={null}
    curl --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer-id>-zone-<zone-name>:<zone-password> "https://duckduckgo.com/?q=pizza&kl=us-en"
    ```

    ### `kad`

    搜索页面界面语言：按钮、菜单。 点击此处查看完整列表:\
    [https://api.brightdata.com/serp/duckduckgo/kad\_values](https://api.brightdata.com/serp/duckduckgo/kad_values)

    ```sh theme={null}
    curl --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer-id>-zone-<zone-name>:<zone-password> "https://duckduckgo.com/?q=pizza"
    ```
  </Accordion>

  <Accordion title="安全搜索" icon="shield">
    ### `kp`

    移除搜索结果中的成人内容。

    > **可用值如下：** \
    > ` 1` - 打开安全搜索 \
    > `-1` - 适度搜索内容 \
    > `-2` - 关闭安全搜索

    ```sh theme={null}
    curl --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer-id>-zone-<zone-name>:<zone-password> "https://duckduckgo.com/?q=pizza&kp=1"
    ```
  </Accordion>

  <Accordion title="时间范围" icon="calendar">
    ### `df`

    搜索时间范围。

    > **可用值如下：** \
    > `d` - 过去 2 周 \
    > `w` - 上个月 \
    > `m` - 过去 3 个月 \
    > `w` - 过去 6 个月

    ```sh theme={null}
    curl --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer-id>-zone-<zone-name>:<zone-password> "https://duckduckgo.com/?q=pizza&df=d"
    ```
  </Accordion>

  <Accordion title="设备" icon="mobile-screen-button">
    ### `brd_mobile`

    定义要在用户代理中表示的设备类型

    默认或 `brd_mobile=0` 时将提供随机桌面用户代理，而 `brd_mobile=1` 时将提供随机移动用户代理。

    > **对于特定的移动平台，提供以下值之一：**  \
    > `brd_mobile=ios` - iPhone 用户代理（别名 `brd_mobile=iphone`） \
    > `brd_mobile=ipad` - iPad 用户代理（别名 `brd_mobile=ios_tablet`） \
    > `brd_mobile=android` - 安卓手机 \
    > `brd_mobile=android_tablet` - 安卓平板

    ```sh theme={null}
    curl --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer-id>-zone-<zone-name>:<zone-password> "https://duckduckgo.com/?q=pizza&brd_mobile=1"
    ```
  </Accordion>

  <Accordion title="浏览器" icon="table-columns">
    ### `brd_browser`

    定义 user-agent 中表示的浏览器类型。\
    可与 `brd_mobile` 一起使用以获取对应的移动浏览器。\
    默认会生成随机浏览器。

    > **指定浏览器可使用以下值：** \
    > `brd_browser=chrome` - Google Chrome \
    > `brd_browser=safari` - Safari \
    > `brd_browser=firefox` - Mozilla Firefox（与 `brd_mobile=1` 不兼容）

    ```sh theme={null}
    curl --proxy brd.superproxy.io:44445 --proxy-user brd-customer-<customer-id>-zone-<zone-name>:<zone-password> "https://www.yandex.com/search/?text=pizza&brd_browser=chrome"
    ```
  </Accordion>
</AccordionGroup>
