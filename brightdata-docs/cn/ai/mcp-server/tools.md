> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 工具

> 可用于网页抓取和数据提取的工具概览。

<Note>
  ### 模式：Rapid（免费）与 Pro

  Bright Data 的 MCP 服务器提供两种模式，以满足不同需求：

  * <Icon icon="gift" iconType="duotone" size={20} />   **Rapid（免费）** — 快速抓取搜索结果，并将任意公开网页解锁为干净的 Markdown。

  * <Icon icon="gem" iconType="duotone" size={20} />   **Pro** — 访问高级抓取功能、从顶级平台（Amazon、LinkedIn、X、Instagram 等）获取结构化数据，并支持完整的浏览器自动化。适用于动态和大规模使用场景。

  ***

  要使用 **Pro 模式**：

  * 在 Remote MCP 中，通过设置 `&pro=1` 请求 Pro 功能。
  * 在 Local MCP 中，通过设置 `PRO_MODE=true` 启用 Pro 功能。
</Note>

<Tip>
  **Rapid（免费）** 模式默认启用，并 **推荐** 用于日常浏览和数据需求。
</Tip>

|                         模式                        | 功能                                       | 描述                                                                                     |
| :-----------------------------------------------: | :--------------------------------------- | :------------------------------------------------------------------------------------- |
| <Icon icon="gift" iconType="duotone" size={20} /> | `search_engine`                          | 从 Google、Bing 或 Yandex 抓取搜索结果。Google 返回 JSON，Bing/Yandex 返回 Markdown；支持使用 cursor 参数分页。 |
| <Icon icon="gift" iconType="duotone" size={20} /> | `scrape_as_markdown`                     | 抓取单个网页并进行高级提取，以 Markdown 返回。使用 Bright Data 的 unlocker 处理机器人防护和 CAPTCHA。                |
| <Icon icon="gift" iconType="duotone" size={20} /> | `search_engine_batch`                    | 并行运行最多 10 个搜索查询。Google 返回 JSON，Bing/Yandex 返回 Markdown。                                |
| <Icon icon="gift" iconType="duotone" size={20} /> | `scrape_batch`                           | 在一次请求中抓取最多 10 个网页，并以 Markdown 格式返回 URL/内容对数组。                                          |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `scrape_as_html`                         | 抓取单个网页并返回 HTML 响应正文。可处理受机器人检测或 CAPTCHA 保护的网站。                                          |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `extract`                                | 将网页抓取为 Markdown 并使用 AI 采样转换为结构化 JSON，可选支持自定义提取提示词。                                     |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `session_stats`                          | 报告当前 MCP 会话中每个工具的调用次数。                                                                 |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_amazon_product`                | 快速读取 Amazon 商品的结构化数据。需要包含 /dp/ 的有效商品 URL。通常比抓取更快更可靠。                                   |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_amazon_product_reviews`        | 快速读取 Amazon 商品评论的结构化数据。需要包含 /dp/ 的有效商品 URL。通常比抓取更快更可靠。                                 |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_amazon_product_search`         | 获取 Amazon 搜索的结构化结果。需要搜索关键词和 Amazon 域名 URL；仅限第一页结果。                                     |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_walmart_product`               | 快速读取 Walmart 商品的结构化数据。需要包含 /ip/ 的有效商品 URL。通常比抓取更快更可靠。                                  |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_walmart_seller`                | 快速读取 Walmart 卖家的结构化数据。需要有效的 Walmart 卖家 URL。通常更快更可靠。                                    |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_ebay_product`                  | 快速读取 eBay 商品的结构化数据。需要有效的 eBay 商品 URL。通常更快更可靠。                                          |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_homedepot_products`            | 快速读取 Home Depot 商品数据。需要有效的 homedepot.com 商品 URL。通常更快更可靠。                               |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_zara_products`                 | 快速读取 Zara 商品数据。需要有效的 Zara 商品 URL。通常更快更可靠。                                              |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_etsy_products`                 | 快速读取 Etsy 商品数据。需要有效的 Etsy 商品 URL。通常更快更可靠。                                              |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_bestbuy_products`              | 快速读取 Best Buy 商品数据。需要有效的商品 URL。通常更快更可靠。                                                |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_linkedin_person_profile`       | 快速读取 LinkedIn 个人资料数据。需要有效的个人资料 URL。通常更快更可靠。                                            |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_linkedin_company_profile`      | 快速读取 LinkedIn 公司资料数据。需要有效的公司 URL。通常更快更可靠。                                              |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_linkedin_job_listings`         | 快速读取 LinkedIn 职位列表数据。需要有效的职位 URL 或搜索 URL。通常更快更可靠。                                      |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_linkedin_posts`                | 快速读取 LinkedIn 帖子数据。需要有效的帖子 URL。通常更快更可靠。                                                |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_linkedin_people_search`        | 快速读取 LinkedIn 人物搜索数据。需要有效的搜索 URL。通常更快更可靠。                                              |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_crunchbase_company`            | 快速读取 Crunchbase 公司数据。需要有效的公司 URL。通常更快更可靠。                                              |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_zoominfo_company_profile`      | 快速读取 ZoomInfo 公司数据。需要有效的公司 URL。通常更快更可靠。                                                |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_instagram_profiles`            | 快速读取 Instagram 个人资料数据。需要有效的资料 URL。通常更快更可靠。                                             |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_instagram_posts`               | 快速读取 Instagram 帖子数据。需要有效的帖子 URL。通常更快更可靠。                                               |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_instagram_reels`               | 快速读取 Instagram Reels 数据。需要有效的 Reels URL。通常更快更可靠。                                       |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_instagram_comments`            | 快速读取 Instagram 评论数据。需要有效的 Instagram URL。通常更快更可靠。                                       |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_facebook_posts`                | 快速读取 Facebook 帖子数据。需要有效的帖子 URL。通常更快更可靠。                                                |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_facebook_marketplace_listings` | 快速读取 Facebook Marketplace 商品列表数据。需要有效的 Marketplace URL。通常更快更可靠。                        |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_facebook_company_reviews`      | 快速读取 Facebook 公司评论数据。需要有效的公司 URL 及评论数量。通常更快更可靠。                                        |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_facebook_events`               | 快速读取 Facebook 活动数据。需要有效的活动 URL。通常更快更可靠。                                                |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_tiktok_profiles`               | 快速读取 TikTok 个人资料数据。需要有效的资料 URL。通常更快更可靠。                                                |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_tiktok_posts`                  | 快速读取 TikTok 帖子数据。需要有效的帖子 URL。通常更快更可靠。                                                  |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_tiktok_shop`                   | 快速读取 TikTok Shop 商品数据。需要有效的商品 URL。通常更快更可靠。                                             |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_tiktok_comments`               | 快速读取 TikTok 评论数据。需要有效的视频 URL。通常更快更可靠。                                                  |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_google_maps_reviews`           | 快速读取 Google Maps 评论数据。需要有效的 Maps URL，可选 days\_limit（默认 3）。通常更快更可靠。                     |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_google_shopping`               | 快速读取 Google Shopping 商品数据。需要有效的商品 URL。通常更快更可靠。                                         |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_google_play_store`             | 快速读取 Google Play Store 应用数据。需要有效的应用 URL。通常更快更可靠。                                       |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_apple_app_store`               | 快速读取 Apple App Store 应用数据。需要有效的应用 URL。通常更快更可靠。                                         |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_github_repository_file`        | 快速读取 GitHub 仓库文件数据。需要有效的文件 URL。通常更快更可靠。                                                |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_yahoo_finance_business`        | 快速读取 Yahoo Finance 公司概况数据。需要有效的公司 URL。通常更快更可靠。                                         |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_x_posts`                       | 快速读取 X（Twitter）帖子数据。需要有效的帖子 URL。通常更快更可靠。                                               |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_zillow_properties_listing`     | 快速读取 Zillow 房产列表数据。需要有效的房源 URL。通常更快更可靠。                                                |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_booking_hotel_listings`        | 快速读取 Booking.com 酒店房源数据。需要有效的房源 URL。通常更快更可靠。                                           |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_youtube_videos`                | 快速读取 YouTube 视频元数据。需要有效的视频 URL。通常更快更可靠。                                                |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_youtube_profiles`              | 快速读取 YouTube 频道资料数据。需要有效的频道 URL。通常更快更可靠。                                               |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_youtube_comments`              | 快速读取 YouTube 评论数据。需要有效的视频 URL 和可选 num\_of\_comments（默认 10）。通常更快更可靠。                    |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `web_data_reddit_posts`                  | 快速读取 Reddit 帖子数据。需要有效的帖子 URL。通常更快更可靠。                                                  |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `scraping_browser_navigate`              | 打开或复用 scraping-browser 会话并导航到提供的 URL，同时重置网络请求记录。                                       |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `scraping_browser_go_back`               | 在 scraping-browser 会话中返回上一页，并报告新 URL 和标题。                                              |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `scraping_browser_go_forward`            | 在 scraping-browser 会话中前进到下一页，并报告新 URL 和标题。                                             |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `scraping_browser_snapshot`              | 捕获当前页面的 ARIA 快照，列出交互元素及其引用，用于后续基于 ref 的操作。                                             |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `scraping_browser_click_ref`             | 使用 ARIA 快照中的 ref 点击元素；需要提供 ref 和可读描述。                                                  |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `scraping_browser_type_ref`              | 填写由 ref 标识的元素，并可选输入完成后按回车提交。                                                           |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `scraping_browser_screenshot`            | 截取当前页面的截图；支持可选 full\_page 模式拍摄完整页面。                                                    |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `scraping_browser_network_requests`      | 列出自页面加载以来记录的所有网络请求，包括 HTTP 方法、URL 和状态码，用于调试。                                           |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `scraping_browser_wait_for_ref`          | 等待由 ARIA ref 标识的元素变为可见，可设置毫秒超时。                                                        |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `scraping_browser_get_text`              | 返回当前页面 body 元素的文本内容。                                                                   |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `scraping_browser_get_html`              | 返回当前页面的 HTML 内容；除非需要 head 或 script 标签，否则避免使用 full\_page。                               |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `scraping_browser_scroll`                | 在 scraping-browser 会话中滚动到页面底部。                                                         |
|  <Icon icon="gem" iconType="duotone" size={20} /> | `scraping_browser_scroll_to_ref`         | 滚动页面直到 ARIA 快照中的引用元素出现在视图中。                                                            |
