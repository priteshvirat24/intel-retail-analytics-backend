> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Pinterest API 抓取工具

## 概览

Pinterest API 套件提供多种 API，每种 API 旨在满足不同的 Pinterest 数据采集需求。以下是这些 API 之间的连接和交互方式概览，基于可用的功能：

<CardGroup cols={1}>
  <Card title="个人资料 API" icon="user" href="/cn/api-reference/scrapers/social-media-apis/pinterest#profiles-api">
    该 API 允许用户根据单个输入（个人资料 URL）收集个人资料详细信息。

    <br />

    *   **发现功能**：

    *   通过关键词发现。

    <br />

    *   **重要字段**：

    *   `name`, `following_count`, `website`, `follower_count`。
  </Card>

  <Card title="帖子 API" icon="images" href="/cn/api-reference/scrapers/social-media-apis/pinterest#posts-api">
    该 API 允许用户基于单个输入收集多个帖子。

    <br />

    *   **发现功能**：

      *   - 通过个人资料 URL 发现。

      *   - 通过关键词发现。

    <br />

    *   **重要字段**：

    *   `title`, `content`, `user_name`, `likes`。
  </Card>
</CardGroup>

## 个人资料 API

### 通过 URL 采集

该 API 允许用户使用提供的个人资料 URL 获取详细的 Pinterest 个人资料信息。

**输入参数**：

<ParamField path="URL" type="string" required="true">
  Pinterest 个人资料 URL。
</ParamField>

**输出结构**：\
包含丰富的数据点：

* **个人资料详情**：\
  `url`, `profile_picture`, `name`, `nickname`, `website`, `bio`, `country_code`, `profile_id`。

  > 查看所有数据点，[点击这里](https://www.bright.cn/cp/scrapers/gd_lk0zv93c2m9qdph46z?tab=overview)。

* **互动与指标**：\
  `following_count`, `follower_count`, `boards_num`, `saved`。

* **附加信息**：\
  `last_updated`, `posts_page_url`, `discovery_input`。

该 API 允许用户收集 Pinterest 个人资料的详细信息，包括用户统计数据、互动指标和个人资料详情。

***

### 通过关键词发现

该 API 允许用户基于指定关键词发现 Pinterest 个人资料。

**输入参数**：

<ParamField path="keyword" type="string" required="true">
  用于搜索个人资料的关键词。
</ParamField>

**输出结构**：\
包含丰富的数据点：

* **个人资料详情**：\
  `url`, `profile_picture`, `name`, `nickname`, `website`, `bio`, `country_code`, `profile_id`。

  > 查看所有数据点，[点击这里](https://www.bright.cn/cp/scrapers/gd_lk0zv93c2m9qdph46z/keyword?tab=overview)。

* **互动与指标**：\
  `following_count`, `follower_count`, `boards_num`, `saved`。

* **附加信息**：\
  `last_updated`, `posts_page_url`, `discovery_input`。

该 API 使用户能够查找与特定关键词相关的 Pinterest 个人资料，提供用户统计数据、互动情况和个人资料详情。

## 帖子 API

### 通过 URL 采集

该 API 允许用户使用提供的帖子 URL 收集特定 Pinterest 帖子的详细数据。

**输入参数**：

<ParamField path="URL" type="string" required="true">
  Pinterest 帖子 URL。
</ParamField>

**输出结构**：\
包含丰富的数据点：

* **帖子详情**：\
  `url`, `post_id`, `title`, `content`, `date_posted`, `post_type`。

  > 查看所有数据点，[点击这里](https://www.bright.cn/cp/scrapers/gd_lk0sjs4d21kdr7cnlv?tab=overview)。

* **用户详情**：\
  `user_name`, `user_url`, `user_id`, `followers`。

* **帖子指标**：\
  `likes`, `comments_num`, `comments`, `categories`。

* **媒体与附件**：\
  `image_video_url`, `video_length`, `attached_files`。

* **标签与发现**：\
  `hashtags`, `discovery_input`。

该 API 允许用户获取特定 Pinterest 帖子的详细信息，包括用户互动、帖子内容、媒体及其他相关信息。

***

### 通过个人资料 URL 发现帖子

该 API 允许用户基于提供的个人资料 URL 获取特定 Pinterest 个人资料下的帖子。

**输入参数**：

<ParamField path="URL" type="string" required="true">
  要采集帖子的 Pinterest 个人资料 URL。
</ParamField>

<ParamField path="num_of_posts" type="number">
  要采集的帖子数量。如果省略，则没有限制。
</ParamField>

<ParamField path="posts_to_not_include" type="array">
  要排除的帖子 ID 数组。
</ParamField>

<ParamField path="start_date" type="string">
  过滤帖子起始日期，格式为 `MM-DD-YYYY`（应早于 `end_date`）。
</ParamField>

<ParamField path="end_date" type="string">
  过滤帖子结束日期，格式为 `MM-DD-YYYY`（应晚于 `start_date`）。
</ParamField>

**输出结构**：\
包含丰富的数据点：

* **帖子详情**：\
  `url`, `post_id`, `title`, `content`, `date_posted`, `user_name`, `user_url`, `user_id`, `followers`, `likes`, `categories`, `source`, `attached_files`, `image_video_url`, `video_length`, `hashtags`, `comments_num`, `comments`, `post_type`。

  > 查看所有数据点，[点击这里](https://www.bright.cn/cp/scrapers/gd_lk0sjs4d21kdr7cnlv/profile_url?tab=overview)。

* **互动与指标**：\
  `followers`, `likes`, `comments_num`。

* **媒体与附件**：\
  `image_video_url`, `video_length`, `attached_files`。

* **附加信息**：\
  `discovery_input`。

该 API 允许用户从特定 Pinterest 个人资料中收集帖子，并支持按日期筛选、排除特定帖子，并获取包含媒体、评论和互动指标的详细帖子数据。

***

### 通过关键词发现帖子

该 API 允许用户基于特定关键词发现 Pinterest 帖子，实现高效的内容发现。

**输入参数**：

<ParamField path="keyword" type="string" required="true">
  用于搜索帖子的关键词，例如 "food" 或其他相关术语。
</ParamField>

**输出结构**：\
包含丰富的数据点：

* **帖子详情**：\
  `url`, `post_id`, `title`, `content`, `date_posted`, `user_name`, `user_url`, `user_id`, `followers`, `likes`, `categories`, `source`, `attached_files`, `image_video_url`, `video_length`, `hashtags`, `comments_num`, `comments`, `post_type`。

  > 查看所有数据点，[点击这里](https://www.bright.cn/cp/scrapers/gd_lk0zv93c2m9qdph46z/keyword?tab=overview)。

* **互动与指标**：\
  `followers`, `likes`, `comments_num`。

* **媒体与附件**：\
  `image_video_url`, `video_length`, `attached_files`。

* **附加信息**：\
  `discovery_input`。

该 API 允许用户基于特定关键词搜索 Pinterest 帖子，并提供详细的内容、互动、媒体及相关指标信息，以实现高效发现。
