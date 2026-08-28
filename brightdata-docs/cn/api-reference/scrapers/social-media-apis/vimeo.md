> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Vimeo API 抓取器

## 概览

Vimeo API 套件提供多种 API，每种 API 都专为从 Vimeo 采集特定数据而设计。以下是这些 API 之间的连接和交互概览，基于可用功能：

<CardGroup cols={1}>
  <Card title="Posts API" icon="images" href="/cn/api-reference/scrapers/social-media-apis/vimeo#posts-api">
    此 API 允许用户基于单个输入 URL 采集多个帖子。

    <br />

    *   **发现功能**：

    *   通过个人资料 URL 发现。

    *   通过关键词和许可证发现。

    <br />

    *   **有趣的字段**：

    *   `title`，`video_length`，`views`，`likes`。
  </Card>
</CardGroup>

## Posts API

### 通过 URL 采集

此 API 允许用户使用提供的视频 URL 采集特定 Vimeo 视频的详细信息。

**输入参数**

<ParamField path="URL" type="string" required="true">
  Vimeo 视频的 URL。
</ParamField>

**输出结构**：\
包含全面的数据点：

* **视频详情**\
  `video_id`，`title`，`url`，`video_url`，`video_length`，`description`，`data_posted`，`transcript`。

  > 查看所有数据点，请[点击这里](https://www.bright.cn/cp/scrapers/gd_lxk88z3v1ketji4pn?tab=overview)。

* **互动与指标**\
  `views`，`likes`，`comments`，`collections`。

* **上传者详情**\
  `uploader`，`uploader_url`，`uploader_id`，`avatar_img_uploader`。

* **视频媒体与内容**\
  `preview_image`，`related_videos`，`music_track`。

* **许可证与质量**\
  `license`，`license_info`，`video_quality`。

* **视频尺寸**\
  `height`，`width`。

此 API 提供 Vimeo 视频的详细洞察，包括视频内容、上传者信息、媒体链接、互动指标等，支持高效的视频分析与内容追踪。

### 通过 URL 发现

此 API 允许用户基于特定 URL 和相关关键词发现 Vimeo 视频，并提供详细的视频信息与洞察。

**输入参数**

<ParamField path="URL" type="string" required="true">
  Vimeo 帖子的 URL。
</ParamField>

<ParamField path="keyword" type="string" required="true">
  要在视频内容中搜索的关键词。
</ParamField>

<ParamField path="pages" type="number" required="true">
  要采集的结果页数。
</ParamField>

**输出结构**：\
包含全面的数据点：

* **视频详情**\
  `video_id`，`title`，`url`，`video_url`，`video_length`，`description`，`data_posted`，`transcript`。

  > 查看所有数据点，请[点击这里](https://www.bright.cn/cp/scrapers/gd_lxk88z3v1ketji4pn/url?tab=overview)。

* **互动与指标**\
  `views`，`likes`，`comments`，`collections`。

* **上传者详情**\
  `uploader`，`uploader_url`，`uploader_id`，`avatar_img_uploader`。

* **视频媒体与内容**\
  `preview_image`，`related_videos`，`music_track`。

* **许可证与质量**\
  `license`，`license_info`，`video_quality`。

* **视频尺寸**\
  `height`，`width`。

此 API 允许用户通过 URL 和关键词发现 Vimeo 视频，并提供详细的视频内容、上传者信息和互动指标。

### 通过关键词和许可证发现

此 API 允许用户基于特定关键词和许可证类型发现 Vimeo 视频，并提供详细的视频信息与洞察。

**输入参数**

<ParamField path="keyword" type="string" required="true">
  要在视频内容中搜索的关键词。
</ParamField>

<ParamField path="license" type="string" required="true">
  用于筛选视频的许可证类型（例如：Creative Commons、标准许可证）。
</ParamField>

<ParamField path="pages" type="number" required="true">
  要采集的结果页数。
</ParamField>

**输出结构**：\
包含全面的数据点：

* **视频详情**\
  `video_id`，`title`，`url`，`video_url`，`video_length`，`description`，`data_posted`，`transcript`。

  > 查看所有数据点，请[点击这里](https://www.bright.cn/cp/scrapers/gd_lxk88z3v1ketji4pn/keyword_and_license?tab=overview)。

* **互动与指标**\
  `views`，`likes`，`comments`，`collections`。

* **上传者详情**\
  `uploader`，`uploader_url`，`uploader_id`，`avatar_img_uploader`。

* **视频媒体与内容**\
  `preview_image`，`related_videos`，`music_track`。

* **许可证与质量**\
  `license`，`license_info`，`video_quality`。

* **视频尺寸**\
  `height`，`width`。

此 API 允许用户基于特定关键词和许可证类型发现 Vimeo 视频，并提供详细的视频内容、上传者信息和互动指标。
