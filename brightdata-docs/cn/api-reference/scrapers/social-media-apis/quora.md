> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Quora API 抓取器

## 概览

<CardGroup cols={1}>
  <Card title="Posts API" icon="images" href="/cn/api-reference/scrapers/social-media-apis/quora#posts-api">
    此 API 允许用户基于单个输入 URL 收集多个帖子。

    <br />

    *   **发现功能**：

    *   不适用

    <br />

    *   **重要字段**：

    *   `author_name`，`title`，`over_all_answers`，`shares`。
  </Card>
</CardGroup>

## Posts API

### 通过 URL 采集

此 API 允许用户使用提供的 Quora 帖子 URL，收集该帖子的详细信息。

**输入参数**

<ParamField path="URL" type="string" required="true">
  Quora 帖子的 URL。
</ParamField>

**输出结构**：\
包含全面的数据点：

* **帖子详情**：\
  `url`，`post_id`，`title`，`post_date`，`originally_answered`，`over_all_answers`，`post_text`，`header`。

  > 查看所有数据点，请[点击这里](https://www.bright.cn/cp/scrapers/gd_lvz1rbj81afv3m6n5y?tab=overview)。

* **媒体 & 链接**：\
  `pictures_urls`，`videos_urls`，`external_urls`。

* **互动 & 指标**：\
  `upvotes`，`shares`，`views`，`author_content_views`。

* **作者详情**：\
  `author_name`，`author_active_spaces`，`author_joined_date`，`author_about`，`author_education`。

* **热门评论**：\
  `top_comments`。

此 API 提供对 Quora 帖子的详细见解，包括内容、媒体、作者信息和互动指标，助力高效的帖子分析和内容追踪。
